"""Pipeline de rédaction IA en 3 étapes (chaining) via l'API Claude.

Le texte du cours est transmis une fois puis mis en cache (prompt caching) ;
chaque étape s'ajoute à la même conversation pour partager le contexte :
  Étape 1 — plan détaillé + déduction du nom du cours
  Étape 2 — rédaction exhaustive, partie par partie (séquentiel)
  Étape 3 — tableaux de synthèse + points à retenir
"""

from __future__ import annotations

import re

from anthropic import AsyncAnthropic

from major_ecn.config import (
    CACHE_READ_MULTIPLIER,
    CACHE_WRITE_MULTIPLIER,
    Settings,
    model_pricing,
)
from major_ecn.models import UsageStats
from major_ecn.prompts import (
    COURSE_CONTEXT,
    STEP1_PLAN,
    STEP2_SECTION,
    STEP3_SYNTHESIS,
    STEP4_EXTRAS,
    SYSTEM_WRITER,
)
from major_ecn.utils.retry import retry_async

# Plafonds de tokens en sortie par étape.
_MAX_TOKENS_PLAN = 3_000
_MAX_TOKENS_SECTION = 8_000
_MAX_TOKENS_SYNTHESIS = 8_000
_MAX_TOKENS_EXTRAS = 5_000

_TAG_BLOCK_RE = re.compile(r"<([a-z_]+)>(.*?)</\1>", re.IGNORECASE | re.DOTALL)


def _extract_tag(raw: str, name: str) -> str:
    """Extrait le contenu texte d'une balise `<name>…</name>`."""
    match = re.search(rf"<{name}>\s*(.*?)\s*</{name}>", raw, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else ""


class AIProcessingError(RuntimeError):
    """Erreur lors d'une étape de rédaction IA."""


class PlanResult:
    """Résultat de l'étape 1 : plan détaillé + nom du cours."""

    def __init__(self, plan_md: str, nom_cours: str, item: str) -> None:
        self.plan_md = plan_md
        self.nom_cours = nom_cours
        self.item = item


class AIProcessor:
    """Conversation IA dédiée à un cours (instance jetable, une par PDF)."""

    def __init__(self, client: AsyncAnthropic, model: str, settings: Settings) -> None:
        self._client = client
        self._model = model
        self._settings = settings
        self._messages: list[dict] = []
        self.usage = UsageStats()
        self._pricing = model_pricing(model)

    # ── Cycle de vie ──────────────────────────────────────────────────────────
    def load_course(self, course_text: str) -> None:
        """Initialise la conversation avec le texte du cours (bloc mis en cache)."""
        truncated = course_text[: self._settings.max_input_chars]
        self._messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": COURSE_CONTEXT.format(course_text=truncated),
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
            }
        ]

    # ── Étapes ────────────────────────────────────────────────────────────────
    async def generate_plan(self) -> PlanResult:
        """Étape 1 — génère le plan détaillé et déduit le nom du cours."""
        raw = await self._exchange(STEP1_PLAN, "étape 1 (plan)", _MAX_TOKENS_PLAN)

        nom_cours = _extract_tag(raw, "nom_cours")
        item = _extract_tag(raw, "item")

        plan_md = _TAG_BLOCK_RE.sub("", raw).strip()
        if not plan_md:
            raise AIProcessingError("Plan vide renvoyé par l'IA.")
        return PlanResult(plan_md=plan_md, nom_cours=nom_cours, item=item)

    async def write_section(self, plan_md: str, numero: str) -> str:
        """Étape 2 — rédige le Markdown (tableaux) d'une grande partie."""
        instruction = STEP2_SECTION.format(plan=plan_md, numero=numero)
        return await self._exchange(
            instruction, f"étape 2 (partie {numero})", _MAX_TOKENS_SECTION
        )

    async def generate_synthesis(self) -> str:
        """Étape 3 — tableaux de synthèse, chiffres-clés et points à retenir."""
        return await self._exchange(
            STEP3_SYNTHESIS, "étape 3 (synthèse)", _MAX_TOKENS_SYNTHESIS
        )

    async def generate_extras(self) -> str:
        """Étape 4 — algorithmes décisionnels et fiche éclair."""
        return await self._exchange(
            STEP4_EXTRAS, "étape 4 (algorithmes & fiche éclair)", _MAX_TOKENS_EXTRAS
        )

    # ── Appel API bas niveau ──────────────────────────────────────────────────
    async def _exchange(self, instruction: str, label: str, max_tokens: int) -> str:
        """Ajoute une instruction, appelle l'API, mémorise la réponse."""
        if not self._messages:
            raise AIProcessingError("Conversation non initialisée (load_course manquant).")

        self._messages.append(
            {"role": "user", "content": [{"type": "text", "text": instruction}]}
        )
        self._apply_cache_breakpoints()

        async def _do_call():
            return await self._client.messages.create(
                model=self._model,
                max_tokens=max_tokens,
                system=SYSTEM_WRITER,
                messages=self._messages,
            )

        try:
            response = await retry_async(_do_call, label=label)
        except Exception as exc:  # noqa: BLE001 — remonte en erreur de traitement
            raise AIProcessingError(f"{label} : appel API échoué ({exc})") from exc

        text = "".join(
            block.text for block in response.content if getattr(block, "type", "") == "text"
        ).strip()
        if not text:
            raise AIProcessingError(f"{label} : réponse IA vide.")

        self._messages.append(
            {"role": "assistant", "content": [{"type": "text", "text": text}]}
        )
        self._track_usage(response.usage)
        return text

    def _apply_cache_breakpoints(self) -> None:
        """Place 2 points de cache : le cours (fixe) et le dernier tour (roulant)."""
        for message in self._messages:
            for block in message["content"]:
                if block is not self._messages[0]["content"][0]:
                    block.pop("cache_control", None)
        # Bloc du cours : toujours mis en cache.
        self._messages[0]["content"][0]["cache_control"] = {"type": "ephemeral"}
        # Dernier bloc : étend le cache au contexte accumulé.
        last_block = self._messages[-1]["content"][-1]
        last_block["cache_control"] = {"type": "ephemeral"}

    def _track_usage(self, usage) -> None:
        """Cumule les tokens et estime le coût USD de l'appel."""
        input_tokens = getattr(usage, "input_tokens", 0) or 0
        output_tokens = getattr(usage, "output_tokens", 0) or 0
        cache_write = getattr(usage, "cache_creation_input_tokens", 0) or 0
        cache_read = getattr(usage, "cache_read_input_tokens", 0) or 0

        in_rate = self._pricing["input"] / 1_000_000
        out_rate = self._pricing["output"] / 1_000_000
        cost = (
            input_tokens * in_rate
            + cache_write * in_rate * CACHE_WRITE_MULTIPLIER
            + cache_read * in_rate * CACHE_READ_MULTIPLIER
            + output_tokens * out_rate
        )
        self.usage.add(
            UsageStats(
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                cache_write_tokens=cache_write,
                cache_read_tokens=cache_read,
                cost_usd=cost,
            )
        )

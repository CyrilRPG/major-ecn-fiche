"""Analyse des images par Claude Vision : scoring de pertinence pédagogique.

Chaque image extraite du PDF est envoyée au modèle vision qui en produit une
description, un concept lié et une note 0-10. Seules les images notées ≥ 6
sont conservées pour la fiche (filtrage effectué en aval).
"""

from __future__ import annotations

import asyncio
import base64
import io
import json

from anthropic import AsyncAnthropic

from major_ecn.config import Settings, model_pricing
from major_ecn.models import AnalyzedImage, ExtractedImage, UsageStats
from major_ecn.prompts import SYSTEM_VISION, VISION_IMAGE
from major_ecn.utils.logger import get_logger
from major_ecn.utils.retry import retry_async

# Formats directement acceptés par l'API vision Anthropic.
_API_IMAGE_FORMATS = {"png", "jpeg", "jpg", "gif", "webp"}
_MAX_IMAGE_EDGE_PX = 1400  # Redimensionnement pour limiter coût et latence
_VISION_CONCURRENCY = 4    # Appels vision simultanés par cours


def _prepare_image(image: ExtractedImage) -> tuple[str, str] | None:
    """Prépare une image pour l'API : format supporté, taille raisonnable.

    Renvoie `(base64, media_type)` ou `None` si l'image est inexploitable.
    """
    try:
        from PIL import Image  # type: ignore
    except ImportError:
        ext = image.ext.lower()
        if ext in _API_IMAGE_FORMATS:
            media = "image/jpeg" if ext == "jpg" else f"image/{ext}"
            return base64.b64encode(image.data).decode("ascii"), media
        return None

    try:
        with Image.open(io.BytesIO(image.data)) as pil_image:
            pil_image = pil_image.convert("RGB")
            longest = max(pil_image.size)
            if longest > _MAX_IMAGE_EDGE_PX:
                ratio = _MAX_IMAGE_EDGE_PX / longest
                new_size = (round(pil_image.width * ratio), round(pil_image.height * ratio))
                pil_image = pil_image.resize(new_size, Image.LANCZOS)
            buffer = io.BytesIO()
            pil_image.save(buffer, format="JPEG", quality=85)
            return base64.b64encode(buffer.getvalue()).decode("ascii"), "image/jpeg"
    except Exception:  # noqa: BLE001 — image corrompue
        return None


def _parse_vision_json(raw: str) -> dict:
    """Extrait le JSON d'une réponse vision, tolérant aux blocs de code."""
    text = raw.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:]
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end == -1:
        return {}
    try:
        parsed = json.loads(text[start : end + 1])
        return parsed if isinstance(parsed, dict) else {}
    except json.JSONDecodeError:
        return {}


def _clamp_score(value: object) -> int:
    """Normalise une note de pertinence en entier borné 0-10."""
    try:
        return max(0, min(10, int(round(float(value)))))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


class ImageAnalyzer:
    """Analyse vision d'un lot d'images via Claude Sonnet."""

    def __init__(self, client: AsyncAnthropic, model: str, settings: Settings) -> None:
        self._client = client
        self._model = model
        self._settings = settings
        self._pricing = model_pricing(model)
        self.usage = UsageStats()

    async def analyze_images(
        self, images: list[ExtractedImage], matiere: str, nom_cours: str
    ) -> list[AnalyzedImage]:
        """Analyse toutes les images (en parallèle) et renvoie les résultats."""
        candidates = [img for img in images if not img.is_decorative_size]
        candidates = candidates[: self._settings.max_images]
        if not candidates:
            return []

        semaphore = asyncio.Semaphore(_VISION_CONCURRENCY)

        async def _bounded(img: ExtractedImage) -> AnalyzedImage:
            async with semaphore:
                return await self._analyze_one(img, matiere, nom_cours)

        results = await asyncio.gather(*(_bounded(img) for img in candidates))
        kept = sum(1 for r in results if r.is_relevant)
        get_logger().debug(
            "Vision : %d images analysées, %d retenues (≥ seuil).", len(results), kept
        )
        return list(results)

    async def _analyze_one(
        self, image: ExtractedImage, matiere: str, nom_cours: str
    ) -> AnalyzedImage:
        """Analyse une image isolée ; renvoie une note 0 en cas d'échec."""
        prepared = _prepare_image(image)
        if prepared is None:
            return AnalyzedImage(source=image, description="(image illisible)")

        b64, media_type = prepared
        prompt = VISION_IMAGE.format(matiere=matiere, nom_cours=nom_cours)

        async def _do_call():
            return await self._client.messages.create(
                model=self._model,
                max_tokens=400,
                system=SYSTEM_VISION,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": media_type,
                                    "data": b64,
                                },
                            },
                            {"type": "text", "text": prompt},
                        ],
                    }
                ],
            )

        try:
            response = await retry_async(_do_call, label="analyse vision")
        except Exception as exc:  # noqa: BLE001 — image ignorée si vision échoue
            get_logger().warning("[yellow]Analyse vision échouée (%s).[/yellow]", exc)
            return AnalyzedImage(source=image, description="(analyse indisponible)")

        self._track_usage(response.usage)
        raw = "".join(
            block.text for block in response.content if getattr(block, "type", "") == "text"
        )
        data = _parse_vision_json(raw)

        return AnalyzedImage(
            source=image,
            description=str(data.get("description", "")).strip(),
            concept_lie=str(data.get("concept_lie", "")).strip(),
            pertinence=_clamp_score(data.get("pertinence_pedagogique", 0)),
            type=str(data.get("type", "autre")).strip() or "autre",
            section_suggeree=str(data.get("section_suggeree", "")).strip(),
        )

    def _track_usage(self, usage) -> None:
        """Cumule tokens et coût estimé d'un appel vision."""
        input_tokens = getattr(usage, "input_tokens", 0) or 0
        output_tokens = getattr(usage, "output_tokens", 0) or 0
        in_rate = self._pricing["input"] / 1_000_000
        out_rate = self._pricing["output"] / 1_000_000
        self.usage.add(
            UsageStats(
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                cost_usd=input_tokens * in_rate + output_tokens * out_rate,
            )
        )

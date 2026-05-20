"""Tests du pipeline IA (avec un client Anthropic factice)."""

from __future__ import annotations

import asyncio

from major_ecn.ai_processor import AIProcessor
from major_ecn.config import Settings


# ── Faux client Anthropic ─────────────────────────────────────────────────────
class _FakeBlock:
    def __init__(self, text: str) -> None:
        self.type = "text"
        self.text = text


class _FakeUsage:
    input_tokens = 1_000
    output_tokens = 400
    cache_creation_input_tokens = 200
    cache_read_input_tokens = 800


class _FakeResponse:
    def __init__(self, text: str) -> None:
        self.content = [_FakeBlock(text)]
        self.usage = _FakeUsage()


class _FakeMessages:
    def __init__(self, replies: list[str]) -> None:
        self._replies = list(replies)
        self.calls: list[dict] = []

    async def create(self, **kwargs) -> _FakeResponse:
        self.calls.append(kwargs)
        return _FakeResponse(self._replies.pop(0))


class _FakeClient:
    def __init__(self, replies: list[str]) -> None:
        self.messages = _FakeMessages(replies)


def _processor(replies: list[str]) -> AIProcessor:
    processor = AIProcessor(_FakeClient(replies), "claude-opus-4-5", Settings())
    processor.load_course("Contenu du cours de cardiologie. " * 50)
    return processor


# ── Tests ─────────────────────────────────────────────────────────────────────
def test_load_course_sets_cache_control() -> None:
    processor = _processor([])
    block = processor._messages[0]["content"][0]
    assert block["cache_control"] == {"type": "ephemeral"}


def test_load_course_truncates() -> None:
    settings = Settings(max_input_chars=100)
    processor = AIProcessor(_FakeClient([]), "claude-opus-4-5", settings)
    processor.load_course("x" * 5_000)
    assert len(processor._messages[0]["content"][0]["text"]) < 400


def test_generate_plan_extracts_tags() -> None:
    reply = (
        "I. **Définition** : Cadre.\n   A. **Seuils** : Critères.\n"
        "<nom_cours>Hypertension Artérielle</nom_cours>\n<item>Item 224</item>"
    )
    processor = _processor([reply])
    result = asyncio.run(processor.generate_plan())
    assert result.nom_cours == "Hypertension Artérielle"
    assert result.item == "Item 224"
    assert "<nom_cours>" not in result.plan_md
    assert "Définition" in result.plan_md


def test_write_section_returns_markdown() -> None:
    reply = (
        "I. **Définition**\n\nA. **Seuils**\n"
        "[LIGNE] ★ Définition\n- **HTA** : PA élevée"
    )
    processor = _processor([reply])
    result = asyncio.run(processor.write_section("plan factice", "I"))
    assert isinstance(result, str)
    assert "[LIGNE]" in result
    assert "★" in result


def test_usage_tracking_accumulates_cost() -> None:
    reply = "I. **A**\n<nom_cours>Test</nom_cours>"
    processor = _processor([reply])
    asyncio.run(processor.generate_plan())
    assert processor.usage.input_tokens == 1_000
    assert processor.usage.output_tokens == 400
    assert processor.usage.cost_usd > 0


def test_synthesis_call_uses_conversation() -> None:
    processor = _processor(["I. **A**\n<nom_cours>T</nom_cours>", "### Tableau\n| a | b |"])
    asyncio.run(processor.generate_plan())
    synthesis = asyncio.run(processor.generate_synthesis())
    assert "Tableau" in synthesis
    # 2 appels API, conversation cumulée (cours + 2 tours user + 2 réponses).
    assert len(processor._messages) == 5

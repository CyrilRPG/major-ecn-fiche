"""Tests des utilitaires : slugify, retry, configuration."""

from __future__ import annotations

import asyncio

import pytest

from major_ecn.config import Settings, model_pricing
from major_ecn.utils.retry import retry_async
from major_ecn.utils.slugify import slugify, strip_accents, titlecase_fr


def test_strip_accents() -> None:
    assert strip_accents("Hépato-Gastro") == "Hepato-Gastro"
    assert strip_accents("Œdème aigu") == "Œdeme aigu"


def test_slugify_basic() -> None:
    assert slugify("Hypertension Artérielle") == "Hypertension-Arterielle"
    assert slugify("Œdème aigu du poumon (OAP)") == "deme-aigu-du-poumon-OAP"
    assert slugify("") == "Sans-Titre"


def test_slugify_separator_collapse() -> None:
    assert slugify("A  ---  B") == "A-B"
    assert slugify("Cardiologie/Pneumologie") == "Cardiologie-Pneumologie"


def test_titlecase_fr() -> None:
    assert titlecase_fr("hypertension arterielle") == "Hypertension Arterielle"
    assert titlecase_fr("infarctus du myocarde") == "Infarctus du Myocarde"


def test_model_pricing_fallback() -> None:
    assert model_pricing("claude-opus-4-5")["input"] == 5.0
    assert model_pricing("modele-inconnu")["input"] > 0


def test_settings_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("MAJOR_ECN_CONCURRENCY", raising=False)
    monkeypatch.setenv("MAJOR_ECN_YEAR", "2026-2027")
    settings = Settings.load()
    assert settings.year == "2026-2027"
    assert 1 <= settings.concurrency <= 8


def test_settings_concurrency_clamped(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("MAJOR_ECN_CONCURRENCY", "999")
    assert Settings.load().concurrency == 8


def test_retry_async_succeeds_after_transient() -> None:
    calls = {"n": 0}

    async def flaky() -> str:
        calls["n"] += 1
        if calls["n"] < 2:
            raise TimeoutError("transient")
        return "ok"

    result = asyncio.run(retry_async(flaky, attempts=2, base_delay=0.01))
    assert result == "ok"
    assert calls["n"] == 2


def test_retry_async_reraises_non_transient() -> None:
    async def boom() -> None:
        raise ValueError("permanent")

    with pytest.raises(ValueError):
        asyncio.run(retry_async(boom, attempts=3, base_delay=0.01))

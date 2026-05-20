"""Slugification de noms de cours pour des noms de fichiers propres et stables."""

from __future__ import annotations

import re
import unicodedata

# Capitalisation : mots courts laissés en minuscule sauf en tête de chaîne.
_SMALL_WORDS = {"de", "des", "du", "la", "le", "les", "et", "a", "au", "aux", "en", "sur"}


def strip_accents(text: str) -> str:
    """Supprime les diacritiques (é → e, ç → c) sans toucher au reste."""
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch))


def slugify(text: str, *, separator: str = "-") -> str:
    """Transforme un libellé en segment de nom de fichier.

    Exemple : « Hypertension Artérielle (HTA) » → « Hypertension-Arterielle-HTA ».
    """
    cleaned = strip_accents(text).strip()
    cleaned = re.sub(r"[’'`]", "", cleaned)
    cleaned = re.sub(r"[^A-Za-z0-9]+", separator, cleaned)
    cleaned = re.sub(rf"{re.escape(separator)}+", separator, cleaned)
    return cleaned.strip(separator) or "Sans-Titre"


def titlecase_fr(text: str) -> str:
    """Met en casse de titre « à la française » (mots de liaison en minuscule)."""
    words = re.split(r"(\s+)", strip_accents(text).strip() or text.strip())
    result: list[str] = []
    seen_word = False
    for token in words:
        if token.isspace() or not token:
            result.append(token)
            continue
        lowered = token.lower()
        if seen_word and lowered in _SMALL_WORDS:
            result.append(lowered)
        else:
            result.append(token[:1].upper() + token[1:].lower())
        seen_word = True
    return "".join(result)

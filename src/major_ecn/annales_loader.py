"""Chargement et extraction des notions des annales EVC médecine générale.

Fournit la liste des thèmes/notions tombés aux EVC de médecine générale
(code 71) pour le placement correct des marqueurs ★.

Usage :
    from major_ecn.annales_loader import load_mg_annales_text, extract_mg_themes

    text = load_mg_annales_text()        # Texte brut combiné des annales
    themes = extract_mg_themes()         # Set de thèmes/mots-clés identifiés
"""

from __future__ import annotations

import re
from pathlib import Path

from major_ecn.config import PROJECT_ROOT

_ANNALES_DIR = PROJECT_ROOT / "Annales"
_CACHE_FILE = PROJECT_ROOT / "output" / ".annales_txt" / "medecine_generale_combined.txt"

# Code spécialité médecine générale dans la nomenclature EVC
MG_CODE = "71"


def _extract_doc_text(doc_path: Path) -> str:
    """Extrait le texte d'un fichier .DOC Word 97 (lecture binaire brute)."""
    raw = doc_path.read_bytes()
    text = raw.decode("latin-1", errors="replace")

    # Chercher le début du contenu textuel
    for marker in ("MEDECINE", "Question", "Sujet"):
        idx = text.find(marker)
        if idx > 0:
            text = text[idx:]
            break

    # Nettoyer les caractères non imprimables
    clean = "".join(c if (c.isprintable() or c in "\n\r\t") else " " for c in text)
    clean = re.sub(r" {2,}", " ", clean)
    clean = re.sub(r"\n{2,}", "\n", clean)
    return clean.strip()


def load_mg_annales_text() -> str:
    """Charge et combine le texte de toutes les annales EVC médecine générale.

    Utilise un cache sur disque pour éviter de re-parser les .DOC à chaque appel.
    """
    if _CACHE_FILE.exists():
        return _CACHE_FILE.read_text(encoding="utf-8")

    annales_files = list(_ANNALES_DIR.rglob(f"*.{MG_CODE}.*"))
    if not annales_files:
        return ""

    parts: list[str] = []
    for f in sorted(annales_files):
        text = _extract_doc_text(f)
        if len(text) > 100:
            # Identifier l'année
            year = "unknown"
            for y in ("2009", "2010", "2011", "2012", "2013",
                      "2015", "2016", "2017", "2018", "2019"):
                if y in str(f):
                    year = y
                    break
            parts.append(f"=== {f.name} ({year}) ===\n{text}")

    combined = "\n\n".join(parts)

    # Persister le cache
    _CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    _CACHE_FILE.write_text(combined, encoding="utf-8")

    return combined


def extract_mg_themes() -> set[str]:
    """Extrait un ensemble de thèmes/mots-clés médicaux des annales MG.

    Retourne un set de termes normalisés (minuscules, sans accents simplifiés)
    qui permettent de vérifier si une notion a été abordée aux EVC MG.
    """
    text = load_mg_annales_text()
    if not text:
        return set()

    # Extraction de termes médicaux significatifs (> 5 caractères)
    words = re.findall(r"[A-ZÀ-Ÿa-zà-ÿ]{5,}", text)
    # Normaliser en minuscules
    themes = {w.lower() for w in words if len(w) >= 5}

    # Ajouter des expressions composées fréquentes
    bigrams = re.findall(
        r"([A-ZÀ-Ÿa-zà-ÿ]{3,})\s+([A-ZÀ-Ÿa-zà-ÿ]{3,})", text
    )
    for a, b in bigrams:
        expr = f"{a.lower()} {b.lower()}"
        if len(expr) > 8:
            themes.add(expr)

    return themes


def is_notion_in_mg_annales(notion: str, themes: set[str] | None = None) -> bool:
    """Vérifie si une notion médicale apparaît dans les annales MG.

    Args:
        notion: Le concept à vérifier (ex: "HTA", "diabète type 2")
        themes: Set pré-chargé (pour éviter de recharger à chaque appel)

    Returns:
        True si la notion semble apparaître dans les annales MG.
    """
    if themes is None:
        themes = extract_mg_themes()

    notion_lower = notion.lower().strip()

    # Vérification directe
    if notion_lower in themes:
        return True

    # Vérification par mots individuels (au moins 2 mots sur 3 doivent matcher)
    words = [w for w in notion_lower.split() if len(w) >= 4]
    if not words:
        return False

    matches = sum(1 for w in words if w in themes)
    return matches >= max(1, len(words) // 2)

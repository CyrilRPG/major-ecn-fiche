"""Configuration centrale du générateur de fiches Major ECN.

Regroupe la charte graphique « luxe médical », les modèles IA, les chemins
du projet et les paramètres lus depuis l'environnement (`.env`).
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

# ── Chemins du projet ─────────────────────────────────────────────────────────
PACKAGE_ROOT: Path = Path(__file__).resolve().parent
PROJECT_ROOT: Path = PACKAGE_ROOT.parent.parent
ASSETS_DIR: Path = PROJECT_ROOT / "assets"
FONTS_DIR: Path = ASSETS_DIR / "fonts"
TEMPLATES_DIR: Path = ASSETS_DIR / "templates"
LOGS_DIR: Path = PROJECT_ROOT / "logs"
LOGO_PATH: Path = ASSETS_DIR / "logo_major_ecn.png"

# ── Charte graphique « luxe médical » ─────────────────────────────────────────
COLOR_RED = "#E11D48"        # Rouge signature
COLOR_GOLD = "#C9A961"       # Or accent
COLOR_CREAM = "#FAF7F2"      # Crème fond
COLOR_ANTHRACITE = "#1F2937"  # Gris anthracite (corps de texte)
COLOR_PEARL = "#9CA3AF"      # Gris perle (texte secondaire)
COLOR_OFFWHITE = "#FFFEFB"   # Blanc cassé (fond de page)
COLOR_RED_PALE = "#FEE2E2"   # Rouge très pâle (encadrés pièges)


@dataclass(frozen=True)
class Palette:
    """Palette de couleurs exposée aux générateurs (PDF, DOCX, HTML)."""

    red: str = COLOR_RED
    gold: str = COLOR_GOLD
    cream: str = COLOR_CREAM
    anthracite: str = COLOR_ANTHRACITE
    pearl: str = COLOR_PEARL
    offwhite: str = COLOR_OFFWHITE
    red_pale: str = COLOR_RED_PALE


PALETTE = Palette()

# ── Typographie ───────────────────────────────────────────────────────────────
FONT_TITLE = "Playfair Display"      # Titres / page de garde
FONT_SUBTITLE = "Cormorant Garamond"  # Sous-titres
FONT_BODY = "Inter"                   # Corps de texte
FONT_MONO = "JetBrains Mono"          # Valeurs chiffrées

FONT_TITLE_FALLBACK = "Times New Roman"
FONT_BODY_FALLBACK = "Helvetica"

# ── Modèles IA (valeurs par défaut, surchargées par l'environnement) ──────────
DEFAULT_WRITER_MODEL = "claude-opus-4-5"   # Rédaction (étapes 1-2-3)
DEFAULT_VISION_MODEL = "claude-sonnet-4-5"  # Analyse d'images (vision)

# Tarifs API approximatifs en USD par million de tokens (estimation des coûts).
# Ajustez-les si la grille tarifaire Anthropic évolue.
MODEL_PRICING: dict[str, dict[str, float]] = {
    "claude-opus-4-5": {"input": 5.0, "output": 25.0},
    "claude-sonnet-4-5": {"input": 3.0, "output": 15.0},
}
DEFAULT_PRICING = {"input": 5.0, "output": 25.0}
CACHE_WRITE_MULTIPLIER = 1.25  # Écriture de cache : 1.25× le tarif input
CACHE_READ_MULTIPLIER = 0.1    # Lecture de cache : 0.1× le tarif input

# ── Légende des marqueurs de fiche ────────────────────────────────────────────
@dataclass(frozen=True)
class LegendEntry:
    """Entrée de légende : un marqueur inséré dans le contenu + sa signification."""

    symbol: str
    label: str
    description: str


# Marqueurs insérés par l'IA dans le contenu et expliqués sur la page de garde.
# ★ est imposé (notion déjà tombée) ; ◆ et ⚠ sont deux propositions à évaluer.
FICHE_LEGEND: tuple[LegendEntry, ...] = (
    LegendEntry("★", "Déjà tombé aux ECN",
                "Notion déjà posée lors d'une épreuve classante nationale."),
    LegendEntry("◆", "Notion à haut rendement",
                "Point à fort enjeu, statistiquement très rentable — à maîtriser en priorité."),
    LegendEntry("⚠", "Piège classique",
                "Erreur fréquemment commise ou confusion à éviter — vigilance requise."),
)

# ── Catégories sémantiques des sous-parties ───────────────────────────────────
@dataclass(frozen=True)
class Category:
    """Catégorie sémantique d'une sous-partie (code couleur + libellé)."""

    key: str
    label: str
    color: str


CATEGORIES: dict[str, Category] = {
    "generalites": Category("generalites", "Généralités", "#64748B"),
    "physiopathologie": Category("physiopathologie", "Physiopathologie", "#0F766E"),
    "clinique": Category("clinique", "Clinique", "#B45309"),
    "paraclinique": Category("paraclinique", "Diagnostic & examens", "#1D4ED8"),
    "traitement": Category("traitement", "Prise en charge", "#15803D"),
    "suivi": Category("suivi", "Pronostic & suivi", "#7E22CE"),
}
DEFAULT_CATEGORY = "generalites"

# ── Lignes-réflexe intégrées aux tableaux (libellé + couleur) ─────────────────
REFLEXE_TYPES: dict[str, tuple[str, str]] = {
    "a_retenir": ("À retenir", "#E11D48"),
    "piege": ("Piège", "#B91C1C"),
    "mnemo": ("Moyen mnémotechnique", "#9A7B33"),
}

# ── Paramètres métier ─────────────────────────────────────────────────────────
DEFAULT_YEAR = "2025-2026"
IMAGE_RELEVANCE_THRESHOLD = 6  # Note minimale de pertinence pédagogique (0-10)
MIN_IMAGE_DIMENSION_PX = 90    # En dessous : image considérée décorative (icône)
SCANNED_TEXT_THRESHOLD = 120   # Caractères par page en dessous desquels on tente l'OCR
READING_SPEED_WPM = 170        # Mots/minute pour estimer la durée de lecture


@dataclass
class Settings:
    """Paramètres d'exécution résolus depuis l'environnement et la CLI."""

    anthropic_api_key: str = ""
    writer_model: str = DEFAULT_WRITER_MODEL
    vision_model: str = DEFAULT_VISION_MODEL
    year: str = DEFAULT_YEAR
    concurrency: int = 4
    max_input_chars: int = 140_000
    max_images: int = 40

    @classmethod
    def load(cls, env_file: Path | None = None) -> "Settings":
        """Charge les paramètres depuis le fichier `.env` puis l'environnement."""
        load_dotenv(dotenv_path=env_file, override=False)

        def _int(name: str, default: int) -> int:
            raw = os.environ.get(name, "").strip()
            try:
                return int(raw) if raw else default
            except ValueError:
                return default

        return cls(
            anthropic_api_key=os.environ.get("ANTHROPIC_API_KEY", "").strip(),
            writer_model=os.environ.get("MAJOR_ECN_WRITER_MODEL", DEFAULT_WRITER_MODEL).strip()
            or DEFAULT_WRITER_MODEL,
            vision_model=os.environ.get("MAJOR_ECN_VISION_MODEL", DEFAULT_VISION_MODEL).strip()
            or DEFAULT_VISION_MODEL,
            year=os.environ.get("MAJOR_ECN_YEAR", DEFAULT_YEAR).strip() or DEFAULT_YEAR,
            concurrency=max(1, min(_int("MAJOR_ECN_CONCURRENCY", 4), 8)),
            max_input_chars=_int("MAJOR_ECN_MAX_INPUT_CHARS", 140_000),
            max_images=_int("MAJOR_ECN_MAX_IMAGES", 40),
        )


def model_pricing(model: str) -> dict[str, float]:
    """Renvoie la grille tarifaire (USD / MTok) d'un modèle, avec repli générique."""
    for key, pricing in MODEL_PRICING.items():
        if model.startswith(key):
            return pricing
    return DEFAULT_PRICING

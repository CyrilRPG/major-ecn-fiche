"""Modèles de données partagés par tout le pipeline.

Une `FicheData` est la représentation structurée et complète d'une fiche,
indépendante du format de sortie (HTML, PDF, DOCX).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

# Types d'encadrés spéciaux reconnus (voir prompt étape 2).
ENCADRE_TYPES = {"a_retenir", "piege_ecn", "mots_cles_tombes", "mnemo"}

ENCADRE_LABELS: dict[str, str] = {
    "a_retenir": "À retenir",
    "piege_ecn": "Piège ECN",
    "mots_cles_tombes": "Mots-clés tombés",
    "mnemo": "Astuce mnémotechnique",
}

ENCADRE_ICONS: dict[str, str] = {
    "a_retenir": "🎯",
    "piege_ecn": "⚠️",
    "mots_cles_tombes": "🔑",
    "mnemo": "💡",
}


@dataclass
class ExtractedImage:
    """Image brute extraite d'un PDF source."""

    data: bytes
    ext: str
    page: int
    index: int
    width: int
    height: int
    sha: str

    @property
    def is_decorative_size(self) -> bool:
        """Vrai si l'image est trop petite pour être pédagogiquement utile."""
        from major_ecn.config import MIN_IMAGE_DIMENSION_PX

        return self.width < MIN_IMAGE_DIMENSION_PX or self.height < MIN_IMAGE_DIMENSION_PX


@dataclass
class ExtractedDocument:
    """Résultat de l'extraction d'un PDF : texte intégral + images."""

    text: str
    images: list[ExtractedImage] = field(default_factory=list)
    page_count: int = 0
    used_ocr: bool = False


@dataclass
class AnalyzedImage:
    """Image enrichie par l'analyse vision (scoring pédagogique)."""

    source: ExtractedImage
    description: str = ""
    concept_lie: str = ""
    pertinence: int = 0
    type: str = "autre"
    section_suggeree: str = ""
    saved_path: Path | None = None
    figure_number: int = 0

    @property
    def is_relevant(self) -> bool:
        """Vrai si l'image dépasse le seuil de pertinence pédagogique."""
        from major_ecn.config import IMAGE_RELEVANCE_THRESHOLD

        return self.pertinence >= IMAGE_RELEVANCE_THRESHOLD


@dataclass
class Encadre:
    """Encadré spécial inséré dans une section."""

    type: str
    titre: str
    contenu: str


@dataclass
class PlanSousPartie:
    """Sous-partie du plan (page sommaire)."""

    lettre: str
    titre: str
    resume: str = ""


@dataclass
class PlanPartie:
    """Grande partie du plan (page sommaire)."""

    numero: str  # Chiffre romain (I, II, III…)
    titre: str
    resume: str = ""
    sous_parties: list[PlanSousPartie] = field(default_factory=list)


@dataclass
class SousPartie:
    """Sous-partie rédigée du corps de la fiche."""

    lettre: str
    titre: str
    corps_md: str = ""
    images: list[AnalyzedImage] = field(default_factory=list)


@dataclass
class Partie:
    """Grande partie rédigée du corps de la fiche."""

    numero: str
    titre: str
    intro_md: str = ""
    sous_parties: list[SousPartie] = field(default_factory=list)
    encadres: list[Encadre] = field(default_factory=list)


@dataclass
class TableauSynthese:
    """Tableau de synthèse final (Markdown)."""

    titre: str
    markdown: str


@dataclass
class UsageStats:
    """Comptage de tokens et coût estimé d'un ou plusieurs appels API."""

    input_tokens: int = 0
    output_tokens: int = 0
    cache_write_tokens: int = 0
    cache_read_tokens: int = 0
    cost_usd: float = 0.0

    def add(self, other: "UsageStats") -> None:
        """Cumule les statistiques d'un autre relevé."""
        self.input_tokens += other.input_tokens
        self.output_tokens += other.output_tokens
        self.cache_write_tokens += other.cache_write_tokens
        self.cache_read_tokens += other.cache_read_tokens
        self.cost_usd += other.cost_usd


@dataclass
class FicheData:
    """Représentation complète et structurée d'une fiche Major ECN."""

    matiere: str
    nom_cours: str
    annee: str
    item: str = ""
    plan: list[PlanPartie] = field(default_factory=list)
    parties: list[Partie] = field(default_factory=list)
    tableaux: list[TableauSynthese] = field(default_factory=list)
    points_cles: list[str] = field(default_factory=list)
    images: list[AnalyzedImage] = field(default_factory=list)
    fiche_numero: str = ""
    usage: UsageStats = field(default_factory=UsageStats)

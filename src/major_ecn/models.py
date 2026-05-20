"""Modèles de données partagés par tout le pipeline.

Une `FicheData` est la représentation structurée et complète d'une fiche,
indépendante du format de sortie (HTML, PDF, DOCX).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


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
class FicheRow:
    """Ligne de tableau de fiche.

    `kind` vaut « normal » (concept | détail) ou un type de ligne-réflexe
    (« a_retenir », « piege », « mnemo ») rendue pleine largeur.
    """

    concept: str
    detail_md: str = ""
    kind: str = "normal"


@dataclass
class SousPartie:
    """Sous-partie du corps, rendue sous forme de tableau structuré."""

    lettre: str
    titre: str
    rows: list[FicheRow] = field(default_factory=list)
    images: list[AnalyzedImage] = field(default_factory=list)


@dataclass
class Partie:
    """Grande partie rédigée du corps de la fiche."""

    numero: str
    titre: str
    sous_parties: list[SousPartie] = field(default_factory=list)


@dataclass
class TableauSynthese:
    """Tableau de synthèse (Markdown)."""

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
    chiffres_cles: TableauSynthese | None = None
    points_cles: list[str] = field(default_factory=list)
    fiche_eclair_md: str = ""
    images: list[AnalyzedImage] = field(default_factory=list)
    fiche_numero: str = ""
    usage: UsageStats = field(default_factory=UsageStats)

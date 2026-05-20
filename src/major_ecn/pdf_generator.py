"""Génération du PDF final : HTML stylé → PDF via WeasyPrint."""

from __future__ import annotations

from pathlib import Path

from major_ecn.config import ASSETS_DIR
from major_ecn.html_renderer import render_fiche_html
from major_ecn.models import FicheData


class PDFGenerationError(RuntimeError):
    """Erreur lors du rendu PDF."""


def render_pdf(fiche: FicheData, output_path: Path) -> Path:
    """Génère le PDF d'une fiche et l'écrit sur disque.

    `base_url` pointe sur le dossier `assets/` pour résoudre les polices
    référencées en chemin relatif dans la feuille de style.
    """
    try:
        from weasyprint import HTML  # Import différé : dépendances système lourdes
    except OSError as exc:  # pragma: no cover — Pango/Cairo manquants
        raise PDFGenerationError(
            f"WeasyPrint indisponible — bibliothèques système manquantes ({exc})."
        ) from exc

    html_content = render_fiche_html(fiche)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        HTML(string=html_content, base_url=str(ASSETS_DIR)).write_pdf(str(output_path))
    except Exception as exc:  # noqa: BLE001 — remonté en erreur de génération
        raise PDFGenerationError(f"Échec du rendu PDF ({exc})") from exc

    return output_path

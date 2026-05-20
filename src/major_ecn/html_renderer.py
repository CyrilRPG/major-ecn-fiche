"""Rendu HTML d'une `FicheData` via Jinja2 et conversion Markdown.

Produit un document HTML autonome (CSS inliné) prêt à être converti en PDF
par WeasyPrint, en appliquant la charte « luxe médical ».
"""

from __future__ import annotations

from pathlib import Path

import markdown as md_lib
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

from major_ecn.config import LOGO_PATH, PALETTE, TEMPLATES_DIR
from major_ecn.models import ENCADRE_ICONS, ENCADRE_LABELS, FicheData

# Extensions Markdown : tableaux + listes imbriquées fiables.
_MD_EXTENSIONS = ["tables", "sane_lists"]


def _markdown_converter() -> md_lib.Markdown:
    """Crée un convertisseur Markdown réutilisable (réinitialisé à chaque appel)."""
    return md_lib.Markdown(extensions=_MD_EXTENSIONS, output_format="html")


def render_markdown(text: str) -> Markup:
    """Convertit du Markdown en HTML sûr (bloc complet)."""
    if not text or not text.strip():
        return Markup("")
    converter = _markdown_converter()
    return Markup(converter.convert(text))


def render_markdown_inline(text: str) -> Markup:
    """Convertit du Markdown court en HTML sans paragraphe enveloppant."""
    html = str(render_markdown(text)).strip()
    if html.startswith("<p>") and html.endswith("</p>"):
        html = html[3:-4]
    return Markup(html)


def _file_uri(path: Path | str | None) -> str:
    """Convertit un chemin en URI `file://` absolue (vide si introuvable)."""
    if path is None:
        return ""
    path = Path(path)
    return path.resolve().as_uri() if path.exists() else ""


def _build_environment() -> Environment:
    """Construit l'environnement Jinja2 avec les filtres de la fiche."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["md"] = render_markdown
    env.filters["md_inline"] = render_markdown_inline
    env.filters["file_uri"] = _file_uri
    return env


def render_fiche_html(fiche: FicheData) -> str:
    """Rend la fiche complète en HTML autonome (CSS inliné)."""
    env = _build_environment()
    css_content = (TEMPLATES_DIR / "styles.css").read_text(encoding="utf-8")

    template = env.get_template("fiche.html")
    return template.render(
        fiche=fiche,
        css=css_content,
        palette=PALETTE,
        logo_uri=_file_uri(LOGO_PATH),
        encadre_labels=ENCADRE_LABELS,
        encadre_icons=ENCADRE_ICONS,
    )

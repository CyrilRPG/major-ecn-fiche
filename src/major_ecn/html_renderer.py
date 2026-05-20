"""Rendu HTML d'une `FicheData` via Jinja2 et conversion Markdown.

Produit un document HTML autonome (CSS inliné) prêt à être converti en PDF
par WeasyPrint, en appliquant la charte « luxe médical ».
"""

from __future__ import annotations

import re
from pathlib import Path

import markdown as md_lib
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

from major_ecn.config import (
    FICHE_LEGEND,
    LOGO_PATH,
    PALETTE,
    REFLEXE_TYPES,
    TEMPLATES_DIR,
)
from major_ecn.models import FicheData

# Extensions Markdown : tableaux + listes imbriquées fiables.
_MD_EXTENSIONS = ["tables", "sane_lists"]

# Marqueurs de légende → classe CSS pour la coloration.
_MARKER_CLASSES = {"★": "m-ecn", "◆": "m-yield", "⚠": "m-trap"}

# Détection des tableaux Markdown (ligne de cellules + ligne de séparation).
_TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
_TABLE_DELIM_RE = re.compile(r"^\s*\|(?:\s*:?-+:?\s*\|)+\s*$")


def _normalize_tables(text: str) -> str:
    """Isole les tableaux Markdown pour qu'ils soient toujours interprétés.

    Python-Markdown n'interprète un tableau que s'il est précédé d'une ligne
    vide et écrit sans indentation. Le contenu généré par l'IA omet
    fréquemment ces règles (tableau collé à une puce, lignes indentées), ce
    qui fait apparaître le tableau en texte brut. On rétablit ici la ligne
    vide avant/après et on désindente les lignes du tableau.
    """
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)
    while i < n:
        if (
            i + 1 < n
            and _TABLE_ROW_RE.match(lines[i])
            and _TABLE_DELIM_RE.match(lines[i + 1])
        ):
            if out and out[-1].strip():
                out.append("")
            j = i
            while j < n and _TABLE_ROW_RE.match(lines[j]):
                out.append(lines[j].strip())
                j += 1
            if j < n and lines[j].strip():
                out.append("")
            i = j
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out)


def _markdown_converter() -> md_lib.Markdown:
    """Crée un convertisseur Markdown réutilisable (réinitialisé à chaque appel)."""
    return md_lib.Markdown(extensions=_MD_EXTENSIONS, output_format="html")


def _highlight_markers(html: str) -> str:
    """Enveloppe les marqueurs de légende (★ ◆ ⚠) dans des spans stylables."""
    for symbol, css_class in _MARKER_CLASSES.items():
        html = html.replace(
            symbol, f'<span class="fmark {css_class}">{symbol}</span>'
        )
    return html


def render_markdown(text: str) -> Markup:
    """Convertit du Markdown en HTML sûr (bloc complet)."""
    if not text or not text.strip():
        return Markup("")
    converter = _markdown_converter()
    return Markup(_highlight_markers(converter.convert(_normalize_tables(text))))


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
        legend=FICHE_LEGEND,
        reflexe_labels={key: label for key, (label, _) in REFLEXE_TYPES.items()},
    )

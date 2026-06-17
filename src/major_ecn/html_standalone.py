"""Rendu d'une fiche en HTML **autoporté** (self-contained).

Produit une chaîne HTML entièrement autonome — polices et images encodées en
base64 — destinée à être stockée dans `fiches.content_html` puis affichée
telle quelle côté site (éditeur Tiptap) ou re-rendue en PDF sans dépendre du
système de fichiers local.

On part du rendu Jinja standard (`render_fiche_html`), qui inline déjà le CSS
mais référence les polices via des URL relatives `url("fonts/…")` et les
images via des URI `file://`. On remplace ici :

  - `url("fonts/X.ttf")`           → `url("data:font/ttf;base64,…")`
  - `src="file:///…"` / `url("file:///…")` (images, logo, filigrane)
                                    → data URI base64 selon le type MIME.
"""

from __future__ import annotations

import base64
import mimetypes
import re
import urllib.parse
from pathlib import Path

from major_ecn.config import FONTS_DIR
from major_ecn.html_renderer import render_fiche_html
from major_ecn.models import FicheData

_FONT_URL_RE = re.compile(r'url\("fonts/([^"]+)"\)')
_FILE_URI_RE = re.compile(r'(src|href)="(file://[^"]+)"')
_CSS_FILE_URI_RE = re.compile(r'url\("(file://[^"]+)"\)')

_FONT_MIME = {
    ".ttf": "font/ttf",
    ".otf": "font/otf",
    ".woff": "font/woff",
    ".woff2": "font/woff2",
}


def _b64(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def _font_data_uri(filename: str) -> str | None:
    path = FONTS_DIR / filename
    if not path.exists():
        return None
    mime = _FONT_MIME.get(path.suffix.lower(), "font/ttf")
    return f"data:{mime};base64,{_b64(path.read_bytes())}"


def _file_uri_to_path(uri: str) -> Path:
    """Convertit une URI `file://` en chemin local décodé."""
    parsed = urllib.parse.urlparse(uri)
    return Path(urllib.parse.unquote(parsed.path))


def _file_data_uri(uri: str) -> str | None:
    path = _file_uri_to_path(uri)
    if not path.exists():
        return None
    mime, _ = mimetypes.guess_type(str(path))
    mime = mime or "application/octet-stream"
    return f"data:{mime};base64,{_b64(path.read_bytes())}"


def _inline_fonts(html: str) -> str:
    def _repl(m: re.Match) -> str:
        uri = _font_data_uri(m.group(1))
        return f'url("{uri}")' if uri else m.group(0)
    return _FONT_URL_RE.sub(_repl, html)


def _inline_file_uris(html: str) -> str:
    def _repl_attr(m: re.Match) -> str:
        uri = _file_data_uri(m.group(2))
        return f'{m.group(1)}="{uri}"' if uri else m.group(0)

    def _repl_css(m: re.Match) -> str:
        uri = _file_data_uri(m.group(1))
        return f'url("{uri}")' if uri else m.group(0)

    html = _FILE_URI_RE.sub(_repl_attr, html)
    html = _CSS_FILE_URI_RE.sub(_repl_css, html)
    return html


def render_fiche_html_standalone(fiche: FicheData) -> str:
    """Rend la fiche en HTML autoporté (polices + images en base64)."""
    html = render_fiche_html(fiche)
    html = _inline_fonts(html)
    html = _inline_file_uris(html)
    return html

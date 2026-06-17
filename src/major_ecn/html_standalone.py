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

from major_ecn.config import ASSETS_DIR, FONTS_DIR
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


# Charset fixe couvrant le français médical + symboles employés (★ ◆ ⚠ • ◦ …).
# On sous-ensemble les polices à ces caractères : ~9 Mo de TTF → ~1 Mo de woff2,
# ce qui allège massivement `content_html` (stockage DB + éditeur Tiptap).
_SUBSET_VERSION = "v2"


def _subset_unicodes() -> set[int]:
    cps: set[int] = set()
    cps |= set(range(0x20, 0x7F))      # ASCII imprimable
    cps |= set(range(0xA0, 0x100))     # Latin-1 (accents français)
    cps |= set(range(0x100, 0x180))    # Latin Extended-A (œ, etc.)
    for cp in (0x2009, 0x202F, 0x2013, 0x2014, 0x2018, 0x2019, 0x201C, 0x201D,
               0x2022, 0x2026, 0x25E6, 0x25C6, 0x2605, 0x26A0, 0x20AC, 0x2190,
               0x2191, 0x2192, 0x2193, 0x2264, 0x2265, 0x00B0, 0x00B1, 0x00D7,
               0x00F7, 0x00B5, 0x00B2, 0x00B3, 0x2032, 0x2033):
        cps.add(cp)
    return cps


_CACHE_DIR = Path("/tmp/font_subset_cache")


def _subset_font_bytes(path: Path) -> tuple[bytes, str]:
    """Sous-ensemble une police → (octets, mime). Cache disque. woff2 si possible."""
    _CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache = _CACHE_DIR / f"{path.stem}.{_SUBSET_VERSION}.woff2"
    if cache.exists():
        return cache.read_bytes(), "font/woff2"
    try:
        from fontTools.subset import Options, Subsetter
        from fontTools.ttLib import TTFont
        import io

        font = TTFont(str(path))
        opts = Options()
        opts.flavor = "woff2"
        opts.desubroutinize = True
        opts.notdef_outline = True
        opts.recalc_bounds = False
        opts.layout_features = []   # on n'a pas besoin des features OpenType
        opts.glyph_names = False
        opts.name_IDs = []
        opts.legacy_kern = False
        ss = Subsetter(options=opts)
        ss.populate(unicodes=_subset_unicodes())
        ss.subset(font)
        buf = io.BytesIO()
        font.save(buf)
        data = buf.getvalue()
        cache.write_bytes(data)
        return data, "font/woff2"
    except Exception:
        # Repli : police complète non sous-ensemblée (rare).
        mime = _FONT_MIME.get(path.suffix.lower(), "font/ttf")
        return path.read_bytes(), mime


def _font_data_uri(filename: str) -> str | None:
    path = FONTS_DIR / filename
    if not path.exists():
        return None
    data, mime = _subset_font_bytes(path)
    return f"data:{mime};base64,{_b64(data)}"


def _file_uri_to_path(uri: str) -> Path:
    """Convertit une URI `file://` en chemin local décodé."""
    parsed = urllib.parse.urlparse(uri)
    return Path(urllib.parse.unquote(parsed.path))


_IMG_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp"}
_IMG_MAX_DIM = 1300       # côté max des figures (lisibilité conservée)
_DECOR_MAX_DIM = 360      # côté max des décorations (logo, filigrane)


def _image_data_uri(path: Path, max_dim: int = _IMG_MAX_DIM) -> tuple[str, bytes] | None:
    """Recompresse une image pour l'inline HTML : downscale + JPEG (ou PNG si
    transparence). Réduit fortement `content_html` sans dégrader le PDF (qui,
    lui, lit toujours le fichier d'origine en pleine résolution)."""
    try:
        from PIL import Image
        import io

        img = Image.open(path)
        img.load()
        w, h = img.size
        if max(w, h) > max_dim:
            s = max_dim / max(w, h)
            img = img.resize((max(1, int(w * s)), max(1, int(h * s))))
        has_alpha = img.mode in ("RGBA", "LA") or (
            img.mode == "P" and "transparency" in img.info
        )
        buf = io.BytesIO()
        if has_alpha:
            img.convert("RGBA").save(buf, format="PNG", optimize=True)
            return "image/png", buf.getvalue()
        img.convert("RGB").save(buf, format="JPEG", quality=85, optimize=True)
        return "image/jpeg", buf.getvalue()
    except Exception:
        return None


def _file_data_uri(uri: str) -> str | None:
    path = _file_uri_to_path(uri)
    if not path.exists():
        return None
    if path.suffix.lower() in _IMG_EXTS:
        # Logo / filigrane (dans assets/) = décoration → plafond bas.
        try:
            is_decor = ASSETS_DIR in path.resolve().parents
        except Exception:
            is_decor = False
        out = _image_data_uri(path, _DECOR_MAX_DIM if is_decor else _IMG_MAX_DIM)
        if out is not None:
            mime, data = out
            return f"data:{mime};base64,{_b64(data)}"
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

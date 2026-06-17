"""Génération du PDF final : HTML stylé → PDF via Playwright (Chromium headless).

Utilise le même rendu HTML/CSS que la version WeasyPrint, mais remplace le
moteur de rendu par Chromium via Playwright, ce qui élimine la dépendance aux
bibliothèques système GTK3/Pango.

Stratégie : rendu en une seule passe pour que la numérotation des pages soit
correcte (cover = page 1). La page de garde utilise des marges négatives CSS
pour s'étendre en pleine page malgré les marges du PDF.
"""

from __future__ import annotations

import re
import tempfile
from pathlib import Path

from major_ecn.config import ASSETS_DIR, PALETTE
from major_ecn.html_renderer import render_fiche_html
from major_ecn.models import FicheData


class PDFGenerationError(RuntimeError):
    """Erreur lors du rendu PDF."""


_FONT_URL_RE = re.compile(r'url\("(fonts/[^"]+)"\)')

_TOP_MM = 24
_RIGHT_MM = 18
_BOTTOM_MM = 20
_LEFT_MM = 18


def _resolve_font_urls(html: str) -> str:
    """Remplace les URL relatives des polices par des file:// absolues."""
    def _replacer(m: re.Match) -> str:
        abs_path = (ASSETS_DIR / m.group(1)).resolve()
        return f'url("{abs_path.as_uri()}")'
    return _FONT_URL_RE.sub(_replacer, html)


def _strip_weasyprint_page_rules(html: str) -> str:
    """Retire les @page margin boxes (non supportés par Chromium)."""
    html = re.sub(r'@top-(?:left|right)\s*\{[^}]*\}', '', html)
    html = re.sub(r'@bottom-(?:center|right)\s*\{[^}]*\}', '', html)
    html = re.sub(
        r'@page\s*:first\s*\{[^}]*(?:\{[^}]*\}[^}]*)*\}', '', html
    )
    html = re.sub(r'border-top:\s*0\.7pt\s+solid\s+var\(--navy\);', '', html)
    html = re.sub(
        r'@page\s*\{[^}]*\}', '', html
    )
    return html


def _inject_chromium_overrides(html: str) -> str:
    """Injecte du CSS pour le rendu Chromium (cover pleine page, etc.)."""
    navy = PALETTE.navy
    pearl = PALETTE.pearl
    overrides = f"""<style>
/* Chromium PDF overrides */
@page {{
  size: A4;
  margin: {_TOP_MM}mm {_RIGHT_MM}mm {_BOTTOM_MM}mm {_LEFT_MM}mm;
}}
.cover {{
  margin: -{_TOP_MM}mm -{_RIGHT_MM}mm 0 -{_LEFT_MM}mm;
  width: 210mm;
  height: 297mm;
  page-break-after: always;
}}
.cover-band {{
  height: 297mm;
}}
/* En-tête répété sur chaque page (sauf cover via first-child) */
.page-header-bar {{
  position: running(pageHeader);
  font-family: 'Inter', sans-serif;
  font-size: 8pt;
  display: flex;
  justify-content: space-between;
  border-top: 0.7pt solid {navy};
  padding-top: 2mm;
  margin-bottom: 3mm;
}}
.page-header-left {{ color: {pearl}; }}
.page-header-right {{ color: {navy}; font-style: italic; }}
/* Pied de page */
.page-footer-bar {{
  font-family: 'Inter', sans-serif;
  font-size: 7.6pt;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 4mm;
}}
.page-footer-left {{
  color: {pearl};
  letter-spacing: 0.12em;
  text-transform: uppercase;
}}
.page-footer-pill {{
  color: #fff;
  background: {navy};
  border-radius: 2.4mm;
  padding: 1.5mm 4mm;
  font-weight: 700;
  font-size: 8pt;
}}
/* Pas de page vide à la fin */
section:last-child {{ page-break-after: auto; }}
.eclair-page {{ page-break-after: avoid; }}
</style>"""
    return html.replace("</head>", f"{overrides}\n</head>")


def render_pdf(fiche: FicheData, output_path: Path) -> Path:
    """Génère le PDF d'une fiche via Chromium headless (Playwright)."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise PDFGenerationError(
            "Playwright non installé — pip install playwright && "
            "python -m playwright install chromium"
        ) from exc

    html_content = render_fiche_html(fiche)
    html_content = _resolve_font_urls(html_content)
    html_content = _strip_weasyprint_page_rules(html_content)
    html_content = _inject_chromium_overrides(html_content)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_dir = ASSETS_DIR / "templates"
    tmp_html = tmp_dir / "_tmp_render.html"

    try:
        tmp_html.write_text(html_content, encoding="utf-8")
        file_url = tmp_html.resolve().as_uri()

        pw = sync_playwright().start()
        # Permet d'utiliser un binaire Chromium pré-installé (sandbox sans accès
        # au CDN Playwright) via PLAYWRIGHT_CHROMIUM_EXECUTABLE.
        import os
        exe = os.environ.get("PLAYWRIGHT_CHROMIUM_EXECUTABLE", "").strip()
        launch_kwargs = {"executable_path": exe} if exe else {}
        browser = pw.chromium.launch(**launch_kwargs)
        page = browser.new_page()
        page.goto(file_url, wait_until="networkidle")
        page.wait_for_timeout(1500)

        # La fiche éclair doit tenir sur UNE seule page : on la réduit via `zoom`
        # (qui, contrairement à `transform`, réduit aussi la hauteur de mise en
        # page) si son contenu dépasse la hauteur utile d'une page A4.
        page.evaluate(
            """(args) => {
              const [topMm, bottomMm] = args;
              const mmToPx = (mm) => (mm * 96) / 25.4;
              const avail = mmToPx(297 - topMm - bottomMm) - 4;
              document.querySelectorAll('.eclair-card').forEach((card) => {
                card.style.zoom = '1';
                const h = card.getBoundingClientRect().height;
                if (h > avail) {
                  card.style.zoom = String(Math.max(0.5, avail / h));
                }
              });
            }""",
            [_TOP_MM, _BOTTOM_MM],
        )

        navy = PALETTE.navy
        pearl = PALETTE.pearl

        header_tpl = (
            f'<div style="width:100%;font-size:8pt;font-family:Inter,sans-serif;'
            f'padding:0 {_LEFT_MM}mm;display:flex;justify-content:space-between;'
            f'border-top:0.7pt solid {navy};padding-top:2mm;">'
            f'<span style="color:{pearl};">{fiche.nom_cours}</span>'
            f'<span style="color:{navy};font-style:italic;">'
            f'<span class="pageNumber"></span>/<span class="totalPages"></span>'
            f'</span></div>'
        )

        footer_tpl = (
            f'<div style="width:100%;font-size:7.6pt;font-family:Inter,sans-serif;'
            f'padding:0 {_LEFT_MM}mm;display:flex;justify-content:space-between;'
            f'align-items:center;">'
            f'<span style="color:{pearl};letter-spacing:0.12em;text-transform:uppercase;">'
            f'Major ECN &middot; {fiche.annee}</span>'
            f'<span style="color:#fff;background:{navy};border-radius:2.4mm;'
            f'padding:1.5mm 4mm;font-weight:700;font-size:8pt;">'
            f'<span class="pageNumber"></span>/<span class="totalPages"></span>'
            f'</span></div>'
        )

        page.pdf(
            path=str(output_path),
            format="A4",
            print_background=True,
            margin={
                "top": f"{_TOP_MM}mm",
                "right": f"{_RIGHT_MM}mm",
                "bottom": f"{_BOTTOM_MM}mm",
                "left": f"{_LEFT_MM}mm",
            },
            display_header_footer=True,
            header_template=header_tpl,
            footer_template=footer_tpl,
        )

        browser.close()
        pw.stop()

    except Exception as exc:
        raise PDFGenerationError(f"Échec du rendu PDF ({exc})") from exc
    finally:
        tmp_html.unlink(missing_ok=True)

    return output_path

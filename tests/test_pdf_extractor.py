"""Tests de l'extraction PDF (texte + images)."""

from __future__ import annotations

import io
from pathlib import Path

import fitz
import pytest

from major_ecn.pdf_extractor import PDFExtractionError, extract_document


def _make_pdf(path: Path, *, with_image: bool = False, text: str | None = None) -> None:
    """Crée un PDF de test avec du texte et, optionnellement, une image."""
    doc = fitz.open()
    page = doc.new_page()
    body = text if text is not None else ("Cours de cardiologie sur l'HTA. " * 80)
    page.insert_textbox(fitz.Rect(40, 40, 555, 800), body, fontsize=11)
    if with_image:
        from PIL import Image

        buffer = io.BytesIO()
        Image.new("RGB", (220, 180), (210, 30, 70)).save(buffer, "PNG")
        page.insert_image(fitz.Rect(60, 500, 280, 680), stream=buffer.getvalue())
    doc.save(str(path))
    doc.close()


def test_extract_text(tmp_path: Path) -> None:
    pdf = tmp_path / "cours.pdf"
    _make_pdf(pdf)
    document = extract_document(pdf)
    assert document.page_count == 1
    assert "cardiologie" in document.text.lower()
    assert len(document.text) > 200
    assert document.used_ocr is False


def test_extract_with_image(tmp_path: Path) -> None:
    pdf = tmp_path / "cours_img.pdf"
    _make_pdf(pdf, with_image=True)
    document = extract_document(pdf)
    assert len(document.images) == 1
    image = document.images[0]
    assert image.width >= 90 and image.height >= 90
    assert image.page == 1


def test_missing_file_raises() -> None:
    with pytest.raises(PDFExtractionError):
        extract_document(Path("/chemin/inexistant/cours.pdf"))


def test_empty_pdf_raises(tmp_path: Path) -> None:
    pdf = tmp_path / "vide.pdf"
    _make_pdf(pdf, text=" ")
    with pytest.raises(PDFExtractionError):
        extract_document(pdf)

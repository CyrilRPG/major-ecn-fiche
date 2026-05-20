"""Extraction de texte et d'images depuis un PDF de cours (PyMuPDF).

Stratégie :
  1. Extraction du texte natif page par page.
  2. Si le PDF est scanné (peu de texte natif), repli OCR (`pytesseract`).
  3. Extraction de toutes les images, dédoublonnées et filtrées par taille.
"""

from __future__ import annotations

import hashlib
import io
from pathlib import Path

import fitz  # PyMuPDF

from major_ecn.config import MIN_IMAGE_DIMENSION_PX, SCANNED_TEXT_THRESHOLD
from major_ecn.models import ExtractedDocument, ExtractedImage
from major_ecn.utils.logger import get_logger


class PDFExtractionError(RuntimeError):
    """Erreur fatale lors de l'extraction d'un PDF."""


def _looks_scanned(text: str, page_count: int) -> bool:
    """Heuristique : un PDF avec très peu de texte par page est probablement scanné."""
    if page_count == 0:
        return False
    return len(text.strip()) / page_count < SCANNED_TEXT_THRESHOLD


def _ocr_document(pdf_path: Path) -> str:
    """Repli OCR pour les PDF scannés. Renvoie une chaîne vide si OCR indisponible."""
    logger = get_logger()
    try:
        import pytesseract  # type: ignore
        from pdf2image import convert_from_path  # type: ignore
    except ImportError:
        logger.warning("[yellow]OCR indisponible (pytesseract/pdf2image absents).[/yellow]")
        return ""

    try:
        pages = convert_from_path(str(pdf_path), dpi=220)
    except Exception as exc:  # noqa: BLE001 — poppler manquant ou PDF illisible
        logger.warning("[yellow]OCR impossible (%s) — Poppler installé ?[/yellow]", exc)
        return ""

    chunks: list[str] = []
    for page_image in pages:
        try:
            chunks.append(pytesseract.image_to_string(page_image, lang="fra"))
        except Exception as exc:  # noqa: BLE001 — tesseract ou langue manquante
            logger.warning("[yellow]Échec OCR d'une page (%s).[/yellow]", exc)
    return "\n\n".join(chunks).strip()


def _extract_images(doc: fitz.Document) -> list[ExtractedImage]:
    """Extrait et dédoublonne les images significatives du PDF."""
    images: list[ExtractedImage] = []
    seen_sha: set[str] = set()

    for page_index in range(doc.page_count):
        page = doc[page_index]
        for img_index, img_info in enumerate(page.get_images(full=True)):
            xref = img_info[0]
            try:
                raw = doc.extract_image(xref)
            except Exception:  # noqa: BLE001 — xref corrompu
                continue

            data: bytes = raw.get("image", b"")
            if not data:
                continue
            width = int(raw.get("width", 0))
            height = int(raw.get("height", 0))
            if width < MIN_IMAGE_DIMENSION_PX or height < MIN_IMAGE_DIMENSION_PX:
                continue  # Icône / puce décorative

            sha = hashlib.sha1(data).hexdigest()
            if sha in seen_sha:
                continue  # Même logo répété sur chaque page
            seen_sha.add(sha)

            images.append(
                ExtractedImage(
                    data=data,
                    ext=raw.get("ext", "png"),
                    page=page_index + 1,
                    index=img_index,
                    width=width,
                    height=height,
                    sha=sha,
                )
            )
    return images


def extract_document(pdf_path: Path) -> ExtractedDocument:
    """Extrait le texte et les images d'un PDF de cours.

    Lève `PDFExtractionError` si le PDF est illisible.
    """
    logger = get_logger()
    if not pdf_path.is_file():
        raise PDFExtractionError(f"Fichier introuvable : {pdf_path}")

    try:
        doc = fitz.open(pdf_path)
    except Exception as exc:  # noqa: BLE001 — PDF corrompu / chiffré
        raise PDFExtractionError(f"Ouverture impossible ({exc})") from exc

    try:
        if doc.page_count == 0:
            raise PDFExtractionError("PDF sans page.")

        text_parts = [doc[i].get_text("text") for i in range(doc.page_count)]
        text = "\n\n".join(text_parts).strip()
        page_count = doc.page_count
        images = _extract_images(doc)
    finally:
        doc.close()

    used_ocr = False
    if _looks_scanned(text, page_count):
        logger.info("[cyan]PDF probablement scanné — tentative OCR…[/cyan]")
        ocr_text = _ocr_document(pdf_path)
        if len(ocr_text) > len(text):
            text = ocr_text
            used_ocr = True

    if len(text.strip()) < 200:
        raise PDFExtractionError("Texte exploitable insuffisant (PDF vide ou non-OCR-isable).")

    logger.debug(
        "Extraction %s : %d pages, %d caractères, %d images%s",
        pdf_path.name, page_count, len(text), len(images),
        " (OCR)" if used_ocr else "",
    )
    return ExtractedDocument(text=text, images=images, page_count=page_count, used_ocr=used_ocr)


def normalize_image_to_png(image: ExtractedImage) -> bytes:
    """Convertit une image extraite en PNG (compatibilité WeasyPrint / python-docx)."""
    if image.ext.lower() == "png":
        return image.data
    try:
        from PIL import Image  # type: ignore

        with Image.open(io.BytesIO(image.data)) as pil_image:
            buffer = io.BytesIO()
            pil_image.convert("RGB").save(buffer, format="PNG")
            return buffer.getvalue()
    except Exception:  # noqa: BLE001 — repli sur les octets bruts
        return image.data

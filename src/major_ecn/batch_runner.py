"""Orchestration du traitement par lot : extraction → IA → rendu, en parallèle.

Traite 4 à 8 PDF simultanément (selon la configuration), affiche une barre de
progression `rich` (PDF, %, ETA, coût API) et produit un récapitulatif complet.
"""

from __future__ import annotations

import asyncio
import shutil
import time
from dataclasses import dataclass, field
from pathlib import Path

from anthropic import AsyncAnthropic
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)

from major_ecn.ai_processor import AIProcessingError
from major_ecn.config import LOGO_PATH, Settings
from major_ecn.content_builder import build_fiche, output_basename
from major_ecn.docx_generator import DocxGenerationError, render_docx
from major_ecn.models import UsageStats
from major_ecn.pdf_extractor import PDFExtractionError, extract_document
from major_ecn.pdf_generator import PDFGenerationError, render_pdf
from major_ecn.utils.logger import console, get_logger
from major_ecn.utils.slugify import slugify


@dataclass
class BatchOptions:
    """Options d'exécution d'un lot."""

    recursive: bool = False
    generate_pdf: bool = True
    generate_docx: bool = True
    output_dir: Path | None = None
    limit: int | None = None


@dataclass
class PDFResult:
    """Résultat du traitement d'un PDF."""

    pdf: Path
    success: bool = False
    nom_cours: str = ""
    pdf_path: Path | None = None
    docx_path: Path | None = None
    error: str = ""
    failed_step: str = ""
    duration: float = 0.0
    usage: UsageStats = field(default_factory=UsageStats)


@dataclass
class BatchSummary:
    """Bilan complet d'un lot."""

    matiere: str
    output_dir: Path
    log_path: Path
    results: list[PDFResult] = field(default_factory=list)
    duration: float = 0.0

    @property
    def succeeded(self) -> list[PDFResult]:
        return [r for r in self.results if r.success]

    @property
    def failed(self) -> list[PDFResult]:
        return [r for r in self.results if not r.success]

    @property
    def total_cost(self) -> float:
        return sum(r.usage.cost_usd for r in self.results)


class _CostMeter:
    """Compteur de coût partagé, mis à jour au fil des PDF terminés."""

    def __init__(self) -> None:
        self.cost = 0.0

    def add(self, amount: float) -> None:
        self.cost += amount


def discover_pdfs(folder: Path, recursive: bool) -> list[Path]:
    """Liste les PDF d'un dossier (récursif optionnel), triés par nom."""
    pattern = "**/*.pdf" if recursive else "*.pdf"
    pdfs = [p for p in folder.glob(pattern) if p.is_file()]
    # Ignore le dossier de sortie s'il est imbriqué.
    pdfs = [p for p in pdfs if "Fiches_Major_ECN" not in p.parts]
    return sorted(pdfs, key=lambda p: p.name.lower())


def _classify_error(exc: Exception) -> str:
    """Associe une exception à l'étape du pipeline qui a échoué."""
    if isinstance(exc, PDFExtractionError):
        return "extraction PDF"
    if isinstance(exc, AIProcessingError):
        return "rédaction IA"
    if isinstance(exc, PDFGenerationError):
        return "rendu PDF"
    if isinstance(exc, DocxGenerationError):
        return "génération DOCX"
    return "inconnue"


async def _process_one(
    pdf: Path,
    *,
    matiere: str,
    output_dir: Path,
    client: AsyncAnthropic,
    settings: Settings,
    options: BatchOptions,
    semaphore: asyncio.Semaphore,
    progress: Progress,
    task_id,
    cost_meter: _CostMeter,
) -> PDFResult:
    """Traite un PDF de bout en bout (extraction → IA → rendu PDF/DOCX)."""
    logger = get_logger()
    result = PDFResult(pdf=pdf)
    work_dir = output_dir / ".work" / slugify(pdf.stem)
    started = time.monotonic()

    async with semaphore:
        loop = asyncio.get_running_loop()
        logger.info("[cyan]▶[/cyan] Traitement : %s", pdf.name)
        try:
            extracted = await loop.run_in_executor(None, extract_document, pdf)

            fiche = await build_fiche(
                extracted,
                matiere=matiere,
                fallback_nom_cours=pdf.stem,
                client=client,
                settings=settings,
                work_dir=work_dir,
            )
            result.nom_cours = fiche.nom_cours
            result.usage = fiche.usage

            basename = output_basename(matiere, fiche.nom_cours, settings.year)
            if options.generate_pdf:
                pdf_out = output_dir / f"{basename}.pdf"
                await loop.run_in_executor(None, render_pdf, fiche, pdf_out)
                result.pdf_path = pdf_out
            if options.generate_docx:
                logo = LOGO_PATH if LOGO_PATH.exists() else None
                docx_out = output_dir / f"{basename}.docx"
                await loop.run_in_executor(None, render_docx, fiche, docx_out, logo)
                result.docx_path = docx_out

            result.success = True
            logger.info("[green]✓[/green] Fiche générée : %s", fiche.nom_cours)
        except Exception as exc:  # noqa: BLE001 — un PDF en échec ne stoppe pas le lot
            result.success = False
            result.error = str(exc)
            result.failed_step = _classify_error(exc)
            logger.error(
                "[red]✗[/red] Échec sur %s (étape : %s) — %s",
                pdf.name, result.failed_step, exc,
            )
            logger.debug("Trace complète", exc_info=True)
        finally:
            shutil.rmtree(work_dir, ignore_errors=True)
            result.duration = time.monotonic() - started
            cost_meter.add(result.usage.cost_usd)
            progress.update(task_id, advance=1, cost=cost_meter.cost)

    return result


async def run_batch(
    folder: Path, settings: Settings, options: BatchOptions, verbose: bool = False
) -> BatchSummary:
    """Traite tous les PDF d'un dossier et renvoie le bilan du lot."""
    from major_ecn.utils.logger import setup_logging

    logger, log_path = setup_logging(verbose=verbose)
    matiere = folder.name
    output_dir = options.output_dir or (folder.parent / "Fiches_Major_ECN")
    output_dir.mkdir(parents=True, exist_ok=True)

    pdfs = discover_pdfs(folder, options.recursive)
    if options.limit is not None:
        pdfs = pdfs[: options.limit]

    summary = BatchSummary(matiere=matiere, output_dir=output_dir, log_path=log_path)
    if not pdfs:
        logger.warning("[yellow]Aucun PDF trouvé dans %s[/yellow]", folder)
        return summary

    logger.info(
        "[bold]Matière :[/bold] %s  ·  [bold]%d PDF[/bold]  ·  "
        "concurrence %d  ·  modèle %s",
        matiere, len(pdfs), settings.concurrency, settings.writer_model,
    )

    semaphore = asyncio.Semaphore(settings.concurrency)
    cost_meter = _CostMeter()
    started = time.monotonic()

    client = AsyncAnthropic(api_key=settings.anthropic_api_key)
    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold]Fiches Major ECN"),
            BarColumn(bar_width=32),
            MofNCompleteColumn(),
            TextColumn("·  coût ~[bold]${task.fields[cost]:.2f}"),
            TimeElapsedColumn(),
            TextColumn("·  ETA"),
            TimeRemainingColumn(),
            console=console,
        ) as progress:
            task_id = progress.add_task("batch", total=len(pdfs), cost=0.0)
            tasks = [
                _process_one(
                    pdf,
                    matiere=matiere,
                    output_dir=output_dir,
                    client=client,
                    settings=settings,
                    options=options,
                    semaphore=semaphore,
                    progress=progress,
                    task_id=task_id,
                    cost_meter=cost_meter,
                )
                for pdf in pdfs
            ]
            summary.results = await asyncio.gather(*tasks)
    finally:
        await client.close()
        shutil.rmtree(output_dir / ".work", ignore_errors=True)

    summary.duration = time.monotonic() - started
    _log_summary(summary)
    return summary


def _log_summary(summary: BatchSummary) -> None:
    """Trace le récapitulatif du lot dans le fichier de log."""
    logger = get_logger()
    logger.info("──────── RÉCAPITULATIF DU LOT ────────")
    logger.info("Matière : %s", summary.matiere)
    logger.info("Durée totale : %.1f s", summary.duration)
    logger.info("Coût API estimé : ~$%.2f", summary.total_cost)
    logger.info("PDF traités avec succès : %d", len(summary.succeeded))
    for result in summary.succeeded:
        logger.info(
            "  ✅ %s → %s", result.pdf.name, result.nom_cours or "(sans titre)"
        )
    logger.info("PDF en échec : %d", len(summary.failed))
    for result in summary.failed:
        logger.info(
            "  ❌ %s (étape : %s) — %s",
            result.pdf.name, result.failed_step, result.error,
        )

"""Point d'entrée CLI du générateur de fiches Major ECN (Typer)."""

from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Optional

import typer
from rich.panel import Panel
from rich.table import Table

from major_ecn import __version__
from major_ecn.batch_runner import BatchOptions, BatchSummary, run_batch
from major_ecn.config import Settings
from major_ecn.utils.logger import console

app = typer.Typer(
    name="major-ecn",
    help="Transforme un dossier de PDF de cours en fiches de révision Major ECN "
    "(export PDF + Word).",
    add_completion=False,
    no_args_is_help=True,
)


def _version_callback(value: bool) -> None:
    if value:
        console.print(f"major-ecn-generator [bold]{__version__}[/bold]")
        raise typer.Exit()


@app.command()
def generate(
    folder: Path = typer.Argument(
        ...,
        help="Dossier contenant les PDF de cours (son nom = la matière).",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True,
    ),
    recursive: bool = typer.Option(
        False, "--recursive", "-r", help="Parcourt aussi les sous-dossiers."
    ),
    year: Optional[str] = typer.Option(
        None, "--year", help="Année universitaire affichée (défaut : 2025-2026)."
    ),
    output: Optional[Path] = typer.Option(
        None, "--output", "-o", help="Dossier de sortie (défaut : ../Fiches_Major_ECN)."
    ),
    concurrency: Optional[int] = typer.Option(
        None, "--concurrency", "-c", min=1, max=8,
        help="Nombre de PDF traités en parallèle (1 à 8).",
    ),
    limit: Optional[int] = typer.Option(
        None, "--limit", "-l", min=1, help="Ne traite que les N premiers PDF."
    ),
    no_pdf: bool = typer.Option(False, "--no-pdf", help="N'exporte pas le PDF."),
    no_docx: bool = typer.Option(False, "--no-docx", help="N'exporte pas le DOCX."),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Affiche les logs détaillés."
    ),
    _version: bool = typer.Option(
        False, "--version", callback=_version_callback, is_eager=True,
        help="Affiche la version et quitte.",
    ),
) -> None:
    """Génère les fiches Major ECN pour tous les PDF d'un dossier."""
    settings = Settings.load()
    if year:
        settings.year = year
    if concurrency:
        settings.concurrency = concurrency

    if not settings.anthropic_api_key:
        console.print(
            "[bold red]Erreur :[/bold red] clé API Anthropic manquante.\n"
            "Renseignez [bold]ANTHROPIC_API_KEY[/bold] dans le fichier [bold].env[/bold] "
            "(voir .env.example)."
        )
        raise typer.Exit(code=1)

    if no_pdf and no_docx:
        console.print("[bold red]Erreur :[/bold red] --no-pdf et --no-docx désactivent "
                      "toute sortie.")
        raise typer.Exit(code=1)

    options = BatchOptions(
        recursive=recursive,
        generate_pdf=not no_pdf,
        generate_docx=not no_docx,
        output_dir=output,
        limit=limit,
    )

    console.print(
        Panel.fit(
            f"[bold #E11D48]Major ECN Generator[/bold #E11D48]  ·  v{__version__}\n"
            f"Matière : [bold]{folder.name}[/bold]\n"
            f"Dossier : {folder}",
            border_style="#C9A961",
        )
    )

    try:
        summary = asyncio.run(run_batch(folder, settings, options, verbose=verbose))
    except KeyboardInterrupt:  # pragma: no cover
        console.print("[yellow]Interruption demandée — arrêt.[/yellow]")
        raise typer.Exit(code=130) from None

    _print_recap(summary)
    if summary.results and not summary.succeeded:
        raise typer.Exit(code=1)


def _print_recap(summary: BatchSummary) -> None:
    """Affiche le récapitulatif final du lot dans le terminal."""
    table = Table(show_header=False, box=None, pad_edge=False)
    table.add_column(style="bold")
    table.add_column()
    table.add_row("Fiches générées", f"[green]{len(summary.succeeded)}[/green]")
    table.add_row("Échecs", f"[red]{len(summary.failed)}[/red]")
    table.add_row("Durée totale", f"{summary.duration:.1f} s")
    table.add_row("Coût API estimé", f"~${summary.total_cost:.2f}")
    table.add_row("Dossier de sortie", str(summary.output_dir))
    table.add_row("Journal", str(summary.log_path))

    console.print(
        Panel(table, title="[bold]Récapitulatif", border_style="#C9A961", expand=False)
    )

    if summary.failed:
        fail_table = Table(title="PDF en échec", title_style="bold red",
                           border_style="red")
        fail_table.add_column("Fichier")
        fail_table.add_column("Étape")
        fail_table.add_column("Raison")
        for result in summary.failed:
            fail_table.add_row(result.pdf.name, result.failed_step, result.error)
        console.print(fail_table)

    if summary.succeeded:
        console.print("[bold green]Fiches disponibles :[/bold green]")
        for result in summary.succeeded:
            paths = [str(p) for p in (result.pdf_path, result.docx_path) if p]
            console.print(f"  [green]✓[/green] {result.nom_cours}")
            for path in paths:
                console.print(f"    [dim]{path}[/dim]")


if __name__ == "__main__":  # pragma: no cover
    app()

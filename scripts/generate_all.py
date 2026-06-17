"""Génère les 18 fiches Major ECN (PDF uniquement) depuis inputs/.

Usage :
    python scripts/generate_all.py

Prérequis :
    - Clé API dans .env : ANTHROPIC_API_KEY=sk-ant-...
    - PDFs sources dans inputs/
"""

from __future__ import annotations

import asyncio
import shutil
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from anthropic import AsyncAnthropic

from major_ecn.config import LOGO_PATH, Settings
from major_ecn.content_builder import build_fiche
from major_ecn.pdf_extractor import extract_document
from major_ecn.pdf_generator import render_pdf
from major_ecn.utils.slugify import slugify

# ── Configuration ─────────────────────────────────────────────────────────────
INPUTS_DIR = PROJECT_ROOT / "inputs"
OUTPUT_DIR = PROJECT_ROOT / "output" / "fiches"
MATIERE = "Médecine générale"       # Toutes les fiches = médecine générale
CONCURRENCY = 2                      # 2 en parallèle pour ne pas saturer l'API


async def process_one(
    pdf_path: Path,
    client: AsyncAnthropic,
    settings: Settings,
    semaphore: asyncio.Semaphore,
) -> tuple[str, bool, str]:
    """Traite un PDF : extraction → IA → PDF. Retourne (nom, succès, erreur)."""
    specialty = pdf_path.stem  # Ex: "Psychiatrie", "Cardiologie"
    work_dir = OUTPUT_DIR / ".work" / slugify(specialty)
    work_dir.mkdir(parents=True, exist_ok=True)

    async with semaphore:
        print(f"\n{'='*60}")
        print(f"▶ Traitement : {specialty}")
        print(f"  Source : {pdf_path.name} ({pdf_path.stat().st_size / 1e6:.1f} MB)")
        print(f"{'='*60}")

        try:
            t0 = time.monotonic()

            # 1. Extraction texte + images du PDF source.
            print(f"  [1/4] Extraction du PDF...")
            loop = asyncio.get_running_loop()
            extracted = await loop.run_in_executor(None, extract_document, pdf_path)
            print(f"         → {len(extracted.text)} caractères, {len(extracted.images)} images")

            # 2. Pipeline IA complet (plan → rédaction → synthèse → éclair + vision).
            print(f"  [2/4] Pipeline IA (rédaction + vision)...")
            fiche = await build_fiche(
                extracted,
                matiere=MATIERE,
                fallback_nom_cours=specialty,
                client=client,
                settings=settings,
                work_dir=work_dir,
            )
            # Force le nom du cours = nom de la spécialité (pas le titre IA).
            fiche.nom_cours = specialty
            fiche.matiere = MATIERE
            print(f"         → {len(fiche.parties)} parties, "
                  f"{sum(len(p.sous_parties) for p in fiche.parties)} sous-parties, "
                  f"{len(fiche.images)} images")
            print(f"         → Coût API : ~${fiche.usage.cost_usd:.2f}")

            # 3. Génération PDF.
            print(f"  [3/4] Génération PDF...")
            basename = f"Medecine_generale_{slugify(specialty)}_{settings.year}"
            pdf_out = OUTPUT_DIR / f"{basename}.pdf"
            await loop.run_in_executor(None, render_pdf, fiche, pdf_out)
            print(f"         → {pdf_out.name} ({pdf_out.stat().st_size / 1e6:.1f} MB)")

            elapsed = time.monotonic() - t0
            print(f"  ✅ {specialty} terminé en {elapsed:.0f}s")
            return specialty, True, ""

        except Exception as exc:
            print(f"  ❌ ERREUR sur {specialty} : {exc}")
            return specialty, False, str(exc)

        finally:
            shutil.rmtree(work_dir, ignore_errors=True)


async def main() -> None:
    settings = Settings.load(env_file=PROJECT_ROOT / ".env")
    if not settings.anthropic_api_key:
        print("❌ Clé API manquante ! Renseigne ANTHROPIC_API_KEY dans .env")
        print("   cp .env.example .env && notepad .env")
        sys.exit(1)

    # Découverte des PDFs.
    pdfs = sorted(INPUTS_DIR.glob("*.pdf"), key=lambda p: p.stem)
    if not pdfs:
        print(f"❌ Aucun PDF trouvé dans {INPUTS_DIR}")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"╔{'═'*58}╗")
    print(f"║  MAJOR ECN — Génération batch de {len(pdfs)} fiches{' '*14}║")
    print(f"║  Matière : {MATIERE:<46}║")
    print(f"║  Modèle : {settings.writer_model:<47}║")
    print(f"║  Concurrence : {CONCURRENCY:<43}║")
    print(f"╚{'═'*58}╝")

    for i, pdf in enumerate(pdfs, 1):
        print(f"  {i:2d}. {pdf.stem}")

    client = AsyncAnthropic(api_key=settings.anthropic_api_key)
    semaphore = asyncio.Semaphore(CONCURRENCY)

    try:
        t_start = time.monotonic()
        tasks = [
            process_one(pdf, client, settings, semaphore)
            for pdf in pdfs
        ]
        results = await asyncio.gather(*tasks)
        elapsed = time.monotonic() - t_start

        # Récapitulatif.
        ok = [r for r in results if r[1]]
        ko = [r for r in results if not r[1]]

        print(f"\n{'═'*60}")
        print(f" RÉCAPITULATIF — {len(ok)}/{len(results)} fiches générées en {elapsed:.0f}s")
        print(f"{'═'*60}")
        for name, success, err in results:
            status = "✅" if success else "❌"
            suffix = f" — {err[:60]}" if err else ""
            print(f"  {status} {name}{suffix}")

        if ko:
            print(f"\n⚠ {len(ko)} fiche(s) en échec — relancer le script pour réessayer.")

        print(f"\n📁 Fiches PDF dans : {OUTPUT_DIR}")

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())

"""Assemblage d'une fiche : orchestration IA + parsing en `FicheData`.

Transforme les sorties Markdown brutes des 3 étapes IA en une structure
exploitable par les générateurs (HTML/PDF/DOCX), et place les images
pertinentes dans les sous-parties correspondantes.
"""

from __future__ import annotations

import asyncio
import re
from collections.abc import Callable
from difflib import SequenceMatcher
from pathlib import Path

from anthropic import AsyncAnthropic

from major_ecn.ai_processor import AIProcessor
from major_ecn.image_analyzer import ImageAnalyzer
from major_ecn.models import (
    AnalyzedImage,
    ExtractedDocument,
    FicheData,
    FicheRow,
    Partie,
    PlanPartie,
    PlanSousPartie,
    SousPartie,
    TableauSynthese,
)
from major_ecn.config import Settings
from major_ecn.pdf_extractor import normalize_image_to_png
from major_ecn.utils.logger import get_logger
from major_ecn.utils.slugify import slugify, strip_accents, titlecase_fr

ProgressCallback = Callable[[str], None]

_ROMAN_RE = re.compile(r"^\s{0,3}([IVXLCDM]{1,6})[.)]\s+(.+)$")
_LETTER_RE = re.compile(r"^\s{0,6}([A-Z])[.)]\s+(.+)$")
_TITLE_RE = re.compile(r"^\*\*(.+?)\*\*\s*[:：–-]?\s*(.*)$", re.DOTALL)
_HEADING_RE = re.compile(r"^\s*#{1,6}\s+(.*)$")
_LIGNE_RE = re.compile(r"^\s*\[(?:LIGNE|ROW|LINE)\]\s*(.*)$", re.IGNORECASE)
_REFLEXE_RE = re.compile(r"^\s*\[(RETENIR|PIEGE|MNEMO)\]\s*(.*)$", re.IGNORECASE)
_REFLEXE_KIND = {"RETENIR": "a_retenir", "PIEGE": "piege", "MNEMO": "mnemo"}


# ── Helpers de parsing ────────────────────────────────────────────────────────
def _split_title_resume(body: str) -> tuple[str, str]:
    """Sépare « **Titre** : résumé » en (titre, résumé)."""
    body = body.strip()
    match = _TITLE_RE.match(body)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    if ":" in body:
        title, _, resume = body.partition(":")
        return title.strip().strip("*"), resume.strip()
    return body.strip("*").strip(), ""


def _normalize_indentation(text: str) -> str:
    """Réindente les listes à puces sur 4 espaces/niveau pour Markdown."""
    lines = text.split("\n")
    out: list[str] = []
    indent_stack: list[int] = []

    for raw_line in lines:
        stripped = raw_line.lstrip(" \t")
        if not stripped:
            out.append("")
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        is_bullet = bool(re.match(r"[-*+]\s+", stripped)) or bool(re.match(r"\d+\.\s+", stripped))

        if is_bullet:
            while indent_stack and indent < indent_stack[-1]:
                indent_stack.pop()
            if not indent_stack or indent > indent_stack[-1]:
                indent_stack.append(indent)
            level = len(indent_stack) - 1
            out.append("    " * level + stripped)
        else:
            level = max(0, len(indent_stack) - 1)
            out.append("    " * level + stripped if indent_stack else stripped)
    return "\n".join(out).strip()


def parse_plan(plan_md: str) -> list[PlanPartie]:
    """Transforme le Markdown de l'étape 1 en liste de `PlanPartie`."""
    parties: list[PlanPartie] = []
    current: PlanPartie | None = None

    for raw_line in plan_md.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue

        roman = _ROMAN_RE.match(line)
        letter = _LETTER_RE.match(line)
        indent = len(raw_line) - len(raw_line.lstrip(" "))

        if roman and indent <= 3:
            title, resume = _split_title_resume(roman.group(2))
            current = PlanPartie(numero=roman.group(1), titre=title, resume=resume)
            parties.append(current)
        elif letter and current is not None:
            title, resume = _split_title_resume(letter.group(2))
            current.sous_parties.append(
                PlanSousPartie(lettre=letter.group(1), titre=title, resume=resume)
            )
        elif current is not None:
            # Ligne de continuation : rattachée au dernier résumé.
            extra = line.strip().lstrip("-*").strip()
            if current.sous_parties:
                last = current.sous_parties[-1]
                last.resume = f"{last.resume} {extra}".strip()
            else:
                current.resume = f"{current.resume} {extra}".strip()
    return parties


def parse_section(section_md: str, numero: str, fallback_title: str) -> Partie:
    """Transforme le Markdown d'une partie (étape 2) en `Partie` (tableaux).

    Chaque sous-partie (A., B., …) devient un tableau catégorisé ; `[LIGNE]`
    ouvre une ligne « concept | détail », `[RETENIR]/[PIEGE]/[MNEMO]` une
    ligne-réflexe pleine largeur.
    """
    lines = section_md.splitlines()
    partie = Partie(numero=numero, titre=fallback_title)
    sous_parties: list[SousPartie] = []
    current_sp: SousPartie | None = None
    current_row: FicheRow | None = None
    detail_lines: list[str] = []
    title_found = False

    def _flush_row() -> None:
        nonlocal current_row
        if current_row is not None:
            current_row.detail_md = _normalize_indentation("\n".join(detail_lines))
        detail_lines.clear()
        current_row = None

    def _ensure_sp() -> SousPartie:
        nonlocal current_sp
        if current_sp is None:
            current_sp = SousPartie(lettre="A", titre=partie.titre)
            sous_parties.append(current_sp)
        return current_sp

    for raw_line in lines:
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped and current_row is None:
            continue

        roman = _ROMAN_RE.match(line)
        letter = _LETTER_RE.match(line)
        ligne = _LIGNE_RE.match(line)
        reflexe = _REFLEXE_RE.match(line)
        is_bullet = bool(re.match(r"[-*+]\s", stripped))

        # Titre de la grande partie (première occurrence).
        if not title_found and roman and not is_bullet and not ligne and not reflexe:
            title, _ = _split_title_resume(roman.group(2))
            partie.titre = title or fallback_title
            title_found = True
            continue

        # Entête de sous-partie (A., B., …).
        if letter and not is_bullet and not ligne and not reflexe:
            _flush_row()
            title, _ = _split_title_resume(letter.group(2))
            current_sp = SousPartie(lettre=letter.group(1), titre=title)
            sous_parties.append(current_sp)
            continue

        # Ligne-réflexe (à retenir / piège / mnémo).
        if reflexe:
            _flush_row()
            kind = _REFLEXE_KIND[reflexe.group(1).upper()]
            current_row = FicheRow(concept="", kind=kind)
            _ensure_sp().rows.append(current_row)
            if reflexe.group(2).strip():
                detail_lines.append(reflexe.group(2).strip())
            continue

        # Nouvelle ligne de tableau standard.
        if ligne:
            _flush_row()
            concept = ligne.group(1).strip().strip("*").strip()
            current_row = FicheRow(concept=concept)
            _ensure_sp().rows.append(current_row)
            continue

        # Ligne de contenu (détail de la colonne droite).
        if current_row is not None:
            detail_lines.append(line)
        elif stripped:
            current_row = FicheRow(concept="Généralités")
            _ensure_sp().rows.append(current_row)
            detail_lines.append(line)

    _flush_row()

    for sous in sous_parties:
        sous.rows = [r for r in sous.rows if r.detail_md.strip() or r.concept.strip()]
    partie.sous_parties = [sous for sous in sous_parties if sous.rows]

    # Repli : aucun contenu structuré exploitable.
    if not partie.sous_parties:
        body = _normalize_indentation(section_md)
        partie.sous_parties = [
            SousPartie(
                lettre="A",
                titre=partie.titre,
                rows=[FicheRow(concept="Points clés", detail_md=body)],
            )
        ]
    return partie


def _split_heading_blocks(text: str) -> list[tuple[str, list[str]]]:
    """Découpe un Markdown en blocs (titre « ### », lignes de contenu)."""
    blocks: list[tuple[str, list[str]]] = []
    current_title = ""
    current_lines: list[str] = []
    for raw_line in text.splitlines():
        heading = _HEADING_RE.match(raw_line)
        if heading:
            if current_title or current_lines:
                blocks.append((current_title, current_lines))
            current_title = heading.group(1).strip().strip("*")
            current_lines = []
        else:
            current_lines.append(raw_line)
    if current_title or current_lines:
        blocks.append((current_title, current_lines))
    return blocks


def parse_synthesis(
    synthesis_md: str,
) -> tuple[list[TableauSynthese], TableauSynthese | None, list[str]]:
    """Sépare tableaux de synthèse, chiffres-clés et points à retenir (étape 3)."""
    tableaux: list[TableauSynthese] = []
    chiffres: TableauSynthese | None = None
    points: list[str] = []

    for title, body_lines in _split_heading_blocks(synthesis_md):
        body = "\n".join(body_lines).strip()
        normalized = strip_accents(title).lower()
        if "points a retenir" in normalized or "retenir absolument" in normalized:
            for line in body_lines:
                item = line.strip()
                if item.startswith(("-", "*", "•")):
                    cleaned = item.lstrip("-*• ").strip()
                    if cleaned:
                        points.append(cleaned)
        elif "chiffre" in normalized and "|" in body:
            chiffres = TableauSynthese(titre="Chiffres-clés", markdown=body)
        elif "|" in body:
            tableaux.append(TableauSynthese(titre=title or "Tableau de synthèse",
                                            markdown=body))

    # Repli : pas de titres « ### » mais des tableaux bruts présents.
    if not tableaux and chiffres is None and "|" in synthesis_md:
        tableaux.append(TableauSynthese(titre="Tableaux de synthèse",
                                        markdown=synthesis_md.strip()))
    return tableaux, chiffres, points


def parse_extras(extras_md: str) -> str:
    """Extrait la fiche éclair (étape 4)."""
    for title, body_lines in _split_heading_blocks(extras_md):
        body = "\n".join(body_lines).strip()
        if body and "fiche eclair" in strip_accents(title).lower():
            return body
    # Repli : pas de titre « ### » mais du contenu présent.
    return extras_md.strip()


# ── Placement des images ──────────────────────────────────────────────────────
def _similarity(a: str, b: str) -> float:
    """Similarité 0-1 entre deux libellés (insensible aux accents/casse)."""
    return SequenceMatcher(None, strip_accents(a).lower(), strip_accents(b).lower()).ratio()


def _place_images(parties: list[Partie], images: list[AnalyzedImage]) -> None:
    """Affecte chaque image pertinente à la sous-partie la plus proche."""
    targets: list[tuple[SousPartie, str]] = []
    for partie in parties:
        for sp in partie.sous_parties:
            context = f"{partie.titre} {sp.titre}"
            targets.append((sp, context))
    if not targets:
        return

    for image in images:
        if not image.is_relevant or image.saved_path is None:
            continue
        needle = f"{image.section_suggeree} {image.concept_lie}".strip()
        best_sp, best_score = targets[0][0], -1.0
        for sp, context in targets:
            score = max(
                _similarity(needle, context),
                _similarity(image.section_suggeree, context),
            )
            if score > best_score:
                best_sp, best_score = sp, score
        best_sp.images.append(image)


def _persist_images(images: list[AnalyzedImage], work_dir: Path) -> None:
    """Enregistre les images pertinentes sur disque et numérote les figures."""
    work_dir.mkdir(parents=True, exist_ok=True)
    figure = 0
    for image in images:
        if not image.is_relevant:
            continue
        figure += 1
        image.figure_number = figure
        png_bytes = normalize_image_to_png(image.source)
        path = work_dir / f"figure_{figure:02d}.png"
        path.write_bytes(png_bytes)
        image.saved_path = path


# ── Orchestration ─────────────────────────────────────────────────────────────
async def build_fiche(
    extracted: ExtractedDocument,
    *,
    matiere: str,
    fallback_nom_cours: str,
    client: AsyncAnthropic,
    settings: Settings,
    work_dir: Path,
    on_progress: ProgressCallback | None = None,
) -> FicheData:
    """Exécute le pipeline IA complet et renvoie une `FicheData` assemblée."""
    logger = get_logger()

    def _progress(message: str) -> None:
        if on_progress is not None:
            on_progress(message)

    processor = AIProcessor(client, settings.writer_model, settings)
    processor.load_course(extracted.text)
    analyzer = ImageAnalyzer(client, settings.vision_model, settings)

    # Étape 1 — plan + nom du cours.
    _progress("plan")
    plan_result = await processor.generate_plan()
    nom_cours = plan_result.nom_cours or titlecase_fr(fallback_nom_cours)
    logger.debug("Cours identifié : %s", nom_cours)

    plan_parties = parse_plan(plan_result.plan_md)
    if not plan_parties:
        plan_parties = [PlanPartie(numero="I", titre=nom_cours,
                                   resume="Contenu intégral du cours.")]

    # Analyse vision lancée en parallèle de la rédaction (étapes 2-3).
    vision_task = asyncio.create_task(
        analyzer.analyze_images(extracted.images, matiere, nom_cours)
    )

    # Étape 2 — rédaction exhaustive partie par partie.
    parties: list[Partie] = []
    for index, plan_partie in enumerate(plan_parties, start=1):
        _progress(f"rédaction {index}/{len(plan_parties)}")
        section_md = await processor.write_section(plan_result.plan_md, plan_partie.numero)
        parties.append(parse_section(section_md, plan_partie.numero, plan_partie.titre))

    # Étape 3 — tableaux de synthèse, chiffres-clés, points à retenir.
    _progress("synthèse")
    synthesis_md = await processor.generate_synthesis()
    tableaux, chiffres_cles, points_cles = parse_synthesis(synthesis_md)

    # Étape 4 — fiche éclair.
    _progress("fiche éclair")
    extras_md = await processor.generate_extras()
    fiche_eclair_md = parse_extras(extras_md)

    # Récupération de l'analyse vision et placement des images.
    _progress("images")
    analyzed_images = await vision_task
    _persist_images(analyzed_images, work_dir)
    _place_images(parties, analyzed_images)

    usage = processor.usage
    usage.add(analyzer.usage)

    fiche = FicheData(
        matiere=titlecase_fr(matiere),
        nom_cours=nom_cours,
        annee=settings.year,
        item=plan_result.item,
        plan=plan_parties,
        parties=parties,
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[img for img in analyzed_images if img.is_relevant],
        fiche_numero=_fiche_numero(plan_result.item),
        usage=usage,
    )
    return fiche


def _fiche_numero(item: str) -> str:
    """Extrait un numéro de fiche depuis l'item ECN si disponible."""
    match = re.search(r"\d+", item or "")
    return f"Item {match.group(0)}" if match else ""


def output_basename(matiere: str, nom_cours: str, year: str) -> str:
    """Construit le nom de fichier de sortie (sans extension)."""
    return f"{slugify(titlecase_fr(matiere))}_{slugify(nom_cours)}_{year}"

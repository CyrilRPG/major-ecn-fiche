"""Assemble une fiche depuis les fichiers .md produits par les agents et rend en PDF.

Usage :
    python scripts/render_fiche.py <nom_specialite>

    Cherche les fichiers dans output/.work/<slug>/ :
      - plan.md      (étape 1 - plan)
      - section_I.md, section_II.md, ...  (étape 2 - sections)
      - synthesis.md  (étape 3 - synthèse)
      - eclair.md     (étape 4 - fiche éclair)
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

# Ensure stdout can handle UTF-8 (Windows cp1252 chokes on emoji characters).
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from major_ecn.config import LOGO_PATH, MIN_IMAGE_DIMENSION_PX, Settings
from major_ecn.content_builder import (
    parse_extras,
    parse_plan,
    parse_section,
    parse_synthesis,
)
from major_ecn.models import (
    AnalyzedImage,
    ExtractedImage,
    FicheData,
    PlanPartie,
    UsageStats,
)
from major_ecn.pdf_extractor import normalize_image_to_png
from major_ecn.pdf_generator import render_pdf
from major_ecn.utils.slugify import slugify


def extract_tag(raw: str, name: str) -> str:
    match = re.search(rf"<{name}>\s*(.*?)\s*</{name}>", raw, re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else ""


def _load_image_captions(work_dir: Path) -> dict[int, dict]:
    """Charge les légendes d'images depuis le fichier JSON produit par l'agent d'analyse."""
    import json
    captions_file = work_dir / "image_captions.json"
    if captions_file.exists():
        try:
            data = json.loads(captions_file.read_text(encoding="utf-8"))
            return {entry["page"]: entry for entry in data if entry.get("relevant", True)}
        except Exception:
            pass
    return {}


def _extract_and_place_images(
    pdf_path: Path, parties: list, work_dir: Path, max_images: int = 30
) -> list[AnalyzedImage]:
    """Extrait les images du PDF source et les distribue par page dans les sections.

    Stratégie : on découpe les pages du PDF proportionnellement entre les parties,
    puis chaque image est affectée à la sous-partie correspondant à sa page.
    """
    import fitz

    if not pdf_path.exists() or not parties:
        return []

    try:
        doc = fitz.open(str(pdf_path))
    except Exception as e:
        print(f"  [WARN] Ouverture PDF impossible : {e}")
        return []

    total_pages = doc.page_count
    if total_pages == 0:
        doc.close()
        return []

    # Extraire toutes les images significatives et non-dupliquées.
    raw_images: list[tuple[int, ExtractedImage]] = []
    seen_sha: set[str] = set()

    for page_idx in range(total_pages):
        page = doc[page_idx]
        for img_idx, img_info in enumerate(page.get_images(full=True)):
            xref = img_info[0]
            try:
                raw = doc.extract_image(xref)
            except Exception:
                continue
            data: bytes = raw.get("image", b"")
            if not data:
                continue
            w, h = int(raw.get("width", 0)), int(raw.get("height", 0))
            # Filtrer agressivement : au moins 200px de côté pour être pédagogique.
            if w < 200 or h < 200:
                continue
            # Filtrer les images très allongées (barres, lignes, bandeaux).
            ratio = max(w, h) / max(min(w, h), 1)
            if ratio > 5:
                continue
            sha = hashlib.sha1(data).hexdigest()
            if sha in seen_sha:
                continue
            seen_sha.add(sha)
            raw_images.append((
                page_idx,
                ExtractedImage(data=data, ext=raw.get("ext", "png"),
                               page=page_idx + 1, index=img_idx,
                               width=w, height=h, sha=sha),
            ))

    doc.close()

    if not raw_images:
        return []

    # Charger les légendes produites par l'agent d'analyse (si disponible).
    captions = _load_image_captions(work_dir)

    # Filtrer par le fichier de captions : ne garder QUE les images marquées pertinentes.
    if captions:
        raw_images = [
            (pi, img) for pi, img in raw_images
            if img.page in captions and captions[img.page].get("relevant", True)
        ]

    # Limiter au nombre max.
    raw_images = raw_images[:max_images]

    # Calculer les tranches de pages pour chaque partie.
    n_parties = len(parties)
    pages_per_partie = total_pages / n_parties

    # Persister les images sur disque et créer les AnalyzedImage.
    figures_dir = work_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    all_images: list[AnalyzedImage] = []
    fig_num = 0

    for page_idx, ext_img in raw_images:
        fig_num += 1
        # Persister en PNG.
        try:
            png_bytes = normalize_image_to_png(ext_img)
        except Exception:
            png_bytes = ext_img.data
        fig_path = figures_dir / f"figure_{fig_num:02d}.png"
        fig_path.write_bytes(png_bytes)

        # Légende : du fichier JSON si dispo, sinon description générique.
        cap = captions.get(ext_img.page, {})
        description = cap.get("description", "")
        concept = cap.get("concept", "")
        section = cap.get("section", "")

        analyzed = AnalyzedImage(
            source=ext_img,
            description=description,
            concept_lie=concept,
            pertinence=7,
            type=cap.get("type", "schema"),
            section_suggeree=section,
            saved_path=fig_path,
            figure_number=fig_num,
        )
        all_images.append(analyzed)

        # Affecter via section_suggeree (si dispo) ou par position de page.
        placed = False
        if section:
            # Chercher la meilleure sous-partie par similarité de titre.
            from major_ecn.content_builder import _similarity
            best_sp, best_score = None, -1.0
            for partie in parties:
                for sp in partie.sous_parties:
                    ctx = f"{partie.titre} {sp.titre}"
                    score = _similarity(section, ctx)
                    if score > best_score:
                        best_sp, best_score = sp, score
            if best_sp and best_score > 0.3:
                best_sp.images.append(analyzed)
                placed = True

        if not placed:
            # Placement par position de page.
            partie_idx = min(int(page_idx / pages_per_partie), n_parties - 1)
            partie = parties[partie_idx]
            if partie.sous_parties:
                n_sp = len(partie.sous_parties)
                fraction = (page_idx - partie_idx * pages_per_partie) / pages_per_partie
                sp_idx = min(int(fraction * n_sp), n_sp - 1)
                partie.sous_parties[sp_idx].images.append(analyzed)

    print(f"  [IMG] {len(all_images)} images placees dans {n_parties} parties")
    return all_images


def build_and_render(specialty: str) -> Path:
    """Assemble la FicheData depuis les .md et génère le PDF."""
    slug = slugify(specialty)
    work_dir = PROJECT_ROOT / "output" / ".work" / slug
    settings = Settings.load(env_file=PROJECT_ROOT / ".env")

    if not work_dir.exists():
        raise FileNotFoundError(f"Dossier de travail introuvable : {work_dir}")

    # 1. Plan.
    plan_md = (work_dir / "plan.md").read_text(encoding="utf-8")
    nom_cours = extract_tag(plan_md, "nom_cours") or specialty
    item = extract_tag(plan_md, "item")
    plan_clean = re.sub(r"<[a-z_]+>.*?</[a-z_]+>", "", plan_md, flags=re.DOTALL).strip()
    plan_parties = parse_plan(plan_clean)
    # Ne garder que les VRAIES grandes parties (chiffres romains I-VII),
    # pas les lettres (A, B, C, D, L, M) que le parser confond avec des romains.
    _VALID_ROMAN = {"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"}
    plan_parties = [p for p in plan_parties if p.numero in _VALID_ROMAN]
    # Limiter à 7 pour que la légende reste visible sur la page de garde.
    plan_parties = plan_parties[:7]
    if not plan_parties:
        plan_parties = [PlanPartie(numero="I", titre=specialty)]

    # 2. Sections.
    parties = []
    for plan_partie in plan_parties:
        section_file = work_dir / f"section_{plan_partie.numero}.md"
        if section_file.exists():
            section_md = section_file.read_text(encoding="utf-8")
        else:
            print(f"  [WARN] Section {plan_partie.numero} manquante, skip")
            continue
        parties.append(parse_section(section_md, plan_partie.numero, plan_partie.titre))

    if not parties:
        raise RuntimeError(f"Aucune section trouvée pour {specialty}")

    # 3. Synthèse.
    synth_file = work_dir / "synthesis.md"
    if synth_file.exists():
        synthesis_md = synth_file.read_text(encoding="utf-8")
        tableaux, chiffres_cles, points_cles = parse_synthesis(synthesis_md)
    else:
        tableaux, chiffres_cles, points_cles = [], None, []

    # 4. Fiche éclair.
    eclair_file = work_dir / "eclair.md"
    if eclair_file.exists():
        eclair_md = eclair_file.read_text(encoding="utf-8")
        fiche_eclair_md = parse_extras(eclair_md)
    else:
        fiche_eclair_md = ""

    # 5. Images — extraire du PDF source et distribuer par page.
    pdf_path = PROJECT_ROOT / "inputs" / f"{specialty}.pdf"
    images = _extract_and_place_images(pdf_path, parties, work_dir)

    # 6. Assemblage FicheData.
    fiche = FicheData(
        matiere="Médecine Générale",
        nom_cours=specialty,
        annee=settings.year,
        item=item,
        plan=plan_parties,
        parties=parties,
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[img for img in images if img.is_relevant],
        fiche_numero="",
        usage=UsageStats(),
    )

    # 7. Rendu PDF.
    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / f"Medecine_generale_{slug}_{settings.year}.pdf"
    render_pdf(fiche, pdf_out)
    size_mb = pdf_out.stat().st_size / 1e6
    print(f"  [OK] PDF : {pdf_out.name} ({size_mb:.1f} MB)")
    return pdf_out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/render_fiche.py <nom_specialite>")
        sys.exit(1)
    build_and_render(sys.argv[1])

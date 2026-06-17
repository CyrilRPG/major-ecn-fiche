"""Rend les 22 PDFs des fiches de cardiologie (1 par item ECN).

Pour chaque scripts/generate_item_<num>.py :
1. Importe build_fiche()
2. Extrait les images du candidates_images/ correspondant
3. Filtre par image_captions.json
4. Place les images dans les sous-parties
5. Rend le PDF dans output/fiches/cardiologie/
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from major_ecn.models import AnalyzedImage, ExtractedImage
from major_ecn.pdf_extractor import normalize_image_to_png
from major_ecn.pdf_generator import render_pdf
from major_ecn.utils.slugify import slugify


# Items à traiter (22 au total)
ITEMS = [
    "152", "153", "203", "221", "222", "223", "224", "225", "226",
    "230", "231", "232", "233", "234", "235", "236", "237", "238",
    "330", "331", "339", "342",
]


def _load_build_fiche(item_num: str):
    """Importe build_fiche() depuis scripts/generate_item_<num>.py."""
    script = PROJECT_ROOT / "scripts" / f"generate_item_{item_num}.py"
    if not script.exists():
        return None
    spec = importlib.util.spec_from_file_location(f"gen_item_{item_num}", str(script))
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        print(f"    ERREUR import: {e}")
        return None
    fn = getattr(mod, "build_fiche", None)
    return fn


def _load_captions(item_num: str) -> dict[int, dict]:
    """Charge image_captions.json pour un item."""
    cap_file = PROJECT_ROOT / "output" / ".work" / "cardio" / f"item_{item_num}" / "image_captions.json"
    if not cap_file.exists():
        return {}
    for enc in ("utf-8-sig", "utf-8"):
        try:
            data = json.loads(cap_file.read_text(encoding=enc))
            return {e["page"]: e for e in data if e.get("relevant", True)}
        except Exception:
            continue
    return {}


def _extract_image_data(img_path: Path) -> bytes:
    """Lit un PNG depuis le disque."""
    return img_path.read_bytes()


def _place_images_on_fiche(fiche, item_num: str, max_images: int) -> int:
    """Extrait les images candidates et les place dans les sous-parties."""
    img_dir = PROJECT_ROOT / "output" / ".work" / "cardio" / f"item_{item_num}" / "candidate_images"
    if not img_dir.exists() or not fiche.parties:
        return 0

    captions = _load_captions(item_num)
    if not captions:
        # Pas de captions = pas d'images filtrées
        return 0

    # Lister tous les fichiers d'images candidats avec leur numéro
    img_files = []
    for f in sorted(img_dir.glob("p*.png")):
        # Extraire le numéro (p001 -> 1)
        m = re.match(r"p(\d+)_", f.name)
        if not m:
            continue
        page = int(m.group(1))
        # Filtrer par captions
        cap = captions.get(page)
        if not cap or not cap.get("relevant", True):
            continue
        img_files.append((page, f, cap))

    # Limiter
    img_files = img_files[:max_images]

    if not img_files:
        return 0

    # Préparer le dossier final
    fig_dir = PROJECT_ROOT / "output" / ".work" / "cardio" / f"item_{item_num}" / "figures_final"
    fig_dir.mkdir(parents=True, exist_ok=True)

    all_images = []
    n_parties = len(fiche.parties)

    for fig_num, (page, img_path, cap) in enumerate(img_files, start=1):
        # Copier l'image
        fig_path = fig_dir / f"fig_{fig_num:02d}.png"
        fig_path.write_bytes(img_path.read_bytes())

        # Créer un ExtractedImage minimal
        png_bytes = img_path.read_bytes()
        ext_img = ExtractedImage(
            data=png_bytes, ext="png",
            page=page, index=fig_num,
            width=cap.get("w", 800), height=cap.get("h", 600),
            sha=hashlib.sha1(png_bytes).hexdigest(),
        )

        analyzed = AnalyzedImage(
            source=ext_img,
            description=cap.get("description", ""),
            concept_lie=cap.get("concept", ""),
            pertinence=8,
            type=cap.get("type", "schema"),
            section_suggeree=cap.get("section", ""),
            saved_path=fig_path,
            figure_number=fig_num,
        )
        all_images.append(analyzed)

        # Placement par similarité de section
        placed = False
        section = cap.get("section", "")
        if section:
            from difflib import SequenceMatcher
            best_sp, best_score = None, 0.0
            for partie in fiche.parties:
                for sp in partie.sous_parties:
                    ctx = f"{partie.titre} {sp.titre}".lower()
                    score = SequenceMatcher(None, section.lower(), ctx).ratio()
                    if score > best_score:
                        best_sp, best_score = sp, score
            if best_sp and best_score > 0.25:
                best_sp.images.append(analyzed)
                placed = True

        # Fallback : placement proportionnel par numéro de page
        if not placed:
            # Distribuer les images uniformément
            partie_idx = min((fig_num - 1) * n_parties // len(img_files), n_parties - 1)
            partie = fiche.parties[partie_idx]
            if partie.sous_parties:
                sp_idx = (fig_num - 1) % len(partie.sous_parties)
                partie.sous_parties[sp_idx].images.append(analyzed)

    fiche.images = [img for img in all_images if img.is_relevant]
    return len(fiche.images)


def process_item(item_num: str) -> bool:
    """Génère le PDF pour un item donné."""
    print(f"\n  [Item {item_num}]")

    # 0. Validation
    script_path = PROJECT_ROOT / "scripts" / f"generate_item_{item_num}.py"
    if script_path.exists():
        try:
            sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
            from validate_fiche import validate
            result = validate(script_path, fix=True)
            if result.fixes_applied:
                print(f"    Auto-fix: {', '.join(result.fixes_applied)}")
            if result.errors:
                print(f"    ALERTES: {'; '.join(result.errors)}")
        except ImportError:
            pass

    # 1. Charger la fiche
    build_fn = _load_build_fiche(item_num)
    if build_fn is None:
        print(f"    SKIP: generate_item_{item_num}.py introuvable ou cassé")
        return False

    try:
        fiche = build_fn()
    except Exception as e:
        print(f"    ERREUR build: {e}")
        return False

    # 2. Déterminer le nombre max d'images selon la taille de la fiche
    total_rows = sum(len(sp.rows) for p in fiche.parties for sp in p.sous_parties)
    if total_rows < 30:
        max_images = 5
    elif total_rows < 70:
        max_images = 15
    else:
        max_images = 25

    # 3. Placer les images
    n_images = _place_images_on_fiche(fiche, item_num, max_images)
    print(f"    {n_images} images placées (max {max_images})")

    # 4. Rendre le PDF
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    # Nom du fichier : Cardiologie_Item-XXX_titre-slug_2025-2026.pdf
    title_slug = slugify(fiche.nom_cours.replace(f"Item {item_num} - ", ""))[:40]
    pdf_out = output_dir / f"Cardiologie_Item-{item_num}_{title_slug}_2025-2026.pdf"

    try:
        render_pdf(fiche, pdf_out)
        size_mb = pdf_out.stat().st_size / 1e6
        print(f"    PDF: {pdf_out.name} ({size_mb:.1f} MB)")
        return True
    except Exception as e:
        print(f"    ERREUR render: {e}")
        return False


def main():
    print("=" * 60)
    print(f"  RENDU DES {len(ITEMS)} FICHES DE CARDIOLOGIE")
    print("=" * 60)

    ok, ko = 0, 0
    failed = []
    for item_num in ITEMS:
        if process_item(item_num):
            ok += 1
        else:
            ko += 1
            failed.append(item_num)

    print(f"\n{'=' * 60}")
    print(f"  {ok}/{ok + ko} fiches générées")
    if failed:
        print(f"  Échecs : items {', '.join(failed)}")
    print(f"  Dossier : output/fiches/cardiologie/")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()

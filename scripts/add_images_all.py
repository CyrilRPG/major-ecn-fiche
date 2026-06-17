"""Ajoute les images pertinentes du PDF source à chaque fiche et régénère les PDFs.

Pour chaque spécialité :
1. Importe build_fiche() depuis scripts/generate_<slug>.py
2. Extrait les images du PDF source (inputs/<Specialite>.pdf)
3. Filtre par image_captions.json si disponible, sinon par taille/ratio
4. Place dans les sous-parties correspondantes
5. Régénère le PDF dans output/fiches/
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

# Fix Windows encoding
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import fitz
from major_ecn.models import AnalyzedImage, ExtractedImage
from major_ecn.pdf_extractor import normalize_image_to_png
from major_ecn.pdf_generator import render_pdf
from major_ecn.utils.slugify import slugify


SPECIALTIES = [
    "Cardiologie", "Endocrinologie", "Gériatrie", "Gynécologie",
    "Hématologie", "Hépato-gastro-entérologie", "Infectiologie",
    "Médecine interne", "Néphrologie", "Neurologie",
    "Ophtalmologie", "ORL", "Pharmacologie", "Psychiatrie",
    "Pédiatrie", "Réanimation", "Rhumatologie", "Urologie",
]


def _load_build_fiche(slug: str):
    """Importe dynamiquement build_fiche() depuis scripts/generate_<slug>.py."""
    script = PROJECT_ROOT / "scripts" / f"generate_{slug}.py"
    if not script.exists():
        return None
    spec = importlib.util.spec_from_file_location(f"gen_{slug}", str(script))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # Cherche build_fiche ou build_pneumologie_fiche ou build_<slug>_fiche
    for name in ("build_fiche", f"build_{slug}_fiche", "build"):
        fn = getattr(mod, name, None)
        if fn:
            return fn
    # Cherche toute fonction build_*
    for name in dir(mod):
        if name.startswith("build") and callable(getattr(mod, name)):
            return getattr(mod, name)
    return None


def _load_captions(slug: str) -> dict[int, dict]:
    """Charge image_captions.json si disponible."""
    cap_file = PROJECT_ROOT / "output" / ".work" / slug / "image_captions.json"
    if cap_file.exists():
        try:
            data = json.loads(cap_file.read_text(encoding="utf-8-sig"))
            return {e["page"]: e for e in data if e.get("relevant", True)}
        except Exception:
            try:
                data = json.loads(cap_file.read_text(encoding="utf-8"))
                return {e["page"]: e for e in data if e.get("relevant", True)}
            except Exception:
                pass
    return {}


def _extract_images(pdf_path: Path, captions: dict, max_images: int = 25):
    """Extrait les images pertinentes du PDF source."""
    if not pdf_path.exists():
        return []

    doc = fitz.open(str(pdf_path))
    raw_images = []
    seen = set()

    for pi in range(doc.page_count):
        page = doc[pi]
        for ii, info in enumerate(page.get_images(full=True)):
            xref = info[0]
            try:
                raw = doc.extract_image(xref)
            except Exception:
                continue
            data = raw.get("image", b"")
            if not data:
                continue
            w, h = int(raw.get("width", 0)), int(raw.get("height", 0))
            if w < 200 or h < 200:
                continue
            ratio = max(w, h) / max(min(w, h), 1)
            if ratio > 5:
                continue
            sha = hashlib.sha1(data).hexdigest()
            if sha in seen:
                continue
            seen.add(sha)
            raw_images.append((pi, ExtractedImage(
                data=data, ext=raw.get("ext", "png"),
                page=pi + 1, index=ii, width=w, height=h, sha=sha,
            )))

    doc.close()

    # Filtrer par captions si disponibles
    if captions:
        raw_images = [
            (pi, img) for pi, img in raw_images
            if img.page in captions
        ]

    return raw_images[:max_images]


def _place_images(fiche, pdf_path: Path, slug: str):
    """Extrait, persiste et place les images dans la fiche."""
    captions = _load_captions(slug)
    raw_images = _extract_images(pdf_path, captions)

    if not raw_images or not fiche.parties:
        return

    # Persist
    fig_dir = PROJECT_ROOT / "output" / ".work" / slug / "figures_final"
    fig_dir.mkdir(parents=True, exist_ok=True)

    total_pages = max(img.page for _, img in raw_images) + 1
    n_parties = len(fiche.parties)
    pages_per_partie = total_pages / n_parties

    all_images = []
    fig_num = 0

    for page_idx, ext_img in raw_images:
        fig_num += 1
        try:
            png = normalize_image_to_png(ext_img)
        except Exception:
            png = ext_img.data
        fig_path = fig_dir / f"fig_{fig_num:02d}.png"
        fig_path.write_bytes(png)

        cap = captions.get(ext_img.page, {})
        desc = cap.get("description", f"Illustration du cours")
        concept = cap.get("concept", "")
        section = cap.get("section", "")

        analyzed = AnalyzedImage(
            source=ext_img,
            description=desc,
            concept_lie=concept,
            pertinence=7,
            type=cap.get("type", "schema"),
            section_suggeree=section,
            saved_path=fig_path,
            figure_number=fig_num,
        )
        all_images.append(analyzed)

        # Place par similarité de section si section_suggeree est dispo
        placed = False
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

        # Fallback : placement par position de page
        if not placed:
            partie_idx = min(int(page_idx / pages_per_partie), n_parties - 1)
            partie = fiche.parties[partie_idx]
            if partie.sous_parties:
                n_sp = len(partie.sous_parties)
                frac = (page_idx - partie_idx * pages_per_partie) / pages_per_partie
                sp_idx = min(int(frac * n_sp), n_sp - 1)
                partie.sous_parties[sp_idx].images.append(analyzed)

    fiche.images = [img for img in all_images if img.is_relevant]
    print(f"    {len(fiche.images)} images placees")


def process_one(specialty: str) -> bool:
    """Traite une spécialité : valide, charge fiche, ajoute images, rend PDF."""
    slug = slugify(specialty)
    print(f"\n  [{specialty}]")

    # 0. Validation automatique du script
    script_path = PROJECT_ROOT / "scripts" / f"generate_{slug}.py"
    if script_path.exists():
        try:
            from validate_fiche import validate
            result = validate(script_path, fix=True)
            if result.fixes_applied:
                print(f"    Auto-fix: {', '.join(result.fixes_applied)}")
            if result.errors:
                print(f"    ALERTES: {'; '.join(result.errors)}")
        except ImportError:
            pass  # validate_fiche.py pas dans le path

    # 1. Charger la fiche
    build_fn = _load_build_fiche(slug)
    if build_fn is None:
        print(f"    SKIP: pas de script generate_{slug}.py")
        return False

    try:
        fiche = build_fn()
    except Exception as e:
        print(f"    ERREUR build: {e}")
        return False

    # 2. Ajouter les images
    pdf_path = PROJECT_ROOT / "inputs" / f"{specialty}.pdf"
    if not pdf_path.exists():
        # Essayer sans accents
        for p in (PROJECT_ROOT / "inputs").glob("*.pdf"):
            if slugify(p.stem) == slug:
                pdf_path = p
                break
    _place_images(fiche, pdf_path, slug)

    # 3. Rendre le PDF
    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / f"Medecine_generale_{slug.replace('-', '_').title().replace('_', '-')}_2025-2026.pdf"
    # Normaliser le nom
    nice_name = specialty.replace("é", "e").replace("è", "e").replace("ê", "e") \
                         .replace("à", "a").replace("ô", "o").replace("î", "i") \
                         .replace("ù", "u").replace("û", "u")
    pdf_out = output_dir / f"Medecine_generale_{nice_name}_2025-2026.pdf"

    try:
        render_pdf(fiche, pdf_out)
        size = pdf_out.stat().st_size / 1e6
        print(f"    PDF: {pdf_out.name} ({size:.1f} MB)")
        return True
    except Exception as e:
        print(f"    ERREUR render: {e}")
        return False


def main():
    print("=" * 60)
    print("  AJOUT D'IMAGES ET REGENERATION DES 18 FICHES")
    print("=" * 60)

    ok, ko = 0, 0
    for specialty in SPECIALTIES:
        if process_one(specialty):
            ok += 1
        else:
            ko += 1

    print(f"\n{'=' * 60}")
    print(f"  {ok}/{ok + ko} fiches regenerees avec images")
    if ko:
        print(f"  {ko} en echec")
    print(f"  Dossier: output/fiches/")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()

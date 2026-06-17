"""Fiche de revision Pneumothorax (Medecine Generale, ~5 pages)."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from major_ecn.models import (
    AnalyzedImage,
    ExtractedImage,
    FicheData,
    FicheRow,
    Partie,
    PlanPartie,
    PlanSousPartie,
    SousPartie,
    TableauSynthese,
    UsageStats,
)
from major_ecn.config import LOGO_PATH
from major_ecn.pdf_generator import render_pdf


_SOURCE_IMAGES = [
    {
        "file": "pneumothorax_tdm.png",
        "partie": 0,
        "sp": 2,  # C. Imagerie
        "desc": "TDM thoracique : pneumothorax bilatéral",
        "concept": "Imagerie pneumothorax",
        "type": "imagerie",
    },
    {
        "file": "pneumothorax_radio.png",
        "partie": 0,
        "sp": 2,  # C. Imagerie
        "desc": "Radiographie de thorax : pneumothorax",
        "concept": "Imagerie pneumothorax",
        "type": "photo_clinique",  # → small (float-right) pour économie de place
    },
]


def build_fiche() -> FicheData:
    plan = [
        PlanPartie(
            numero="I",
            titre="Pneumothorax",
            sous_parties=[
                PlanSousPartie(lettre="A", titre="Definition et classification"),
                PlanSousPartie(lettre="B", titre="Clinique"),
                PlanSousPartie(lettre="C", titre="Imagerie"),
                PlanSousPartie(lettre="D", titre="Prise en charge"),
            ],
        ),
    ]

    partie_i = Partie(
        numero="I",
        titre="Pneumothorax",
        sous_parties=[
            # ── A. DÉFINITION ET CLASSIFICATION ──
            SousPartie(lettre="A", titre="Définition et classification", rows=[
                FicheRow(concept="Définition", detail_md=(
                    "- **Pneumothorax** = présence d'**air dans la cavité pleurale**"
                )),
                FicheRow(concept="★ Classification", detail_md=(
                    "- **PNO spontané primaire** :\n"
                    "  - Sujet jeune, **exposition tabagique**, longiligne\n"
                    "  - Sans pathologie pulmonaire sous-jacente\n"
                    "- **PNO spontané secondaire** :\n"
                    "  - Sur poumon pathologique (BPCO, emphysème, fibrose)\n"
                    "- **PNO traumatique** :\n"
                    "  - Fractures costales\n"
                    "  - Iatrogène (ponction, ventilation mécanique)"
                )),
            ]),

            # ── B. CLINIQUE ──
            SousPartie(lettre="B", titre="Clinique", rows=[
                FicheRow(concept="Signes fonctionnels", detail_md=(
                    "- **Douleur** :\n"
                    "  - Brutale\n"
                    "  - Unilatérale\n"
                    "  - Latéro-thoracique\n"
                    "  - Rythmée par la respiration\n"
                    "- **Dyspnée** : inconstante"
                )),
                FicheRow(concept="★ Signes physiques", detail_md=(
                    "- **Hémithorax distendu**, peu mobile\n"
                    "- Syndrome pleural aérien :\n"
                    "  - Diminution ou **abolition du murmure vésiculaire**\n"
                    "  - Abolition des **vibrations vocales**\n"
                    "  - **Tympanisme** à la percussion"
                )),
                FicheRow(concept="⚠ Signes de gravité", detail_md=(
                    "- **Hypoxémie** (baisse de la SpO2)\n"
                    "- **Bradycardie**\n"
                    "- **Hypotension**\n"
                    "- **Déviation médiastinale** sur la radiographie de thorax"
                )),
                FicheRow(concept="", detail_md=(
                    "- Le **pneumothorax suffocant** désigne un pneumothorax qui cause une "
                    "**détresse respiratoire aiguë** ou une **défaillance hémodynamique**\n"
                    "  - **Complication rare**\n"
                    "  - Nécessite un **diagnostic rapide** selon la tolérance respiratoire "
                    "du patient : **FAST échographie** aux urgences / **radiographie de thorax au lit**\n"
                    "  - **Exsufflation en urgence au lit du patient**"
                ), kind="a_retenir"),
            ]),

            # ── C. IMAGERIE ──
            SousPartie(lettre="C", titre="Imagerie", rows=[
                FicheRow(concept="◆ Examens clés", detail_md=(
                    "- Le **diagnostic est posé par l'imagerie thoracique**\n"
                    "- **Radiographie de thorax en inspiration** (1re intention) :\n"
                    "  - **Hyperclarté avasculaire périphérique**\n"
                    "  - **Ligne de rétraction** du parenchyme pulmonaire\n"
                    "  - Recherche d'une **déviation médiastinale** = signe de gravité\n"
                    "- **Échographie pleurale** :\n"
                    "  - Permet de faire le diagnostic\n"
                    "  - Plus sensible que la radio si opérateur expérimenté\n"
                    "- **TDM thoracique non injecté** :\n"
                    "  - À réaliser en cas de doute diagnostique\n"
                    "  - Quantification précise, recherche de blebs/bulles"
                )),
                FicheRow(concept="", detail_md=(
                    "- **Définition radiologique du PSP de grande abondance** : "
                    "**décollement sur toute la ligne axillaire** ET d'au moins "
                    "**2 cm de largeur au niveau du hile pulmonaire**"
                ), kind="a_retenir"),
            ]),

            # ── D. PRISE EN CHARGE ──
            SousPartie(lettre="D", titre="Prise en charge", rows=[
                FicheRow(concept="★ ◆ PNO spontané primaire", detail_md=(
                    "- **Surveillance 4 h aux urgences** au minimum si :\n"
                    "  - **Absence de critères** de prise en charge active\n"
                    "  - Bien toléré + faible abondance\n"
                    "- **Exsufflation ou drainage thoracique** si critères présents :\n"
                    "  - **Mauvaise tolérance clinique** : dyspnée, douleur, signes de gravité\n"
                    "  - **OU grande abondance** :\n"
                    "    - Décollement sur toute la ligne axillaire\n"
                    "    - ET > **2 cm** au niveau du hile pulmonaire"
                )),
                FicheRow(concept="★ PNO spontané secondaire", detail_md=(
                    "- En général : **drainage** si taille suffisante pour sa mise en place\n"
                    "- Surveillance hospitalière obligatoire"
                )),
                FicheRow(concept="PNO récidivant", detail_md=(
                    "- **Prise en charge chirurgicale** (pleurodèse, bullectomie)"
                )),
                FicheRow(concept="⚠ PNO suffocant / compressif", detail_md=(
                    "- **Augmentation de la pression intrathoracique**, pouvant aller "
                    "jusqu'à la **tamponnade gazeuse**\n"
                    "- **Définition** : PNO causant **détresse respiratoire aiguë** ou "
                    "**défaillance hémodynamique** (en général avec signes de "
                    "**décompensation cardiaque droite**, notamment **turgescence jugulaire**)\n"
                    "- **Prise en charge** :\n"
                    "  - Nécessite un **diagnostic rapide** selon la tolérance respiratoire "
                    "du patient : **FAST échographie** aux urgences / **radiographie de "
                    "thorax au lit**\n"
                    "  - **Exsufflation en urgence au lit du patient**"
                )),
            ]),
        ],
    )

    # ── SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Classification et indications de PEC active (PNO primaire)", markdown=(
            "| Critère | Seuil / Type | Conduite |\n"
            "|---------|--------------|----------|\n"
            "| **PNO spontané primaire** | Jeune, tabac, longiligne | Surveillance 4 h ou exsufflation ou drainage selon critères |\n"
            "| **PNO spontané secondaire** | BPCO, emphysème, fibrose | **Drainage** en général |\n"
            "| **PNO traumatique** | Fractures, iatrogène | Drainage selon abondance |\n"
            "| Mauvaise tolérance | Dyspnée, douleur, gravité | **Exsufflation ou drainage** |\n"
            "| Décollement axillaire | Toute la ligne ET > **2 cm** au hile | **Exsufflation ou drainage** |\n"
            "| **PNO compressif** | Détresse respiratoire ou défaillance hémodynamique | **Exsufflation en URGENCE au lit** |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Surveillance urgences | **4 h minimum** | PSP bien toléré |\n"
        "| PSP grande abondance | Décollement sur toute la ligne axillaire ET ≥ **2 cm** au hile pulmonaire | Indication exsufflation / drainage |\n"
        "| Examen physique | MV ↓ + VV ↓ + tympanisme | Syndrome pleural aérien |\n"
        "| Gravité (PNO compressif) | Détresse respiratoire ou défaillance hémodynamique | Turgescence jugulaire possible |\n"
        "| Imagerie 1re intention | Radio thorax inspiration | Hyperclarté + ligne de rétraction |"
    ))

    points_cles = [
        "**PNO = air dans la cavité pleurale** ; 3 types : primaire, secondaire, traumatique",
        "**PSP (PNO spontané primaire)** : jeune, longiligne, **tabac**, sans pathologie pulmonaire",
        "Examen physique : abolition MV + abolition VV + **tympanisme**",
        "PNO compressif : **détresse respiratoire aiguë** ou **défaillance hémodynamique**",
        "Diagnostic = **imagerie** : radio thorax inspiration ± échographie ± TDM si doute",
        "PSP bien toléré + faible abondance : **surveillance 4 h** aux urgences",
        "**Grande abondance** = décollement axillaire complet **ET** > **2 cm** au hile → exsufflation/drainage",
        "PNO spontané secondaire : drainage en général",
        "PNO récidivant : **chirurgie** (pleurodèse, bullectomie)",
        "**PNO compressif = urgence vitale** → exsufflation urgente au lit après diagnostic rapide",
    ]

    fiche_eclair_md = (
        "**Définition** : air dans la cavité pleurale.\n\n"
        "**Classification** : spontané primaire (jeune, longiligne, **tabac**, "
        "poumon sain) ; spontané secondaire (BPCO, emphysème, fibrose) ; "
        "traumatique (fractures costales, iatrogène).\n\n"
        "**Clinique** : douleur brutale unilatérale latéro-thoracique rythmée par "
        "la respiration ± dyspnée inconstante.\n\n"
        "**Examen physique** : hémithorax distendu peu mobile, MV ↓ + VV ↓ + "
        "**tympanisme**.\n\n"
        "**Gravité** : PNO compressif = **détresse respiratoire aiguë** ou "
        "**défaillance hémodynamique** (turgescence jugulaire possible).\n\n"
        "**Imagerie** : radio thorax inspiration (hyperclarté avasculaire + ligne de "
        "rétraction) ; échographie pleurale (plus sensible si opérateur expérimenté) ; "
        "TDM non injecté si doute diagnostique.\n\n"
        "**PSP bien toléré** : surveillance **4 h** aux urgences.\n\n"
        "**PSP mal toléré OU grande abondance** (décollement axillaire complet "
        "ET > **2 cm** au hile) : **exsufflation ou drainage**.\n\n"
        "**PNO spontané secondaire** : drainage en général.\n\n"
        "**PNO récidivant** : chirurgie (pleurodèse, bullectomie).\n\n"
        "**PNO compressif** : **URGENCE VITALE** → exsufflation urgente au lit du "
        "patient après un diagnostic rapide (FAST écho / radio au lit)."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Pneumothorax",
        annee="2025-2026",
        item="Pneumothorax",
        plan=plan,
        parties=[partie_i],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Pneumothorax",
        usage=UsageStats(),
    )


def _make_analyzed_image(path: Path, desc: str, concept: str, section: str,
                         fig_num: int, img_type: str = "schema") -> AnalyzedImage:
    from PIL import Image
    try:
        with Image.open(str(path)) as img:
            width, height = img.size
    except Exception:
        width, height = 1200, 900

    return AnalyzedImage(
        source=ExtractedImage(
            data=b"", ext="png", page=fig_num, index=fig_num,
            width=width, height=height, sha=path.stem,
        ),
        description=desc, concept_lie=concept, pertinence=9,
        type=img_type, section_suggeree=section, saved_path=path,
        figure_number=fig_num,
    )


def _place_source_images(fiche: FicheData, figures_dir: Path) -> None:
    all_images = []
    for i, entry in enumerate(_SOURCE_IMAGES):
        path = figures_dir / entry["file"]
        if not path.exists():
            print(f"  [SKIP] {entry['file']} not found")
            continue
        img = _make_analyzed_image(
            path, entry["desc"], entry["concept"], entry["desc"],
            fig_num=i + 1, img_type=entry.get("type", "schema"),
        )
        all_images.append(img)
        pi, si = entry["partie"], entry["sp"]
        if pi < len(fiche.parties) and si < len(fiche.parties[pi].sous_parties):
            fiche.parties[pi].sous_parties[si].images.append(img)
    fiche.images = all_images


def main() -> None:
    fiche = build_fiche()

    figures_dir = PROJECT_ROOT / "output" / "figures_user"
    if figures_dir.exists():
        _place_source_images(fiche, figures_dir)
        print(f"Placed {len(fiche.images)} source images")

    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Medecine_generale_Pneumothorax_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out} ({pdf_out.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()

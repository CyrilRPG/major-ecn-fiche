#!/usr/bin/env python3
"""Génère une fiche d'exemple à partir de données fictives (sans appel API).

Permet de valider le rendu visuel (PDF + DOCX) de la charte « luxe médical »,
de l'organisation en tableaux, des lignes-réflexe et de l'insertion d'images.
Sortie : dossier `examples/`.
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from major_ecn.config import LOGO_PATH  # noqa: E402
from major_ecn.content_builder import output_basename  # noqa: E402
from major_ecn.docx_generator import render_docx  # noqa: E402
from major_ecn.models import (  # noqa: E402
    AnalyzedImage,
    ExtractedImage,
    FicheData,
    FicheRow,
    Partie,
    PlanPartie,
    PlanSousPartie,
    SousPartie,
    TableauSynthese,
)
from major_ecn.pdf_generator import render_pdf  # noqa: E402

FIGURES_DIR = PROJECT_ROOT / "examples" / "sample_figures"


def _row(concept: str, detail: str) -> FicheRow:
    return FicheRow(concept=concept, detail_md=detail)


# ── Génération d'images-schémas de démonstration ──────────────────────────────
def _font(size: int):
    """Charge une police pour le rendu des schémas, avec repli."""
    from PIL import ImageFont

    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Georgia.ttf",
    ):
        if Path(candidate).exists():
            try:
                return ImageFont.truetype(candidate, size)
            except OSError:
                continue
    try:
        return ImageFont.load_default(size=size)
    except TypeError:  # Pillow < 10.1
        return ImageFont.load_default()


def _make_schema(path: Path, title: str, nodes: list[str]) -> None:
    """Dessine un schéma de démonstration (suite de nœuds reliés par des flèches)."""
    from PIL import Image, ImageDraw

    width, height = 960, 430
    red, gold, anthracite, cream = (
        (225, 29, 72), (201, 169, 97), (31, 41, 55), (250, 247, 242),
    )
    image = Image.new("RGB", (width, height), (255, 255, 251))
    draw = ImageDraw.Draw(image)

    draw.text((width / 2, 48), title, fill=anthracite, font=_font(32), anchor="mm")
    draw.line([(width / 2 - 170, 84), (width / 2 + 170, 84)], fill=gold, width=3)

    count = len(nodes)
    box_w, box_h, margin = 232, 118, 44
    gap = (width - 2 * margin - count * box_w) / max(1, count - 1) if count > 1 else 0
    top = 210
    edges: list[tuple[float, float]] = []
    for index, label in enumerate(nodes):
        left = margin + index * (box_w + gap)
        draw.rounded_rectangle(
            [left, top, left + box_w, top + box_h],
            radius=16, fill=cream, outline=red, width=3,
        )
        draw.multiline_text(
            (left + box_w / 2, top + box_h / 2), label, fill=anthracite,
            font=_font(21), anchor="mm", align="center", spacing=6,
        )
        edges.append((left, left + box_w))
        if index > 0:
            mid_y = top + box_h / 2
            start_x, end_x = edges[index - 1][1] + 6, left - 14
            draw.line([(start_x, mid_y), (end_x, mid_y)], fill=red, width=4)
            draw.polygon(
                [(end_x, mid_y - 9), (end_x, mid_y + 9), (end_x + 14, mid_y)],
                fill=red,
            )

    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "PNG")


def _figure(path: Path, description: str, concept: str, number: int) -> AnalyzedImage:
    """Construit un `AnalyzedImage` prêt à être inséré dans une sous-partie."""
    source = ExtractedImage(data=b"", ext="png", page=1, index=number,
                            width=960, height=430, sha=f"demo-{number}")
    return AnalyzedImage(
        source=source, description=description, concept_lie=concept,
        pertinence=9, type="schema", section_suggeree=concept,
        saved_path=path, figure_number=number,
    )


def _mock_fiche() -> FicheData:
    """Construit une `FicheData` fictive et complète (HTA)."""
    fig1 = FIGURES_DIR / "figure_01.png"
    fig2 = FIGURES_DIR / "figure_02.png"
    _make_schema(fig1, "Démarche diagnostique de l'HTA",
                 ["PA élevée\nau cabinet", "Confirmation\npar MAPA",
                  "Bilan +\ntraitement"])
    _make_schema(fig2, "Retentissement sur les organes cibles",
                 ["Cœur\n(HVG)", "Rein\n(↓ DFG)", "Œil\n(rétinopathie)"])

    plan = [
        PlanPartie("I", "Définition et épidémiologie",
                   "Cadre nosologique et poids de santé publique.",
                   [PlanSousPartie("A", "Définitions et seuils", "Seuils et grades."),
                    PlanSousPartie("B", "Épidémiologie", "Prévalence et FdR.")]),
        PlanPartie("II", "Diagnostic et bilan initial",
                   "Confirmation et recherche du retentissement.",
                   [PlanSousPartie("A", "Mesure de la PA", "Conditions et MAPA."),
                    PlanSousPartie("B", "Bilan de retentissement", "Organes cibles.")]),
        PlanPartie("III", "Prise en charge thérapeutique",
                   "Mesures hygiéno-diététiques et médicaments.",
                   [PlanSousPartie("A", "Mesures non médicamenteuses", "RHD."),
                    PlanSousPartie("B", "Traitement médicamenteux", "Classes.")]),
    ]

    partie_1 = Partie("I", "Définition et épidémiologie", [
        SousPartie("A", "Définitions et seuils", [
            _row("★ Définition de l'HTA",
                 "- **HTA** : **PAS** ≥ **140 mmHg** et/ou **PAD** ≥ **90 mmHg** "
                 "au cabinet\n"
                 "  - diagnostic confirmé sur **deux consultations**\n"
                 "  - automesure : seuil abaissé à **≥ 135/85 mmHg**"),
            _row("◆ Grades de sévérité",
                 "| Grade | PAS (mmHg) | PAD (mmHg) |\n"
                 "|-------|-----------|-----------|\n"
                 "| **Grade 1** | 140-159 | 90-99 |\n"
                 "| **Grade 2** | 160-179 | 100-109 |\n"
                 "| **Grade 3** | ≥ 180 | ≥ 110 |"),
            FicheRow(concept="", kind="piege", detail_md=(
                "Ne pas confondre l'**HTA blouse blanche** (PA élevée au cabinet "
                "uniquement) et l'**HTA masquée** (PA normale au cabinet, élevée "
                "en ambulatoire) : le pronostic diffère.")),
        ], images=[_figure(fig1, "Étapes de la démarche diagnostique devant une "
                           "pression artérielle élevée.", "démarche diagnostique", 1)]),
        SousPartie("B", "Épidémiologie", [
            _row("Prévalence",
                 "- environ **30 %** de la population adulte\n"
                 "- augmente avec l'**âge**\n"
                 "- premier motif de consultation en médecine générale"),
            _row("◆ Facteurs de risque",
                 "- **Non modifiables** : âge, sexe masculin, hérédité\n"
                 "- **Modifiables** : surpoids, sédentarité, **sel**, alcool, tabac"),
            FicheRow(concept="", kind="a_retenir", detail_md=(
                "L'HTA est un **facteur de risque cardiovasculaire majeur** : "
                "AVC, insuffisance cardiaque, coronaropathie, néphropathie.")),
        ]),
    ])

    partie_2 = Partie("II", "Diagnostic et bilan initial", [
        SousPartie("A", "Mesure de la pression artérielle", [
            _row("Conditions de mesure",
                 "- patient au **repos** depuis 5 minutes, assis\n"
                 "- brassard adapté à la circonférence du bras\n"
                 "- mesure aux **deux bras** lors du bilan initial"),
            _row("★ MAPA",
                 "- mesure **ambulatoire** de la PA sur 24 h\n"
                 "- examen de **référence** pour confirmer le diagnostic\n"
                 "- dépiste l'**HTA masquée**"),
            FicheRow(concept="", kind="mnemo", detail_md=(
                "Automesure — **règle des 3** : 3 mesures matin et soir, "
                "3 jours de suite.")),
        ]),
        SousPartie("B", "Bilan de retentissement", [
            _row("◆ Organes cibles",
                 "- **Cœur** : ECG, hypertrophie ventriculaire gauche\n"
                 "- **Rein** : créatininémie, **DFG**, protéinurie\n"
                 "- **Œil** : rétinopathie hypertensive si HTA sévère"),
            _row("Bilan biologique",
                 "- kaliémie, glycémie à jeun\n- bilan lipidique, créatininémie"),
            FicheRow(concept="", kind="piege", detail_md=(
                "⚠ Rechercher une **HTA secondaire** si HTA résistante, sujet "
                "jeune ou signes d'orientation.")),
        ], images=[_figure(fig2, "Principaux organes cibles atteints par "
                           "l'hypertension artérielle.", "organes cibles", 2)]),
    ])

    partie_3 = Partie("III", "Prise en charge thérapeutique", [
        SousPartie("A", "Mesures non médicamenteuses", [
            _row("Règles hygiéno-diététiques",
                 "- réduction des apports en **sel** (< 6 g/j)\n"
                 "- **perte de poids** en cas de surpoids\n"
                 "- **activité physique** régulière (30 min/j)\n"
                 "- limitation de l'**alcool**, arrêt du **tabac**"),
        ]),
        SousPartie("B", "Traitement médicamenteux", [
            _row("★ Classes de 1re intention",
                 "| Classe | Exemple | Indication |\n"
                 "|--------|---------|-----------|\n"
                 "| **IEC** | Ramipril | Diabète, IC |\n"
                 "| **ARA II** | Losartan | Intolérance aux IEC |\n"
                 "| **I. calcique** | Amlodipine | Sujet âgé |\n"
                 "| **Diurétique** | HCTZ | Sujet âgé |"),
            _row("◆ Stratégie",
                 "- **bithérapie d'emblée** souvent recommandée\n"
                 "  - privilégier les **associations fixes**\n"
                 "- objectif : **< 140/90 mmHg**, voire **< 130/80 mmHg**"),
            FicheRow(concept="", kind="mnemo", detail_md=(
                "Les 5 classes — moyen mnémotechnique **« A-B-C-D »** : "
                "**A**RA II / IEC, **B**êtabloquants, **C**alciques, "
                "**D**iurétiques.")),
        ]),
    ])

    tableaux = [
        TableauSynthese("Grades de sévérité de l'HTA",
                        "| Grade | PAS (mmHg) | PAD (mmHg) |\n"
                        "|-------|-----------|-----------|\n"
                        "| **Grade 1** | 140-159 | 90-99 |\n"
                        "| **Grade 2** | 160-179 | 100-109 |\n"
                        "| **Grade 3** | ≥ 180 | ≥ 110 |"),
        TableauSynthese("Classes thérapeutiques de première intention",
                        "| Classe | Exemple | Indication préférentielle |\n"
                        "|--------|---------|---------------------------|\n"
                        "| **IEC** | Ramipril | Diabète, insuffisance cardiaque |\n"
                        "| **ARA II** | Losartan | Intolérance aux IEC (toux) |\n"
                        "| **Inhibiteur calcique** | Amlodipine | Sujet âgé |\n"
                        "| **Diurétique thiazidique** | HCTZ | Sujet âgé |\n"
                        "| **Bêtabloquant** | Bisoprolol | Coronaropathie associée |"),
    ]

    chiffres_cles = TableauSynthese(
        "Chiffres-clés",
        "| Paramètre | Valeur | Précision |\n"
        "|-----------|--------|-----------|\n"
        "| Seuil HTA au cabinet | **140/90 mmHg** | sur 2 consultations |\n"
        "| Seuil en automesure | **135/85 mmHg** | règle des 3 |\n"
        "| Apports en sel conseillés | **< 6 g/j** | mesure hygiéno-diététique |\n"
        "| Objectif tensionnel | **< 140/90 mmHg** | voire < 130/80 si toléré |\n"
        "| Prévalence de l'HTA | **≈ 30 %** | population adulte |",
    )

    points_cles = [
        "L'**HTA** est définie par une PA **≥ 140/90 mmHg** au cabinet, confirmée "
        "sur des mesures répétées.",
        "La **MAPA** et l'**automesure** confirment le diagnostic et dépistent "
        "l'HTA blouse blanche et l'HTA masquée.",
        "Le bilan initial recherche une **atteinte des organes cibles** et une "
        "**HTA secondaire**.",
        "Les **règles hygiéno-diététiques** sont la base du traitement.",
        "Cinq classes de 1re intention ; la **bithérapie** est souvent d'emblée.",
        "Objectif : **< 140/90 mmHg**, idéalement **< 130/80 mmHg** si toléré.",
    ]

    fiche_eclair = (
        "**Définition** : PA ≥ 140/90 mmHg au cabinet (135/85 en automesure), "
        "confirmée sur 2 consultations.\n\n"
        "**Diagnostic** : MAPA = examen de référence ; rechercher HTA blouse "
        "blanche et HTA masquée.\n\n"
        "**Bilan** : organes cibles (cœur, rein, œil) + bilan biologique "
        "minimal ; évoquer une HTA secondaire si résistance ou sujet jeune.\n\n"
        "**Traitement** : RHD systématiques + 5 classes (IEC, ARA II, calciques, "
        "diurétiques, bêtabloquants) ; bithérapie d'emblée fréquente ; "
        "objectif < 140/90 mmHg."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Hypertension Artérielle",
        annee="2025-2026",
        item="Item 224",
        plan=plan,
        parties=[partie_1, partie_2, partie_3],
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair,
        images=[],
        fiche_numero="Item 224",
    )


def main() -> None:
    """Génère la fiche d'exemple en PDF et DOCX."""
    fiche = _mock_fiche()
    output_dir = PROJECT_ROOT / "examples"
    output_dir.mkdir(exist_ok=True)
    basename = output_basename(fiche.matiere, fiche.nom_cours, fiche.annee)
    logo = LOGO_PATH if LOGO_PATH.exists() else None

    pdf_path = render_pdf(fiche, output_dir / f"{basename}.pdf")
    print(f"PDF généré  : {pdf_path}")

    docx_path = render_docx(fiche, output_dir / f"{basename}.docx", logo)
    print(f"DOCX généré : {docx_path}")


if __name__ == "__main__":
    main()

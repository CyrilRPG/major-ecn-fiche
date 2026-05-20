#!/usr/bin/env python3
"""Génère une fiche d'exemple à partir de données fictives (sans appel API).

Permet de valider le rendu visuel (PDF + DOCX) de la charte « luxe médical »
et de l'organisation en tableaux. Sortie : dossier `examples/`.
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
    FicheData,
    FicheRow,
    Partie,
    PlanPartie,
    PlanSousPartie,
    SousPartie,
    TableauSynthese,
)
from major_ecn.pdf_generator import render_pdf  # noqa: E402


def _mock_fiche() -> FicheData:
    """Construit une `FicheData` fictive et complète (HTA), en tableaux."""
    plan = [
        PlanPartie(
            numero="I",
            titre="Définition et épidémiologie",
            resume="Cadre nosologique de l'HTA et poids de santé publique.",
            sous_parties=[
                PlanSousPartie("A", "Définitions et seuils",
                               "Seuils tensionnels et grades."),
                PlanSousPartie("B", "Épidémiologie",
                               "Prévalence et facteurs de risque."),
            ],
        ),
        PlanPartie(
            numero="II",
            titre="Diagnostic et bilan initial",
            resume="Confirmation diagnostique et recherche du retentissement.",
            sous_parties=[
                PlanSousPartie("A", "Mesure de la pression artérielle",
                               "Conditions de mesure et MAPA."),
                PlanSousPartie("B", "Bilan de retentissement",
                               "Atteinte des organes cibles."),
            ],
        ),
        PlanPartie(
            numero="III",
            titre="Prise en charge thérapeutique",
            resume="Mesures hygiéno-diététiques et traitement médicamenteux.",
            sous_parties=[
                PlanSousPartie("A", "Mesures non médicamenteuses",
                               "Règles hygiéno-diététiques."),
                PlanSousPartie("B", "Traitement médicamenteux",
                               "Classes et stratégie d'association."),
            ],
        ),
    ]

    partie_1 = Partie(
        numero="I",
        titre="Définition et épidémiologie",
        sous_parties=[
            SousPartie(
                lettre="A",
                titre="Définitions et seuils",
                rows=[
                    FicheRow(
                        concept="★ Définition de l'HTA",
                        detail_md=(
                            "- **Hypertension artérielle (HTA)** : pression "
                            "artérielle systolique (**PAS**) ≥ **140 mmHg** "
                            "et/ou diastolique (**PAD**) ≥ **90 mmHg** au cabinet\n"
                            "  - diagnostic confirmé sur **deux consultations** "
                            "distinctes\n"
                            "  - en automesure, seuil abaissé à **≥ 135/85 mmHg**"
                        ),
                    ),
                    FicheRow(
                        concept="◆ Grades de sévérité",
                        detail_md=(
                            "| Grade | PAS (mmHg) | PAD (mmHg) |\n"
                            "|-------|-----------|-----------|\n"
                            "| **Grade 1** | 140-159 | 90-99 |\n"
                            "| **Grade 2** | 160-179 | 100-109 |\n"
                            "| **Grade 3** | ≥ 180 | ≥ 110 |"
                        ),
                    ),
                    FicheRow(
                        concept="⚠ HTA blouse blanche",
                        detail_md=(
                            "- élévation tensionnelle **au cabinet uniquement**\n"
                            "- à confirmer par **MAPA** ou **automesure**\n"
                            "- ⚠ à ne pas confondre avec l'**HTA masquée** "
                            "(normale au cabinet, élevée en ambulatoire)"
                        ),
                    ),
                ],
            ),
            SousPartie(
                lettre="B",
                titre="Épidémiologie",
                rows=[
                    FicheRow(
                        concept="Prévalence",
                        detail_md=(
                            "- environ **30 %** de la population adulte\n"
                            "- augmente avec l'**âge**\n"
                            "- premier motif de consultation en médecine générale"
                        ),
                    ),
                    FicheRow(
                        concept="◆ Facteurs de risque",
                        detail_md=(
                            "- **Non modifiables** : âge, sexe masculin, hérédité\n"
                            "- **Modifiables** : surpoids, sédentarité, "
                            "consommation de **sel**, alcool, tabac"
                        ),
                    ),
                ],
            ),
        ],
    )

    partie_2 = Partie(
        numero="II",
        titre="Diagnostic et bilan initial",
        sous_parties=[
            SousPartie(
                lettre="A",
                titre="Mesure de la pression artérielle",
                rows=[
                    FicheRow(
                        concept="Conditions de mesure",
                        detail_md=(
                            "- patient au **repos** depuis 5 minutes, assis\n"
                            "- brassard adapté à la circonférence du bras\n"
                            "- mesure aux **deux bras** lors du bilan initial"
                        ),
                    ),
                    FicheRow(
                        concept="★ MAPA",
                        detail_md=(
                            "- mesure **ambulatoire** de la PA sur 24 h\n"
                            "- examen de **référence** pour confirmer le diagnostic\n"
                            "- dépiste l'**HTA masquée**"
                        ),
                    ),
                    FicheRow(
                        concept="Automesure",
                        detail_md=(
                            "- **règle des 3** : 3 mesures matin et soir, "
                            "3 jours de suite"
                        ),
                    ),
                ],
            ),
            SousPartie(
                lettre="B",
                titre="Bilan de retentissement",
                rows=[
                    FicheRow(
                        concept="◆ Organes cibles",
                        detail_md=(
                            "- **Cœur** : ECG, hypertrophie ventriculaire gauche\n"
                            "- **Rein** : créatininémie, **DFG**, protéinurie\n"
                            "- **Œil** : rétinopathie hypertensive si HTA sévère"
                        ),
                    ),
                    FicheRow(
                        concept="Bilan biologique",
                        detail_md=(
                            "- kaliémie, glycémie à jeun\n"
                            "- bilan lipidique, créatininémie"
                        ),
                    ),
                    FicheRow(
                        concept="⚠ HTA secondaire",
                        detail_md=(
                            "- à rechercher si **HTA résistante**, sujet jeune "
                            "ou signes d'orientation"
                        ),
                    ),
                ],
            ),
        ],
    )

    partie_3 = Partie(
        numero="III",
        titre="Prise en charge thérapeutique",
        sous_parties=[
            SousPartie(
                lettre="A",
                titre="Mesures non médicamenteuses",
                rows=[
                    FicheRow(
                        concept="Règles hygiéno-diététiques",
                        detail_md=(
                            "- réduction des apports en **sel** (< 6 g/j)\n"
                            "- **perte de poids** en cas de surpoids\n"
                            "- **activité physique** régulière (30 min/j)\n"
                            "- limitation de l'**alcool**, arrêt du **tabac**"
                        ),
                    ),
                ],
            ),
            SousPartie(
                lettre="B",
                titre="Traitement médicamenteux",
                rows=[
                    FicheRow(
                        concept="★ Classes de 1re intention",
                        detail_md=(
                            "| Classe | Exemple | Indication préférentielle |\n"
                            "|--------|---------|---------------------------|\n"
                            "| **IEC** | Ramipril | Diabète, insuffisance cardiaque |\n"
                            "| **ARA II** | Losartan | Intolérance aux IEC (toux) |\n"
                            "| **Inhibiteur calcique** | Amlodipine | Sujet âgé |\n"
                            "| **Diurétique thiazidique** | HCTZ | Sujet âgé |"
                        ),
                    ),
                    FicheRow(
                        concept="◆ Stratégie thérapeutique",
                        detail_md=(
                            "- **bithérapie d'emblée** souvent recommandée\n"
                            "  - privilégier les **associations fixes**\n"
                            "- objectif : **< 140/90 mmHg**, voire "
                            "**< 130/80 mmHg** si bien toléré"
                        ),
                    ),
                ],
            ),
        ],
    )

    tableaux = [
        TableauSynthese(
            titre="Grades de sévérité de l'HTA",
            markdown=(
                "| Grade | PAS (mmHg) | PAD (mmHg) |\n"
                "|-------|-----------|-----------|\n"
                "| **Grade 1** | 140-159 | 90-99 |\n"
                "| **Grade 2** | 160-179 | 100-109 |\n"
                "| **Grade 3** | ≥ 180 | ≥ 110 |"
            ),
        ),
        TableauSynthese(
            titre="Classes thérapeutiques de première intention",
            markdown=(
                "| Classe | Exemple | Indication préférentielle |\n"
                "|--------|---------|---------------------------|\n"
                "| **IEC** | Ramipril | Diabète, insuffisance cardiaque |\n"
                "| **ARA II** | Losartan | Intolérance aux IEC (toux) |\n"
                "| **Inhibiteur calcique** | Amlodipine | Sujet âgé, sujet noir |\n"
                "| **Diurétique thiazidique** | Hydrochlorothiazide | Sujet âgé |\n"
                "| **Bêtabloquant** | Bisoprolol | Coronaropathie associée |"
            ),
        ),
    ]

    points_cles = [
        "L'**HTA** est définie par une PA **≥ 140/90 mmHg** au cabinet, confirmée "
        "sur des mesures répétées.",
        "La **MAPA** et l'**automesure** confirment le diagnostic et dépistent "
        "l'HTA blouse blanche et l'HTA masquée.",
        "Le bilan initial recherche systématiquement une **atteinte des organes "
        "cibles** et une **HTA secondaire**.",
        "Les **règles hygiéno-diététiques** sont la base du traitement, toujours "
        "associées aux médicaments.",
        "Cinq classes de première intention ; la **bithérapie** est souvent "
        "instaurée d'emblée.",
        "L'objectif tensionnel est **< 140/90 mmHg**, idéalement **< 130/80 mmHg** "
        "si la tolérance le permet.",
    ]

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Hypertension Artérielle",
        annee="2025-2026",
        item="Item 224",
        plan=plan,
        parties=[partie_1, partie_2, partie_3],
        tableaux=tableaux,
        points_cles=points_cles,
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

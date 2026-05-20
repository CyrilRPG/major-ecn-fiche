#!/usr/bin/env python3
"""Génère une fiche d'exemple à partir de données fictives (sans appel API).

Permet de valider le rendu visuel (PDF + DOCX) de la charte « luxe médical ».
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
    Encadre,
    FicheData,
    Partie,
    PlanPartie,
    PlanSousPartie,
    SousPartie,
    TableauSynthese,
)
from major_ecn.pdf_generator import render_pdf  # noqa: E402


def _mock_fiche() -> FicheData:
    """Construit une `FicheData` fictive et complète (HTA)."""
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
                corps_md=(
                    "- **Hypertension artérielle (HTA)** : pression artérielle "
                    "systolique (**PAS**) ≥ **140 mmHg** et/ou pression artérielle "
                    "diastolique (**PAD**) ≥ **90 mmHg** au cabinet.\n"
                    "    - Mesure confirmée à **deux consultations** distinctes.\n"
                    "    - Seuils abaissés en automesure : **≥ 135/85 mmHg**.\n"
                    "- **Grades de sévérité** :\n"
                    "    - **Grade 1** : 140-159 / 90-99 mmHg.\n"
                    "    - **Grade 2** : 160-179 / 100-109 mmHg.\n"
                    "    - **Grade 3** : ≥ 180 / 110 mmHg.\n"
                    "- **HTA blouse blanche** : élévation tensionnelle limitée au "
                    "cabinet médical, à confirmer par **MAPA** ou **automesure**."
                ),
            ),
            SousPartie(
                lettre="B",
                titre="Épidémiologie",
                corps_md=(
                    "- **Prévalence** : environ **30 %** de la population adulte ; "
                    "augmente avec l'âge.\n"
                    "- Premier motif de consultation en médecine générale.\n"
                    "- **Facteurs de risque** :\n"
                    "    - Non modifiables : **âge**, **sexe masculin**, hérédité.\n"
                    "    - Modifiables : **surpoids**, **sédentarité**, "
                    "**consommation de sel**, **alcool**, tabac.\n"
                    "- L'HTA est un facteur de risque **cardiovasculaire majeur** : "
                    "AVC, insuffisance cardiaque, coronaropathie, néphropathie."
                ),
            ),
        ],
        encadres=[
            Encadre(
                type="a_retenir",
                titre="À retenir",
                contenu="Le diagnostic d'HTA repose sur des mesures **répétées** "
                "et **standardisées**. Une seule mesure élevée ne suffit jamais.",
            ),
            Encadre(
                type="piege_ecn",
                titre="Piège ECN",
                contenu="Ne pas confondre **HTA blouse blanche** (PA élevée au "
                "cabinet uniquement) et **HTA masquée** (PA normale au cabinet, "
                "élevée en ambulatoire) — pronostic différent.",
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
                corps_md=(
                    "- **Conditions de mesure** :\n"
                    "    - Patient au **repos** depuis 5 minutes, assis.\n"
                    "    - Brassard adapté à la circonférence du bras.\n"
                    "    - Mesure aux **deux bras** lors du bilan initial.\n"
                    "- **MAPA** (mesure ambulatoire sur 24 h) : référence pour "
                    "confirmer le diagnostic et dépister l'**HTA masquée**.\n"
                    "- **Automesure** : 3 mesures matin et soir, 3 jours de suite "
                    "(**règle des 3**)."
                ),
            ),
            SousPartie(
                lettre="B",
                titre="Bilan de retentissement",
                corps_md=(
                    "- Recherche d'une **atteinte des organes cibles** :\n"
                    "    - **Cœur** : ECG, hypertrophie ventriculaire gauche.\n"
                    "    - **Rein** : créatininémie, **DFG**, protéinurie.\n"
                    "    - **Œil** : rétinopathie hypertensive si HTA sévère.\n"
                    "- **Bilan biologique minimal** : kaliémie, glycémie à jeun, "
                    "bilan lipidique, créatininémie.\n"
                    "- Recherche d'une **HTA secondaire** si HTA résistante, "
                    "sujet jeune ou signes d'orientation."
                ),
            ),
        ],
        encadres=[
            Encadre(
                type="mots_cles_tombes",
                titre="Mots-clés tombés",
                contenu="- MAPA\n- Hypertrophie ventriculaire gauche\n"
                "- Organes cibles\n- HTA secondaire\n- Protéinurie",
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
                corps_md=(
                    "- **Règles hygiéno-diététiques**, systématiques :\n"
                    "    - Réduction des apports en **sel** (< 6 g/j).\n"
                    "    - Perte de poids en cas de surpoids.\n"
                    "    - **Activité physique** régulière (30 min/j).\n"
                    "    - Limitation de l'**alcool**, arrêt du **tabac**.\n"
                    "- Toujours associées au traitement médicamenteux."
                ),
            ),
            SousPartie(
                lettre="B",
                titre="Traitement médicamenteux",
                corps_md=(
                    "- **Cinq classes** de première intention :\n"
                    "    - **IEC** et **ARA II** : bloqueurs du système "
                    "rénine-angiotensine.\n"
                    "    - **Inhibiteurs calciques**.\n"
                    "    - **Diurétiques thiazidiques**.\n"
                    "    - **Bêtabloquants** (indications spécifiques).\n"
                    "- Stratégie : **bithérapie d'emblée** souvent recommandée, "
                    "en privilégiant les **associations fixes**.\n"
                    "- Objectif tensionnel : **< 140/90 mmHg**, voire "
                    "**< 130/80 mmHg** si bien toléré."
                ),
            ),
        ],
        encadres=[
            Encadre(
                type="mnemo",
                titre="Astuce mnémotechnique",
                contenu="Les 5 classes — moyen mnémotechnique « **A-B-C-D** » : "
                "**A**RA II / IEC, **B**êtabloquants, **C**alciques, "
                "**D**iurétiques.",
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

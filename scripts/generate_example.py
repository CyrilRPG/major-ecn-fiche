#!/usr/bin/env python3
"""Génère une fiche d'exemple à partir de données fictives (sans appel API).

Permet de valider le rendu visuel (PDF + DOCX) de la charte « luxe médical »,
de l'organisation en tableaux et des enrichissements pédagogiques.
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
    Algorithme,
    FicheData,
    FicheEnTete,
    FicheRow,
    Partie,
    PlanPartie,
    PlanSousPartie,
    SousPartie,
    TableauSynthese,
)
from major_ecn.pdf_generator import render_pdf  # noqa: E402


def _row(concept: str, detail: str) -> FicheRow:
    return FicheRow(concept=concept, detail_md=detail)


def _mock_fiche() -> FicheData:
    """Construit une `FicheData` fictive et complète (HTA)."""
    en_tete = FicheEnTete(
        objectifs=[
            "Définir l'HTA et connaître ses seuils diagnostiques",
            "Conduire le bilan initial et rechercher le retentissement",
            "Hiérarchiser la prise en charge thérapeutique",
        ],
        prerequis=[
            "Régulation de la pression artérielle",
            "Système rénine-angiotensine-aldostérone",
        ],
        mots_cles=[
            "HTA", "PAS / PAD", "MAPA", "Automesure", "Organes cibles",
            "IEC", "ARA II", "Bithérapie", "HTA secondaire",
        ],
        items_lies=[
            "Item 222 — Facteurs de risque cardiovasculaire",
            "Item 232 — Insuffisance cardiaque",
            "Item 264 — Néphropathie vasculaire",
        ],
        vignette=(
            "Un homme de 58 ans, sans antécédent, consulte pour un bilan "
            "systématique. La pression artérielle mesurée est de 158/96 mmHg, "
            "confirmée à deux reprises. Il est asymptomatique. Comment confirmer "
            "le diagnostic, évaluer le retentissement et instaurer la prise en "
            "charge ?"
        ),
    )

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
        SousPartie("A", "Définitions et seuils", "generalites", [
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
        ]),
        SousPartie("B", "Épidémiologie", "generalites", [
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
        SousPartie("A", "Mesure de la pression artérielle", "paraclinique", [
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
        SousPartie("B", "Bilan de retentissement", "clinique", [
            _row("◆ Organes cibles",
                 "- **Cœur** : ECG, hypertrophie ventriculaire gauche\n"
                 "- **Rein** : créatininémie, **DFG**, protéinurie\n"
                 "- **Œil** : rétinopathie hypertensive si HTA sévère"),
            _row("Bilan biologique",
                 "- kaliémie, glycémie à jeun\n- bilan lipidique, créatininémie"),
            FicheRow(concept="", kind="piege", detail_md=(
                "⚠ Rechercher une **HTA secondaire** si HTA résistante, sujet "
                "jeune ou signes d'orientation.")),
        ]),
    ])

    partie_3 = Partie("III", "Prise en charge thérapeutique", [
        SousPartie("A", "Mesures non médicamenteuses", "traitement", [
            _row("Règles hygiéno-diététiques",
                 "- réduction des apports en **sel** (< 6 g/j)\n"
                 "- **perte de poids** en cas de surpoids\n"
                 "- **activité physique** régulière (30 min/j)\n"
                 "- limitation de l'**alcool**, arrêt du **tabac**"),
        ]),
        SousPartie("B", "Traitement médicamenteux", "traitement", [
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

    algorithmes = [
        Algorithme(
            titre="Démarche diagnostique devant une PA élevée",
            arbre_md=(
                "- PA ≥ 140/90 mmHg au cabinet\n"
                "  - OUI → confirmer par **MAPA** ou **automesure**\n"
                "    - MAPA ≥ 135/85 → **HTA confirmée** → bilan + traitement\n"
                "    - MAPA < 135/85 → **HTA blouse blanche** → surveillance\n"
                "  - NON → **pas d'HTA** → contrôle annuel"
            ),
        ),
    ]

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
        en_tete=en_tete,
        plan=plan,
        parties=[partie_1, partie_2, partie_3],
        algorithmes=algorithmes,
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
    fiche.en_tete.duree_lecture = 12
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

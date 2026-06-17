"""Génère la fiche de l'Item 223 - Dyslipidémies (Cardiologie)."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from major_ecn.models import (
    AnalyzedImage, ExtractedImage, FicheData, FicheRow, Partie,
    PlanPartie, PlanSousPartie, SousPartie, TableauSynthese, UsageStats,
)
from major_ecn.config import LOGO_PATH
from major_ecn.pdf_generator import render_pdf


def build_fiche() -> FicheData:
    plan = [
        PlanPartie(numero="I", titre="Généralités et risques associés", sous_parties=[
            PlanSousPartie(lettre="A", titre="Risques médicaux"),
            PlanSousPartie(lettre="B", titre="Conversions g/L ↔ mmol/L"),
        ]),
        PlanPartie(numero="II", titre="Diagnostic phénotypique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Bilan lipidique (EAL)"),
            PlanSousPartie(lettre="B", titre="Classification pragmatique"),
            PlanSousPartie(lettre="C", titre="Valeurs normales"),
        ]),
        PlanPartie(numero="III", titre="Hyperlipidémies secondaires", sous_parties=[
            PlanSousPartie(lettre="A", titre="Étiologies à éliminer"),
            PlanSousPartie(lettre="B", titre="Causes iatrogènes"),
        ]),
        PlanPartie(numero="IV", titre="Hyperlipidémies primitives", sous_parties=[
            PlanSousPartie(lettre="A", titre="Hypercholestérolémies familiales monogéniques"),
            PlanSousPartie(lettre="B", titre="Hypercholestérolémies polygéniques"),
            PlanSousPartie(lettre="C", titre="Hyperlipidémie familiale combinée"),
            PlanSousPartie(lettre="D", titre="Dysbêtalipoprotéinémie"),
            PlanSousPartie(lettre="E", titre="Hypertriglycéridémies et hyperchylomicronémies"),
        ]),
        PlanPartie(numero="V", titre="Évaluation du risque cardiovasculaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Outil SCORE2 / SCORE2-OP"),
            PlanSousPartie(lettre="B", titre="Catégories de risque"),
            PlanSousPartie(lettre="C", titre="Objectifs LDL-C"),
        ]),
        PlanPartie(numero="VI", titre="Prise en charge thérapeutique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Objectifs thérapeutiques"),
            PlanSousPartie(lettre="B", titre="Traitement diététique"),
            PlanSousPartie(lettre="C", titre="Traitement médicamenteux"),
            PlanSousPartie(lettre="D", titre="Hypercholestérolémie familiale hétérozygote"),
            PlanSousPartie(lettre="E", titre="Anticorps anti-PCSK9"),
        ]),
        PlanPartie(numero="VII", titre="Surveillance du traitement", sous_parties=[
            PlanSousPartie(lettre="A", titre="Efficacité"),
            PlanSousPartie(lettre="B", titre="Tolérance musculaire"),
            PlanSousPartie(lettre="C", titre="Tolérance hépatique"),
        ]),
    ]

    # ── PARTIE I : GÉNÉRALITÉS ──
    partie_i = Partie(numero="I", titre="Généralités et risques associés", sous_parties=[
        SousPartie(lettre="A", titre="Risques médicaux des dyslipidémies", rows=[
            FicheRow(concept="◆ Risque cardiovasculaire athéromateux", detail_md=(
                "- Risque principal des dyslipidémies, quelle que soit la localisation "
                "(coronaire, cérébrale, périphérique)\n"
                "- Le risque est associé :\n"
                "  - Positivement et de façon graduelle à la concentration de **LDL-cholestérol**\n"
                "  - Négativement et de façon graduelle à la concentration de **HDL-cholestérol**\n"
                "  - À l'**hypertriglycéridémie (HTG)** : risque en grande partie dépendant des "
                "autres marqueurs (surpoids, diabète, HDL-C bas)"
            )),
            FicheRow(concept="◆ Risque de pancréatite aiguë", detail_md=(
                "- Risque rare mais sévère\n"
                "- Survient en cas d'**HTG > 10 g/L**\n"
                "- Risque majeur dans les hyperchylomicronémies primitives"
            )),
            FicheRow(concept="", detail_md=(
                "- Risque CV : **LDL-C** positivement gradué, **HDL-C** négativement gradué\n"
                "- **HTG > 10 g/L** → risque de pancréatite aiguë"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Conversions des unités", rows=[
            FicheRow(concept="Conversions cholestérol", detail_md=(
                "- **g/L × 2,58 = mmol/L**\n"
                "- **mmol/L × 0,387 = g/L**"
            )),
            FicheRow(concept="Conversions triglycérides", detail_md=(
                "- **g/L × 1,14 = mmol/L**\n"
                "- **mmol/L × 0,875 = g/L**"
            )),
        ]),
    ])

    # ── PARTIE II : DIAGNOSTIC PHÉNOTYPIQUE ──
    partie_ii = Partie(numero="II", titre="Diagnostic phénotypique", sous_parties=[
        SousPartie(lettre="A", titre="Bilan lipidique (EAL)", rows=[
            FicheRow(concept="◆ Indication du bilan lipidique", detail_md=(
                "- Conseillé chez tous les adultes\n"
                "- En l'absence d'anomalie : pas de recontrôle avant **5 ans**\n"
                "- Le phénotype est une situation instantanée, variable selon les facteurs "
                "environnementaux (alimentation, statut pondéral)\n"
                "- Un même génotype peut s'exprimer sous plusieurs phénotypes chez un même sujet"
            )),
            FicheRow(concept="◆ Composition de l'EAL", detail_md=(
                "- L'**Exploration d'une Anomalie Lipidique (EAL)** comporte :\n"
                "  - Cholestérol total (CT)\n"
                "  - HDL-cholestérol\n"
                "  - Triglycérides (TG)\n"
                "- Le LDL-cholestérol est calculé par la **formule de Friedewald**"
            )),
            FicheRow(concept="◆ Formule de Friedewald", detail_md=(
                "- **LDL-C = CT − HDL-C − TG/5** (en g/L)\n"
                "- **LDL-C = CT − HDL-C − TG/2,2** (en mmol/L)\n"
                "- ⚠ Formule non valable si **TG ≥ 3,5 g/L**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La formule de **Friedewald** n'est pas valable pour des **TG > 3,5 g/L** : "
                "il faut alors un dosage direct du LDL-C"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Classification pragmatique en 3 types", rows=[
            FicheRow(concept="◆ Hypercholestérolémie pure (HCH)", detail_md=(
                "- Ex-type **IIa** de Fredrickson\n"
                "- **LDL-C > 1,60 g/L**"
            )),
            FicheRow(concept="◆ Hypertriglycéridémie pure (HTG)", detail_md=(
                "- Essentiellement **type IV** de Fredrickson\n"
                "- **TG > 1,5 g/L**"
            )),
            FicheRow(concept="◆ Hyperlipidémie mixte (HLM)", detail_md=(
                "- Association d'une hypercholestérolémie et d'une hypertriglycéridémie\n"
                "- Essentiellement **type IIb**, très rarement type III"
            )),
            FicheRow(concept="Hypo-HDLémie", detail_md=(
                "- **< 0,40 g/L** chez l'homme\n"
                "- **< 0,50 g/L** chez la femme\n"
                "- Peut être associée à l'une des 3 catégories précédentes"
            )),
            FicheRow(concept="", detail_md=(
                "- Classification ancienne de **Fredrickson** (types I, IIa, IIb, III, IV, V) "
                "de moins en moins utilisée, remplacée par la classification pragmatique en 3 types : "
                "**HCH, HTG, HLM**"
            ), kind="mnemo"),
        ]),
        SousPartie(lettre="C", titre="Valeurs normales (Afssaps 2005)", rows=[
            FicheRow(concept="◆ Bilan lipidique normal", detail_md=(
                "- Chez un sujet sans autre facteur de risque, les valeurs suivantes doivent "
                "être présentes **simultanément** :\n"
                "  - **LDL-C < 1,6 g/L**\n"
                "  - **HDL-C > 0,4 g/L**\n"
                "  - **TG < 1,5 g/L**"
            )),
        ]),
    ])

    # ── PARTIE III : HYPERLIPIDÉMIES SECONDAIRES ──
    partie_iii = Partie(numero="III", titre="Éliminer une cause d'hyperlipidémie secondaire", sous_parties=[
        SousPartie(lettre="A", titre="Étiologies à éliminer en priorité", rows=[
            FicheRow(concept="◆ Hypothyroïdie", detail_md=(
                "- Outil diagnostique : **TSH**\n"
                "- Type : HCH ou HLM"
            )),
            FicheRow(concept="◆ Cholestase hépatique", detail_md=(
                "- Outils diagnostiques : bilirubine, phosphatases alcalines\n"
                "- Type : HCH"
            )),
            FicheRow(concept="◆ Syndrome néphrotique", detail_md=(
                "- Outils diagnostiques : protéinurie, œdèmes\n"
                "- Type : HLM"
            )),
            FicheRow(concept="◆ Insuffisance rénale chronique", detail_md=(
                "- Outil diagnostique : créatinine\n"
                "- Type : HTG ou HLM"
            )),
            FicheRow(concept="◆ Alcoolisme", detail_md=(
                "- Outil diagnostique : interrogatoire\n"
                "- Type : HTG"
            )),
            FicheRow(concept="◆ Diabète", detail_md=(
                "- Outils diagnostiques : glycémie, HbA1c\n"
                "- Type : HTG"
            )),
        ]),
        SousPartie(lettre="B", titre="Causes iatrogènes", rows=[
            FicheRow(concept="Médicaments inducteurs", detail_md=(
                "| Médicament | Type d'hyperlipidémie |\n"
                "|------------|------------------------|\n"
                "| Œstrogènes | HTG |\n"
                "| Corticoïdes | HLM / HTG |\n"
                "| Rétinoïdes | HTG |\n"
                "| Antirétroviraux | HTG |\n"
                "| Ciclosporine | HCH / HLM |\n"
                "| Antipsychotiques | HLM / HTG |"
            )),
            FicheRow(concept="", detail_md=(
                "- Mnémonique des causes secondaires : **Hypothyroïdie, Cholestase, "
                "syndrome Néphrotique, IRC, Alcool, Diabète, Iatrogène**"
            ), kind="mnemo"),
            FicheRow(concept="", detail_md=(
                "- ⚠ Ne jamais oublier de rechercher une **hypothyroïdie** devant toute "
                "hypercholestérolémie : la **TSH** doit être systématique"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE IV : HYPERLIPIDÉMIES PRIMITIVES ──
    partie_iv = Partie(numero="IV", titre="Hyperlipidémies primitives", sous_parties=[
        SousPartie(lettre="A", titre="Hypercholestérolémies familiales monogéniques", rows=[
            FicheRow(concept="◆ Mutation du gène du LDL-récepteur (LDL-R)", detail_md=(
                "- Cause la plus fréquente d'hypercholestérolémie familiale monogénique\n"
                "- Existe sous 2 formes : **hétérozygote** (fréquente) et **homozygote** (très rare)"
            )),
            FicheRow(concept="◆ Caractéristiques : hétérozygote vs homozygote", detail_md=(
                "| Critère | Hétérozygote | Homozygote |\n"
                "|---------|--------------|------------|\n"
                "| Récepteurs LDL atteints | 50 % | ≈ 100 % |\n"
                "| Fréquence | 1/300 (80 % de mutations retrouvées) | 1/500 000 (très rare) |\n"
                "| LDL-C | 2 à 4 g/L | > 5 g/L |\n"
                "| Dépôts lipidiques | Xanthomes tendineux, arc cornéen prématuré (inconstants) | "
                "Xanthomes dès l'enfance |\n"
                "| Risque CV | Élevé | Complications dès la 1re décennie (incluant RAo) |"
            )),
            FicheRow(concept="◆ Score Dutch-HF", detail_md=(
                "- **Score clinicobiologique** d'aide au diagnostic de probabilité\n"
                "- Sommation de points associés à :\n"
                "  - Antécédents familiaux ou personnels (notamment maladie CV athéroscléreuse "
                "prématurée)\n"
                "  - Signes cliniques (xanthome)\n"
                "  - Niveau de LDL-C"
            )),
            FicheRow(concept="Mutation du gène de l'apoB (rare)", detail_md=(
                "- Mutation entraînant une moindre affinité des LDL pour leur récepteur (LDL-R)\n"
                "- Expression plus modérée : **LDL-C 2 à 3 g/L**\n"
                "- Xanthomes rares"
            )),
            FicheRow(concept="Mutation du gène de PCSK9 (très rare)", detail_md=(
                "- Mutation **« gain de fonction »** : ↑ affinité de PCSK9 pour LDL-R\n"
                "- Conséquence : dégradation du LDL-R après internalisation des LDL → "
                "non-réutilisation du récepteur"
            )),
        ]),
        SousPartie(lettre="B", titre="Hypercholestérolémies polygéniques", rows=[
            FicheRow(concept="◆ Caractéristiques", detail_md=(
                "- Hyperlipidémies très fréquentes\n"
                "- **LDL-C entre 1,3 et 2,5 g/L** le plus souvent\n"
                "- Une HTG est parfois associée\n"
                "- Prédisposition familiale polygénique\n"
                "- Physiopathologie multifactorielle\n"
                "- Sensibles à l'alimentation\n"
                "- Risque CV modulé par le niveau de cholestérol et les autres FDR"
            )),
        ]),
        SousPartie(lettre="C", titre="Hyperlipidémie familiale combinée", rows=[
            FicheRow(concept="◆ Caractéristiques", detail_md=(
                "- Fréquente : **1 à 2 %** de la population\n"
                "- Caractère polygénique probable\n"
                "- Phénotypes variables dans la famille (et chez un même individu selon poids "
                "et alimentation) :\n"
                "  - Hyperlipidémie mixte\n"
                "  - Hypercholestérolémie pure\n"
                "  - Hypertriglycéridémie pure"
            )),
            FicheRow(concept="◆ Expression typique (HLM modérée)", detail_md=(
                "- Cholestérol total : **2,5 à 3,5 g/L**\n"
                "- LDL-C : **1,6 à 2,5 g/L**\n"
                "- Triglycérides : **1,5 à 5 g/L**\n"
                "- Risque CV dépendant du niveau d'hyperlipidémie et des autres FDR associés"
            )),
        ]),
        SousPartie(lettre="D", titre="Dysbêtalipoprotéinémie (ex-type III)", rows=[
            FicheRow(concept="◆ Caractéristiques", detail_md=(
                "- Rare : fréquence **1/10 000 à 1/5 000**\n"
                "- 2 conditions nécessaires :\n"
                "  - Prédisposition génétique : isoforme **E2 de l'apoE** à l'état "
                "**homozygote E2/E2**\n"
                "  - + un autre facteur : surpoids, diabète, hypothyroïdie, certains traitements"
            )),
            FicheRow(concept="◆ Profil biologique", detail_md=(
                "- Cholestérol : **3 à 6 g/L**\n"
                "- Triglycérides : **4 à 10 g/L**\n"
                "- Lipidogramme : accumulation des **IDL** (intermediate density lipoproteins)\n"
                "- Typage de l'apoE pertinent"
            )),
            FicheRow(concept="◆ Signes cliniques caractéristiques", detail_md=(
                "- **Xanthomes plans palmaires**\n"
                "- **Xanthomes tubéreux jaune orangé**\n"
                "- Signes caractéristiques mais rares"
            )),
            FicheRow(concept="◆ Risque et traitement", detail_md=(
                "- Risque CV élevé\n"
                "- Traitement : diététique + statines\n"
                "- ⚠ Particularité : les **fibrates sont souvent efficaces** dans cette forme"
            )),
        ]),
        SousPartie(lettre="E", titre="Hypertriglycéridémies primitives", rows=[
            FicheRow(concept="◆ Hypertriglycéridémie familiale (ex-type IV)", detail_md=(
                "- Assez fréquente\n"
                "- HTG pure chez le sujet et les apparentés atteints\n"
                "- Diagnostics différentiels : HTG alimentaire, hyperlipidémie familiale combinée\n"
                "- Grande variabilité des TG selon surpoids, alcool et sucres\n"
                "- Chylomicronémie associée (type V) possible en cas de poussée majeure\n"
                "- Risque athérogène incertain\n"
                "- **Risque de pancréatite aiguë** si **TG > 10 g/L**"
            )),
            FicheRow(concept="◆ Hyperchylomicronémies primitives (ex-types I et V)", detail_md=(
                "- Très rares\n"
                "- **HTG majeure > 10 g/L**, pouvant atteindre 100 g/L\n"
                "- Type I : hyperchylomicronémie pure (enfant)\n"
                "- Type V : élévation des chylomicrons et des VLDL\n"
                "- Mutation génétique sous-jacente\n"
                "- **Risque majeur de pancréatite aiguë**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La **pancréatite aiguë** est le risque essentiel des HTG > 10 g/L : "
                "particulièrement à craindre dans les **hyperchylomicronémies primitives**"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE V : ÉVALUATION DU RISQUE CV ──
    partie_v = Partie(numero="V", titre="Évaluation du risque cardiovasculaire global", sous_parties=[
        SousPartie(lettre="A", titre="Outil SCORE2 / SCORE2-OP (ESC 2021)", rows=[
            FicheRow(concept="◆ SCORE2 en prévention primaire", detail_md=(
                "- Évalue le risque d'événement CV majeur à 10 ans :\n"
                "  - Infarctus du myocarde\n"
                "  - AVC\n"
                "  - Décès cardiovasculaire\n"
                "- Variables utilisées :\n"
                "  - Zone géographique\n"
                "  - Sexe\n"
                "  - Âge (**40 à 69 ans**)\n"
                "  - Statut tabagique\n"
                "  - Pression artérielle systolique\n"
                "  - **Cholestérol non-HDL** (= CT − HDL-C)"
            )),
            FicheRow(concept="◆ SCORE2-OP (Old Person)", detail_md=(
                "- Outil disponible pour les sujets d'âge **≥ 70 ans**"
            )),
            FicheRow(concept="◆ SCORE2-Diabetes (ESC 2023)", detail_md=(
                "- Estime le risque CV chez les personnes atteintes de **diabète de type 2** "
                "sans MCV athérosclérotique ni lésion grave d'organe cible"
            )),
            FicheRow(concept="◆ Limites de SCORE2", detail_md=(
                "- Outil non adapté dans les situations suivantes :\n"
                "  - Diabète (utiliser SCORE2-Diabetes)\n"
                "  - Insuffisance rénale chronique (DFG < 60 mL/min)\n"
                "  - Hypercholestérolémie familiale\n"
                "  - Maladie CV documentée (prévention secondaire)\n"
                "- Dans ces cas, le risque est d'emblée considéré comme **élevé ou très élevé**"
            )),
        ]),
        SousPartie(lettre="B", titre="Catégories de risque cardiovasculaire", rows=[
            FicheRow(concept="◆ 4 catégories de risque", detail_md=(
                "| Catégorie | Profil |\n"
                "|-----------|--------|\n"
                "| Faible-modéré à très élevé | Sujet apparemment sain selon SCORE2/SCORE2-OP |\n"
                "| Élevé | IRC : DFG 30-45 RAC<30, ou DFG 45-59 RAC 30-299, ou DFG>60 RAC>300 |\n"
                "| Élevé | Hypercholestérolémie familiale |\n"
                "| Élevé | Db type 2 ou Db type 1 > 40 ans, sans MCV, sans AOC, avec FDR ou > 10 ans |\n"
                "| Très élevé | IRC : DFG < 30, ou DFG 30-44 avec RAC > 30 |\n"
                "| Très élevé | Db avec MCV ou AOC sévère (IRC, microangiopathie 3 sites) |\n"
                "| Très élevé | Maladie CV établie : coronaire, AIT/AVC, AOMI (prévention secondaire) |"
            )),
            FicheRow(concept="◆ Risque selon âge et SCORE2 (sujet sain)", detail_md=(
                "| Catégorie | < 50 ans | 50-69 ans | ≥ 70 ans |\n"
                "|-----------|----------|-----------|----------|\n"
                "| Faible-modéré | < 2,5 % | < 5 % | < 7,5 % |\n"
                "| Élevé | 2,5-7,5 % | 5-10 % | 7,5-15 % |\n"
                "| Très élevé | > 7,5 % | > 10 % | > 15 % |\n"
                "- Traitement médicamenteux généralement non indiqué si risque faible-modéré\n"
                "- Traitement médicamenteux le plus souvent indiqué si risque élevé\n"
                "- Traitement médicamenteux généralement indiqué si risque très élevé"
            )),
            FicheRow(concept="Db bien contrôlé < 10 ans, sans AOC, sans FDR", detail_md=(
                "- Catégorie : **risque modéré**"
            )),
        ]),
        SousPartie(lettre="C", titre="Objectifs LDL-C selon le risque (ESC 2019)", rows=[
            FicheRow(concept="◆ Objectifs en prévention primaire", detail_md=(
                "| Catégorie | Objectif LDL-C (g/L) | Objectif LDL-C (mmol/L) |\n"
                "|-----------|----------------------|--------------------------|\n"
                "| Bas risque | < 1,15 | < 3 |\n"
                "| Risque modéré | < 1 | < 2,6 |\n"
                "| Risque élevé | < 0,70 | < 1,8 |\n"
                "| Risque très élevé | < 0,55 | < 1,4 |"
            )),
            FicheRow(concept="◆ Objectif en prévention secondaire", detail_md=(
                "- Toujours catégorie risque très élevé\n"
                "- **LDL-C < 0,55 g/L** (< 1,4 mmol/L)"
            )),
            FicheRow(concept="◆ Stratégie selon LDL-C et risque (ESC 2019)", detail_md=(
                "- En **bas risque** : conseils de mode de vie quel que soit le LDL-C ; "
                "médicaments seulement si LDL-C ≥ 1,9 g/L\n"
                "- En **risque modéré** : conseils de mode de vie ; médicaments si non contrôlé "
                "(à partir de 1 g/L) ou d'emblée si LDL-C ≥ 1,9 g/L\n"
                "- En **risque élevé** : médicaments d'emblée dès LDL-C ≥ 1 g/L "
                "(association systématique au-delà de 1,8 g/L environ)\n"
                "- En **risque très élevé** : médicaments d'emblée dès LDL-C ≥ 0,7 g/L\n"
                "- En **prévention secondaire** : médicaments d'emblée si LDL-C > 0,55 g/L"
            )),
            FicheRow(concept="", detail_md=(
                "- Mémoriser les 4 objectifs LDL-C : **1,15 / 1 / 0,7 / 0,55 g/L** "
                "(bas / modéré / élevé / très élevé)"
            ), kind="mnemo"),
        ]),
    ])

    # ── PARTIE VI : PRISE EN CHARGE THÉRAPEUTIQUE ──
    partie_vi = Partie(numero="VI", titre="Prise en charge thérapeutique", sous_parties=[
        SousPartie(lettre="A", titre="Objectifs thérapeutiques", rows=[
            FicheRow(concept="◆ LDL-C : cible principale", detail_md=(
                "- Le **LDL-C** est l'objectif thérapeutique principal\n"
                "- Les preuves de bénéfice CV reposent sur son abaissement\n"
                "- 4 objectifs définis selon les 4 catégories de risque\n"
                "- ⚠ Ces objectifs ne s'appliquent pas à l'**hypercholestérolémie familiale** "
                "(risque CV élevé d'emblée)"
            )),
            FicheRow(concept="◆ Stratégie générale ESC", detail_md=(
                "- Toujours donner des conseils de mode de vie\n"
                "- Envisager un traitement médicamenteux si LDL-C reste supérieur à l'objectif\n"
                "- Associer certainement un traitement médicamenteux si LDL-C reste nettement "
                "supérieur à l'objectif\n"
                "- Associer d'emblée un traitement médicamenteux si LDL-C > objectif en "
                "**prévention secondaire**"
            )),
        ]),
        SousPartie(lettre="B", titre="Traitement diététique", rows=[
            FicheRow(concept="◆ Indication universelle", detail_md=(
                "- Toujours indiqué en présence de toute anomalie lipidique et de "
                "tout facteur de risque\n"
                "- Poursuivi au long cours dans tous les cas\n"
                "- Délai avant traitement médicamenteux : **3 mois** si LDL-C reste éloigné de "
                "l'objectif (ou d'emblée si LDL-C très supérieur à l'objectif, surtout en "
                "prévention secondaire)"
            )),
            FicheRow(concept="◆ Modifications du régime alimentaire", detail_md=(
                "- Limitation acides gras saturés (graisses animales) **< 10-12 %** des calories\n"
                "- Suppression des **acides gras trans** (« partiellement hydrogénés »)\n"
                "- Augmentation des AG poly-insaturés oméga-3 (poissons)\n"
                "- Augmentation des fibres (fruits, légumes, céréales complètes)\n"
                "- Limitation modérée du cholestérol alimentaire : **œufs ≤ 3/semaine**\n"
                "- Aliments enrichis en stérols végétaux discutés"
            )),
            FicheRow(concept="◆ Régime méditerranéen", detail_md=(
                "- Recommandé pour son bénéfice cardiovasculaire\n"
                "- Huile d'olive\n"
                "- Fruits et légumes : **5 portions/jour**\n"
                "- Fruits à coque (noix, noisettes, amandes) : **30 g/jour**\n"
                "- Limiter l'alcool (surtout pour les TG)\n"
                "- Contrôle du poids et lutte contre la sédentarité"
            )),
            FicheRow(concept="◆ Mesures spécifiques aux HTG modérées", detail_md=(
                "- 4 facteurs importants :\n"
                "  - Réduction pondérale (notamment adiposité abdominale)\n"
                "  - Réduction de l'alcool\n"
                "  - Réduction des sucres\n"
                "  - Équilibrage d'un diabète associé\n"
                "- Ces mesures constituent l'essentiel du traitement ; les médicaments ont un "
                "impact mineur"
            )),
            FicheRow(concept="◆ HTG majeures (> 10 g/L) avec hyperchylomicronémie", detail_md=(
                "- Avis spécialisé nécessaire\n"
                "- Réduction de l'**apport lipidique < 30 g/jour**"
            )),
            FicheRow(concept="", detail_md=(
                "- **HTG modérée** : le traitement est avant tout nutritionnel "
                "(perte de poids, alcool, sucres, diabète). Les médicaments ont peu d'impact"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Traitement médicamenteux", rows=[
            FicheRow(concept="◆ Principes généraux", detail_md=(
                "- En prévention primaire : introduction après au moins **3 mois** de diététique "
                "bien suivie\n"
                "- Posologies initiales faibles ou modérées, adaptation progressive\n"
                "- En risque très élevé (a fortiori prévention secondaire) : traitement "
                "d'emblée avec posologies fortes cherchant à abaisser le LDL-C de **plus de 50 %**\n"
                "- ⚠ **Statines contre-indiquées en cas de grossesse**"
            )),
            FicheRow(concept="◆ HCH pures et HLM : 1er choix = statines", detail_md=(
                "- Bénéfice CV le mieux démontré\n"
                "- Molécules anciennes : **simvastatine, pravastatine**\n"
                "- Molécules récentes : **atorvastatine, rosuvastatine**\n"
                "- Réduction du LDL-C de **25 à 50 %** selon molécule et posologie"
            )),
            FicheRow(concept="◆ Si objectif non atteint", detail_md=(
                "- Intensifier le schéma thérapeutique :\n"
                "  - Augmenter jusqu'à la dose maximale tolérée\n"
                "  - Substituer par une statine plus puissante\n"
                "- À la dose maximale tolérée de statine, associer l'**ézétimibe (Ezetrol®)** : "
                "réduction supplémentaire d'environ **20 % du LDL-C**\n"
                "- En dernier lieu : association avec la **colestyramine (Questran®)**"
            )),
            FicheRow(concept="◆ 2e choix : intolérance aux statines", detail_md=(
                "- **Ézétimibe**\n"
                "- Voire **colestyramine**\n"
                "- Rarement les fibrates"
            )),
            FicheRow(concept="◆ HTG pures", detail_md=(
                "- TG entre **1,5 et 5 g/L** : traitement diététique seul\n"
                "- TG **> 5 g/L** malgré diététique bien suivie : **fibrate** (parallèlement à la "
                "diététique)\n"
                "- AGPI n-3 à forte posologie possibles (formulation non commercialisée en France "
                "en 2025)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Les **statines sont contre-indiquées pendant la grossesse**"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Hypercholestérolémie familiale hétérozygote", rows=[
            FicheRow(concept="◆ Dépistage en cascade", detail_md=(
                "- Recherche de la maladie chez les **apparentés du 1er degré** d'un patient "
                "diagnostiqué"
            )),
            FicheRow(concept="◆ Objectifs thérapeutiques", detail_md=(
                "- Jusqu'à 20 ans : **LDL-C < 1,3 g/L** (3,4 mmol/L)\n"
                "- Au-delà de 20 ans : objectifs des patients à risque CV élevé ou de "
                "prévention secondaire, selon la catégorie de risque du sujet"
            )),
            FicheRow(concept="◆ Traitement", detail_md=(
                "- Identique à celui de l'hypercholestérolémie isolée\n"
                "- En cas de résistance : avis spécialisé"
            )),
        ]),
        SousPartie(lettre="E", titre="Anticorps anti-PCSK9", rows=[
            FicheRow(concept="◆ Molécules disponibles", detail_md=(
                "- **Alirocumab (Praluent®)**\n"
                "- **Évolocumab (Repatha®)**\n"
                "- Immunoglobulines monoclonales humaines injectables (voie SC)"
            )),
            FicheRow(concept="◆ Effet", detail_md=(
                "- Diminution du LDL-C de **50 %** en plus de la baisse obtenue avec les statines\n"
                "- Réduction démontrée des événements CV dans des essais randomisés vs placebo"
            )),
            FicheRow(concept="◆ Indications remboursables (France)", detail_md=(
                "- Coût élevé → accord préalable de l'assurance maladie nécessaire\n"
                "- Chez l'adulte, dans les situations suivantes :\n"
                "  - **Prévention secondaire** d'une maladie CV avérée\n"
                "  - Patient dont le **LDL-C reste > 0,7 g/L** malgré un traitement hypolipémiant "
                "optimisé comprenant au moins une statine à dose maximale tolérée "
                "(poursuivie)"
            )),
        ]),
    ])

    # ── PARTIE VII : SURVEILLANCE ──
    partie_vii = Partie(numero="VII", titre="Surveillance du traitement hypolipémiant", sous_parties=[
        SousPartie(lettre="A", titre="Efficacité du traitement", rows=[
            FicheRow(concept="◆ Bilan lipidique de contrôle", detail_md=(
                "- Délai : **8 à 12 semaines** après l'instauration de la prise en charge\n"
                "- Bilan lipidique également 8 à 12 semaines après chaque adaptation du "
                "traitement, jusqu'à l'obtention des valeurs cibles"
            )),
        ]),
        SousPartie(lettre="B", titre="Tolérance musculaire", rows=[
            FicheRow(concept="◆ Myalgies sous statines", detail_md=(
                "- Effet indésirable le plus fréquent des hypolipémiants, notamment des "
                "**statines**\n"
                "- Surveillance essentiellement clinique"
            )),
            FicheRow(concept="◆ Dosage des CPK", detail_md=(
                "- Pas de dosage systématique\n"
                "- Indiqué dans les situations à risque suivantes :\n"
                "  - Douleurs musculaires\n"
                "  - Insuffisance rénale modérée à sévère\n"
                "  - Hypothyroïdie\n"
                "  - ATCD personnel ou familial de maladie musculaire génétique\n"
                "  - Abus d'alcool\n"
                "  - Âge > 70 ans"
            )),
            FicheRow(concept="◆ Arrêt des statines", detail_md=(
                "- Recommandé pour **CPK > 5 N**\n"
                "- À distance d'une activité sportive"
            )),
        ]),
        SousPartie(lettre="C", titre="Tolérance hépatique", rows=[
            FicheRow(concept="◆ Modalités du suivi des ALAT", detail_md=(
                "- Avant le traitement\n"
                "- **8 à 12 semaines** après le début du traitement médicamenteux ou après toute "
                "augmentation de posologie\n"
                "- Puis tous les ans si **ALAT < 3 N**"
            )),
            FicheRow(concept="◆ ALAT > 3 N", detail_md=(
                "- Arrêter la statine ou réduire la posologie\n"
                "- Contrôler les enzymes hépatiques après **4 à 6 semaines**"
            )),
            FicheRow(concept="", detail_md=(
                "- **Surveillance des statines** : bilan lipidique à 2-3 mois ; "
                "myalgies cliniques ; transaminases à 3 mois ; **CPK** uniquement si "
                "symptômes ou situation à risque"
            ), kind="a_retenir"),
        ]),
    ])

    tableaux = [
        TableauSynthese(titre="Synthèse - Classification pragmatique des dyslipidémies", markdown=(
            "| Type | Définition | Ex-type Fredrickson |\n"
            "|------|------------|----------------------|\n"
            "| Hypercholestérolémie pure (HCH) | LDL-C > 1,60 g/L | IIa |\n"
            "| Hypertriglycéridémie pure (HTG) | TG > 1,5 g/L | IV |\n"
            "| Hyperlipidémie mixte (HLM) | HCH + HTG associées | IIb (rarement III) |\n"
            "| Hypo-HDLémie | HDL-C < 0,40 g/L (H), < 0,50 g/L (F) | Associée aux 3 précédents |"
        )),
        TableauSynthese(titre="Synthèse - Hyperlipidémies secondaires", markdown=(
            "| Étiologie | Outil diagnostique | Type d'hyperlipidémie |\n"
            "|-----------|--------------------|------------------------|\n"
            "| Hypothyroïdie | TSH | HCH / HLM |\n"
            "| Cholestase | Bilirubine, PAL | HCH |\n"
            "| Syndrome néphrotique | Protéinurie, œdèmes | HLM |\n"
            "| Insuffisance rénale chronique | Créatinine | HTG / HLM |\n"
            "| Alcoolisme | Interrogatoire | HTG |\n"
            "| Diabète | Glycémie, HbA1c | HTG |\n"
            "| Œstrogènes | Interrogatoire | HTG |\n"
            "| Corticoïdes | Interrogatoire | HLM / HTG |\n"
            "| Rétinoïdes | Interrogatoire | HTG |\n"
            "| Antirétroviraux | Interrogatoire | HTG |\n"
            "| Ciclosporine | Interrogatoire | HCH / HLM |\n"
            "| Antipsychotiques | Interrogatoire | HLM / HTG |"
        )),
        TableauSynthese(titre="Synthèse - Hyperlipidémies primitives", markdown=(
            "| Type | Fréquence | Profil lipidique | Particularités |\n"
            "|------|-----------|-------------------|-----------------|\n"
            "| HCH familiale hétérozygote (LDL-R) | 1/300 | LDL-C 2-4 g/L | Xanthomes tendineux, arc cornéen |\n"
            "| HCH familiale homozygote (LDL-R) | 1/500 000 | LDL-C > 5 g/L | Xanthomes enfance, RAo précoce |\n"
            "| HCH par mutation apoB | Rare | LDL-C 2-3 g/L | Xanthomes rares |\n"
            "| HCH par mutation PCSK9 | Très rare | Variable | Gain de fonction |\n"
            "| HCH polygénique | Très fréquente | LDL-C 1,3-2,5 g/L | Sensible à l'alimentation |\n"
            "| Hyperlipidémie familiale combinée | 1-2 % | CT 2,5-3,5 ; LDL 1,6-2,5 ; TG 1,5-5 g/L | Phénotype variable |\n"
            "| Dysbêtalipoprotéinémie | 1/5 000-10 000 | CT 3-6 g/L ; TG 4-10 g/L | apoE E2/E2 + facteur, xanthomes plans |\n"
            "| HTG familiale (type IV) | Fréquente | TG variables | Risque athérogène incertain |\n"
            "| Hyperchylomicronémies (I et V) | Très rares | TG > 10 g/L (jusqu'à 100) | Risque majeur pancréatite |"
        )),
        TableauSynthese(titre="Synthèse - Objectifs LDL-C selon le risque CV (ESC 2019)", markdown=(
            "| Catégorie de risque | LDL-C (g/L) | LDL-C (mmol/L) |\n"
            "|---------------------|--------------|-----------------|\n"
            "| Bas risque | < 1,15 | < 3,0 |\n"
            "| Risque modéré | < 1,0 | < 2,6 |\n"
            "| Risque élevé | < 0,70 | < 1,8 |\n"
            "| Risque très élevé (et prévention secondaire) | < 0,55 | < 1,4 |"
        )),
        TableauSynthese(titre="Synthèse - Stratégie thérapeutique selon la dyslipidémie", markdown=(
            "| Dyslipidémie | 1er choix | 2e choix / Associations |\n"
            "|--------------|-----------|---------------------------|\n"
            "| HCH pure / HLM | Statine | Statine + ézétimibe ; puis colestyramine ; ézétimibe seul si intolérance |\n"
            "| HTG 1,5-5 g/L | Diététique seule | - |\n"
            "| HTG > 5 g/L malgré diététique | Fibrate | AGPI n-3 (non commercialisé en France 2025) |\n"
            "| Dysbêtalipoprotéinémie | Diététique + statine | Fibrates souvent efficaces |\n"
            "| HCH familiale + statine max tolérée + LDL > 0,7 g/L | Statine + anti-PCSK9 (prévention secondaire) | Alirocumab / Évolocumab SC |\n"
            "| Grossesse | CI aux statines | Diététique seule |"
        )),
        TableauSynthese(titre="Synthèse - Surveillance du traitement", markdown=(
            "| Paramètre | Moment | Seuil d'action |\n"
            "|-----------|--------|----------------|\n"
            "| Bilan lipidique | 8-12 semaines après instauration, puis après chaque adaptation | Atteinte de la cible |\n"
            "| Myalgies | Clinique systématique | Selon symptômes |\n"
            "| CPK | Si symptômes ou situation à risque | Arrêt si > 5 N |\n"
            "| ALAT | Avant traitement, 8-12 semaines, puis annuel | Arrêt/réduction si > 3 N, contrôle 4-6 semaines |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Bilan lipidique normal (LDL-C) | < 1,6 g/L | Sujet sans autre FDR |\n"
        "| Bilan lipidique normal (HDL-C) | > 0,4 g/L | Sujet sans autre FDR |\n"
        "| Bilan lipidique normal (TG) | < 1,5 g/L | Sujet sans autre FDR |\n"
        "| Hypo-HDLémie | < 0,40 g/L (H) / < 0,50 g/L (F) | Critère |\n"
        "| Formule de Friedewald (g/L) | LDL-C = CT − HDL-C − TG/5 | Valable si TG < 3,5 g/L |\n"
        "| Formule de Friedewald (mmol/L) | LDL-C = CT − HDL-C − TG/2,2 | - |\n"
        "| Conversion cholestérol | g/L × 2,58 = mmol/L | - |\n"
        "| Conversion triglycérides | g/L × 1,14 = mmol/L | - |\n"
        "| Recontrôle bilan lipidique | 5 ans | Si bilan normal |\n"
        "| HCH familiale hétérozygote | 1/300 ; LDL-C 2-4 g/L | LDL-R |\n"
        "| HCH familiale homozygote | 1/500 000 ; LDL-C > 5 g/L | LDL-R |\n"
        "| Dysbêtalipoprotéinémie | 1/5 000 à 1/10 000 | apoE E2/E2 + facteur |\n"
        "| HTG familiale | TG variables | Risque pancréatite si > 10 g/L |\n"
        "| Pancréatite aiguë | TG > 10 g/L | Hyperchylomicronémies |\n"
        "| Hyperchylomicronémie majeure | TG jusqu'à 100 g/L | Type I ou V |\n"
        "| Objectif LDL-C bas risque | < 1,15 g/L (< 3 mmol/L) | ESC 2019 |\n"
        "| Objectif LDL-C risque modéré | < 1 g/L (< 2,6 mmol/L) | ESC 2019 |\n"
        "| Objectif LDL-C risque élevé | < 0,70 g/L (< 1,8 mmol/L) | ESC 2019 |\n"
        "| Objectif LDL-C risque très élevé | < 0,55 g/L (< 1,4 mmol/L) | ESC 2019 et prévention secondaire |\n"
        "| HCH familiale jusqu'à 20 ans | LDL-C < 1,3 g/L (3,4 mmol/L) | Cible spécifique |\n"
        "| Délai pré-traitement médicamenteux | 3 mois | Diététique seule en prévention primaire |\n"
        "| Acides gras saturés | < 10-12 % des calories | Diététique |\n"
        "| Cholestérol alimentaire (œufs) | ≤ 3/semaine | Diététique |\n"
        "| Fruits et légumes | 5 portions/jour | Régime méditerranéen |\n"
        "| Fruits à coque | 30 g/jour | Régime méditerranéen |\n"
        "| Apport lipidique (HTG majeure) | < 30 g/jour | Hyperchylomicronémie |\n"
        "| Baisse LDL-C avec statine | 25 à 50 % | Selon molécule et dose |\n"
        "| Baisse LDL-C avec statine + ézétimibe | + 20 % | Association |\n"
        "| Anti-PCSK9 : baisse LDL-C | 50 % | En plus des statines |\n"
        "| Remboursement anti-PCSK9 | LDL-C > 0,7 g/L sous statine max tolérée | Prévention secondaire |\n"
        "| Objectif LDL-C en risque très élevé | Baisse > 50 % | Cible visée |\n"
        "| Bilan lipidique de contrôle | 8-12 semaines | Après instauration ou adaptation |\n"
        "| Arrêt statine | CPK > 5 N | À distance d'une activité sportive |\n"
        "| Arrêt/réduction statine | ALAT > 3 N | Contrôle après 4-6 semaines |\n"
        "| SCORE2 | 40-69 ans, prévention primaire | ESC 2021 |\n"
        "| SCORE2-OP | ≥ 70 ans | Old Person |\n"
        "| SCORE2-Diabetes | Diabète type 2 sans MCV ni AOC | ESC 2023 |\n"
        "| Limite Friedewald | TG ≥ 3,5 g/L | Formule non valable |"
    ))

    points_cles = [
        "Risque CV gradué avec **LDL-C** (+) et **HDL-C** (−) ; **pancréatite aiguë** si **HTG > 10 g/L**",
        "**EAL** = CT, HDL-C, TG ; **Friedewald** : LDL-C = CT − HDL-C − TG/5 ; non valable si **TG ≥ 3,5 g/L**",
        "Bilan normal : **LDL < 1,6** / **HDL > 0,4** / **TG < 1,5 g/L** (simultanés)",
        "Classification : **HCH** (LDL > 1,6), **HTG** (TG > 1,5), **HLM** (association des deux)",
        "Causes secondaires : hypothyroïdie (**TSH systématique**), cholestase, sd néphrotique, IRC, diabète, alcool",
        "**HCH familiale** : LDL-R (1/300 hétéro, 1/500 000 homo), apoB, PCSK9 ; score **Dutch-HF**",
        "Risque CV : **SCORE2** (40-69 ans) / **SCORE2-OP** (≥ 70 ans) ; 4 catégories (bas/modéré/élevé/très élevé)",
        "Objectifs **LDL-C** : **1,15 / 1 / 0,70 / 0,55 g/L** (bas / modéré / élevé / très élevé = prévention secondaire)",
        "**HCH/HLM** : statine 1er choix (− 25-50 %) ± ézétimibe (− 20 %) ± colestyramine ; **CI grossesse**",
        "Surveillance : bilan à **8-12 sem** ; arrêt si **CPK > 5 N** ou **ALAT > 3 N**",
    ]

    fiche_eclair_md = (
        "**Définition** : anomalies du bilan lipidique exposant au risque CV athéromateux (LDL-C +, HDL-C −) ; pancréatite aiguë si HTG > 10 g/L.\n\n"
        "**EAL** : CT, HDL-C, TG. LDL-C = CT − HDL-C − TG/5 (Friedewald, non valable si TG ≥ 3,5 g/L). Bilan normal : LDL < 1,6 / HDL > 0,4 / TG < 1,5 g/L.\n\n"
        "**Classification** : HCH pure (LDL > 1,6), HTG pure (TG > 1,5), HLM (association). Hypo-HDL : H < 0,40 / F < 0,50 g/L.\n\n"
        "**Causes secondaires** : hypothyroïdie (TSH systématique), cholestase, syndrome néphrotique, IRC, diabète, alcool. Iatrogènes : corticoïdes, œstrogènes, rétinoïdes, antirétroviraux, ciclosporine, antipsychotiques.\n\n"
        "**HCH familiale monogénique** : LDL-R (1/300 hétéro, 1/500 000 homo), apoB rare, PCSK9 très rare. Score Dutch-HF. Xanthomes tendineux, arc cornéen.\n\n"
        "**HCH polygénique** : très fréquente, LDL 1,3-2,5. Hyperlipidémie familiale combinée : 1-2 %, HLM modérée. Dysbêta : apoE E2/E2 + facteur. Hyperchylomicronémies (I, V) : TG > 10, risque pancréatite.\n\n"
        "**Risque CV (ESC 2021)** : SCORE2 (40-69 ans), SCORE2-OP (≥ 70), SCORE2-Diabetes. 4 catégories. D'emblée élevé : HCH familiale, IRC, diabète. Très élevé : IRC sévère, prévention secondaire.\n\n"
        "**Objectifs LDL-C (ESC 2019)** : 1,15 / 1 / 0,70 / 0,55 g/L (bas / modéré / élevé / très élevé).\n\n"
        "**Diététique** : toujours, au long cours. Régime méditerranéen, AGS < 10-12 %, 5 fruits/légumes, 30 g fruits à coque, œufs ≤ 3/sem.\n\n"
        "**HCH/HLM** : statine 1er choix (− 25-50 %), + ézétimibe (− 20 %), puis colestyramine. CI grossesse.\n\n"
        "**HTG pure** : diététique seule si 1,5-5 g/L ; fibrate si > 5 g/L. HTG > 10 + chylomicronémie : avis spé, lipides < 30 g/j.\n\n"
        "**Anti-PCSK9** (alirocumab, évolocumab) SC : − 50 %. Remboursés en prévention secondaire ou LDL > 0,7 g/L sous statine max.\n\n"
        "**Surveillance** : bilan à 8-12 semaines. Myalgies cliniques, CPK si symptômes (arrêt > 5 N). ALAT avant + 3 mois + annuel (arrêt si > 3 N, contrôle 4-6 sem)."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 223 - Dyslipidémies",
        annee="2025-2026",
        item="Item 223",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi, partie_vii],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 223",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-223_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

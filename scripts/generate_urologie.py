"""Génère la fiche exhaustive d'Urologie à partir du PDF source."""

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
from major_ecn.docx_generator import render_docx


def build_fiche() -> FicheData:
    plan = [
        PlanPartie(numero="I", titre="Hématurie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition et étiologies"),
            PlanSousPartie(lettre="B", titre="Diagnostic positif et fausses hématuries"),
            PlanSousPartie(lettre="C", titre="Conduite à tenir et examens complémentaires"),
            PlanSousPartie(lettre="D", titre="Prise en charge"),
        ]),
        PlanPartie(numero="II", titre="Cancer de la prostate", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et présentation clinique"),
            PlanSousPartie(lettre="B", titre="Examens diagnostiques et classification"),
            PlanSousPartie(lettre="C", titre="Bilan d'extension et classification TNM"),
            PlanSousPartie(lettre="D", titre="Options thérapeutiques"),
            PlanSousPartie(lettre="E", titre="Stratégie thérapeutique et suivi"),
        ]),
        PlanPartie(numero="III", titre="Troubles de l'érection et urgences péniennes", sous_parties=[
            PlanSousPartie(lettre="A", titre="Dysfonction érectile"),
            PlanSousPartie(lettre="B", titre="Maladie de Lapeyronie et fracture des corps caverneux"),
            PlanSousPartie(lettre="C", titre="Priapisme"),
        ]),
        PlanPartie(numero="IV", titre="Rétention aiguë d'urine", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition et tableau clinique"),
            PlanSousPartie(lettre="B", titre="Étiologies"),
            PlanSousPartie(lettre="C", titre="Examens complémentaires et prise en charge"),
        ]),
        PlanPartie(numero="V", titre="Lithiase urinaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et composition des calculs"),
            PlanSousPartie(lettre="B", titre="Colique néphrétique aiguë"),
            PlanSousPartie(lettre="C", titre="Examens complémentaires et traitement en urgence"),
            PlanSousPartie(lettre="D", titre="Prise en charge à long terme et traitement chirurgical"),
        ]),
        PlanPartie(numero="VI", titre="Infections urinaires", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et microbiologie"),
            PlanSousPartie(lettre="B", titre="Cystite aiguë"),
            PlanSousPartie(lettre="C", titre="Pyélonéphrite aiguë"),
            PlanSousPartie(lettre="D", titre="Prostatite"),
        ]),
        PlanPartie(numero="VII", titre="Infections génitales et HBP", sous_parties=[
            PlanSousPartie(lettre="A", titre="Urétrite aiguë et orchi-épididymite"),
            PlanSousPartie(lettre="B", titre="Hypertrophie bénigne de la prostate"),
            PlanSousPartie(lettre="C", titre="Traitement médical et chirurgical de l'HBP"),
        ]),
    ]

    # ── PARTIE I : HÉMATURIE ──
    partie_i = Partie(numero="I", titre="Hématurie", sous_parties=[
        SousPartie(lettre="A", titre="Définition et étiologies", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Hématurie** : présence quantité anormale d'hématies dans les urines "
                "(> **10/mm³** ou 10⁴/mL) lors de la miction\n"
                "- **Hématurie macroscopique** :\n"
                "  - Coloration rouge, rosée ou brunâtre visible à l'oeil nu\n"
                "  - > 500 hématies/mm³\n"
                "  - Sans caillots : oriente vers origine **glomérulaire**\n"
                "  - Avec caillots : oriente vers origine **urologique**\n"
                "- **Hématurie microscopique** : invisible à l'oeil nu, > 10 hématies/mm³"
            )),
            FicheRow(concept="Étiologies urologiques", detail_md=(
                "| Fréquence | Étiologies |\n"
                "|-----------|------------|\n"
                "| **Fréquentes** | Infections urinaires, tumeurs vésicales, cancer du rein, lithiase rénale, cancer prostatique, prostatite aiguë |\n"
                "| **Contexte particulier** | Traumatisme rein/voies urinaires |\n"
                "| **Rares** | Polykystose rénale, angiomyolipome, tumeurs voie excrétrice supérieure, tuberculose rénale, bilharziose, drépanocytose |\n"
                "| **Iatrogènes** | Anticoagulants, cyclophosphamide |\n"
            )),
            FicheRow(concept="Étiologies parenchymateuses", detail_md=(
                "- Hématurie **totale**, **indolore**, **sans caillot**\n"
                "- Le plus souvent glomérulaires :\n"
                "  - GN à dépôts mésangiaux d'IgA\n"
                "  - GN post-infectieuse\n"
                "  - GN membranoproliférative\n"
                "  - GN extracapillaire\n"
                "  - Syndrome d'Alport\n"
                "- Parfois néphrite interstitielle aiguë médicamenteuse"
            )),
            FicheRow(concept="", detail_md=(
                "- L'hématurie **sans caillots** oriente vers une origine **glomérulaire**\n"
                "- L'hématurie **avec caillots** oriente vers une origine **urologique**\n"
                "- Toujours éliminer les **fausses hématuries** avant d'explorer"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Diagnostic positif et fausses hématuries", rows=[
            FicheRow(concept="Circonstances de découverte", detail_md=(
                "- Hématurie macroscopique : clinique\n"
                "- Hématurie microscopique : découverte sur **BU** (urines du matin, fraîchement émises, après toilette génitale)\n"
                "- Contexte : enquête HTA, OMI, insuffisance rénale, protéinurie, ATCD néphropathie familiale"
            )),
            FicheRow(concept="⚠ Fausses hématuries", detail_md=(
                "- **Hématurie de voisinage** :\n"
                "  - Urétrorragie : persistance saignement hors mictions\n"
                "  - Génitale, hémospermie\n"
                "- **Coloration alimentaire** : betteraves, mûres, myrtilles, rhubarbe, chou rouge\n"
                "- **Coloration médicamenteuse** : rifampicine, érythromycine, métronidazole, aspirine, ibuprofène, vitamine B12\n"
                "- **Origine métabolique** : hémoglobinurie (hémolyse), myoglobinurie (rhabdomyolyse), porphyrie\n"
                "- **Intoxications** : plomb, mercure"
            )),
            FicheRow(concept="Confirmation diagnostique", detail_md=(
                "- **ECBU** avec examen direct du sédiment urinaire\n"
                "- Hématurie confirmée si > **10 hématies/mm³** à l'examen cytologique quantitatif\n"
                "- Orientation glomérulaire si :\n"
                "  - Présence de **cylindres hématiques**\n"
                "  - Présence de **déformations des hématies**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La rifampicine et les betteraves sont les causes les plus fréquentes de fausses hématuries\n"
                "- ⚠ L'urétrorragie (saignement hors miction) n'est PAS une hématurie"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Conduite à tenir et examens complémentaires", rows=[
            FicheRow(concept="Interrogatoire", detail_md=(
                "- Origine ethnique, notion de voyage en zone d'endémie (bilharziose, tuberculose)\n"
                "- ATCD familiaux : PKRAD, cancers, insuffisance rénale, surdité héréditaire\n"
                "- ATCD personnels : diabète, drépanocytose, troubles coagulation, infections urinaires, lithiase\n"
                "- Traitements : **anticoagulants**, AAP, AINS\n"
                "- FDR de **carcinome urothélial**"
            )),
            FicheRow(concept="◆ Chronologie mictionnelle", detail_md=(
                "| Chronologie | Localisation suggérée |\n"
                "|-------------|----------------------|\n"
                "| **Initiale** (début de miction) | Urétroprostatique |\n"
                "| **Terminale** (fin de miction) | Vésicale |\n"
                "| **Totale** | Rénale |\n"
            )),
            FicheRow(concept="Examen clinique", detail_md=(
                "- Recherche fièvre, AEG, douleurs osseuses\n"
                "- Palpation hypogastrique : recherche **globe vésical**\n"
                "- Percussion fosses lombaires : douleur de CN\n"
                "- Recherche **varicocèle** : évocateur de tumeur rénale gauche\n"
                "- **TR** : recherche HBP, cancer prostate, masse pelvienne\n"
                "- Inspection et palpation MI : recherche oedèmes"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- **ECBU** systématique (éliminer infection urinaire)\n"
                "- Protéinurie des 24h (> **2 g/j** : évocatrice d'atteinte glomérulaire)\n"
                "- NFS-plaquettes, TP, TCA (retentissement)\n"
                "- Urée, créatinine (fonction rénale)\n"
                "- **Cytologie urinaire** (urines du matin) : détection tumeurs vésicales\n"
                "- Si origine urologique : **uroscanner+++**, fibroscopie vésicale\n"
                "- Si suspicion néphrologique : CAT spécifique"
            )),
        ]),
        SousPartie(lettre="D", titre="Prise en charge", rows=[
            FicheRow(concept="Traitement", detail_md=(
                "- **Traitement étiologique**\n"
                "- Si hématurie macroscopique importante avec caillotage et/ou RAU :\n"
                "  - **Sonde vésicale double courant** (ECBU lors de la pose)\n"
                "  - Irrigations/lavages en continu +/- décaillotages à la seringue\n"
                "  - Surveillance volumes d'entrées/sorties\n"
                "- **CI cathéter sus-pubien** en cas d'hématurie macroscopique"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Le cathéter sus-pubien est **contre-indiqué** en cas d'hématurie macroscopique\n"
                "- Toujours réaliser un ECBU lors de la pose de sonde vésicale"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE II : CANCER DE LA PROSTATE ──
    partie_ii = Partie(numero="II", titre="Cancer de la prostate", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et présentation clinique", rows=[
            FicheRow(concept="Épidémiologie", detail_md=(
                "- **Cancer le plus fréquent** chez l'homme > 50 ans\n"
                "- Incidence sur séries autopsiques H > 90 ans : **70%**\n"
                "- 1/8 français aura un cancer de la prostate au cours de sa vie\n"
                "- **2ème cause de décès** par cancer chez l'homme (après poumon), mortalité en baisse\n"
                "- 10% des décès par cancer\n"
                "- Exceptionnel avant 40 ans"
            )),
            FicheRow(concept="Facteurs de risque", detail_md=(
                "- Patients **afro-antillais**\n"
                "- ATCD familial de cancer de la prostate :\n"
                "  - 2 parents collatéraux\n"
                "  - Survenue chez un parent < 55 ans\n"
                "  - 3 membres d'une famille atteints : **RR = 11**"
            )),
            FicheRow(concept="Histologie", detail_md=(
                "- **90% adénocarcinome**, se développant au niveau de la **zone périphérique**\n"
                "- Carcinome neuroendocrine, sarcome prostatique : très rare"
            )),
            FicheRow(concept="Présentation clinique", detail_md=(
                "- **Asymptomatique** le plus souvent\n"
                "- Cancer localement avancé/métastatique :\n"
                "  - Troubles urinaires irritatifs/obstructifs\n"
                "  - Hémospermie, hématurie\n"
                "  - AEG, **douleurs osseuses** (métastases)\n"
                "  - Signes neurologiques : syndrome de la queue de cheval (compression médullaire)"
            )),
            FicheRow(concept="TR", detail_md=(
                "- **Examen clé** qui recherche :\n"
                "  - Nodule **dur**, **irrégulier**, **non douloureux**\n"
                "  - Envahissement capsule, vésicules séminales\n"
                "- Devant toute anomalie au TR : **biopsies de la prostate**"
            )),
            FicheRow(concept="", detail_md=(
                "- Le cancer de la prostate est le plus souvent **asymptomatique** au stade localisé\n"
                "- Le TR et le PSA sont les 2 examens du dépistage individuel\n"
                "- Pas de dépistage systématique, dépistage individuel à partir de **50 ans** (45 ans si FDR)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Examens diagnostiques et classification", rows=[
            FicheRow(concept="Dosage PSA", detail_md=(
                "- Valeur normale : < **4 ng/mL**\n"
                "- Adaptation selon l'âge :\n"
                "  - 50-60 ans : < 3 ng/mL\n"
                "  - 60-70 ans : < 4 ng/mL\n"
                "  - > 70 ans : < 5 ng/mL\n"
                "- **Non spécifique** du cancer de la prostate"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Le PSA est **non spécifique** : il peut être élevé dans l'HBP, la prostatite, "
                "après biopsie, éjaculation, TR\n"
                "- Un PSA normal n'exclut pas un cancer"
            ), kind="piege"),
            FicheRow(concept="Biopsies prostatiques", detail_md=(
                "- Biopsies **échoguidées** avec examen anatomopathologique\n"
                "- Indications : suspicion au TR, progression/élévation PSA\n"
                "- Minimum **12 prélèvements** (6 dans chaque lobe)\n"
                "- Modalités :\n"
                "  - ECBU négatif avant procédure\n"
                "  - Arrêt anticoagulants 5-7 jours avant\n"
                "  - Voie **transrectale** : antibioprophylaxie + badigeon rectal povidone iodée\n"
                "  - Voie **transpérinéale** : pas d'antibioprophylaxie, badigeon cutané périnée"
            )),
            FicheRow(concept="Complications biopsies", detail_md=(
                "- Rétention d'urine, douleurs périnéales\n"
                "- Malaise vagal, hypotension\n"
                "- **Prostatite aiguë** (2%), septicémie\n"
                "- Urétrorragie, rectorragie, hémospermie, hématurie\n"
                "- Dysfonctionnement érectile transitoire"
            )),
            FicheRow(concept="Score de Gleason", detail_md=(
                "- **Facteur pronostic essentiel**\n"
                "- Score histopronostic : addition des 2 grades histologiques (1-5)\n"
                "- **Score 6** : cancer bien différencié, bon pronostic\n"
                "- **Score 7** : moyennement différencié (4+3 ≠ 3+4 : agressivité différente)\n"
                "- **Score 8-10** : peu différencié, **mauvais pronostic**"
            )),
            FicheRow(concept="◆ Classification d'Amico", detail_md=(
                "| Risque | PSA | Gleason | Stade clinique |\n"
                "|--------|-----|---------|----------------|\n"
                "| **Faible** | < 10 ng/mL | ≤ 6 | T1c-T2a |\n"
                "| **Intermédiaire** | 10-20 ng/mL | 7 | T2b |\n"
                "| **Élevé** | > 20 ng/mL | ≥ 8 | ≥ T2c |\n"
            )),
            FicheRow(concept="Rapport PSA libre/total", detail_md=(
                "- En seconde intention si PSA élevé + 1ère série de biopsies négatives\n"
                "- **PSA L/T < 20%** : en faveur cancer/prostatite → 2ème série de biopsies\n"
                "- **PSA L/T > 20%** : en faveur **HBP**"
            )),
        ]),
        SousPartie(lettre="C", titre="Bilan d'extension et classification TNM", rows=[
            FicheRow(concept="◆ Bilan d'extension", detail_md=(
                "| Risque | Bilan |\n"
                "|--------|-------|\n"
                "| **Faible** | IRM prostatique et pelvienne |\n"
                "| **Intermédiaire favorable** | IRM prostatique et pelvienne |\n"
                "| **Intermédiaire défavorable / Haut risque** | **TEP PSMA** (à défaut TEP choline, à défaut scintigraphie osseuse + scanner TAP) |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Le bilan d'extension ne doit **pas retarder** la prise en charge curative\n"
                "- La TEP PSMA remplace progressivement la scintigraphie osseuse"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Options thérapeutiques", rows=[
            FicheRow(concept="Mesures générales", detail_md=(
                "- Prise en charge **pluridisciplinaire** en **RCP**\n"
                "- Urologues, oncologues, radiothérapeutes, radiologues, anatomopathologistes\n"
                "- Établissement PPS, prise en charge 100%, soutien psychologique"
            )),
            FicheRow(concept="Surveillance active", detail_md=(
                "- PSA tous les 3-6 mois (temps de doublement)\n"
                "- TR tous les 6-12 mois\n"
                "- Nouvelles biopsies entre 3-6 mois après biopsie initiale\n"
                "- Si aggravation : envisager traitement actif"
            )),
            FicheRow(concept="Prostatectomie totale", detail_md=(
                "- Exérèse complète prostate + vésicules séminales\n"
                "- Curage ilio-obturateur bilatéral si risque intermédiaire/élevé\n"
                "- Anastomose vésico-urétrale\n"
                "- **Effets indésirables** :\n"
                "  - IU : régresse dans les semaines/mois (10%)\n"
                "  - **Dysfonction érectile** (60%)\n"
                "  - Infertilité et anéjaculation : **constantes**"
            )),
            FicheRow(concept="Radiothérapie externe", detail_md=(
                "- Technique conformationnelle tridimensionnelle\n"
                "- 70 Gy en 6 semaines (5 séances/semaine)\n"
                "- Effets indésirables : cystite/rectite radique, dysfonction érectile (50%)\n"
                "- CI : ATCD irradiation pelvienne, maladie inflammatoire rectale"
            )),
            FicheRow(concept="Curiethérapie", detail_md=(
                "- Grains d'**iode 125** par voie transpérinéale\n"
                "- Non indiquée si : prostate > 50 mL, lobe médian, ATCD résection endoscopique"
            )),
            FicheRow(concept="Suppression androgénique", detail_md=(
                "- **Objectif** : testostéronémie < **0,5 ng/mL** et PSA < 1 ng/mL\n"
                "- **Agonistes LHRH** (triptoréline, leuproréline) :\n"
                "  - Commencer **anti-androgène 10j avant** + 1 mois après : prévention **effet flare-up**\n"
                "- **Antagonistes LHRH** (dégarelix) : effondrement testostéronémie immédiat\n"
                "- **Anti-androgènes** : cyprotérone (stéroïdien), bicalutamide (non stéroïdien)"
            )),
            FicheRow(concept="◆ EI suppression androgénique", detail_md=(
                "- Chute libido, dysfonction érectile\n"
                "- Bouffées de chaleur, gynécomastie\n"
                "- **Syndrome métabolique** : ostéoporose, diabète, HTA, prise de poids, cardiopathies\n"
                "- Cytolyse hépatique, fibrose pulmonaire selon le traitement"
            )),
            FicheRow(concept="", detail_md=(
                "- L'hormonosensibilité ne dure qu'un temps → **résistance à la castration** (moyenne 18 mois)\n"
                "- Critères : testostéronémie aux taux de castration + 3 augmentations PSA à 2 semaines d'intervalle + PSA > 2 ng/mL\n"
                "- Médiane de survie : 1 an"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="E", titre="Stratégie thérapeutique et suivi", rows=[
            FicheRow(concept="Stade localisé — faible risque", detail_md=(
                "- Prostatectomie totale +/- curage OU\n"
                "- Radiothérapie externe conformationnelle OU\n"
                "- Curiethérapie iode 125 OU\n"
                "- **Surveillance active** (espérance de vie > 10 ans)\n"
                "- Abstention-surveillance si espérance de vie < 10 ans"
            )),
            FicheRow(concept="Stade localisé — risque intermédiaire", detail_md=(
                "- Prostatectomie totale +/- curage OU\n"
                "- Radiothérapie externe avec escalade de dose OU\n"
                "- RT sans escalade + suppression androgénique courte (**6 mois**) OU\n"
                "- Curiethérapie + RT externe"
            )),
            FicheRow(concept="Haut risque et localement avancé", detail_md=(
                "- RT externe + suppression androgénique prolongée **2-3 ans** OU\n"
                "- Prostatectomie totale **élargie** + curage ganglionnaire"
            )),
            FicheRow(concept="Stade métastatique", detail_md=(
                "- Traitement **palliatif**\n"
                "- 1ère intention : suppression androgénique + hormonothérapie 2ème génération\n"
                "  - +/- chimiothérapie si haut volume\n"
                "- RT pelvi-prostatique à discuter si N+M0\n"
                "- Métastases osseuses : **dénosumab/bisphosphonates**"
            )),
            FicheRow(concept="◆ Récidive", detail_md=(
                "- Après prostatectomie :\n"
                "  - Profil récidive locale → **RT de rattrapage** au plus tôt\n"
                "  - Profil récidive métastatique → suppression androgénique\n"
                "- Après RT/curiethérapie : chirurgie de rattrapage curative\n"
                "- Résistance à la castration métastatique :\n"
                "  - Asymptomatique : hormonothérapie 2ème ligne (abiratérone)\n"
                "  - Symptomatique : chimiothérapie (docétaxel)"
            )),
            FicheRow(concept="Dépistage et suivi", detail_md=(
                "- **Pas de dépistage systématique**\n"
                "- Dépistage individuel à partir de **50 ans** (45 ans si FDR) : TR + PSA\n"
                "- Suivi métastatique : créatinine, PAL, calcémie tous les 3-6 mois\n"
                "- Sous hormonothérapie : suivi du risque CV et osseux"
            )),
        ]),
    ])

    # ── PARTIE III : TROUBLES DE L'ÉRECTION ET URGENCES PÉNIENNES ──
    partie_iii = Partie(numero="III", titre="Troubles de l'érection et urgences péniennes", sous_parties=[
        SousPartie(lettre="A", titre="Dysfonction érectile", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Incapacité d'obtenir/maintenir une érection suffisante pour permettre une "
                "activité sexuelle satisfaisante pendant au moins **3 mois**\n"
                "- Concerne **1/3** des hommes après 40 ans\n"
                "- Prévalence augmente avec HTA, diabète, dyslipidémie, obésité"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "| Catégorie | Exemples |\n"
                "|-----------|----------|\n"
                "| **Psychogène** | Anxiété de performance, dépression, conflits conjugaux |\n"
                "| **Toxique** | OH, tabac, cannabis, héroïne, méthadone |\n"
                "| **Neurologique** | Lésions médullaires, SEP, Parkinson, Alzheimer |\n"
                "| **Endocrinologique** | Diabète, hypogonadisme, dysthyroïdie, Cushing |\n"
                "| **Vasculaire** | Athérosclérose, HTA, fuite veineuse |\n"
                "| **Iatrogène** | AntiHTA, antidépresseurs, anti-androgènes, RT pelvienne |\n"
                "| **Urologique** | Maladie de Lapeyronie, séquelles priapisme |\n"
            )),
            FicheRow(concept="◆ Organique vs psychogène", detail_md=(
                "| Critère | Organique | Psychogène |\n"
                "|---------|-----------|------------|\n"
                "| Début | **Progressif** | **Brutal** |\n"
                "| Érections nocturnes/matinales | Disparues | Conservées |\n"
                "| Libido | Conservée (sauf hypogonadisme) | Diminuée |\n"
                "| Éjaculation | Verge molle | Absente |\n"
                "| Facteur déclenchant | Absent | Présent |\n"
                "| Examen clinique | Anormal | Normal |\n"
            )),
            FicheRow(concept="Score IIEF", detail_md=(
                "- **Score 5-10** : DE sévère\n"
                "- **Score 11-15** : DE modérée\n"
                "- **Score 16-20** : DE légère\n"
                "- **Score 21-25** : DE normale"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- Glycémie à jeun (+HbA1c si diabétique)\n"
                "- EAL : cholestérol total, HDL, TG\n"
                "- **Testostéronémie** totale et biodisponible si > 50 ans avec signes de DALA\n"
                "- NFS, créatinine, ionogramme, BHC"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Mesures systématiques** : information, hygiène de vie, sevrage tabagique, perte de poids\n"
                "- **1ère ligne : IPDE5** (traitement de référence) :\n"
                "  - Sildénafil (Viagra) : 30 min avant, 6-10h\n"
                "  - Tadalafil (Cialis) : 1h avant + quotidien, 48h\n"
                "  - Vardénafil (Lévitra) : 30 min avant, 6-10h\n"
                "  - Efficacité : **65-85%**, non remboursés\n"
                "  - **CI : dérivés nitrés et donneurs de NO**\n"
                "- **2ème ligne : IIC de PGE1** si CI/échec IPDE5\n"
                "- **3ème ligne : implants péniens**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Vérifier l'aptitude physique au rapport (20 min marche/j, monter 2 étages)\n"
                "- ⚠ **CI absolue** des IPDE5 : prise de dérivés nitrés"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Maladie de Lapeyronie et fracture des corps caverneux", rows=[
            FicheRow(concept="Maladie de Lapeyronie", detail_md=(
                "- **Fibrose localisée** de l'albuginée formant une plaque\n"
                "- Concerne 3-9% des hommes\n"
                "- **Phase inflammatoire** : plaque de novo + douleurs\n"
                "- **Phase cicatricielle** : stabilisation\n"
                "- Courbure de la verge en érection, peut empêcher l'intromission\n"
                "- Diagnostic clinique : palpation des plaques\n"
                "- Traitement : AINS, vitamine E, colchicine (phase inflammatoire), chirurgie si gênant"
            )),
            FicheRow(concept="Fracture des corps caverneux", detail_md=(
                "- Traumatisme des corps caverneux en érection : **faux pas du coït**\n"
                "- **Douleur rapide**, perte de rigidité\n"
                "- Hématome abondant : aspect d'**aubergine**\n"
                "- Perception subjective d'un craquement\n"
                "- Pas d'examens complémentaires (+/- IRM si doute)\n"
                "- **Traitement chirurgical en urgence relative** (< 24h) :\n"
                "  - Évacuation hématome + suture corps caverneux\n"
                "- Cicatrisation après **6 semaines** sans rapports sexuels"
            )),
        ]),
        SousPartie(lettre="C", titre="Priapisme", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Érection prolongée > **4 heures** en dehors de toute stimulation sexuelle\n"
                "- Affection rare, concerne les corps caverneux"
            )),
            FicheRow(concept="Priapisme à bas débit", detail_md=(
                "- Stagnation de sang hypoxique dans les espaces sinusoïdes\n"
                "- **Douloureux+++**\n"
                "- Étiologies : injection intracaverneuse+++, drépanocytose, thalassémie, LMC\n"
                "- Gazométrie du sang caverneux\n"
                "- **PEC urgente** :\n"
                "  - < 6h : effort physique, réfrigération pénienne, alphastimulant PO\n"
                "  - > 6h : **ponction évacuatrice intracaverneuse**\n"
                "  - Récidive : injection intracaverneuse d'alphastimulant\n"
                "  - Échec : shunt caverno-spongieux\n"
                "- Si traitement > 6h : risque de **DE définitive**"
            )),
            FicheRow(concept="Priapisme à haut débit", detail_md=(
                "- Secondaire à **traumatisme périnéal** → fistule artério-caverneuse\n"
                "- **Non douloureux**, souvent partiel, pas d'ischémie\n"
                "- PEC : artériographie pelvienne + **embolisation**\n"
                "- Évolution favorable avec récupération de la fonction érectile"
            )),
            FicheRow(concept="", detail_md=(
                "- Le priapisme à bas débit est une **urgence** : risque de DE définitive si > 6h\n"
                "- Ne pas confondre bas débit (douloureux, urgence) et haut débit (non douloureux, bon pronostic)"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE IV : RÉTENTION AIGUË D'URINE ──
    partie_iv = Partie(numero="IV", titre="Rétention aiguë d'urine", sous_parties=[
        SousPartie(lettre="A", titre="Définition et tableau clinique", rows=[
            FicheRow(concept="★ Définition", detail_md=(
                "- **Impossibilité totale d'uriner** malgré la réplétion vésicale"
            )),
            FicheRow(concept="Interrogatoire", detail_md=(
                "- Événements déclenchants : boissons abondantes, long voyage assis, prise médicaments\n"
                "- Signes fonctionnels : état algique, anxiété, agitation, envie d'uriner permanente\n"
                "- ⚠ **Peut être indolore** si diabète ou traumatisé du rachis\n"
                "- Signes associés : dysurie, SFU, brûlures mictionnelles, hyperthermie, hématurie"
            )),
            FicheRow(concept="ATCD à rechercher", detail_md=(
                "- Urologiques : épisodes antérieurs, HBP, cancer prostate, sténose urétrale\n"
                "- Neurologiques : blessés médullaires, SEP, spina bifida, Parkinson, neuropathie diabétique\n"
                "- Traitements : médicaments induisant RAU, AAP, AVK, héparine"
            )),
            FicheRow(concept="Examen physique", detail_md=(
                "- **Globe vésical** : diagnostic positif\n"
                "  - Voussure à convexité supérieure en hypogastre\n"
                "  - **Matité** à la percussion sus-pubienne, souvent douloureuse\n"
                "- **TR systématique**\n"
                "- Examen OGE : recherche phimosis serré"
            )),
        ]),
        SousPartie(lettre="B", titre="Étiologies", rows=[
            FicheRow(concept="Étiologies", detail_md=(
                "| Catégorie | Exemples |\n"
                "|-----------|----------|\n"
                "| **Prostatiques** | HBP, prostatite, cancer de la prostate |\n"
                "| **Neurologiques centrales** | SEP, compression médullaire, Parkinson, AVC |\n"
                "| **Neurologiques périphériques** | Diabète |\n"
                "| **Médicamenteuses** | Anticholinergiques, neuroleptiques, ADT, morphiniques, sympathomimétiques |\n"
                "| **Urétrales** | Sténose post-traumatique/post-infectieuse |\n"
                "| **Autres** | Caillotage vésical, prolapsus génital, fécalome, phimosis serré |\n"
            )),
            FicheRow(concept="◆ Causes médicamenteuses (détail)", detail_md=(
                "- **Anticholinergiques** : collyre mydriatique, traitements instabilité vésicale\n"
                "- **Neuroleptiques** : phénothiazines\n"
                "- ADT imipraminiques\n"
                "- Antalgiques : **néfopam**, tiémonium\n"
                "- Bronchodilatateurs bétamimétiques\n"
                "- **Antihistaminiques**, morphiniques, inhibiteurs calciques"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours rechercher une cause **médicamenteuse** de RAU\n"
                "- ⚠ La RAU peut être **indolore** chez le patient diabétique"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Examens complémentaires et prise en charge", rows=[
            FicheRow(concept="Bilan pré-thérapeutique", detail_md=(
                "- **Aucun examen en urgence**\n"
                "- Bilan d'hémostase si drainage par cathéter sus-pubien\n"
                "- Échographie vésicale si doute clinique (obèse)"
            )),
            FicheRow(concept="Bilan post-thérapeutique", detail_md=(
                "- **Retentissement** : ionogramme, créatinine +/- échographie haut appareil\n"
                "- **Étiologique** : ECBU systématique, échographie vésico-prostatique\n"
                "  - Résidu post-mictionnel, retentissement vésical, lithiase, tumeur, volume prostatique\n"
                "- Discutés : débitmétrie, urétrocystoscopie si hématurie"
            )),
            FicheRow(concept="Prise en charge : urgence", detail_md=(
                "| | Sondage à demeure (SAD) | Cathétérisme sus-pubien |\n"
                "|--|------------------------|------------------------|\n"
                "| **CI** | Sténose urétrale, traumatisme urètre/bassin, RAU fébrile (prostatite) | Grossesse, troubles hémostase/anticoagulants, ATCD tumeur vessie, caillotage vésical, hématurie |\n"
                "| **Modalités** | Asepsie stricte, système clos, ECBU à la pose | Idem |\n"
                "| **Avantages** | Simple, épreuve de clampage possible | Pas de fausses routes urétrales, moins de complications au long cours |\n"
                "| **Inconvénients** | Sténose à distance | Calibre moins large |\n"
            )),
            FicheRow(concept="◆ Surveillance", detail_md=(
                "- Prévention hémorragie **a vacuo** : clampage tous les **500 cc**\n"
                "- Prévention syndrome de **levée d'obstacle** : surveillance diurèse, compensation volume à volume\n"
                "- Épreuve de clampage pendant 24h : si miction spontanée → retrait"
            )),
            FicheRow(concept="Complications", detail_md=(
                "- **IRA**\n"
                "- **Syndrome de levée d'obstacle**\n"
                "- **Hématurie a vacuo** (favorisée par anticoagulants)\n"
                "- **Vessie claquée** : distension détrusorienne → claquage musculaire → diverticules vésicaux"
            )),
            FicheRow(concept="", detail_md=(
                "- Le SAD est **contre-indiqué** en cas de prostatite (RAU fébrile) → cathéter sus-pubien\n"
                "- Le cathéter sus-pubien est CI si troubles de l'hémostase ou ATCD de tumeur vésicale"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE V : LITHIASE URINAIRE ──
    partie_v = Partie(numero="V", titre="Lithiase urinaire", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et composition des calculs", rows=[
            FicheRow(concept="Épidémiologie", detail_md=(
                "- Affection fréquente : 5% femme, **10% homme**\n"
                "- Risque de récidive à 5 ans : > **50%**\n"
                "- Représente 3% des causes d'IRT"
            )),
            FicheRow(concept="Facteurs favorisants", detail_md=(
                "- **Alimentaires** : produits laitiers, protéines animales, sel, aliments riches en oxalate "
                "(chocolat, fruits secs, épinards, thé), purines, sucres rapides\n"
                "- Diurèse insuffisante (apports liquidiens < 1L)\n"
                "- Facteurs familiaux (40%)\n"
                "- Infections urinaires\n"
                "- Anomalies anatomiques (stase urinaire)\n"
                "- **Médicaments** : indinavir, vitamine D, acétazolamide"
            )),
            FicheRow(concept="Composition des calculs", detail_md=(
                "| Type | Fréquence | Caractéristiques |\n"
                "|------|-----------|------------------|\n"
                "| **Oxalate de Ca monohydraté** (whewellite) | 50% | Brunâtre, lisse, résistant à la LEC |\n"
                "| **Oxalate de Ca dihydraté** (weddellite) | 25% | Jaunâtre, spiculé |\n"
                "| **Phosphate de calcium** | 15% | Crayeux, pH alcalin |\n"
                "| **Acide urique** | 6% | Jaune, lisse, **radiotransparent**, pH acide |\n"
                "| **Struvite** (PAM) | 2% | Coralliforme, pH alcalin, germes uréasiques |\n"
                "| **Cystine** | 1% | Coralliforme bilatéral, pH acide |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Les calculs d'**acide urique** sont **radiotransparents** (invisibles à l'ASP)\n"
                "- Les calculs de struvite sont liés aux **infections à germes uréasiques**\n"
                "- Le whewellite est **résistant à la LEC**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Colique néphrétique aiguë", rows=[
            FicheRow(concept="CNA simple", detail_md=(
                "- Facteurs déclenchants : voyage prolongé, pays chaud, immobilisation, déshydratation\n"
                "- **Début brutal**\n"
                "- Douleur **intense**, **sans position antalgique**, crises paroxystiques\n"
                "- Unilatérale, prédominance lombaire, irradiation vers OGE\n"
                "- Signes vésicaux : pollakiurie, hématurie micro/macroscopique\n"
                "- Signes digestifs : nausées, vomissements, iléus\n"
                "- BU : souvent négative, association infection fréquente"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Si les signes digestifs prédominent → diagnostic trompeur (DD : pathologies abdominales)\n"
                "- La douleur de CNA qui cède brutalement = signe de **rupture de fornix**"
            ), kind="piege"),
            FicheRow(concept="CNA compliquée (< 6%)", detail_md=(
                "- **CNA fébrile / PNA obstructive** : urgence médico-chirurgicale\n"
                "  - Fièvre > 38°C, frissons, marbrures, instabilité hémodynamique\n"
                "- **CNA anurique** : IRA, hyperkaliémie\n"
                "- **CNA hyperalgique** : résistante au traitement AINS IV + morphiniques\n"
                "- Critères morphologiques : calcul > **6 mm**, calculs multiples/bilatéraux"
            )),
            FicheRow(concept="◆ Diagnostics différentiels", detail_md=(
                "- CNA non lithiasique (20%) : syndrome de jonction, infarctus rénal\n"
                "- Pathologies digestives : colique hépatique, cholécystite, PA, appendicite, diverticulite\n"
                "- Pathologies gynécologiques : **GEU**, torsion kyste ovarien\n"
                "- Pathologies vasculaires : fissuration AAA"
            )),
        ]),
        SousPartie(lettre="C", titre="Examens complémentaires et traitement en urgence", rows=[
            FicheRow(concept="Bilan biologique", detail_md=(
                "- ECBU + culture + ATBG si BU positive\n"
                "- Hémocultures si fièvre > 38,5°C\n"
                "- **NFS-plaquettes, ionogramme, créatinine+++**"
            )),
            FicheRow(concept="Imagerie", detail_md=(
                "- **Échographie réno-vésicale** dans les 48h :\n"
                "  - Dilatation CPC, siège et taille du calcul, autres calculs\n"
                "- **Scanner abdomino-pelvien sans injection** :\n"
                "  - Mise en évidence calcul, mesure densité\n"
                "  - Permet affirmer le diagnostic si doute\n"
                "- ASP : image hyperéchogène + cône d'ombre postérieur"
            )),
            FicheRow(concept="CNA simple — traitement", detail_md=(
                "- **Traitement ambulatoire**\n"
                "- **AINS** (kétoprofène IV puis PO) : diminution DFG + diminution oedème local\n"
                "- **Morphiniques** (titration IV) si CI aux AINS ou résistance\n"
                "- +/- antispasmodiques\n"
                "- Apport hydrique : libre selon la soif\n"
                "- Au domicile : poursuite traitement 7j, surveillance T°, **tamisage des urines++**"
            )),
            FicheRow(concept="CNA compliquée — traitement", detail_md=(
                "- **Hospitalisation** en urologie\n"
                "- Rééquilibration hydroélectrolytique\n"
                "- **Drainage urines haut appareil** :\n"
                "  - **Sonde JJ** (urétérale interne) par voie endoscopique\n"
                "  - Échec : **néphrostomie percutanée** sous échographie\n"
                "- Prélèvement urines per-opératoire pour bactériologie\n"
                "- Si PNA obstructive : ATB IV dès prélèvements effectués"
            )),
        ]),
        SousPartie(lettre="D", titre="Prise en charge à long terme et traitement chirurgical", rows=[
            FicheRow(concept="Mesures diététiques", detail_md=(
                "- Objectif diurèse > **2 000 mL** (densité urinaire < 1015)\n"
                "- Boissons réparties tout au long de la journée\n"
                "- Calcium 800 mg-1 g/j, sel < 9 g/j, protéines animales < 1,2 g/kg/j\n"
                "- Limiter oxalates et boissons sucrées\n"
                "- Calculs uriques : **alcalinisation urines** (eau de Vichy, pH 6,5-7)\n"
                "- Calculs PAM : suppression boissons alcalines, acidification\n"
                "- Calculs cystine : alcalinisation (pH > 7,5), diurèse > 3 L/j"
            )),
            FicheRow(concept="Traitement chirurgical — indications", detail_md=(
                "- Taille > **6 mm**\n"
                "- Douleurs résistantes au traitement médical\n"
                "- Rein obstrué unique, obstruction bilatérale\n"
                "- Infection urinaire, risque pyonéphrose/sepsis"
            )),
            FicheRow(concept="Techniques chirurgicales", detail_md=(
                "| Technique | Indication | Particularités |\n"
                "|-----------|-----------|----------------|\n"
                "| **LEC** | Calculs rein < 20 mm, urétéraux, radio-opaques, densité < 1000 UH | Ambulatoire, non invasif, CI grossesse, SF 30-76% |\n"
                "| **Urétéroscopie** | Résistance LEC, densité > 1000 UH, calculs uretère pelvien | Sous AG, voie rétrograde |\n"
                "| **NLPC** | Calculs > 2 cm, coralliformes/complexes | Voie percutanée, SF 80-85% |\n"
                "| **Chémolyse orale** | Calculs d'acide urique uniquement | Alcalinisation PO |\n"
            )),
            FicheRow(concept="Complications LEC", detail_md=(
                "- CNA post-LEC par migration de fragments (20%)\n"
                "- Hématurie, infections urinaires\n"
                "- CI : grossesse, infection non traitée, obstacle en aval, anévrisme artère rénale/aorte, "
                "troubles coagulation"
            )),
            FicheRow(concept="Surveillance", detail_md=(
                "- Rythme : 1/6 mois pendant 1 an puis 1/an\n"
                "- Bilan urinaire, spectrophotométrie infrarouge des calculs expulsés\n"
                "- Bilan métabolique à plus d'1 mois de tout épisode aigu"
            )),
        ]),
    ])

    # ── PARTIE VI : INFECTIONS URINAIRES ──
    partie_vi = Partie(numero="VI", titre="Infections urinaires", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et microbiologie", rows=[
            FicheRow(concept="Définitions", detail_md=(
                "- **IU simple** : sans FDR de complications\n"
                "- **IU à risque de complications** : anomalie organique/fonctionnelle arbre urinaire, "
                "sexe masculin, grossesse, sujet > 65 ans fragile, immunodépression, IRC < 30 mL/min\n"
                "- **IU grave** : PNA/IU masculine + sepsis grave/choc septique/indication de drainage\n"
                "- **Cystite récidivante** : ≥ **4 épisodes** sur 12 mois\n"
                "- **Colonisation urinaire** : MO dans les urines sans manifestations cliniques"
            )),
            FicheRow(concept="Microbiologie", detail_md=(
                "| Germe | Épidémiologie | Particularités |\n"
                "|-------|--------------|----------------|\n"
                "| **E. coli** | 75-90% en ville, 50% hospitalier | 40% R amoxicilline, 10% R FLQ |\n"
                "| **Proteus mirabilis** | 10% en ville | Germe uréase+, favorise lithiases |\n"
                "| **Entérocoques** | | Résistance naturelle aux C3G |\n"
                "| **Klebsiella, Pseudomonas** | Hospitalier | Germes souvent résistants, SAD |\n"
                "| **Candida** | Hospitalier | SAD, diabétiques, post-ATB large spectre |\n"
            )),
            FicheRow(concept="Voies de dissémination", detail_md=(
                "- **Voie ascendante** (97%) : favorisée par stase, corps étranger, glucose urinaire\n"
                "- Voie hématogène (rare)\n"
                "- 2ème site d'infection bactérienne après arbre respiratoire\n"
                "- 50% des femmes auront au moins 1 IU dans leur vie"
            )),
        ]),
        SousPartie(lettre="B", titre="Cystite aiguë", rows=[
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Brûlures mictionnelles, gêne/douleurs sus-pubiennes\n"
                "- Pollakiurie, impériosités\n"
                "- Urines troubles, malodorantes +/- hématurie\n"
                "- **PAS de fièvre** ni de douleurs lombaires\n"
                "- BU systématique : leucocytes +/- nitrites"
            )),
            FicheRow(concept="Cystite simple", detail_md=(
                "- **Aucun examen complémentaire**\n"
                "- ATB de 1ère intention :\n"
                "  - **Fosfomycine-trométamol** (dose unique) OU\n"
                "  - **Pivmécillinam** 5 jours\n"
                "- Mesures associées (RHD) : cure de diurèse, lutte contre constipation, "
                "uriner après rapport sexuel"
            )),
            FicheRow(concept="Cystite à risque de complications", detail_md=(
                "- BU + **ECBU systématiques**\n"
                "- Différer ATB si possible pour adaptation à l'ATBG\n"
                "- Traitement pouvant être différé : amoxicilline > pivmécillinam > nitrofurantoïne > "
                "fosfomycine-trométamol > triméthoprime\n"
                "- Si ne peut être différé : nitrofurantoïne en 1ère intention"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La cystite simple ne nécessite **aucun examen complémentaire** (pas d'ECBU)\n"
                "- L'absence de nitrites n'exclut pas l'infection (cocci gram+, Pseudomonas)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Pyélonéphrite aiguë", rows=[
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Début brutal\n"
                "- **Fièvre > 38,5°C** avec frissons\n"
                "- Douleurs lombaires unilatérales, irradiation type CNA\n"
                "- Douleurs à l'**ébranlement de la fosse lombaire**\n"
                "- Signes inconstants de cystite"
            )),
            FicheRow(concept="PNA simple", detail_md=(
                "- BU + **ECBU avec ATBG** :\n"
                "  - Leucocyturie > 10⁴/mL + bactériurie > 10³ UFC/mL (E. coli)\n"
                "- Échographie rénale dans les 24h si hyperalgique\n"
                "- ATB à débuter **immédiatement après ECBU**\n"
                "- Hospitalisation si : PNA hyperalgique, vomissements, doute diagnostic"
            )),
            FicheRow(concept="PNA grave", detail_md=(
                "- ECBU + hémocultures systématiques + NFS, CRP, créatinine\n"
                "- **Uroscanner en urgence** (max 24h)\n"
                "- **Hospitalisation systématique**\n"
                "- Sans choc ni FDR résistance C3G : **C3G IV + amikacine**\n"
                "- Si FDR résistance : pipéracilline-tazobactam ou **carbapénème** + amikacine\n"
                "- Choc septique + FDR résistance : **carbapénème + amikacine**\n"
                "- Drainage en urgence si obstacle\n"
                "- Durée totale : **10-14 jours**"
            )),
            FicheRow(concept="Complications PNA", detail_md=(
                "- Choc septique\n"
                "- **Abcès rénal** : prolongation ATB/ponction-drainage sous TDM\n"
                "- Insuffisance rénale si PNA à répétition\n"
                "- Suppuration périnéphritique"
            )),
        ]),
        SousPartie(lettre="D", titre="Prostatite", rows=[
            FicheRow(concept="Prostatite aiguë", detail_md=(
                "- Infection bactérienne du parenchyme prostatique\n"
                "- FDR : HBP, résidu post-mictionnel, diabète, immunodépression\n"
                "- Signes de cystite + syndrome fébrile > 38°C\n"
                "- Douleurs pelviennes (périnéales, urétrales, péniennes)\n"
                "- **TR** : prostate **douloureuse**, augmentée de volume, tendue\n"
                "- BU : leucocytes et/ou nitrites"
            )),
            FicheRow(concept="Examens et traitement", detail_md=(
                "- **ECBU systématique** (seuil 10³ UFC/mL)\n"
                "- Hémocultures si fièvre, **PSA inutile**\n"
                "- Échographie sus-pubienne si douleurs lombaires/suspicion RAU\n"
                "  - **PAS d'échographie endorectale**\n"
                "- Si évolution défavorable à 72h : **IRM prostatique** (recherche abcès)\n"
                "- ATB : FLQ PO (ciprofloxacine/lévofloxacine) > cotrimoxazole > C3G IV\n"
                "- RAU : drainage par **cathéter sus-pubien** (pas de SAD)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Le **sondage vésical est contre-indiqué** en cas de prostatite → cathéter sus-pubien\n"
                "- ⚠ Le dosage de PSA est **inutile** en phase aiguë (toujours élevé)\n"
                "- ⚠ Pas d'échographie **endorectale** en phase aiguë"
            ), kind="piege"),
            FicheRow(concept="Prostatite chronique", detail_md=(
                "- Suite à absence/insuffisance de traitement de la prostatite aiguë\n"
                "- Évolution par poussées aiguës\n"
                "- Signes : dysurie, pollakiurie, douleurs pelviennes, douleurs éjaculation, hémospermie\n"
                "- TR : normal ou prostate irrégulière\n"
                "- **ATB prolongée 12 semaines** : FLQ, cotrimoxazole, cyclines\n"
                "- Contrôle ECBU 1 mois après arrêt traitement"
            )),
            FicheRow(concept="Cystite de l'homme", detail_md=(
                "- ECBU d'emblée (pas de BU systématique)\n"
                "- N'est plus traitée d'office comme une prostatite\n"
                "- Traitement de référence : **fosfomycine-trométamol** J1, J3, J5\n"
                "- Alternative : pivmécillinam 7 jours\n"
                "- Réévaluation impérative si persistance des symptômes"
            )),
        ]),
    ])

    # ── PARTIE VII : INFECTIONS GÉNITALES ET HBP ──
    partie_vii = Partie(numero="VII", titre="Infections génitales et HBP", sous_parties=[
        SousPartie(lettre="A", titre="Urétrite aiguë et orchi-épididymite", rows=[
            FicheRow(concept="Urétrite aiguë", detail_md=(
                "- Inflammation de l'urètre et des glandes péri-urétrales — **IST**\n"
                "- Germes : **C. trachomatis**, **N. gonorrhoeae**\n"
                "- Chlamydia : incubation 3-10j, écoulement clair, peu douloureux\n"
                "- Gonocoque : incubation 2-5j, écoulement **purulent jaunâtre**, brûlures intenses\n"
                "- **Portage asymptomatique possible**"
            )),
            FicheRow(concept="Traitement urétrite", detail_md=(
                "- Toujours traiter gonocoque **ET** chlamydia :\n"
                "  - **Ceftriaxone** 500 mg IM/IV (gonocoque)\n"
                "  - **Doxycycline** 200 mg/j pendant 7j (chlamydia)\n"
                "- Mesures associées :\n"
                "  - Abstinence/préservatifs jusqu'à guérison\n"
                "  - Dépistage et traitement des partenaires\n"
                "  - Dépistage systématique des autres IST\n"
                "- Contrôle à **J7**"
            )),
            FicheRow(concept="Orchi-épididymite", detail_md=(
                "- Inflammation testicule et épididyme\n"
                "- Homme jeune : **IST** (Chlamydia, gonocoque)\n"
                "- Homme âgé : voie urinaire rétrograde (entérobactéries)\n"
                "- Fièvre, douleurs scrotales, grosse bourse aiguë\n"
                "- **Signe de Chevassu** négatif (disparition sillon épididymo-testiculaire)\n"
                "- **Signe de Prehn** positif\n"
                "- TR systématique : recherche prostatite"
            )),
            FicheRow(concept="◆ DD grosse bourse aiguë", detail_md=(
                "- **Torsion du cordon spermatique** (urgence chirurgicale)\n"
                "- Torsion annexe testiculaire\n"
                "- Cancer du testicule\n"
                "- Hernie inguinale engouée/étranglée\n"
                "- Traumatisme scrotal"
            )),
            FicheRow(concept="Complications urétrite/orchi-épididymite", detail_md=(
                "- Urétrite : prostatite, orchi-épididymite, sténose urètre, "
                "syndrome de Fiessinger-Leroy-Reiter (arthrite réactionnelle à Chlamydia)\n"
                "- Orchi-épididymite : fonte purulente du testicule, abcès, "
                "**azoospermie** si récidive/atteinte bilatérale"
            )),
        ]),
        SousPartie(lettre="B", titre="Hypertrophie bénigne de la prostate", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- **Hyperplasie** de la zone de transition de la prostate\n"
                "- Affection bénigne, très fréquente : **75% après 70 ans**\n"
                "- FDR : âge, statut hormonal\n"
                "- Facteurs de progression : âge, taux PSA, volume prostate"
            )),
            FicheRow(concept="SBAU", detail_md=(
                "- **Signes obstructifs** : retard au démarrage, dysurie, jet faible, gouttes retardataires\n"
                "- **Signes irritatifs** : pollakiurie, urgenturie, impériosités, brûlures mictionnelles\n"
                "- Score **IPSS** :\n"
                "  - 0-7 : léger\n"
                "  - 8-19 : modéré\n"
                "  - 20-35 : sévère"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ **Pas de parallélisme anatomo-clinique** entre la sévérité des SBAU et le volume de l'HBP\n"
                "- Une grosse prostate peut être peu symptomatique et inversement"
            ), kind="piege"),
            FicheRow(concept="TR", detail_md=(
                "- Augmentation de volume (> **20 g**)\n"
                "- **Souple, indolore, lisse, régulière**\n"
                "- Disparition du sillon médian\n"
                "- Permet de dépister un éventuel cancer de la prostate"
            )),
            FicheRow(concept="◆ Complications", detail_md=(
                "- **Aiguës** : RAU, prostatite, orchi-épididymite, hématurie macro initiale, IRA obstructive\n"
                "- **Chroniques** : rétention vésicale chronique, lithiase vésicale de stase, IRC obstructive\n"
                "- Rechercher : globe vésical, mictions par regorgement, hernie inguinale"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- **ECBU** : éliminer infection\n"
                "- **PSA** : dépister cancer associé (> 4 ng/mL → biopsies)\n"
                "- Créatinine : dépister IRC\n"
                "- **Débitmétrie** : dysurie si Qmax < **10 mL/s** (minimum 150 mL pour interprétation)\n"
                "- Échographie réno-vésico-prostatique : retentissement haut et bas appareil, volume prostatique"
            )),
        ]),
        SousPartie(lettre="C", titre="Traitement médical et chirurgical de l'HBP", rows=[
            FicheRow(concept="Abstention/surveillance", detail_md=(
                "- HBP non compliquée + SBAU minimes sans altération qualité de vie\n"
                "- Éducation, RHD : réduction hydrique après 18h, diminution caféine/OH, "
                "arrêt médicaments favorisant dysurie"
            )),
            FicheRow(concept="Traitement médical", detail_md=(
                "| Classe | Action | EI | Exemples |\n"
                "|--------|--------|----|---------|\n"
                "| **Alpha-bloquants** | Diminution tonus urètre (48h) | HypoTA orthostatique, céphalées, éjaculation rétrograde | Alfuzosine, tamsulosine |\n"
                "| **Inhibiteurs 5-alpha-réductase** | Diminution volume prostate (6 mois) | **Diminution PSA 50%**, troubles érection, gynécomastie | Finastéride, dutastéride |\n"
                "| **IPDE5** | Mal connu | Aucun significatif | Tadalafil 5 mg |\n"
                "| **Phytothérapie** | Mal connu | Aucun | Serenoa repens |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Les inhibiteurs de la 5-alpha-réductase **diminuent le PSA de 50%** → "
                "multiplier par 2 le PSA mesuré pour obtenir la valeur réelle\n"
                "- Alpha-bloquants en 1ère intention le plus souvent"
            ), kind="piege"),
            FicheRow(concept="Traitement chirurgical", detail_md=(
                "| Technique | Indication | Complications |\n"
                "|-----------|-----------|---------------|\n"
                "| **ICP** | Prostate < 30 g | Hématurie, RAU, éjaculation rétrograde |\n"
                "| **RTUP** | Prostate < 80 g | Hématurie, RAU, **TURP syndrome**, sténose |\n"
                "| **AVH** | Prostate > 80 g | Hématurie, RAU, hématome, sténose |\n"
                "| **Énucléation laser** | Toute taille | Moins de saignements, hospitalisation courte |\n"
            )),
            FicheRow(concept="◆ TURP syndrome", detail_md=(
                "- Réabsorption du liquide d'irrigation (glycocolle)\n"
                "- Myodésopsies, céphalée, hypotension, bradycardie\n"
                "- **Hyponatrémie de dilution** + surcharge volémique\n"
                "- FDR : saignement important + durée opératoire > 60 min\n"
                "- Traitement :\n"
                "  - Na > 120 : restriction hydrique + diurétique\n"
                "  - Na < 120 : **sérum hypertonique** en perfusion lente"
            )),
            FicheRow(concept="", detail_md=(
                "- Un **cancer de la prostate** peut toujours se développer à partir de la "
                "zone périphérique laissée en place après chirurgie de l'HBP\n"
                "- L'adénome est systématiquement envoyé en anatomopathologie"
            ), kind="a_retenir"),
            FicheRow(concept="Surveillance", detail_md=(
                "- Consultation urologie **1/an** : TR, questionnaire IPSS\n"
                "- Dépistage complications 1/an : PSA, créatinine, ECBU"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Sondage vésical vs cathéter sus-pubien", markdown=(
            "| Critère | Sondage à demeure | Cathéter sus-pubien |\n"
            "|---------|-------------------|--------------------|\n"
            "| CI | Sténose urétrale, traumatisme urètre, prostatite | Grossesse, troubles hémostase, ATCD tumeur vessie, hématurie |\n"
            "| Avantages | Simple, épreuve de clampage | Pas de fausses routes, moins de complications |\n"
            "| Inconvénients | Sténose à distance | Calibre moins large |\n"
        )),
        TableauSynthese(titre="Classification d'Amico — Cancer de la prostate", markdown=(
            "| Risque | PSA | Gleason | Stade |\n"
            "|--------|-----|---------|-------|\n"
            "| Faible | < 10 ng/mL | ≤ 6 | T1c-T2a |\n"
            "| Intermédiaire | 10-20 ng/mL | 7 | T2b |\n"
            "| Élevé | > 20 ng/mL | ≥ 8 | ≥ T2c |\n"
        )),
        TableauSynthese(titre="Composition des calculs urinaires", markdown=(
            "| Type | Fréquence | Radio | pH | Terrain |\n"
            "|------|-----------|-------|----|---------|\n"
            "| Oxalate Ca monohydraté | 50% | Opaque | Variable | Résistant LEC |\n"
            "| Oxalate Ca dihydraté | 25% | Opaque | Variable | — |\n"
            "| Phosphate Ca | 15% | Très opaque | Alcalin | — |\n"
            "| Acide urique | 6% | Transparent | Acide | Goutte, syndrome métabolique |\n"
            "| Struvite | 2% | Faiblement opaque | Alcalin | Infections uréasiques |\n"
            "| Cystine | 1% | Faiblement opaque | Acide | Cystinurie |\n"
        )),
        TableauSynthese(titre="Traitement chirurgical des calculs urinaires", markdown=(
            "| Technique | Indication | SF |\n"
            "|-----------|-----------|----|\n"
            "| LEC | Rein < 20 mm, densité < 1000 UH | 30-76% |\n"
            "| Urétéroscopie | Résistance LEC, densité > 1000 UH | Variable |\n"
            "| NLPC | > 2 cm, coralliformes | 80-85% |\n"
            "| Chémolyse orale | Acide urique uniquement | Variable |\n"
        )),
        TableauSynthese(titre="Traitements médicaux de l'HBP", markdown=(
            "| Classe | Délai action | EI principaux |\n"
            "|--------|-------------|---------------|\n"
            "| Alpha-bloquants | 48h | HypoTA orthostatique, éjaculation rétrograde |\n"
            "| Inhibiteurs 5AR | 6 mois | Diminution PSA 50%, troubles sexuels |\n"
            "| IPDE5 | Variable | Aucun significatif |\n"
            "| Phytothérapie | Variable | Aucun |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Hématurie | > **10 hématies/mm³** | Définition |\n"
        "| PSA normal | < **4 ng/mL** | Dépistage cancer prostate |\n"
        "| Biopsies prostate | **12** prélèvements minimum | 6 par lobe |\n"
        "| Gleason bon pronostic | **6** | Bien différencié |\n"
        "| Gleason mauvais pronostic | **8-10** | Peu différencié |\n"
        "| Dysfonction érectile | > **3 mois** | Définition |\n"
        "| IPDE5 efficacité | **65-85%** | Traitement de référence DE |\n"
        "| Priapisme urgence | > **4 heures** | Risque DE définitive si > 6h |\n"
        "| Récidive lithiase 5 ans | > **50%** | Justifie enquête étiologique |\n"
        "| Calcul chirurgical | > **6 mm** | Indication traitement |\n"
        "| Diurèse cible lithiase | > **2000 mL** | Objectif prévention |\n"
        "| Cystite récidivante | ≥ **4 épisodes/12 mois** | Définition |\n"
        "| PNA grave durée ATB | **10-14 jours** | Durée totale |\n"
        "| Prostatite chronique ATB | **12 semaines** | Durée prolongée |\n"
        "| HBP fréquence | **75%** après 70 ans | Très fréquent |\n"
        "| Débitmétrie dysurie | Qmax < **10 mL/s** | Obstruction |\n"
    ))

    points_cles = [
        "L'hématurie sans caillots oriente vers une atteinte glomérulaire, avec caillots vers une origine urologique",
        "Le cancer de la prostate est le cancer le plus fréquent chez l'homme > 50 ans, dépistage individuel par TR + PSA à partir de 50 ans",
        "Le score de Gleason est le facteur pronostic essentiel du cancer de la prostate (6 = bon, 8-10 = mauvais)",
        "La CI absolue des IPDE5 est la prise de dérivés nitrés ; les IPDE5 sont le traitement de 1re ligne de la DE",
        "Le priapisme à bas débit est une urgence : risque de DE définitive si traitement > 6 heures",
        "La RAU fébrile (prostatite) contre-indique le sondage vésical → cathéter sus-pubien",
        "La CNA fébrile/PNA obstructive est une urgence médico-chirurgicale nécessitant un drainage",
        "La PNA grave nécessite C3G IV + amikacine en 1re intention, carbapénème si FDR de résistance",
        "L'HBP n'a pas de parallélisme anatomo-clinique : le volume ne corrèle pas avec les symptômes",
        "Les inhibiteurs de la 5-alpha-réductase diminuent le PSA de 50% : multiplier par 2 la valeur mesurée",
    ]

    fiche_eclair_md = (
        "**Hématurie** : > 10/mm³. Sans caillots = glomérulaire, avec caillots = urologique. "
        "ECBU + cytologie + uroscanner. CI cathéter sus-pubien si hématurie macro.\n\n"
        "**Cancer prostate** : 1er cancer H > 50 ans, 90% ADK zone périphérique. "
        "PSA < 4 ng/mL (non spécifique). Biopsies 12 prélèvements. Gleason 6/7/8-10. "
        "Amico : faible/intermédiaire/élevé. Dépistage individuel 50 ans (45 si FDR).\n\n"
        "**DE** : > 3 mois. IPDE5 en 1re ligne (CI dérivés nitrés). IIC PGE1 en 2e. "
        "Implants en 3e. Organique = progressif, psychogène = brutal.\n\n"
        "**Priapisme bas débit** : douloureux, urgence. Ponction si > 6h. "
        "Haut débit : traumatisme périnéal, non douloureux, embolisation.\n\n"
        "**RAU** : globe vésical. SAD sauf si prostatite (cathéter sus-pubien). "
        "Clampage /500 cc. Surveillance levée d'obstacle.\n\n"
        "**Lithiase** : 10% H, récidive > 50%. CNA simple = AINS + morphiniques. "
        "CNA compliquée = drainage JJ/néphrostomie. LEC < 20 mm, NLPC > 2 cm.\n\n"
        "**Cystite simple** : pas d'ECBU, fosfomycine dose unique. "
        "PNA grave : C3G + amikacine, uroscanner 24h, 10-14j.\n\n"
        "**Prostatite** : TR douloureux, PSA inutile, pas d'écho endorectale, "
        "SAD CI → cathéter sus-pubien. Chronique = ATB 12 sem.\n\n"
        "**HBP** : 75% > 70 ans. IPSS. Alpha-bloquants 1re ligne. "
        "I5AR diminuent PSA de 50%. RTUP < 80g, AVH > 80g. TURP syndrome."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Urologie",
        annee="2025-2026",
        item="Items 257, 307, 122, 342, 262, 157, 158, 123",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi, partie_vii],
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="",
        usage=UsageStats(),
    )


def main():
    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(exist_ok=True)

    fiche = build_fiche()

    docx_path = output_dir / "Medecine_generale_Urologie_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Medecine_generale_Urologie_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path}")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

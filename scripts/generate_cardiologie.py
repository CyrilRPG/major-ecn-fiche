"""Génère la fiche exhaustive de Cardiologie à partir du PDF source."""

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
        PlanPartie(numero="I", titre="Facteurs de risque cardio-vasculaire et prévention", sous_parties=[
            PlanSousPartie(lettre="A", titre="FdRCV et marqueurs de risque"),
            PlanSousPartie(lettre="B", titre="Évaluation du risque CV global"),
            PlanSousPartie(lettre="C", titre="Prise en charge des FdRCV"),
        ]),
        PlanPartie(numero="II", titre="Hypertension artérielle", sous_parties=[
            PlanSousPartie(lettre="A", titre="Diagnostic et bilan initial"),
            PlanSousPartie(lettre="B", titre="Classification et HTA secondaire"),
            PlanSousPartie(lettre="C", titre="Traitement et complications"),
        ]),
        PlanPartie(numero="III", titre="Dyslipidémie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Diagnostic et classification"),
            PlanSousPartie(lettre="B", titre="Prise en charge thérapeutique"),
        ]),
        PlanPartie(numero="IV", titre="Maladie coronaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Angor d'effort"),
            PlanSousPartie(lettre="B", titre="SCA avec sus-décalage du ST (SCA ST+)"),
            PlanSousPartie(lettre="C", titre="SCA sans sus-décalage du ST (SCA non ST+)"),
            PlanSousPartie(lettre="D", titre="Arrêt cardio-respiratoire"),
        ]),
        PlanPartie(numero="V", titre="Insuffisance cardiaque", sous_parties=[
            PlanSousPartie(lettre="A", titre="Diagnostic et classification"),
            PlanSousPartie(lettre="B", titre="Étiologies"),
            PlanSousPartie(lettre="C", titre="Traitement de fond de l'IC à FE altérée"),
            PlanSousPartie(lettre="D", titre="OAP et complications"),
        ]),
        PlanPartie(numero="VI", titre="Fibrillation atriale", sous_parties=[
            PlanSousPartie(lettre="A", titre="Diagnostic et classification"),
            PlanSousPartie(lettre="B", titre="Prise en charge thérapeutique"),
            PlanSousPartie(lettre="C", titre="Complications et scores"),
        ]),
        PlanPartie(numero="VII", titre="Valvulopathies et prothèses", sous_parties=[
            PlanSousPartie(lettre="A", titre="Insuffisance mitrale"),
            PlanSousPartie(lettre="B", titre="Rétrécissement aortique"),
            PlanSousPartie(lettre="C", titre="Endocardite infectieuse"),
            PlanSousPartie(lettre="D", titre="Prothèses valvulaires cardiaques"),
        ]),
        PlanPartie(numero="VIII", titre="Maladie thromboembolique et AOMI", sous_parties=[
            PlanSousPartie(lettre="A", titre="Embolie pulmonaire et TVP"),
            PlanSousPartie(lettre="B", titre="AOMI et ischémie aiguë de membre"),
        ]),
    ]

    # ── PARTIE I : FACTEURS DE RISQUE CARDIO-VASCULAIRE ──
    partie_i = Partie(numero="I", titre="Facteurs de risque cardio-vasculaire et prévention", sous_parties=[
        SousPartie(lettre="A", titre="FdRCV et marqueurs de risque", rows=[
            FicheRow(concept="Définitions", detail_md=(
                "- **FdRCV** : état clinique ou biologique augmentant le risque de survenue d'un "
                "événement CV avec **relation de causalité** facteur/maladie\n"
                "- **Marqueur de risque CV** : pas de responsabilité causale démontrée, "
                "simple témoin de la maladie"
            )),
            FicheRow(concept="FdRCV non modifiables", detail_md=(
                "- **Âge** : hommes >= 50 ans, femmes >= 60 ans\n"
                "- **Sexe masculin**\n"
                "- **ATCD familiaux** d'accidents CV précoces :\n"
                "  - IDM/AVC/mort subite avant **55 ans** chez apparenté 1er degré masculin\n"
                "  - IDM/AVC/mort subite avant **65 ans** chez apparenté 1er degré féminin"
            )),
            FicheRow(concept="FdRCV modifiables", detail_md=(
                "- **Tabac** : reste un FdRCV si sevré depuis < 3 ans\n"
                "- **HTA** : TA > 140/90 mmHg traitée ou non\n"
                "- **Dyslipidémie** : LDL-c > 1,6 g/L, HDL-c < 0,4 g/L\n"
                "- **Diabète** de type 1 ou 2\n"
                "- **Obésité** : IMC > 30 kg/m2"
            )),
            FicheRow(concept="Marqueurs de risque", detail_md=(
                "- **Syndrome métabolique** : obésité centrale (PA > 94 cm homme, > 80 cm femme) "
                "avec au moins 2 parmi :\n"
                "  - TG > 1,5 g/L\n"
                "  - HDL-c < 0,4 g/L (H) ou < 0,5 g/L (F)\n"
                "  - TA > 130/85 mmHg\n"
                "  - Glycémie > 1,1 g/L\n"
                "- Insuffisance rénale, sédentarité, alcool, stress, conditions socio-économiques défavorables"
            )),
            FicheRow(concept="Facteurs protecteurs", detail_md=(
                "- Consommation de fruits et légumes\n"
                "- Activité physique régulière (au moins **30 min/jour**)\n"
                "- Consommation d'alcool modérée\n"
                "- HDL-c > **0,60 g/L**"
            )),
        ]),
        SousPartie(lettre="B", titre="Évaluation du risque CV global", rows=[
            FicheRow(concept="Risque CV global", detail_md=(
                "- Probabilité de survenue d'un événement CV majeur dans les **10 prochaines années** "
                "en fonction de l'ensemble des FdRCV\n"
                "- **SCORE 2** +++ : pour les patients de 40 à 79 ans\n"
                "- **SCORE 2-OP** : pour les patients > 80 ans"
            )),
            FicheRow(concept="Stratégie selon le RCV", detail_md=(
                "| RCV global | Conduite à tenir |\n"
                "|------------|------------------|\n"
                "| Faible | Pas d'examen complémentaire |\n"
                "| Modéré | Discuter coroscanner ou test d'ischémie |\n"
                "| Élevé | Test d'ischémie ou coroscanner |\n"
            )),
        ]),
        SousPartie(lettre="C", titre="Prise en charge des FdRCV", rows=[
            FicheRow(concept="Règles hygiéno-diététiques", detail_md=(
                "- **Sevrage tabagique** : soutien psychologique, patchs et gommes nicotiniques\n"
                "- **Traitement antihypertenseur** : objectif TA < 130 mmHg si < 65 ans, "
                "entre 130-139 mmHg si > 65 ans\n"
                "- Alimentation équilibrée, exercice physique >= 30 min/jour\n"
                "- Éducation thérapeutique"
            )),
            FicheRow(concept="", detail_md=(
                "- La PEC des FdRCV est un **traitement à vie** et doit être réévaluée régulièrement\n"
                "- Le sevrage tabagique est la mesure la plus **rentable** en terme de réduction du RCV"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE II : HYPERTENSION ARTÉRIELLE ──
    partie_ii = Partie(numero="II", titre="Hypertension artérielle", sous_parties=[
        SousPartie(lettre="A", titre="Diagnostic et bilan initial", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **HTA** : PA >= **140/90 mmHg**\n"
                "- Mesure en consultation après **5 min de repos**\n"
                "- HTA confirmée si chiffres élevés lors de **2 mesures** sur **3 consultations** "
                "sur une période de **3 à 6 mois**\n"
                "- > 50% des plus de 80 ans\n"
                "- Majoration du risque CV : AVC, SCA, AOMI"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- Souvent **asymptomatique**\n"
                "- Céphalée occipitale battante, phosphènes\n"
                "- Fatigabilité, nervosité, insomnie, épistaxis"
            )),
            FicheRow(concept="Confirmation diagnostique", detail_md=(
                "- **MAPA** sur 24h : HTA si TA > 135/85 (diurne), > 120/70 (nocturne), "
                "> 130/80 (sur 24h)\n"
                "- **ATM** (automesure tensionnelle) : HTA si TA > **135/85 mmHg** "
                "(3 mesures matin et soir, 5 min de repos, 3 jours)\n"
                "- Élimine l'**effet blouse blanche**"
            )),
            FicheRow(concept="Bilan OMS de 1re intention", detail_md=(
                "- Glycémie à jeun, exploration des anomalies lipidiques\n"
                "- **Kaliémie**\n"
                "- Créatininémie, DFG\n"
                "- Bandelette urinaire (protéinurie)\n"
                "- **ECG de repos**\n"
                "- Hb, Ht, acide urique"
            )),
            FicheRow(concept="Examens selon contexte", detail_md=(
                "- ETT (recherche HVG)\n"
                "- Écho-Doppler des TSA\n"
                "- **Index de pression systolique** (IPS)\n"
                "- Fond d'oeil"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours confirmer l'HTA par une **mesure ambulatoire** (MAPA ou ATM) "
                "avant de débuter un traitement\n"
                "- ⚠ La kaliémie est indispensable au bilan initial (dépistage hyperaldostéronisme)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Classification et HTA secondaire", rows=[
            FicheRow(concept="Classification", detail_md=(
                "| Grade | PAS (mmHg) | PAD (mmHg) |\n"
                "|-------|------------|------------|\n"
                "| HTA grade 1 | 140-159 | 90-99 |\n"
                "| HTA grade 2 | 160-179 | 100-109 |\n"
                "| HTA grade 3 | >= 180 | >= 110 |\n"
                "| HTA systolique isolée | >= 140 | < 90 |\n"
            )),
            FicheRow(concept="★ HTA résistante", detail_md=(
                "- HTA non contrôlée sur mesure ambulatoire malgré :\n"
                "  - Règles hygiéno-diététiques\n"
                "  - Au moins **3 traitements** anti-HTA à **posologie maximale** dont un **diurétique**\n"
                "- Rechercher : mauvaise observance, interaction médicamenteuse, **HTA secondaire**"
            )),
            FicheRow(concept="HTA secondaire", detail_md=(
                "- Indications de dépistage : point d'appel clinique, HTA grade 3, "
                "âge < 40 ans, HTA résistante\n"
                "- **Néphropathie parenchymateuse** : créat, protéinurie, sédiment urinaire\n"
                "- **HTA réno-vasculaire** : écho-Doppler AR, angio-TDM/IRM "
                "(athérome ou dysplasie fibro-musculaire)\n"
                "- **Phéochromocytome** : dosage dérivés méthoxylés urinaires/plasmatiques\n"
                "- **Hyperaldostéronisme primaire** (Conn) : rapport rénine/aldostérone\n"
                "- Syndrome de Cushing, acromégalie, hyperthyroïdie\n"
                "- **Coarctation aortique** : ETT, angio-TDM\n"
                "- **SAOS** : polysomnographie\n"
                "- Iatrogène : cocaïne, amphétamines, AINS, corticoïdes, ciclosporine, réglisse"
            )),
        ]),
        SousPartie(lettre="C", titre="Traitement et complications", rows=[
            FicheRow(concept="Objectifs", detail_md=(
                "- TA < **140/90 mmHg** (objectif général)\n"
                "- PAS < **150 mmHg** chez sujet > 80 ans"
            )),
            FicheRow(concept="RHD", detail_md=(
                "- Indiquées pour **tous** les patients HTA\n"
                "- Sevrage tabagique, réduction consommation d'alcool\n"
                "- Contrôle du poids (IMC < 25), lutte contre la sédentarité\n"
                "- Limiter l'apport sodé"
            )),
            FicheRow(concept="Traitement anti-HTA", detail_md=(
                "- Après 3 mois de RHD si non contrôlée sur mesure ambulatoire "
                "(d'emblée si diabète ou HTA grade 3)\n"
                "- **1re intention** en bithérapie de préférence :\n"
                "  - **Inhibiteur calcique** : amlodipine, lercanidipine\n"
                "  - **IEC** ou ARA2 si intolérance : périndopril, ramipril\n"
                "  - **Diurétique thiazidique** : indapamide, hydrochlorothiazide\n"
                "- **2e intention** : bétabloquant, alphabloquant, antihypertenseurs centraux\n"
                "- Majoration si non contrôlé après 3 mois"
            )),
            FicheRow(concept="Complications de l'HTA", detail_md=(
                "- **Neurologiques** : AVC ischémique, AIT, hémorragie cérébrale, "
                "encéphalopathie hypertensive, démence vasculaire, rétinopathie hypertensive\n"
                "- **CV** : SCA, HVG, dysfonction diastolique VG, FA, AOMI\n"
                "- **Rénales** : néphro-angiosclérose, insuffisance rénale\n"
                "- **HTA maligne** : HTA grade 3 + atteinte d'organe aiguë "
                "(oedème papillaire, ICG, IRA, protéinurie, hématurie) => USIC, urapidil ou nicardipine IVSE"
            )),
        ]),
    ])

    # ── PARTIE III : DYSLIPIDÉMIE ──
    partie_iii = Partie(numero="III", titre="Dyslipidémie", sous_parties=[
        SousPartie(lettre="A", titre="Diagnostic et classification", rows=[
            FicheRow(concept="Bilan lipidique", detail_md=(
                "- Après **12h de jeun**\n"
                "- Valeurs normales : LDL-c < 1,6 g/L, TG < 1,5 g/L, HDL-c > 0,40 g/L\n"
                "- **Formule de Friedewald** (si TG < 3,4 g/L) :\n"
                "  - LDL-c = CT - HDL-c - TG/5 (en g/L)"
            )),
            FicheRow(concept="Étiologies secondaires", detail_md=(
                "- **Hypercholestérolémie** secondaire : hypothyroïdie, cholestase, "
                "syndrome néphrotique, grossesse, Cushing, anorexie mentale, immunosuppresseurs\n"
                "- **Hypertriglycéridémie** secondaire : obésité, diabète de type 2, "
                "alcool, hypothyroïdie, grossesse (TG x2 au 3e trimestre), "
                "médicaments (CTC, isotrétinoïne, bétabloquants, thiazidiques)"
            )),
            FicheRow(concept="◆ Dyslipidémie primitive", detail_md=(
                "- A suspecter si LDL-c > 1,9 g/L (adulte) ou > 1,6 g/L (enfant), "
                "MCV athéromateuse précoce, signes cliniques évocateurs\n"
                "- **Xanthomes tendineux**, arc cornéen avant 45 ans\n"
                "- Hypercholestérolémie familiale monogénique (mutation récepteur LDL-c, type IIa)\n"
                "- Hyperlipidémie combinée familiale, dysbêtalipoprotéinémie (type III)"
            )),
        ]),
        SousPartie(lettre="B", titre="Prise en charge thérapeutique", rows=[
            FicheRow(concept="Objectifs LDL-c", detail_md=(
                "| Niveau de risque | Objectif LDL-c |\n"
                "|-----------------|----------------|\n"
                "| Très haut risque / prévention secondaire | < **0,55 g/L** |\n"
                "| Événements CV récurrents | < **0,4 g/L** |\n"
                "| Haut risque | < **0,7 g/L** |\n"
                "| Risque modéré | < **1 g/L** |\n"
                "| Bas risque | < 1,16 g/L |\n"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **RHD** : arrêt tabac, perte de poids, alimentation équilibrée, "
                "exercice physique >= 30 min/jour\n"
                "- **1re intention : Statines** +++ (simvastatine, atorvastatine)\n"
                "- Si objectif non atteint : + **Ezetimibe**\n"
                "- **Ac anti-PCSK9** : en prévention secondaire ou hypercholestérolémie familiale "
                "non contrôlée sous statines fortes doses + ezetimibe\n"
                "- Patient > 75 ans : statines en prévention secondaire uniquement"
            )),
            FicheRow(concept="Surveillance", detail_md=(
                "- Bilan lipidique avant traitement + contrôle à **4-6 semaines**\n"
                "- **ALAT > 3N** : arrêter ou réduire posologie, contrôle à 4-6 semaines\n"
                "- Dosage CPK si symptôme musculaire inexpliqué (pas de dosage systématique)"
            )),
            FicheRow(concept="", detail_md=(
                "- Les **statines** sont le traitement de 1re intention quelle que soit la cause "
                "de la dyslipidémie\n"
                "- Objectif LDL-c < **0,55 g/L** en prévention secondaire"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE IV : MALADIE CORONAIRE ──
    partie_iv = Partie(numero="IV", titre="Maladie coronaire", sous_parties=[
        SousPartie(lettre="A", titre="Angor d'effort", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Déséquilibre besoins-apports en O2 => **ischémie myocardique**\n"
                "- Déclenché par l'effort ou l'émotion\n"
                "- Sténose significative : **70%** pour les principaux troncs, "
                "**50%** pour le tronc commun"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- DT **d'effort** ou au froid ou en postprandial\n"
                "- **Constrictive**, rétrosternale, irradiant bras et mâchoire\n"
                "- Cédant en quelques secondes à la **trinitrine** (TNT)\n"
                "- Disparaissant à l'arrêt de l'effort\n"
                "- Formes atypiques : dyspnée, blockpnée d'effort\n"
                "- ⚠ Ischémie **silencieuse** du diabétique"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- **ECG** : repos normal, per-critique anormal\n"
                "- **Épreuve d'effort** : positive si modifications ECG et/ou DT "
                "(interprétable si 85% de la FMT atteinte). "
                "CI : RAo serré symptomatique, CMH obstructive, HTA > 220/120\n"
                "- Tests d'ischémie avec **imagerie fonctionnelle** : "
                "scintigraphie myocardique, échographie de stress, IRM de stress\n"
                "- **CoroTDM** : score calcique, si faible probabilité clinique\n"
                "- ETT, biologie (EAL, BNP, CRP)\n"
                "- **Coronarographie** : essentiellement thérapeutique"
            )),
            FicheRow(concept="PEC de l'angor", detail_md=(
                "- **Crise** : repos + dérivés nitrés sublingual (NATISPRAY) => "
                "consulter en urgence si persistance DT\n"
                "- **Fond** :\n"
                "  - Contrôle des FdRCV, exercice physique, éducation thérapeutique\n"
                "  - **Bétabloquants** : aténolol, bisoprolol (CI si angor de Prinzmetal)\n"
                "  - **Anticalciques** si CI aux BB ou angor spastique\n"
                "  - **AAP** : aspirine 75 mg/j + clopidogrel 75 mg/j après stent\n"
                "  - Statines, IEC ou ARA2 si FEVG altérée\n"
                "- **Revascularisation** après test fonctionnel : angioplastie + stent "
                "=> bithérapie AAP (aspirine + clopidogrel) 6 mois si risque hémorragique faible"
            )),
            FicheRow(concept="◆ Dépistage ischémie silencieuse (diabétique)", detail_md=(
                "- DT1 > 45 ans évoluant > 15 ans + >= 2 FdRCV\n"
                "- DT1 > 45 ans et reprise activité physique\n"
                "- DT2 évoluant > 10 ans ou > 60 ans + >= 2 FdRCV\n"
                "- Atteinte vasculaire extracardiaque ou protéinurie + 2 FdRCV"
            )),
        ]),
        SousPartie(lettre="B", titre="SCA avec sus-décalage du ST (SCA ST+)", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Nécrose myocardique** d'origine ischémique\n"
                "- Athérome coronarien +++ (rupture de plaque => thrombose occlusive)"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- DT rétrosternale en barre, constrictive, irradiant avant-bras et mâchoire\n"
                "- **Prolongée > 20 min**, **trinitro-résistante**\n"
                "- Possible douleur atypique, épigastrique, asthénie, nausées"
            )),
            FicheRow(concept="ECG 18 dérivations en urgence", detail_md=(
                "- **Sus-décalage ST** dans un territoire : > 1 mm frontales, > 2 mm précordiales\n"
                "- **Miroir** : sous-décalage ST dans le territoire opposé\n"
                "- BdB gauche : perte de la discordance (sous-ST en V1-V2, sus-ST en V5-V6)\n"
                "- Onde Q de nécrose"
            )),
            FicheRow(concept="Autres étiologies", detail_md=(
                "- Spasme coronaire (Prinzmetal)\n"
                "- **Tako-Tsubo** : sidération myocardique catécholaminergique liée au stress "
                "(DT + sus-ST + troponine positive + coro normale + akinésie apicale transitoire)\n"
                "- Embolies coronaires, thrombose de stent, dissection aortique\n"
                "- Cocaïne, CIVD, thrombocytémie essentielle"
            )),
            FicheRow(concept="PEC immédiate", detail_md=(
                "- Transfert SAMU => **USIC**, scope, DAI à portée\n"
                "- Morphine IV si douleur +++\n"
                "- **Double AAP en dose de charge** :\n"
                "  - Aspirine **250 mg IV**\n"
                "  - Ticagrelor 180 mg PO (CI si ATCD AVC hémorragique) ou "
                "prasugrel 60 mg PO (CI si ATCD AVC ischémique) ou clopidogrel 600 mg\n"
                "- **Anticoagulation** : HNF 70 UI/kg en bolus"
            )),
            FicheRow(concept="Revascularisation", detail_md=(
                "- Si délai 1er contact - salle d'angioplastie **< 120 min** => "
                "**coronarographie** pour angioplastie primaire\n"
                "- Si délai **> 120 min** => **fibrinolyse** en urgence\n"
                "- Signes de reperfusion : sédation douleur, arythmies ventriculaires (ESV, TV, RIVA), "
                "régression du sus-ST"
            )),
            FicheRow(concept="", detail_md=(
                "- Le délai **< 120 min** entre le 1er contact médical et l'angioplastie "
                "est le critère décisionnel fondamental\n"
                "- Si fibrinolyse : seul le **clopidogrel** est autorisé comme anti-P2Y12"
            ), kind="a_retenir"),
            FicheRow(concept="PEC au long cours", detail_md=(
                "- PEC des FdRCV, éducation thérapeutique\n"
                "- **Bi-AAP** pendant 1 an : aspirine 75 mg + ticagrelor 90 mg x2/j "
                "ou prasugrel 10 mg ou clopidogrel 75 mg\n"
                "- **Bétabloquant** (CI en phase aiguë d'IDM inférieur)\n"
                "- **IEC** ou ARA2\n"
                "- Anti-aldostérone (aldactone) si FEVG < **35%**\n"
                "- **Statines forte dose** +/- ezetimibe\n"
                "- IPP si besoin, diurétiques si IC"
            )),
            FicheRow(concept="Complications précoces", detail_md=(
                "- **Mort subite** sur troubles du rythme ventriculaire\n"
                "- TdR ventriculaires : TV => CEE si mal tolérée, FV = ACR\n"
                "- TdR auriculaires : FA\n"
                "- Troubles de conduction : bradycardie sinusale, BAV\n"
                "- **Complications mécaniques** (ETT +++) :\n"
                "  - Choc cardiogénique\n"
                "  - **IM** (dilatation anneau, dysfonction/rupture pilier) => OAP massif, chirurgie\n"
                "  - **Rupture septale** => CIV, chirurgie différée\n"
                "  - **Tamponnade** sur rupture paroi libre VG\n"
                "  - Thrombose précoce de stent"
            )),
            FicheRow(concept="Complications tardives (> J15)", detail_md=(
                "- **IC chronique** : traitement IC, discuter DAI\n"
                "- TdR ventriculaires : DAI si FEVG < **35%** à 6 semaines malgré traitement optimal\n"
                "- **Anévrisme ventriculaire** : persistance sus-ST > 3 semaines, "
                "thrombus intra-ventriculaire possible\n"
                "- Thrombose/resténose de stent\n"
                "- Péricardite tardive = **Syndrome de Dressler** (3e semaine)\n"
                "- Syndrome épaule-main"
            )),
        ]),
        SousPartie(lettre="C", titre="SCA sans sus-décalage du ST (SCA non ST+)", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Thrombose coronaire non occlusive**\n"
                "- DT angineuse prolongée > 20 min, au repos"
            )),
            FicheRow(concept="Diagnostic", detail_md=(
                "- **ECG 18 dérivations en urgence** (< 10 min) : toute anomalie "
                "qui n'est pas un sus-ST => sous-ST, ondes T négatives ou très pointues\n"
                "- **Troponines ultra-sensibles** +++\n"
                "- Bio : NFS, plaquettes, ionogramme, créat, BH, lipase\n"
                "- ETT, RP : pour diagnostics différentiels"
            )),
            FicheRow(concept="Stratification du risque", detail_md=(
                "- En fonction : ATCD (coronaropathie, FdRCV), âge, DT, examen clinique "
                "(PA, FC, Killip), ECG, troponine, créatinine, hémoglobine\n"
                "- Détermine l'indication et le **délai de la coronarographie** ou test fonctionnel"
            )),
            FicheRow(concept="PEC immédiate", detail_md=(
                "- Transfert SAMU, hospitalisation USIC\n"
                "- Scope, O2 si SpO2 < 95%, morphine IV si douleur\n"
                "- **Dérivés nitrés** sublingual ou IVSE si PAS > 100 mmHg\n"
                "- **Bétabloquants** PO : bisoprolol ou aténolol\n"
                "- **Aspirine** 150-300 mg PO ou IV\n"
                "- Pas d'inhibiteur P2Y12 **avant** la coronarographie\n"
                "- Anticoagulation : **fondaparinux** 2,5 mg SC\n"
                "- IPP (pantoprazole)"
            )),
            FicheRow(concept="PEC au long cours", detail_md=(
                "- Bi-AAP : aspirine 75 mg/j + ticagrelor 90 mg x2/j ou clopidogrel 75 mg/j "
                "pendant **6 mois**\n"
                "- Bétabloquant, IEC, aldactone si FEVG < 35%\n"
                "- Statines forte dose +/- ezetimibe\n"
                "- **Pas d'anticoagulant** au long cours"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Dans le SCA non ST+ : **pas d'inhibiteur P2Y12** avant la coronarographie\n"
                "- ⚠ Contrairement au SCA ST+, l'anticoagulation de choix est le "
                "**fondaparinux** (et non l'HNF)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Arrêt cardio-respiratoire", rows=[
            FicheRow(concept="Diagnostic", detail_md=(
                "- **Ventilation absente** ou anormale (gasps)\n"
                "- Absence de réponse à la stimulation\n"
                "- **Abolition pouls** fémoral et carotidien (recherche < 10 secondes)\n"
                "- Hypotonie totale"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **Ischémique** +++ : SCA ST+ (le plus fréquent), cardiopathie ischémique ancienne\n"
                "- CMD avec altération sévère FEVG\n"
                "- CMH : **mort subite à l'effort** +++\n"
                "- Dysplasie arythmogène du VD, myocardite\n"
                "- Congénitales : Wolff-Parkinson-White, Brugada, QT long/court"
            )),
            FicheRow(concept="PEC : ABCD", detail_md=(
                "- Alerter : appel SAMU 15\n"
                "- **A** (Airways) : libération voies aériennes\n"
                "- **B** (Breathing) : insufflation si RCP à 2 personnes ; IOT + O2 15 L/min en hospitalier\n"
                "- **C** (Circulation) : MCE sur plan dur, mains sur sternum, **100/min**, "
                "dépression ~5 cm, décompression passive\n"
                "- **D** (Défibrillateur) : défibrillation externe"
            )),
            FicheRow(concept="◆ Dissociation électromécanique", detail_md=(
                "- Activité cardiaque scopique **sans efficacité circulatoire**\n"
                "- QRS larges : hyperK+ ou intoxication tricycliques => **alcalinisation**\n"
                "- QRS fins : tamponnade => drainage, PNO => drainage, "
                "EP massive => thrombolyse, hypovolémie => remplissage"
            )),
        ]),
    ])

    # ── PARTIE V : INSUFFISANCE CARDIAQUE ──
    partie_v = Partie(numero="V", titre="Insuffisance cardiaque", sous_parties=[
        SousPartie(lettre="A", titre="Diagnostic et classification", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Incapacité du coeur à délivrer un **débit suffisant**\n"
                "- IC droite (ICD), gauche (ICG), ou globale"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- **ICG** : dyspnée selon NYHA, orthopnée, toux nocturne, "
                "tachypnée, crépitants bilatéraux\n"
                "- **ICD** : hépatalgies d'effort/repos, TJ, RHJ, hépatomégalie, "
                "OMI prenant le godet, ascite\n"
                "- IC aiguë : choc cardiogénique, OAP"
            )),
            FicheRow(concept="★ Facteurs déclenchants", detail_md=(
                "- **SCA**, EP, poussée hypertensive\n"
                "- Trouble du rythme ou de la conduction\n"
                "- Tamponnade\n"
                "- Écart au régime sans sel, anémie, infection pulmonaire\n"
                "- **Iatrogène** : inotropes négatifs, bétabloquants"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- **ECG** : tachycardie sinusale, signes étiologiques\n"
                "- **RP** : cardiomégalie (ICT > 0,5), surcharge pulmonaire, "
                "épanchements pleuraux\n"
                "- **Biologie** : BNP et NT-proBNP\n"
                "  - Dyspnée chronique : BNP > 35 pg/L / NT-proBNP > 125 pg/L\n"
                "  - Dyspnée aiguë : BNP > 100 pg/L / NT-proBNP > 300 pg/L\n"
                "- **ETT** +++ : FEVG, VG dilaté/hypertrophié, cinétique, "
                "valvulopathies, VD, OG, pressions pulmonaires"
            )),
            FicheRow(concept="★ ◆ Classification FEVG", detail_md=(
                "| Type | FEVG |\n"
                "|------|------|\n"
                "| IC à FEVG **altérée** | < 40% |\n"
                "| IC à FEVG **modérément altérée** | 40-49% |\n"
                "| IC à FEVG **préservée** | >= 50% |\n"
            )),
        ]),
        SousPartie(lettre="B", titre="Étiologies", rows=[
            FicheRow(concept="Étiologies de l'ICG", detail_md=(
                "- **Cardiopathie ischémique** +++ (1re cause)\n"
                "- Cardiopathie hypertensive\n"
                "- **CMD** : génétique, alcoolique, post-myocardite, carence B12, "
                "iatrogènes (anthracyclines, herceptin)\n"
                "- **CMH** +/- obstructive : génétique, amylose\n"
                "- Cardiomyopathies restrictives : amylose cardiaque\n"
                "- **Valvulopathies** : IM, IA, RM, RA\n"
                "- TdR ou de la conduction : TSV, TV\n"
                "- Péricardite chronique constrictive\n"
                "- Cardiopathies congénitales"
            )),
            FicheRow(concept="Causes d'ICD", detail_md=(
                "- **ICG** : 1re cause d'ICD +++\n"
                "- Pathologies pulmonaires\n"
                "- HTP\n"
                "- Valvulopathies droites\n"
                "- Infarctus du VD"
            )),
        ]),
        SousPartie(lettre="C", titre="Traitement de fond de l'IC à FE altérée", rows=[
            FicheRow(concept="Quadrithérapie de base", detail_md=(
                "- Association systématique pour **tout patient IC à FE altérée** :\n"
                "  - **Bétabloquant** cardiosélectif : bisoprolol 10 mg/j\n"
                "  - **IEC** (ramipril) ou ARA2 (valsartan) si toux, "
                "ou **sacubitril/valsartan** si FEVG < 35%\n"
                "  - **Anti-aldostérone** : spironolactone ou éplérénone\n"
                "  - **iSGLT2** : dapagliflozine/empagliflozine 10 mg/j "
                "(patient diabétique ou non)"
            )),
            FicheRow(concept="Traitements complémentaires", detail_md=(
                "- **Ivabradine** si FC > 70/min ou CI aux bétabloquants\n"
                "- **Digoxine** si FA avec FC > 70/min\n"
                "- **Diurétiques de l'anse** (furosémide) si signes congestifs, "
                "à posologie minimale efficace\n"
                "- Si FEVG < 35% malgré 3 mois de traitement optimal : "
                "**DAI** en prévention primaire. Si QRS > 130 ms : DAI + resynchronisation"
            )),
            FicheRow(concept="Tableau des molécules", detail_md=(
                "| Classe | Molécule | EI principaux | Surveillance |\n"
                "|--------|----------|---------------|-------------|\n"
                "| BB | Bisoprolol | Bradycardie, hypoTA | TA, FC |\n"
                "| IEC | Ramipril | **Toux**, hypoTA, hyperK, IR | TA, créat, K |\n"
                "| ARA2 | Valsartan | HypoTA, hyperK, IR | TA, créat, K |\n"
                "| Anti-aldo | Spironolactone | HypoTA, hyperK, gynécomastie | TA, créat, K |\n"
                "| Diurétique anse | Furosémide | HypoTA, hypoK | TA, créat, K, Na |\n"
                "| ARNI | Sacubitril/valsartan | HypoTA, IRA | TA, créat |\n"
                "| iSGLT2 | Dapagliflozine | Hypoglycémie, acidocétose | Glycémie |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- **Médicaments CI** dans l'IC : inhibiteurs calciques bradycardisants "
                "(vérapamil, diltiazem), anti-arythmiques de classe I (flécaïne)\n"
                "- La quadrithérapie doit être instaurée **chez tous** les patients IC à FE altérée"
            ), kind="a_retenir"),
            FicheRow(concept="Suivi", detail_md=(
                "- Cardiologue 1/an, MT 1/6 mois\n"
                "- Clinique : NYHA, poids, observance, FC, PA, signes IC\n"
                "- Biologie : ionogramme et créatinine 1/6 mois\n"
                "- ECG, ETT si modification clinique\n"
                "- Si IC réfractaire : assistance, transplantation"
            )),
        ]),
        SousPartie(lettre="D", titre="OAP et complications", rows=[
            FicheRow(concept="★ OAP", detail_md=(
                "- IC brutale : dyspnée + polypnée + désaturation\n"
                "- **Appel SAMU**, hospitalisation USIC\n"
                "- Position assise/demi-assise, VVP, monitorage (FC, PA, SpO2, scope)\n"
                "- **O2** pour SpO2 > 90% (lunettes, MHC, VNI, IOT si insuffisant)\n"
                "- **Furosémide 80 mg IV** à adapter à la diurèse\n"
                "- **Dérivés nitrés IVSE** (trinitrine 1 mg/h) si PAS > 100 mmHg\n"
                "- Anticoagulation préventive HBPM\n"
                "- Diminution/arrêt BB selon hémodynamique"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Dérivés nitrés **CI si PAS < 100 mmHg**\n"
                "- ⚠ Ne pas oublier l'anticoagulation préventive systématique"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE VI : FIBRILLATION ATRIALE ──
    partie_vi = Partie(numero="VI", titre="Fibrillation atriale", sous_parties=[
        SousPartie(lettre="A", titre="Diagnostic et classification", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **TdR le plus fréquent**\n"
                "- Perte de l'activité atriale organisée => perte contraction atriale "
                "et accélération fréquence ventriculaire"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- Asymptomatique, palpitations, dyspnée/orthopnée\n"
                "- Rythme cardiaque **irrégulier**, pouls d'amplitude variable\n"
                "- Tolérance hémodynamique variable, possibles signes IC"
            )),
            FicheRow(concept="ECG", detail_md=(
                "- **Tachycardie irrégulière à QRS fins**\n"
                "- Absence d'ondes P, **trémulation** de la ligne de base\n"
                "- Rythme ventriculaire irrégulier\n"
                "- QRS large possible si BdB associé\n"
                "- FA régulière possible si BAV3 associé"
            )),
            FicheRow(concept="Classification", detail_md=(
                "| Type | Définition |\n"
                "|------|------------|\n"
                "| **Paroxystique** | Réduction spontanée < 7 jours (souvent < 48h) |\n"
                "| **Persistante** | > 7 jours, nécessite cardioversion |\n"
                "| **Persistante longue durée** | > 1 an avec stratégie contrôle rythme |\n"
                "| **Permanente** | FA tolérée au long cours |\n"
            )),
            FicheRow(concept="Bilan complémentaire", detail_md=(
                "- Biologie : ionogramme, **TSH**, fonction rénale, BH, NFS, plaquettes\n"
                "- RP, ETT (cardiopathie, FEVG, PAP)\n"
                "- **ETO** : recherche thrombus OG si cardioversion avant 3 semaines de TAC\n"
                "- Holter ECG, test d'effort si FA induite par l'effort"
            )),
            FicheRow(concept="★ Étiologies", detail_md=(
                "- **Cardiaques** : valvulopathies, CMH, cardiopathie hypertensive, CMI, "
                "post-CCV, péricardite, SCA\n"
                "- **Extracardiaques** : pneumopathies, infections, **hyperthyroïdie**, "
                "hypoK+, hypoMg2+, phéochromocytome, alcool aigu\n"
                "- FA idiopathique"
            )),
        ]),
        SousPartie(lettre="B", titre="Prise en charge thérapeutique", rows=[
            FicheRow(concept="Prévention thromboembolique", detail_md=(
                "- TAC au long cours pour toute FA si **CHA2DS2-VASc >= 1** (homme) "
                "ou **>= 2** (femme)\n"
                "- **1re intention : AOD** :\n"
                "  - Dabigatran 150 mg x2/j (110 mg x2/j si DFG 30-45, > 75 ans, vérapamil)\n"
                "  - Rivaroxaban 20 mg/j (15 mg si DFG 15-49)\n"
                "  - Apixaban 5 mg x2/j (2,5 mg x2/j si 2/3 parmi : > 80 ans, < 60 kg, créat > 133)\n"
                "- **AVK** (warfarine, INR 2-3) si CI aux AOD (IRC sévère, IH sévère, prothèse mécanique)\n"
                "- **Occlusion percutanée auricule** si CI formelle au TAC et CHA2DS2-VASc >= 4"
            )),
            FicheRow(concept="Contrôle de la FC", detail_md=(
                "- Indications : attente réduction, > 75 ans, CI anti-arythmique, RM serré, "
                "OG > 55 mm, FA > 2 ans, échec réduction\n"
                "- **FEVG préservée** : bétabloquants +++, inhibiteurs calciques bradycardisants, digoxine\n"
                "- **FEVG altérée** : bétabloquants de l'IC +++, digoxine\n"
                "- Si échec : pacemaker + ablation NAV"
            )),
            FicheRow(concept="Contrôle du rythme", detail_md=(
                "- Après **3 semaines de TAC efficace** ou contrôle ETO (absence thrombus)\n"
                "- **CEE** sous AG (cardioversion électrique)\n"
                "- **Cardioversion médicamenteuse** : amiodarone IV/PO ou flécaïne sur coeur sain\n"
                "- Prévention récidive : flécaïne (coeur sain), sotalol (CMI), amiodarone (IC)\n"
                "- Ablation FA si récidive\n"
                "- Si **FA mal tolérée** (choc, syncope, OAP massif) => **CEE en urgence**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Jamais de **flécaïne** sur coeur pathologique (cardiopathie structurelle)\n"
                "- ⚠ Cardioversion uniquement après 3 semaines de TAC ou ETO excluant un thrombus"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Complications et scores", rows=[
            FicheRow(concept="★ Score CHA2DS2-VASc", detail_md=(
                "| Critère | Points |\n"
                "|---------|--------|\n"
                "| C : IC, dysfonction VG | 1 |\n"
                "| H : HTA | 1 |\n"
                "| A2 : Âge >= 75 ans | **2** |\n"
                "| D : Diabète | 1 |\n"
                "| S2 : AVC/AIT/embolie | **2** |\n"
                "| V : Pathologie vasculaire (coronaropathie, AOMI) | 1 |\n"
                "| A : Âge 65-74 ans | 1 |\n"
            )),
            FicheRow(concept="◆ Score HAS-BLED", detail_md=(
                "| Critère | Points |\n"
                "|---------|--------|\n"
                "| H : HTA non contrôlée >= 160 | 1 |\n"
                "| A : Anomalie rénale/hépatique | 1 |\n"
                "| S : AVC (Stroke) | 1 |\n"
                "| B : Saignement (Bleeding) | 1 |\n"
                "| L : INR labile | 1 |\n"
                "| E : Elderly > 65 ans | 1 |\n"
                "| D : Drogue/Alcool | 1 |\n"
            )),
            FicheRow(concept="Complications", detail_md=(
                "- **Thromboemboliques** +++ : AVC ischémique\n"
                "- Insuffisance cardiaque\n"
                "- Récidives FA (fréquentes)\n"
                "- **Maladie rythmique auriculaire** : alternance hyperexcitabilité et "
                "bradycardie (dysfonction sinusale) => FA + pacemaker\n"
                "- **Cardiomyopathie rythmique** : altération FEVG réversible après réduction"
            )),
        ]),
    ])

    # ── PARTIE VII : VALVULOPATHIES ET PROTHÈSES ──
    partie_vii = Partie(numero="VII", titre="Valvulopathies et prothèses", sous_parties=[
        SousPartie(lettre="A", titre="Insuffisance mitrale", rows=[
            FicheRow(concept="Physiopathologie", detail_md=(
                "- Fuite de sang du VG vers l'OG en systole => dilatation OG et VG "
                "=> dysfonction VG et HTP post-capillaire"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- **IM aiguë** : OAP aigu (rupture de cordage : OAP précédé d'un claquement)\n"
                "- **IM chronique** : asymptomatique, dyspnée d'effort, orthopnée\n"
                "- **Souffle holosystolique**, foyer mitral, en jet de vapeur, "
                "irradiant vers l'aisselle\n"
                "- Éclat B2 si HTP, crépitants si IC"
            )),
            FicheRow(concept="ETT +++", detail_md=(
                "- Diagnostic positif : reflux systolique VG vers OG\n"
                "- Étiologie : dilatation annulaire, prolapsus\n"
                "- Sévérité : **SOR > 40 mm2**, reflux dans les veines pulmonaires\n"
                "- Retentissement : dilatation VG/OG, FEVG, pressions pulmonaires\n"
                "- Lésions associées"
            )),
            FicheRow(concept="Classification de Carpentier", detail_md=(
                "- Type I : mouvement valvulaire normal (perforation, dilatation anneau)\n"
                "- Type II : mouvement valvulaire excessif (**prolapsus**, rupture cordage)\n"
                "- Type III : mouvement valvulaire restrictif (RAA, IM fonctionnelle)"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **IM aiguë** : rupture cordages, rupture/dysfonction pilier ischémique\n"
                "- **IM chronique primitive** : dystrophique +++ "
                "(Barlow = dégénérescence myxoïde, dégénérescence fibro-élastique), "
                "post-rhumatismale, EI\n"
                "- **IM fonctionnelle** : remodelage VG"
            )),
            FicheRow(concept="PEC", detail_md=(
                "- **Plastie mitrale** privilégiée, sinon remplacement valvulaire "
                "(biologique ou mécanique)\n"
                "- IM aiguë : **chirurgie en urgence**\n"
                "- IM chronique : TEER (MitraClip), TMVI (TAVI mitral)\n"
                "- Traitement IC si nécessaire"
            )),
            FicheRow(concept="Complications", detail_md=(
                "- **EI** : prophylaxie +++\n"
                "- TdR : FA/flutter (dilatation OG), TdR ventriculaires (IC avancée)\n"
                "- IC tardive dans IM chronique, rapide dans IM aiguë\n"
                "- Complications thromboemboliques : thrombose OG, risque embolique (FA++)"
            )),
        ]),
        SousPartie(lettre="B", titre="Rétrécissement aortique", rows=[
            FicheRow(concept="Physiopathologie", detail_md=(
                "- Obstacle à l'éjection VG => majoration pressions VG => "
                "gradient VG-Aorte => HVG => dysfonction diastolique puis systolique"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- Asymptomatique ou symptômes **d'effort** : dyspnée, angor, **syncope**\n"
                "- Souffle foyer aortique, **mésosystolique**, rude/râpeux, intense, "
                "irradiant aux carotides, **B2 aboli**"
            )),
            FicheRow(concept="ETT +++", detail_md=(
                "- Valve aortique remaniée, bicuspide\n"
                "- **RA serré** : surface valvulaire < **1 cm2** (ou < 0,5 cm2/m2), "
                "gradient moyen > **40 mmHg**, Vmax > **4 m/s**\n"
                "- Retentissement : HVG, dilatation VG, FEVG"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **RAo dégénératif** (Monckeberg) : sujet > 65-70 ans\n"
                "- **Bicuspidie aortique** (congénitale) : sujet 30-65 ans "
                "(association : coarctation, dilatation/dissection aorte)\n"
                "- RAA (rare)"
            )),
            FicheRow(concept="PEC", detail_md=(
                "- **TAVI** : patients à haut risque ou risque chirurgical intermédiaire. "
                "Complications : troubles de conduction (PM), AVC ischémique\n"
                "- **Remplacement valvulaire chirurgical** :\n"
                "  - Prothèse **mécanique** : patient jeune, TAC à vie\n"
                "  - Prothèse **biologique** : > 65 ans, pas de TAC à vie\n"
                "- Épreuve d'effort si RA asymptomatique (CI si symptomatique)"
            )),
            FicheRow(concept="", detail_md=(
                "- La triade symptomatique du RA serré est : **dyspnée, angor, syncope d'effort**\n"
                "- Le RA serré symptomatique est une indication chirurgicale formelle"
            ), kind="a_retenir"),
            FicheRow(concept="Complications", detail_md=(
                "- **Mort subite** +++\n"
                "- IC, FA mal tolérée, troubles de conduction\n"
                "- EI, embolies calcaires systémiques"
            )),
        ]),
        SousPartie(lettre="C", titre="Endocardite infectieuse", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Infection d'une ou plusieurs valves cardiaques ou de l'endocarde pariétal\n"
                "- Diagnostic : **fièvre + souffle** = EI jusqu'à preuve du contraire"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- **Fièvre** (souvent prolongée)\n"
                "- **Souffle** +++ (surtout diastolique)\n"
                "- Signes périphériques : splénomégalie, nodules de Roth au FO, "
                "faux panaris d'Osler, placards de Janeway, purpura pétéchial\n"
                "- Recherche porte d'entrée +++\n"
                "- Signes de complications emboliques"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- **Hémocultures** +++ : 3 paires (aéro-anaérobie), à 30 min d'intervalle, "
                "au pic fébrile, avant tout ATB\n"
                "- Sérologies si hémocultures négatives : Coxiella (fièvre Q), bartonellose, "
                "Chlamydia, brucellose, Whipple\n"
                "- **ETT** +/- ETO : végétations, fuites, retentissement, abcès\n"
                "- **TEP-scanner au FDG** +++ : intérêt sur prothèse valvulaire\n"
                "- IRM cérébrale + TDM TAP : recherche emboles septiques\n"
                "- ECG quotidien : **BAV** = penser abcès de l'anneau"
            )),
            FicheRow(concept="Germes", detail_md=(
                "| Porte d'entrée | Germes |\n"
                "|----------------|--------|\n"
                "| Cutanée | **S. aureus** +++, SCN |\n"
                "| ORL/bucco-dentaire | Streptocoques oraux, HACEK |\n"
                "| Digestive | Streptocoques groupe D, entérocoques |\n"
                "| Toxicomane/KT dialyse | Fungiques |\n"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Team endocardite**, hospitalisation USIC\n"
                "- **ATB IV** adaptée à l'antibiogramme, prolongée (4-6 semaines)\n"
                "- J1 de traitement = J1 d'hémocultures négatives\n"
                "- Valve native SAMS : cloxacilline 12 g/j IV (4-6 sem)\n"
                "- Valve native SAMR : vancomycine 30-60 mg/kg/j IV\n"
                "- Entérocoque : amoxicilline 200 mg/kg/j + gentamicine 3 mg/kg/j\n"
                "- Sur prothèse : ajouter rifampicine + gentamicine 2 semaines"
            )),
            FicheRow(concept="Indications chirurgicales", detail_md=(
                "- **3 indications** : IC, infection non contrôlée, prévention embolie\n"
                "- Urgence < 24h : choc cardiogénique, OAP réfractaire, fistule\n"
                "- Court terme (2-3j) : IA/IM avec mauvaise tolérance, "
                "infection non contrôlée, végétation mitrale > 30 mm\n"
                "- Sur prothèse : mêmes indications + désinsertion + végétation obstructive"
            )),
            FicheRow(concept="Prophylaxie", detail_md=(
                "- Information et éducation patient\n"
                "- Hygiène stricte : consultation dentiste biannuelle, désinfection plaies, "
                "éviter tatouages/piercings\n"
                "- **ATBprophylaxie** pour patients à haut risque lors de gestes dentaires à risque : "
                "**amoxicilline 2 g PO** (ou clindamycine 600 mg si allergie) **1h avant**"
            )),
            FicheRow(concept="Complications", detail_md=(
                "- **Cardiaques** : IC, OAP, abcès myocardique, troubles conductifs\n"
                "- **Infectieuses** : choc septique, emboles septiques "
                "(FDR : végétation > 10 mm, mobile, mitrale, S. aureus)\n"
                "- **Anévrismes mycotiques** : TDM/IRM, embolisation "
                "(CI anticoagulation curative sauf prothèse mécanique)\n"
                "- Rénales : GN, infarctus rénal, IRA, néphrotoxicité ATB\n"
                "- Neurologiques : AVC ischémiques"
            )),
        ]),
        SousPartie(lettre="D", titre="Prothèses valvulaires cardiaques", rows=[
            FicheRow(concept="Types de prothèses", detail_md=(
                "- **Prothèses mécaniques** : anticoagulation **AVK à vie**. "
                "Doubles ailettes = St Jude\n"
                "- **Prothèses biologiques** (bioprothèses) : hétérogreffes (porc), "
                "homogreffes (humain), autogreffes. Pas de TAC à vie"
            )),
            FicheRow(concept="Surveillance", detail_md=(
                "- Bilan de référence à **6-12 semaines** post-intervention\n"
                "- Clinique tous les 3-6 mois (MT), 1/an (cardiologue)\n"
                "- **INR** +++ pour prothèses mécaniques\n"
                "- Bioprothèse mitrale/tricuspide : AVK 3 mois. "
                "Bioprothèse aortique : aspirine 3 mois. "
                "TAVI : aspirine + clopidogrel 3-6 mois\n"
                "- ETT, ECG, Rx thoracique, bilan stomatologique 2 fois/an"
            )),
            FicheRow(concept="Complications", detail_md=(
                "- **Thrombose de prothèse** +++ : suspecter si majoration gradient, "
                "dyspnée, embole\n"
                "  - Obstructive : brutale, IC aiguë, ACR => urgence USIC, HNF IVSE\n"
                "  - Non obstructive : embolies périphériques, plus insidieuse\n"
                "- **EI sur prothèse** : ETT + ETO, TEP-TDM au FDG. "
                "Risque : désinsertion, embolies\n"
                "- Hémolyse : anémie régénérative, LDH > 2N\n"
                "- **Dégénérescence** : médiane 8-10 ans mitrale, 12-15 ans aortique"
            )),
            FicheRow(concept="", detail_md=(
                "- La **chirurgie dentaire** ne nécessite **pas** d'arrêt des AVK "
                "chez le porteur de prothèse mécanique\n"
                "- Si nécessité d'arrêt des AVK : relais par HNF"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE VIII : MALADIE THROMBOEMBOLIQUE ET AOMI ──
    partie_viii = Partie(numero="VIII", titre="Maladie thromboembolique et AOMI", sous_parties=[
        SousPartie(lettre="A", titre="Embolie pulmonaire et TVP", rows=[
            FicheRow(concept="FDR de MTEV", detail_md=(
                "| | Transitoires | Persistants |\n"
                "|--|-------------|-------------|\n"
                "| **Majeurs** | Chirurgie AG > 30 min, immobilisation > 3j, "
                "COP/grossesse/post-partum | Néoplasie active, thrombophilie majeure (SAPL) |\n"
                "| **Mineurs** | Trauma MI, voyage > 6h | Thrombophilie non majeure "
                "(prot. C/S, Leiden), MICI |\n"
            )),
            FicheRow(concept="★ Clinique EP", detail_md=(
                "- **DT** + **dyspnée** isolée + hémoptysie\n"
                "- Signes de choc si EP grave\n"
                "- ICD : TJ, RHJ, OMI\n"
                "- Tachypnée, tachycardie\n"
                "- Auscultation pulmonaire **normale**"
            )),
            FicheRow(concept="Clinique TVP", detail_md=(
                "- Douleur unilatérale MI\n"
                "- Oedème unilatéral, cyanose déclive, circulation collatérale\n"
                "- Chaleur cutanée, Homans positif\n"
                "- Veines superficielles dilatées"
            )),
            FicheRow(concept="Score de Wells (EP)", detail_md=(
                "| Critère | Points |\n"
                "|---------|--------|\n"
                "| ATCD EP/TVP | +1,5 |\n"
                "| Chirurgie/immobilisation < 4 sem | +1,5 |\n"
                "| Cancer actif | +1 |\n"
                "| Hémoptysie | +1 |\n"
                "| FC > 100/min | +1 |\n"
                "| Signes de TVP | +3 |\n"
                "| Diagnostic alternatif moins probable | +3 |\n"
                "| **Faible : 0-1 / Intermédiaire : 2-6 / Forte : >= 7** | |\n"
            )),
            FicheRow(concept="Examens EP", detail_md=(
                "- RP : normale, atélectasie, épanchement pleural\n"
                "- ECG : normal, BdBD, S1Q3, tachycardie, T neg V1-V3\n"
                "- GDS : hypoxémie + hypocapnie, effet shunt (PaO2 + PaCO2 < 90)\n"
                "- **D-dimères** si probabilité faible/intermédiaire "
                "(seuil ajusté : >= 500 si <= 50 ans, >= 10 x âge si > 50 ans)\n"
                "- **Angioscanner** si probabilité forte ou D-dimères positifs\n"
                "- Écho-Doppler MI : recherche TVP\n"
                "- Scintigraphie V/Q si CI angioscanner\n"
                "- ETT si EP à haut risque"
            )),
            FicheRow(concept="◆ Score sPESI (pronostic)", detail_md=(
                "| Critère | Points |\n"
                "|---------|--------|\n"
                "| Âge > 80 ans | +1 |\n"
                "| SpO2 < 90% | +1 |\n"
                "| PAS < 100 mmHg | +1 |\n"
                "| FC > 110/min | +1 |\n"
                "| Cancer | +1 |\n"
                "| IC ou IRC | +1 |\n"
                "| **0 pt = mortalité J30 faible / >= 1 pt = élevée** | |\n"
            )),
            FicheRow(concept="PEC anticoagulante", detail_md=(
                "- **Urgence thérapeutique**, TAC dès suspicion diagnostique\n"
                "- **AOD en 1re intention** :\n"
                "  - Rivaroxaban 15 mg x2/j (21j) puis 20 mg/j\n"
                "  - Apixaban 10 mg x2/j (7j) puis 5 mg x2/j\n"
                "  - Dabigatran 150 mg x2/j après 5j d'anticoagulation parentérale\n"
                "- **AVK** si CI aux AOD (relais héparine) : INR 2-3\n"
                "- HBPM, HNF ou fondaparinux en phase initiale\n"
                "- Durée : 3-6 mois si facteur transitoire majeur, > 6 mois si récidive "
                "ou facteur persistant, HBPM si néoplasie active"
            )),
            FicheRow(concept="Mesures associées", detail_md=(
                "- **Contention veineuse** si TVP ou EP avec TVP\n"
                "- **Fibrinolyse** si EP à haut risque\n"
                "- **Filtre cave** si CI au TAC ou récidive sous TAC\n"
                "- Embolectomie chirurgicale si échec thrombolyse"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Les D-dimères sont **inutiles** si probabilité clinique forte => "
                "angioscanner d'emblée\n"
                "- ⚠ Seuil D-dimères ajusté à l'âge après 50 ans : >= 10 x âge"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="AOMI et ischémie aiguë de membre", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Obstruction partielle/totale des artères des MI\n"
                "- Homme > femme, prévalence 4% après 40 ans\n"
                "- FdR : **tabac** ++, **diabète** ++, dyslipidémie, HTA"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- **Claudication intermittente** : crampe du mollet à la marche, "
                "périmètre de marche, disparition < 5 min à l'arrêt\n"
                "- **Douleurs de décubitus** : brûlures orteils/avant-pied, "
                "améliorées en position déclive, insomniantes\n"
                "- Douleurs permanentes, dysfonction érectile\n"
                "- Pied froid, abolition pouls, TRC > 3 sec\n"
                "- Troubles trophiques : peau mince, perte pilosité, ulcères artériels, gangrène"
            )),
            FicheRow(concept="IPS", detail_md=(
                "- **IPS** = PAS cheville / PAS bras\n"
                "- Normal : 1,00-1,30\n"
                "- **AOMI** : IPS < **0,9**\n"
                "- AOMI sévère : IPS < 0,60\n"
                "- IPS > 1,40 : rigidité artérielle (médiacalcose : diabétique, âgé, dialysé)"
            )),
            FicheRow(concept="Classification de Leriche et Fontaine", detail_md=(
                "| Stade | Description |\n"
                "|-------|------------|\n"
                "| I | Asymptomatique |\n"
                "| II | Claudication intermittente |\n"
                "| III | Douleurs de décubitus |\n"
                "| IV | Troubles trophiques |\n"
            )),
            FicheRow(concept="PEC AOMI", detail_md=(
                "- Contrôle des FdRCV : sevrage tabac, HTA, dyslipidémie, diabète\n"
                "- Dès stade asymptomatique :\n"
                "  - **Statines** même sans dyslipidémie\n"
                "  - **IEC ou ARA2** même sans HTA\n"
                "  - **AAP** (aspirine ou clopidogrel) si symptomatique\n"
                "- Ischémie d'effort : réadaptation marche, revascularisation si échec 3 mois\n"
                "- Ischémie de repos : revascularisation, antalgiques, prévention escarres"
            )),
            FicheRow(concept="★ Ischémie aiguë de membre", detail_md=(
                "- Arrêt brutal circulation => hypoxie : apoptose nerveuse dès **2h**, "
                "musculaire dès **6h**, nécrose cutanée dès **24h**\n"
                "- Syndrome de reperfusion : hyperK+, acidose métabolique, CIVD\n"
                "- DT brutale et intense, impotence, membre froid, abolition pouls en aval\n"
                "- **Urgence** : HNF IVSE, antalgiques palier 1-2-3, "
                "protection membre, désobstruction artérielle\n"
                "- Embolie sur artère saine : embolectomie (sonde de Fogarty)\n"
                "- Thrombose sur artère pathologique : pontage/endartériectomie/angioplastie\n"
                "- Aponévrotomie si ischémie prolongée (syndrome des loges)\n"
                "- Risque d'amputation si ischémie > **6h**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ L'ischémie aiguë de membre est une **urgence** : "
                "aucun examen ne doit retarder la PEC\n"
                "- Signes de gravité : douleur à la palpation des masses musculaires "
                "(rhabdomyolyse), déficit moteur"
            ), kind="piege"),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="SCA ST+ vs SCA non ST+", markdown=(
            "| Critère | SCA ST+ | SCA non ST+ |\n"
            "|---------|---------|-------------|\n"
            "| Occlusion | Complète | Incomplète |\n"
            "| ECG | Sus-décalage ST | Sous-ST, T neg |\n"
            "| Troponine | Toujours positive | Peut être positive |\n"
            "| Anti-P2Y12 | Dose de charge immédiate | Après coronarographie |\n"
            "| Anticoagulation | HNF bolus | Fondaparinux SC |\n"
            "| Revascularisation | Angioplastie < 120 min ou fibrinolyse | Selon stratification risque |\n"
            "| Bi-AAP | 1 an | 6 mois |\n"
        )),
        TableauSynthese(titre="Traitements de l'IC à FEVG altérée", markdown=(
            "| Classe | Molécule | Posologie | EI principaux |\n"
            "|--------|----------|-----------|---------------|\n"
            "| BB | Bisoprolol | 10 mg/j | Brady, hypoTA |\n"
            "| IEC | Ramipril | 10 mg/j | Toux, hyperK |\n"
            "| Anti-aldo | Spironolactone | 12,5-75 mg/j | HyperK, gynécomastie |\n"
            "| iSGLT2 | Dapagliflozine | 10 mg/j | Hypoglycémie |\n"
            "| ARNI | Sacubitril/valsartan | Titration | HypoTA, IRA |\n"
            "| Diurétique | Furosémide | 20-40 mg/j | HypoK |\n"
        )),
        TableauSynthese(titre="Anticoagulation dans la FA", markdown=(
            "| AOD | Posologie standard | Adaptation |\n"
            "|-----|-------------------|------------|\n"
            "| Dabigatran | 150 mg x2/j | 110 mg si DFG 30-45, > 75 ans |\n"
            "| Rivaroxaban | 20 mg/j | 15 mg si DFG 15-49 |\n"
            "| Apixaban | 5 mg x2/j | 2,5 mg si >= 2/3 critères (âge, poids, créat) |\n"
            "| AVK (warfarine) | INR 2-3 | Si CI AOD, prothèse mécanique |\n"
        )),
        TableauSynthese(titre="Objectifs LDL-c selon le risque", markdown=(
            "| Niveau de risque | Objectif LDL-c |\n"
            "|-----------------|----------------|\n"
            "| Très haut risque / prévention secondaire | < 0,55 g/L |\n"
            "| Événements CV récurrents | < 0,4 g/L |\n"
            "| Haut risque | < 0,7 g/L |\n"
            "| Risque modéré | < 1 g/L |\n"
            "| Bas risque | < 1,16 g/L |\n"
        )),
        TableauSynthese(titre="Valvulopathies : IM vs RA", markdown=(
            "| Critère | IM | RA |\n"
            "|---------|----|----|---|\n"
            "| Souffle | Holosystolique, jet de vapeur, aisselle | Mésosystolique, rude, carotides |\n"
            "| Sévérité ETT | SOR > 40 mm2 | Surface < 1 cm2, gradient > 40 mmHg |\n"
            "| Chirurgie | Plastie > remplacement | TAVI ou RVA |\n"
            "| Complication redoutée | IC tardive, EI | Mort subite |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| HTA | PA >= **140/90** mmHg | Confirmée par MAPA/ATM |\n"
        "| HTA résistante | >= **3** anti-HTA max + diurétique | Non contrôlée |\n"
        "| BNP dyspnée chronique | > **35** pg/L | NT-proBNP > 125 pg/L |\n"
        "| BNP dyspnée aiguë | > **100** pg/L | NT-proBNP > 300 pg/L |\n"
        "| FEVG altérée | < **40%** | IC systolique |\n"
        "| DAI IC | FEVG < **35%** malgré 3 mois tt | Prévention primaire |\n"
        "| RA serré | Surface < **1 cm2** | Gradient > 40 mmHg, Vmax > 4 m/s |\n"
        "| SCA ST+ délai | **< 120 min** | Angioplastie vs fibrinolyse |\n"
        "| IPS normal | 1,00-1,30 | AOMI si < **0,9** |\n"
        "| D-dimères (< 50 ans) | >= **500** | Seuil ajusté > 50 ans : 10 x âge |\n"
        "| LDL-c prévention secondaire | < **0,55** g/L | Objectif thérapeutique |\n"
        "| CHA2DS2-VASc homme | >= **1** | Indication TAC |\n"
        "| Ischémie aiguë nécrose | **6h** | Risque amputation |\n"
    ))

    points_cles = [
        "L'HTA doit toujours être confirmée par mesure ambulatoire (MAPA ou ATM) avant traitement",
        "Le SCA ST+ impose une revascularisation en urgence : angioplastie si délai < 120 min, sinon fibrinolyse",
        "La quadrithérapie de l'IC à FE altérée : BB + IEC/ARNI + anti-aldostérone + iSGLT2",
        "Les médicaments CI dans l'IC : vérapamil, diltiazem, flécaïne",
        "FA : TAC au long cours si CHA2DS2-VASc >= 1 (homme) ou >= 2 (femme), AOD en 1re intention",
        "Endocardite : fièvre + souffle = EI jusqu'à preuve du contraire, hémocultures avant ATB",
        "AOMI : IPS < 0,9 ; statines et IEC dès le stade asymptomatique",
        "L'ischémie aiguë de membre est une urgence absolue : risque d'amputation après 6h",
    ]

    fiche_eclair_md = (
        "**FdRCV** : âge, sexe, ATCD familiaux, tabac, HTA, dyslipidémie, diabète, "
        "obésité. SCORE 2 pour évaluation du RCV global.\n\n"
        "**HTA** : PA >= 140/90, confirmer par MAPA/ATM. Bithérapie 1re intention : "
        "ICa + IEC/ARA2 + thiazidique. HTA résistante = rechercher HTA secondaire.\n\n"
        "**Dyslipidémie** : LDL-c < 0,55 g/L en prévention secondaire. "
        "Statines 1re intention, + ézétimibe, +/- anti-PCSK9.\n\n"
        "**Angor** : DT d'effort, trinitro-sensible. BB + AAP + statines + IEC. "
        "Revascularisation après test fonctionnel.\n\n"
        "**SCA ST+** : sus-ST, tropo+. Aspirine + P2Y12 + HNF. "
        "Angioplastie < 120 min sinon fibrinolyse. Bi-AAP 1 an.\n\n"
        "**SCA non ST+** : sous-ST/T nég. Aspirine + fondaparinux. "
        "P2Y12 après coro. Bi-AAP 6 mois.\n\n"
        "**IC** : BNP/NT-proBNP + ETT. FE altérée : BB + IEC/ARNI + anti-aldo + iSGLT2. "
        "CI : vérapamil, diltiazem, flécaïne. DAI si FE < 35%.\n\n"
        "**FA** : TdR le plus fréquent. CHA2DS2-VASc pour TAC (AOD 1re intention). "
        "Contrôle FC ou rythme. CEE si mal tolérée.\n\n"
        "**IM** : souffle holosystolique, jet de vapeur. Plastie > remplacement.\n\n"
        "**RA** : mésosystolique, B2 aboli. Serré si surface < 1 cm2. "
        "TAVI ou RVA. Mort subite si symptomatique.\n\n"
        "**EI** : fièvre + souffle. Hémocultures + ETT/ETO + TEP-FDG. "
        "ATB IV 4-6 sem. Chirurgie si IC/infection non contrôlée/embolies.\n\n"
        "**EP/TVP** : Wells/Genève, D-dimères, angioscanner. AOD 1re intention. "
        "Fibrinolyse si EP haut risque.\n\n"
        "**AOMI** : IPS < 0,9. Statines + IEC + AAP. Ischémie aiguë = urgence (6h)."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Cardiologie",
        annee="2025-2026",
        item="Items 219, 220, 221, 223, 224, 230, 231, 232, 149, 150, 327, 334",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v,
                 partie_vi, partie_vii, partie_viii],
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()

    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)

    docx_path = output_dir / "Medecine_generale_Cardiologie_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Medecine_generale_Cardiologie_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path} ({pdf_path.stat().st_size / 1e6:.1f} MB)")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

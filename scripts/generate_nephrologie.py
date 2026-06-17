"""Génère la fiche exhaustive de Néphrologie à partir du PDF source."""

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


def build_nephrologie_fiche() -> FicheData:
    plan = [
        PlanPartie(numero="I", titre="Rappels physiologiques et outils diagnostiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Physiologie rénale"),
            PlanSousPartie(lettre="B", titre="Diurétiques"),
            PlanSousPartie(lettre="C", titre="Examen urinaire et évaluation de la fonction rénale"),
            PlanSousPartie(lettre="D", titre="Biopsie rénale"),
        ]),
        PlanPartie(numero="II", titre="Troubles hydroélectrolytiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Dysnatrémies : rappels et démarche diagnostique"),
            PlanSousPartie(lettre="B", titre="Dysnatrémies : traitements"),
            PlanSousPartie(lettre="C", titre="Acidose métabolique"),
            PlanSousPartie(lettre="D", titre="Dyskaliémies : hypokaliémie"),
            PlanSousPartie(lettre="E", titre="Dyskaliémies : hyperkaliémie"),
            PlanSousPartie(lettre="F", titre="Dyscalcémies"),
        ]),
        PlanPartie(numero="III", titre="Insuffisance rénale aiguë", sous_parties=[
            PlanSousPartie(lettre="A", titre="Démarche diagnostique et classification"),
            PlanSousPartie(lettre="B", titre="IRA fonctionnelle"),
            PlanSousPartie(lettre="C", titre="IRA obstructive"),
            PlanSousPartie(lettre="D", titre="IRA organique"),
            PlanSousPartie(lettre="E", titre="IRA du greffé rénal"),
        ]),
        PlanPartie(numero="IV", titre="Maladie rénale chronique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Classification et étiologies"),
            PlanSousPartie(lettre="B", titre="Complications de la MRC"),
            PlanSousPartie(lettre="C", titre="Néphroprotection"),
            PlanSousPartie(lettre="D", titre="Suppléance : greffe et dialyse"),
        ]),
        PlanPartie(numero="V", titre="Néphropathies glomérulaires", sous_parties=[
            PlanSousPartie(lettre="A", titre="Syndrome néphrotique"),
            PlanSousPartie(lettre="B", titre="Glomérulonéphrite rapidement progressive"),
            PlanSousPartie(lettre="C", titre="Néphropathies glomérulaires spécifiques"),
        ]),
        PlanPartie(numero="VI", titre="Néphropathies spécifiques et iatrogénie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Néphropathie diabétique"),
            PlanSousPartie(lettre="B", titre="Néphropathie lupique"),
            PlanSousPartie(lettre="C", titre="Polykystose rénale autosomique dominante"),
            PlanSousPartie(lettre="D", titre="Atteinte rénale du myélome"),
            PlanSousPartie(lettre="E", titre="Iatrogénie en néphrologie"),
        ]),
    ]

    # ── PARTIE I : RAPPELS PHYSIOLOGIQUES ET OUTILS DIAGNOSTIQUES ──
    partie_i = Partie(numero="I", titre="Rappels physiologiques et outils diagnostiques", sous_parties=[
        SousPartie(lettre="A", titre="Physiologie rénale", rows=[
            FicheRow(concept="◆ Anatomie fonctionnelle", detail_md=(
                "- **Reins** : taille 12 x 6 x 3 cm\n"
                "- **Unité fonctionnelle** = néphron : glomérule + tubule (TCP - branche de Henlé - TCD - tubule collecteur)\n"
                "- 3 compartiments : **glomérulaire** / **vasculaire** / **tubulo-interstitiel**\n"
                "- Vascularisation : artères rénales, débit sanguin rénal = **20-25%** du débit cardiaque"
            )),
            FicheRow(concept="◆ Filtration glomérulaire", detail_md=(
                "- Débit plasmatique rénal = 0,55 x débit sanguin rénal\n"
                "- **DFG** = 20% du débit plasmatique rénal = **~180 L/j** soit **~120 mL/min**\n"
                "- Urine primitive ensuite réabsorbée par le tubule (> **99%**) pour former l'urine définitive"
            )),
            FicheRow(concept="◆ Grandes fonctions du rein", detail_md=(
                "- Maintien de l'**homéostasie** du milieu intérieur : équilibre ionique (Na, K, Cl, HCO3-, Ca2+), acido-basique\n"
                "- Maintien de la **volémie**\n"
                "- **Élimination des toxiques** : médicaments, déchets métaboliques\n"
                "- **Fonctions endocrines** : vitamine D active (1,25-(OH)2D3), sécrétion d'**EPO**, "
                "contrôle de la PA par sécrétion de **rénine**"
            )),
            FicheRow(concept="Système rénine-angiotensine-aldostérone", detail_md=(
                "- La **rénine** (appareil juxtaglomérulaire) convertit l'angiotensinogène en angiotensine I\n"
                "- L'**ECA** convertit l'angiotensine I en angiotensine II\n"
                "- L'angiotensine II stimule la sécrétion d'**aldostérone** par les surrénales\n"
                "- Effets : vasoconstriction, rétention hydrosodée, sécrétion d'aldostérone"
            )),
        ]),
        SousPartie(lettre="B", titre="Diurétiques", rows=[
            FicheRow(concept="◆ Furosémide (Lasilix)", detail_md=(
                "- Diurétique de l'**anse de Henlé**\n"
                "- Dose : **20 mg à 1000 mg/j** PO ou IV (dose IV = 2 x dose PO)\n"
                "- Durée d'action : environ **4h**\n"
                "- **1re intention** si : DFG < 30 mL/min, insuffisance cardiaque, syndrome néphrotique"
            )),
            FicheRow(concept="Hydrochlorothiazide", detail_md=(
                "- Diurétique **thiazidique** (TCD)\n"
                "- Dose de départ : **12,5 mg**, 1 à 2 fois/jour\n"
                "- Effet **antihypertenseur** + diurétique\n"
                "- Association possible avec furosémide si déplétion résistante (effet d'hypertrophie du TCD)"
            )),
            FicheRow(concept="Diurétiques épargneurs de K+", detail_md=(
                "- **Spironolactone** et **amiloride**\n"
                "- ⚠ **Contre-indiqués si DFG ≤ 30 mL/min**\n"
                "- Risque d'hyperkaliémie"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Adapter le choix du diurétique au **DFG** : furosémide si DFG < 30, "
                "thiazidiques si DFG > 30, épargneurs de K+ CI si DFG ≤ 30"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Examen urinaire et évaluation de la fonction rénale", rows=[
            FicheRow(concept="◆ Bandelette urinaire", detail_md=(
                "- **Protéines** : détecte uniquement l'**albumine** (fausse négative pour protéinuries de bas poids moléculaire : chaînes légères)\n"
                "- **Hématurie** : très sensible (1+ = 5000/mL), détecte l'hème → positive aussi en cas d'**hémolyse massive** ou de **rhabdomyolyse**"
            )),
            FicheRow(concept="◆ ECBU", detail_md=(
                "- **Hématurie** : détecte le GR → spécifique, quantification fine (positive si > 10 000/mL soit > **10/mm3**)\n"
                "- **Leucocyturie** : signe d'infection mais aussi d'atteinte **tubulo-interstitielle**"
            )),
            FicheRow(concept="◆ Ionogramme urinaire", detail_md=(
                "- Orientation IRA **fonctionnelle** vs **organique** :\n"
                "  - Fonctionnelle : Na < **20 mmol/L**, Na/K < 1, FE urée < **30%**\n"
                "- Protéinurie sur échantillon : rapport protéinurie/créatininurie en **g/mmol**\n"
                "  - Approximation : 0,2 g/mmol ≈ protéinurie de **2 g/j** (créatininurie ~10 mmol/j)"
            )),
            FicheRow(concept="Urines des 24h", detail_md=(
                "- Apport sodé = natriurèse (mmol/24h) / 17 (170 mmol = 10 g/24h)\n"
                "- Apport protéique = urée (mmol/24h) / 5 (400 mmol = 80 g/24h)\n"
                "- Protéinurie exacte"
            )),
            FicheRow(concept="Évaluation du DFG", detail_md=(
                "| Situation | Formule recommandée |\n"
                "|-----------|--------------------|\n"
                "| Patient standard | **CKD-EPI 2021** (pas de facteur ethnie/poids) |\n"
                "| Patient standard (alternative) | MDRD |\n"
                "| Enfant | **Schwartz** |\n"
                "| Dénutri, sarcopénie, amputation | CKD-EPI **créatinine + cystatine** |\n"
                "| Certitude requise (don de rein, néphrectomie) | **Mesure du DFG** (Iohexol) |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- La formule de **Cockcroft et Gault** est **obsolète**\n"
                "- CKD-EPI 2021 est la formule de référence actuelle, sans facteur correctif lié à l'ethnie"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Biopsie rénale", rows=[
            FicheRow(concept="◆ Examen phare", detail_md=(
                "- **Biopsie rénale** = examen de référence pour explorer une IRA ou IRC d'étiologie indéterminée"
            )),
            FicheRow(concept="◆ Bilan pré-biopsie", detail_md=(
                "- **Consentement** libre et éclairé\n"
                "- **Échographie rénale** : recherche CI locales (malformation, rein unique, kystes importants)\n"
                "- **Contrôle tensionnel**\n"
                "- **Bilan d'hémostase** : TP, TCA, plaquettes +/- temps de saignement\n"
                "- Vérifier l'absence de traitement **anticoagulant**\n"
                "- **NFS** : recherche d'anémie préalable, Hb de référence\n"
                "- **Groupe sanguin + Rhésus** : en cas de saignement nécessitant transfusion\n"
                "- **ECBU** : recherche de colonisation/infection urinaire"
            )),
            FicheRow(concept="◆ Consignes post-biopsie", detail_md=(
                "- **Décubitus dorsal strict** pendant **24h**\n"
                "- Pas de sport ni port de charge lourde pendant **10 jours**\n"
                "- Consulter en urgence si : douleurs lombaires/abdominales, **hématurie macroscopique**"
            )),
        ]),
    ])

    # ── PARTIE II : TROUBLES HYDROÉLECTROLYTIQUES ──
    partie_ii = Partie(numero="II", titre="Troubles hydroélectrolytiques", sous_parties=[
        SousPartie(lettre="A", titre="Dysnatrémies : rappels et démarche diagnostique", rows=[
            FicheRow(concept="◆ Répartition hydrique", detail_md=(
                "- Eau totale = **60%** du poids corporel (homme adulte), moins chez la femme et avec l'âge\n"
                "- Volume **intracellulaire** : 8/12 = 2/3 de l'eau totale (40% du poids)\n"
                "- Volume **extracellulaire** : 4/12 (plasmatique 1/12 = 5% du poids, interstitiel 3/12 = 15% du poids)\n"
                "- Osmolarité normale : environ **285 mOsm/kg**\n"
                "- Formule : Osm = (**Na x 2**) + glycémie (mmol/L)"
            )),
            FicheRow(concept="", detail_md=(
                "- **Volémie** = reflète la quantité de **Na+** (secteur extracellulaire)\n"
                "- **Natrémie** = reflète l'**hydratation intracellulaire**\n"
                "- Hyponatrémie = **hyperhydratation** intracellulaire\n"
                "- Hypernatrémie = **déshydratation** intracellulaire"
            ), kind="a_retenir"),
            FicheRow(concept="Hyponatrémie", detail_md=(
                "- Na < **135 mmol/L**\n"
                "- Démarche diagnostique : évaluer le **secteur extracellulaire** (clinique) :\n"
                "  - **Déshydratation extracellulaire** (DEC) → hyponatrémie de déplétion\n"
                "  - **Hyperhydratation extracellulaire** (HEC) → IC, syndrome néphrotique, cirrhose\n"
                "  - **Secteur extracellulaire normal** → SIADH, potomanie, tea and toast"
            )),
            FicheRow(concept="★ ◆ SIADH", detail_md=(
                "- Sécrétion inappropriée d'ADH\n"
                "- Hyponatrémie avec secteur extracellulaire cliniquement **normal**\n"
                "- Urines **concentrées** (osmolalité urinaire inadaptée)\n"
                "- Étiologies : néoplasies (pulmonaires ++), pathologies neurologiques, médicaments, "
                "pathologies pulmonaires"
            )),
            FicheRow(concept="◆ Hypernatrémie", detail_md=(
                "- Na > **145 mmol/L**\n"
                "- Trouble ionique **plus rare** : si accès libre à l'eau → pas d'hypernatrémie\n"
                "- Contexte : personnes âgées, patients non autonomes, nourrissons"
            )),
        ]),
        SousPartie(lettre="B", titre="Dysnatrémies : traitements", rows=[
            FicheRow(concept="Traitement hyponatrémie", detail_md=(
                "| Cause | Traitement |\n"
                "|-------|------------|\n"
                "| Apport d'eau excessif (potomanie, tea and toast) | **Diminuer l'eau** + augmenter apports en osmoles |\n"
                "| Hyponatrémie de déplétion (DEC) | **Rétablir la volémie** (NaCl) |\n"
                "| HEC (IC, SN, cirrhose) | **Déplétion** + traitement de la cause + restriction hydrique |\n"
                "| SIADH | **Restriction hydrique** + traitement de la cause |\n"
            )),
            FicheRow(concept="Traitement hypernatrémie", detail_md=(
                "- Apport d'**eau** PO ou perfusion de **glucosé**\n"
                "- Traitement de la cause\n"
                "- Si déshydratation globale : NaCl + glucosé"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Correction de la natrémie toujours **progressive** : risque de myélinolyse centropontine "
                "si correction trop rapide d'une hyponatrémie chronique"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Acidose métabolique", rows=[
            FicheRow(concept="Diagnostic", detail_md=(
                "- pH < 7,38 avec **HCO3- diminués** (trouble primaire métabolique)\n"
                "- Compensation respiratoire attendue : hyperventilation (diminution PaCO2)"
            )),
            FicheRow(concept="Trou anionique plasmatique", detail_md=(
                "- **TA = Na + K - Cl - HCO3-**\n"
                "- Première étape diagnostique devant une acidose métabolique\n"
                "- Si TA > **20 mmol/L** (augmenté) = présence d'un **anion indosé** :\n"
                "  - **Lactate** (acidose lactique)\n"
                "  - **Corps cétoniques** (acidocétose diabétique)\n"
                "  - **Insuffisance rénale sévère** (accumulation d'acides organiques)\n"
                "- Si TA **normal** → **diarrhées** ou **tubulopathies** (perte de HCO3-)"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant une acidose métabolique, le **trou anionique** est le premier réflexe diagnostique\n"
                "- TA augmenté = accumulation d'acide ; TA normal = perte de bicarbonates"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Dyskaliémies : hypokaliémie", rows=[
            FicheRow(concept="Démarche diagnostique", detail_md=(
                "- K < **3,5 mmol/L**\n"
                "- Étape 1 : éliminer une **redistribution** (transfert intracellulaire) : alcalose, insuline, catécholamines\n"
                "- Étape 2 : **kaliurèse** :\n"
                "  - Kaliurèse **basse** (adaptée) → pertes **extra-rénales** : diarrhées, vomissements, laxatifs\n"
                "  - Kaliurèse **élevée** (inadaptée) → pertes **rénales** : diurétiques, hyperaldostéronisme"
            )),
            FicheRow(concept="◆ HTA + Hypokaliémie", detail_md=(
                "- Kaliurèse inadaptée → hyperactivation du canal **ENaC** :\n"
                "- **Hyperaldostéronisme primaire** (aldostérone haute / rénine basse) :\n"
                "  - Adénome surrénalien (Conn)\n"
                "  - Hyperplasie bilatérale des surrénales\n"
                "- **Hyperaldostéronisme secondaire** (aldostérone haute / rénine haute) :\n"
                "  - Sténose des artères rénales, HTA maligne, tumeurs à rénine\n"
                "- **Pseudo-hyperaldostéronisme** (aldostérone basse) :\n"
                "  - Cushing, acide glycyrrhizique, syndrome de Liddle"
            )),
            FicheRow(concept="◆ Symptomatologie", detail_md=(
                "- Hypokaliémie = **hyperexcitabilité** myocardique\n"
                "- Peu symptomatique : crampes, myalgies, constipation\n"
                "- **Signes ECG** +++ (troubles du rythme) :\n"
                "  - Fibrillation atriale\n"
                "  - **Torsade de pointe**\n"
                "  - Allongement PR\n"
                "  - Sous-décalage du ST\n"
                "  - Inversion onde T\n"
                "  - Apparition **onde U**"
            )),
        ]),
        SousPartie(lettre="E", titre="Dyskaliémies : hyperkaliémie", rows=[
            FicheRow(concept="Symptomatologie", detail_md=(
                "- Hyperkaliémie = **hypoexcitabilité** myocardique\n"
                "- Symptomatique uniquement si kaliémie **très élevée** → trompeur ++\n"
                "- Faiblesse musculaire généralisée, asthénie, hypotension\n"
                "- **Signes ECG** : « étirement de l'ECG »\n"
                "  - Ondes T **amples, pointues et symétriques**\n"
                "  - BAV 1 à 3, BSA, diminution puis disparition de l'onde P\n"
                "  - **Élargissement des QRS**\n"
                "  - Bradycardie à QRS large → **arrêt cardiorespiratoire**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ L'hyperkaliémie est **trompeuse** cliniquement : peu de symptômes jusqu'à la kaliémie très élevée\n"
                "- Toujours réaliser un **ECG** devant toute hyperkaliémie"
            ), kind="piege"),
            FicheRow(concept="◆ Traitement d'urgence", detail_md=(
                "- **Si signes ECG** → monitoring cardiaque :\n"
                "- **Gluconate de calcium 10%** : 1-2 ampoules (10 mL) → stabilise la membrane myocardique\n"
                "  - ⚠ **Ne diminue PAS la kaliémie** +++\n"
                "  - CI si intoxication digitalique (→ chlorure de magnésium)\n"
                "- **Insuline-Glucose** : 10-15 UI insuline rapide dans 500 mL G10% en 30 min\n"
                "- **Aérosols de salbutamol** : 20 mg sur 10 min (en même temps que insuline-G10)"
            )),
            FicheRow(concept="◆ Traitements selon contexte", detail_md=(
                "- **Kayexalate** PO : action plus lente\n"
                "- Si acidose métabolique à TA normal sans surcharge pulmonaire : **bicarbonate de sodium**\n"
                "- Si surcharge hydrosodée : **diurétique**\n"
                "- Si IR sévère oligurique/anurique sans cause rapidement résolutive : **hémodialyse en urgence**\n"
                "- Dans **tous les cas** : arrêt des traitements favorisant l'hyperkaliémie"
            )),
        ]),
        SousPartie(lettre="F", titre="Dyscalcémies", rows=[
            FicheRow(concept="◆ Hypercalcémie — Clinique", detail_md=(
                "- **Polyurie** → déshydratation hydrosodée +/- IRA fonctionnelle\n"
                "- Asthénie\n"
                "- Troubles digestifs : constipation, nausées/vomissements\n"
                "- Troubles neurologiques : confusion, ralentissement\n"
                "- **Lithiases urinaires**"
            )),
            FicheRow(concept="◆ Hypercalcémie — ECG", detail_md=(
                "- Mnémo : « **Ta raquette plate perd son rythme** »\n"
                "  - **Ta**chycardie\n"
                "  - **Ra**ccourcissement du QT\n"
                "  - Ondes T **plates**\n"
                "  - Allongement **PR**\n"
                "  - Trouble du **rythme**"
            ), kind="mnemo"),
            FicheRow(concept="Hypercalcémie — Étiologies", detail_md=(
                "- 2 grandes causes représentent > 90% :\n"
                "  - **Hyperparathyroïdie primaire** : PTH élevée, contexte ambulatoire\n"
                "  - **Hypercalcémie paranéoplasique** : PTH basse, contexte néoplasique\n"
                "- Traitement : cause + **réhydratation** + discuter **bisphosphonates**"
            )),
            FicheRow(concept="◆ Hypocalcémie — Définition et clinique", detail_md=(
                "- Ca2+ totale < **2,20 mmol/L** ou Ca2+ ionisée < **1,15 mmol/L**\n"
                "- Manifestations **neuromusculaires** : paresthésies (pourtour des lèvres, doigts), spasmes\n"
                "- Signe de **Chvostek** : contraction faciale par percussion du nerf facial\n"
                "- Signe de **Trousseau** : main d'accoucheur par compression de l'artère brachiale\n"
                "- **ECG** : allongement QT ++ → BAV → FV"
            )),
            FicheRow(concept="◆ Hypocalcémie — Étiologies", detail_md=(
                "- PTH **normale ou basse** (inadaptée) → **hypoparathyroïdie**\n"
                "- PTH **élevée** → **insuffisance rénale chronique** / **carence en vitamine D**\n"
                "- Causes génétiques rares"
            )),
        ]),
    ])

    # ── PARTIE III : INSUFFISANCE RÉNALE AIGUË ──
    partie_iii = Partie(numero="III", titre="Insuffisance rénale aiguë", sous_parties=[
        SousPartie(lettre="A", titre="Démarche diagnostique et classification", rows=[
            FicheRow(concept="Démarche diagnostique", detail_md=(
                "- Devant toute insuffisance rénale → distinguer **aiguë** vs **chronique**\n"
                "- Arguments pour le caractère aigu : créatinine antérieure normale, reins de taille normale, "
                "absence d'anémie ni d'hypocalcémie\n"
                "- 3 grandes causes d'IRA :\n"
                "  - **Fonctionnelle** (pré-rénale)\n"
                "  - **Obstructive** (post-rénale)\n"
                "  - **Organique** (rénale intrinsèque)"
            )),
            FicheRow(concept="◆ Classification KDIGO 2012", detail_md=(
                "| Stade | Créatinine | Diurèse |\n"
                "|-------|-----------|--------|\n"
                "| 1 | x 1,5-1,9 ou augmentation ≥ 26,5 µmol/L | < 0,5 mL/kg/h pendant 6-12h |\n"
                "| 2 | x 2-2,9 | < 0,5 mL/kg/h pendant ≥ 12h |\n"
                "| 3 | x ≥ 3 ou créat ≥ 354 µmol/L ou dialyse | < 0,3 mL/kg/h ≥ 24h ou anurie ≥ 12h |\n"
            )),
            FicheRow(concept="◆ Complications engageant le pronostic vital", detail_md=(
                "- **Hyperkaliémie menaçante** (signes ECG)\n"
                "- **OAP** oxygéno-dépendant\n"
                "- **Acidose métabolique** sévère\n"
                "- **Encéphalopathie urémique** (hyper-urémie symptomatique)"
            )),
            FicheRow(concept="", detail_md=(
                "- Ces 4 complications sont des **indications d'hémodialyse en urgence** si non rapidement résolutives"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="IRA fonctionnelle", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- **Baisse de la perfusion rénale** sans lésion organique du parenchyme\n"
                "- Mécanisme : diminution du débit sanguin rénal → diminution de la pression de filtration"
            )),
            FicheRow(concept="◆ Clinique", detail_md=(
                "- Déshydratation : **soif**, pli cutané\n"
                "- **Hypotension artérielle**, hypotension orthostatique, tachycardie\n"
                "- Contexte ++ : troubles digestifs (vomissements, diarrhées), sueurs, brûlures, sepsis"
            )),
            FicheRow(concept="Biologie", detail_md=(
                "| Paramètre | IRA fonctionnelle |\n"
                "|-----------|------------------|\n"
                "| Natriurèse | < **20 mmol/L** |\n"
                "| Na/K urinaire | < **1** |\n"
                "| FE urée | < **30%** |\n"
                "| Urée/créatinine | Urée x 10 > créatinine |\n"
                "| Urines | **Concentrées** |\n"
            )),
            FicheRow(concept="◆ Étiologies", detail_md=(
                "- **Déshydratation extracellulaire** : hypovolémie vraie\n"
                "- **Iatrogénie** : AINS, IEC/ARAII, diurétiques\n"
                "- **Hypovolémie efficace** (HEC avec hypovolémie relative) : insuffisance cardiaque, "
                "syndrome néphrotique, syndrome hépato-rénal"
            )),
            FicheRow(concept="", detail_md=(
                "- Le **meilleur argument** diagnostique = récupération rénale après rétablissement de la volémie\n"
                "- Risque si persistance : évolution vers **NTA** (nécrose tubulaire aiguë) = IRA organique"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="IRA obstructive", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- Obstruction mécanique à l'évacuation des urines avec retentissement sur la fonction rénale\n"
                "- **L'imagerie fait le diagnostic** +++ (échographie rénale : dilatation des cavités pyélocalicielles)"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- Contexte +++ : homme avec symptômes d'obstruction du bas appareil, ATCD de radiothérapie\n"
                "- Douleurs abdominales ou pelviennes\n"
                "- **Miction par regorgement** possible (fuites urinaires)"
            )),
            FicheRow(concept="◆ Étiologies", detail_md=(
                "| Niveau | Étiologies principales |\n"
                "|--------|----------------------|\n"
                "| Sous-vésical | **HBP** +++, cancer de prostate |\n"
                "| Vésical | Vessie de lutte, tumeur vésicale, vessie radique (post-radiothérapie col utérus ++) |\n"
                "| Urétéral | Fibrose rétropéritonéale, post-radiothérapie, lithiase bilatérale |\n"
            )),
        ]),
        SousPartie(lettre="D", titre="IRA organique", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- Atteinte de la **structure** du rein : glomérules et/ou vaisseaux et/ou tubule et/ou interstitium"
            )),
            FicheRow(concept="◆ Orientation diagnostique", detail_md=(
                "| Compartiment | Protéinurie | Hématurie | Contexte |\n"
                "|-------------|------------|----------|----------|\n"
                "| **Vasculaire** | < 1 g/g | Possible | Terrain vasculaire, HTA |\n"
                "| **Tubulo-interstitiel** | Variable, < 50% albumine | Non | Toxique/médicamenteux/infectieux |\n"
                "| **Glomérulaire** | > 1 g/g, > 50% albumine | Possible (prolifération) | Variable |\n"
            )),
            FicheRow(concept="◆ Hématurie", detail_md=(
                "- Hématies urinaires > **10/mm3** (ou 10 000/mL)\n"
                "- Différencier l'origine **urologique** (caillots, GR non déformés) et **rénale** (cylindres hématiques, GR déformés)"
            )),
        ]),
        SousPartie(lettre="E", titre="IRA du greffé rénal", rows=[
            FicheRow(concept="◆ Étiologies spécifiques", detail_md=(
                "- Mêmes causes que le rein natif + causes spécifiques :\n"
                "  - **Surdosage en immunosuppresseurs** : typiquement surdosage en **tacrolimus** lors de diarrhées\n"
                "  - **Pyélonéphrite** du greffon\n"
                "  - Causes **vasculaires** : thrombose artère/veine rénale → toujours **échographie-Doppler du greffon**\n"
                "  - **Néphrite à BK virus** (infection opportuniste)\n"
                "  - **Rejet** +++ : cellulaire ou humoral"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant une IRA chez un greffé rénal : toujours réaliser une **échographie-Doppler du greffon** "
                "et doser les **taux résiduels d'immunosuppresseurs**"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE IV : MALADIE RÉNALE CHRONIQUE ──
    partie_iv = Partie(numero="IV", titre="Maladie rénale chronique", sous_parties=[
        SousPartie(lettre="A", titre="Classification et étiologies", rows=[
            FicheRow(concept="★ Classification KDIGO", detail_md=(
                "| Stade | DFG (mL/min/1,73m2) | Description |\n"
                "|-------|-------------------|------------|\n"
                "| G1 | ≥ 90 | Normal ou augmenté |\n"
                "| G2 | 60-89 | Légèrement diminué |\n"
                "| G3a | 45-59 | Diminution légère à modérée |\n"
                "| G3b | 30-44 | Diminution modérée à sévère |\n"
                "| G4 | 15-29 | Diminution sévère |\n"
                "| G5 | < 15 | **Insuffisance rénale terminale** |\n"
            )),
            FicheRow(concept="◆ Étiologies principales", detail_md=(
                "- **Néphropathie diabétique** : 2e cause d'IRCT en France\n"
                "- **Néphropathies vasculaires** (néphroangiosclérose)\n"
                "- **Glomérulonéphrites chroniques**\n"
                "- **Polykystose rénale** autosomique dominante\n"
                "- Néphropathies interstitielles chroniques"
            )),
        ]),
        SousPartie(lettre="B", titre="Complications de la MRC", rows=[
            FicheRow(concept="Anomalies biologiques", detail_md=(
                "- **Anémie** : normochrome, normocytaire, arégénérative (carence en EPO + malabsorption du fer)\n"
                "- **Troubles phosphocalciques** : hypocalcémie, hyperparathyroïdie secondaire (PTH augmentée), "
                "hyperphosphatémie, déficit en vitamine D active\n"
                "- **Acidose métabolique**\n"
                "- Hyperuricémie\n"
                "- Dyslipidémie\n"
                "- Troubles ioniques tardifs : hyponatrémie, **hyperkaliémie**"
            )),
            FicheRow(concept="◆ Complications cardiovasculaires", detail_md=(
                "- **Maladie athéromateuse** : coronaropathie, AOMI, athérome carotidien, calcifications vasculaires\n"
                "- **HTA**\n"
                "- 1re cause de mortalité dans la MRC"
            )),
            FicheRow(concept="◆ Autres complications", detail_md=(
                "- **Dénutrition** protéino-énergétique\n"
                "- Anomalies cliniques tardives : asthénie, surcharge hydrosodée, urémie symptomatique (IRC terminale)\n"
                "- Anomalies morphologiques : diminution de la taille des reins, dédifférenciation cortico-sinusale"
            )),
            FicheRow(concept="", detail_md=(
                "- Certaines pathologies conservent des reins de **taille normale ou augmentée** : "
                "**diabète**, **amylose**, **polykystose**"
            ), kind="piege"),
            FicheRow(concept="◆ Hypocalcémie de l'IRC", detail_md=(
                "- Mécanisme : réduction néphronique → défaut d'hydroxylation de la vitamine D active → "
                "**hyperparathyroïdie secondaire** → augmentation FGF23 → hyperphosphatémie → "
                "**déminéralisation osseuse**"
            )),
            FicheRow(concept="Anémie de l'IRC", detail_md=(
                "- Bilan : réticulocytes, bilan d'hémolyse, bilan martial (ferritinémie, CST), "
                "vitamines B9/B12, EPS, CRP\n"
                "- Traitement :\n"
                "  - **Supplémentation martiale** (PO ou IV si inefficace) : objectif ferritinémie > **100 ng/mL** et/ou CST > **20%**\n"
                "  - Corriger toutes les carences **avant** EPO\n"
                "  - **EPO** si Hb < **10 g/dL**\n"
                "  - Objectif : Hb ne doit pas être volontairement > **12 g/dL** sous EPO"
            )),
        ]),
        SousPartie(lettre="C", titre="Néphroprotection", rows=[
            FicheRow(concept="◆ Mesures de néphroprotection", detail_md=(
                "- **Éviction des néphrotoxiques** : CI aux AINS, éviter les produits de contraste iodés\n"
                "- Éviter les épisodes de **déshydratation**\n"
                "- **Contrôle de la protéinurie** : objectif < **0,5 g/g** → IEC ou ARAII dose maximale tolérée\n"
                "- **Gliflozines** (iSGLT2) : si DFG ≥ 20 mL/min et albuminurie > 0,2 g/g, en association avec IEC/ARAII\n"
                "- **Contrôle de la TA** : objectif < **130/80 mmHg** (voire PAS < 120 mmHg, recommandations KDIGO)\n"
                "- **Contrôle du diabète** : privilégier gliflozines + analogues du GLP-1\n"
                "- **Dyslipidémie** : atorvastatine, simvastatine, rosuvastatine"
            )),
            FicheRow(concept="◆ Mesures hygiéno-diététiques", detail_md=(
                "- Lutte contre le **surpoids** (IMC < 25)\n"
                "- Exercice physique : ≥ **150 min/semaine** d'activité modérée\n"
                "- **Arrêt du tabac**\n"
                "- Apports de sel contrôlés\n"
                "- Apports protéiques **modérés** +++"
            )),
            FicheRow(concept="", detail_md=(
                "- Les objectifs sont de **ralentir la progression** vers l'IRCT et de **limiter les conséquences cardiovasculaires**\n"
                "- Les IEC/ARAII sont le pilier de la néphroprotection grâce à leur effet **antiprotéinurique**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Suppléance : greffe et dialyse", rows=[
            FicheRow(concept="◆ Greffe rénale", detail_md=(
                "- Meilleure **survie** et **qualité de vie** parmi les modalités de suppléance\n"
                "- Nécessite un traitement **immunosuppresseur à vie** (contraignant, effets secondaires)\n"
                "- Greffe préemptive rarement possible"
            )),
            FicheRow(concept="◆ Types de greffons", detail_md=(
                "- **Donneur décédé** : mort encéphalique ou Maastricht\n"
                "- **Donneur vivant** : toute personne avec lien étroit et stable > **2 ans**, "
                "dont le bilan médical permet le prélèvement d'un rein compatible\n"
                "- L'accès à la greffe dépend du bilan pré-greffe et de l'**immunisation** du patient"
            )),
            FicheRow(concept="Traitements majeurs en néphrologie", detail_md=(
                "- **IEC/ARAII** : antihypertenseur de choix en IRC, effet **antiprotéinurique** majeur "
                "(la protéinurie est toxique pour le rein)\n"
                "- **Inhibiteurs du SGLT2** (gliflozines) : révolution thérapeutique\n"
                "  - Indications : IC, diabète si DFG > 60 mL/min, IRC si albuminurie persistante malgré IEC/ARAII "
                "à dose max et DFG > 20 mL/min\n"
                "  - ⚠ Effets indésirables : infections urinaires, **acidocétose diabétique euglycémique**"
            )),
        ]),
    ])

    # ── PARTIE V : NÉPHROPATHIES GLOMÉRULAIRES ──
    partie_v = Partie(numero="V", titre="Néphropathies glomérulaires", sous_parties=[
        SousPartie(lettre="A", titre="Syndrome néphrotique", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- **Protéinurie** composée d'albumine ≥ **3 g/g** **ET**\n"
                "- **Albuminémie** < **30 g/L**"
            )),
            FicheRow(concept="◆ Syndrome néphrotique pur vs impur", detail_md=(
                "| Critère | Pur | Impur |\n"
                "|---------|-----|-------|\n"
                "| Insuffisance rénale | **Absente** | Présente |\n"
                "| Hématurie | **Absente** | Présente |\n"
                "| HTA | **Absente** | Présente |\n"
            )),
            FicheRow(concept="◆ Clinique et complications", detail_md=(
                "- Tableau de **surcharge hydrosodée** ++ (oedèmes)\n"
                "- **IRA** par 3 mécanismes :\n"
                "  - IRA fonctionnelle (hypovolémie relative)\n"
                "  - IRA organique par NTA (si persistance de l'IRA fonctionnelle)\n"
                "  - **Thrombose des veines rénales**\n"
                "- **Thromboses veineuses profondes** et artérielles (état pro-thrombotique)\n"
                "- **Infections à germes encapsulés** (hypogammaglobulinémie) : **pneumocoque** ++, Haemophilus\n"
                "- Dénutrition protéique, dyslipidémie\n"
                "- Modification du métabolisme des médicaments à fixation protéique (hypoalbuminémie)"
            )),
            FicheRow(concept="", detail_md=(
                "- Syndrome néphrotique = état **pro-thrombotique** : anticoagulation efficace si albuminémie < **20 g/L**\n"
                "- Risque infectieux majoré par l'**hypogammaglobulinémie** (perte urinaire d'Ig)"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Traitement symptomatique", detail_md=(
                "- **Restriction sodée** : NaCl < 4 g/24h (idéalement < 2 g/24h)\n"
                "- **Furosémide** en 1re intention (parfois IV si oedème digestif)\n"
                "  - Si résistance : association thiazidique ou **amiloride** +++ (action sur ENaC + non hypokaliémiant)\n"
                "- Anticoagulation efficace si albuminémie < **20 g/L**\n"
                "- IEC/ARAII si SN persistant\n"
                "- Traitement de la dyslipidémie si persistante"
            )),
            FicheRow(concept="◆ Traitement curatif", detail_md=(
                "- Dépend de l'étiologie (biopsie rénale ++) :\n"
                "  - Forme **secondaire** : traitement de la cause\n"
                "  - **GEM** : selon risque de progression → symptomatique à immunosuppresseur\n"
                "  - **LGM** : **corticothérapie** en 1re intention\n"
                "  - **HSF** : **corticothérapie** en 1re intention"
            )),
            FicheRow(concept="◆ Étiologies des oedèmes généralisés", detail_md=(
                "- Insuffisance **cardiaque**\n"
                "- Insuffisance **hépato-cellulaire**\n"
                "- **Syndrome néphrotique**\n"
                "- Hypoalbuminémie profonde\n"
                "- Troubles de la perméabilité capillaire"
            )),
        ]),
        SousPartie(lettre="B", titre="Glomérulonéphrite rapidement progressive", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- **IRA organique rapidement progressive** associée à une hématurie et protéinurie glomérulaire\n"
                "- Urgence diagnostique et thérapeutique"
            )),
            FicheRow(concept="◆ Maladie de Goodpasture", detail_md=(
                "- Histologie : prolifération extracapillaire avec dépôts **linéaires d'IgG** le long des membranes basales glomérulaires\n"
                "- Clinique : IRA sévère rapidement **anurique** +/- **hémorragie intra-alvéolaire** (syndrome pneumo-rénal)\n"
                "- Typiquement : homme jeune ou personne ~60 ans"
            )),
            FicheRow(concept="◆ Vascularites à ANCA", detail_md=(
                "- Histologie : prolifération extracapillaire avec **absence de dépôts** en IF (pauci-immune)\n"
                "- Associées à des **ANCA** sériques\n"
                "- IRA +/- signes de vascularite systémique"
            )),
            FicheRow(concept="◆ Trois vascularites à ANCA", detail_md=(
                "| Pathologie | Caractéristiques |\n"
                "|-----------|------------------|\n"
                "| **Granulomatose avec polyangéite** (Wegener) | Atteinte ORL, granulome rétro-orbitaire et pulmonaire |\n"
                "| **Granulomatose éosinophilique avec polyangéite** (Churg-Strauss) | Asthme + hyperéosinophilie |\n"
                "| **Polyangéite microscopique** | Atteinte rénale souvent isolée |\n"
            )),
        ]),
        SousPartie(lettre="C", titre="Néphropathies glomérulaires spécifiques", rows=[
            FicheRow(concept="◆ Lésions glomérulaires minimes (LGM)", detail_md=(
                "- Histologie : microscopie optique et IF **normales**\n"
                "- Clinique : SN **pur** +++ de début **brutal**\n"
                "- Cause la plus fréquente de SN chez l'**enfant**\n"
                "- Étiologies : primitive (probable facteur circulant), secondaires (AINS, interféron, lymphome)\n"
                "- Traitement : **corticothérapie** ++"
            )),
            FicheRow(concept="◆ Glomérulonéphrite extramembraneuse (GEM)", detail_md=(
                "- Histologie : dépôts extramembraneux **granuleux d'IgG** en IF\n"
                "- Clinique : SN **impur** ++\n"
                "- Évolution : 1/3 rémission spontanée, 1/3 séquelles rénales, 1/3 IRCT\n"
                "- Étiologies : primitive (anticorps anti-PLA2R), secondaires (**cancers solides** : poumon +++, "
                "colon, mélanome ; lupus ; AINS ; infections)\n"
                "- Traitement : néphroprotection ++ ; si grave/persistant : **rituximab**"
            )),
            FicheRow(concept="◆ Néphropathie à IgA (Berger)", detail_md=(
                "- **Glomérulopathie primitive la plus fréquente**\n"
                "- Histologie : dépôts d'**IgA** en IF +/- prolifération\n"
                "- Présentation variable : hématurie isolée, IRC glomérulaire, GNRP, "
                "**hématurie macroscopique récidivante** (typiquement post-infection ORL)\n"
                "- Étiologies : primitive (défaut de glycosylation des IgA), "
                "secondaires (cirrhose, MICI, spondylarthropathies)\n"
                "- **Purpura rhumatoïde** = vascularite à IgA\n"
                "- Traitement : néphroprotection ++, parfois corticoïdes"
            )),
            FicheRow(concept="◆ Amylose rénale", detail_md=(
                "- Histologie : organisation en feuillet bêta-plissé, coloration **rouge Congo**\n"
                "- Clinique : **SN** +++, IR, **hypotension artérielle** ou orthostatique\n"
                "- Étiologies : amylose **AA** (inflammation chronique), amylose **AL** (gammapathie monoclonale)\n"
                "- Traitement : néphroprotection + traitement de la cause"
            )),
        ]),
    ])

    # ── PARTIE VI : NÉPHROPATHIES SPÉCIFIQUES ET IATROGÉNIE ──
    partie_vi = Partie(numero="VI", titre="Néphropathies spécifiques et iatrogénie", sous_parties=[
        SousPartie(lettre="A", titre="Néphropathie diabétique", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- **2e cause d'IRCT** en France\n"
                "- Présentation typique : diabète **déséquilibré**, déjà compliqué (**rétinopathie diabétique** ++), "
                "évoluant depuis plusieurs années\n"
                "- Classiquement **pas d'hématurie** significative\n"
                "- Protéinurie progressive : d'abord **microalbuminurie**, puis protéinurie franche et dégradation du DFG"
            )),
            FicheRow(concept="◆ Prise en charge", detail_md=(
                "- **Contrôle du diabète** +++\n"
                "- Néphroprotection en privilégiant les traitements à **double action** rein + diabète :\n"
                "  - **Gliflozines** (Forxiga/dapagliflozine)\n"
                "  - **Analogues du GLP-1**\n"
                "- La biopsie rénale se discute selon la présentation (atypie = indication de biopsie)"
            )),
        ]),
        SousPartie(lettre="B", titre="Néphropathie lupique", rows=[
            FicheRow(concept="◆ Indication de biopsie", detail_md=(
                "- Tout patient avec lupus et **protéinurie ≥ 0,5 g/g** ou IR → **biopsie rénale**"
            )),
            FicheRow(concept="◆ Traitement selon la classe", detail_md=(
                "| Classe ISN/RPS | Traitement |\n"
                "|---------------|------------|\n"
                "| Classe III ou IV (proliférative) | **Corticoïdes** + **Endoxan** ou **MMF** |\n"
                "| Classe V (membraneuse) | **Rituximab** |\n\n"
                "- **Plaquenil** (hydroxychloroquine) en l'absence de CI : traitement de fond systématique du lupus"
            )),
        ]),
        SousPartie(lettre="C", titre="Polykystose rénale autosomique dominante", rows=[
            FicheRow(concept="◆ Généralités", detail_md=(
                "- Maladie génétique **autosomique dominante**\n"
                "- Mutation de **PKD1** (polycystine 1) ou **PKD2** (polycystine 2)\n"
                "- Polykystose **hépato-rénale** avec IR progressive → IRCT à âge variable (plus précoce si PKD1)\n"
                "- Profil **tubulo-interstitiel**"
            )),
            FicheRow(concept="◆ Pathologies associées", detail_md=(
                "- **Anévrisme cérébral** +++ :\n"
                "  - Signes évocateurs : céphalées, mort subite familiale\n"
                "  - Examen de référence : **Angio-IRM cérébrale avec TOF** (sans injection de PDC)\n"
                "- Insuffisance **mitrale**\n"
                "- **Kystes hépatiques** : rarement problématiques"
            )),
            FicheRow(concept="◆ Complications aiguës rénales", detail_md=(
                "- Pyélonéphrite aiguë\n"
                "- **Infection de kyste**\n"
                "- Rupture hémorragique / hémorragie intra-kystique\n"
                "- Colique néphrétique"
            )),
            FicheRow(concept="◆ Prise en charge", detail_md=(
                "- Néphroprotection comme les autres néphropathies (objectifs TA parfois plus bas)\n"
                "- **Hyperdiurèse**\n"
                "- **Tolvaptan** : réservé aux patients DFG > 25 mL/min et **progresseurs rapides**\n"
                "- Pronostic : score **PROKD**"
            )),
        ]),
        SousPartie(lettre="D", titre="Atteinte rénale du myélome", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Maladie hématologique : prolifération **plasmocytaire**\n"
                "- Multiples mécanismes d'atteinte rénale"
            )),
            FicheRow(concept="Trois atteintes rénales majeures", detail_md=(
                "| Atteinte | Mécanisme | Clinique |\n"
                "|----------|-----------|----------|\n"
                "| IRA fonctionnelle | Secondaire à l'**hypercalcémie** | IRA pré-rénale |\n"
                "| Néphropathie à cylindres myélomateux | Précipitation intratubulaire de chaînes légères | "
                "IRA nue, **BU négative** |\n"
                "| Amylose AL | Dépôts glomérulaires de chaînes légères | **SN** +++ (protéinurie d'albumine) |\n"
            )),
            FicheRow(concept="◆ Autres atteintes", detail_md=(
                "- **Syndrome de Fanconi** (réabsorption tubulaire de chaînes légères)\n"
                "- Dépôts d'Ig monoclonale (maladie de Randall)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La néphropathie à cylindres myélomateux donne une protéinurie **négative à la BU** "
                "(car composée de chaînes légères, non détectées par la BU qui ne détecte que l'albumine)\n"
                "- Facteurs favorisants : déshydratation, diurétiques, injection de produit de contraste"
            ), kind="piege"),
        ]),
        SousPartie(lettre="E", titre="Iatrogénie en néphrologie", rows=[
            FicheRow(concept="AINS", detail_md=(
                "- En cas de déshydratation : favorisent l'**IRA fonctionnelle**\n"
                "- Atteinte spécifique possible : néphropathie à **lésions glomérulaires minimes**\n"
                "- **Contre-indiqués** en cas de MRC et en association avec IEC/ARAII"
            )),
            FicheRow(concept="IEC/ARAII", detail_md=(
                "- Traitement **majeur** de la MRC (néphroprotection)\n"
                "- ⚠ À **arrêter** en cas de déshydratation ou troubles digestifs importants (vomissements, diarrhées)\n"
                "- Sinon risque d'**IRA fonctionnelle** ++"
            )),
            FicheRow(concept="Metformine", detail_md=(
                "- Traitement de **1re intention** du diabète\n"
                "- À **arrêter** en cas de troubles digestifs ou de déshydratation ++\n"
                "- Risque d'**acidose lactique** à la metformine si IRC + troubles digestifs"
            )),
            FicheRow(concept="Diurétiques", detail_md=(
                "- Attention à la **déshydratation** : si majoration des doses ou déshydratation associée"
            )),
            FicheRow(concept="◆ Maladie des emboles de cholestérol", detail_md=(
                "- Après un **geste vasculaire artériel** (typiquement coronarographie)\n"
                "- Biologie : hyperéosinophilie possible, **hypocomplémentémie** (C3 bas)\n"
                "- HTA fréquente\n"
                "- Clinique : **orteil bleu**, emboles périphériques, **livedo reticularis**, purpura, ulcérations nécrotiques\n"
                "- **Fond d'oeil** : emboles visibles\n"
                "- Traitement par corticoïdes à discuter"
            )),
            FicheRow(concept="", detail_md=(
                "- Règle d'or : en cas de **déshydratation** ou **troubles digestifs**, arrêter temporairement "
                "IEC/ARAII, metformine et diurétiques pour prévenir l'IRA"
            ), kind="a_retenir"),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="IRA fonctionnelle vs organique", markdown=(
            "| Paramètre | IRA fonctionnelle | IRA organique (NTA) |\n"
            "|-----------|------------------|--------------------|\n"
            "| Natriurèse | < 20 mmol/L | > 40 mmol/L |\n"
            "| Na/K urinaire | < 1 | > 1 |\n"
            "| FE urée | < 30% | > 30% |\n"
            "| Urines | Concentrées | Diluées |\n"
            "| Réponse au remplissage | Oui | Non |\n"
        )),
        TableauSynthese(titre="Hypokaliémie vs Hyperkaliémie — Signes ECG", markdown=(
            "| | Hypokaliémie | Hyperkaliémie |\n"
            "|--|-------------|---------------|\n"
            "| Excitabilité | Hyperexcitabilité | Hypoexcitabilité |\n"
            "| Onde T | Aplatie/inversée | Ample, pointue, symétrique |\n"
            "| Onde U | Apparition | Absente |\n"
            "| QRS | Normal | Élargi |\n"
            "| PR | Allongé | Allongé (BAV) |\n"
            "| Risque majeur | Torsade de pointe | Bradycardie → ACR |\n"
        )),
        TableauSynthese(titre="Syndrome néphrotique — Pur vs Impur", markdown=(
            "| Critère | SN pur | SN impur |\n"
            "|---------|-------|----------|\n"
            "| Protéinurie | ≥ 3 g/g (albumine) | ≥ 3 g/g (albumine) |\n"
            "| Albuminémie | < 30 g/L | < 30 g/L |\n"
            "| IR | Absente | Présente |\n"
            "| Hématurie | Absente | Présente |\n"
            "| HTA | Absente | Présente |\n"
            "| Étiologies classiques | LGM (enfant) | GEM, NIgA |\n"
        )),
        TableauSynthese(titre="GNRP — Goodpasture vs Vascularites à ANCA", markdown=(
            "| | Goodpasture | Vascularites à ANCA |\n"
            "|--|------------|--------------------|\n"
            "| IF | Dépôts linéaires IgG | Pauci-immune (pas de dépôts) |\n"
            "| Sérologie | Anti-MBG | ANCA (PR3 ou MPO) |\n"
            "| Atteinte pulmonaire | Hémorragie intra-alvéolaire | Selon le type |\n"
            "| Terrain | Homme jeune ou ~60 ans | Variable |\n"
        )),
        TableauSynthese(titre="Traitements à risque néphrotoxique", markdown=(
            "| Médicament | Risque | Conduite |\n"
            "|-----------|--------|----------|\n"
            "| AINS | IRA fonctionnelle, LGM | CI si MRC, CI avec IEC/ARAII |\n"
            "| IEC/ARAII | IRA fonctionnelle si déshydratation | Arrêt temporaire si DEC |\n"
            "| Metformine | Acidose lactique si IRC + DEC | Arrêt temporaire si DEC |\n"
            "| Diurétiques | Déshydratation, dyskaliémie | Surveillance étroite |\n"
            "| PDC iodés | IRA, emboles de cholestérol | Hydratation préventive |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| DFG normal | **~120 mL/min** | 180 L/j d'urine primitive |\n"
        "| Osmolarité plasmatique | **~285 mOsm/kg** | Osm = Na x 2 + glycémie |\n"
        "| Hyponatrémie | Na < **135 mmol/L** | Hyperhydratation intracellulaire |\n"
        "| Hypernatrémie | Na > **145 mmol/L** | Déshydratation intracellulaire |\n"
        "| TA plasmatique augmenté | > **20 mmol/L** | Anion indosé (acidose métabolique) |\n"
        "| Hypocalcémie | Ca2+ < **2,20 mmol/L** | Ou Ca2+ ionisée < 1,15 |\n"
        "| SN — Protéinurie | ≥ **3 g/g** | Composée d'albumine |\n"
        "| SN — Albuminémie | < **30 g/L** | Définition du SN |\n"
        "| Anticoagulation SN | Albumine < **20 g/L** | Indication anticoagulation efficace |\n"
        "| Objectif protéinurie MRC | < **0,5 g/g** | Sous IEC/ARAII dose max |\n"
        "| Objectif TA en MRC | < **130/80 mmHg** | KDIGO (voire PAS < 120) |\n"
        "| Hb pour introduction EPO | < **10 g/dL** | Après correction des carences |\n"
        "| Hb max sous EPO | < **12 g/dL** | Ne pas dépasser volontairement |\n"
        "| IRA fonctionnelle — Na U | < **20 mmol/L** | Na/K < 1, FE urée < 30% |\n"
        "| Gliflozines — DFG seuil | ≥ **20 mL/min** | Avec albuminurie > 0,2 g/g |\n"
    ))

    points_cles = [
        "La natrémie reflète l'hydratation **intracellulaire**, la volémie reflète le stock de **Na+**",
        "Devant une acidose métabolique, calculer le **trou anionique** : augmenté (lactate, cétones, IR) vs normal (diarrhées, tubulopathies)",
        "L'hyperkaliémie est trompeuse cliniquement : toujours faire un **ECG** ; gluconate de calcium en urgence mais ne diminue **PAS** la kaliémie",
        "IRA fonctionnelle : natriurèse < 20, Na/K < 1, FE urée < 30% ; le meilleur argument = récupération après **remplissage**",
        "Les IEC/ARAII sont le pilier de la **néphroprotection** (effet antiprotéinurique) ; les gliflozines sont la révolution thérapeutique",
        "Le syndrome néphrotique (protéinurie ≥ 3 g/g + albumine < 30 g/L) expose aux **thromboses** et aux **infections à pneumocoque**",
        "La néphropathie à IgA est la **glomérulopathie primitive la plus fréquente** ; LGM est la 1re cause de SN chez l'enfant",
        "En cas de déshydratation : arrêter **IEC/ARAII, metformine et diurétiques** pour prévenir l'IRA",
    ]

    fiche_eclair_md = (
        "**Physiologie rénale** : DFG ~120 mL/min, 180 L/j d'urine primitive, réabsorption tubulaire > 99%. "
        "Fonctions : homéostasie ionique, volémie, EPO, vitamine D, rénine.\n\n"
        "**Dysnatrémies** : volémie = Na+, natrémie = hydratation intracellulaire. "
        "Hyponatrémie : évaluer le secteur extracellulaire (DEC/HEC/normal-SIADH). "
        "Correction toujours progressive.\n\n"
        "**Dyskaliémies** : hypoK = hyperexcitabilité (onde U, TdP) ; hyperK = hypoexcitabilité "
        "(ondes T amples, QRS large, ACR). Gluconate de Ca2+ NE diminue PAS la kaliémie.\n\n"
        "**IRA** : fonctionnelle (Na U < 20, remplissage) vs obstructive (écho) vs organique (biopsie). "
        "4 urgences vitales : hyperK, OAP, acidose sévère, encéphalopathie urémique.\n\n"
        "**MRC** : classification KDIGO G1-G5. Néphroprotection : IEC/ARAII (protéinurie < 0,5 g/g) + "
        "gliflozines + TA < 130/80. Anémie : fer puis EPO si Hb < 10.\n\n"
        "**Syndrome néphrotique** : protéinurie ≥ 3 g/g + albumine < 30. Pur (LGM) vs impur (GEM). "
        "Risques : thromboses, infections pneumocoque. Anticoagulation si albumine < 20.\n\n"
        "**GNRP** : Goodpasture (dépôts linéaires IgG, hémorragie alvéolaire) vs vascularites ANCA (pauci-immune).\n\n"
        "**Iatrogénie** : AINS CI si MRC, IEC/ARAII arrêt si DEC, metformine arrêt si DEC (acidose lactique)."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Néphrologie",
        annee="2025-2026",
        item="Items 265, 267, 268, 269, 261, 262, 263, 197, 258, 201, 330, 245, 190, 329",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        usage=UsageStats(),
    )


def main():
    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(exist_ok=True)

    fiche = build_nephrologie_fiche()

    docx_path = output_dir / "Medecine_generale_nephrologie_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Medecine_generale_nephrologie_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path}")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

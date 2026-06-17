"""Genere la fiche exhaustive de Reanimation a partir du texte source."""

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
        PlanPartie(numero="I", titre="Anomalies du bilan de l'eau et du sodium", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités"),
            PlanSousPartie(lettre="B", titre="Deshydratation extracellulaire (DEC)"),
            PlanSousPartie(lettre="C", titre="Hyperhydratation extracellulaire (HEC)"),
            PlanSousPartie(lettre="D", titre="Deshydratation intracellulaire (DIC)"),
            PlanSousPartie(lettre="E", titre="Hyperhydratation intracellulaire (HIC)"),
        ]),
        PlanPartie(numero="II", titre="Desordres de l'equilibre acide-base", sous_parties=[
            PlanSousPartie(lettre="A", titre="GDS arteriel et interpretation"),
            PlanSousPartie(lettre="B", titre="Acidoses metaboliques"),
            PlanSousPartie(lettre="C", titre="Alcaloses metaboliques et respiratoires"),
        ]),
        PlanPartie(numero="III", titre="Detresse respiratoire aigue et SDRA", sous_parties=[
            PlanSousPartie(lettre="A", titre="Diagnostic positif de la detresse respiratoire aigue"),
            PlanSousPartie(lettre="B", titre="Prise en charge et etiologies"),
            PlanSousPartie(lettre="C", titre="SDRA"),
        ]),
        PlanPartie(numero="IV", titre="Etats de choc", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et diagnostic positif"),
            PlanSousPartie(lettre="B", titre="Principes generaux de prise en charge"),
            PlanSousPartie(lettre="C", titre="Choc cardiogenique et hypovolemique"),
            PlanSousPartie(lettre="D", titre="Choc septique et obstructif"),
        ]),
        PlanPartie(numero="V", titre="Hypercalcemie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Definition et tableau clinique"),
            PlanSousPartie(lettre="B", titre="Étiologies"),
            PlanSousPartie(lettre="C", titre="Prise en charge symptomatique"),
        ]),
        PlanPartie(numero="VI", titre="Oedeme de Quincke et reaction anaphylactique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et epidemiologie"),
            PlanSousPartie(lettre="B", titre="Tableau clinique et classification de Ring et Messmer"),
            PlanSousPartie(lettre="C", titre="Prise en charge"),
        ]),
        PlanPartie(numero="VII", titre="Anomalies du bilan du potassium", sous_parties=[
            PlanSousPartie(lettre="A", titre="Hyperkaliemie"),
            PlanSousPartie(lettre="B", titre="Hypokaliemie"),
        ]),
    ]

    # == PARTIE I : ANOMALIES DU BILAN DE L'EAU ET DU SODIUM ==
    partie_i = Partie(numero="I", titre="Anomalies du bilan de l'eau et du sodium", sous_parties=[
        SousPartie(lettre="A", titre="Généralités", rows=[
            FicheRow(concept="Repartition hydrique", detail_md=(
                "- L'eau represente **60%** du poids du corps\n"
                "- Repartie entre compartiment **intracellulaire** (IC) et **extracellulaire** (EC)\n"
                "- Trouble d'hydratation IC : consequence d'un **bilan hydrique** non nul\n"
                "- Trouble d'hydratation EC : consequence d'un **bilan sode** non nul"
            )),
            FicheRow(concept="", detail_md=(
                "- Trouble hydratation **IC** = probleme d'**eau** (natremie anormale)\n"
                "- Trouble hydratation **EC** = probleme de **sodium** (natremie normale)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Deshydratation extracellulaire (DEC)", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Diminution du volume du compartiment extracellulaire\n"
                "- Due a une **perte de sodium** et donc d'eau"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **Pertes extra-renales** :\n"
                "  - Digestives : vomissements prolonges, diarrhees profuses\n"
                "  - Cutanees : sudation+++ (fievre prolongee, exercice intense), "
                "exsudation (brulure etendue, dermatose bulleuse diffuse)\n"
                "- **Pertes renales** :\n"
                "  - Nephropathie interstitielle avec perte de sel\n"
                "  - Syndrome de levee d'obstacle\n"
                "  - Polyurie osmotique (diabete non compense, mannitol)\n"
                "  - Hypercalcemie, diuretiques, insuffisance surrenale aigue\n"
                "- **Troisieme secteur** : peritonites, pancreatites aigues, "
                "occlusions intestinales, rhabdomyolyse traumatique"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Perte de poids\n"
                "- **Signe du pli cutane** (epaule, sternum, front)\n"
                "- **Hypotension arterielle orthostatique** puis de decubitus\n"
                "- Tachycardie compensatrice reflexe\n"
                "- **Choc hypovolemique** si pertes > **30%**\n"
                "- Aplatissement veines superficielles, globes oculaires cernes\n"
                "- Oligurie avec concentration des urines si cause extra-renale\n"
                "- Secheresse peau au niveau des aisselles"
            )),
            FicheRow(concept="Biologie", detail_md=(
                "- Osmolalite plasmatique et natremie **normale** (DEC pure)\n"
                "- **Syndrome d'hemoconcentration** :\n"
                "  - Protidemie > **75 g/L**\n"
                "  - Ht > **50%** (sauf hemorragie)\n"
                "- Consequences de l'hypovolemie :\n"
                "  - Insuffisance renale fonctionnelle\n"
                "  - Hyperuricemie\n"
                "  - Alcalose metabolique de contraction"
            )),
            FicheRow(concept="Demarche etiologique", detail_md=(
                "| Critere | Pertes extra-renales | Pertes renales |\n"
                "|---------|---------------------|----------------|\n"
                "| Diurese | **Oligurie** < 400 mL/24h | Normale/augmentee > 1 000 mL/24h |\n"
                "| Natriurese | Effondree UNa < **20 mmol/L** | Elevee UNa > **20 mmol/L** |\n"
                "| Na/K urinaire | < 1 | > 1 |\n"
                "| Urines | Concentrees (U/P uree > 10) | Non concentrees (U/P uree < 10) |\n"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- **Apport de NaCl** :\n"
                "  - PO : augmentation ration sel + gelule de NaCl\n"
                "  - IV : solute sale a **9 g/L** de NaCl (+/- bicarbonate de sodium isotonique si acidose)\n"
                "- Quantite NaCl = **20% x poids actuel x ((Ht actuelle/0,45) - 1)**\n"
                "- Traitement etiologique\n"
                "- Prevention : utilisation prudente des diuretiques chez les sujets ages"
            )),
        ]),
        SousPartie(lettre="C", titre="Hyperhydratation extracellulaire (HEC)", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Augmentation du volume du compartiment extracellulaire, surtout secteur **interstitiel**\n"
                "- Traduit un **bilan sode positif**"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **Insuffisance cardiaque**\n"
                "- Cirrhose avec ascite\n"
                "- **Syndrome nephrotique**\n"
                "- Hypoproteidemies : denutrition, enteropathies exsudatives"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- **Prise de poids**\n"
                "- Secteur interstitiel : oedemes peripheriques generalises, **blancs, mous, declives, "
                "indolores, prenant le godet**\n"
                "- Épanchements sereux : epanchement pericardique, pleural, peritoneal (**anasarque**)\n"
                "- Secteur plasmatique : augmentation PA, **OAP**\n"
                "- Biologie : signes d'hemodilution (anemie, hypoproteidemie), "
                "osmolalite plasmatique et natremie **normale**"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- Regime alimentaire **desode < 2 g/24h** + reduction apports hydriques\n"
                "- Repos au lit si syndrome oedemateux important\n"
                "- **Diuretiques** d'action rapide souvent necessaires\n"
                "- Traitement etiologique"
            )),
        ]),
        SousPartie(lettre="D", titre="Deshydratation intracellulaire (DIC)", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Diminution du volume intracellulaire secondaire a une **hyperosmolalite plasmatique** "
                "efficace > **300 mOsm/kg**\n"
                "- Due a un bilan hydrique negatif --> **Hypernatremie**\n"
                "- Posm = **(Na x 2) + glycemie** (mmol/L) ; normale = 285 mOsmol/kg"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **Perte d'eau non compensee** :\n"
                "  - Extra-renale : cutanee (coup de chaleur, brulure), respiratoire "
                "(polypnee, hyperventilation), digestive (diarrhee osmotique)\n"
                "  - Renale : polyuries osmotiques (diabete, mannitol), "
                "**diabete insipide** (central : pathologie hypophysaire ; "
                "nephrogenique : lithium, nephropathie interstitielle)\n"
                "- Apport massif de sodium (solute bicarbonate hypertonique)\n"
                "- **Deficit d'apport d'eau** : hypodipsie primitive, absence d'acces libre a l'eau"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- **Troubles neurologiques** : somnolence, asthenie, irritabilite, fievre "
                "d'origine centrale, crises convulsives, coma\n"
                "- Hemorragies cerebro-meningees, hematomes sous-duraux, TVC\n"
                "- **Soif intense** +++\n"
                "- Secheresse muqueuse (face interne des joues)\n"
                "- Syndrome polyuro-polydipsique si diabete insipide\n"
                "- Perte de poids"
            )),
            FicheRow(concept="Biologie et prise en charge", detail_md=(
                "- Posm > **300 mOsmol/kg** ; hypernatremie > **145 mmol/L**\n"
                "- Quantite d'eau a administrer = **60% x poids x ((natremie/140) - 1)**\n"
                "- Formes d'administration : eau pure PO/sonde gastrique, solute glucose 2,5/5% IV, "
                "NaCl hypotonique\n"
                "- **Vitesse de correction** :\n"
                "  - Hypernatremie aigue symptomatique : diminution max **1 mmol/L/h** jusqu'a 145 mmol/L\n"
                "  - Hypernatremie ancienne : max **10 mmol/L/j**"
            )),
            FicheRow(concept="", detail_md=(
                "- DIC pure : eau pure PO (**jamais IV**)\n"
                "- Deshydratation globale : solute sale hypotonique\n"
                "- DIC + HEC : diuretique + eau pure PO / solute hypotonique IV"
            ), kind="a_retenir"),
            FicheRow(concept="", detail_md=(
                "- Ne pas corriger trop vite la natremie : risque de **myelinolyse centro-pontine**"
            ), kind="piege"),
        ]),
        SousPartie(lettre="E", titre="Hyperhydratation intracellulaire (HIC)", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Transfert d'eau du secteur EC vers IC du a une **hypoosmolalite plasmatique**\n"
                "- Se traduit toujours par une **hyponatremie < 135 mmol/L**"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **Ingestion d'eau excessive** : potomanie, syndrome Tea and toast\n"
                "- **Excretion d'eau diminuee** :\n"
                "  - IRC avec DFG < 20 mL/min\n"
                "  - Hypovolemie vraie (causes de DEC)\n"
                "  - Hypovolemie efficace : insuffisance cardiaque, cirrhose, syndrome nephrotique\n"
                "  - **SIADH** : causes infectieuses (meningite, tuberculose, legionellose), "
                "cancers bronchiques, medicamenteuse (sulfamides hypoglycemiants, psychotropes)"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Troubles neurologiques : NV, anorexie, cephalees, obnubilation, coma, crises convulsives\n"
                "- Prise de poids moderee\n"
                "- **Degout de l'eau**\n"
                "- Biologie : Posm < **280 mOsmol/kg**, natremie < **135 mmol/L**"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- Quantite d'eau en exces = **60% x poids x ((natremie/140) - 1)**\n"
                "- Hyponatremie chronique asymptomatique : **restriction hydrique** (500-700 cc/j)\n"
                "- En fonction de l'etat du secteur EC :\n"
                "  - HIC + DEC : apport supplementaire en **NaCl**\n"
                "  - HIC pure : restriction hydrique +/- apport d'osmoles (NaCl) + furosemide 20-60 mg\n"
                "  - HIC + HEC : regime hyposode + diuretiques de l'anse\n"
                "- Vitesse de correction : < **8 mmol/L/j**"
            )),
            FicheRow(concept="", detail_md=(
                "- Hyponatremie severe < 120 mOsmol/kg et symptomatique :\n"
                "  - Perfusion **NaCl hypertonique** avec correction < 1-2 mmol/L/h dans les 3-4 premieres heures\n"
                "  - Ne pas depasser **8-12 mmol/L dans les 24 premieres heures**\n"
                "  - Surveillance **USI** + correction de toute hypoxie"
            ), kind="a_retenir"),
            FicheRow(concept="", detail_md=(
                "- Vitesse de correction > 8 mmol/L/j : risque de **myelinolyse centro-pontine**"
            ), kind="piege"),
        ]),
    ])

    # == PARTIE II : DESORDRES DE L'EQUILIBRE ACIDE-BASE ==
    partie_ii = Partie(numero="II", titre="Desordres de l'equilibre acide-base", sous_parties=[
        SousPartie(lettre="A", titre="GDS arteriel et interpretation", rows=[
            FicheRow(concept="Valeurs normales", detail_md=(
                "| Parametre | Arteriel | Veineux |\n"
                "|-----------|---------|--------|\n"
                "| pH | **7,38-7,42** | 7,32-7,38 |\n"
                "| H+ (nmol/L) | 37-43 | 42-48 |\n"
                "| PCO2 (mmHg) | **36-44** | 42-50 |\n"
                "| HCO3- (mmol/L) | **22-26** | 23-27 |\n"
            )),
            FicheRow(concept="Distinction des desordres acide-base", detail_md=(
                "| Desordre | pH | HCO3- | PCO2 |\n"
                "|----------|----|----- |------|\n"
                "| Acidose metabolique | < 7,38 | **< 22** | < 36 |\n"
                "| Acidose respiratoire | < 7,38 | > 26 | **> 44** |\n"
                "| Alcalose metabolique | > 7,42 | **> 26** | > 44 |\n"
                "| Alcalose respiratoire | > 7,42 | < 22 | **< 36** |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Sang preleve **sans air** dans une seringue heparinee\n"
                "- Toujours verifier la coherence pH / HCO3- / PCO2 et la reponse compensatrice"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Acidoses metaboliques", rows=[
            FicheRow(concept="Tableau clinique", detail_md=(
                "- **Acidose aigue severe** :\n"
                "  - Hyperventilation : **dyspnee de Kussmaul**\n"
                "  - Detresse respiratoire\n"
                "  - Bas debit cardiaque\n"
                "  - Obnubilation, convulsions, coma\n"
                "- **Acidose chronique** :\n"
                "  - Lithiases et nephrocalcinose\n"
                "  - Amyotrophie, retard de croissance\n"
                "  - Osteomalacie, fractures pathologiques"
            )),
            FicheRow(concept="Trou anionique plasmatique", detail_md=(
                "- **TA = (Na+) - ((Cl-) + (HCO3-))** = 12 +/- 4 mmol/L\n"
                "- TA > **16 mmol/L** : TA eleve\n"
                "- Acidose avec TA normal : acidose metabolique **hyperchloremique**\n"
                "- Acidose avec TA eleve : addition d'un acide autre que HCl"
            )),
            FicheRow(concept="Acidose metabolique a TA augmente", detail_md=(
                "| Type | Causes | Anion indose |\n"
                "|------|--------|-------------|\n"
                "| Acidose lactique | Hypoxie tissulaire (choc), biguanides, IHC | Lactate |\n"
                "| Acidocetose | Diabete, alcool, jeune | B hydroxy-butyrate |\n"
                "| Intoxications | Aspirine, ethylene glycol, methanol | Salicylates, glyoxalate, formate |\n"
                "| Insuffisance renale | IRC | Sulfates, phosphates, hippurate |\n"
            )),
            FicheRow(concept="Acidose hyperchloremique", detail_md=(
                "- **Trou anionique urinaire (TAU)** = UNa + UK - UCl\n"
                "- TAU < 0 : reponse renale adaptee --> origine **extra-renale** "
                "(pertes digestives HCO3- : diarrhees, aspirations digestives basses)\n"
                "- TAU > 0 : reponse renale inadaptee --> origine **tubulaire renale** "
                "(acidoses tubulaires proximale ou distale)"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- **Urgence vitale** si pH < **7,10** / bicarbonatmie < **8 mmol/L**\n"
                "- Traitement **etiologique** +++ en priorite\n"
                "- Alcalinisation tres rarement indiquee\n"
                "- EER si insuffisance renale organique associee\n"
                "- Acidose chronique renale : maintenir HCO3- > **25 mmol/L** par bicarbonate de Na 1-6 g/j"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant une acidose metabolique, toujours calculer le **trou anionique plasmatique** "
                "puis le **TAU** si TA normal"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Alcaloses metaboliques et respiratoires", rows=[
            FicheRow(concept="Alcalose metabolique", detail_md=(
                "- Contexte evocateur : diuretiques, abus de laxatifs, vomissements\n"
                "- Manifestations cliniques peu specifiques :\n"
                "  - Crampes, myoclonies, crises de tetanie\n"
                "  - Faiblesse musculaire, hypoventilation\n"
                "  - Arythmie, comitialite, coma"
            )),
            FicheRow(concept="Facteurs d'entretien", detail_md=(
                "- **Contraction volemique**\n"
                "- Hypermineralocorticisme avec HTA"
            )),
            FicheRow(concept="Prise en charge alcalose metabolique", detail_md=(
                "- Correction contraction VEC (DEC) : administration **chlorure de Na**\n"
                "- Corriger carence en **Mg/K**\n"
                "- Supprimer source d'exces en mineralocorticoides / spironolactone / amiloride\n"
                "- Arreter traitement diuretique / aspiration naso-gastrique"
            )),
            FicheRow(concept="Alcalose respiratoire", detail_md=(
                "- Hyperventilation, pas de signes specifiques\n"
                "- Affirmer par GDS\n"
                "- Traitement etiologique de la cause de l'hyperventilation"
            )),
            FicheRow(concept="", detail_md=(
                "- pH > **7,60** engage le **pronostic vital** (alcalose metabolique ou respiratoire)"
            ), kind="piege"),
        ]),
    ])

    # == PARTIE III : DETRESSE RESPIRATOIRE AIGUE ET SDRA ==
    partie_iii = Partie(numero="III", titre="Detresse respiratoire aigue et SDRA", sous_parties=[
        SousPartie(lettre="A", titre="Diagnostic positif de la detresse respiratoire aigue", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Ensemble de signes respiratoires temoignant de la gravite d'une affection "
                "de l'appareil respiratoire\n"
                "- A ne pas confondre avec le **SDRA** (oedeme lesionnel du poumon)"
            )),
            FicheRow(concept="Signes de lutte", detail_md=(
                "- **Polypnee superficielle** : acceleration FR + diminution volume courant "
                "(difficulte a parler, inefficacite de toux)\n"
                "- Recrutement muscles inspiratoires et expiratoires, **tirage** :\n"
                "  - Muscles expiratoires : activation muscles abdominaux (expiration abdominale active)\n"
                "  - Muscles inspiratoires extra-diaphragmatiques : contraction scalenes et SCM "
                "(pouls inspiratoires), tirage intercostal\n"
                "  - Muscles dilatateurs VAS : **battement des ailes du nez**"
            )),
            FicheRow(concept="Signes de faillite", detail_md=(
                "- **Respiration abdominale paradoxale** (faillite de la pompe ventilatoire) :\n"
                "  - Recul paroi anterieure de l'abdomen lors de l'inspiration\n"
                "  - Indique absence de participation du diaphragme a la ventilation\n"
                "  - Fait craindre une defaillance a court terme\n"
                "- **Cyanose** : coloration bleutee des teguments et muqueuses\n"
                "  - Traduit hypoxemie profonde (SpO2 de l'ordre de **80%** pour Hb a 14 g/dL)\n"
                "  - Impose une **oxygenotherapie immediate**"
            )),
            FicheRow(concept="Retentissement neurologique", detail_md=(
                "- Evocateurs d'**hypercapnie** :\n"
                "  - **Asterixis** (flapping tremor)\n"
                "  - Alterations du comportement et de la vigilance (voire coma)\n"
                "  - Cephalees, hypervascularisation des conjonctives\n"
                "  - Tremblements, sueurs, tachycardie, HTA"
            )),
            FicheRow(concept="Retentissement circulatoire", detail_md=(
                "- **Coeur pulmonaire aigu** :\n"
                "  - Turgescence jugulaire, reflux hepato-jugulaire\n"
                "  - Hepatomegalie douloureuse\n"
                "  - **Signe de Harzer** : perception anormale des battements du VD dans le creux epigastrique\n"
                "- **Pouls paradoxal** : diminution de la PA a l'inspiration "
                "(evoque tamponnade ou asthme aigu grave)\n"
                "- **Etat de choc** : peau froide, marbrures, TRC augmente, "
                "PAS < **90 mmHg**, tachycardie > **120/min**, polypnee > **25-30/min**, oligurie"
            )),
            FicheRow(concept="", detail_md=(
                "- La **respiration abdominale paradoxale** est le signe de faillite le plus alarmant : "
                "elle annonce une defaillance respiratoire imminente"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Prise en charge et etiologies", rows=[
            FicheRow(concept="PEC : Urgence+++", detail_md=(
                "- Appel **SAMU/reanimateur**\n"
                "- Surveillance immediate : SpO2 en continu, FC, PA et FR / 10 min\n"
                "- **Oxygenotherapie** au masque nasal\n"
                "- Pose d'une VVP de gros calibre\n"
                "- **Ventilation non invasive** (VNI) : utilisable surtout dans 2 situations :\n"
                "  - Decompensations hypercapniques de **BPCO**\n"
                "  - **OAP cardiogeniques**\n"
                "  - Necessite la cooperation du malade (CI si signes neurologiques)\n"
                "- **Ventilation invasive** (intubation oro-tracheale + ventilation mecanique) :\n"
                "  - D'emblee si defaillance circulatoire ou neurologique associee"
            )),
            FicheRow(concept="Examens complementaires", detail_md=(
                "- NFS-plaquettes, +/- Gr, Rh, RAI\n"
                "- Ionogramme sanguin, uree, creatinine +/- acide lactique\n"
                "- **RXT** face au lit\n"
                "- **GDS** : PaO2 < **60 mmHg**, SaO2 < **90%**, hypercapnie si > 60 mmHg et pH < 7,30\n"
                "- **ECG**\n"
                "- BNP/pro-BNP si doute OAP, PCT si doute pneumonie, HC si fievre"
            )),
            FicheRow(concept="Étiologies avec anomalies radiologiques", detail_md=(
                "- Trois diagnostics en priorite :\n"
                "  - **Pneumonie infectieuse**\n"
                "  - **OAP cardiogenique**\n"
                "  - **Pneumothorax compressif**\n"
                "- En 2e intention : SDRA, exacerbation de pneumopathie infiltrante"
            )),
            FicheRow(concept="Étiologies SANS anomalies radiologiques", detail_md=(
                "- **Decompensation aigue d'une pathologie respiratoire chronique** :\n"
                "  - BPCO +++, obesite morbide, pathologies neuromusculaires\n"
                "  - Hypercapnie et/ou elevation des bicarbonates (hypercapnie chronique)\n"
                "- **Pathologies respiratoires de novo** :\n"
                "  - **Embolie pulmonaire** +++\n"
                "  - Asthme aigu grave"
            )),
            FicheRow(concept="Obstruction VAS", detail_md=(
                "- Diagnostic clinique : **bradypnee inspiratoire** avec allongement du temps inspiratoire\n"
                "- Auscultation : **stridor**\n"
                "- Causes : inhalation corps etranger, laryngite, oedeme de Quincke"
            )),
            FicheRow(concept="", detail_md=(
                "- Detresse respiratoire avec RXT **normale** : penser en priorite a l'**EP** et a l'**AAG**"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="SDRA", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- **Insuffisance respiratoire aigue** (debut brutal/rapidement progressif)\n"
                "- Images **alveolaires bilaterales** sur RXT face, non expliquees par un epanchement "
                "ou une atelectasie\n"
                "- **Sans defaillance cardiaque** ni surcharge volemique\n"
                "- Sévérité definie par le rapport **PaO2/FiO2**"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- Causes pulmonaires : pneumonies infectieuses, inhalation de liquide gastrique\n"
                "- Causes extra-pulmonaires : sepsis, pancreatite aigue, polytraumatisme, "
                "transfusion massive"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- **Intubation oro-tracheale** avec ventilation mecanique\n"
                "- Sedation et/ou curarisation\n"
                "- Traitement de l'etat de choc associe\n"
                "- Correction troubles hydro-electrolytiques et insuffisance renale\n"
                "- Correction anomalies hematologiques severes\n"
                "- Support nutritionnel par alimentation **enterale**\n"
                "- Prevention complications du sejour prolonge en reanimation\n"
                "- Si echec VM : **decubitus ventral** puis possible **ECMO** (circulation extra-corporelle)"
            )),
            FicheRow(concept="", detail_md=(
                "- Le SDRA necessite une prise en charge en **reanimation** avec ventilation mecanique protectrice\n"
                "- L'escalade therapeutique : VM --> decubitus ventral --> ECMO"
            ), kind="a_retenir"),
        ]),
    ])

    # == PARTIE IV : ETATS DE CHOC ==
    partie_iv = Partie(numero="IV", titre="Etats de choc", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et diagnostic positif", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Etat de choc = defaillance du systeme circulatoire aboutissant a une "
                "**inadequation entre apport et besoins tissulaires en O2**\n"
                "- 4 grands mecanismes (souvent intriques) :\n"
                "  - **Hypovolemie**\n"
                "  - **Defaillance myocardique**\n"
                "  - **Obstruction** du lit vasculaire\n"
                "  - Anomalies **distributives**\n"
                "- PAM = 1/3 PAS + 2/3 PAD"
            )),
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- **Hypotension arterielle** +++ :\n"
                "  - PAS < **90 mmHg** ou baisse > 30% ou 40 mmHg par rapport a la PA habituelle\n"
                "  - PAD effondree : en faveur d'un choc **distributif**\n"
                "  - PA differentielle **pincee** : en faveur d'un choc **hypovolemique ou cardiogenique**\n"
                "- Diminution debit sanguin cutane : froideur, cyanose extremites, paleur, "
                "**marbrures** (genoux++), peau moite, TRC > **3 sec**\n"
                "- Troubles de la conscience : confusion, coma\n"
                "- Tachycardie > **120/min** avec pouls filant et tachypnee\n"
                "- **Oligurie** < 0,5 mL/kg/h"
            )),
            FicheRow(concept="Orientation etiologique clinique", detail_md=(
                "| Signe | Choc evoque |\n"
                "|-------|------------|\n"
                "| Saignement exteriorise, paleur, anticoagulant | **Hemorragique** |\n"
                "| ATCD cardiopathie, signes IC | **Cardiogenique** |\n"
                "| Fievre/hypothermie, foyer infectieux | **Septique** |\n"
                "| Signes ICD aigue + signes respiratoires | **Obstructif** |\n"
                "| Exposition allergene, urticaire, bronchospasme | **Anaphylactique** |\n"
            )),
            FicheRow(concept="Examens complementaires", detail_md=(
                "- NFS-plaquettes, GDS et **lactates** (signe cardinal de l'etat de choc)\n"
                "- Ionogramme, uree, creatinine, PCT, CRP\n"
                "- Bilan d'hemostase, bilan hepatique, bilan pre-transfusionnel\n"
                "- ECG, enzymes cardiaques (troponines, CPK)\n"
                "- RXT\n"
                "- **ETT** : examen de reference pour evaluer l'hemodynamique :\n"
                "  - Évaluation fonction VG, mesure debit cardiaque\n"
                "  - Évaluation pressions de remplissage et volemie\n"
                "  - Recherche anomalie valvulaire, epanchement pericardique, signes d'EP"
            )),
            FicheRow(concept="", detail_md=(
                "- L'**elevation des lactates arteriels** est le signe cardinal biologique "
                "commun a tous les etats de choc"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Principes generaux de prise en charge", rows=[
            FicheRow(concept="Mesures generales", detail_md=(
                "- **URGENCE therapeutique** : transfert en reanimation\n"
                "- Surveillance continue : monitorage cardiaque, hemodynamique et respiratoire\n"
                "- Pose de **2 VVP** ou d'une voie veineuse centrale"
            )),
            FicheRow(concept="Oxygenation", detail_md=(
                "- Oxygenotherapie au masque a haute concentration si necessaire\n"
                "- Intubation oro-tracheale + ventilation mecanique si :\n"
                "  - Etat de choc severe\n"
                "  - Insuffisance respiratoire aigue\n"
                "  - Agitation et/ou coma\n"
                "- Objectif de saturation : **92-95%**"
            )),
            FicheRow(concept="Remplissage vasculaire", detail_md=(
                "- Objectif : **PAM > 65 mmHg**\n"
                "- En l'absence de signes de surcharge :\n"
                "  - Epreuve de remplissage : **500 mL de cristalloides isotoniques** "
                "(NaCl 0,9% ou Ringer lactate) en debit libre (10 a 20 min)\n"
                "  - Efficacite a evaluer sur PAM, diminution FC, regression signes d'hypoperfusion\n"
                "  - A repeter si besoin\n"
                "- **Cristalloides en 1re intention**\n"
                "- Colloides de synthese : ne doivent **plus etre utilises** (toxicite renale, risque allergique)\n"
                "- CG si choc hemorragique : objectif Ht > **30%** et Hb > **8 g/dL**"
            )),
            FicheRow(concept="Catecholamines", detail_md=(
                "| Catecholamine | Effet principal |\n"
                "|---------------|----------------|\n"
                "| **Dobutamine** | Inotrope marque |\n"
                "| **Adrenaline** | Inotrope + vasoconstricteur |\n"
                "| **Noradrenaline** | Vasoconstricteur |\n"
                "| **Isoprenaline** | Chronotrope |\n"
            )),
            FicheRow(concept="Indications catecholamines", detail_md=(
                "- Etat de choc persistant malgre remplissage adequat\n"
                "- Choc **cardiogenique** en 1re intention : **dobutamine**\n"
                "- Choc **anaphylactique** en 1re intention : **adrenaline**\n"
                "- Par voie IV, a la seringue electrique, sur voie dediee (idealement catheter central)\n"
                "- Surveillance PAM en continu par **catheter arteriel**"
            )),
            FicheRow(concept="", detail_md=(
                "- Choc cardiogenique : **PAS de remplissage** --> dobutamine d'emblee\n"
                "- Choc hypovolemique : remplissage massif\n"
                "- Choc septique : remplissage puis noradrenaline + ATB\n"
                "- Choc anaphylactique : adrenaline d'emblee"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Choc cardiogenique et hypovolemique", rows=[
            FicheRow(concept="Choc cardiogenique", detail_md=(
                "- Defaillance de la pompe cardiaque avec chute du debit cardiaque + "
                "**augmentation des pressions de remplissage**\n"
                "- Étiologies : **IDM** ++++, poussee d'IC, bradycardie/tachycardie extreme "
                "(BAV haut degre, TV), causes mecaniques (rupture de cordage, endocardite)\n"
                "- Clinique : signes d'IC gauche et droite, PA differentielle **pincee**\n"
                "- Hemodynamique : diminution debit cardiaque, augmentation resistances vasculaires peripheriques"
            )),
            FicheRow(concept="Traitement choc cardiogenique", detail_md=(
                "- **PAS de remplissage** +++\n"
                "- Catecholamines en 1re intention : **dobutamine**\n"
                "- Traitement de la cause :\n"
                "  - **Revascularisation coronaire** si SCA +++\n"
                "  - Assistance mecanique si necessaire : ballon de contre-pulsion intra-aortique, "
                "**ECMO veino-arterielle**"
            )),
            FicheRow(concept="Choc hypovolemique", detail_md=(
                "- Diminution du volume intravasculaire responsable d'une chute du debit cardiaque "
                "(diminution de la precharge)\n"
                "- Étiologies : **hemorragie** (digestive +++, rupture de rate), brulures etendues, "
                "pertes digestives (diarrhees, vomissements)\n"
                "- Clinique : signes de deshydratation (pli cutane), signes d'anemie si hemorragique\n"
                "- Hemodynamique : diminution DC, vasoconstriction peripherique, augmentation FC"
            )),
            FicheRow(concept="Traitement choc hypovolemique", detail_md=(
                "- **Remplissage vasculaire massif** par cristalloides\n"
                "- Catecholamines rarement necessaires (bonne reponse au remplissage) ; "
                "si besoin : **noradrenaline**\n"
                "- **Transfusion** si hemorragie +++\n"
                "- Traitement de la cause : geste d'hemostase (endoscopique, radiologique ou chirurgical)"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant un choc cardiogenique, le remplissage est **contre-indique** "
                "(aggrave la surcharge) : dobutamine d'emblee"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Choc septique et obstructif", rows=[
            FicheRow(concept="Definitions sepsis", detail_md=(
                "- **Sepsis** = syndrome infectieux associe a une dysfonction d'organe "
                "(augmentation >= 2 points du score **SOFA**)\n"
                "- On n'utilise **plus** le terme sepsis severe\n"
                "- **Quick SOFA (qSOFA)** : 3 items :\n"
                "  - PAS < **100 mmHg**\n"
                "  - FR > **22/min**\n"
                "  - Confusion\n"
                "  - 2 items requis pour suspecter le diagnostic de sepsis"
            )),
            FicheRow(concept="★ Choc septique", detail_md=(
                "- Sepsis avec defaillance circulatoire, metabolique et cellulaire\n"
                "- Defini par l'association de :\n"
                "  1. Sepsis\n"
                "  2. Besoin d'amines vasopressives pour maintenir PAM > **65 mmHg**\n"
                "  3. **Hyperlactatemie > 2 mmol/L** malgre remplissage adequat\n"
                "- Choc **distributif** : augmentation permeabilite capillaire, hypovolemie "
                "absolue et relative (vasodilatation peripherique), atteinte myocardique precoce"
            )),
            FicheRow(concept="Clinique et portes d'entree", detail_md=(
                "- A evoquer devant etat de choc **febrile** (ou hypothermie)\n"
                "- PAD basse frequente\n"
                "- Identifier la **porte d'entree** +++ :\n"
                "  - Pulmonaire : **50%**\n"
                "  - Hepato-digestive : 20%\n"
                "  - Urinaire : 10%\n"
                "  - Catheter : 5%\n"
                "  - Cutanee et meningee : < 5%\n"
                "  - Aucune porte identifiee : 15-20%\n"
                "- Hemocultures positives dans **30%** des cas seulement"
            )),
            FicheRow(concept="Traitement choc septique", detail_md=(
                "- **Remplissage vasculaire** +++\n"
                "- Catecholamines si echec du remplissage : **noradrenaline**\n"
                "- **Antibiotherapie IV** a debuter rapidement +++ :\n"
                "  - Double, a large spectre, bactericidie rapide\n"
                "  - Depend du type d'infection suspectee et du terrain\n"
                "  - Exemple : **C3G + aminoside**\n"
                "- Traitement du foyer infectieux : drainage ou intervention chirurgicale"
            )),
            FicheRow(concept="Choc obstructif", detail_md=(
                "- Consequence d'un obstacle au remplissage ou a l'ejection du coeur\n"
                "- Étiologies : **EP massive**, **tamponnade**, **pneumothorax compressif**\n"
                "- Clinique : association signes respiratoires + ICD aigue "
                "(sans signes d'IC gauche)\n"
                "- Hemodynamique : chute DC, fonction cardiaque gauche et volemie preservees"
            )),
            FicheRow(concept="Traitement choc obstructif", detail_md=(
                "- Remplissage vasculaire **modere** par cristalloides\n"
                "- Catecholamines si necessaire : noradrenaline\n"
                "- Traitement de la cause +++ :\n"
                "  - **Fibrinolyse** si EP massive\n"
                "  - **Drainage pericardique** si tamponnade\n"
                "  - **Exsufflation et drainage** si pneumothorax compressif"
            )),
            FicheRow(concept="Surveillance des etats de choc", detail_md=(
                "- **PAM** > 65 mmHg\n"
                "- Diurese horaire (reflet redistribution debit cardiaque)\n"
                "- Debit cardiaque, temperature cutanee, marbrures\n"
                "- Biologie : **lactates arteriels**, GDS, NFS, hemostase, ionogramme, uree, creatinine"
            )),
            FicheRow(concept="", detail_md=(
                "- Le **qSOFA** (PAS < 100, FR > 22, confusion) permet un depistage rapide du sepsis "
                "au lit du malade : 2 criteres sur 3 requis"
            ), kind="a_retenir"),
        ]),
    ])

    # == PARTIE V : HYPERCALCEMIE ==
    partie_v = Partie(numero="V", titre="Hypercalcemie", sous_parties=[
        SousPartie(lettre="A", titre="Definition et tableau clinique", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Calcemie normale : **2,2-2,6 mmol/L**\n"
                "- Regulation : **vitamine D** et **PTH** (hypercalcemiante)\n"
                "- Calcemie corrigee :\n"
                "  - Mesure du calcium ionise **1,15-1,35** (dosage recommande par le CUEN)\n"
                "  - Calcul : calcemie corrigee = calcemie mesuree + ((40 - Alb) / 40)\n"
                "  - Ou : calcemie corrigee = calcemie mesuree + ((40 - Alb) x 0,025)"
            )),
            FicheRow(concept="Hypercalcemie aigue", detail_md=(
                "- **Asymptomatique** si Ca < **3 mmol/L** (40%)\n"
                "- **Symptomatique** si Ca > **3 mmol/L** :\n"
                "  - Generaux : amaigrissement avec DEC, fievre\n"
                "  - Digestifs : anorexie, NV, douleurs abdominales, constipation, rares PA\n"
                "  - Neurologiques et psy : asthenie, cephalees, syndrome pseudo-polynévritique, "
                "hypotonie, agitation, confusion, syndrome depressif\n"
                "  - Renaux : syndrome polyuro-polydipsique (diabete insipide nephrogénique), "
                "DEC, IRAF\n"
                "  - Cardio-vasculaires : tachycardie sinusale, **raccourcissement ST et QT**, "
                "aplatissement onde T, allongement PR, TDR, HTA"
            )),
            FicheRow(concept="Hypercalcemie severe", detail_md=(
                "- Ca > **4,5 mmol/L** :\n"
                "  - Deshydratation avec risque IRAF\n"
                "  - Fievre, obnubilation, coma\n"
                "  - Troubles du rythme et de la conduction cardiaque\n"
                "  - Douleurs abdominales pseudo-chirurgicales\n"
                "  - Vomissements"
            )),
            FicheRow(concept="Hypercalcemie chronique", detail_md=(
                "- Lithiases renales calciques, lithiases biliaires\n"
                "- IRC : nephrocalcinose\n"
                "- Depots calciques : arteres coronaires, valves, fibres myocardiques\n"
                "- Pancreatite chronique calcifiante / pancreatite aigue\n"
                "- Douleurs osseuses diffuses, demineralisation\n"
                "- Chondrocalcinose articulaire"
            )),
            FicheRow(concept="", detail_md=(
                "- A l'**ECG** : raccourcissement du QT = signe le plus precoce de l'hypercalcemie"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Étiologies", rows=[
            FicheRow(concept="Hyperparathyroidie primaire", detail_md=(
                "- PTH inadaptee : normale ou elevee\n"
                "- F > 60 ans\n"
                "- Manifestations osseuses : douleurs mecaniques zones portantes, fractures spontanees, "
                "**osteoporose**\n"
                "- Manifestations extra-osseuses : lithiases renales bilaterales avec nephrocalcinose, "
                "ulcere gastro-duodenal, pancreatite calcifiante, HTA, chondrocalcinose\n"
                "- Biologie : hypercalcemie chronique moderee (< 2,75 mmol/L), PTH normale/augmentee, "
                "**hypercalciurie**, **hypophosphatemie** ++"
            )),
            FicheRow(concept="Étiologies hyperparathyroidie", detail_md=(
                "| Étiologie | Frequence |\n"
                "|-----------|----------|\n"
                "| **Adenome parathyroidien** | 80% |\n"
                "| Hyperplasie diffuse des 4 glandes | 10-15% |\n"
                "| Carcinome parathyroidien | < 2% |\n"
            )),
            FicheRow(concept="Bilan et traitement", detail_md=(
                "- Bilan etiologique : echographie cervicale, scintigraphie au **MIBI**, "
                "+/- scanner/IRM cervicale\n"
                "- Bilan d'extension : DMO (complications osseuses)\n"
                "- Traitement : **chirurgical** +++\n"
                "- Si CI chirurgicale : abstention + surveillance PTH 1-84 et bilan phospho-calcique 1/an"
            )),
            FicheRow(concept="Affections neoplasiques", detail_md=(
                "- Metastases de cancers osteophiles : **sein, rein, thyroide, prostate, poumon, testicule**\n"
                "- Hemopathies : **myelome multiple** des os\n"
                "- Syndrome paraneoplasique : cancer secretant **PTHrp**"
            )),
            FicheRow(concept="Autres etiologies", detail_md=(
                "- **Medicamenteuses** : prise excessive calcium PO, hypervitaminose D exogene, "
                "hypervitaminose A, lithium, diuretiques thiazidiques\n"
                "- Maladies granulomateuses : production 1,25-dihydroxyvitD3 par granulomes\n"
                "- Causes endocriniennes : hyperthyroidie, pheochromocytome, acromegalie\n"
                "- IRC (hyperparathyroidie tertiaire)"
            )),
        ]),
        SousPartie(lettre="C", titre="Prise en charge symptomatique", rows=[
            FicheRow(concept="Moyens therapeutiques", detail_md=(
                "- Arret traitements a risque / inducteurs\n"
                "- Diminution absorption intestinale calcium : glucocorticoides (10-20 mg prednisone/j)\n"
                "- Augmentation elimination urinaire calcium : **NaCl IV** +++\n"
                "- Inhibition resorption osseuse : **biphosphonates** (pamidronate) a adapter a la fonction renale"
            )),
            FicheRow(concept="Hypercalcemie < 3 mmol/L asymptomatique", detail_md=(
                "- Arret traitements inducteurs\n"
                "- **Hydratation large** +++\n"
                "- Traitement de la cause"
            )),
            FicheRow(concept="Hypercalcemie > 3 mmol/L symptomatique", detail_md=(
                "- Arret traitements inducteurs\n"
                "- **Rehydratation IV** par serum physiologique fort debit : **2 000 mL/j**\n"
                "- Puis **biphosphonates**\n"
                "- Moins utilises : diurese forcee au furosemide, calcitonine"
            )),
            FicheRow(concept="Hypercalcemie aigue severe", detail_md=(
                "- Hospitalisation en urgence (+/- reanimation)\n"
                "- Mise en condition : scope cardio-tensionnel/ECG, saturometre, oxygenotherapie, VVP, "
                "SNG si vomissements\n"
                "- Arret medicaments hypercalcemiants, traitement d'une hypoK+ associee\n"
                "- **Remplissage vasculaire massif** IV par serum sale isotonique : **2-6 L/24h**\n"
                "- **Biphosphonates IV** 90 mg (effet retarde 2-3j mais prolonge)\n"
                "- Corticotherapie PO/IV si : forme iatrogene, myelome, granulomatose\n"
                "- **EER** en urgence si :\n"
                "  - Hypercalcemie maligne > **3,75 mmol/L**\n"
                "  - Et/ou echec des mesures precedentes\n"
                "  - Et/ou IRA oligo-anurique"
            )),
            FicheRow(concept="", detail_md=(
                "- Le traitement de 1re ligne de l'hypercalcemie est toujours la **rehydratation** par NaCl IV\n"
                "- Les biphosphonates IV ont un effet retarde de **2-3 jours**"
            ), kind="a_retenir"),
        ]),
    ])

    # == PARTIE VI : OEDEME DE QUINCKE ET REACTION ANAPHYLACTIQUE ==
    partie_vi = Partie(numero="VI", titre="Oedeme de Quincke et reaction anaphylactique", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et epidemiologie", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Reaction anaphylactique : reaction immunologique aigue menacant le pronostic vital\n"
                "- Definie par l'association de symptomes **cardio-vasculaires, respiratoires, "
                "cutanes ou digestifs** d'apparition immediate apres contact avec un allergene\n"
                "- Mecanisme **IgE-dependant** :\n"
                "  - Degranulation basophiles circulants : reaction systemique\n"
                "  - Degranulation mastocytes au sein des tissus : reactions d'organe"
            )),
            FicheRow(concept="Épidémiologie", detail_md=(
                "- Incidence reactions anaphylactiques severes : **10-20/100 000 hab/an** ; 75 deces/an\n"
                "- Accidents per-anesthesiques : 1/130 000 anesthesies, mortalite **6%**"
            )),
            FicheRow(concept="Agents etiologiques", detail_md=(
                "- **Aliments** : 40-60% (90% chez l'enfant) :\n"
                "  - **Arachide** +++ (40% des anaphylaxies alimentaires)\n"
                "  - Proteines oeuf et lait de vache (10%), fruits exotiques (10%)\n"
                "  - Sesame, moutarde\n"
                "- **Medicaments** : 15-20% : ATB (amoxicilline 30%), AINS, curares, PDC iodes\n"
                "- **Venins d'hymenopteres** : 15-20% (guepes, abeilles, frelon)\n"
                "- Latex, effort (delai > 5h entre alimentation/activite sportive)\n"
                "- **Anaphylaxie idiopathique** : 20-30%"
            )),
            FicheRow(concept="FDR de reactions severes", detail_md=(
                "- Maladies cardio-vasculaires\n"
                "- **Asthme non controle**\n"
                "- Prise de **BB-**\n"
                "- Type d'allergene et son caractere masque\n"
                "- Reaction initiale severe\n"
                "- Facteurs amplificateurs : effort, alcool, AINS, infections aigues, fievre, stress"
            )),
        ]),
        SousPartie(lettre="B", titre="Tableau clinique et classification de Ring et Messmer", rows=[
            FicheRow(concept="Manifestations cutanees et muqueuses", detail_md=(
                "- Les premieres a apparaitre, rarement absentes\n"
                "- **Prurit intense** : paumes, plantes +/- muqueuses oropharyngees\n"
                "- Rash cutane erythemateux : exantheme touchant visage, cou, decollete puis tout le corps\n"
                "- **Urticaire** prurigineux\n"
                "- **Angiooedeme** : gonflement de taille variable, mal limite, ferme, non erythemateux, "
                "non/peu prurigineux"
            )),
            FicheRow(concept="Oedeme de Quincke", detail_md=(
                "- Angiooedeme grave de la region laryngee/cou\n"
                "- Gonflement localise : paupieres, levres, teinte blanche/rosee, consistance ferme, "
                "sensation de cuisson\n"
                "- **Gene respiratoire haute** : dyspnee, dysphonie, raucite de la voix, dysphagie\n"
                "- Examen : gonflement langue, luette, paupieres, levres et/ou face, tirage, cornage"
            )),
            FicheRow(concept="Manifestations respiratoires et CV", detail_md=(
                "- Respiratoires : dyspnee, dysphonie, **bronchospasme** (toux seche, sifflante, frein expiratoire), "
                "risque d'arret cardiaque asphyxique\n"
                "- Cardio-vasculaires :\n"
                "  - Hypotension : adulte PAS < **100 mmHg** ou chute > 30%\n"
                "  - Enfant : 0-1 mois 50-60 mmHg, 1-12 mois 70 mmHg, "
                "1-10 ans 70 + (age x 2), 10-17 ans 90 mmHg\n"
                "  - Pouls difficilement perceptible, paleur, hypotonie, perte de connaissance\n"
                "  - Troubles du rythme/conduction, ischemie myocardique, arret cardiaque\n"
                "- Digestives : nausees, vomissements, diarrhees, douleurs pelviennes chez la femme"
            )),
            FicheRow(concept="Classification de Ring et Messmer", detail_md=(
                "| Grade | Symptomes |\n"
                "|-------|----------|\n"
                "| I | Signes cutaneo-muqueux generalises (erytheme, urticaire +/- oedeme) |\n"
                "| II | Atteinte multiviscerale moderee (cutane + hypotension/tachycardie + toux) |\n"
                "| III | Atteinte multiviscerale **severe** (collapsus, bradycardie, bronchospasme) |\n"
                "| IV | Inefficacite cardio-circulatoire, arret respiratoire |\n"
                "| V | Deces par echec de reanimation cardio-pulmonaire |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- La reaction peut etre **biphasique** avec reapparition des symptomes > 4h "
                "apres la phase initiale : surveillance prolongee obligatoire"
            ), kind="piege"),
            FicheRow(concept="Diagnostic differentiel", detail_md=(
                "- Choc anaphylactique : malaise vagal, choc septique/cardiogenique, hypoglycemie, "
                "mastocytose\n"
                "- Oedeme de Quincke isole : syndrome cave superieur, erysipele du visage, "
                "angio-oedeme a bradykinine (ATCD familiaux, pas de prurit ni d'urticaire), "
                "inhalation de corps etranger"
            )),
        ]),
        SousPartie(lettre="C", titre="Prise en charge", rows=[
            FicheRow(concept="Examens complementaires", detail_md=(
                "- **Histamine plasmatique** : s'eleve en quelques minutes, decroissance rapide en 1h "
                "(prelevement precoce +++)\n"
                "- **Tryptase serique** : quasi-specifique du mastocyte\n"
                "  - Detectable jusqu'a 12-24h post-choc\n"
                "  - Prelevements des que possible puis 1-2h et 24h plus tard\n"
                "  - Argument medico-legal, parametre de severite, depistage mastocytose latente\n"
                "- Bilan allergologique a distance > **1 mois** : prick-tests, IDR, +/- IgE specifiques, "
                "+/- tests de provocation"
            )),
            FicheRow(concept="Mesures generales en urgence", detail_md=(
                "- **Stopper le contact** avec l'allergene presume\n"
                "- Patient allonge, jambes surelevees, ne pas verticaliser\n"
                "- Transport medicalise (SAMU)\n"
                "- Liberation VAS si oedeme de Quincke (intubation/tracheotomie si necessaire)\n"
                "- **Oxygenotherapie** haut debit > 10 L/min au masque haute concentration\n"
                "- Bronchodilatateurs en nebulisation si bronchospasme\n"
                "- Remplissage vasculaire par **cristalloides** 500-1 000 mL (20 mL/kg chez l'enfant)"
            )),
            FicheRow(concept="Adrenaline en URGENCE", detail_md=(
                "- Chez tout patient avec manifestations de **grade >= II**\n"
                "- Voie d'administration : **IM** (1/3 moyen cuisse / quadrant antero-externe fesse / deltoide)\n"
                "- Doses :\n"
                "  - Grade I : **pas d'adrenaline**\n"
                "  - Grade II : bolus de **10-20 ug**\n"
                "  - Grade III : bolus de **100-200 ug**\n"
                "  - Grade IV : bolus de **1-2 mg** +/- massage cardiaque externe\n"
                "- Repeter injection IM toutes les **5 min** si non amelioration\n"
                "- Monitoring FC, TA, SpO2, ECG\n"
                "- Si non-reponse (notamment sous BB-) : **glucagon**"
            )),
            FicheRow(concept="Hors urgence", detail_md=(
                "- Surveillance hospitaliere prolongee :\n"
                "  - 8h si reaction systemique sans chute tensionnelle\n"
                "  - **24h** si choc anaphylactique avere\n"
                "- **Corticotherapie** : pas un traitement de l'urgence, permet d'eviter les rechutes"
            )),
            FicheRow(concept="Prevention au long cours", detail_md=(
                "- **Eviction allergene causal** a vie (information/education patient et entourage, PAI chez l'enfant)\n"
                "- **Trousse d'urgence** avec adrenaline auto-injectable :\n"
                "  - Indications absolues : reaction anterieure avec symptomes CV/respiratoires a aliment/"
                "piqure/latex, anaphylaxie induite par l'exercice, anaphylaxie idiopathique, "
                "enfant avec allergie alimentaire + asthme\n"
                "  - Indications relatives : reaction a petite quantite d'aliment, ATCD reaction legere "
                "arachide/fruits a coque, domicile eloigne, allergie alimentaire chez adolescent\n"
                "- Carte d'allergique, liste des medicaments/aliments a risque\n"
                "- **Immunotherapie specifique** (desensibilisation) selon l'allergene"
            )),
            FicheRow(concept="", detail_md=(
                "- L'**adrenaline IM** est le traitement de 1re ligne du choc anaphylactique (grade >= II)\n"
                "- Les corticoides ne sont **PAS** un traitement de l'urgence anaphylactique"
            ), kind="a_retenir"),
        ]),
    ])

    # == PARTIE VII : ANOMALIES DU BILAN DU POTASSIUM ==
    partie_vii = Partie(numero="VII", titre="Anomalies du bilan du potassium", sous_parties=[
        SousPartie(lettre="A", titre="Hyperkaliemie", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Compartiment IC : contient 90% du K+ de l'organisme (K+IC : 100-150 mEq/L)\n"
                "- Compartiment EC : contient < 2% du K+ (K+EC : **3,5-5,0 mmol/L**)\n"
                "- Hyperkaliemie : K+EC > **5,0 mmol/L**"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- **Signes cardiaques** (ECG++++) :\n"
                "  - Augmentation amplitude onde T, **pointue et symetrique** (precordiales)\n"
                "  - Troubles conduction auriculaire : diminution/disparition onde P\n"
                "  - Troubles conduction AV : BSA et BAV\n"
                "  - **Elargissement QRS**\n"
                "  - Tachycardie ventriculaire puis FV et **arret cardiaque**\n"
                "- Signes neurologiques : paresthesies extremites et peribuccales, "
                "faiblesse musculaire/paralysie debutant aux MI, evolution ascendante\n"
                "- Signes digestifs : NV, ileus"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **Exces d'apport** : rare hors insuffisance renale, administration massive IV\n"
                "- **Transfert IC --> EC** :\n"
                "  - Acidose metabolique (elevation 0,5 mmol/L par diminution de 0,1 du pH)\n"
                "  - Catabolisme cellulaire accru : rhabdomyolyse, brulures, hemolyse massive, "
                "lyse tumorale, hemorragie digestive severe\n"
                "  - Hypothermie, exercice physique intense\n"
                "  - Medicaments : BB- non selectifs, intoxication digitalique, agonistes alpha\n"
                "- **Reduction excretion renale** :\n"
                "  - IRA/IRC\n"
                "  - Deficit en mineralocorticoides (insuffisance surrenalienne)\n"
                "  - Iatrogene++ : **AINS, IEC, ARA2**\n"
                "  - Anti-aldosterone"
            )),
            FicheRow(concept="", detail_md=(
                "- Toujours rechercher une **fausse hyperkaliemie** : hemolyse, hyperleucocytose "
                "> 10^5/mm3, thrombocytemie > 10^6/mm3, centrifugation tardive du tube"
            ), kind="piege"),
            FicheRow(concept="Prise en charge", detail_md=(
                "- **Arret** medicaments hyperkaliemiants\n"
                "- **Antagonistes membranaires** : gluconate/chlorure de calcium 10% :\n"
                "  - Ne font pas baisser le K+ mais **protegent le myocarde**\n"
                "  - Injection IV en 2-3 min, amelioration en 1-3 min\n"
                "- **Transfert K+ vers compartiment IC** :\n"
                "  - Insuline 12-16 UI IV + solute glucose 10% (baisse 0,5-1,2 mmol/L en 1-2h)\n"
                "  - Salbutamol 20 mg en nebulisation\n"
                "  - Alcalinisation si acidose metabolique prealable\n"
                "- **Elimination surcharge potassique** :\n"
                "  - Diuretiques de l'anse (1-4h)\n"
                "  - Kayexalate PO/lavement (baisse 0,5-1 mmol/L)\n"
                "  - **EER par hemodialyse** : moyen le plus rapide et efficace"
            )),
            FicheRow(concept="Principes de traitement", detail_md=(
                "- **HyperK+ severe > 7 mmol/L / menacante a l'ECG** :\n"
                "  1. Sel de calcium IV (si signes ECG)\n"
                "  2. Insuline + glucose +/- salbutamol\n"
                "  3. Bicarbonate si acidose metabolique aigue\n"
                "  4. Si OAP : furosemide forte dose + Kayexalate lavement (CI bicarbonate !)\n"
                "  5. EER en urgence\n"
                "- **HyperK+ moderee sans retentissement ECG** :\n"
                "  - Diminution apports potassiques alimentaires et IV\n"
                "  - Eviction medicaments hyperkaliemiants\n"
                "  - Resine echangeuse d'ions PO"
            )),
        ]),
        SousPartie(lettre="B", titre="Hypokaliemie", rows=[
            FicheRow(concept="Definition et tableau clinique", detail_md=(
                "- Hypokaliemie : K+EC < **3,5 mmol/L**\n"
                "- **Signes cardiaques** (ECG+++) :\n"
                "  - Depression segment ST\n"
                "  - Affaissement/inversion onde T\n"
                "  - Augmentation amplitude **onde U**\n"
                "  - Allongement espace QU, elargissement QRS\n"
                "  - TDR supraventriculaires (FA, flutter) et ventriculaires (ESV, TV, torsade de pointes, FV)\n"
                "- Signes musculaires : crampes, myalgies, faiblesse musculaire/paralysie flasque "
                "(debutant aux MI, progression ascendante), rhabdomyolyse si hypoK+ severe\n"
                "- Signes digestifs : constipation, ileus paralytique"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **Carence d'apport** : anorexie mentale, alcoolisme\n"
                "- **Transfert EC --> IC** : alcalose metabolique/respiratoire, "
                "administration d'insuline, agents beta-adrenergiques (salbutamol, dobutamine)\n"
                "- **Augmentation des pertes** :\n"
                "  - Pertes digestives (K+U < 20 mmol/L) : diarrhees aigues/chroniques\n"
                "  - Pertes renales (K+U > 20 mmol/L) :\n"
                "    - Avec HTA : hypermineralocorticisme, syndrome de Cushing\n"
                "    - Sans HTA + acidose : acidocetose diabetique, acidose tubulaire\n"
                "    - Sans HTA + alcalose + chlorurie basse : **vomissements**\n"
                "    - Sans HTA + alcalose + chlorurie elevee : **diuretiques thiazidiques/anse**"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- Traitement **etiologique** ++\n"
                "- **ECG** systematique +++\n"
                "- **HypoK+ moderee sans signe ECG** : supplementation K+ PO :\n"
                "  - Aliments riches en K+ : fruits frais et secs, legumes, viandes, chocolat\n"
                "  - Sels de K+ (Diffu-K, Kaleorid)\n"
                "- **HypoK+ severe (< 2 mmol/L) et/ou troubles ECG** :\n"
                "  - But : retablir kaliemie > **3 mmol/L**\n"
                "  - Chlorure de K+ IV, debit de perfusion < **1,5 g/h**\n"
                "  - Surveillance repetee kaliemie, FC (patient scope), veine perfusee (veinotoxicite KCl)"
            )),
            FicheRow(concept="", detail_md=(
                "- L'**ECG** est l'examen le plus urgent devant toute dyskaliemie\n"
                "- HyperK+ : ondes T amples, pointues et symetriques\n"
                "- HypoK+ : depression ST, onde U, allongement QU"
            ), kind="a_retenir"),
        ]),
    ])

    # == TABLEAUX DE SYNTHESE ==
    tableaux = [
        TableauSynthese(titre="Troubles de l'hydratation -- Synthese", markdown=(
            "| Trouble | Secteur | Cause | Natremie | Signe cle |\n"
            "|---------|---------|-------|---------|----------|\n"
            "| DEC | Extracellulaire | Bilan sode negatif | Normale | Pli cutane, hypotension |\n"
            "| HEC | Extracellulaire | Bilan sode positif | Normale | Oedemes, prise de poids |\n"
            "| DIC | Intracellulaire | Bilan hydrique negatif | > 145 | Soif, troubles neuro |\n"
            "| HIC | Intracellulaire | Bilan hydrique positif | < 135 | Troubles neuro, degout eau |\n"
        )),
        TableauSynthese(titre="Desordres acide-base -- Synthese", markdown=(
            "| Desordre | pH | HCO3- | PCO2 | Signe clinique cle |\n"
            "|----------|-----|------|------|--------------------|\n"
            "| Acidose metabolique | < 7,38 | < 22 | < 36 | Dyspnee de Kussmaul |\n"
            "| Acidose respiratoire | < 7,38 | > 26 | > 44 | Hypoventilation |\n"
            "| Alcalose metabolique | > 7,42 | > 26 | > 44 | Crampes, tetanie |\n"
            "| Alcalose respiratoire | > 7,42 | < 22 | < 36 | Hyperventilation |\n"
        )),
        TableauSynthese(titre="Etats de choc -- Comparaison", markdown=(
            "| Type | Mecanisme | PA diff | DC | Remplissage | Catecholamine |\n"
            "|------|-----------|---------|------|------------|---------------|\n"
            "| Cardiogenique | Defaillance pompe | Pincee | Diminue | CI | Dobutamine |\n"
            "| Hypovolemique | Perte volume | Pincee | Diminue | Massif | +/- Noradrenaline |\n"
            "| Septique | Distributif | PAD basse | Variable | +++ | Noradrenaline |\n"
            "| Obstructif | Obstacle ejection | Variable | Diminue | Modere | +/- Noradrenaline |\n"
            "| Anaphylactique | Vasodilatation | Basse | Variable | +++ | Adrenaline |\n"
        )),
        TableauSynthese(titre="Classification de Ring et Messmer -- Anaphylaxie", markdown=(
            "| Grade | Manifestations | Adrenaline |\n"
            "|-------|---------------|------------|\n"
            "| I | Cutaneo-muqueux generalises | Non |\n"
            "| II | Multiviscerale moderee | 10-20 ug IM |\n"
            "| III | Multiviscerale severe | 100-200 ug IM |\n"
            "| IV | Inefficacite cardio-circulatoire | 1-2 mg IM +/- MCE |\n"
            "| V | Deces | - |\n"
        )),
        TableauSynthese(titre="Dyskaliemies -- Signes ECG comparatifs", markdown=(
            "| Signe ECG | Hyperkaliemie | Hypokaliemie |\n"
            "|-----------|--------------|-------------|\n"
            "| Onde T | Ample, pointue, symetrique | Aplatie/inversee |\n"
            "| Onde P | Diminuee/absente | Normale |\n"
            "| Onde U | Absente | Augmentee |\n"
            "| QRS | Elargi | Elargi |\n"
            "| Risque ultime | TV, FV, arret cardiaque | Torsade de pointes, FV |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-cles", markdown=(
        "| Parametre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Eau corporelle | **60%** poids du corps | Repartition IC/EC |\n"
        "| Hemoconcentration | Protidemie > **75 g/L**, Ht > **50%** | DEC |\n"
        "| Hypernatremie | > **145 mmol/L** | DIC |\n"
        "| Hyponatremie | < **135 mmol/L** | HIC |\n"
        "| Correction hypoNa | < **8 mmol/L/j** | Risque myelinolyse |\n"
        "| Trou anionique | **12 +/- 4 mmol/L** | Normal |\n"
        "| Urgence vitale pH | < **7,10** | Acidose metabolique |\n"
        "| pH vital | > **7,60** | Alcalose metabolique/respi |\n"
        "| PAS choc | < **90 mmHg** | Diagnostic etat de choc |\n"
        "| PAM cible | > **65 mmHg** | Objectif therapeutique |\n"
        "| Lactates | Eleves | Signe cardinal etat de choc |\n"
        "| qSOFA | >= 2 items/3 | Depistage sepsis |\n"
        "| Calcemie normale | **2,2-2,6 mmol/L** | Definition |\n"
        "| Calcemie severe | > **4,5 mmol/L** | Urgence vitale |\n"
        "| EER hypercalcemie | > **3,75 mmol/L** | Si echec traitement |\n"
        "| Kaliemie normale | **3,5-5,0 mmol/L** | Definition |\n"
        "| HyperK+ severe | > **7 mmol/L** | Menacante ECG |\n"
        "| Correction hypoK+ IV | < **1,5 g/h** | Debit max KCl |\n"
    ))

    points_cles = [
        "Trouble IC = probleme d'eau (natremie) ; trouble EC = probleme de sodium",
        "Correction hyponatremie : < 8 mmol/L/j sinon risque de myelinolyse centro-pontine",
        "Devant une acidose metabolique : calculer le trou anionique puis le TAU si TA normal",
        "La respiration abdominale paradoxale annonce une defaillance respiratoire imminente",
        "L'elevation des lactates arteriels est le signe cardinal biologique de l'etat de choc",
        "Choc cardiogenique = PAS de remplissage, dobutamine d'emblee",
        "qSOFA (PAS < 100, FR > 22, confusion) : 2 items/3 pour suspecter un sepsis",
        "L'adrenaline IM est le traitement de 1re ligne du choc anaphylactique (grade >= II)",
        "L'ECG est l'examen le plus urgent devant toute dyskaliemie",
        "Hypercalcemie : rehydratation NaCl IV en 1re ligne puis biphosphonates IV",
    ]

    fiche_eclair_md = (
        "**Hydratation** : IC = eau (natremie), EC = sodium. DEC : pli cutane, hemoconcentration. "
        "HEC : oedemes, regime desode. DIC : hypernatremie > 145, soif, correction < 10 mmol/L/j. "
        "HIC : hyponatremie < 135, restriction hydrique, correction < 8 mmol/L/j.\n\n"
        "**Acide-base** : pH/HCO3-/PCO2. Acidose metabolique : TA plasmatique (TA > 16 = TA eleve). "
        "TA normal : TAU (< 0 extra-renal, > 0 renal). Urgence si pH < 7,10. "
        "Alcalose : pH > 7,60 = pronostic vital engage.\n\n"
        "**Detresse respiratoire** : signes de lutte (polypnee, tirage) puis faillite "
        "(respiration paradoxale, cyanose). VNI si BPCO/OAP. Intubation si defaillance neuro/circulatoire. "
        "SDRA : VM protectrice, DV, ECMO.\n\n"
        "**Etats de choc** : PAS < 90, marbrures, TRC > 3s, oligurie, lactates eleves. "
        "Cardiogenique : dobutamine (pas de remplissage). Hypovolemique : remplissage massif. "
        "Septique : remplissage + noradrenaline + ATB (C3G + aminoside). "
        "Obstructif : traitement cause (fibrinolyse EP, drainage tamponnade). "
        "Anaphylactique : adrenaline IM.\n\n"
        "**Hypercalcemie** : > 3 mmol/L symptomatique. Rehydratation NaCl IV puis biphosphonates. "
        "EER si > 3,75 mmol/L. Étiologies : hyperparathyroidie 1re (adenome 80%), neoplasies.\n\n"
        "**Anaphylaxie** : Ring et Messmer I-V. Adrenaline IM >= grade II. "
        "Tryptase serique pour diagnostic. Eviction + trousse d'urgence + desensibilisation.\n\n"
        "**Potassium** : ECG systematique. HyperK+ : ondes T amples --> calcium IV + insuline/glucose "
        "--> EER si menacante. HypoK+ : onde U, depression ST --> KCl IV < 1,5 g/h si severe."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Reanimation",
        annee="2025-2026",
        item="Items 265, 267, 268, 328, 332, 338, 343, 345, 347, 354",
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
    fiche = build_fiche()

    # Images : charger depuis image_captions.json si disponible
    captions_file = PROJECT_ROOT / "output" / ".work" / "reanimation" / "image_captions.json"
    if captions_file.exists():
        import json
        try:
            captions = json.loads(captions_file.read_text(encoding="utf-8"))
            print(f"  Loaded {len(captions)} image captions")
        except Exception as e:
            print(f"  Could not load image captions: {e}")

    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(exist_ok=True)

    docx_path = output_dir / "Medecine_generale_Reanimation_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Medecine_generale_Reanimation_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path}")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

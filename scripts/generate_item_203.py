"""Génère la fiche de l'Item 203 - Dyspnée aiguë et chronique (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Généralités et analyse sémiologique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition de la dyspnée"),
            PlanSousPartie(lettre="B", titre="Interrogatoire et échelles d'évaluation"),
            PlanSousPartie(lettre="C", titre="Examen clinique et signes de gravité"),
            PlanSousPartie(lettre="D", titre="Examens complémentaires"),
        ]),
        PlanPartie(numero="II", titre="Dyspnée aiguë - étiologies cardiaques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Œdème aigu du poumon (OAP)"),
            PlanSousPartie(lettre="B", titre="Pseudoasthme cardiaque"),
            PlanSousPartie(lettre="C", titre="Tamponnade"),
            PlanSousPartie(lettre="D", titre="Troubles du rythme et choc cardiogénique"),
        ]),
        PlanPartie(numero="III", titre="Dyspnée aiguë - embolie pulmonaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Contexte et clinique"),
            PlanSousPartie(lettre="B", titre="Gazométrie et examens complémentaires"),
        ]),
        PlanPartie(numero="IV", titre="Dyspnée aiguë - étiologies pulmonaires/pleurales", sous_parties=[
            PlanSousPartie(lettre="A", titre="Crise d'asthme et asthme aigu grave"),
            PlanSousPartie(lettre="B", titre="Exacerbation de BPCO"),
            PlanSousPartie(lettre="C", titre="Pneumopathie infectieuse et SDRA"),
            PlanSousPartie(lettre="D", titre="Étiologies pleurales et traumatismes"),
        ]),
        PlanPartie(numero="V", titre="Dyspnée aiguë - causes laryngotrachéales et autres", sous_parties=[
            PlanSousPartie(lettre="A", titre="Étiologies laryngotrachéales"),
            PlanSousPartie(lettre="B", titre="Autres étiologies extra-cardiopulmonaires"),
            PlanSousPartie(lettre="C", titre="Orientation étiologique"),
        ]),
        PlanPartie(numero="VI", titre="Dyspnée chronique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Démarche diagnostique"),
            PlanSousPartie(lettre="B", titre="Étiologies cardiaques et pulmonaires"),
            PlanSousPartie(lettre="C", titre="HTAP et HTP post-embolique"),
            PlanSousPartie(lettre="D", titre="Autres causes"),
        ]),
    ]

    # ── PARTIE I : GÉNÉRALITÉS ET ANALYSE SÉMIOLOGIQUE ──
    partie_i = Partie(numero="I", titre="Généralités et analyse sémiologique", sous_parties=[
        SousPartie(lettre="A", titre="Définition de la dyspnée", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- **Dyspnée** : inconfort ou difficulté respiratoire survenant pour un "
                "niveau d'activité usuelle n'entraînant normalement aucune gêne\n"
                "- Sensation subjective\n"
                "- Symptôme très fréquent\n"
                "- Causes multiples : ORL, pneumologiques, cardiologiques, neurologiques"
            )),
            FicheRow(concept="Distinctions essentielles", detail_md=(
                "- Dyspnée **aiguë** : apparition récente (heures à jours)\n"
                "- Dyspnée **chronique** : évolution sur semaines à mois\n"
                "- Dyspnée ≠ insuffisance respiratoire (les deux termes ne sont pas synonymes)"
            )),
            FicheRow(concept="", detail_md=(
                "- Dyspnée sans insuffisance respiratoire : ex. anémie aiguë\n"
                "- Insuffisance respiratoire sans dyspnée : ex. coma"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Interrogatoire et échelles d'évaluation", rows=[
            FicheRow(concept="Interrogatoire", detail_md=(
                "- Terrain : antécédents, comorbidités, traitement en cours\n"
                "- Rapidité d'installation : aiguë (heures/jours) ou chronique (semaines/mois)\n"
                "- Circonstances :\n"
                "  - repos ou effort\n"
                "  - position : décubitus (**orthopnée**) ou orthostatisme (**platypnée**)\n"
                "  - facteurs saisonniers, climatiques, environnementaux, toxiques\n"
                "  - horaire de survenue\n"
                "- Recherche de signes fonctionnels associés : généraux, respiratoires, "
                "cardiologiques, ORL, neurologiques"
            )),
            FicheRow(concept="◆ Classification NYHA", detail_md=(
                "| Stade | Caractéristiques |\n"
                "|-------|------------------|\n"
                "| I | Absence de dyspnée pour les efforts habituels |\n"
                "| II | Dyspnée pour efforts importants (marche rapide, côte, >= 2 étages) |\n"
                "| III | Dyspnée pour efforts peu intenses (marche à plat, < 2 étages) |\n"
                "| IV | Dyspnée permanente de repos ou pour efforts minimes |\n"
            )),
            FicheRow(concept="Échelle MRC (Medical Research Council)", detail_md=(
                "- Utilisée en pneumologie, à rapprocher de la NYHA\n"
                "| Stade | Caractéristiques |\n"
                "|-------|------------------|\n"
                "| 0 | Exercice intense |\n"
                "| 1 | Marche rapide sur terrain plat ou pente légère |\n"
                "| 2 | Marche à plat plus lente que les gens du même âge |\n"
                "| 3 | Arrêt nécessaire après 100 m ou quelques minutes |\n"
                "| 4 | Empêchant de sortir ou survenant à l'habillement |\n"
            )),
            FicheRow(concept="Évaluation de la dyspnée aiguë", detail_md=(
                "- **EVA** (échelle visuelle analogique) de 10 cm : 0 = absence, 10 = maximale\n"
                "- **Échelle de Borg** : de 0 à 10 (s'applique aussi après exercice prédéterminé)\n"
                "- Nombre d'oreillers utilisés la nuit en cas d'orthopnée"
            )),
        ]),
        SousPartie(lettre="C", titre="Examen clinique et signes de gravité", rows=[
            FicheRow(concept="Phase du cycle respiratoire", detail_md=(
                "- Dyspnée **inspiratoire** : oriente vers cause laryngée\n"
                "- Dyspnée **expiratoire** : oriente vers asthme, BPCO\n"
                "- Dyspnée aux deux temps"
            )),
            FicheRow(concept="Fréquence et rythme respiratoires", detail_md=(
                "- Fréquence :\n"
                "  - tachypnée ou polypnée : **> 20 cycles/min**\n"
                "  - bradypnée : **< 10 cycles/min**\n"
                "- Intensité :\n"
                "  - hyperpnée : augmentation de l'amplitude du volume courant\n"
                "  - hypopnée / oligopnée : diminution de l'amplitude du volume courant"
            )),
            FicheRow(concept="◆ Rythmes pathologiques", detail_md=(
                "- **Dyspnée de Kussmaul** : alternance inspiration / pause / expiration / pause "
                "→ acidose métabolique\n"
                "- **Dyspnée de Cheynes-Stokes** : succession de périodes de polypnée croissante "
                "puis décroissante entrecoupées d'apnées → IC grave, dyspnée d'origine centrale, "
                "bas débit au niveau des centres respiratoires ou du tronc cérébral"
            )),
            FicheRow(concept="Éléments d'orientation étiologique", detail_md=(
                "- Signes généraux : fièvre, frissons, amaigrissement\n"
                "- Symptômes associés : douleur thoracique, toux, expectorations, "
                "bruits respiratoires (wheezing, cornage)\n"
                "- Auscultation pulmonaire : crépitants, sibilants, râles bronchiques, "
                "abolition du murmure vésiculaire\n"
                "- Percussion : matité ou tympanisme\n"
                "- Examens complémentaires : cardiovasculaire (signes d'IC, TVP), ORL, "
                "thyroïdien, neuromusculaire"
            )),
            FicheRow(concept="◆ Signes de gravité d'une dyspnée aiguë", detail_md=(
                "- Mise en jeu des muscles respiratoires accessoires :\n"
                "  - tirage sus-sternal ou sus-claviculaire\n"
                "  - creusement intercostal\n"
                "  - battement des ailes du nez\n"
                "  - balancement thoraco-abdominal\n"
                "  - contracture active expiratoire abdominale\n"
                "- Cyanose, sueurs\n"
                "- **Tachycardie > 120/min**, signes de choc (marbrures), angoisse\n"
                "- **SpO2 < 90 %**\n"
                "- Retentissement neurologique : encéphalopathie respiratoire "
                "(astérixis), agitation, somnolence, sueurs, coma"
            )),
            FicheRow(concept="", detail_md=(
                "- Toujours rechercher les signes de gravité devant toute dyspnée aiguë\n"
                "- SpO2 < 90 % = hypoxémie → indication d'oxygénothérapie immédiate"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Examens complémentaires", rows=[
            FicheRow(concept="◆ Examens de 1re intention", detail_md=(
                "- **Gazométrie artérielle** : apprécie la gravité (hypoxémie, hypercapnie) "
                "et permet une orientation étiologique\n"
                "- **ECG** : signes d'embolie pulmonaire, coronaropathie, trouble du rythme\n"
                "- **Radiographie du thorax** : anomalie pariétale, pleurale, parenchymateuse, "
                "médiastinale, cardiomégalie\n"
                "- Bilan biologique : NFS-plaquettes, ionogramme sanguin, glycémie, "
                "BNP ou NT-proBNP, D-dimères (si suspicion d'embolie pulmonaire)"
            )),
            FicheRow(concept="◆ BNP / NT-proBNP - valeurs seuils", detail_md=(
                "- Devant une dyspnée aiguë :\n"
                "  - **BNP < 100 pg/mL** ou **NT-proBNP < 300 pg/mL** : IC peu probable\n"
                "  - BNP >= 100 pg/mL ou NT-proBNP >= 300 pg/mL : en faveur d'une IC\n"
                "- Seuils NT-proBNP selon l'âge (ESC 2021) :\n"
                "  - > 450 pg/mL si âge < 55 ans\n"
                "  - > 900 pg/mL si âge entre 55 et 75 ans\n"
                "  - > 1 800 pg/mL si âge > 75 ans"
            )),
            FicheRow(concept="D-dimères", detail_md=(
                "- **D-dimères < 500 µg/mL** : permet d'exclure une embolie pulmonaire "
                "si la probabilité clinique est faible ou intermédiaire"
            )),
            FicheRow(concept="Examens de 2e intention", detail_md=(
                "- Selon contexte et orientation étiologique :\n"
                "  - Échodoppler veineux des membres inférieurs\n"
                "  - **Angioscanner pulmonaire** ou **scintigraphie V/Q** si suspicion EP\n"
                "  - Échocardiographie doppler\n"
                "  - Épreuves fonctionnelles respiratoires (EFR)\n"
                "  - Cathétérisme cardiaque\n"
                "  - Épreuve d'effort métabolique (mesure des gaz respiratoires, VO2)"
            )),
        ]),
    ])

    # ── PARTIE II : DYSPNÉE AIGUË - ÉTIOLOGIES CARDIAQUES ──
    partie_ii = Partie(numero="II", titre="Dyspnée aiguë - étiologies cardiaques", sous_parties=[
        SousPartie(lettre="A", titre="Œdème aigu du poumon (OAP)", rows=[
            FicheRow(concept="◆ Généralités", detail_md=(
                "- Étiologie cardiaque la plus fréquente des dyspnées aiguës\n"
                "- Première cause de dyspnée aiguë chez l'adulte avec EP et décompensation "
                "respiratoire chronique"
            )),
            FicheRow(concept="Clinique de l'OAP", detail_md=(
                "- **Orthopnée**, wheezing\n"
                "- **Crépitants bilatéraux** à l'auscultation pulmonaire\n"
                "- **Expectoration rose saumonée**\n"
                "- Terrain : cardiopathie connue, antécédent d'infarctus, "
                "facteurs déclenchants (ex : FA)"
            )),
            FicheRow(concept="Examens paracliniques", detail_md=(
                "- Radiographie thoracique : œdème alvéolaire, cardiomégalie\n"
                "- ECG : anomalies (onde Q de nécrose), fibrillation atriale rapide\n"
                "- BNP (ou NT-proBNP) augmenté"
            )),
            FicheRow(concept="Argument thérapeutique", detail_md=(
                "- Réponse à un traitement adapté (**diurétique** ou **trinitrine IV**) = "
                "argument en faveur du diagnostic"
            )),
        ]),
        SousPartie(lettre="B", titre="Pseudoasthme cardiaque", rows=[
            FicheRow(concept="⚠ Définition", detail_md=(
                "- Doit être considéré comme un **équivalent d'OAP**\n"
                "- Subœdème pulmonaire à forme bronchospastique"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- Orthopnée\n"
                "- Auscultation pulmonaire : sibilants ± crépitants"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Tableau trompeur : ressemble à de l'asthme mais c'est de l'OAP\n"
                "- ⚠ Risque de méconnaissance et d'utilisation à tort de bronchodilatateurs"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Tamponnade", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- Complication des péricardites avec **épanchement péricardique**\n"
                "- En général : tableau de collapsus ou d'**état de choc** avec signes "
                "d'insuffisance ventriculaire droite"
            )),
            FicheRow(concept="◆ Tableau clinique", detail_md=(
                "- Orthopnée\n"
                "- Tachycardie\n"
                "- Auscultation cardiaque : **assourdissement des bruits du cœur**\n"
                "- Auscultation pulmonaire normale\n"
                "- **Turgescence jugulaire**\n"
                "- **Pouls paradoxal** (diminuant à l'inspiration profonde)"
            )),
        ]),
        SousPartie(lettre="D", titre="Troubles du rythme et choc cardiogénique", rows=[
            FicheRow(concept="Troubles du rythme cardiaque mal tolérés", detail_md=(
                "- Troubles du rythme supraventriculaire et tachycardie ventriculaire "
                "peuvent s'accompagner d'une dyspnée"
            )),
            FicheRow(concept="Choc cardiogénique", detail_md=(
                "- La dyspnée n'est pas au premier plan\n"
                "- Tableau dominé par : collapsus et signes d'hypoperfusion"
            )),
            FicheRow(concept="", detail_md=(
                "- Dans la dyspnée avec **état de choc**, la dyspnée s'efface devant "
                "la prise en charge du choc"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE III : DYSPNÉE AIGUË - EMBOLIE PULMONAIRE ──
    partie_iii = Partie(numero="III", titre="Dyspnée aiguë - embolie pulmonaire", sous_parties=[
        SousPartie(lettre="A", titre="Contexte et clinique", rows=[
            FicheRow(concept="◆ Généralités", detail_md=(
                "- Très fréquente, diagnostic souvent difficile\n"
                "- Une des trois principales causes de dyspnée aiguë chez l'adulte"
            )),
            FicheRow(concept="◆ Contexte favorisant", detail_md=(
                "- Alitement\n"
                "- Voyage de longue durée\n"
                "- Immobilisation sous plâtre\n"
                "- Contexte postopératoire"
            )),
            FicheRow(concept="Présentation clinique", detail_md=(
                "- Survenue en règle très brutale\n"
                "- Dyspnée d'intensité variable\n"
                "- Généralement associée à une **douleur thoracique**\n"
                "- Auscultation cardiaque et pulmonaire souvent normale sauf tachycardie"
            )),
        ]),
        SousPartie(lettre="B", titre="Gazométrie et examens complémentaires", rows=[
            FicheRow(concept="◆ Gazométrie artérielle", detail_md=(
                "- **Effet shunt** caractéristique : **hypoxie + hypocapnie**"
            )),
            FicheRow(concept="Démarche diagnostique", detail_md=(
                "- D-dimères si probabilité faible/intermédiaire (**< 500 µg/mL** = exclusion)\n"
                "- **Angioscanner pulmonaire** ou scintigraphie V/Q\n"
                "- Échodoppler veineux des membres inférieurs"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Attention à l'EP survenant sur un terrain bronchoemphysémateux "
                "(tableau trompeur)\n"
                "- ⚠ Toujours évoquer une EP devant une dyspnée isolée (douleur inconstante)"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE IV : DYSPNÉE AIGUË - ÉTIOLOGIES PULMONAIRES/PLEURALES ──
    partie_iv = Partie(numero="IV", titre="Dyspnée aiguë - étiologies pulmonaires et pleurales", sous_parties=[
        SousPartie(lettre="A", titre="Crise d'asthme et asthme aigu grave", rows=[
            FicheRow(concept="Crise d'asthme", detail_md=(
                "- Dyspnée expiratoire\n"
                "- Sibilants à l'auscultation pulmonaire"
            )),
            FicheRow(concept="◆ Asthme aigu grave", detail_md=(
                "- Thorax bloqué en inflation\n"
                "- **Sibilants non retrouvés** ni le murmure vésiculaire\n"
                "- Pouls paradoxal possible\n"
                "- Élocution impossible\n"
                "- **Urgence vitale**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Asthme aigu grave : **silence auscultatoire** = signe de gravité majeur\n"
                "- ⚠ Ne pas être faussement rassuré par l'absence de sibilants"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Exacerbation de BPCO", rows=[
            FicheRow(concept="◆ Définition exacerbation", detail_md=(
                "- Survient souvent à l'occasion d'une surinfection bronchique\n"
                "- Définie par majoration : de la dyspnée, de la toux, du volume ou de la "
                "**purulence des expectorations**"
            )),
            FicheRow(concept="Terrain", detail_md=(
                "- Antécédents de tabagisme\n"
                "- BPCO ou emphysème connus"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- Dyspnée expiratoire avec sibilants\n"
                "- Toux, expectoration\n"
                "- Parfois hippocratisme digital"
            )),
            FicheRow(concept="◆ Signes de gravité (décompensation)", detail_md=(
                "- Dyspnée de repos, cyanose, désaturation\n"
                "- **Polypnée > 25/min**\n"
                "- Défaillance hémodynamique\n"
                "- Signes neurologiques\n"
                "- Hypercapnie\n"
                "- → décompensation engageant le **pronostic vital**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Une surinfection bronchopulmonaire sur BPCO peut déclencher une "
                "poussée d'IC (intrication des deux pathologies)\n"
                "- ⚠ Toujours penser à une embolie pulmonaire associée\n"
                "- ⚠ Attention au diagnostic d'**OAP porté par excès** chez les patients BPCO "
                "avec encombrement trachéobronchique"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Pneumopathie infectieuse et SDRA", rows=[
            FicheRow(concept="Pneumopathie infectieuse", detail_md=(
                "- Syndrome infectieux : fièvre + toux majorée ou expectoration purulente ± "
                "douleur thoracique\n"
                "- Auscultation : **foyer de crépitants** ± syndrome de condensation\n"
                "- Radiographie thorax : foyer avec opacité parenchymateuse systématisée"
            )),
            FicheRow(concept="◆ SDRA - Définition", detail_md=(
                "- Forme très sévère de défaillance pulmonaire aiguë\n"
                "- Caractérisé par :\n"
                "  - augmentation de la perméabilité de la membrane alvéolocapillaire\n"
                "  - **mortalité élevée**\n"
                "  - œdème pulmonaire lésionnel (diagnostic différentiel = OAP hémodynamique)"
            )),
            FicheRow(concept="SDRA - Causes et PEC", detail_md=(
                "- Causes multiples : pneumopathies infectieuses, sepsis, inhalation, "
                "embolie pulmonaire, traumatisme, état de choc, origine toxique\n"
                "- Traitement : hospitalisation en **réanimation**"
            )),
            FicheRow(concept="", detail_md=(
                "- SDRA = étiologie **gravissime** de dyspnée aiguë nécessitant un traitement "
                "en réanimation"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Étiologies pleurales et traumatismes", rows=[
            FicheRow(concept="Pneumothorax", detail_md=(
                "- Terrain : sujet longiligne, tabac, notion d'emphysème\n"
                "- Début brutal, parfois déclenché à l'effort\n"
                "- Douleur latérothoracique\n"
                "- Abolition des vibrations vocales et du murmure vésiculaire\n"
                "- **Tympanisme** à la percussion\n"
                "- Hyperclarté à la radiographie"
            )),
            FicheRow(concept="Épanchement pleural", detail_md=(
                "- Étiologie pleurale fréquente de dyspnée aiguë\n"
                "- Syndrome pleural à l'examen physique"
            )),
            FicheRow(concept="Atélectasies pulmonaires", detail_md=(
                "- Origine maligne ou bénigne\n"
                "- Diagnostic radiologique"
            )),
            FicheRow(concept="Traumatismes du thorax", detail_md=(
                "- Hémopéricarde\n"
                "- Contusion pulmonaire\n"
                "- Pneumothorax, pneumomédiastin\n"
                "- Hémothorax\n"
                "- Volet thoracique"
            )),
        ]),
    ])

    # ── PARTIE V : DYSPNÉE AIGUË - LARYNGOTRACHÉALES ET AUTRES ──
    partie_v = Partie(numero="V", titre="Dyspnée aiguë - causes laryngotrachéales et autres", sous_parties=[
        SousPartie(lettre="A", titre="Étiologies laryngotrachéales", rows=[
            FicheRow(concept="◆ Présentation clinique", detail_md=(
                "- **Dyspnée inspiratoire** avec bradypnée inspiratoire\n"
                "- Cornage\n"
                "- Tirage\n"
                "- Dysphonie fréquemment associée en cas d'origine laryngée"
            )),
            FicheRow(concept="◆ Œdème de Quincke", detail_md=(
                "- **Œdème de la glotte**\n"
                "- Souvent dans un contexte de choc anaphylactique\n"
                "- Gravité fréquemment sous-estimée"
            )),
            FicheRow(concept="Autres étiologies", detail_md=(
                "- Inhalation de corps étranger (le plus souvent chez l'enfant)\n"
                "- Étiologies infectieuses chez l'enfant : **épiglottite**, **laryngite**\n"
                "- Étiologies trachéales :\n"
                "  - sténose tumorale endoluminale ou extraluminale\n"
                "  - corps étranger\n"
                "  - granulome post-intubation"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant une dyspnée inspiratoire : **laisser le patient assis** et "
                "éviter l'examen de l'oropharynx"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Autres étiologies extra-cardiopulmonaires", rows=[
            FicheRow(concept="Liste des causes", detail_md=(
                "- États de choc\n"
                "- Acidose métabolique\n"
                "- Causes neurologiques : atteintes bulbaires, polyradiculonévrite, "
                "myasthénie\n"
                "- Intoxication au monoxyde de carbone\n"
                "- Anémie aiguë\n"
                "- Hyperthermie\n"
                "- Syndrome d'hyperventilation ou dyspnée psychogène"
            )),
            FicheRow(concept="", detail_md=(
                "- Les causes extrathoraciques (acidose, anémie) entraînent davantage "
                "une **polypnée** qu'une véritable dyspnée\n"
                "- En cas d'atteinte neuromusculaire, la dyspnée est tardive et peut "
                "précéder de peu l'**arrêt respiratoire** (gravité sous-estimée)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Orientation étiologique", rows=[
            FicheRow(concept="◆ Arbre décisionnel - signes auscultatoires", detail_md=(
                "| Signe | Orientation |\n"
                "|-------|-------------|\n"
                "| Dyspnée inspiratoire | Cause laryngée (néoplasique si progressive) |\n"
                "| Dyspnée expiratoire + ronchi/sibilants | Asthme, BPCO |\n"
                "| Crépitants | IVG (attention pseudoasthme cardiaque / OAP lésionnel) |\n"
                "| Fièvre + condensation + toux | Pneumopathie |\n"
                "| Syndrome pleural | Pneumothorax, épanchement pleural |\n"
                "| Dyspnée isolée | EP, sepsis sévère, anémie, acidose métabolique |\n"
            )),
            FicheRow(concept="◆ Étiologies pédiatriques", detail_md=(
                "- Chez l'enfant, les étiologies les plus fréquentes de dyspnée aiguë sont :\n"
                "  - **Inhalation de corps étranger**\n"
                "  - **Laryngite**\n"
                "  - **Épiglottite**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Devant une dyspnée isolée sans cause évidente : penser à l'**EP** "
                "(douleur inconstante), puis sepsis, anémie, acidose métabolique\n"
                "- ⚠ Le syndrome d'hyperventilation / dyspnée psychogène est un diagnostic "
                "d'élimination"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE VI : DYSPNÉE CHRONIQUE ──
    partie_vi = Partie(numero="VI", titre="Dyspnée chronique", sous_parties=[
        SousPartie(lettre="A", titre="Démarche diagnostique", rows=[
            FicheRow(concept="◆ Principes généraux", detail_md=(
                "- Toutes les causes de dyspnée aiguë peuvent évoluer initialement de façon "
                "chronique ou subaiguë\n"
                "- Principales causes : d'origine cardiopulmonaire\n"
                "- Bilan sans urgence contrairement à la dyspnée aiguë"
            )),
            FicheRow(concept="◆ Examens complémentaires", detail_md=(
                "- **NFS-plaquettes** : toujours éliminer une **anémie** avant les bilans poussés\n"
                "- **EFR** avec gazométrie artérielle\n"
                "- ECG\n"
                "- Échocardiographie doppler\n"
                "- Radiographie du thorax\n"
                "- Épreuve d'effort métabolique : mesure des gaz respiratoires, VO2 ± SpO2 "
                "à l'effort - permet évaluation objective et orientation cardiaque vs pulmonaire\n"
                "- Scanner thoracique pour l'étude du parenchyme pulmonaire\n"
                "- Cathétérisme cardiaque"
            )),
            FicheRow(concept="", detail_md=(
                "- L'**EFR avec gazométrie** est l'examen clé d'orientation de la dyspnée chronique\n"
                "- Toujours **éliminer une anémie** en premier (NFS) avant tout bilan poussé"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Étiologies cardiaques et pulmonaires", rows=[
            FicheRow(concept="◆ Étiologies cardiaques", detail_md=(
                "- Toutes causes d'IC :\n"
                "  - cardiopathies valvulaires\n"
                "  - cardiopathies ischémiques\n"
                "  - cardiomyopathies dilatées primitive ou toxique\n"
                "  - **IC à fonction systolique préservée**\n"
                "- Constriction péricardique"
            )),
            FicheRow(concept="Démarche dyspnée d'origine cardiaque", detail_md=(
                "- Examen clinique, ECG, radiographie thorax\n"
                "- **BNP / NT-proBNP** : aide à l'orientation vers IC (moins validé qu'en aigu)\n"
                "  - BNP strictement normal → IC peu probable\n"
                "- Échocardiographie : recherche d'une cardiopathie et de signes "
                "d'augmentation des pressions intracardiaques"
            )),
            FicheRow(concept="◆ Pulmonaires - trouble obstructif", detail_md=(
                "- BPCO\n"
                "- Asthme à dyspnée continue"
            )),
            FicheRow(concept="◆ Pulmonaires - trouble restrictif", detail_md=(
                "- **Pneumopathies infiltrantes diffuses** :\n"
                "  - infiltration diffuse de la charpente conjonctive du poumon\n"
                "  - et souvent des espaces alvéolaires, bronchioles, vaisseaux de petit calibre\n"
                "  - avec atteinte extracellulaire (fibrose collagène ou dépôt d'autres substances)\n"
                "- Pneumoconioses : maladies pulmonaires non néoplasiques résultant de "
                "l'inhalation de particules (ex : asbestose)\n"
                "- Séquelles pleurales post-tuberculeuses\n"
                "- Paralysie phrénique\n"
                "- Cyphoscoliose\n"
                "- Obésité morbide"
            )),
        ]),
        SousPartie(lettre="C", titre="HTAP et HTP post-embolique", rows=[
            FicheRow(concept="◆ HTAP - Étiologies", detail_md=(
                "- **HTAP idiopathique** (anciennement primitive)\n"
                "- Forme familiale\n"
                "- Associée à une connectivite : le plus souvent sclérodermie\n"
                "- Associée à un shunt intracardiaque (ex : CIA)\n"
                "- Associée à une infection à VIH\n"
                "- D'origine toxique : antécédents d'anorexigènes "
                "(dexfenfluramine - Isoméride - retiré du marché)"
            )),
            FicheRow(concept="◆ Définition hémodynamique (HTP précapillaire)", detail_md=(
                "- **PAPm > 25 mmHg au repos** ou **> 30 mmHg à l'effort**\n"
                "- **Pression capillaire moyenne < 15 mmHg**\n"
                "- Mesurée lors d'un cathétérisme cardiaque droit"
            )),
            FicheRow(concept="HTAP vs HTP - terminologie", detail_md=(
                "- **HTAP** = élévation isolée de pression dans les artères pulmonaires\n"
                "- **HTP** = terme à employer dans les autres cas :\n"
                "  - HTP post-capillaire associée à une cardiopathie gauche\n"
                "  - HTP associée à une maladie respiratoire ou post-embolique"
            )),
            FicheRow(concept="Présentation et diagnostic", detail_md=(
                "- Patient de tout âge\n"
                "- Examen cardiologique et pulmonaire pouvant rester normal\n"
                "- Radiographie thorax sans modification franche\n"
                "- Diagnostic évoqué par **échocardiographie** : élévation des pressions pulmonaires\n"
                "- Confirmé par **cathétérisme cardiaque droit**"
            )),
            FicheRow(concept="Pronostic et traitement", detail_md=(
                "- Pronostic réservé mais nettement amélioré récemment\n"
                "- Émergence de nouvelles thérapeutiques :\n"
                "  - Antagonistes des récepteurs de l'endothéline : "
                "**bosentan** (Tracleer)"
            )),
            FicheRow(concept="HTP post-embolique", detail_md=(
                "- Complication grave de la maladie thromboembolique\n"
                "- Fait suite à un ou plusieurs épisodes d'embolie pulmonaire\n"
                "- Persistance d'une hypertension pulmonaire précapillaire"
            )),
        ]),
        SousPartie(lettre="D", titre="Autres causes", rows=[
            FicheRow(concept="Obstacles VAS et anémie", detail_md=(
                "- Obstacles sur les voies aériennes supérieures :\n"
                "  - tumeur ORL\n"
                "  - corps étranger méconnu\n"
                "  - tumeurs trachéales ou médiastinales\n"
                "- **Anémie** (toujours y penser)\n"
                "- Acidose métabolique"
            )),
            FicheRow(concept="Causes neurologiques et psychogènes", detail_md=(
                "- Causes neuromusculaires : myopathie\n"
                "- Syndrome d'hyperventilation ou dyspnée psychogène"
            )),
            FicheRow(concept="Pathologies du transport de l'oxygène", detail_md=(
                "- Sulfhémoglobinémie\n"
                "- Méthémoglobinémie\n"
                "- Intoxication au monoxyde de carbone"
            )),
            FicheRow(concept="◆ Syndrome platypnée-orthodéoxie", detail_md=(
                "- Dyspnée en orthostatisme associée à une désaturation\n"
                "- Fait rechercher un **shunt droite-gauche** :\n"
                "  - foramen ovale perméable"
            )),
        ]),
    ])

    # ── SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Comparaison NYHA / MRC", markdown=(
            "| Stade | NYHA (cardiologie) | MRC (pneumologie) |\n"
            "|-------|--------------------|--------------------|\n"
            "| 0 / I | Pas de dyspnée pour efforts habituels | Exercice intense |\n"
            "| 1 / II | Marche rapide, côte, >= 2 étages | Marche rapide à plat / pente |\n"
            "| 2 / III | Marche à plat, < 2 étages | Marche plus lente que le même âge |\n"
            "| 3 / IV | Dyspnée de repos ou efforts minimes | Arrêt après 100 m |\n"
            "| 4 | — | Empêche de sortir / habillement |\n"
        )),
        TableauSynthese(titre="Étiologies des dyspnées aiguës", markdown=(
            "| Origine | Étiologies principales |\n"
            "|---------|------------------------|\n"
            "| Cardiaque | OAP, pseudoasthme cardiaque, tamponnade, troubles du rythme, choc cardiogénique |\n"
            "| Embolie pulmonaire | EP (très fréquente, diagnostic difficile) |\n"
            "| Pulmonaire/pleurale | Asthme, BPCO, pneumopathie, SDRA, décompensation IRC, atélectasie, pneumothorax, épanchement, traumatisme |\n"
            "| Laryngotrachéale | Œdème de Quincke, corps étranger, épiglottite, laryngite, sténose trachéale |\n"
            "| Autres | États de choc, acidose, neuro (bulbaire, PRN, myasthénie), CO, anémie, hyperthermie, psychogène |\n"
        )),
        TableauSynthese(titre="Étiologies des dyspnées chroniques", markdown=(
            "| Origine | Étiologies principales |\n"
            "|---------|------------------------|\n"
            "| Cardiaque | Insuffisance cardiaque, constriction péricardique |\n"
            "| Pulmonaire (TVO) | BPCO, asthme à dyspnée continue |\n"
            "| Pulmonaire (TVR) | PID, pneumoconioses, séquelles pleurales, paralysie phrénique, cyphoscoliose, obésité morbide |\n"
            "| HTAP | Idiopathique, familiale, connectivite, shunt, VIH, toxique |\n"
            "| HTP post-embolique | Suite à EP avec HTP précapillaire persistante |\n"
            "| Autres | Obstacles VAS, anémie, acidose, myopathie, psychogène, CO, sulfhémo/méthémoglobinémie, platypnée-orthodéoxie |\n"
        )),
        TableauSynthese(titre="Orientation auscultatoire d'une dyspnée aiguë", markdown=(
            "| Signe clinique | Diagnostic à évoquer |\n"
            "|----------------|----------------------|\n"
            "| Crépitants bilatéraux + orthopnée | OAP |\n"
            "| Sibilants + orthopnée | Pseudoasthme cardiaque ou crise d'asthme |\n"
            "| Sibilants + toux + expectorations + tabac | Exacerbation BPCO |\n"
            "| Foyer de crépitants + fièvre | Pneumopathie infectieuse |\n"
            "| Bradypnée inspiratoire + cornage + tirage | Cause laryngotrachéale |\n"
            "| Auscultation normale + douleur thoracique brutale | Embolie pulmonaire |\n"
            "| Abolition MV + tympanisme | Pneumothorax |\n"
            "| Assourdissement bruits du cœur + pouls paradoxal + TJ | Tamponnade |\n"
        )),
        TableauSynthese(titre="Rythmes respiratoires pathologiques", markdown=(
            "| Rythme | Description | Étiologie |\n"
            "|--------|-------------|----------|\n"
            "| Kussmaul | Alternance inspi/pause/expi/pause | Acidose métabolique |\n"
            "| Cheynes-Stokes | Polypnée croissante puis décroissante + apnées | IC grave, bas débit cérébral |\n"
            "| Tachypnée / polypnée | > 20 cycles/min | Multiples |\n"
            "| Bradypnée | < 10 cycles/min | Multiples |\n"
            "| Hyperpnée | Augmentation amplitude | Acidose, anémie |\n"
            "| Hypopnée / oligopnée | Diminution amplitude | Épuisement, neuro |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Tachypnée / polypnée | > 20 cycles/min | Fréquence respiratoire |\n"
        "| Bradypnée | < 10 cycles/min | Fréquence respiratoire |\n"
        "| Tachycardie de gravité | > 120/min | Signe de gravité dyspnée aiguë |\n"
        "| SpO2 - seuil hypoxémie | < 90 % | Indication oxygénothérapie |\n"
        "| Polypnée BPCO décompensée | > 25/min | Signe de gravité BPCO |\n"
        "| BNP - IC peu probable (aigu) | < 100 pg/mL | Dyspnée aiguë |\n"
        "| BNP - en faveur d'IC (aigu) | >= 100 pg/mL | Dyspnée aiguë |\n"
        "| NT-proBNP - IC peu probable | < 300 pg/mL | Dyspnée aiguë |\n"
        "| NT-proBNP - en faveur d'IC | >= 300 pg/mL | Dyspnée aiguë |\n"
        "| NT-proBNP (ESC 2021) | > 450 pg/mL | Si âge < 55 ans |\n"
        "| NT-proBNP (ESC 2021) | > 900 pg/mL | Si âge 55-75 ans |\n"
        "| NT-proBNP (ESC 2021) | > 1 800 pg/mL | Si âge > 75 ans |\n"
        "| D-dimères - exclusion EP | < 500 µg/mL | Si probabilité faible/intermédiaire |\n"
        "| PAPm HTP précapillaire (repos) | > 25 mmHg | Cathétérisme droit |\n"
        "| PAPm HTP précapillaire (effort) | > 30 mmHg | Cathétérisme droit |\n"
        "| Pression capillaire HTP précap. | < 15 mmHg | Cathétérisme droit |\n"
        "| Échelle EVA dyspnée | 0 à 10 cm | 0=absence, 10=maximale |\n"
        "| Échelle de Borg | 0 à 10 | 0=nulle, 10=maximale |\n"
    ))

    points_cles = [
        "Dyspnée = inconfort respiratoire **subjectif** ; **différent** de l'insuffisance respiratoire",
        "**NYHA I-IV** (cardio) ≈ **MRC 0-4** (pneumo) pour la dyspnée chronique",
        "Gravité aiguë : tirage, cyanose, **FC > 120**, **SpO2 < 90 %**, astérixis",
        "Bilan 1re intention : **gazométrie**, ECG, RxT, NFS, **BNP/NT-proBNP**, D-dimères",
        "**BNP < 100** ou **NT-proBNP < 300** : IC peu probable ; **D-dimères < 500** : EP exclue",
        "3 causes aiguës adulte : **OAP**, **EP**, décompensation respi chronique",
        "Pseudoasthme cardiaque = **équivalent d'OAP** ; toujours évoquer **EP sur BPCO**",
        "Enfant : **corps étranger**, **laryngite**, **épiglottite** = principales causes aiguës",
        "Quincke (laryngé) et atteinte neuromusculaire : **gravité sous-estimée**",
        "**SDRA** = urgence réa ; acidose/anémie donnent polypnée plus que vraie dyspnée",
    ]

    fiche_eclair_md = (
        "**Définition** : inconfort respiratoire pour activité usuelle, subjective. Aiguë vs chronique. "
        "Dyspnée ≠ insuffisance respiratoire.\n\n"
        "**Sémiologie** : inspiratoire = laryngé ; expiratoire = asthme/BPCO. Orthopnée (décubitus), "
        "platypnée (= shunt D-G). Kussmaul = acidose ; Cheynes-Stokes = IC grave. NYHA I-IV ≈ MRC 0-4.\n\n"
        "**Gravité** : tirage, balancement, cyanose, tachycardie > 120/min, SpO2 < 90 %, astérixis.\n\n"
        "**Bilan** : gazométrie + ECG + RxT + NFS + BNP/NT-proBNP + D-dimères. "
        "BNP < 100 / NT-proBNP < 300 → IC peu probable. D-dimères < 500 µg/mL → EP exclue.\n\n"
        "**3 causes aiguës adulte** : OAP, EP, décompensation respi chronique.\n\n"
        "**OAP** : orthopnée + crépitants bilatéraux + expectoration rose saumonée. Réponse diurétique/trinitrine.\n\n"
        "**EP** : brutal, douleur thoracique, auscultation normale, effet shunt (hypoxie + hypocapnie). "
        "Contexte : alitement, voyage, postop.\n\n"
        "**Tamponnade** : orthopnée + assourdissement BdC + TJ + pouls paradoxal.\n\n"
        "**Asthme aigu grave** : silence auscultatoire, thorax bloqué. Urgence vitale.\n\n"
        "**Exacerbation BPCO** : sibilants + expectoration purulente. Polypnée > 25/min = gravité.\n\n"
        "**Laryngé** : inspiratoire + cornage + tirage. Quincke, corps étranger, épiglottite (enfant). Patient assis.\n\n"
        "**Pièges** : pseudoasthme cardiaque = OAP. EP sur BPCO. OAP par excès chez BPCO encombré. "
        "Dyspnée isolée → EP, sepsis, anémie, acidose.\n\n"
        "**Chronique** : NFS d'abord, puis EFR + gazométrie. Cardiaque, TVO (BPCO/asthme), TVR (PID, "
        "pneumoconioses, cyphoscoliose, obésité).\n\n"
        "**HTAP** : PAPm > 25 mmHg + Pcap < 15 mmHg (KT droit). Bosentan.\n"
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 203 - Dyspnée aiguë et chronique",
        annee="2025-2026",
        item="Item 203",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 203",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-203_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

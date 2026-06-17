"""Génère la fiche de l'Item 330 - Prescription et surveillance des classes de médicaments (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Antiagrégants plaquettaires (AAP)", sous_parties=[
            PlanSousPartie(lettre="A", titre="Aspirine"),
            PlanSousPartie(lettre="B", titre="Thiénopyridines et ticagrélor"),
            PlanSousPartie(lettre="C", titre="Gestion péri-opératoire"),
        ]),
        PlanPartie(numero="II", titre="Héparines et héparinoïdes", sous_parties=[
            PlanSousPartie(lettre="A", titre="Médicaments et pharmacologie"),
            PlanSousPartie(lettre="B", titre="Posologies et surveillance"),
            PlanSousPartie(lettre="C", titre="Indications et effets indésirables"),
            PlanSousPartie(lettre="D", titre="Héparinoïdes apparentés"),
        ]),
        PlanPartie(numero="III", titre="Antivitamines K (AVK)", sous_parties=[
            PlanSousPartie(lettre="A", titre="Médicaments et mode d'action"),
            PlanSousPartie(lettre="B", titre="Relais héparine-AVK et surveillance"),
            PlanSousPartie(lettre="C", titre="Posologie et adaptation"),
            PlanSousPartie(lettre="D", titre="Gestion péri-opératoire"),
        ]),
        PlanPartie(numero="IV", titre="Anticoagulants oraux directs (AOD)", sous_parties=[
            PlanSousPartie(lettre="A", titre="Mode d'action et médicaments"),
            PlanSousPartie(lettre="B", titre="Surveillance et indications"),
            PlanSousPartie(lettre="C", titre="Contre-indications"),
        ]),
        PlanPartie(numero="V", titre="Thrombolytiques (fibrinolytiques)", sous_parties=[
            PlanSousPartie(lettre="A", titre="Médicaments et mode d'action"),
            PlanSousPartie(lettre="B", titre="Indications et surveillance"),
            PlanSousPartie(lettre="C", titre="Contre-indications"),
        ]),
        PlanPartie(numero="VI", titre="Accidents des anticoagulants", sous_parties=[
            PlanSousPartie(lettre="A", titre="Accidents hémorragiques sous héparine"),
            PlanSousPartie(lettre="B", titre="Thrombopénies induites par l'héparine (TIH)"),
            PlanSousPartie(lettre="C", titre="Accidents hémorragiques sous AVK"),
            PlanSousPartie(lettre="D", titre="Accidents sous AOD"),
        ]),
    ]

    # PARTIE I - Antiagrégants plaquettaires
    partie_i = Partie(numero="I", titre="Antiagrégants plaquettaires (AAP)", sous_parties=[
        SousPartie(lettre="A", titre="Aspirine", rows=[
            FicheRow(concept="Médicaments disponibles", detail_md=(
                "- Aspirine Protect® (cp)\n"
                "- Kardégic® (poudre)\n"
                "- Aspégic® (poudre)\n"
                "- Résitune® (cp)\n"
                "- Association possible avec clopidogrel : Duoplavin®"
            )),
            FicheRow(concept="◆ Mode d'action", detail_md=(
                "- Inhibition de la **cyclo-oxygénase** (Cox-1 ++, Cox-2 à un moindre niveau)\n"
                "- Diminue le taux de thromboxane A2 (proagrégant)\n"
                "- Effet **irréversible** sur la plaquette : dure toute la vie de la plaquette (**7-10 jours**)\n"
                "- Autres propriétés :\n"
                "  - Antalgique, antipyrétique, anti-inflammatoire à doses > 1 g/j\n"
                "  - Effet anticancéreux (essentiellement adénocarcinomes)"
            )),
            FicheRow(concept="◆ Posologies", detail_md=(
                "| Indication | Dose |\n"
                "|------------|------|\n"
                "| Dose de charge pour SCA | **250-300 mg** |\n"
                "| Dose d'entretien (coronaropathie, AVC) | **75-160 mg/j** |\n"
                "| Dose anti-inflammatoire / antipyrétique | 500 mg à 2 g/j |\n\n"
                "- Action rapide per os (quelques dizaines de minutes)"
            )),
            FicheRow(concept="Indications", detail_md=(
                "- **Prévention secondaire** :\n"
                "  - Coronaropathie\n"
                "  - Artériopathie des membres inférieurs (AOMI)\n"
                "  - AVC\n"
                "- **Prévention primaire** : sujets à très haut risque vasculaire et faible risque hémorragique\n"
                "- ⚠ La prescription systématique d'aspirine en prévention primaire n'est plus recommandée, "
                "même chez le diabétique"
            )),
            FicheRow(concept="Surveillance", detail_md=(
                "- **Pas de test biologique fiable**"
            )),
            FicheRow(concept="Effets indésirables", detail_md=(
                "- Saignements (effet principal)\n"
                "- Intolérances gastriques\n"
                "- Allergies rares (suspicion bien plus fréquente que les formes avérées)\n"
                "- **Syndrome de Widal** : asthme + polypose nasale + allergie à l'aspirine"
            )),
            FicheRow(concept="", detail_md=(
                "- Aspirine = AAP de référence : inhibition **irréversible** de la Cox-1 pendant **7-10 j**.\n"
                "- Aucun test biologique ne permet de surveiller son efficacité.\n"
                "- Prévention primaire systématique abandonnée, y compris chez le diabétique."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Thiénopyridines et ticagrélor", rows=[
            FicheRow(concept="Médicaments disponibles", detail_md=(
                "- **Clopidogrel** (Plavix®)\n"
                "- **Prasugrel** (Efient®)\n"
                "- **Ticagrélor** (Brilique®)"
            )),
            FicheRow(concept="◆ Mode d'action", detail_md=(
                "- Blocage de la voie de l'ADP par le récepteur plaquettaire **P2Y12** "
                "(mode d'action différent de l'aspirine)\n"
                "- **Clopidogrel** : prodrogue, métabolisme par **CYP2C19** (cytochrome P450)\n"
                "  - ⚠ Chez **15-25 %** des patients : métabolisme insuffisant → médicament peu ou pas actif\n"
                "- Prasugrel : inhibiteur du récepteur P2Y12\n"
                "- Ticagrélor : cyclo-pentyl-triazolo-pyrimidine, antagoniste sélectif du récepteur P2Y12\n"
                "- ◆ Prasugrel et ticagrélor : effet plus puissant et plus rapide que clopidogrel\n"
                "  - Inhibition plaquettaire : **70-80 %** vs **40-50 %** pour le clopidogrel"
            )),
            FicheRow(concept="★ ◆ Posologies", detail_md=(
                "| Molécule | Dose de charge | Entretien |\n"
                "|----------|----------------|-----------|\n"
                "| **Clopidogrel** | 300-600 mg | **75 mg/j** |\n"
                "| **Prasugrel** | 60 mg | **10 mg/j** |\n"
                "| **Ticagrélor** | 180 mg | **90 mg x 2/j** |"
            )),
            FicheRow(concept="Indications", detail_md=(
                "- Clopidogrel :\n"
                "  - Angioplastie coronaire programmée\n"
                "  - SCA (si prasugrel/ticagrélor non indiqués ou après fibrinolyse)\n"
                "  - En association avec aspirine, durée 3 à 12 mois\n"
                "- Prasugrel :\n"
                "  - SCA + association à aspirine\n"
                "  - Chez patients < 75 ans traités par angioplastie\n"
                "- Ticagrélor :\n"
                "  - SCA + association à aspirine\n"
                "- Bithérapie typique dans le SCA : **12 mois** (variable 1-12 mois selon risque hémorragique)\n"
                "- Tendance actuelle :\n"
                "  - Raccourcir la durée de la bithérapie AAP\n"
                "  - Substituer l'aspirine par l'autre AAP au long cours"
            )),
            FicheRow(concept="Surveillance", detail_md=(
                "- **Pas de test biologique fiable**"
            )),
            FicheRow(concept="★ ⚠ Précautions et contre-indications", detail_md=(
                "- **Prasugrel** :\n"
                "  - **Contre-indication absolue** : antécédent d'**AVC**\n"
                "  - Contre-indications relatives :\n"
                "    - Poids **< 60 kg**\n"
                "    - Âge **> 75 ans**\n"
                "- **Ticagrélor** :\n"
                "  - Effet indésirable principal : **dyspnée** (18 % des patients)"
            )),
            FicheRow(concept="", detail_md=(
                "- **Prasugrel** : antécédent d'AVC = contre-indication absolue ; poids < 60 kg ou âge > 75 ans = "
                "contre-indications relatives.\n"
                "- **Ticagrélor** : dyspnée chez 18 % des patients."
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Gestion péri-opératoire", rows=[
            FicheRow(concept="★ ◆ Bonne gestion du traitement antiplaquettaire", detail_md=(
                "- En cas d'arrêt de l'aspirine pour crainte hémorragique : risque "
                "d'évènement athérothrombotique\n"
                "- Après **stent coronarien** : retarder de **3-6 mois** tout acte invasif "
                "à risque hémorragique non urgent\n"
                "- Pour les actes à risque hémorragique modéré (chirurgie/fibroscopie/biopsie) : "
                "ne pas arrêter l'aspirine\n"
                "- Quand le risque hémorragique est très important (chirurgie ORL, urologique, "
                "neurologique) :\n"
                "  - Arrêt **5 jours avant**\n"
                "  - Reprise le plus tôt possible après l'acte"
            )),
            FicheRow(concept="", detail_md=(
                "- Après stent : pas d'acte invasif programmé pendant **3-6 mois**.\n"
                "- Risque modéré : continuer aspirine.\n"
                "- Risque élevé : arrêt **5 j** seulement, reprise rapide."
            ), kind="a_retenir"),
        ]),
    ])

    # PARTIE II - Héparines et héparinoïdes
    partie_ii = Partie(numero="II", titre="Héparines et héparinoïdes", sous_parties=[
        SousPartie(lettre="A", titre="Médicaments et pharmacologie", rows=[
            FicheRow(concept="Classification des héparines", detail_md=(
                "- **Héparine non fractionnée (HNF)** :\n"
                "  - Héparine IV\n"
                "  - Héparine calcique (Calciparine®, voie SC)\n"
                "- **Héparines de bas poids moléculaire (HBPM)** :\n"
                "  - Énoxaparine (Lovenox®)\n"
                "  - Tinzaparine (Innohep®)\n"
                "  - Nadroparine (Fraxiparine®)\n"
                "  - Daltéparine (Fragmine®)\n"
                "- Apparentés :\n"
                "  - **Fondaparinux** (Arixtra®)\n"
                "  - Danaparoïde (Orgaran®)\n"
                "  - Bivalirudine"
            )),
            FicheRow(concept="◆ Mode d'action", detail_md=(
                "- HNF, HBPM et fondaparinux : activation de l'**antithrombine** "
                "(anticoagulant physiologique)\n"
                "- **HNF IV** : effet anticoagulant immédiat\n"
                "  - Demi-vie **≈ 1 h 30**\n"
                "  - Administration : perfusion continue (SAP) ou plusieurs injections/nycthémère\n"
                "  - Héparine calcique : SC x 2 ou x 3/j\n"
                "- HBPM : demi-vie plus longue, SC en 1 ou 2 fois/j\n"
                "- Fondaparinux : demi-vie longue, IV ou SC 1 fois/j"
            )),
            FicheRow(concept="◆ Élimination et insuffisance rénale", detail_md=(
                "- HNF : éliminée par protéines, cellules endothéliales, macrophages (++) "
                "et rein (peu)\n"
                "- HBPM et fondaparinux : élimination essentiellement rénale\n"
                "- ◆ **HNF** : seul anticoagulant utilisable en insuffisance rénale sévère "
                "(**ClCr < 20-30 mL/min**)\n"
                "- ⚠ **HBPM et fondaparinux** : contre-indiqués si **ClCr < 30 mL/min**\n"
                "  - Énoxaparine : règles récentes l'autorisent si ClCr < 30 mL/min"
            )),
            FicheRow(concept="◆ Antidote de l'HNF", detail_md=(
                "- **Sulfate de protamine** IV\n"
                "- Neutralise instantanément l'action de l'HNF"
            )),
        ]),
        SousPartie(lettre="B", titre="Posologies et surveillance", rows=[
            FicheRow(concept="◆ Posologies curatives", detail_md=(
                "- **HNF (curative)** :\n"
                "  - Bolus : **70-80 UI/kg** (≈ 5 000 UI pour 70 kg)\n"
                "  - Entretien : **18 UI/kg/h** (≈ 500 UI/kg/j, soit 30 000 UI/24 h en SAP)\n"
                "- **HBPM (curative)** :\n"
                "  - Fonction du poids : **100 UI anti-Xa/kg**\n"
                "  - Ex : énoxaparine 0,8 mL x 2 pour 80 kg\n"
                "  - ⚠ Connaître précisément le poids du malade"
            )),
            FicheRow(concept="◆ Surveillance HNF", detail_md=(
                "- **TCA** (temps de céphaline avec activateur) : doit être prolongé **2 à 3 fois le témoin**\n"
                "- Et/ou activité anti-Xa : entre **0,5 et 0,8/mL**\n"
                "- 1er TCA : à la **5e heure** après l'instauration du traitement\n"
                "- Adaptation : TCA au moins 1 fois/j"
            )),
            FicheRow(concept="Adaptation des doses HNF IV (selon TCA)", detail_md=(
                "| TCA (s) | Dose de charge (UI/24 h) | Action supplémentaire |\n"
                "|---------|--------------------------|------------------------|\n"
                "| **< 45** | + 6 000 | Bolus 5 000 UI |\n"
                "| 46-54 | + 3 000 | / |\n"
                "| **55-85** | 0 (cible) | / |\n"
                "| 86-110 | -3 000 | Stop SAP 1 h |\n"
                "| **> 110** | -6 000 | Stop SAP 1 h |"
            )),
            FicheRow(concept="Surveillance HBPM", detail_md=(
                "- Sauf exception : pas de mesure de l'activité thérapeutique\n"
                "- Conditions : prescription adaptée au poids + absence d'insuffisance rénale"
            )),
        ]),
        SousPartie(lettre="C", titre="Indications et effets indésirables", rows=[
            FicheRow(concept="◆ Indications", detail_md=(
                "- Anticoagulant d'action rapide : toute situation où une anticoagulation "
                "urgente est nécessaire\n"
                "- Indications principales :\n"
                "  - **TVP et embolie pulmonaire (EP)**\n"
                "  - Troubles du rythme nécessitant anticoagulation (souvent en attente "
                "de l'efficacité des AC oraux)\n"
                "  - **Syndrome coronarien aigu (SCA)**\n"
                "- HBPM : largement utilisées en prévention de la TVP en contexte "
                "chirurgical ou médical"
            )),
            FicheRow(concept="◆ Effets indésirables", detail_md=(
                "- **Complications hémorragiques** (principal)\n"
                "- **TIH** : complication classique mais rare, "
                "phénomène **immunoallergique** (cf. VI)\n"
                "- Complications rares :\n"
                "  - Ostéoporose\n"
                "  - Alopécie\n"
                "  - Élévation des transaminases\n"
                "  - Priapisme\n"
                "  - Insuffisance surrénalienne aiguë"
            )),
            FicheRow(concept="", detail_md=(
                "- HBPM et fondaparinux contre-indiqués si **ClCr < 30 mL/min** (sauf règles récentes pour énoxaparine).\n"
                "- En IR sévère, **HNF** = seule option.\n"
                "- **Sulfate de protamine** = antidote (HNF uniquement)."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Héparinoïdes apparentés", rows=[
            FicheRow(concept="Danaparoïde (Orgaran®)", detail_md=(
                "- Utilisé chez patients ayant présenté ou présentant une **TIH**\n"
                "- Et nécessitant un traitement anticoagulant"
            )),
            FicheRow(concept="Bivalirudine", detail_md=(
                "- Anticoagulant IV\n"
                "- Utilisée essentiellement lors des angioplasties coronariennes"
            )),
        ]),
    ])

    # PARTIE III - Antivitamines K
    partie_iii = Partie(numero="III", titre="Antivitamines K (AVK)", sous_parties=[
        SousPartie(lettre="A", titre="Médicaments et mode d'action", rows=[
            FicheRow(concept="◆ Médicaments AVK", detail_md=(
                "- Anticoagulants oraux pour traitements de longue durée\n"
                "- **Warfarine** (Coumadine®) : AVK de référence dans le monde\n"
                "- **Fluindione** (Préviscan®) : très utilisée en France, mais instauration "
                "déconseillée par l'ANSM depuis **2017**\n"
                "  - ⚠ Risque rare mais grave d'**insuffisance rénale immunoallergique** (< 6 mois)\n"
                "  - Pas de remplacement si patient bien équilibré depuis longtemps\n"
                "- **Acénocoumarol** (Sintrom®) : administration 2 fois/j, non recommandée"
            )),
            FicheRow(concept="◆ Mode d'action", detail_md=(
                "- Blocage hépatique de la synthèse des **facteurs II, VII, IX et X** de la coagulation\n"
                "- Inhibition de la synthèse des **protéines C et S** "
                "(anticoagulants physiologiques circulants)\n"
                "- ⚠ Délai d'action long : pleine efficacité après **3 à 5 jours** de prise\n"
                "  - Lié à la longue demi-vie des cofacteurs vitamine K-dépendants"
            )),
        ]),
        SousPartie(lettre="B", titre="Relais héparine-AVK et surveillance", rows=[
            FicheRow(concept="★ ◆ Relais héparine - AVK", detail_md=(
                "- AVK non efficaces rapidement → précédées d'un traitement par "
                "héparine (HNF, HBPM ou fondaparinux)\n"
                "- Introduction AVK : précoce, dès J1\n"
                "- Non effective avant 4 à 6 jours\n"
                "- 2 conditions pour l'arrêt de l'héparine :\n"
                "  - Au moins **4-5 jours de chevauchement**\n"
                "  - **2 INR efficaces** à 24 heures d'intervalle"
            )),
            FicheRow(concept="◆ Surveillance par INR", detail_md=(
                "- INR (international normalized ratio) : rapport temps de Quick témoin/patient\n"
                "- INR normal sans traitement = **1**\n"
                "- **INR cible** pour la plupart des indications : **2-3**\n"
                "- INR cible plus élevé : domaine des spécialistes (ex : valve mécanique mitrale)\n"
                "- Surveillance :\n"
                "  - Rigoureuse à l'instauration (éviter sur/sous-dosage)\n"
                "  - Espacée avec équilibration\n"
                "  - Au minimum **1 fois/mois** au long cours\n"
                "- Patient équilibré = **≥ 70 %** des INR dans la cible"
            )),
            FicheRow(concept="Éducation thérapeutique", detail_md=(
                "- Éviter les coprescriptions\n"
                "- Connaître les seuils d'alerte des résultats d'INR\n"
                "- Faire appel en cas de saignement\n"
                "- Prévenir tout médecin du traitement au long cours"
            )),
            FicheRow(concept="Automesure de l'INR", detail_md=(
                "- Appareils type Coagucheck® INRange (similaires à ceux de glycémie)\n"
                "- Remboursement en France : enfants et porteurs de valves mécaniques uniquement"
            )),
            FicheRow(concept="◆ Antidotes des AVK", detail_md=(
                "- **PPSB** (initiale des 4 facteurs vitamine K-dépendants) : action très rapide\n"
                "- **Vitamine K** : antagonise les effets en quelques heures"
            )),
            FicheRow(concept="⚠ Grossesse", detail_md=(
                "- AVK = **tératogènes**\n"
                "- Contre-indiqués lors de la première partie du **1er trimestre** de la grossesse"
            )),
        ]),
        SousPartie(lettre="C", titre="Posologie et adaptation", rows=[
            FicheRow(concept="Posologie d'approche", detail_md=(
                "- Pas de dose prédéfinie pour l'efficacité thérapeutique\n"
                "- Dose de départ : plus faible chez la personne âgée\n"
                "- Très liés aux protéines plasmatiques\n"
                "- Métabolisme accéléré ou ralenti par d'autres coprescriptions\n"
                "- ⚠ Coprescriptions contre-indiquées : ex. **miconazole** (Daktarin®)"
            )),
            FicheRow(concept="Exemple warfarine - Initiation", detail_md=(
                "- Coumadine® 5 mg : boîte bleue, cp bisécables\n"
                "- Coumadine® 2 mg : boîte rose, cp bisécables\n"
                "- Schéma :\n"
                "  - J0 : 1 cp (5 mg) le soir\n"
                "  - J1 : 1 cp (5 mg) le soir\n"
                "  - J2 : 1 cp (5 mg) le soir\n"
                "- 1er contrôle INR : matin de **J4** (lendemain de la 3e prise)\n"
                "- INR cible : **2,0 - 3,0**"
            )),
            FicheRow(concept="Adaptation à J4 selon INR", detail_md=(
                "| INR à J4 | Adaptation 4e prise |\n"
                "|----------|----------------------|\n"
                "| **< 1,3** | Augmenter à 8 mg |\n"
                "| 1,3 ≤ INR < 1,5 | Augmenter à 7 ou 6 mg |\n"
                "| 1,5 ≤ INR < 1,75 | Pas de modification (5 mg) |\n"
                "| 1,75 ≤ INR < 2 | Diminuer à 4 ou 3 mg |\n"
                "| 2 ≤ INR < 2,5 | Diminuer à 3 ou 2,5 mg |\n"
                "| **INR ≥ 2,5** | Saut d'une prise puis 2,5 mg |"
            )),
            FicheRow(concept="Adaptation à J6 ± 1", detail_md=(
                "| INR à J6 | Adaptation posologique |\n"
                "|----------|-------------------------|\n"
                "| **INR ≤ 1,6** | Augmenter de 30 à 20 % |\n"
                "| 1,6 < INR ≤ 2,5 | Continuer sans modifier |\n"
                "| 2,5 < INR ≤ 3,5 | Diminuer de 20 à 40 % |\n"
                "| **INR ≥ 3,5** | CAT surdosage |\n\n"
                "- Contrôles suivants : toutes les 48-72 h jusqu'à équilibre "
                "(2 INR successifs entre 2,0 et 3,0)\n"
                "- Si INR < 2 : augmenter de 10 %, attendre 1 semaine pour réévaluer"
            )),
            FicheRow(concept="◆ Indications des AVK aujourd'hui", detail_md=(
                "- Réservées à :\n"
                "  - **Porteurs de valves mécaniques**\n"
                "  - **Insuffisance rénale sévère**\n"
                "  - **SAPL triples positifs**\n"
                "- Pour les autres indications : **AOD** se substituent de plus en plus aux AVK"
            )),
        ]),
        SousPartie(lettre="D", titre="Gestion péri-opératoire", rows=[
            FicheRow(concept="◆ Risque hémorragique modéré", detail_md=(
                "- Pas d'interruption de l'AVK pour la plupart des actes :\n"
                "  - Petite chirurgie\n"
                "  - Soins dentaires\n"
                "  - Certaines ponctions-biopsies\n"
                "- Vérifier que l'INR est dans la limite basse de la fourchette"
            )),
            FicheRow(concept="★ ◆ Risque hémorragique important - Options", detail_md=(
                "- **Option 1 : arrêt AVK 3-4 jours** sans relais héparine\n"
                "  - Indications :\n"
                "    - TVP/EP au-delà du 3e mois du traitement\n"
                "    - FA à faible risque embolique\n"
                "  - Reprise le soir même après normalisation INR\n"
                "- **Option 2 : relais par héparine**\n"
                "  - Arrêt AVK **4-5 jours avant**\n"
                "  - Reprise post-acte sous couverture héparine\n"
                "  - Indications :\n"
                "    - TVP/EP récente (< 3 mois)\n"
                "    - FA à risque embolique élevé\n"
                "    - Porteurs de valves mécaniques\n"
                "- ⚠ Les relais par héparines sont source de complications "
                "hémorragiques et thrombotiques"
            )),
            FicheRow(concept="Objectif INR pour acte programmé", detail_md=(
                "- INR au moment de l'intervention : **< 1,5**\n"
                "- **< 1,2** si neurochirurgie"
            )),
            FicheRow(concept="★ Tableau de gestion AVK selon indication", detail_md=(
                "| Indication | Conduite |\n"
                "|-----------|----------|\n"
                "| FA sans antécédent embolique, MTEV à risque modéré | Arrêt AVK sans relais ; reprise 24-48 h |\n"
                "| Valves mécaniques (tout type), FA avec antécédent embolique, MTEV à haut risque | "
                "Arrêt AVK + **relais héparine à dose curative** |"
            )),
            FicheRow(concept="", detail_md=(
                "- INR cible **2-3** pour la plupart des indications.\n"
                "- Relais héparine-AVK : chevauchement **4-5 j** + 2 INR efficaces à 24 h d'intervalle.\n"
                "- AVK = **1ère cause iatrogène d'hospitalisation** (13 % des hospitalisations pour effets indésirables médicamenteux)."
            ), kind="a_retenir"),
            FicheRow(concept="", detail_md=(
                "- ⚠ Ne pas instaurer de **fluindione** (déconseillée par l'ANSM depuis 2017).\n"
                "- Ne pas associer **miconazole** (Daktarin®) avec AVK.\n"
                "- Tératogénicité : pas d'AVK au **1er trimestre** de grossesse."
            ), kind="piege"),
        ]),
    ])

    # PARTIE IV - Anticoagulants oraux directs
    partie_iv = Partie(numero="IV", titre="Anticoagulants oraux directs (AOD)", sous_parties=[
        SousPartie(lettre="A", titre="Mode d'action et médicaments", rows=[
            FicheRow(concept="◆ Mode d'action", detail_md=(
                "- Antithrombotiques oraux directs : inhibent\n"
                "  - Soit le **facteur II (anti-IIa)**\n"
                "  - Soit le **facteur X (anti-Xa)**\n"
                "- Développement favorisé par les difficultés de gestion des AVK"
            )),
            FicheRow(concept="◆ Médicaments disponibles en France", detail_md=(
                "| Molécule | DCI | Cible |\n"
                "|----------|-----|-------|\n"
                "| **Pradaxa®** | Dabigatran | Anti-IIa |\n"
                "| **Xarelto®** | Rivaroxaban | Anti-Xa |\n"
                "| **Eliquis®** | Apixaban | Anti-Xa |"
            )),
            FicheRow(concept="◆ Élimination rénale", detail_md=(
                "- **Dabigatran** : **80 %** rénale\n"
                "- **Rivaroxaban** : **33 %** rénale\n"
                "- **Apixaban** : **25 %** rénale\n"
                "- ⚠ S'enquérir systématiquement de la fonction rénale\n"
                "- Déconseillés si **ClCr (Cockcroft) < 25-30 mL/min**"
            )),
            FicheRow(concept="Nombre de prises/j", detail_md=(
                "- Dabigatran et apixaban : **2 fois/j**\n"
                "- Rivaroxaban : 1 fois/j dans la plupart des indications\n"
                "  - 2 fois/j en début de traitement de TVP/EP"
            )),
            FicheRow(concept="◆ Interactions médicamenteuses", detail_md=(
                "- Moins d'interactions qu'avec les AVK\n"
                "- Existent toutefois avec :\n"
                "  - Macrolides\n"
                "  - Antiprotéases\n"
                "  - Antifongiques azolés\n"
                "  - Certains anticancéreux\n"
                "  - Amiodarone\n"
                "  - Diltiazem, vérapamil\n"
                "- ⚠ **AINS** à éviter (augmentent le risque hémorragique), comme avec AVK"
            )),
            FicheRow(concept="◆ Rapidité d'action", detail_md=(
                "- Efficacité rapide : environ **2 heures** après la 1re prise\n"
                "- Patient en consultation pour indication établie (TVP, EP, FA) : "
                "anticoagulé immédiatement sans relais héparine"
            )),
        ]),
        SousPartie(lettre="B", titre="Surveillance et indications", rows=[
            FicheRow(concept="◆ Surveillance biologique", detail_md=(
                "- **Pas de test biologique** en routine pour vérifier l'efficacité\n"
                "- Médicaments validés sans suivi biologique\n"
                "- Dosage du médicament possible mais réservé aux situations particulières\n"
                "- ⚠ La plupart des tests de coagulation (TCA, TP, INR) sont perturbés par les AOD\n"
                "  - Ne peuvent **PAS** servir à connaître l'efficacité du traitement"
            )),
            FicheRow(concept="Antidotes", detail_md=(
                "- Dabigatran : antidote spécifique = **idarucizumab (Praxbind®)**\n"
                "- Anti-Xa : antidote en cours de commercialisation"
            )),
            FicheRow(concept="◆ Indications principales (FA, MTEV, SCA)", detail_md=(
                "- Indications et posologies variables selon molécule et indication\n"
                "- Indications principales :\n"
                "  - **FA non valvulaire** (prévention thromboembolique)\n"
                "  - Traitement curatif TVP/EP (anti-Xa)\n"
                "  - Prévention et traitement de la MTEV (anti-Xa)\n"
                "  - Prévention post-chirurgie orthopédique\n"
                "- ⚠ AOD perturbent la recherche des **APL** (LA/DRVVT)\n"
                "  - Arrêter **2-3 j avant** un bilan de thrombophilie avec recherche d'APL"
            )),
            FicheRow(concept="Avantages des AOD vs AVK", detail_md=(
                "- Action rapide (≈ 2 h)\n"
                "- Pas de surveillance biologique\n"
                "- Moins d'interactions médicamenteuses\n"
                "- Pas de relais héparine nécessaire\n"
                "- Posologie en fonction de l'âge, poids, fonction rénale"
            )),
        ]),
        SousPartie(lettre="C", titre="Contre-indications", rows=[
            FicheRow(concept="⚠ Contre-indications absolues", detail_md=(
                "- **Valves cardiaques mécaniques**\n"
                "- **Rétrécissement mitral (RM) serré**\n"
                "- **Insuffisance rénale sévère** (ClCr < 30 mL/min, déconseillés)"
            )),
            FicheRow(concept="", detail_md=(
                "- Pas d'AOD dans prothèses valvulaires mécaniques ou rétrécissement mitral.\n"
                "- Pas d'AOD ni d'HBPM en insuffisance rénale sévère.\n"
                "- Pas de surveillance biologique en routine, mais arrêt 2-3 j avant recherche d'APL."
            ), kind="a_retenir"),
        ]),
    ])

    # PARTIE V - Thrombolytiques
    partie_v = Partie(numero="V", titre="Thrombolytiques (fibrinolytiques)", sous_parties=[
        SousPartie(lettre="A", titre="Médicaments et mode d'action", rows=[
            FicheRow(concept="◆ Mode d'action", detail_md=(
                "- Activateurs de la fibrinolyse physiologique, en particulier du **plasminogène**\n"
                "- Détruisent le caillot une fois formé"
            )),
            FicheRow(concept="Médicaments", detail_md=(
                "- Anciennes générations :\n"
                "  - Streptokinase : plus commercialisée\n"
                "  - Urokinase : risque allergique\n"
                "- Nouvelles générations :\n"
                "  - **Altéplase** (Actilyse®)\n"
                "  - **Ténectéplase** (Métalyse®)\n"
                "    - Demi-vie relativement longue → administration simplifiée en un seul bolus IV"
            )),
        ]),
        SousPartie(lettre="B", titre="Indications et surveillance", rows=[
            FicheRow(concept="◆ Indications", detail_md=(
                "- Administration IV dans des conditions très précises\n"
                "- **Infarctus du myocarde** :\n"
                "  - **< 6 à 12 h**\n"
                "  - Pas de possibilité d'angioplastie\n"
                "  - En France : essentiellement par les SAMU en préhospitalier\n"
                "- **AVC ischémique** :\n"
                "  - Dans les **4 h 30**\n"
                "  - Après exclusion d'une cause hémorragique\n"
                "- **Embolie pulmonaire grave**"
            )),
            FicheRow(concept="◆ Surveillance", detail_md=(
                "- Risque hémorragique important : pèse l'indication\n"
                "- Risque d'**hémorragie intracérébrale** : **0,7 à 2 %**\n"
                "- Tests classiques (TCA, TP) perturbés pendant toute la durée de l'effet (≈ 24 h)\n"
                "- Surveillance des saignements cliniques et infracliniques :\n"
                "  - Point de ponction artérielle\n"
                "  - Voie veineuse\n"
                "  - Sonde urinaire\n"
                "- Groupage sanguin systématique (éviter perte de temps si saignement grave)"
            )),
        ]),
        SousPartie(lettre="C", titre="Contre-indications", rows=[
            FicheRow(concept="⚠ Contre-indications", detail_md=(
                "- Allergie connue au produit\n"
                "- Risque hémorragique accru :\n"
                "  - Trouble de la coagulation congénital ou acquis\n"
                "  - Thrombopathie sévère\n"
                "  - Thrombopénie sévère\n"
                "- Poussée ulcéreuse (< 6 mois)\n"
                "- Chirurgie générale (< 10 jours)\n"
                "- Chirurgie vasculaire (< 1 mois)\n"
                "- Traumatisme grave ou ponction récente de gros vaisseaux non compressibles\n"
                "- Réanimation cardiopulmonaire prolongée\n"
                "- Anévrisme ou malformation artérielle/veineuse, malformation vasculaire cérébrale\n"
                "- **HTA non contrôlée** (> 200 mmHg)\n"
                "- AVC étendu (< 6 mois)\n"
                "- Traitement associé par AVK\n"
                "- Insuffisance hépatique sévère\n"
                "- Péricardite aiguë\n"
                "- Endocardite aiguë ou subaiguë\n"
                "- **Grossesse**"
            )),
            FicheRow(concept="", detail_md=(
                "- Fibrinolyse dans l'IDM : uniquement si angioplastie impossible et **< 6-12 h**.\n"
                "- Fibrinolyse dans l'AVC ischémique : fenêtre **4 h 30**, après élimination d'une cause hémorragique.\n"
                "- Risque d'hémorragie cérébrale : **0,7-2 %**."
            ), kind="a_retenir"),
        ]),
    ])

    # PARTIE VI - Accidents des anticoagulants
    partie_vi = Partie(numero="VI", titre="Accidents des anticoagulants", sous_parties=[
        SousPartie(lettre="A", titre="Accidents hémorragiques sous héparine", rows=[
            FicheRow(concept="Fréquence", detail_md=(
                "- Traitement curatif : **1 à 4 %**\n"
                "- Traitement préventif : **1 à 2 %**"
            )),
            FicheRow(concept="◆ Facteurs de risque hémorragique", detail_md=(
                "- Âge\n"
                "- Sexe féminin\n"
                "- Faible poids corporel\n"
                "- Intensité et durée de l'anticoagulation\n"
                "- Comorbidités :\n"
                "  - Pathologie digestive ou cérébrale à risque hémorragique\n"
                "  - Insuffisance hépatocellulaire\n"
                "  - Traumatisme ou chirurgie récente\n"
                "  - Thrombopénie\n"
                "  - Troubles congénitaux de la coagulation à risque hémorragique\n"
                "  - Insuffisance rénale (surtout HBPM)\n"
                "- Association à un autre antithrombotique (AVK, AAP) ou **AINS** augmente le risque"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Surdosage biologique asymptomatique :\n"
                "  - TCA > 3 fois témoin ou héparinémie élevée pour HNF\n"
                "  - Adapter les doses\n"
                "- Anémie microcytaire ferriprive sans hémorragie apparente\n"
                "  - Nécessité d'une **NFS régulière** au long cours\n"
                "- Hématome ou hémorragie extériorisée grave ou non"
            )),
            FicheRow(concept="◆ CAT en cas d'accident hémorragique", detail_md=(
                "- Évaluer la gravité :\n"
                "  - Examen clinique\n"
                "  - PA, FC, recherche signes de choc\n"
                "  - Dosage hémoglobine et hématocrite\n"
                "- Accident mineur :\n"
                "  - Adapter posologies\n"
                "  - Surveillance clinico-biologique rapprochée\n"
                "- **Accident majeur** :\n"
                "  - Balance risque hémorragique vs risque d'arrêt (valves mécaniques)\n"
                "  - Remplissage IV par macromolécules\n"
                "  - Transfusion CGR si nécessaire\n"
                "  - Évaluer l'intérêt de l'antidote = **sulfate de protamine**"
            )),
            FicheRow(concept="Prévention", detail_md=(
                "- Bien peser l'indication\n"
                "- Adapter les doses au poids (HBPM)\n"
                "- Surveiller quotidiennement la biologie (HNF)\n"
                "- Respecter la contre-indication HBPM en insuffisance rénale sévère"
            )),
        ]),
        SousPartie(lettre="B", titre="Thrombopénies induites par l'héparine (TIH)", rows=[
            FicheRow(concept="◆ Définition et types", detail_md=(
                "- 2 types :\n"
                "  - **Type I (précoce)** : bénigne, non immune, précoce, sans complication, "
                "régresse malgré poursuite de l'héparine\n"
                "  - **Type II (TIH vraie)** : **immunoallergique**, potentiellement grave, "
                "tardive vers **J7-J10**\n"
                "- Mécanisme TIH II : **anticorps anti-PF4** (facteur 4 plaquettaire) modifié par héparine\n"
                "- Activation plaquettaire intense + activation coagulation → thromboses :\n"
                "  - Veineuses (**80 %**)\n"
                "  - Artérielles (**20 %**)\n"
                "- ⚠ Le risque est **thrombotique** (et non hémorragique, sauf CIVD associée)"
            )),
            FicheRow(concept="◆ Épidémiologie", detail_md=(
                "- Incidence : **0,05 à 3 %**\n"
                "- Plus fréquente avec HNF qu'avec HBPM\n"
                "- Plus fréquente en milieu chirurgical (chirurgie cardiaque, orthopédique)\n"
                "- ◆ Délai typique : **5-8 jours** après début héparine\n"
                "  - Peut être plus court (dès J1) si exposition récente (< 3 mois)\n"
                "  - Peut être plus long (> 3 semaines) avec HBPM"
            )),
            FicheRow(concept="◆ Critères HAS de suspicion", detail_md=(
                "- **Plaquettes < 100 000/mm³ (100 G/L)** et/ou chute relative sur 2 numérations "
                "(30-50 %)\n"
                "- ⚠ Nécessité d'une numération plaquettaire avant ou dans les 24 h de l'introduction\n"
                "- Apparition de thromboses ou extension du processus initial sous héparine\n"
                "- Résistance biologique à l'HNF (TCA ne décroche pas)\n"
                "- Placards inflammatoires au site d'injection SC\n"
                "- Rarement : insuffisance surrénalienne aiguë sur nécrose des surrénales\n"
                "- Chez 80 % des patients : thrombopénie 30-70 G/L\n"
                "- **CIVD** associée dans 10-20 % des cas"
            )),
            FicheRow(concept="Localisation des thromboses (si TIH compliquée)", detail_md=(
                "- TVP les plus fréquentes (**80 %**)\n"
                "- Thromboses artérielles : aorte abdominale et branches → thrombus blanc "
                "(riche en plaquettes) caractéristique\n"
                "- Complications neurologiques : **9,5 %** des patients "
                "(AVC ischémiques, thromboses veineuses cérébrales)"
            )),
            FicheRow(concept="◆ Score des 4 T (probabilité TIH)", detail_md=(
                "| Score | Probabilité |\n"
                "|-------|-------------|\n"
                "| **0-3** | Risque faible |\n"
                "| **4-5** | Risque intermédiaire (≥ 4 : poursuivre investigations) |\n"
                "| **6-8** | Risque élevé |"
            )),
            FicheRow(concept="◆ CAT devant suspicion de TIH", detail_md=(
                "- Confirmer la thrombopénie (tube citraté, contrôle sur lame, éliminer thromboagglutination)\n"
                "- Calculer le score T4\n"
                "- Éliminer une autre cause : infectieuse, médicamenteuse, CEC\n"
                "- **Test Elisa** : anticorps anti-PF4 (VPN > VPP)\n"
                "- Ou tests fonctionnels d'activation plaquettaire\n"
                "- Avis spécialisé pour ne pas arrêter l'héparine sans argument\n"
                "- ⚠ La décision d'arrêter l'héparine + remplacement ne peut attendre la biologie "
                "si forte suspicion"
            )),
            FicheRow(concept="◆ Conduite à tenir confirmée", detail_md=(
                "- Hospitalisation : rechercher complication thrombotique infraclinique\n"
                "- Déclaration obligatoire au centre régional de pharmacovigilance\n"
                "- Carte de TIH au patient\n"
                "- **Arrêt total de toute source d'héparine** (attention aux flushs héparinés des cathéters)\n"
                "- Alternatives anticoagulants :\n"
                "  - **Danaparoïde sodique** (Orgaran®) systématique\n"
                "  - Relais possible par AVK (petite dose), fondaparinux, AOD\n"
                "- Numération plaquettaire ≥ 1 fois/j jusqu'à normalisation\n"
                "- Normalisation des plaquettes après arrêt = meilleur argument diagnostique"
            )),
            FicheRow(concept="Prévention primaire", detail_md=(
                "- Durée d'utilisation des héparines la plus courte possible\n"
                "- Relais précoce par AOD ou AVK quand possible\n"
                "- Utilisation préférentielle des HBPM ou fondaparinux"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Risque de TIH = **thrombotique** (veineux 80 % > artériel 20 %), PAS hémorragique.\n"
                "- Délai typique : **J7-J10** (dès J1 si exposition récente).\n"
                "- Score T4 ≥ 4 → poursuivre les investigations ; ne pas attendre la biologie pour arrêter si suspicion forte."
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Accidents hémorragiques sous AVK", rows=[
            FicheRow(concept="◆ Épidémiologie", detail_md=(
                "- **600 000 patients** traités par AVK en France (1 % de la population)\n"
                "- AVK = **1ère cause iatrogène d'hospitalisation**\n"
                "- **13 %** des hospitalisations pour effets indésirables médicamenteux"
            )),
            FicheRow(concept="◆ CAT en cas de surdosage asymptomatique", detail_md=(
                "- Prise en charge le plus souvent ambulatoire\n"
                "- Fonction de l'INR mesuré et de l'INR cible\n"
                "- Rechercher la cause du surdosage (interactions, observance)\n"
                "- Contrôle INR le lendemain\n"
                "- Si persistance INR > fourchette : reconduire mesures\n"
                "- Surveillance ultérieure = celle de l'instauration"
            )),
            FicheRow(concept="◆ Définition d'une hémorragie grave", detail_md=(
                "- Hémorragie extériorisée non contrôlable par moyens usuels\n"
                "- Instabilité hémodynamique (collapsus)\n"
                "- Nécessité d'un geste hémostatique (ou chirurgical)\n"
                "- Nécessité de transfusion de culots globulaires\n"
                "- Localisation menaçant le pronostic vital ou fonctionnel\n"
                "- Si aucun critère : hémorragie non grave"
            )),
            FicheRow(concept="Moyens d'hémostase initiale", detail_md=(
                "- Compression mécanique : suture d'une plaie vasculaire\n"
                "- Application locale d'agent hémostatique (colle fibrine ou thrombine)\n"
                "- Injection locale de vasoconstricteurs (adrénaline) - ex : fibroscopie digestive\n"
                "- Embolisation par radiologie interventionnelle"
            )),
            FicheRow(concept="CAT hémorragie non grave", detail_md=(
                "- Prise en charge le plus souvent ambulatoire (si rapidement contrôlable)\n"
                "- **INR en urgence**\n"
                "- En cas de surdosage : mesures de correction\n"
                "- Cause du saignement recherchée"
            )),
            FicheRow(concept="◆ CAT hémorragie grave", detail_md=(
                "- **Hospitalisation**, AVK arrêtés\n"
                "- INR en urgence (traitement instauré sans attendre le résultat)\n"
                "- Antidotes :\n"
                "  - **Vitamine K** : délai d'action quelques heures\n"
                "  - **CCP/PPSB** (Kanokad®, Confidex®, Octaplex®) : action très rapide, courte durée\n"
                "    - Nécessite administration concomitante de vitamine K\n"
                "- Traitement de l'hémorragie massive :\n"
                "  - Correction hypovolémie\n"
                "  - Transfusion CGR\n"
                "  - Geste hémostatique chirurgical ou endoscopique\n"
                "- Surveillance biologique :\n"
                "  - INR **30 min** après administration CCP\n"
                "  - Si INR > 1,5 : nouvelle administration CCP\n"
                "  - INR **6-8 h** plus tard, puis 1 fois/j en période critique\n"
                "- Réévaluer l'indication des AVK ; relais héparine en attendant"
            )),
            FicheRow(concept="CAT chez le polytraumatisé", detail_md=(
                "- **INR en urgence**\n"
                "- Conduite selon gravité et nature du traumatisme\n"
                "- Traumatisme crânien :\n"
                "  - **Hospitalisation au moins 24 h**\n"
                "  - **Scanner cérébral en urgence**"
            )),
            FicheRow(concept="Prévention", detail_md=(
                "- Éducation thérapeutique\n"
                "- Attention aux interactions médicamenteuses\n"
                "- Automesure INR (peut diminuer le risque ; non remboursée sauf enfant/valve mécanique)"
            )),
        ]),
        SousPartie(lettre="D", titre="Accidents sous AOD", rows=[
            FicheRow(concept="◆ Principes de gestion", detail_md=(
                "- AOD ont une demi-vie courte : le meilleur antidote est le temps écoulé "
                "depuis la dernière prise\n"
                "- Dabigatran : antidote spécifique commercialisé (**idarucizumab/Praxbind®**)\n"
                "- Anti-Xa : antagonisés par **PPSB** ou **Feiba®** (PPSB + facteur VIII)\n"
                "  - Antidote anti-Xa attendu\n"
                "- Dosage du médicament possible pour tous les AOD (labos spécialisés)\n"
                "- En cas de saignement actif : CAT ne peut attendre le dosage"
            )),
            FicheRow(concept="◆ CAT (GIHP) - Encadré 22.1", detail_md=(
                "- À noter :\n"
                "  - Âge, poids\n"
                "  - Nom du médicament, dose, nombre de prises/j\n"
                "  - **Heure de la dernière prise**\n"
                "  - Indication\n"
                "- Prélever :\n"
                "  - **Créatinine** (Cockcroft)\n"
                "  - Dosage spécifique du médicament\n"
                "- Contacter le laboratoire d'hémostase\n"
                "- **Interrompre le traitement**"
            )),
            FicheRow(concept="", detail_md=(
                "- **Sulfate de protamine** = antidote de l'héparine.\n"
                "- **Vitamine K + PPSB/CCP** = antidotes des AVK.\n"
                "- **Idarucizumab (Praxbind®)** = antidote du dabigatran ; **PPSB ou Feiba®** pour les anti-Xa.\n"
                "- En cas d'AVC chez patient sous AVK : INR en urgence, scanner cérébral, hospitalisation."
            ), kind="a_retenir"),
        ]),
    ])

    # Synthèse - Tableaux
    tableaux = [
        TableauSynthese(titre="Comparaison des antiagrégants plaquettaires", markdown=(
            "| Molécule | Cible | Dose de charge | Entretien | Particularités |\n"
            "|----------|-------|----------------|-----------|----------------|\n"
            "| **Aspirine** | Cox-1 (irréversible) | 250-300 mg (SCA) | 75-160 mg/j | Effet 7-10 j |\n"
            "| **Clopidogrel** | P2Y12 (prodrogue) | 300-600 mg | 75 mg/j | CYP2C19 : 15-25 % résistants |\n"
            "| **Prasugrel** | P2Y12 | 60 mg | 10 mg/j | CI : ATCD AVC ; < 60 kg ou > 75 ans |\n"
            "| **Ticagrélor** | P2Y12 | 180 mg | 90 mg x 2/j | Dyspnée 18 % |"
        )),
        TableauSynthese(titre="Pharmacologie des héparines et héparinoïdes", markdown=(
            "| Critère | HNF | HBPM | Fondaparinux |\n"
            "|---------|-----|------|--------------|\n"
            "| **Mode action** | Antithrombine | Antithrombine | Antithrombine (anti-Xa pur) |\n"
            "| **Voie** | IV / SC | SC | SC ou IV |\n"
            "| **Demi-vie** | ≈ 1 h 30 | plus longue | longue |\n"
            "| **Nb prises/j** | continu ou 2-3/j | 1-2/j | 1/j |\n"
            "| **Élimination** | Protéines/endothélium/rein | Rénale | Rénale |\n"
            "| **CI IR sévère** | Utilisable (ClCr < 20-30) | CI si ClCr < 30 | CI si ClCr < 30 |\n"
            "| **Surveillance** | TCA (2-3x) ou anti-Xa (0,5-0,8) | Aucune si adaptée poids | Aucune |\n"
            "| **Antidote** | Sulfate de protamine | Partiel (protamine) | Aucun |"
        )),
        TableauSynthese(titre="AVK vs AOD - Avantages/Inconvénients", markdown=(
            "| Critère | AVK | AOD |\n"
            "|---------|-----|-----|\n"
            "| **Voie** | Orale | Orale |\n"
            "| **Délai d'action** | 3-5 j | ≈ 2 h |\n"
            "| **Relais héparine** | Nécessaire | Non |\n"
            "| **Surveillance** | INR (cible 2-3) | Aucune en routine |\n"
            "| **Interactions** | Nombreuses | Moins nombreuses |\n"
            "| **CI valves mécaniques** | Non (indiqué) | Oui (CI absolue) |\n"
            "| **CI RM serré** | Non | Oui |\n"
            "| **CI IR sévère** | OK (warfarine) | CI (ClCr < 30) |\n"
            "| **Antidote** | Vitamine K + PPSB | Dabigatran : Praxbind® ; Anti-Xa : PPSB/Feiba® |\n"
            "| **Tératogène** | Oui | À éviter |"
        )),
        TableauSynthese(titre="Propriétés des AOD", markdown=(
            "| Molécule | DCI | Cible | Élimination rénale | Nb prises/j |\n"
            "|----------|-----|-------|--------------------|-------------|\n"
            "| **Pradaxa®** | Dabigatran | Anti-IIa | 80 % | 2/j |\n"
            "| **Xarelto®** | Rivaroxaban | Anti-Xa | 33 % | 1/j (2/j début TVP/EP) |\n"
            "| **Eliquis®** | Apixaban | Anti-Xa | 25 % | 2/j |"
        )),
        TableauSynthese(titre="Gestion AVK pour acte programmé", markdown=(
            "| Situation | Conduite |\n"
            "|-----------|----------|\n"
            "| **Risque hémorragique faible** | Ne pas interrompre AVK (vérifier INR limite basse) |\n"
            "| **FA sans antécédent embolique, MTEV à risque modéré** | Arrêt AVK sans relais ; reprise 24-48 h |\n"
            "| **Valves mécaniques, FA avec antécédent embolique, MTEV haut risque** | "
            "Arrêt AVK + relais héparine curative |\n"
            "| **Objectif INR** | < 1,5 (général) ou < 1,2 (neurochirurgie) |"
        )),
        TableauSynthese(titre="Antidotes des antithrombotiques", markdown=(
            "| Médicament | Antidote | Délai d'action |\n"
            "|------------|----------|----------------|\n"
            "| **Héparine (HNF)** | Sulfate de protamine IV | Instantané |\n"
            "| **AVK** | Vitamine K + PPSB/CCP | Vit K : heures ; PPSB : rapide |\n"
            "| **Dabigatran** | Idarucizumab (Praxbind®) | Rapide |\n"
            "| **Anti-Xa (rivaroxaban, apixaban)** | PPSB ou Feiba® | Rapide |"
        )),
        TableauSynthese(titre="Caractéristiques pharmacologiques des AVK", markdown=(
            "| Molécule | Demi-vie (h) | Durée de l'effet (h) | Dosage cp (mg) |\n"
            "|----------|--------------|----------------------|-----------------|\n"
            "| **Warfarine** (Coumadine®) | 35-45 | 96-120 | 2 et 5 |\n"
            "| **Fluindione** (Préviscan®) | — | — | — |\n"
            "| **Acénocoumarol** (Sintrom®) | 8-9 | 36-48 | 4 |\n"
            "| **Mini-Sintrom®** | — | — | 1 |"
        )),
        TableauSynthese(titre="Influence des AVK et AOD sur les tests de coagulation", markdown=(
            "| Test | AVK | Dabigatran | Rivaroxaban | Apixaban |\n"
            "|------|-----|------------|-------------|----------|\n"
            "| **INR** | ↑↑↑ | ↑ | ↑ | Effet très limité |\n"
            "| **TCA (ratio)** | ↑ | ↑ | ↑ | Normal |\n"
            "| **TT (ratio)** | Effet très limité | ↑↑↑ | Aucune influence | Aucune influence |\n"
            "| **Anti-Xa (UI/mL)** | Effet très limité | Aucune influence | ↑↑ | ↑↑ |"
        )),
        TableauSynthese(titre="Posologies des AOD selon les indications", markdown=(
            "| Indication | Dabigatran | Rivaroxaban | Apixaban |\n"
            "|------------|------------|-------------|----------|\n"
            "| **Prévention TVP-EP en orthopédie** | 110 mg x 2/j ou 75 mg x 2/j | 10 mg/j | 2,5 mg x 2/j |\n"
            "| **FA non valvulaire** | 110 ou 150 mg x 2/j (adapter rénal/âge) | 15 ou 20 mg/j (adapter rénal/âge) | 2,5 ou 5 mg x 2/j (rénal/âge/poids) |\n"
            "| **TVP-EP curatif** | 110 ou 150 mg x 2/j (après 5-7 j héparine) | 15 mg x 2/j x 21 j puis 20 mg/j | 10 mg x 2/j x 7 j puis 5 mg x 2/j |\n"
            "| **Post-SCA** | Pas d'indication | 2,5 mg x 2/j | Pas d'indication |"
        )),
        TableauSynthese(titre="Composantes du score 4T pour la TIH", markdown=(
            "| Critère | 0 point | 1 point | 2 points |\n"
            "|---------|---------|---------|----------|\n"
            "| **Thrombopénie** | ↓ < 30 % ou plaquettes < 10 G/L | ↓ 30-50 % ou plaquettes 10-20 G/L | ↓ > 50 % ou plaquettes 20-100 G/L |\n"
            "| **Timing** | Autre que 1 et 2 | ↓ > 10 j ou 24 h si exposition récente (30-100 j) | ↓ 5-10 j ou 24 h si exposition récente (30 j) |\n"
            "| **Thrombose** | Pas de thrombose | Extension/suspicion thrombose ou érythème cutané | Nouvelle thrombose ou réaction systémique ou nécrose cutanée |\n"
            "| **Autres causes** | Certaines | Possibles | Aucune possible |"
        )),
        TableauSynthese(titre="CAT en cas de surdosage AVK selon l'INR", markdown=(
            "| INR mesuré | INR cible 2,5 (fenêtre 2-3) | INR cible 3 (2,5-3,5 ou 3-4,5) |\n"
            "|-----------|-----------------------------|--------------------------------|\n"
            "| **INR < 4** | Pas de saut de prise, pas de vitamine K, adaptation posologie | — |\n"
            "| **4 ≤ INR < 6** | Saut d'une prise, pas de vitamine K, adaptation à la reprise | Pas de saut de prise, pas de vit K, adaptation posologie |\n"
            "| **6 ≤ INR < 10** | Arrêt AVK + 1-2 mg vitamine K per os | Saut d'une prise ; avis spécialisé pour discuter vit K 1-2 mg PO |\n"
            "| **INR > 10** | Arrêt AVK + 5 mg vit K per os (½ ampoule buvable adulte) | Avis spécialisé sans délai ou hospitalisation recommandée |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Effet aspirine sur la plaquette | **7-10 jours** | Inhibition irréversible Cox-1 |\n"
        "| Dose aspirine SCA (charge) | **250-300 mg** | |\n"
        "| Dose entretien aspirine | **75-160 mg/j** | Coronaropathie, AVC |\n"
        "| Dose anti-inflammatoire aspirine | **500 mg à 2 g/j** | |\n"
        "| Patients résistants au clopidogrel | **15-25 %** | CYP2C19 |\n"
        "| Inhibition plaquettaire prasugrel/ticagrélor | **70-80 %** | vs 40-50 % clopidogrel |\n"
        "| Dose de charge clopidogrel | **300-600 mg** | |\n"
        "| Dose entretien clopidogrel | **75 mg/j** | |\n"
        "| Dose de charge prasugrel | **60 mg** | |\n"
        "| Dose entretien prasugrel | **10 mg/j** | |\n"
        "| Dose de charge ticagrélor | **180 mg** | |\n"
        "| Dose entretien ticagrélor | **90 mg x 2/j** | |\n"
        "| Prasugrel CI relatives | **< 60 kg** ou **> 75 ans** | |\n"
        "| Ticagrélor - dyspnée | **18 %** des patients | |\n"
        "| Délai arrêt avant chirurgie majeure (aspirine) | **5 jours** | |\n"
        "| Délai retard acte invasif post-stent | **3-6 mois** | |\n"
        "| Durée bithérapie AAP post-SCA | **12 mois** (1-12) | |\n"
        "| Demi-vie HNF | **≈ 1 h 30** | |\n"
        "| Bolus HNF curatif | **70-80 UI/kg** (≈ 5 000 UI pour 70 kg) | |\n"
        "| Entretien HNF curatif | **18 UI/kg/h** (≈ 500 UI/kg/j) | |\n"
        "| Posologie HBPM curative | **100 UI anti-Xa/kg** | |\n"
        "| TCA cible HNF | **2 à 3 fois le témoin** | |\n"
        "| Activité anti-Xa cible HNF | **0,5 - 0,8 UI/mL** | |\n"
        "| 1er TCA | **5e heure** | |\n"
        "| ClCr seuil HNF | **< 20-30 mL/min** | HNF utilisable |\n"
        "| ClCr seuil HBPM/fondaparinux | **< 30 mL/min** | Contre-indication |\n"
        "| Délai d'action AVK | **3-5 jours** | |\n"
        "| Délai effet AVK | **4-6 jours** | |\n"
        "| INR normal (sans traitement) | **1** | |\n"
        "| INR cible (la plupart des indications) | **2-3** | |\n"
        "| Patient équilibré | **≥ 70 %** INR dans cible | |\n"
        "| Surveillance INR au long cours | **min. 1 fois/mois** | |\n"
        "| Chevauchement héparine-AVK | **4-5 jours** | + 2 INR efficaces à 24 h |\n"
        "| Doses initiales warfarine | **5 mg/j J0-J2** | |\n"
        "| 1er INR de contrôle warfarine | **J4 matin** | |\n"
        "| Patients AVK France | **600 000** (1 % population) | |\n"
        "| AVK et hospitalisations iatrogènes | **13 %** | 1ère cause iatrogène |\n"
        "| Effet AOD | **≈ 2 heures** | Après 1re prise |\n"
        "| Élimination rénale dabigatran | **80 %** | |\n"
        "| Élimination rénale rivaroxaban | **33 %** | |\n"
        "| Élimination rénale apixaban | **25 %** | |\n"
        "| ClCr CI AOD | **< 25-30 mL/min** | |\n"
        "| Arrêt AOD avant bilan APL | **2-3 jours** | LA/DRVVT |\n"
        "| Fenêtre fibrinolyse IDM | **< 6-12 heures** | Si angioplastie impossible |\n"
        "| Fenêtre fibrinolyse AVC | **< 4 h 30** | Après exclusion hémorragique |\n"
        "| Risque hémorragie intracérébrale (fibrinolyse) | **0,7-2 %** | |\n"
        "| Effet fibrinolytique sur tests | **≈ 24 h** | TCA/TP perturbés |\n"
        "| HTA CI fibrinolyse | **> 200 mmHg** | |\n"
        "| Hémorragies sous héparine curative | **1-4 %** | |\n"
        "| Hémorragies sous héparine préventive | **1-2 %** | |\n"
        "| Plaquettes seuil TIH | **< 100 000/mm³ (100 G/L)** | |\n"
        "| Chute relative plaquettes TIH | **30-50 %** | Sur 2 numérations |\n"
        "| Délai typique TIH | **J7-J10** (5-8 j) | |\n"
        "| Incidence TIH | **0,05 à 3 %** | |\n"
        "| Thromboses veineuses si TIH compliquée | **80 %** | |\n"
        "| Thromboses artérielles si TIH compliquée | **20 %** | |\n"
        "| CIVD si TIH | **10-20 %** | |\n"
        "| Complications neurologiques TIH | **9,5 %** | |\n"
        "| Score 4T - risque faible | **0-3** | |\n"
        "| Score 4T - risque intermédiaire | **4-5** | |\n"
        "| Score 4T - risque élevé | **6-8** | |\n"
        "| Objectif INR pré-opératoire | **< 1,5** | < 1,2 si neurochirurgie |\n"
        "| INR à 30 min post-CCP | **≤ 1,5** | Sinon réadministration |\n"
        "| Hospitalisation post-AVK + trauma crânien | **min. 24 h** | + scanner cérébral |"
    ))

    points_cles = [
        "**Aspirine** = AAP de référence : Cox-1 **irréversible** 7-10 j ; aucun test biologique fiable",
        "**P2Y12** (clopidogrel, prasugrel, ticagrélor) : plus puissants que aspirine ; prasugrel CI si **ATCD AVC**",
        "Post-SCA/stent : bithérapie AAP **12 mois** ; pas d'acte invasif **3-6 mois** post-stent",
        "**HBPM/fondaparinux** CI si **ClCr < 30** ; **HNF** = seule option en IR sévère",
        "Surveillance **HNF** : TCA **2-3x** témoin ou anti-Xa **0,5-0,8** ; HBPM sans bio si poids adapté",
        "**AVK** : INR cible **2-3** ; relais héparine **4-5 j** chevauchement + 2 INR efficaces à 24 h",
        "**AVK** = **1ère cause iatrogène** d'hospitalisation (13 %) ; antidotes = **vit K + PPSB**",
        "**AOD** : effet 2 h, pas de bio ; CI si **valves mécaniques, RM serré, ClCr < 30**",
        "**Fibrinolyse** : IDM **< 6-12 h**, AVC **< 4 h 30**, EP grave ; hémorragie cérébrale **0,7-2 %**",
        "**TIH II** : risque **thrombotique** (PAS hémorragique), **J7-J10**, plaquettes < 100 G/L ; arrêt héparine",
    ]

    fiche_eclair_md = (
        "**Aspirine** : Cox-1 irréversible 7-10 j. SCA 250-300 mg, entretien 75-160 mg/j. Pas de bio.\n\n"
        "**P2Y12** : clopidogrel (CYP2C19, 15-25 % résistants), prasugrel (CI ATCD AVC, < 60 kg, > 75 ans), ticagrélor (dyspnée 18 %). Bithérapie post-SCA ≈ 12 mois.\n\n"
        "**Péri-op AAP** : pas d'acte invasif 3-6 mois post-stent. Arrêt aspirine 5 j avant si risque élevé.\n\n"
        "**HNF** : bolus 70-80 UI/kg + 18 UI/kg/h. TCA 2-3x ou anti-Xa 0,5-0,8 à H5. Seule option si ClCr < 30. Antidote protamine.\n\n"
        "**HBPM** : 100 UI anti-Xa/kg SC. CI si ClCr < 30.\n\n"
        "**AVK** : inhibent II-VII-IX-X + protéines C/S, effet 3-5 j. INR cible 2-3. Warfarine référence ; fluindione déconseillée 2017. Tératogène. 1ère cause iatrogène (13 %). Antidotes vit K + PPSB.\n\n"
        "**Relais héparine-AVK** : chevauchement 4-5 j + 2 INR efficaces à 24 h.\n\n"
        "**AOD** : effet 2 h, pas de bio. Dabigatran (anti-IIa, 80 % rénal), rivaroxaban (anti-Xa, 33 %), apixaban (anti-Xa, 25 %). CI : valves mécaniques, RM serré, ClCr < 30. Antidote dabigatran = Praxbind®.\n\n"
        "**Thrombolytiques** : altéplase, ténectéplase. IDM < 6-12 h, AVC < 4 h 30, EP grave. Hémorragie cérébrale 0,7-2 %.\n\n"
        "**TIH II** : immunoallergique J7-J10. Plaquettes < 100 G/L. Risque thrombotique (TVP 80 %). Score 4T ≥ 4. Arrêt héparine + danaparoïde.\n\n"
        "**Hémorragie grave AVK** : arrêt + vit K + PPSB. INR à 30 min, 6-8 h. Trauma crânien : scanner + hospi 24 h."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 330 - Prescription et surveillance des classes de médicaments",
        annee="2025-2026",
        item="Item 330",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 330",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-330_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

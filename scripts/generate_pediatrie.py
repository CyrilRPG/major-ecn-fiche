"""Génère la fiche exhaustive de Pédiatrie à partir du PDF source."""

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
        PlanPartie(numero="I", titre="Fièvre aiguë de l'enfant", sous_parties=[
            PlanSousPartie(lettre="A", titre="Tableau clinique et signes de gravité"),
            PlanSousPartie(lettre="B", titre="Examens complémentaires"),
            PlanSousPartie(lettre="C", titre="Prise en charge"),
        ]),
        PlanPartie(numero="II", titre="Diarrhée aiguë de l'enfant", sous_parties=[
            PlanSousPartie(lettre="A", titre="Tableau clinique et déshydratation"),
            PlanSousPartie(lettre="B", titre="Étiologies"),
            PlanSousPartie(lettre="C", titre="Examens complémentaires"),
            PlanSousPartie(lettre="D", titre="Prise en charge et réhydratation"),
            PlanSousPartie(lettre="E", titre="Complications et prévention"),
        ]),
        PlanPartie(numero="III", titre="Coqueluche", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et épidémiologie"),
            PlanSousPartie(lettre="B", titre="Tableau clinique"),
            PlanSousPartie(lettre="C", titre="Complications et examens complémentaires"),
            PlanSousPartie(lettre="D", titre="Prise en charge et vaccination"),
        ]),
        PlanPartie(numero="IV", titre="Bronchiolite aiguë du nourrisson", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et épidémiologie"),
            PlanSousPartie(lettre="B", titre="Tableau clinique et critères de gravité"),
            PlanSousPartie(lettre="C", titre="Examens complémentaires"),
            PlanSousPartie(lettre="D", titre="Prise en charge"),
            PlanSousPartie(lettre="E", titre="Suivi et prévention VRS"),
        ]),
        PlanPartie(numero="V", titre="Convulsions de l'enfant", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et tableau clinique"),
            PlanSousPartie(lettre="B", titre="Examens complémentaires et étiologies"),
            PlanSousPartie(lettre="C", titre="Crises fébriles : diagnostic et prise en charge"),
        ]),
        PlanPartie(numero="VI", titre="Suivi médical, RGO et pathologies spécifiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Suivi médical de l'enfant et carnet de santé"),
            PlanSousPartie(lettre="B", titre="RGO de l'enfant"),
            PlanSousPartie(lettre="C", titre="Maladie cœliaque"),
            PlanSousPartie(lettre="D", titre="Maltraitance et syndrome du bébé secoué"),
        ]),
        PlanPartie(numero="VII", titre="Éruptions fébriles de l'enfant", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et démarche diagnostique"),
            PlanSousPartie(lettre="B", titre="Scarlatine et rougeole"),
            PlanSousPartie(lettre="C", titre="Rubéole, mégalérythème épidémique et exanthème subit"),
        ]),
    ]

    # ── PARTIE I : FIÈVRE AIGUË DE L'ENFANT ──
    partie_i = Partie(numero="I", titre="Fièvre aiguë de l'enfant", sous_parties=[
        SousPartie(lettre="A", titre="Tableau clinique et signes de gravité", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Fièvre aiguë** : augmentation TC > **38°C** depuis moins de **5 jours** chez le nourrisson, "
                "**7 jours** chez l'enfant plus âgé\n"
                "- Chez enfant normalement couvert, exposé à TC ambiante, en l'absence d'activité physique intense"
            )),
            FicheRow(concept="◆ Diagnostic positif : prise de température", detail_md=(
                "| Méthode | Précision | Correction |\n"
                "|---------|----------|------------|\n"
                "| **Rectale** (référence) | Or standard | Aucune |\n"
                "| Axillaire | Sous-estimation fréquente | **+0,5°C** |\n"
                "| Buccale | Sous-estimation fréquente | **+0,4°C** |\n"
                "| Tympanique (infrarouge) | Imprécis | Non fiable |"
            )),
            FicheRow(concept="Signes de gravité", detail_md=(
                "- **Fièvre > 40°C**\n"
                "- **Signes hémodynamiques** : tachycardie/bradycardie inexpliquée (avant 1 an), "
                "hypotension, TRC allongé, teint gris, marbrures, froideur des extrémités, oligurie\n"
                "- **Signes neurologiques** : somnolence, léthargie, hyporéactivité, Glasgow < 14, "
                "mauvais contact oculaire, signes d'irritation méningée, convulsion, fontanelle bombante\n"
                "- **AEG**, polypnée > 40-60/min, hypoxie, signes de lutte\n"
                "- Déshydratation, pâleur, cris inhabituels\n"
                "- **Purpura extensif**, nécrotique, diamètre > 3 mm (à rechercher sur enfant totalement dévêtu)\n"
                "- Anorexie, vomissements verts"
            )),
            FicheRow(concept="", detail_md=(
                "- **Purpura fébrile** extensif/nécrotique > 3 mm = **urgence vitale** (méningocoque)\n"
                "- Rechercher sur enfant **totalement dévêtu** +++\n"
                "- Nourrisson < 3 mois fébrile = **hospitalisation systématique**"
            ), kind="a_retenir"),
            FicheRow(concept="Complications de la fièvre", detail_md=(
                "- **Crises fébriles** (2-5%) : crise convulsive occasionnelle en climat fébrile, "
                "enfant 1-3 ans, DPM normal, hors atteinte SNC\n"
                "- **Déshydratation aiguë**\n"
                "- **Syndrome d'hyperthermie majeure** : TC > 40,5°C + collapsus + atteintes multi-viscérales"
            )),
            FicheRow(concept="Terrain à risque", detail_md=(
                "- **Nourrisson < 3 mois** +++\n"
                "- Immunodéprimé, drépanocytose, maladie systémique, affection chronique"
            )),
            FicheRow(concept="◆ Enquête étiologique", detail_md=(
                "- **Anamnèse** : âge, ATCD infections sévères, FDR infection néonatale, "
                "terrain (drépanocytose, ID), statut vaccinal, contage infectieux, voyage tropical, "
                "ATB récent\n"
                "- **Caractéristiques fièvre** : début brutal/progressif, signes d'appel clinique, "
                "nombre total jours de fièvre, réponse aux antipyrétiques\n"
                "- **Examen physique** : complet avec recherche signes de gravité et orientation étiologique"
            )),
        ]),
        SousPartie(lettre="B", titre="Examens complémentaires", rows=[
            FicheRow(concept="Principe fondamental", detail_md=(
                "- **Aucun examen** en l'absence de signes de gravité +++\n"
                "- Examens uniquement si signes de gravité ou terrain à risque"
            )),
            FicheRow(concept="Bilan si signes de gravité", detail_md=(
                "| Examen | Indication |\n"
                "|--------|------------|\n"
                "| **Bilan inflammatoire** (NFS, CRP) | Systématique |\n"
                "| Examens bactériologiques | Selon orientation |\n"
                "| **BU +/- ECBU** | Systématique si < 1 mois |\n"
                "| **Hémocultures** | Systématique si < 6 semaines ou sepsis |\n"
                "| **PL** | Systématique si < 6 semaines ou syndrome méningé |\n"
                "| RXT face | Si signes respiratoires |"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ PL **systématique** si âge < 6 semaines\n"
                "- Hémocultures **systématiques** si âge < 6 semaines ou signes de sepsis\n"
                "- BU **systématique** si âge < 1 mois"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Prise en charge", rows=[
            FicheRow(concept="Orientation", detail_md=(
                "- **Ambulatoire** +++ dans la majorité des cas\n"
                "- **Hospitalisation** si signes de gravité, terrain à risque, complications"
            )),
            FicheRow(concept="◆ Signes d'infection potentiellement sévère", detail_md=(
                "- Troubles de la vigilance et/ou du tonus\n"
                "- Troubles du comportement : anomalies du cri, irritabilité\n"
                "- Troubles hémodynamiques : tachycardie, TRC > 3 s, pouls mal perçus\n"
                "- Troubles de la coloration : pâleur, teint gris, cyanose\n"
                "- Signes de détresse respiratoire : polypnée, signes de lutte\n"
                "- Signes de déshydratation aiguë\n"
                "- Douleur à la mobilisation (infection ostéo-articulaire)\n"
                "- Purpura, distension abdominale"
            )),
            FicheRow(concept="PEC symptomatique de la fièvre", detail_md=(
                "- **Objectif** = **confort de l'enfant** (pas la normalisation de la TC)\n"
                "- **Méthodes physiques** : donner à boire souvent, ne pas surcouvrir, "
                "pièce à environ 19°C\n"
                "- **Paracétamol** en 1re intention : **60 mg/kg/j** en 4 prises, monothérapie\n"
                "- Si paracétamol inefficace :\n"
                "  - **Ibuprofène** 20-30 mg/kg/j en 3-4 prises (après **3 mois**)\n"
                "  - Alterner les 2 molécules"
            )),
            FicheRow(concept="", detail_md=(
                "- Paracétamol = **60 mg/kg/j** en 4 prises (monothérapie 1re intention)\n"
                "- Ibuprofène : uniquement après **3 mois** de vie"
            ), kind="a_retenir"),
            FicheRow(concept="Éducation parentale", detail_md=(
                "- Traitement pendant toute la durée de la fièvre\n"
                "- Prise de TC régulière\n"
                "- **Signes de reconsultation** (à écrire sur l'ordonnance) :\n"
                "  - Fièvre > 40°C malgré traitement\n"
                "  - Changement de comportement, pleurs inconsolables\n"
                "  - Enfant difficile à réveiller\n"
                "  - Anomalies du teint, troubles de conscience, détresse respiratoire"
            )),
        ]),
    ])

    # ── PARTIE II : DIARRHÉE AIGUË DE L'ENFANT ──
    partie_ii = Partie(numero="II", titre="Diarrhée aiguë de l'enfant", sous_parties=[
        SousPartie(lettre="A", titre="Tableau clinique et déshydratation", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Diarrhée aiguë** : émission brutale, < **7 jours** (jusqu'à 14 j), "
                "de selles liquides > **3/jour**\n"
                "- Déterminer la perte de poids (en % du poids habituel)"
            )),
            FicheRow(concept="◆ Évaluation de la déshydratation", detail_md=(
                "| Sévérité | Perte de poids | Attitude |\n"
                "|---------|---------------|----------|\n"
                "| **Légère** | < 5% | Ambulatoire + SRO |\n"
                "| **Modérée** | 5-10% | Essai SRO, hospitalisation si échec |\n"
                "| **Sévère** | > 10% | **Hospitalisation systématique** |"
            )),
            FicheRow(concept="Signes de déshydratation", detail_md=(
                "- **Cernes péri-oculaires**, fontanelle déprimée (avant 6 mois), pli cutané persistant\n"
                "- Sécheresse des muqueuses, soif, absence de larmes\n"
                "- Troubles de conscience ou du tonus\n"
                "- **Troubles hémodynamiques** : tachycardie, TRC > 3 s, extrémités froides/marbrures, "
                "pouls mal perçus, hypotension"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Déshydratation > 10% = **hospitalisation systématique**\n"
                "- Fontanelle déprimée = signe précoce de déshydratation chez le nourrisson < 6 mois"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Étiologies", rows=[
            FicheRow(concept="◆ Étiologies virales (70%)", detail_md=(
                "- **Rotavirus** ++ : âge < 5 ans, épidémie automno-hivernale\n"
                "- **Norovirus** : tout âge, épidémies familiales/en collectivité\n"
                "- Adénovirus, entérovirus"
            )),
            FicheRow(concept="Autres étiologies", detail_md=(
                "- Diarrhées bactériennes +/- liées à TIAC\n"
                "- Accélération du transit liée à affection extra-digestive (ORL, urinaire)\n"
                "- Cause chirurgicale (appendicite)\n"
                "- **APLV** (allergie aux protéines de lait de vache)\n"
                "- Diarrhée sous ATB (Augmentin)"
            )),
            FicheRow(concept="Causes de déshydratation (hors digestif)", detail_md=(
                "- Pertes extra-digestives accrues de Na/eau :\n"
                "  - Diabète sucré, diabète insipide\n"
                "  - Insuffisance surrénalienne"
            )),
        ]),
        SousPartie(lettre="C", titre="Examens complémentaires", rows=[
            FicheRow(concept="◆ Stratégie diagnostique", detail_md=(
                "- Diarrhée sans ou avec déshydratation modérée (< 5%) : **AUCUN examen**\n"
                "- Diarrhée avec déshydratation sévère (> 10%) ou échec réhydratation orale :\n"
                "  - **Ionogramme sanguin, urée, créatinine**"
            )),
            FicheRow(concept="Examens optionnels", detail_md=(
                "- Examen virologique des selles : pas utile en pratique\n"
                "- **Coproculture** : si suspicion diarrhée bactérienne (sanglante, fièvre élevée, retour de voyage)\n"
                "- Parasitologie des selles : si séjour zone endémique amibiase\n"
                "- Frottis goutte épaisse : si fièvre + retour de voyage"
            )),
        ]),
        SousPartie(lettre="D", titre="Prise en charge et réhydratation", rows=[
            FicheRow(concept="Orientation", detail_md=(
                "- **Ambulatoire** ++ avec consignes de surveillance\n"
                "- **Critères d'hospitalisation** :\n"
                "  - Troubles hémodynamiques ou neurologiques\n"
                "  - Déshydratation > 10%\n"
                "  - Vomissements incoercibles, impossibilité boire le SRO\n"
                "  - Terrain à risque\n"
                "  - Capacité de surveillance par entourage non assurée"
            )),
            FicheRow(concept="Réhydratation par SRO", detail_md=(
                "| Déshydratation | Prise en charge |\n"
                "|---------------|------------------|\n"
                "| < 5% | **Ambulatoire** : SRO + consignes surveillance |\n"
                "| 5-10% | Essai SRO, si échec → hospitalisation |\n"
                "| > 10% | **Hospitalisation** : remplissage NaCl 0,9% 20 mL/kg IV si troubles hémodynamiques, "
                "puis réhydratation IV 100-150 mL/kg/24h |"
            )),
            FicheRow(concept="", detail_md=(
                "- Le **SRO** est le traitement de **première intention** à tout âge\n"
                "- Remplissage vasculaire par **sérum physiologique 20 mL/kg** en débit libre si troubles hémodynamiques"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Renutrition précoce", detail_md=(
                "- **Allaitement maternel** : pas d'interruption, alterner tétées et SRO\n"
                "- **Allaitement artificiel** : reprise après 4-6h de réhydratation exclusive :\n"
                "  - Préparation standard si diarrhée peu sévère\n"
                "  - Préparation **sans lactose** 1-2 semaines si diarrhée sévère/traînante (non systématique)\n"
                "- **Alimentation diversifiée** : aucun régime particulier à prescrire"
            )),
            FicheRow(concept="Traitement médicamenteux", detail_md=(
                "- Antidiarrhéiques : toujours associés au SRO si prescrits\n"
                "  - Racécadotril (Tiorfan), lactobacille LB (Lactéol)\n"
                "  - **CI lopéramide (Imodium)** et Saccharomyces boulardii (Ultra-levure) avant **2 ans**\n"
                "- **ATB** : pas d'indication si diarrhée aiguë liquidienne"
            )),
            FicheRow(concept="", detail_md=(
                "- **Lopéramide** (Imodium) = **contre-indiqué avant 2 ans**\n"
                "- Pas d'ATB dans la diarrhée aiguë liquidienne"
            ), kind="piege"),
        ]),
        SousPartie(lettre="E", titre="Complications et prévention", rows=[
            FicheRow(concept="Complications", detail_md=(
                "- **Diarrhée traînante** (> 5 jours après reprise alimentation) : régime sans lactose 1-2 semaines\n"
                "- **Complications neurologiques** : convulsions, hématome sous-dural, thromboses veineuses cérébrales\n"
                "- **Complications rénales** : IRF, nécrose corticale, thromboses veines rénales"
            )),
            FicheRow(concept="Prévention", detail_md=(
                "- **Hygiène des mains** +++\n"
                "- Restriction fréquentation collectivité à la phase aiguë\n"
                "- Isolement en milieu hospitalier\n"
                "- **Vaccination contre Rotavirus** : vaccin vivant oral, entre **6 et 12 semaines**"
            )),
            FicheRow(concept="Surveillance ambulatoire", detail_md=(
                "- Reconsulter si : enfant apathique, hypotonie, refus de boire, "
                "diarrhée profuse, vomissements incoercibles, perte de poids, "
                "fièvre élevée, sang dans les selles"
            )),
        ]),
    ])

    # ── PARTIE III : COQUELUCHE ──
    partie_iii = Partie(numero="III", titre="Coqueluche", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et épidémiologie", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Infection bactérienne liée à **Bordetella pertussis** (bacille de Bordet-Gengou), BGN\n"
                "- +/- Bordetella parapertussis\n"
                "- **Contamination inter-humaine** par voie respiratoire lors de la toux\n"
                "- Contamination par **adultes de l'entourage proche** ++\n"
                "- Durée d'incubation : **10 jours** (7-21)\n"
                "- Contagiosité peut durer **3 semaines** après début des symptômes"
            )),
            FicheRow(concept="Sujets à risque", detail_md=(
                "- **Jeunes nourrissons** avant âge de protection vaccinale\n"
                "- Adolescents et adultes ayant perdu la protection vaccinale (5 ans) : "
                "formes pauci-symptomatiques"
            )),
        ]),
        SousPartie(lettre="B", titre="Tableau clinique", rows=[
            FicheRow(concept="Coqueluche typique du grand enfant non vacciné", detail_md=(
                "| Phase | Durée | Caractéristiques |\n"
                "|-------|------|------------------|\n"
                "| **Incubation** | ~10 j (7-21) | Cliniquement silencieuse |\n"
                "| **Catarrhale** | 1-2 semaines | Fièvre absente/modérée < 38,5°C, toux banale + rhinorrhée, "
                "toux devenant tenace et caractéristique en quintes |\n"
                "| **État** (contagiosité max) | 2-6 semaines | **Quintes** : accès répétitifs et violents de toux "
                "sans inspiration efficace, congestion visage/cyanose, reprise = **chant du coq** |\n"
                "| **Convalescence** | Plusieurs mois | Toux non quinteuse, asthénie |"
            )),
            FicheRow(concept="Caractéristiques des quintes", detail_md=(
                "- Déclenchées par déglutition, cris, efforts du pharynx\n"
                "- Caractère **émétisant** évocateur chez enfant/adulte\n"
                "- Épuisantes, jusqu'à **50 quintes/jour**\n"
                "- Caractère **diurne et nocturne** évocateur"
            )),
            FicheRow(concept="Coqueluche du nourrisson", detail_md=(
                "- À évoquer devant toux quinteuse chez tout nourrisson non complètement immunisé\n"
                "- Phase d'invasion plus courte (7 j)\n"
                "- **Signes de gravité** (++ avant 3 mois) :\n"
                "  - Respiratoires : quintes asphyxiantes, cyanosantes, **apnées** +/- cyanose\n"
                "  - CV : bradycardie, tachycardie\n"
                "  - Neurologiques : malaise grave, troubles de conscience, convulsions\n"
                "  - Digestifs : vomissements (dénutrition, déshydratation)\n"
                "- **Absence du chant du coq** chez le nourrisson"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Chez le nourrisson : **pas de chant du coq** (spécificité trompeuse)\n"
                "- Penser à la coqueluche devant toute toux > 1 semaine sans cause évidente"
            ), kind="piege"),
            FicheRow(concept="Coqueluche de l'adolescent/adulte", detail_md=(
                "- À évoquer devant toux sans cause évidente, persistante/s'aggravant > 1 semaine\n"
                "- Notion de contage, incubation longue\n"
                "- Caractère coquelucheux\n"
                "- **Source de contamination des nourrissons** +++"
            )),
        ]),
        SousPartie(lettre="C", titre="Complications et examens complémentaires", rows=[
            FicheRow(concept="Complications", detail_md=(
                "- **Mécaniques** : fractures de côtes, emphysème médiastinal, PNO, "
                "hémorragies sous-conjonctivales, hernie, syndrome de Mallory-Weiss\n"
                "- **Infectieuses** : otites, sinusites, pneumonies à Bordetella/surinfection\n"
                "- **Convulsions** (3%), anoxie\n"
                "- **Encéphalopathie coquelucheuse** : état de mal convulsif, "
                "troubles moteurs (hémiplégie, paraplégie, ataxie), "
                "troubles sensoriels (cécité, surdité)\n"
                "  - Pronostic : **1/3 décès, 1/3 séquelles, 1/3 guérison**"
            )),
            FicheRow(concept="", detail_md=(
                "- Encéphalopathie coquelucheuse : **1/3 décès, 1/3 séquelles, 1/3 guérison**"
            ), kind="a_retenir"),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- **NFS** : +/- hyperlymphocytose évocatrice\n"
                "- **RXT** : normale ou syndrome bronchique (éliminer diagnostic différentiel)\n"
                "- **PCR coqueluche** (Se 90%, Sp 99%) : sur écouvillonnage naso-pharyngé, "
                "résultat en 24h\n"
                "- Examens sérologiques : utiles tardivement"
            )),
        ]),
        SousPartie(lettre="D", titre="Prise en charge et vaccination", rows=[
            FicheRow(concept="Orientation", detail_md=(
                "- **Hospitalisation** si :\n"
                "  - Âge < **3 mois** +++\n"
                "  - Signes cliniques de gravité, apnées, difficultés alimentaires\n"
                "  - Forme compliquée\n"
                "- **Mesures hospitalières** : isolement respiratoire (gouttelettes), "
                "scope cardio-respiratoire, aspirations, position proclive, fractionnement repas\n"
                "- **Ambulatoire** : éviction collectivité pendant 5 j, information parents"
            )),
            FicheRow(concept="Antibiothérapie", detail_md=(
                "- **But** : diminuer la contagiosité, autoriser retour en collectivité après 5 jours "
                "(3 si azithromycine)\n"
                "- **1re intention** : macrolides :\n"
                "  - **Azithromycine** pendant **3 jours** (max 500 mg/j)\n"
                "  - Ou **Clarithromycine** pendant **7 jours**\n"
                "- **2e intention** (allergie macrolides) : Cotrimoxazole **14 jours**"
            )),
            FicheRow(concept="◆ Conduite dans l'entourage", detail_md=(
                "- Mise à jour des vaccinations de la population exposée\n"
                "- **ATBprophylaxie** pour contacts proches, femmes enceintes, nourrissons :\n"
                "  - Toute personne non/mal vaccinée\n"
                "  - Vaccination remontant > 5 ans\n"
                "  - Macrolides mêmes modalités\n"
                "  - Inutile si contage > 21 jours"
            )),
            FicheRow(concept="Vaccination coqueluche", detail_md=(
                "| Recommandation | Calendrier |\n"
                "|----------------|------------|\n"
                "| **Primo-vaccination** | **2 mois** et **4 mois** |\n"
                "| 1er rappel | **11 mois** |\n"
                "| Rappel | **6 ans** puis **11-13 ans** |\n"
                "| Rappel adulte jeune | **25 ans** |\n"
                "| **Cocooning** : femmes enceintes | **Chaque grossesse** |\n"
                "| Foyer lors grossesse | Membres du foyer |\n"
                "| Professionnels | Contact NN et nourrissons < 6 mois |"
            )),
            FicheRow(concept="", detail_md=(
                "- Vaccination/maladie confèrent protection de **5 ans** seulement\n"
                "- **Stratégie cocooning** : vacciner l'entourage du nourrisson, "
                "femme enceinte à chaque grossesse"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE IV : BRONCHIOLITE AIGUË DU NOURRISSON ──
    partie_iv = Partie(numero="IV", titre="Bronchiolite aiguë du nourrisson", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et épidémiologie", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Bronchiolite** : ensemble des bronchopathies obstructives du nourrisson\n"
                "- Origine infectieuse ++ :\n"
                "  - **VRS** (60-70%) : transmission par sécrétions contaminées/mains/matériel souillé, "
                "incubation 2-8 jours\n"
                "  - Rhinovirus (20%)\n"
                "  - Parainfluenzae, influenzae (grippe), métapneumovirus, adénovirus"
            )),
            FicheRow(concept="Épidémiologie", detail_md=(
                "- ++ Nourrissons âgés de **2-8 mois**\n"
                "- Pic épidémique **hivernal**\n"
                "- Contamination inter-humaine\n"
                "- Répétition épisodes > 3 = **asthme du nourrisson**"
            )),
        ]),
        SousPartie(lettre="B", titre="Tableau clinique et critères de gravité", rows=[
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- Début par **rhino-pharyngite** aiguë\n"
                "- **Toux**, augmentation FR\n"
                "- **Signes de lutte respiratoire** : tirage intercostal, balancement thoraco-abdominal, "
                "battement ailes du nez, entonnoir xiphoïdien\n"
                "- TC normale/peu élevée\n"
                "- **Retentissement alimentaire** : prises diminuées, vomissements\n"
                "- **Auscultation** : râles sibilants et freinage expiratoire (bronchiolaire), "
                "+/- râles crépitants (broncho-alvéolite), +/- silence auscultatoire (formes graves)"
            )),
            FicheRow(concept="Critères de gravité", detail_md=(
                "- **FR** > 60 ou < 30/min\n"
                "- **FC** > 180 ou < 80/min\n"
                "- Pauses respiratoires, respiration superficielle\n"
                "- Signes de lutte respiratoire intenses\n"
                "- Alimentation < **50%** quantité habituelle\n"
                "- **SpO2 < 92%**"
            )),
            FicheRow(concept="Critères de vulnérabilité", detail_md=(
                "- < **2 mois** d'âge corrigé\n"
                "- Prématurité < 36 SA\n"
                "- Comorbidités\n"
                "- Contexte social/économique défavorable\n"
                "- Capacité de recours aux soins ne permettant pas retour à domicile"
            )),
            FicheRow(concept="", detail_md=(
                "- SpO2 < 92% = critère de gravité nécessitant hospitalisation\n"
                "- Silence auscultatoire = forme grave (épuisement respiratoire)"
            ), kind="piege"),
            FicheRow(concept="Signes d'inquiétance", detail_md=(
                "- Manifestations respiratoires préalables : pathologie chronique (trachéobronchomalacie, mucoviscidose)\n"
                "- Stridor : pathologie obstructive congénitale\n"
                "- Souffle cardiaque, cardiomégalie : IC\n"
                "- Mauvaise prise pondérale"
            )),
        ]),
        SousPartie(lettre="C", titre="Examens complémentaires", rows=[
            FicheRow(concept="Principe", detail_md=(
                "- **Aucun examen** pour le diagnostic positif\n"
                "- **RXT** seulement si : signes de sévérité, suspicion diagnostic différentiel, "
                "persistance symptômes > 5-7 jours"
            )),
            FicheRow(concept="RXT si indiquée", detail_md=(
                "- **Distension thoracique** : hyperclarté bilatérale, élargissement espaces intercostaux, "
                "horizontalisation côtes, abaissement coupoles diaphragmatiques, "
                "cœur apparaissant de petit volume\n"
                "- Atélectasie, foyer de surinfection\n"
                "- Rechercher cardiomégalie, anomalies vasculaires"
            )),
            FicheRow(concept="Autres examens", detail_md=(
                "- Virologie respiratoire : pas en pratique courante\n"
                "- NFS, CRP, HC : si fièvre mal tolérée ou âge < 3 mois\n"
                "- GDS : si détresse respiratoire sévère avec épuisement\n"
                "- Ionogramme : si vomissements ou perte de poids > 5%"
            )),
        ]),
        SousPartie(lettre="D", titre="Prise en charge", rows=[
            FicheRow(concept="Orientation", detail_md=(
                "| Forme | Prise en charge |\n"
                "|-------|-----------------|\n"
                "| **Légère** | Ambulatoire |\n"
                "| **Modérée** | Hospitalisation si SpO2 < 92%, support nutritionnel, âge < 2 mois |\n"
                "| **Grave** | Hospitalisation systématique, USI si apnées/épuisement respiratoire |"
            )),
            FicheRow(concept="Traitement symptomatique", detail_md=(
                "- **Désobstruction rhinopharyngée** ++ : lavage fosses nasales au sérum physiologique "
                "(avant chaque biberon)\n"
                "- **Hydratation suffisante** ++\n"
                "- Traitement antipyrétique si fièvre élevée\n"
                "- Fractionnement repas +/- épaississement lait artificiel"
            )),
            FicheRow(concept="Traitements NON recommandés", detail_md=(
                "- **Nébulisations B2-mimétiques/adrénaline** : non recommandées 1er épisode\n"
                "- **ATB** : pas d'indication en 1re intention, seulement si surinfection :\n"
                "  - Fièvre > 38,5°C persistante, mal tolérée, d'apparition secondaire\n"
                "  - OMA purulente associée\n"
                "  - Germes : H. influenzae non b, S. pneumoniae, Moraxella catarrhalis\n"
                "  → **Amoxicilline/Augmentin**\n"
                "- **Kinésithérapie respiratoire** : plus d'indication systématique"
            )),
            FicheRow(concept="", detail_md=(
                "- **Pas de bronchodilatateurs, pas d'adrénaline, pas de sérum salé hypertonique** en 1er épisode\n"
                "- **CI** : sirop antitussif, fluidifiant bronchique\n"
                "- Pas d'ATB systématique"
            ), kind="a_retenir"),
            FicheRow(concept="Formes sévères : mesures hospitalières", detail_md=(
                "- Scope cardio-respiratoire, VVP\n"
                "- Isolement respiratoire type gouttelettes\n"
                "- Nutrition entérale si asthénie/vomissements malgré fractionnement\n"
                "- Arrêt alimentation entérale + VVP si épuisement respiratoire\n"
                "- **Oxygénothérapie** : SaO2 cible > **90% sommeil** et > **94% éveil**"
            )),
        ]),
        SousPartie(lettre="E", titre="Suivi et prévention VRS", rows=[
            FicheRow(concept="Suivi immédiat", detail_md=(
                "- **Hospitalisé** : scope, TC, FR, SpO2, FC, conscience, poids, hydratation, "
                "alimentation\n"
                "- **Ambulatoire** : TC, état général, alimentation, surveillance parentale, "
                "conseils notés sur l'ordonnance et carnet de santé"
            )),
            FicheRow(concept="Évolution long terme", detail_md=(
                "- **Guérison** ++ habituelle\n"
                "- Délai 3-4 semaines avant réactivité mucociliaire efficace\n"
                "- Toux résiduelle prolongée possible\n"
                "- FDR récidives : sexe masculin, tabagisme maternel, tabagisme passif, "
                "fréquentation collectivités\n"
                "- Risque d'évolution vers **asthme**"
            )),
            FicheRow(concept="Prévention infections à VRS", detail_md=(
                "- **Mesures générales** : éviction tabagisme passif, garde en collectivité après 6 mois, "
                "hygiène des mains, éducation DRP\n"
                "- **Milieu hospitalier** : plan bronchiolite, masque + gants, lavage mains SHA"
            )),
            FicheRow(concept="◆ Traitements préventifs VRS", detail_md=(
                "| Traitement | Population cible | Posologie |\n"
                "|------------|-----------------|----------|\n"
                "| **ABRYSVO** | Femme enceinte 32-36 SA | Dose unique (sept-janv) |\n"
                "| **BEYFORTUS (nirsevimab)** | Nourrissons (période épidémique) | < 5 kg : 50 mg IM, > 5 kg : 100 mg IM |\n"
                "| **Palivizumab** | Prématurés ≤ 35 SA, DBP, cardiopathie congénitale | 15 mg/kg/mois IM |"
            )),
            FicheRow(concept="", detail_md=(
                "- **Nirsevimab (Beyfortus)** : dose unique pour tous les nourrissons en période épidémique\n"
                "- Extension jusqu'à **24 mois** pour les patients vulnérables"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE V : CONVULSIONS DE L'ENFANT ──
    partie_v = Partie(numero="V", titre="Convulsions de l'enfant", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et tableau clinique", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Convulsions** = manifestations motrices d'une crise d'épilepsie\n"
                "- Soit **occasionnelles** ++, soit récidives répétées sans facteur déclenchant = **épilepsie**"
            )),
            FicheRow(concept="Anamnèse", detail_md=(
                "- Âge, ATCD anténataux et périnataux\n"
                "- ATCD neurologiques personnels et familiaux (crises fébriles, épilepsie)\n"
                "- Maladie chronique (diabète sous insuline)\n"
                "- Circonstances : contage infectieux, TC récent, traitement en cours, FDR maltraitance\n"
                "- **Description crise** : tonico-clonique/clonique/tonique/atonique, "
                "généralisée/partielle, durée"
            )),
            FicheRow(concept="Diagnostics différentiels", detail_md=(
                "- Frissons, trémulations\n"
                "- Myoclonies du sommeil\n"
                "- **Spasmes du sanglot**\n"
                "- Syncopes vagales convulsivantes\n"
                "- Dystonie aux neuroleptiques (Primpéran, Motilium)"
            )),
            FicheRow(concept="Examen clinique", detail_md=(
                "- **Constantes** : TC +++, PA, diurèse, **GLYCÉMIE CAPILLAIRE**\n"
                "- **Examen neurologique** : Glasgow pédiatrique, mesure PC, "
                "palpation fontanelle antérieure, état de conscience, signes méningés, "
                "signes neurologiques focaux\n"
                "- **Téguments** : purpura, exanthème, ecchymoses/hématomes (maltraitance), "
                "pâleur conjonctivale\n"
                "- Auscultation cardio-pulmonaire"
            )),
            FicheRow(concept="", detail_md=(
                "- **Glycémie capillaire** = systématique devant toute convulsion de l'enfant\n"
                "- **TC** = systématique (crise fébrile ?)"
            ), kind="a_retenir"),
            FicheRow(concept="Situations d'urgence", detail_md=(
                "- Durée convulsion > **5 minutes**\n"
                "- Signes respiratoires : bradypnée, apnées, cyanose\n"
                "- Signes hémodynamiques : tachycardie, TRC allongé, marbrures\n"
                "- Signes neurologiques focaux durables, troubles de conscience prolongés\n"
                "- Crise prolongée/récidivante à court terme, déficit post-critique\n"
                "- Urgence liée à la cause : **purpura fébrile**"
            )),
        ]),
        SousPartie(lettre="B", titre="Examens complémentaires et étiologies", rows=[
            FicheRow(concept="Bilan de 1re crise convulsive", detail_md=(
                "| Examen | Indication |\n"
                "|--------|------------|\n"
                "| **PL** | Suspicion infection SNC |\n"
                "| **Scanner cérébral injecté** | Âge < 1 an, signes de localisation, troubles conscience > 30 min |\n"
                "| **Glycémie capillaire** | Systématique |\n"
                "| NFS, ionogramme | Si < 6 mois ou signes de gravité |\n"
                "| EEG | Si atypique ou suspicion épilepsie |"
            )),
            FicheRow(concept="Convulsions occasionnelles sans fièvre", detail_md=(
                "- **Hématomes cérébraux** (sous-dural, extra-dural) :\n"
                "  - Post-traumatique\n"
                "  - **Maltraitance** (à évoquer en priorité si < 1 an avec convulsion non fébrile)\n"
                "- **Troubles métaboliques** (avant 6 mois) : déshydratation, hyponatrémie, "
                "hypocalcémie, **hypoglycémie**\n"
                "- **Intoxications** : CO, antidépresseurs, OH, anti-H2\n"
                "- Syndrome de pré-mort subite (2-5 mois)\n"
                "- 1re crise d'épilepsie, causes tumorales, neuro-vasculaires"
            )),
            FicheRow(concept="", detail_md=(
                "- Convulsion non fébrile chez enfant < 1 an = **évoquer maltraitance** en priorité\n"
                "- Toujours rechercher une cause métabolique avant 6 mois"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Crises fébriles : diagnostic et prise en charge", rows=[
            FicheRow(concept="◆ Généralités crises fébriles", detail_md=(
                "- Concernent **2-5%** des enfants\n"
                "- Fréquence majorée si ATCD familiaux\n"
                "- Survenue ++ à l'ascension thermique / premières heures fièvre élevée"
            )),
            FicheRow(concept="Définition crise fébrile", detail_md=(
                "- Crise convulsive occasionnelle fébrile\n"
                "- Nourrisson/enfant âge **6 mois - 5 ans** (1-3 ans ++)\n"
                "- DPM normal\n"
                "- Après exclusion atteinte du SNC\n"
                "- PL systématique si nourrisson < **9 mois** / au moindre signe d'atteinte SNC"
            )),
            FicheRow(concept="CF simple vs complexe", detail_md=(
                "| Critère | CF simple | CF complexe |\n"
                "|---------|-----------|-------------|\n"
                "| Durée | < 15 min | > 15 min |\n"
                "| Type | Généralisée | Focale possible |\n"
                "| Récidive 24h | Non | Possible |\n"
                "| Déficit post-critique | Non | Possible |\n"
                "| Traitement de fond | **Aucun** | Consultation neuropédiatrie |"
            )),
            FicheRow(concept="Traitement d'urgence", detail_md=(
                "- Mise en **PLS**, libération VAS, O2 si besoin, découvrir enfant\n"
                "- Si crise > **5 min** : **MIDAZOLAM buccal** ou **DIAZEPAM intra-rectal** (0,5 mg/kg)\n"
                "- Si échec après 5 min : 2e dose benzodiazépine 0,5 mg/kg IV si possible\n"
                "- Échec à 30 min = **état de mal épileptique** : "
                "lévétiracétam/phénytoïne/phénobarbital\n"
                "- Traitement de la fièvre\n"
                "- **Éducation parents** : risque récidive 30%, administration diazépam IR si crise > 5 min"
            )),
            FicheRow(concept="", detail_md=(
                "- CF simple = **aucun traitement de fond**\n"
                "- CF complexe = consultation neuropédiatrie pour discuter traitement de fond\n"
                "- Toute crise fébrile non reconnue comme simple : **évoquer infection SNC** (PL +++)"
            ), kind="a_retenir"),
            FicheRow(concept="Diagnostics différentiels des crises fébriles", detail_md=(
                "- **Méningite**, méningo-encéphalite virale/bactérienne (PL +++)\n"
                "- Neuropaludisme en zone d'endémie ou retour de voyage"
            )),
        ]),
    ])

    # ── PARTIE VI : SUIVI MÉDICAL, RGO ET PATHOLOGIES SPÉCIFIQUES ──
    partie_vi = Partie(numero="VI", titre="Suivi médical, RGO et pathologies spécifiques", sous_parties=[
        SousPartie(lettre="A", titre="Suivi médical de l'enfant et carnet de santé", rows=[
            FicheRow(concept="Définitions âges pédiatriques", detail_md=(
                "| Tranche d'âge | Définition |\n"
                "|--------------|----------|\n"
                "| Nouveau-né | < 1 mois |\n"
                "| Nourrisson | 1 mois - 2 ans |\n"
                "| Jeune/grand enfant | 2 ans - début puberté |\n"
                "| Adolescent | Après début puberté |"
            )),
            FicheRow(concept="Carnet de santé", detail_md=(
                "- Pathologies au long cours, allergies, ATCD familiaux\n"
                "- Données période périnatale\n"
                "- Courbe de croissance staturo-pondérale\n"
                "- Synthèse examens bucco-dentaires\n"
                "- Hospitalisations, examens radiologiques, transfusions\n"
                "- **Vaccinations** réalisées, maladies infectieuses contractées"
            )),
            FicheRow(concept="Examens obligatoires", detail_md=(
                "- **20 examens** dont **3 obligatoires** avec certificats médicaux :\n"
                "  - **8e jour** : examen de naissance (Apgar, poids, PC, dépistages, Guthrie)\n"
                "  - **9e mois** : DPM, croissance, dépistages sensoriels, calendrier vaccinal\n"
                "  - **24e mois** : mêmes éléments + **dépistage précoce autisme** +++\n"
                "- 1/mois jusqu'à 6 mois, 2/an jusqu'à 6 ans"
            )),
            FicheRow(concept="5 axes d'évaluation", detail_md=(
                "- Développement psycho-moteur\n"
                "- Développement staturo-pondéral\n"
                "- Dépistages sensoriels\n"
                "- Modalités d'alimentation\n"
                "- Respect calendrier vaccinal"
            )),
            FicheRow(concept="Bilans scolaires", detail_md=(
                "- **4e année** : contrôle 5 axes évolutifs\n"
                "- **6e année** : 5 axes + évaluation neuro-psychomotrice "
                "(troubles apprentissages, affection neurologique)\n"
                "- **9e, 12e et 15e année** : 5 axes + développement pubertaire, "
                "statique vertébrale, écoute projets de vie, repérage mal-être"
            )),
            FicheRow(concept="Institutions", detail_md=(
                "- **PMI** (< 6 ans) : consultations gratuites, prévention, dépistage handicap, "
                "contrôle assistantes maternelles, surveillance école maternelle\n"
                "- **Santé scolaire** (> 6 ans) : PAI, PPS, bilans santé, "
                "éducation à la santé, protection enfant en danger"
            )),
        ]),
        SousPartie(lettre="B", titre="RGO de l'enfant", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **RGO physiologique** : présent à tout âge, régurgitations banales se réduisant avec âge\n"
                "  - 2/3 enfants à 4-5 mois, 1/4 à 6-7 mois, < 5% à 1 an\n"
                "- **RGO pathologique** : œsophagite, manifestations extra-digestives avec reflux prouvé"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- **Régurgitations** : expulsions soudaines sans effort, per/post-prandiales, "
                "favorisées par changements de position\n"
                "- **Œsophagite** : pas de signe clinique spécifique ; évoquer si refus biberon "
                "après quelques succions ; +/- retentissement pondéral\n"
                "- Manifestations **ORL** : dyspnée laryngée, dysphonie, érosions dentaires\n"
                "- Manifestations **pulmonaires** : toux chronique nocturne, "
                "bronchiolites/pneumopathies récidivantes\n"
                "- **Malaises** : perte de contact, cyanose, hypotonie, apnées, bradycardie"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "| Examen | Rôle |\n"
                "|--------|-----|\n"
                "| **pH-métrie œsophagienne** | Référence diagnostic positif : pH < 4 > 10% du temps |\n"
                "| **FOGD** | Référence diagnostic **œsophagite** (si œsophagite, pH-métrie inutile) |\n"
                "| TOGD | Anomalie morphologique, pas d'intérêt pour diagnostic RGO |\n"
                "| Manométrie | Anomalie motricité, ne recherche pas RGO |"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ pH-métrie **inutile** si régurgitations isolées (diagnostic clinique)\n"
                "- ⚠ pH-métrie **inutile** si œsophagite prouvée (RGO alors certain)\n"
                "- FOGD normale **n'élimine pas** le RGO"
            ), kind="piege"),
            FicheRow(concept="Prise en charge", detail_md=(
                "- **RHD toujours** : rassurance parents, épaississement lait (lait AR), "
                "réduction volume biberons si excessif ; aucune mesure spécifique si allaitement maternel\n"
                "- **IPP** : aucune efficacité sur régurgitations (seulement sur l'acidité)\n"
                "  - Indications : œsophagite érosive prouvée, RGO acide authentifié pH-métrie, "
                "pyrosis résistant aux RHD\n"
                "  - **Oméprazole** 1 mg/kg/j ou ésoméprazole, 1 prise avant 1er repas\n"
                "- Chirurgie : exceptionnelle\n"
                "- Évolution habituellement favorable après **6 mois**"
            )),
        ]),
        SousPartie(lettre="C", titre="Maladie cœliaque", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Maladie dysimmunitaire déclenchée et entretenue par l'ingestion de **gluten**\n"
                "- Prédisposition génétique : **HLA DQ2** (95%), **DQ8** (5%)\n"
                "- Événement déclenchant : infection intestinale virale, "
                "âge introduction gluten < 3 mois ou > 6 mois"
            )),
            FicheRow(concept="Tableau clinique typique du nourrisson", detail_md=(
                "- Signes digestifs : **diarrhées chroniques**, ballonnement abdominal\n"
                "- **Cassure** de la courbe pondérale puis staturale\n"
                "- Anorexie, dénutrition progressive, amyotrophie\n"
                "- Pâleur (anémie), apathie, tristesse\n"
                "- Formes tardives atypiques : carence martiale, retard statural isolé, "
                "douleurs abdominales, constipation"
            )),
            FicheRow(concept="", detail_md=(
                "- Maladie cœliaque survient **APRÈS** le début de la diversification alimentaire\n"
                "- Rechercher si cassure pondérale + diarrhées chroniques"
            ), kind="a_retenir"),
            FicheRow(concept="Prise en charge", detail_md=(
                "- **Régime d'éviction gluten à vie** : blé, orge, seigle (avoine tolérée)\n"
                "- +/- Régime sans lactose et supplémentation vitamine/fer transitoirement\n"
                "- Éducation thérapeutique, conseils diététiques, associations de malades\n"
                "- **PAI** indispensable à l'école\n"
                "- Remboursements SS possibles pour produits sans gluten\n"
                "- **Suivi** : dosage Ac à 6-12 mois (évaluation observance)"
            )),
            FicheRow(concept="Complications de la mauvaise observance", detail_md=(
                "- Retard de croissance\n"
                "- Ostéopénie\n"
                "- Augmentation incidence MAI\n"
                "- Risque accru de cancers (**lymphome**)"
            )),
        ]),
        SousPartie(lettre="D", titre="Maltraitance et syndrome du bébé secoué", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Maltraitance** : toute violence physique, abus sexuel, sévice psychologique sévère, "
                "négligence lourde ayant des conséquences préjudiciables\n"
                "- **Syndrome de Münchausen par procuration** : maltraitance où les parents (++ mère) "
                "allèguent des symptômes chez l'enfant conduisant à de multiples examens/interventions\n"
                "- Épidémiologie : 100 000 enfants en danger en France, 20 000 maltraités ; "
                "75% < 3 ans ; entourage proche responsable dans 80% des cas"
            )),
            FicheRow(concept="FDR de maltraitance", detail_md=(
                "| Personne | Facteurs de risque |\n"
                "|----------|-------------------|\n"
                "| **Parents** | Immaturité, grossesse non déclarée, chômage, pauvreté, "
                "monoparentalité, psychose, dépression, sévices subis, addictions |\n"
                "| **Enfant** | Prématurité, handicap, séparations, pleurs incessants |\n"
                "| **Fratrie** | Hospitalisations répétées, MIN inexpliquée, placements |"
            )),
            FicheRow(concept="◆ Éléments d'orientation", detail_md=(
                "- Lésions inexpliquées, délai anormal avant consultation\n"
                "- Incohérence motif / tableau clinique\n"
                "- Hiatus entre explications parents et signes constatés\n"
                "- Manque d'intérêt pour le pronostic, manque de contact avec enfant\n"
                "- Refus d'hospitalisation\n"
                "- Nomadisme médical, consultations fréquentes aux urgences"
            )),
            FicheRow(concept="◆ Lésions évocatrices", detail_md=(
                "- **Hématomes/ecchymoses** : linéaires, en boucle (ceinture), visage, cuir chevelu, "
                "parties couvertes\n"
                "- **Brûlures** : cigarettes, bouche, dos, mains\n"
                "- Griffures, morsures, plaques cheveux arrachés\n"
                "- **Syndrome de Silverman** : lésions osseuses et fractures multiples d'âges différents, "
                "cals osseux, arrachements métaphysaires, décollements périostés"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- **Photographies lésions** en couleurs\n"
                "- **FO** : hémorragies rétiniennes, œdème papillaire\n"
                "- NFS, étude hémostase, recherche toxiques, transaminases\n"
                "- **RX squelette complet** si < 2 ans +/- scintigraphie osseuse\n"
                "- Scanner cérébral si traumatisme cérébral / enfant secoué"
            )),
            FicheRow(concept="DD à connaître", detail_md=(
                "- Syndromes hémorragiques : hémophilie, maladie de von Willebrand\n"
                "- **Ostéogenèse imparfaite** +++\n"
                "- **Taches mongoloïdes** +++\n"
                "- Maladie cœliaque"
            )),
            FicheRow(concept="PEC médico-légale", detail_md=(
                "- **Hospitalisation** obligatoire si maltraitance physique avérée\n"
                "- Si refus parents : demande **d'OPP** en urgence\n"
                "- **Certificat médical descriptif** systématique, non interprétatif\n"
                "- **Signalement** à la CRIP ou au Parquet = dérogation au secret médical\n"
                "- Parents informés sauf intérêt contraire de l'enfant\n"
                "- Suivi prolongé et pluridisciplinaire"
            )),
            FicheRow(concept="Syndrome du bébé secoué", detail_md=(
                "- ++ Nourrissons < **1 an** ; 200 cas/an en France\n"
                "- **Clinique** : bombement fontanelle, convulsions, hypotonie axiale, "
                "troubles vigilance, pâleur, malaise grave, pauses respiratoires, "
                "changement de couloir PC\n"
                "- **Imagerie** : scanner en 1re intention, IRM dès stabilisation :\n"
                "  - **Hématomes sous-duraux** plurifocaux (faux du cerveau, fosse postérieure)\n"
                "  - Lésions anoxiques, contusions\n"
                "- **FO** dans les 48-72h : hémorragies rétiniennes quasi **pathognomoniques** "
                "si multiples, profuses, éclaboussant la rétine (absentes 20%)"
            )),
            FicheRow(concept="", detail_md=(
                "- **Hémorragies rétiniennes profuses** = quasi pathognomoniques du bébé secoué\n"
                "- Toute convulsion non fébrile < 1 an = évoquer maltraitance"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE VII : ÉRUPTIONS FÉBRILES DE L'ENFANT ──
    partie_vii = Partie(numero="VII", titre="Éruptions fébriles de l'enfant", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et démarche diagnostique", rows=[
            FicheRow(concept="Définitions", detail_md=(
                "- **Exanthème** : éruption cutanée touchant l'ensemble du corps (avec intervalles de peau saine)\n"
                "- **Énanthème** : éruption des muqueuses\n"
                "- **Érythrodermie** : éruption cutanée touchant l'ensemble du tégument "
                "(sans intervalle peau saine) avec lésions érythémato-squameuses"
            )),
            FicheRow(concept="Classification des exanthèmes", detail_md=(
                "| Type | Pathologies |\n"
                "|------|------------|\n"
                "| **Érythémateux** | Scarlatine, toxidermie, maladie de Kawasaki |\n"
                "| **Maculo-papuleux** | Rougeole, rubéole, exanthème subit, mégalérythème épidémique |\n"
                "| **Vésiculo-pustuleux** | Varicelle +++, HSV, zona, syndrome pieds-mains-bouche |"
            )),
            FicheRow(concept="Urgences diagnostiques", detail_md=(
                "- **Purpura fébrile** → méningocoque\n"
                "- Érythème fébrile + troubles hémodynamiques → **syndrome toxinique** "
                "(Toxic Shock Syndrome)\n"
                "- Fièvre > **5 jours** : **maladie de Kawasaki**\n"
                "- Décollements épidermiques : toxidermies sévères"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Fièvre > 5 jours chez l'enfant = penser à la **maladie de Kawasaki**\n"
                "- Purpura fébrile = **urgence vitale** (→ méningocoque)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Scarlatine et rougeole", rows=[
            FicheRow(concept="Scarlatine", detail_md=(
                "- Agent : **streptocoque bêta-hémolytique groupe A** (SGA), toxine érythrogène\n"
                "- Transmission directe aérienne ; incubation **3-5 jours**\n"
                "- Contagiosité pendant invasion et **48h** après début ATB"
            )),
            FicheRow(concept="Scarlatine : tableau clinique", detail_md=(
                "- **Phase d'invasion** (24h) : fièvre 39-40°C, angine érythémateuse avec dysphagie, "
                "douleurs abdominales, vomissements, ADP sous-angulo-maxillaires\n"
                "- **Phase éruptive** (24h après invasion) :\n"
                "  - **Énanthème** : amygdales tuméfiées, **glossite** : "
                "langue saburrale → V lingual → aspect **framboisé** → J6, régression en 1 semaine\n"
                "  - **Exanthème scarlatiniforme** : plaques diffuses rouge vif, granitées, "
                "sans intervalle peau saine, prédominant aux plis puis extension\n"
                "  - Respect paumes, plantes et région péribuccale\n"
                "- **Desquamation** post-éruptive en doigt de gant"
            )),
            FicheRow(concept="Scarlatine : PEC", detail_md=(
                "- Diagnostic clinique + TDR streptocoque A\n"
                "- **Amoxicilline 50 mg/kg/j pendant 6 jours**\n"
                "- Éviction scolaire jusque **48h** après début ATB\n"
                "- ATBprophylaxie si épidémie familiale/collectivité fermée"
            )),
            FicheRow(concept="Rougeole", detail_md=(
                "- Agent : **paramyxovirus** (Morbillivirus) ; transmission aérienne\n"
                "- Incubation **10-12 jours** ; contagiosité très importante "
                "dès phase d'invasion (5 j avant éruption) jusqu'à 5 j après\n"
                "- **DO obligatoire**"
            )),
            FicheRow(concept="Rougeole : tableau clinique", detail_md=(
                "- **Phase d'invasion** (2-4 j) : fièvre élevée, catarrhe oculo-respiratoire "
                "(larmoiement, conjonctivite, rhinorrhée, toux)\n"
                "  - Énanthème **pathognomonique** : **signe de Köplik** "
                "(taches punctiformes blanc-bleuté muqueuse jugale)\n"
                "- **Phase éruptive** (~2 sem après contage) : exanthème maculo-papuleux "
                "débutant derrière les oreilles, extension en 24-48h vers face et corps "
                "(direction descendante, 1 seule poussée), régression en 5-6 j\n"
                "- Fièvre décroissante lors généralisation"
            )),
            FicheRow(concept="", detail_md=(
                "- **Signe de Köplik** = pathognomonique de la rougeole\n"
                "- Rougeole = **déclaration obligatoire** (signalement ARS)"
            ), kind="a_retenir"),
            FicheRow(concept="Rougeole : complications et PEC", detail_md=(
                "- **Complications infectieuses** (réascension thermique) : bronchite, pneumopathie, "
                "surinfections pulmonaires, OMA purulente\n"
                "- **Complications neurologiques** : encéphalite aiguë morbilleuse, "
                "panencéphalite sclérosante subaiguë de Van Bogaert (5-10 ans après)\n"
                "- Confirmation : PCR sur salive/sérum (obligatoire)\n"
                "- Traitement symptomatique, ATB si surinfection (Augmentin)\n"
                "- Éviction scolaire **5 jours** après début éruption\n"
                "- Vérification statut vaccinal des contacts"
            )),
        ]),
        SousPartie(lettre="C", titre="Rubéole, mégalérythème épidémique et exanthème subit", rows=[
            FicheRow(concept="◆ Rubéole", detail_md=(
                "- Agent : **Rubivirus** (ARN) ; transmission aérienne/transplacentaire\n"
                "- Incubation **15-21 jours**\n"
                "- Phase d'invasion (1 sem) : fièvre modérée, état général conservé, "
                "absence de catarrhe\n"
                "- Phase éruptive : exanthème maculo-papuleux (macules/papules plus petites/pâles "
                "que rougeole), face puis thorax, 1 poussée sur 72h puis disparition\n"
                "- Signes associés : ADP **occipitales**, +/- splénomégalie\n"
                "- Complications : purpura thrombopénique, arthralgies, encéphalite\n"
                "- Traitement symptomatique, prohibition contact **femme enceinte**"
            )),
            FicheRow(concept="◆ Mégalérythème épidémique", detail_md=(
                "- Primo-infection à **Parvovirus B19**\n"
                "- Âge 5-14 ans ; épidémies familiales/scolaires\n"
                "- Incubation 6-14 jours ; transmission respiratoire\n"
                "- Phase éruptive : exanthème maculo-papuleux aux **joues rouges aspect souffleté**, "
                "puis extension tronc/extrémités (aspect **réticulé en carte de géographie**), "
                "fluctuations 1-3 semaines\n"
                "- Complications : arthralgies/arthrites ; **femme enceinte** : anasarque fœtoplacentaire ; "
                "enfant avec hémolyse chronique : crise arégénérative\n"
                "- Diagnostic : PCR sanguine, IgM spécifiques\n"
                "- Prohibition contact femme enceinte/enfant à hémolyse chronique"
            )),
            FicheRow(concept="◆ Exanthème subit (roséole infantile)", detail_md=(
                "- Primo-infection **HHV6/7** ; âge **6-24 mois**\n"
                "- Transmission respiratoire ; incubation 5-15 jours\n"
                "- Phase d'invasion (3-4 j) : **fièvre isolée brutale** 39-40°C, bien tolérée\n"
                "- Phase éruptive : maculopapules pâles visage/front, disparition 12-24h ; "
                "**apyrexie contemporaine** très caractéristique\n"
                "- ADP cervicales\n"
                "- Complications : crises fébriles simples, méningite\n"
                "- Traitement symptomatique, éviction scolaire non obligatoire"
            )),
            FicheRow(concept="", detail_md=(
                "- Exanthème subit : **chute thermique brutale** contemporaine de l'éruption = très évocateur\n"
                "- Mégalérythème : **joues souffletées** + éruption réticulée = quasi pathognomonique\n"
                "- Rubéole : **ADP occipitales** = élément d'orientation"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Résumé évictions scolaires", detail_md=(
                "| Maladie | Éviction scolaire |\n"
                "|---------|------------------|\n"
                "| Scarlatine | **48h** après début ATB |\n"
                "| Rougeole | **5 jours** après début éruption |\n"
                "| Rubéole | **Non obligatoire** |\n"
                "| Mégalérythème | **Non obligatoire** |\n"
                "| Exanthème subit | **Non obligatoire** |\n"
                "| Coqueluche | **5 jours** après début ATB (3 si azithromycine) |"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Signes de gravité de la fièvre de l'enfant", markdown=(
            "| Système | Signes de gravité |\n"
            "|---------|------------------|\n"
            "| Hémodynamique | Tachycardie/bradycardie, hypotension, TRC allongé, teint gris, marbrures |\n"
            "| Neurologique | Somnolence, léthargie, Glasgow < 14, convulsions, fontanelle bombante |\n"
            "| Respiratoire | Polypnée > 40-60/min, hypoxie, signes de lutte |\n"
            "| Cutané | Purpura extensif nécrotique > 3 mm |\n"
            "| Général | AEG, déshydratation, pâleur, anorexie, cris inhabituels |\n"
            "| Terrain | Nourrisson < 3 mois, ID, drépanocytose |"
        )),
        TableauSynthese(titre="Déshydratation de l'enfant : évaluation et PEC", markdown=(
            "| Sévérité | Perte poids | Signes | PEC |\n"
            "|---------|------------|--------|-----|\n"
            "| Légère | < 5% | Soif, sécheresse muqueuses | Ambulatoire, SRO |\n"
            "| Modérée | 5-10% | Cernes, fontanelle déprimée, pli cutané | Essai SRO, hospit si échec |\n"
            "| Sévère | > 10% | Troubles hémodynamiques, conscience | Hospitalisation, IV |"
        )),
        TableauSynthese(titre="Crises fébriles : simple vs complexe", markdown=(
            "| Critère | CF simple | CF complexe |\n"
            "|---------|-----------|-------------|\n"
            "| Durée | < 15 min | > 15 min |\n"
            "| Type | Généralisée | Focale possible |\n"
            "| Récidive 24h | Non | Possible |\n"
            "| Âge | 1-5 ans | Tout âge |\n"
            "| Examen post-critique | Normal | Anomalies possibles |\n"
            "| TTT de fond | Aucun | Avis neuropédiatrique |"
        )),
        TableauSynthese(titre="Exanthèmes fébriles : orientation diagnostique", markdown=(
            "| Maladie | Agent | Âge | Signe caractéristique |\n"
            "|---------|-------|-----|----------------------|\n"
            "| Scarlatine | SGA | 4-10 ans | Langue framboisée, exanthème granité |\n"
            "| Rougeole | Paramyxovirus | Tout âge | Signe de Köplik, extension descendante |\n"
            "| Rubéole | Rubivirus | Enfant | ADP occipitales, éruption pâle |\n"
            "| Mégalérythème | Parvovirus B19 | 5-14 ans | Joues souffletées, éruption réticulée |\n"
            "| Exanthème subit | HHV6/7 | 6-24 mois | Fièvre brutale puis apyrexie à l'éruption |"
        )),
        TableauSynthese(titre="Prévention VRS : traitements disponibles", markdown=(
            "| Traitement | Cible | Posologie |\n"
            "|------------|-------|-----------|\n"
            "| ABRYSVO | Femme enceinte 32-36 SA | Dose unique sept-janv |\n"
            "| Nirsevimab (Beyfortus) | Nourrissons période épidémique | < 5 kg : 50 mg IM / > 5 kg : 100 mg IM |\n"
            "| Palivizumab | Prématurés, DBP, cardiopathie | 15 mg/kg/mois IM |"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Fièvre aiguë | > **38°C** | Depuis < 5 j (nourrisson) / < 7 j (enfant) |\n"
        "| Paracétamol | **60 mg/kg/j** | En 4 prises, monothérapie |\n"
        "| Ibuprofène | 20-30 mg/kg/j | Après **3 mois** de vie |\n"
        "| Déshydratation sévère | > **10%** poids | Hospitalisation systématique |\n"
        "| Remplissage vasculaire | **20 mL/kg** NaCl 0,9% | En débit libre IV |\n"
        "| Réhydratation IV | 100-150 mL/kg/24h | Déshydratation sévère |\n"
        "| Crises fébriles | **2-5%** enfants | 6 mois - 5 ans |\n"
        "| Crise fébrile à traiter | > **5 min** | Midazolam buccal ou diazépam IR |\n"
        "| Diazépam dose | **0,5 mg/kg** | IR ou buccal |\n"
        "| SpO2 bronchiolite gravité | < **92%** | Hospitalisation |\n"
        "| VRS | **60-70%** bronchiolites | 1re cause bronchiolite |\n"
        "| Nourrissons bronchiolite | **2-8 mois** | Pic épidémique |\n"
        "| Coqueluche incubation | **10 j** (7-21) | Bordetella pertussis |\n"
        "| Coqueluche contagiosité | **3 semaines** | Après début symptômes |\n"
        "| Protection vaccinale coqueluche | **5 ans** | Puis perte immunité |\n"
        "| Lopéramide CI | Avant **2 ans** | Contre-indiqué |\n"
        "| Maltraitance | **75%** < 3 ans | 100 000 enfants en danger |"
    ))

    points_cles = [
        "◆ Fièvre > 40°C, purpura extensif > 3 mm, et nourrisson < 3 mois = **urgence pédiatrique**",
        "◆ SRO = traitement de **1re intention** de la déshydratation ; "
        "remplissage **20 mL/kg** NaCl si troubles hémodynamiques",
        "◆ Lopéramide **contre-indiqué avant 2 ans** ; pas d'ATB dans la diarrhée aiguë liquidienne",
        "◆ Crise fébrile simple (< 15 min, généralisée, 1-5 ans) = **aucun traitement de fond**",
        "◆ Bronchiolite : **pas de bronchodilatateur** ni d'ATB systématique en 1er épisode ; "
        "DRP + hydratation + surveillance",
        "◆ Nirsevimab (Beyfortus) : **dose unique** pour prévention VRS chez tous les nourrissons "
        "en période épidémique",
        "◆ Coqueluche du nourrisson : **pas de chant du coq**, apnées possibles, "
        "azithromycine 3 jours ; vaccination cocooning",
        "◆ Convulsion non fébrile < 1 an = **évoquer maltraitance** ; glycémie capillaire systématique",
        "◆ Signe de Köplik = **pathognomonique** de la rougeole ; DO obligatoire",
        "◆ Syndrome du bébé secoué : hématomes sous-duraux + **hémorragies rétiniennes** "
        "quasi pathognomoniques",
    ]

    fiche_eclair_md = (
        "**Fièvre aiguë** : > 38°C, gravité si > 40°C/purpura/nourrisson < 3 mois. "
        "Paracétamol 60 mg/kg/j 1re intention. Aucun examen si pas de gravité.\n\n"
        "**Diarrhée aiguë** : virale 70% (Rotavirus). SRO = base du traitement. "
        "Déshydratation > 10% = hospitalisation + IV. CI lopéramide < 2 ans.\n\n"
        "**Coqueluche** : Bordetella pertussis, quintes + chant du coq (absent chez nourrisson). "
        "PCR naso-pharyngée. Azithromycine 3j. Vaccination cocooning.\n\n"
        "**Bronchiolite** : VRS 60-70%, nourrisson 2-8 mois. DRP + hydratation. "
        "Pas de bronchodilatateur/ATB/kinésithérapie systématique. "
        "SpO2 < 92% = hospitalisation. Nirsevimab en prévention.\n\n"
        "**Convulsions** : fébriles simples (2-5%, 1-5 ans) = pas de TTT de fond. "
        "Crise > 5 min = midazolam buccal/diazépam IR 0,5 mg/kg. "
        "Glycémie capillaire systématique.\n\n"
        "**RGO** : physiologique fréquent, pathologique si œsophagite. "
        "pH-métrie = référence diagnostic positif. IPP si œsophagite prouvée.\n\n"
        "**Maladie cœliaque** : gluten, HLA DQ2/DQ8. Régime d'éviction à vie.\n\n"
        "**Maltraitance** : 75% < 3 ans. Syndrome de Silverman. "
        "BB secoué : hématomes sous-duraux + hémorragies rétiniennes. "
        "Signalement = dérogation secret médical.\n\n"
        "**Éruptions fébriles** : scarlatine (SGA, langue framboisée), "
        "rougeole (Köplik, DO), rubéole (ADP occipitales), "
        "mégalérythème (joues souffletées), exanthème subit (apyrexie à l'éruption)."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Pédiatrie",
        annee="2025-2026",
        item="Items 147, 286, 163, 151, 344, 47, 55, 349, 114, 164, 165, 166",
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

    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)

    docx_path = output_dir / "Medecine_generale_Pediatrie_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Medecine_generale_Pediatrie_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path} ({pdf_path.stat().st_size / 1e6:.1f} MB)")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

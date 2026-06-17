"""Génère la fiche exhaustive de Gériatrie à partir du texte source extrait."""

from __future__ import annotations

import json
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
        PlanPartie(numero="I", titre="Dénutrition du sujet âgé", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et besoins nutritionnels"),
            PlanSousPartie(lettre="B", titre="Diagnostic positif et dépistage"),
            PlanSousPartie(lettre="C", titre="Conséquences et complications"),
            PlanSousPartie(lettre="D", titre="Prévention et prise en charge nutritionnelle"),
        ]),
        PlanPartie(numero="II", titre="Complications de l'immobilité et du décubitus", sous_parties=[
            PlanSousPartie(lettre="A", titre="Escarres"),
            PlanSousPartie(lettre="B", titre="Complications broncho-pulmonaires"),
            PlanSousPartie(lettre="C", titre="Complications cardiovasculaires"),
            PlanSousPartie(lettre="D", titre="Complications locomotrices"),
            PlanSousPartie(lettre="E", titre="Autres complications (urinaires, digestives, neurologiques)"),
        ]),
        PlanPartie(numero="III", titre="Démences et maladie d'Alzheimer", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et évaluation cognitive"),
            PlanSousPartie(lettre="B", titre="Maladie d'Alzheimer"),
            PlanSousPartie(lettre="C", titre="Diagnostics différentiels"),
            PlanSousPartie(lettre="D", titre="Prise en charge et suivi"),
        ]),
        PlanPartie(numero="IV", titre="Autonomie et dépendance", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définitions et épidémiologie"),
            PlanSousPartie(lettre="B", titre="Évaluation de la dépendance"),
            PlanSousPartie(lettre="C", titre="Plan d'aide et prise en charge sociale"),
        ]),
        PlanPartie(numero="V", titre="Troubles de la marche et chutes du sujet âgé", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et évaluation de la marche"),
            PlanSousPartie(lettre="B", titre="Signes de gravité et bilan d'une chute"),
            PlanSousPartie(lettre="C", titre="Facteurs de risque et prise en charge"),
        ]),
        PlanPartie(numero="VI", titre="Personne âgée malade et fragilité", sous_parties=[
            PlanSousPartie(lettre="A", titre="Polypathologie et évaluation gériatrique standardisée"),
            PlanSousPartie(lettre="B", titre="Modèle de Bouchon et particularités cliniques"),
            PlanSousPartie(lettre="C", titre="Médicaments et concept de fragilité"),
        ]),
    ]

    # ── PARTIE I : DÉNUTRITION DU SUJET ÂGÉ ──
    partie_i = Partie(numero="I", titre="Dénutrition du sujet âgé", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et besoins nutritionnels", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Personne âgée** : personne > **70-75 ans**\n"
                "- **Dénutrition protéino-énergétique (DPE)** :\n"
                "  - **4-10%** des sujets âgés à domicile\n"
                "  - **15-40%** en institution\n"
                "  - **30-70%** à l'hôpital\n"
                "- IMC normal personne âgée : **21-29,9**"
            )),
            FicheRow(concept="Besoins nutritionnels", detail_md=(
                "| Paramètre | Valeur |\n"
                "|-----------|--------|\n"
                "| Ration calorique | **30-40 kcal/kg/j** |\n"
                "| Besoins en eau | **35-45 mL/kg/j** (soit 2,5 L chez sujet de 60 kg) |\n"
                "| Protéines | **1,2-1,5 g/kg/j** |\n"
                "| Glucides | 50-55% des calories |\n"
                "| Calcium | **1 200 mg/j** |\n"
            )),
            FicheRow(concept="Obésité du sujet âgé", detail_md=(
                "- Prévalence : **17%** à 80 ans\n"
                "- Effet **protecteur** contre le risque fracturaire\n"
                "- Augmente la survie dans pathologies chroniques (IR, BPCO, IC, rhumatismes inflammatoires)\n"
                "- Objectif : **stabilisation du poids**, activité physique modérée (pas de régime restrictif)"
            )),
        ]),
        SousPartie(lettre="B", titre="Diagnostic positif et dépistage", rows=[
            FicheRow(concept="Critères diagnostiques", detail_md=(
                "| Critère | Dénutrition | Dénutrition sévère |\n"
                "|---------|-------------|--------------------|\n"
                "| Perte de poids | ≥ 5% en 1 mois ou ≥ 10% en 6 mois | ≥ 10% en 1 mois ou ≥ 15% en 6 mois |\n"
                "| IMC | < 21 | < 18 |\n"
                "| Albuminémie | < 35 g/L | < 30 g/L |\n"
                "| MNA global | < 17 | — |\n"
            )),
            FicheRow(concept="Facteurs de risque", detail_md=(
                "- **Psycho-socio-environnementaux** : isolement social, maltraitance, hospitalisation, institutionnalisation\n"
                "- **Pathologies aiguës** : toute affection aiguë ou décompensation chronique, douleur, fracture, escarre\n"
                "- **Médicaments** : polymédication, sécheresse buccale, troubles digestifs, anorexie, corticothérapie au long cours\n"
                "- **Troubles bucco-dentaires** : mastication, candidose oro-pharyngée, dysgueusie\n"
                "- **Régimes restrictifs** : sans sel, diabétique, hypocholestérolémiant\n"
                "- **Troubles neurologiques/psychiatriques** : syndromes démentiels, troubles de la déglutition, **dépression** +++\n"
                "- **Dépendance** pour les actes de la vie quotidienne (pour manger ++)"
            )),
            FicheRow(concept="◆ États d'hypercatabolisme", detail_md=(
                "- Pathologie **infectieuse**\n"
                "- Phénomènes de destruction tissulaire (AVC, IDM)\n"
                "- Situations de remodelage/cicatrisation (tumeurs, fractures, escarres)\n"
                "- IC, insuffisance respiratoire\n"
                "- Hyperthyroïdie\n"
                "- Intervention chirurgicale"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours rechercher une **dépression** devant une dénutrition du sujet âgé\n"
                "- ⚠ Les **régimes restrictifs** sont à proscrire chez le sujet âgé (sans sel, diabétique strict)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Conséquences et complications", rows=[
            FicheRow(concept="Conséquences", detail_md=(
                "- **Morbi-mortalité** significativement augmentée\n"
                "- **Sarcopénie** : diminution masse, force et fonction musculaire\n"
                "  - Diagnostic : vitesse de marche + force de préhension + masse musculaire (impédancemétrie)\n"
                "- **Immunodépression** : lymphopénie, altération réaction immunitaire, augmentation infections (++ nosocomiales)\n"
                "- **Escarres**\n"
                "- **Déshydratation**\n"
                "- Déficits vitaminiques (groupe B, C, E) et micronutriments (zinc, sélénium)"
            )),
            FicheRow(concept="", detail_md=(
                "- La **sarcopénie** est une conséquence majeure de la dénutrition du sujet âgé\n"
                "- Elle contribue au risque de **chutes**, de **fractures** et de **perte d'autonomie**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Prévention et prise en charge nutritionnelle", rows=[
            FicheRow(concept="Prévention", detail_md=(
                "- Identification des **FDR** de dénutrition\n"
                "- Analyse de l'alimentation habituelle : revenus, courses, préparation repas, nombre de repas/j, contexte (seul/compagnie)\n"
                "- Mesure du **poids**, calcul perte de poids, calcul **IMC**, calcul **MNA**\n"
                "- Hygiène de vie : activité physique régulière, hygiène corporelle et buccale"
            )),
            FicheRow(concept="Stratégie de prise en charge", detail_md=(
                "| Apport alimentaire | Dénutrition | Dénutrition sévère |\n"
                "|-------------------|-------------|--------------------|\n"
                "| Normaux | Conseils diététiques + alimentation enrichie, réévaluation J15 ; si échec : CNO | Conseils + alimentation enrichie, réévaluation J15 ; si échec : CNO |\n"
                "| Diminués > 1/2 | Conseils + alimentation enrichie + CNO, réévaluation S1 ; si échec : NE | Conseils + alimentation enrichie + CNO, réévaluation S1 ; si échec : NE |\n"
                "| Très diminués < 1/2 | Conseils + alimentation enrichie + CNO, réévaluation S1 ; si échec : NE | Conseils + alimentation enrichie + **NE d'emblée**, réévaluation S1 |\n"
            )),
            FicheRow(concept="◆ Moyens thérapeutiques", detail_md=(
                "- **Conseils nutritionnels** : augmenter fréquence des prises, produits riches en énergie/protéines, adapter textures\n"
                "- **Alimentation enrichie** : poudre de lait, lait concentré entier, beurre fondu, poudre de protéines\n"
                "- **CNO** (compléments nutritionnels oraux) : si échec enrichissement\n"
                "- **Nutrition entérale** (NE) : sonde naso-gastrique ou gastrostomie, augmentation progressive des apports\n"
                "- **Nutrition parentérale** (IV) : à **éviter** en raison des EI (infections, perturbations métaboliques)"
            )),
            FicheRow(concept="Supplémentation", detail_md=(
                "- **Vitamine D** : supplémentation **systématique** 800-1 000 UI/j (ou 100 000 UI/2-3 mois) chez > 65 ans, **sans dosage préalable**\n"
                "- Pas de supplémentation systématique en micronutriments\n"
                "- **Alpha-cétoglutarate d'ornithine** : adjuvant chez sujet âgé dénutri (AMM), max 6 semaines\n"
                "- Activité physique encadrée par kinésithérapeute"
            )),
            FicheRow(concept="Surveillance", detail_md=(
                "- **Poids** : régulier\n"
                "- **Ingesta** : quantification des apports\n"
                "- **Albumine** (sauf si initialement normale) : 1/mois\n"
                "- Aides à domicile : ménagères, auxiliaire de vie sociale, portage repas"
            )),
        ]),
    ])

    # ── PARTIE II : COMPLICATIONS DE L'IMMOBILITÉ ET DU DÉCUBITUS ──
    partie_ii = Partie(numero="II", titre="Complications de l'immobilité et du décubitus", sous_parties=[
        SousPartie(lettre="A", titre="Escarres", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Lésions d'origine **ischémique** par compression > pression de perfusion capillaire\n"
                "- Entre reliefs osseux et plan dur\n"
                "- Apparition possible dès appui prolongé > **3-4 heures** (voire 2 heures)\n"
                "- Localisations les plus fréquentes (décubitus dorsal) :\n"
                "  - **Région sacro-coccygienne** ++\n"
                "  - **Talons** ++\n"
                "  - Occiput\n"
                "- L'escarre s'étend d'abord **verticalement** puis horizontalement"
            )),
            FicheRow(concept="Facteurs favorisants", detail_md=(
                "- **Facteurs extrinsèques** : pression (intensité et durée), poids, friction, macération (sudation/incontinence), cisaillement, éléments traumatisants au contact peau\n"
                "- **Facteurs intrinsèques** :\n"
                "  - Hypovolémie, anémie, hypoxie\n"
                "  - État nutritionnel\n"
                "  - Incontinences urinaire et fécale\n"
                "  - État psychologique\n"
                "  - Âge\n"
                "  - Traitements : corticoïdes, cytotoxiques, vasoconstricteurs\n"
                "  - Comorbidités : diabète, pathologie cardiorespiratoire, tabagisme\n"
                "  - Troubles sensibilité, conscience, vigilance"
            )),
            FicheRow(concept="Classification des stades", detail_md=(
                "| Stade | Description |\n"
                "|-------|------------|\n"
                "| 0 | Hyperhémie réactionnelle, érythème disparaissant à la pression digitale, réversible < 24h |\n"
                "| 1 | **Érythème persistant** ne disparaissant pas à la pression, modification chaleur/douleur |\n"
                "| 2 | Abrasion/phlyctène/ulcération peu profonde touchant épiderme et/ou derme |\n"
                "| 3 | Nécrose des 3 plans cutanés + tissu sous-cutané, pouvant atteindre le fascia |\n"
                "| 4 | Destruction importante dépassant le fascia (muscles, tendons, os) |\n"
            )),
            FicheRow(concept="Prise en charge selon stade", detail_md=(
                "- **Stades 0-1** : suppression appui sur la zone, adaptation des positions, +/- film semi-perméable/hydrocolloïde\n"
                "- **Stade 2** : évacuation contenu phlyctène (ponction/bistouri), maintien épiderme décollé, pansement hydrocolloïde/gras\n"
                "- **Lésions ouvertes** :\n"
                "  - Nettoyage au **sérum physiologique**\n"
                "  - Détersion mécanique ou par pansement (hydrogels, alginates)\n"
                "  - Pansement de recouvrement respectant bourgeonnement\n"
                "  - VAC réservé aux échecs thérapeutiques\n"
                "- Évaluation douleur systématique, adaptation/intensification correction FDR"
            )),
            FicheRow(concept="◆ Complications", detail_md=(
                "- **Locales** : extension nécrose, infection (colonisation systématique si plaie ouverte), fistule, perforation viscères/vaisseaux, cancérisation\n"
                "- **Générales** : septicémie, choc septique, dénutrition, hypercatabolisme, anémie, embolies septiques, endocardite\n"
                "- ⚠ ATB **non justifiés** si simple colonisation bactérienne ; uniquement si signes d'**infection** (érythème, chaleur, suppuration)"
            )),
            FicheRow(concept="Prévention", detail_md=(
                "- Dès admission si risque cutané : évaluation par **échelle de Norton** (score < **16** = patient à risque)\n"
                "- Mesures : examen pluriquotidien état cutané, changement de position toutes les **2-3 heures**, mise au fauteuil/verticalisation dès que possible\n"
                "- Éviter macération, maintien hygiène cutanée, équilibre nutritionnel, hydratation\n"
                "- Éducation thérapeutique patient et entourage\n"
                "- **Supports adaptés** selon risque : surmatelas statique → matelas statique → surmatelas dynamique → matelas dynamique"
            )),
            FicheRow(concept="", detail_md=(
                "- Le score de **Norton < 16** impose la mise en place de mesures préventives\n"
                "- Le retournement toutes les **2-3 heures** est la mesure préventive fondamentale"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Complications broncho-pulmonaires", rows=[
            FicheRow(concept="◆ Physiopathologie", detail_md=(
                "- Modification course diaphragmatique et jeu costal\n"
                "- Altération cinétique muco-ciliaire : stase sécrétions bronchiques\n"
                "- Conséquences : **encombrement bronchique**, **atélectasie**, **infection bronchopulmonaire**\n"
                "- Troubles de déglutition : **pneumopathies d'inhalation** (++ côté droit, segments postérieur lobe supérieur et apical lobe inférieur)"
            )),
            FicheRow(concept="Facteurs favorisants", detail_md=(
                "- Tabac, BPCO\n"
                "- Traitements inhibant le réflexe de toux (++ **opiacés**)\n"
                "- Manoeuvre endotrachéale récente (fibroscopie, intubation)\n"
                "- Douleurs pariétales/thoraciques/abdominales post-traumatiques ou post-chirurgicales"
            )),
            FicheRow(concept="Prévention", detail_md=(
                "- Auscultation **quotidienne**\n"
                "- Hydratation correcte\n"
                "- Prise des repas en **position assise/demi-assise** dès que possible\n"
                "- Kinésithérapie de désencombrement si signes d'encombrement\n"
                "- Kinésithérapie active au lit + adaptation programme rééducatif"
            )),
        ]),
        SousPartie(lettre="C", titre="Complications cardiovasculaires", rows=[
            FicheRow(concept="Maladie thromboembolique", detail_md=(
                "- Immobilisation favorise **stase veineuse** : réduction débit vasculaire, baisse d'activité musculaire\n"
                "- Peut survenir dès les **premiers jours** de décubitus\n"
                "- **Prévention** :\n"
                "  - Anticoagulation préventive\n"
                "  - Contention veineuse élastique (bas/bandes)\n"
                "  - Drainage manuel par massage\n"
                "  - Respiration abdomino-diaphragmatique (favorise retour veineux)\n"
                "  - +/- Électromyostimulation MI"
            )),
            FicheRow(concept="Hypotension orthostatique", detail_md=(
                "- Désadaptation réflexes neurovégétatifs, stase veineuse, dégradation sensibilité barorécepteurs, déshydratation\n"
                "- ++ Sujet âgé, patients hypertendus traités, certains traitements (antiHTA, diurétiques, neuroleptiques)\n"
                "- Recherche **systématique** avant verticalisation\n"
                "- Prévention : activité physique pendant décubitus, contention MI avant lever, verticalisation **progressive**, hydratation correcte"
            )),
            FicheRow(concept="Désadaptation cardiaque", detail_md=(
                "- Apparaît en quelques **semaines**\n"
                "- Majoration FC repos, réduction volume sanguin total, atrophie fibres myocardiques\n"
                "- Chute VES et réduction performances cardiaques\n"
                "- Augmentation diurèse (diminution ADH) : risque de perte sodique chez sujet âgé\n"
                "- Prévention : rééducation active, contention élastique classe 2, réentraînement progressif"
            )),
            FicheRow(concept="Oedèmes déclives", detail_md=(
                "- Modifications répartition volume sanguin, diminution tonus sympathique\n"
                "- +/- Oedèmes de dénutrition chez sujet âgé\n"
                "- PEC : surélévation membres, massages drainage, contention, contractions musculaires actives MI"
            )),
        ]),
        SousPartie(lettre="D", titre="Complications locomotrices", rows=[
            FicheRow(concept="Ostéoporose d'immobilisation", detail_md=(
                "- Réduction ostéoformation + augmentation résorption osseuse\n"
                "- **Hypercalcémie** (modérée) + **hypercalciurie** (risque lithiase urinaire)\n"
                "- Touche essentiellement régions osseuses en charge, prédomine sur os trabéculaire\n"
                "- **Réversible** à la reprise d'appui et de déambulation\n"
                "- Prévention : travail musculaire actif, verticalisation précoce ; si handicap sévère et chronique : bisphosphonates IV"
            )),
            FicheRow(concept="◆ Enraidissement articulaire", detail_md=(
                "- Rétractions capsulo-ligamentaires, puis ankylose si immobilisation prolongée\n"
                "- Déformations fréquentes : **flessum** hanche/genou, **équin**, griffe orteils, réduction rotation externe/abduction épaule\n"
                "- Prévention : installation correcte au lit, postures alternées, mobilisation non douloureuse (passive puis active dès que possible)"
            )),
            FicheRow(concept="◆ Complications musculaires", detail_md=(
                "- **Amyotrophie** rapide\n"
                "- Diminution force maximale : **-15 à 30% force quadriceps dès J8**\n"
                "- Réduction endurance à l'effort\n"
                "- Prévention ASAP : installation correcte, mobilisations articulaires, étirements, correction carences protéiques\n"
                "- Amyotrophie en partie réversible à reprise activités mais nécessite rééducation prolongée"
            )),
            FicheRow(concept="", detail_md=(
                "- La perte de **15 à 30% de la force du quadriceps dès J8** d'immobilisation\n"
                "- Justifie une prévention musculaire dès le **premier jour** de décubitus"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="E", titre="Autres complications (urinaires, digestives, neurologiques)", rows=[
            FicheRow(concept="Complications urinaires", detail_md=(
                "- Décubitus limite vidange vésicale (bas-fond vésical non déclive) : **RPM**, risque IU et lithiase\n"
                "- Recherche RPM par **échographie** au moindre doute\n"
                "- Si RPM important : sondages intermittents\n"
                "- Assurer diurèse > **1,5 L/24h**\n"
                "- Drainage continu à éviter sauf CI/impossibilité sondages intermittents ou escarres imposant continence parfaite"
            )),
            FicheRow(concept="Complications digestives", detail_md=(
                "- **RGO** : favorisé par décubitus, prévention par position assise/demi-assise 1h après repas\n"
                "- **Fausses routes** : recherche systématique (toux lors repas, voix mouillée) ; prévention par position semi-assise, bonne hygiène bucco-dentaire, adaptation textures\n"
                "- **Constipation** : fréquente chez sujet alité ; prévention par hydratation, alimentation équilibrée, verticalisation précoce ; traitement par laxatifs osmotiques/lubrifiants"
            )),
            FicheRow(concept="Complications neurologiques", detail_md=(
                "- **Compression nerfs périphériques** : nerf ulnaire (gouttière épitrochléo-olécranienne), nerf radial, nerf sciatique, nerf fibulaire commun (col fibula)\n"
                "- EMG : neuropraxies (bon pronostic 2-3 mois) vs atteintes axonales (pronostic moins favorable)\n"
                "- Prévention : installation correcte, changements réguliers de position, +/- orthèses"
            )),
            FicheRow(concept="Conséquences psychiques", detail_md=(
                "- Réactions d'**angoisse** : insomnies, plaintes somatiques, épisodes d'agitation\n"
                "- Réactions **dépressives**\n"
                "- **Régression psychologique**\n"
                "- PEC : écoute, information, aide au maintien contacts, prise en charge psychologique, +/- psychotropes"
            )),
            FicheRow(concept="Désadaptation posturale", detail_md=(
                "- Déconditionnement sensoriel (réduction informations visuelles, vestibulaires, proprioceptives)\n"
                "- Altération perception de la verticale, difficultés transferts, **rétropulsion** aux premiers levers\n"
                "- ++ Chez sujet âgé, après quelques jours seulement\n"
                "- Prévention : rééducation posturale **précoce**"
            )),
        ]),
    ])

    # ── PARTIE III : DÉMENCES ET MALADIE D'ALZHEIMER ──
    partie_iii = Partie(numero="III", titre="Démences et maladie d'Alzheimer", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et évaluation cognitive", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Association de **deux critères** :\n"
                "  - Atteinte d'au moins **2 fonctions supérieures** : mémoire, attention, langage, gnosies, praxies, raisonnement, jugement et/ou comportement\n"
                "  - **Altération de l'autonomie** dans la vie quotidienne\n"
                "- Gradation selon retentissement dans la vie quotidienne\n"
                "- Prévalence : **6,4%**"
            )),
            FicheRow(concept="Bilan initial", detail_md=(
                "- **Interrogatoire** patient + entourage : date début, mode évolutif, ATCD familiaux (démences), ATCD personnels (psychiatriques, cérébro-vasculaires, FDRCV)\n"
                "- Évaluation du **retentissement** sur activités quotidiennes (grille **AGGIR**)\n"
                "- **Examen clinique** : poids, état CV, degré vigilance (confusion ?), déficits sensoriels, examen neurologique"
            )),
            FicheRow(concept="Évaluation cognitive", detail_md=(
                "- **MMSE** ++ : évaluation cognitive globale\n"
                "- Tests de mémoire : épreuve de rappel des **5 mots**, MIS\n"
                "- Autres : test de l'horloge, test de fluence verbale\n"
                "- Évaluation fonctionnelle : **IADL** simplifiée, échelle **ADL**, échelle DAD\n"
                "- Évaluation psychique : échelle **GDS** (dépression), échelle **NPI** (troubles comportementaux)"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- **Systématiques** : NFS, VS, CRP, ionogramme, urée/créatinine, TSH, calcémie, glycémie, albuminémie\n"
                "- **IRM** séquences T1, T2, T2*, FLAIR + coupes coronales (visualisation hippocampe)\n"
                "- **Selon contexte** : B12, folates, BHC, TPHA-VDRL, sérologie VIH, sérologie Lyme\n"
                "- **Rares** : imagerie fonctionnelle (TEMP, DAT-scan, TEP), analyse LCR (protéine Bêta-amyloïde + Tau), EEG, étude génétique"
            )),
        ]),
        SousPartie(lettre="B", titre="Maladie d'Alzheimer", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- **Première cause de démence** : un million de personnes en France\n"
                "- Prévalence en augmentation régulière\n"
                "- Âge moyen de survenue : **65 ans**\n"
                "- FDR : prédisposition génétique, FDRCV, faible niveau d'éducation"
            )),
            FicheRow(concept="Phases cliniques", detail_md=(
                "| Phase | Caractéristiques |\n"
                "|-------|------------------|\n"
                "| Pré-démentielle (prodromale) | Patients autonomes, trouble consolidation **mémoire épisodique** (oubli à mesure), **anosognosie**, test 5 mots : non amélioré par l'indiçage |\n"
                "| Démentielle | Autonomie significativement altérée, syndrome **aphaso-apraxo-agnosique** |\n"
                "| Très avancée (après 7-8 ans) | Perte d'autonomie totale, troubles comportement (agitation, hallucinations, déambulation), signes neurologiques (épilepsie, myoclonies, syndrome pyramidal/extrapyramidal) |\n"
            )),
            FicheRow(concept="Diagnostic", detail_md=(
                "- Diagnostic de **probabilité** du vivant du patient (certitude = autopsie)\n"
                "- Repose sur :\n"
                "  - Arguments **positifs cliniques** : profil des troubles cognitifs\n"
                "  - Arguments **neuro-imagerie** : atrophie hippocampique (IRM)\n"
                "  - Arguments **négatifs biologiques** : bilan systématique normal\n"
                "  - +/- Arguments imagerie métabolique : hypométabolisme cortex associatifs\n"
                "  - +/- Biomarqueurs LCR : baisse **Abêta-42** + augmentation **Tau hyperphosphorylée**\n"
                "- L'association examen clinique + IRM + bilan biologique suffit dans l'immense majorité des cas"
            )),
            FicheRow(concept="", detail_md=(
                "- Le trouble de la **mémoire épisodique** non amélioré par l'indiçage (test des 5 mots) est le signe cardinal initial\n"
                "- L'**anosognosie** est habituelle dans la maladie d'Alzheimer (contrairement à la dépression)"
            ), kind="a_retenir"),
            FicheRow(concept="Imagerie", detail_md=(
                "- **IRM** : atrophie corticale d'abord limitée aux régions **para-hippocampiques**, puis diffuse (effacement sillons, dilatation ventriculaire)\n"
                "- Scintigraphie de perfusion / TEP au FDG : hypométabolisme régions corticales associatives et temporales internes\n"
                "- Dosage LCR si diagnostic difficile : baisse massive Abêta-42, augmentation Tau hyperphosphorylée"
            )),
        ]),
        SousPartie(lettre="C", titre="Diagnostics différentiels", rows=[
            FicheRow(concept="Syndrome confusionnel", detail_md=(
                "- ⚠ Chez le sujet âgé, le syndrome confusionnel peut être un **mode de découverte** d'une démence\n"
                "- La confusion **n'élimine pas** la démence"
            )),
            FicheRow(concept="Causes fonctionnelles", detail_md=(
                "- **Dépression** +++ (diagnostic différentiel principal)\n"
                "- Troubles du sommeil (insomnie, apnées du sommeil)\n"
                "- Anxiété chronique\n"
                "- Prise de psychotropes"
            )),
            FicheRow(concept="Démences secondaires curables", detail_md=(
                "| Étiologie | Éléments clés |\n"
                "|-----------|---------------|\n"
                "| Hypothyroïdie | Dosage TSH systématique |\n"
                "| Carence B12/folates | Dosage selon contexte |\n"
                "| Syphilis, VIH | Sérologies |\n"
                "| **Hydrocéphalie à pression normale** | Triade de **Hakim** : marche à petits pas + troubles cognitifs (syndrome frontal) + troubles sphinctériens ; imagerie : dilatation tétraventriculaire sans effet de masse ; PL évacuatrice diagnostique et thérapeutique |\n"
                "| Hématome sous-dural chronique | Imagerie cérébrale |\n"
                "| Démences vasculaires | HTA, diabète, contrôle FDRCV |\n"
            )),
            FicheRow(concept="Autres démences dégénératives", detail_md=(
                "- **Démence frontale** (DLFT) : souvent familiale (30%), troubles comportement au 1er plan (perte convenances sociales, gloutonnerie, anosognosie, apathie), IRM : atrophie frontale\n"
                "- **Maladie à corps de Lewy** : troubles cognitifs **fluctuants** + syndrome **parkinsonien** + **hallucinations** précoces ; très mauvaise tolérance des neuroleptiques"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours évoquer l'**hydrocéphalie à pression normale** (triade de Hakim) : cause **curable** de démence\n"
                "- ⚠ Les **neuroleptiques** sont formellement à éviter dans la maladie à corps de Lewy"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Prise en charge et suivi", rows=[
            FicheRow(concept="Traitement médicamenteux", detail_md=(
                "- 4 molécules avec AMM : 3 anti-cholinestérasiques + 1 anti-glutamate\n"
                "- **Aucun n'est remboursé** par la sécurité sociale\n"
                "- Indiqués dans la phase démentielle légère à modérément sévère\n"
                "- EI : troubles digestifs, risque de syncope et chute (ECG systématique)\n"
                "- Initié par **neurologue, psychiatre ou gériatre**"
            )),
            FicheRow(concept="Traitement non médicamenteux", detail_md=(
                "- Maintien activité physique, loisirs, sociale\n"
                "- Rééducation : kinésithérapie motrice, **orthophoniste** ++, interventions cognitives\n"
                "- **PEC sociale** : ALD 30, APA, tutelle/curatelle, réseau de soins spécialisé, association de malades\n"
                "- **PEC entourage** : soutien logistique et psychologique des aidants, personne de confiance/directives anticipées"
            )),
            FicheRow(concept="Prévention des complications", detail_md=(
                "- Soutien psychologique du patient\n"
                "- Aménagement du domicile\n"
                "- Éviter médicaments potentiellement **confusiogènes**\n"
                "- **Pas de conduite automobile**\n"
                "- Prise en charge nutritionnelle\n"
                "- **Institutionnalisation** (EHPAD, long séjour) quand maintien à domicile impossible"
            )),
            FicheRow(concept="◆ Suivi standardisé", detail_md=(
                "- Spécialiste : 1/6 mois ; médecin traitant : 1/3 mois\n"
                "- Tous les 6 mois :\n"
                "  - Examen clinique, poids, IMC\n"
                "  - Chutes et risque de chute\n"
                "  - **MMSE**\n"
                "  - **NPI** (évaluation comportementale)\n"
                "  - **ADL** et **IADL** (autonomie)\n"
                "  - Évaluation de l'aidant (EDM)\n"
                "  - Évaluation sociale et juridique (tutelle/curatelle)"
            )),
        ]),
    ])

    # ── PARTIE IV : AUTONOMIE ET DÉPENDANCE ──
    partie_iv = Partie(numero="IV", titre="Autonomie et dépendance", sous_parties=[
        SousPartie(lettre="A", titre="Définitions et épidémiologie", rows=[
            FicheRow(concept="Définitions", detail_md=(
                "- **Autonomie** : capacité à se gouverner soi-même, présuppose capacité de jugement et liberté d'agir\n"
                "- **Dépendance** (perte d'indépendance fonctionnelle) : impossibilité partielle/totale d'effectuer sans aide humaine les activités de la vie quotidienne\n"
                "- Épidémiologie :\n"
                "  - **11%** des > 65 ans bénéficient de l'APA\n"
                "  - 60% vivent en EHPAD, 40% au domicile\n"
                "  - Âge = principal FDR : **20%** des > 80 ans, **8%** des > 65 ans"
            )),
            FicheRow(concept="Causes de perte d'indépendance", detail_md=(
                "- **Maladies neurologiques** : AVC, démences, Parkinson\n"
                "- **Maladies ostéo-articulaires** : fractures, arthrose, rhumatismes inflammatoires\n"
                "- **Maladies cardio-respiratoires** : IC, IRC, artériopathie sévère\n"
                "- **Déficits neuro-sensoriels** : cataracte, DMLA, RD, surdité\n"
                "- Conditions diverses : dénutrition, dépression, plaies chroniques"
            )),
            FicheRow(concept="◆ Dépendance iatrogène hospitalière", detail_md=(
                "- Perte fonctionnelle entre entrée et sortie d'hospitalisation\n"
                "- L'environnement hospitalier ne correspond pas aux besoins spécifiques de la personne âgée\n"
                "- Causes principales : **syndrome d'immobilisation**, confusion, dénutrition, chutes, EI médicaments, incontinence urinaire de novo\n"
                "- Privilégier hospitalisation en gériatrie ou équipe mobile de gériatrie"
            )),
            FicheRow(concept="", detail_md=(
                "- L'**hospitalisation** elle-même est un facteur de dépendance chez le sujet âgé\n"
                "- Toujours privilégier une prise en charge en milieu gériatrique adapté"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Évaluation de la dépendance", rows=[
            FicheRow(concept="Échelle ADL", detail_md=(
                "- Échelle des activités basiques de la vie quotidienne\n"
                "- Score < **3** : fortement dépendant\n"
                "- **Avantages** : simplicité, brièveté, très utilisée internationalement\n"
                "- **Inconvénients** : décrit seulement perte autonomie très sévère, ne prend pas en compte dépendances cognitives"
            )),
            FicheRow(concept="Échelle IADL", detail_md=(
                "- Échelle des activités instrumentales de la vie quotidienne\n"
                "- Évalue comportement et utilisation outils vie quotidienne\n"
                "- **Avantages** : temps bref, adapté au domicile, dépistage précoce troubles fonctions exécutives\n"
                "- **Inconvénients** : difficulté auto-évaluation, cotation différente hommes/femmes"
            )),
            FicheRow(concept="Grille AGGIR", detail_md=(
                "- **AGGIR** = Autonomie Gérontologie Groupes Iso-Ressources\n"
                "- Évalue état fonctionnel et classe en **6 niveaux GIR** :\n"
                "  - **GIR 1** : confiné lit/fauteuil, fonctions intellectuelles gravement altérées, présence continue nécessaire\n"
                "  - **GIR 2** : confiné lit/fauteuil avec fonctions intellectuelles non totalement altérées OU fonctions mentales altérées mais capacité de déplacement conservée\n"
                "  - **GIR 3** : fonctions intellectuelles conservées, capacité partielle de déplacement, aide pour autonomie corporelle\n"
                "  - **GIR 4** : s'alimente seul, pas de problème déplacement mais aide pour activités corporelles et repas\n"
                "  - **GIR 5** : aide ponctuelle (toilette, préparation repas, ménage)\n"
                "  - **GIR 6** : autonome pour actes vie courante\n"
                "- Usage réglementaire pour attribution **APA** et tarification institutions"
            )),
        ]),
        SousPartie(lettre="C", titre="Plan d'aide et prise en charge sociale", rows=[
            FicheRow(concept="Évaluation gérontologique", detail_md=(
                "- État mental, état nutritionnel\n"
                "- Marche et risque de chute\n"
                "- Adaptation au domicile\n"
                "- Évaluation de l'aidant et du tissu social\n"
                "- Besoins liés au suivi des pathologies et traitements"
            )),
            FicheRow(concept="Aides à domicile", detail_md=(
                "- **Entourage familial** : soutien par plateformes de répit, groupes de paroles, associations\n"
                "- **Aide professionnelle** : personnel infirmier/aides-soignants (soins, surveillance traitement, toilette médicalisée), sur prescription médicale\n"
                "- Aides ménagères et auxiliaires de vie\n"
                "- Kinésithérapeutes, ergothérapeutes\n"
                "- **Services et aides techniques** : portage repas, téléassistance, matériels médicalisés, aménagement domicile"
            )),
            FicheRow(concept="APA", detail_md=(
                "- **Allocation Personnalisée d'Autonomie**\n"
                "- Conditions : > **60 ans**, résidence en France > 3 mois, perte autonomie **AGGIR 1-4**\n"
                "- Montant dépend : degré dépendance, revenus, lieu de vie\n"
                "- Peut financer :\n"
                "  - À domicile : heures auxiliaire de vie, téléalarme, portage repas, accueil de jour, aménagement habitat\n"
                "  - En établissement : EHPAD"
            )),
            FicheRow(concept="Changement de lieu de vie", detail_md=(
                "- Lorsque prise en charge à domicile non réalisable, **à anticiper** au maximum\n"
                "- Résidences services, résidence autonomie (foyer logement), famille d'accueil agréée\n"
                "- **EHPAD** : hébergement + soins infirmiers + médecin coordinateur\n"
                "- **USLD** : structures hospitalières pour personnes âgées lourdement dépendantes"
            )),
        ]),
    ])

    # ── PARTIE V : TROUBLES DE LA MARCHE ET CHUTES DU SUJET ÂGÉ ──
    partie_v = Partie(numero="V", titre="Troubles de la marche et chutes du sujet âgé", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et évaluation de la marche", rows=[
            FicheRow(concept="Épidémiologie", detail_md=(
                "- **1/3** des > 65 ans et **1/2** des > 85 ans font une ou plusieurs chutes par an\n"
                "- Conséquences :\n"
                "  - Physiques (fractures osseuses) : **50%** des cas\n"
                "  - Psychologiques : **40%** des cas\n"
                "  - Aggravation dépendance : **50%** des cas\n"
                "  - Institutionnalisation : **40%** des cas\n"
                "  - Hospitalisation : **20%** des cas\n"
                "  - **12 000** décès/an en France"
            )),
            FicheRow(concept="Effets du vieillissement", detail_md=(
                "- Vieillissement des systèmes antigravitaires et d'adaptation posturale\n"
                "- Marche du sujet âgé : augmentation oscillations à la station debout, diminution vitesse, réduction longueur/hauteur du pas, augmentation temps double appui, variabilité du pas plus élevée"
            )),
            FicheRow(concept="Tests d'évaluation", detail_md=(
                "| Test | Modalité | Anormal si | Conséquence |\n"
                "|------|----------|-----------|-------------|\n"
                "| **Station unipodale** | Se tenir debout sur un pied | Impossibilité > **5 sec** et/ou écart des bras | Risque de chute traumatisante |\n"
                "| **Timed Up and Go** | Lever chaise, marcher 3 m, demi-tour, s'asseoir | Temps > **20 sec** | Prédictif nouvelle chute |\n"
                "| **Five Times Sit-to-Stand** | 5 lever-assis sans aide des bras | Temps > **15 sec** | Risque accru chutes, association troubles cognitifs |\n"
                "| **Stop Walking When Talking** | Parler en marchant | Arrêt ou ralentissement marche | Trouble contrôle moteur cérébral, risque chutes |\n"
            )),
        ]),
        SousPartie(lettre="B", titre="Signes de gravité et bilan d'une chute", rows=[
            FicheRow(concept="Gravité liée aux conséquences", detail_md=(
                "- **Traumatiques** : contusions, hématomes, plaies, luxations, fractures\n"
                "- **Impossibilité de se relever** : station au sol prolongée > **1 heure** → rhabdomyolyse, IRA, hyperkaliémie, pneumopathie d'inhalation, hypothermie, déshydratation, escarres\n"
                "- **Psychologiques** ++++ : peur de tomber, refus de verticalisation, dépression"
            )),
            FicheRow(concept="Syndrome post-chute", detail_md=(
                "- **Rétropulsion** rendant station debout impossible sans aide\n"
                "- Composante **anxieuse** majeure en position debout (phobie de la marche)\n"
                "- Troubles de la marche : petits pas glissés, appui talonnier sans déroulement, élargissement polygone de sustentation, retard initiation/freezing\n"
                "- Troubles neurologiques : hypertonie oppositionnelle, altération réactions posturales\n"
                "- **Mauvais pronostic** : urgence gériatrique nécessitant hospitalisation"
            )),
            FicheRow(concept="", detail_md=(
                "- Le **syndrome post-chute** est une **urgence gériatrique** nécessitant hospitalisation et rééducation\n"
                "- Chutes **à répétition** : au moins 2 chutes sur 12 mois"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Bilan paraclinique de gravité", detail_md=(
                "- Radiographies osseuses si suspicion de fracture\n"
                "- **CPK et créatinine** si séjour au sol > 1 heure\n"
                "- ECG si malaise ou perte de connaissance\n"
                "- Glycémie si patient diabétique\n"
                "- Scanner crânien si traumatisme crânien ou confusion"
            )),
        ]),
        SousPartie(lettre="C", titre="Facteurs de risque et prise en charge", rows=[
            FicheRow(concept="★ Facteurs prédisposants", detail_md=(
                "- Âge > **80 ans**, sexe féminin\n"
                "- ATCD chutes/fractures (risque **x16**)\n"
                "- **Polymédication** (> 4 médicaments)\n"
                "- Iatrogénie : **psychotropes** (neuroleptiques, BZP), anticholinergiques, diurétiques\n"
                "- Troubles marche/équilibre (TUG > 20 s, appui unipodal < 5 s)\n"
                "- Atteintes neurologiques : AVC, démences, Parkinson\n"
                "- Faiblesse musculaire MI, dénutrition (IMC < 21, MNA test)\n"
                "- Arthrose, neuropathies périphériques\n"
                "- Baisse acuité visuelle, dépression, déclin cognitif"
            )),
            FicheRow(concept="Facteurs précipitants", detail_md=(
                "- **Intrinsèques** :\n"
                "  - CV : troubles du rythme, conduction, SCA, EP, **hypotension orthostatique** +++\n"
                "  - Neurologiques : AVC, crise épileptique\n"
                "  - Vestibulaires, infectieux (fièvre, déshydratation)\n"
                "  - Métaboliques : hyponatrémie, hypoglycémie, hypercalcémie\n"
                "  - Toxiques : iatrogénie, intoxication alcoolique\n"
                "- **Comportementaux** : prise de risque, précipitation, intoxication alcoolique\n"
                "- **Extrinsèques** : mobilier inadapté, sol irrégulier, éclairage insuffisant, mauvais chaussage"
            )),
            FicheRow(concept="Bilan étiologique", detail_md=(
                "- Ionogramme (troubles hydro-électrolytiques)\n"
                "- NFS (anémie)\n"
                "- Dosage **vitamine D**\n"
                "- HbA1c chez patients diabétiques\n"
                "- ECG si signes d'appel cardiaque\n"
                "- Autres selon données cliniques"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- **Systématiquement** :\n"
                "  - Révision ordonnance médicaments\n"
                "  - Correction FDR prédisposants/précipitants modifiables\n"
                "  - Chaussures à talons larges et bas\n"
                "  - Marche régulière (≥ **30 min/j**)\n"
                "  - Correction **hypovitaminose D**\n"
                "  - Apport calcique alimentaire **0,8-1,2 g/j**\n"
                "- **Si troubles marche/équilibre** : kinésithérapie motrice plurihebdomadaire (marche, musculation, équilibre, transferts, relevé du sol), aménagement environnement, aide technique\n"
                "- **Si syndrome post-chute** : hospitalisation, rééducation fonctionnelle, soutien psychologique, PEC pluridisciplinaire"
            )),
        ]),
    ])

    # ── PARTIE VI : PERSONNE ÂGÉE MALADE ET FRAGILITÉ ──
    partie_vi = Partie(numero="VI", titre="Personne âgée malade et fragilité", sous_parties=[
        SousPartie(lettre="A", titre="Polypathologie et évaluation gériatrique standardisée", rows=[
            FicheRow(concept="Polypathologie", detail_md=(
                "- **HTA** (75%), IC, cardiopathies ischémiques, FA\n"
                "- **DT2** (> 10% après 65 ans)\n"
                "- Maladie d'Alzheimer, maladie de Parkinson\n"
                "- Ostéoporose, dépression\n"
                "- Adénome prostatique, cataracte, DMLA, cancers\n"
                "- Attention aux **événements médicaux aigus** : infections, anémie, EDM, traumatismes, vague de chaleur, facteurs iatrogènes → cascade avec défaillance multi-organes"
            )),
            FicheRow(concept="Évaluation gériatrique standardisée (EGS)", detail_md=(
                "- Réalisée **en dehors** d'une situation aiguë, chez patient stable\n"
                "- Évalue :\n"
                "  - Fonctions cognitives : **MMSE**\n"
                "  - Autonomie/indépendance : **ADL** et **IADL**\n"
                "  - Risque de chute : appui unipodal, Timed Up and Go\n"
                "  - État nutritionnel : **MNA** test\n"
                "  - Confusion mentale : **CAM** test\n"
                "  - Dépression : **GDS** (Geriatric Depression Scale)\n"
                "  - Risque escarre : Norton ou Braden\n"
                "  - Fonction rénale, continence, polymédication, douleur, situation sociale"
            )),
        ]),
        SousPartie(lettre="B", titre="Modèle de Bouchon et particularités cliniques", rows=[
            FicheRow(concept="Modèle de Bouchon 1+2+3", detail_md=(
                "- **1** = Vieillissement physiologique\n"
                "- **2** = Facteurs favorisants/prédisposants = maladies chroniques qui accélèrent le vieillissement\n"
                "- **3** = Facteurs précipitants/déclenchants = situations aiguës, en général **réversibles**\n"
                "- Démarche diagnostique :\n"
                "  - Détecter les situations de vulnérabilité (1+2) : ATCD, évaluer autonomie/indépendance\n"
                "  - Traquer les facteurs de décompensation (3) : toujours rechercher une **iatrogénie** (polymédication si > 4 médicaments)"
            )),
            FicheRow(concept="", detail_md=(
                "- Le modèle **1+2+3** de Bouchon est fondamental en gériatrie\n"
                "- Toujours rechercher le **facteur 3** (précipitant, souvent réversible) devant toute décompensation"
            ), kind="a_retenir"),
            FicheRow(concept="Particularités cliniques", detail_md=(
                "- Douleur thoracique parfois **absente** dans SCA\n"
                "- **Fièvre** peut manquer dans les infections\n"
                "- Défense remplace souvent contracture dans les péritonites\n"
                "- Tristesse peut manquer dans les EDM\n"
                "- Douleur typique d'UGD souvent absente, remplacée par anorexie\n"
                "- **Confusion mentale** peut être seule manifestation de RAU/occlusion intestinale\n"
                "- Ronchis peuvent être seul signe auscultatoire d'un foyer de condensation\n"
                "- La polypathologie complique l'interprétation des symptômes"
            )),
            FicheRow(concept="Particularités biologiques", detail_md=(
                "- Absence d'hyperleucocytose si infection patente (défenses immunitaires réduites)\n"
                "- Créatinine **normale** malgré IR significative (baisse masse musculaire)\n"
                "- CRP **très élevée** lors d'une simple infection bactérienne\n"
                "- Valeurs normales de ferritinémie plus hautes\n"
                "- PaO2 diminuée, augmentation taux BNP"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Une **créatinine normale** chez un sujet âgé n'exclut PAS une IR significative\n"
                "- ⚠ La **confusion mentale** peut être la seule manifestation d'une pathologie aiguë"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Médicaments et concept de fragilité", rows=[
            FicheRow(concept="★ Iatrogénie médicamenteuse", detail_md=(
                "- EI médicamenteux : **10%** des hospitalisations du sujet âgé\n"
                "- FDR : surdosage, associations déconseillées, traitement trop long, manque de surveillance, erreurs d'observance, changement d'état passé inaperçu\n"
                "- Prévention : respect démarche **DICTIAS** (si patient répond non à une/plusieurs questions : s'interroger sur dose/arrêt médicament)\n"
                "- Ne pas oublier l'oubli de médicaments utiles"
            )),
            FicheRow(concept="Concept de fragilité (Fried)", detail_md=(
                "- Ne concerne **pas tous** les patients âgés\n"
                "- **5 critères de Fried** :\n"
                "  - Perte de poids involontaire > **4,5 kg** en 1 an\n"
                "  - Fatigue subjective (GDS)\n"
                "  - Diminution de l'activité physique\n"
                "  - Diminution de la **vitesse de marche**\n"
                "  - Diminution de la **force de préhension**"
            )),
            FicheRow(concept="Classification fragilité", detail_md=(
                "| Nombre de critères | Statut |\n"
                "|-------------------|--------|\n"
                "| 0 | **Robuste** (non fragile) |\n"
                "| 1-2 | **Pré-fragile** |\n"
                "| ≥ 3 | **Fragile** |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Le dépistage de la **fragilité** prédit le risque de perte d'indépendance, de chutes et de décès\n"
                "- Son intérêt principal est de permettre des **interventions préventives** avant la survenue de la dépendance"
            ), kind="a_retenir"),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Critères diagnostiques de dénutrition du sujet âgé", markdown=(
            "| Critère | Dénutrition | Dénutrition sévère |\n"
            "|---------|-------------|--------------------|\n"
            "| Perte de poids | ≥ 5% en 1 mois ou ≥ 10% en 6 mois | ≥ 10% en 1 mois ou ≥ 15% en 6 mois |\n"
            "| IMC | < 21 | < 18 |\n"
            "| Albuminémie | < 35 g/L | < 30 g/L |\n"
            "| MNA global | < 17 | — |\n"
        )),
        TableauSynthese(titre="Stades des escarres", markdown=(
            "| Stade | Description | PEC |\n"
            "|-------|-------------|-----|\n"
            "| 0 | Hyperhémie réactionnelle, réversible < 24h | Surveillance |\n"
            "| 1 | Érythème persistant ne disparaissant pas à la pression | Suppression appui |\n"
            "| 2 | Abrasion/phlyctène/ulcération superficielle | Évacuation phlyctène + pansement |\n"
            "| 3 | Nécrose 3 plans cutanés + tissu sous-cutané | Détersion + pansement |\n"
            "| 4 | Destruction dépassant le fascia (muscles, tendons, os) | Avis chirurgical |\n"
        )),
        TableauSynthese(titre="Tests d'évaluation de la marche du sujet âgé", markdown=(
            "| Test | Seuil pathologique | Interprétation |\n"
            "|------|-------------------|----------------|\n"
            "| Station unipodale | < 5 secondes | Risque chute traumatisante |\n"
            "| Timed Up and Go | > 20 secondes | Prédictif nouvelle chute |\n"
            "| Five Times Sit-to-Stand | > 15 secondes | Risque accru chutes |\n"
            "| Stop Walking When Talking | Arrêt marche | Trouble contrôle moteur cérébral |\n"
        )),
        TableauSynthese(titre="Échelles d'évaluation gériatrique", markdown=(
            "| Échelle | Domaine | Points clés |\n"
            "|---------|---------|-------------|\n"
            "| MMSE | Cognition | Évaluation cognitive globale |\n"
            "| ADL | Activités basiques | Score < 3 = fortement dépendant |\n"
            "| IADL | Activités instrumentales | Dépistage précoce troubles exécutifs |\n"
            "| AGGIR (GIR 1-6) | Dépendance globale | Attribution APA si GIR 1-4 |\n"
            "| MNA | Nutrition | Dépistage dénutrition |\n"
            "| GDS | Dépression | Geriatric Depression Scale |\n"
            "| Norton | Risque escarre | Score < 16 = patient à risque |\n"
            "| NPI | Comportement | Troubles comportementaux démences |\n"
            "| CAM | Confusion | Confusion Assessment Method |\n"
        )),
        TableauSynthese(titre="Comparaison Alzheimer vs Démence frontale vs Corps de Lewy", markdown=(
            "| Critère | Alzheimer | Démence frontale (DLFT) | Corps de Lewy |\n"
            "|---------|-----------|------------------------|---------------|\n"
            "| Signe initial | Troubles mémoire épisodique | Troubles comportement | Troubles cognitifs fluctuants |\n"
            "| Anosognosie | Oui | Oui | Variable |\n"
            "| Syndrome parkinsonien | Tardif | Non | Précoce |\n"
            "| Hallucinations | Tardives | Non | Précoces |\n"
            "| Neuroleptiques | Possible (prudence) | Possible | CONTRE-INDIQUÉS |\n"
            "| IRM | Atrophie hippocampique | Atrophie frontale | Peu spécifique |\n"
            "| Familial | Rare (< 5%) | Fréquent (30%) | Rare |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| IMC normal sujet âgé | **21-29,9** | Seuil dénutrition < 21 |\n"
        "| Protéines sujet âgé | **1,2-1,5 g/kg/j** | Besoins nutritionnels |\n"
        "| Calcium sujet âgé | **1 200 mg/j** | Besoins nutritionnels |\n"
        "| Vitamine D | **800-1 000 UI/j** | Supplémentation systématique > 65 ans |\n"
        "| Albuminémie dénutrition | < **35 g/L** | Sévère si < 30 g/L |\n"
        "| Norton score à risque | < **16** | Risque d'escarre |\n"
        "| Escarre : appui critique | > **3-4 heures** | Durée d'appui à risque |\n"
        "| Force quadriceps immobilisation | **-15 à -30%** dès J8 | Complications musculaires |\n"
        "| Chutes > 65 ans | **1/3** par an | Prévalence |\n"
        "| Décès par chute | **12 000/an** | France |\n"
        "| Station unipodale anormale | < **5 sec** | Risque chute traumatisante |\n"
        "| Timed Up and Go anormal | > **20 sec** | Prédictif nouvelle chute |\n"
        "| Polymédication | > **4** médicaments | FDR iatrogénie |\n"
        "| Iatrogénie | **10%** hospitalisations | Sujet âgé |\n"
        "| Fragilité (Fried) | ≥ **3** critères | Sur 5 critères |\n"
        "| Perte poids (fragilité) | > **4,5 kg**/an | Critère de Fried |\n"
        "| APA conditions | > **60 ans** + AGGIR 1-4 | Allocation personnalisée autonomie |\n"
    ))

    points_cles = [
        "La denutrition touche 30-70% des sujets ages hospitalises ; depistage par poids, IMC, MNA et albuminemie",
        "Les escarres sont des lesions ischemiques par compression ; prevention par retournement toutes les 2-3 heures et echelle de Norton",
        "L'immobilisation entraine une perte de 15-30% de la force du quadriceps des J8 : prevention musculaire des le premier jour",
        "La maladie d'Alzheimer est la premiere cause de demence : trouble memoire episodique non ameliore par l'indicage",
        "L'hydrocephalie a pression normale (triade de Hakim) est une cause curable de demence a toujours evoquer",
        "Le syndrome post-chute avec retropulsion est une urgence geriatrique necessitant hospitalisation",
        "Le modele de Bouchon 1+2+3 est fondamental : toujours rechercher le facteur precipitant (3) reversible et l'iatrogenie",
        "La fragilite (criteres de Fried >= 3/5) predit le risque de perte d'independance et permet des interventions preventives",
    ]

    fiche_eclair_md = (
        "**Denutrition** : DPE 30-70% a l'hopital. IMC normal 21-29,9. "
        "Albumine < 35 g/L (severe < 30). Proteines 1,2-1,5 g/kg/j. "
        "Vitamine D systematique > 65 ans. Strategie : conseils > enrichissement > CNO > NE. "
        "Attention regimes restrictifs proscrits.\n\n"
        "**Escarres** : compression > pression perfusion capillaire. "
        "Norton < 16 = a risque. Retournement /2-3h. "
        "Stades 0-4. Stades 0-1 : suppression appui. "
        "Stade 2 : evacuation phlyctene. Stades 3-4 : detersion + pansement.\n\n"
        "**Immobilite** : MTEV des premiers jours (anticoagulation preventive + contention). "
        "Hypotension orthostatique (verticalisation progressive). "
        "Amyotrophie -15 a -30% quadriceps J8. "
        "Desadaptation posturale chez sujet age.\n\n"
        "**Alzheimer** : 1ere cause demence. Memoire episodique (oubli a mesure). "
        "Anosognosie. Test 5 mots non ameliore par indicage. "
        "IRM : atrophie hippocampique. Diagnostic de probabilite. "
        "Traitements non rembourses.\n\n"
        "**Dependance** : ADL < 3 = tres dependant. AGGIR GIR 1-6. "
        "APA si > 60 ans et GIR 1-4. "
        "Hospitalisation = facteur de dependance iatrogene.\n\n"
        "**Chutes** : 1/3 des > 65 ans. TUG > 20 s, appui unipodal < 5 s. "
        "Syndrome post-chute = urgence geriatrique. "
        "CPK + creatinine si sol > 1h. "
        "Toujours reviser ordonnance + corriger FDR.\n\n"
        "**Fragilite** : 5 criteres de Fried (perte poids > 4,5 kg, fatigue, "
        "inactivite, vitesse marche, force prehension). "
        ">= 3 = fragile. Modele Bouchon 1+2+3 : "
        "rechercher facteur precipitant reversible."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Gériatrie",
        annee="2025-2026",
        item="Items 116, 119, 126, 128, 129, 130, 131",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
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
    captions_file = PROJECT_ROOT / "output" / ".work" / "geriatrie" / "image_captions.json"
    if captions_file.exists():
        try:
            captions = json.loads(captions_file.read_text(encoding="utf-8"))
            print(f"Loaded {len(captions)} image captions")
        except Exception as e:
            print(f"Warning: could not load image captions: {e}")

    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)

    docx_path = output_dir / "Medecine_generale_Geriatrie_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Medecine_generale_Geriatrie_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path} ({pdf_path.stat().st_size / 1e6:.1f} MB)")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

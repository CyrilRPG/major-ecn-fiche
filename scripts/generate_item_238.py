"""Génère la fiche de l'Item 238 - Souffle cardiaque chez l'enfant (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Généralités sur les cardiopathies de l'enfant", sous_parties=[
            PlanSousPartie(lettre="A", titre="Souffle organique vs anorganique"),
            PlanSousPartie(lettre="B", titre="Épidémiologie et orientation selon l'âge"),
        ]),
        PlanPartie(numero="II", titre="Particularités de l'auscultation de l'enfant", sous_parties=[
            PlanSousPartie(lettre="A", titre="Conditions techniques et rythme"),
            PlanSousPartie(lettre="B", titre="Bruits du cœur (B2, B3, clic)"),
        ]),
        PlanPartie(numero="III", titre="Circonstances de découverte", sous_parties=[
            PlanSousPartie(lettre="A", titre="Symptômes faisant suspecter une cardiopathie"),
            PlanSousPartie(lettre="B", titre="Anomalies de l'examen cardiovasculaire"),
            PlanSousPartie(lettre="C", titre="Symptômes extracardiaques"),
            PlanSousPartie(lettre="D", titre="Contextes particuliers et syndromes génétiques"),
        ]),
        PlanPartie(numero="IV", titre="Clinique et examens complémentaires", sous_parties=[
            PlanSousPartie(lettre="A", titre="Signes fonctionnels"),
            PlanSousPartie(lettre="B", titre="Caractéristiques du souffle"),
            PlanSousPartie(lettre="C", titre="Signes associés"),
            PlanSousPartie(lettre="D", titre="Examens complémentaires (RxT, ECG, ETT)"),
        ]),
        PlanPartie(numero="V", titre="Principales cardiopathies selon l'âge", sous_parties=[
            PlanSousPartie(lettre="A", titre="Nouveau-né (0-2 mois)"),
            PlanSousPartie(lettre="B", titre="Nourrisson (2 mois à la marche)"),
            PlanSousPartie(lettre="C", titre="Deuxième enfance (2-16 ans)"),
        ]),
        PlanPartie(numero="VI", titre="Souffles anorganiques (innocents)", sous_parties=[
            PlanSousPartie(lettre="A", titre="Caractéristiques sémiologiques"),
            PlanSousPartie(lettre="B", titre="Circonstances favorisantes et conduite à tenir"),
        ]),
    ]

    # ── PARTIE I : GÉNÉRALITÉS ──
    partie_i = Partie(numero="I", titre="Généralités sur les cardiopathies de l'enfant", sous_parties=[
        SousPartie(lettre="A", titre="Souffle organique vs anorganique", rows=[
            FicheRow(concept="◆ Définition d'un souffle de l'enfant", detail_md=(
                "- Découverte très fréquente en pédiatrie\n"
                "- Deux grandes catégories :\n"
                "  - **Souffle organique** : anomalie cardiaque anatomique sous-jacente\n"
                "  - **Souffle anorganique** (fonctionnel, « innocent ») : sans anomalie sous-jacente"
            )),
            FicheRow(concept="◆ Situations rencontrées", detail_md=(
                "- Malformation cardiaque congénitale : touche **1 % des enfants** à la naissance\n"
                "- Rarement : cardiomyopathie ou myocardite\n"
                "- Exceptionnellement : cardiopathie acquise\n"
                "  - Les valvulopathies rhumatismales ont disparu dans les pays occidentaux\n"
                "- Souffle fonctionnel (« innocent ») : surtout chez le grand enfant\n"
                "  - Concerne **1/3 à 1/2 des enfants d'âge scolaire**"
            )),
            FicheRow(concept="", detail_md=(
                "- La découverte d'un souffle cardiaque est une source d'anxiété majeure pour les parents : "
                "le plus souvent innocent, parfois seul point d'appel d'une cardiopathie congénitale."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Épidémiologie et orientation selon l'âge", rows=[
            FicheRow(concept="◆ Orientation selon l'âge", detail_md=(
                "- L'âge oriente d'emblée vers une cause organique ou fonctionnelle :\n"
                "  - **90 % des souffles du nourrisson** sont organiques\n"
                "  - **> 75 % des souffles de l'enfant d'âge scolaire** sont fonctionnels"
            )),
            FicheRow(concept="Répartition selon l'âge (tableau)", detail_md=(
                "| Tranche d'âge | Probabilité organique | Probabilité fonctionnelle |\n"
                "|---------------|----------------------|---------------------------|\n"
                "| Nourrisson | **~90 %** | ~10 % |\n"
                "| Âge scolaire | < 25 % | **> 75 %** |"
            )),
            FicheRow(concept="", detail_md=(
                "- Penser organique chez le petit, fonctionnel chez le grand — mais toujours vérifier "
                "les caractéristiques du souffle."
            ), kind="mnemo"),
        ]),
    ])

    # ── PARTIE II : AUSCULTATION ──
    partie_ii = Partie(numero="II", titre="Particularités de l'auscultation de l'enfant", sous_parties=[
        SousPartie(lettre="A", titre="Conditions techniques et rythme", rows=[
            FicheRow(concept="Conditions de l'auscultation", detail_md=(
                "- Auscultation difficile chez le petit enfant : cœur rapide, gênée par cris, pleurs, agitation\n"
                "- Distraire l'enfant : jouets, sucette, etc.\n"
                "- Utiliser un stéthoscope pédiatrique"
            )),
            FicheRow(concept="◆ Rythme cardiaque pédiatrique", detail_md=(
                "- Rythme rapide et souvent irrégulier\n"
                "- L'**arythmie sinusale respiratoire** est physiologique chez l'enfant et peut être très marquée\n"
                "- En cas de doute : **ECG** obligatoire"
            )),
        ]),
        SousPartie(lettre="B", titre="Bruits du cœur (B2, B3, clic)", rows=[
            FicheRow(concept="◆ Dédoublement du 2e bruit (DB2)", detail_md=(
                "- **DB2 variable** avec la respiration le long du bord sternal gauche : fréquent et physiologique\n"
                "- ⚠ **DB2 large et fixe** = anormal :\n"
                "  - Communication interatriale (CIA)\n"
                "  - Bloc de branche droit"
            )),
            FicheRow(concept="Éclat du 2e bruit", detail_md=(
                "- Accentuation / éclat de B2 le long du bord sternal gauche\n"
                "- Évoque une **hypertension artérielle pulmonaire (HTAP)**"
            )),
            FicheRow(concept="3e bruit (B3)", detail_md=(
                "- Fréquent à l'apex chez l'enfant (**50 % des cas**)\n"
                "- Physiologique"
            )),
            FicheRow(concept="Bruits surajoutés (clic)", detail_md=(
                "- Non exceptionnels chez l'enfant :\n"
                "  - **Clic mésosystolique apexien** (foyer mitral) : prolapsus mitral\n"
                "  - **Clic protosystolique** : sténose valvulaire d'un gros vaisseau (aorte ou artère pulmonaire)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Il n'y a **pas de corrélation entre l'intensité d'un souffle et la gravité** "
                "de la maladie sous-jacente."
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE III : CIRCONSTANCES DE DÉCOUVERTE ──
    partie_iii = Partie(numero="III", titre="Circonstances de découverte", sous_parties=[
        SousPartie(lettre="A", titre="Symptômes faisant suspecter une cardiopathie", rows=[
            FicheRow(concept="◆ Nouveau-né et nourrisson", detail_md=(
                "- **Cyanose** : coloration bleutée de la peau et des téguments\n"
                "  - Peut témoigner d'une hypoxie\n"
                "  - DD : hypothermie, hypoglycémie\n"
                "  - Mesure de la SpO2 : diagnostic d'**hypoxie réfractaire à l'O2** si origine cardiaque\n"
                "- **Insuffisance cardiaque** :\n"
                "  - Difficultés alimentaires\n"
                "  - Retard staturopondéral\n"
                "  - Signes respiratoires : polypnée, tirage, toux"
            )),
            FicheRow(concept="Enfant plus grand", detail_md=(
                "- Mêmes symptômes (plus rares)\n"
                "- Infections respiratoires à répétition\n"
                "- Dyspnée d'effort, fatigabilité\n"
                "- Rarement : syncope ou douleur thoracique d'effort\n"
                "  - Évoquer un **obstacle à l'éjection du VG** : sténose aortique ou cardiomyopathie obstructive\n"
                "- Parfois : AEG (anorexie, asthénie, douleurs abdominales)"
            )),
        ]),
        SousPartie(lettre="B", titre="Anomalies de l'examen cardiovasculaire", rows=[
            FicheRow(concept="◆ Signes orientant vers une cardiopathie", detail_md=(
                "- Présents même en l'absence de symptômes\n"
                "- **Hépatomégalie** = signe le plus pertinent d'insuffisance cardiaque chez nourrisson/enfant\n"
                "- Les œdèmes des membres inférieurs sont exceptionnels chez l'enfant\n"
                "- Souffle cardiaque découvert à un âge variable, anomalie des bruits du cœur\n"
                "- Plus rarement :\n"
                "  - **Absence de pouls fémoral** : oriente vers une coarctation aortique\n"
                "  - Trouble du rythme à l'auscultation"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ **Œdèmes des MI = exceptionnels** chez l'enfant : c'est l'hépatomégalie qui signe "
                "l'insuffisance cardiaque."
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Symptômes extracardiaques", rows=[
            FicheRow(concept="Signes faisant évoquer une cause cardiologique", detail_md=(
                "- Accident vasculaire cérébral (AVC)\n"
                "- Fièvre au long cours\n"
                "- Cassure de la courbe de croissance pondérale"
            )),
        ]),
        SousPartie(lettre="D", titre="Contextes particuliers et syndromes génétiques", rows=[
            FicheRow(concept="◆ Contextes à risque", detail_md=(
                "- **Syndrome polymalformatif** : échocardiographie systématique lors du bilan, "
                "qu'il y ait ou non symptômes/souffle\n"
                "- Maladie génétique familiale pouvant toucher cœur/gros vaisseaux : **syndrome de Marfan**\n"
                "- Cardiopathie congénitale familiale chez un apparenté du 1er degré"
            )),
            FicheRow(concept="◆ Syndromes génétiques associés aux cardiopathies congénitales", detail_md=(
                "- **Trisomie 21**\n"
                "- **Microdélétion 22q11** (syndrome de DiGeorge)\n"
                "- **Syndrome de Turner** (45, X0)\n"
                "- Syndrome de Williams-Beuren (microdélétion du chromosome 7)\n"
                "- Syndrome de Noonan\n"
                "- Syndrome CHARGE (coloboma, heart defect, atresia choanae, retarded growth, "
                "genital hypoplasia, ear anomalies)\n"
                "- **Syndrome de Marfan**"
            )),
            FicheRow(concept="Adressage au cardiopédiatre", detail_md=(
                "- Dans ces situations, adresser au cardiopédiatre\n"
                "- Bilan : examen clinique + **échocardiographie doppler** ± ECG\n"
                "- Conduit le plus souvent au diagnostic d'emblée"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant tout syndrome polymalformatif : **échocardiographie systématique**, "
                "même asymptomatique."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE IV : CLINIQUE ET EXAMENS ──
    partie_iv = Partie(numero="IV", titre="Clinique et examens complémentaires", sous_parties=[
        SousPartie(lettre="A", titre="Signes fonctionnels", rows=[
            FicheRow(concept="Signes fonctionnels", detail_md=(
                "- Souvent absents : souffle = découverte fortuite à l'examen systématique\n"
                "- **Dyspnée d'effort** : symptôme le plus commun\n"
                "- Douleurs thoraciques : fréquentes mais exceptionnellement d'origine cardiaque "
                "chez l'enfant (contrairement à l'adulte)"
            )),
            FicheRow(concept="◆ Malaises", detail_md=(
                "- Motif fréquent, mais rarement d'origine cardiaque\n"
                "- Petit nourrisson : spasmes du sanglot\n"
                "- Enfant plus grand / adolescent : malaises vagaux (communs)\n"
                "- Syncopes d'effort des obstacles aortiques : rares\n"
                "- Syncopes du BAV congénital ou canalopathies (**QT long congénital**, **Brugada**) : "
                "diagnostiquées par ECG et Holter"
            )),
        ]),
        SousPartie(lettre="B", titre="Caractéristiques du souffle", rows=[
            FicheRow(concept="◆ Éléments à préciser (comme l'adulte)", detail_md=(
                "- **Temps** : systolique, diastolique, systolodiastolique, continu, ou double souffle\n"
                "- Durée pour systolique : proto, méso, télé, holo\n"
                "- Caractère frémissant ou non\n"
                "- Topographie : foyers pulmonaire, aortique, mitral, tricuspidien, sous-claviculaire G, "
                "fontanelle antérieure (nourrisson)\n"
                "- Irradiations : dos, en écharpe base-apex, en rayons de roue précordium\n"
                "- Variabilité : respiration, position (couché/assis/debout), compression vasculaire\n"
                "- Modifications associées des bruits (DB2 fixe ou variable, éclat de B2)"
            )),
            FicheRow(concept="◆ Échelle d'intensité du souffle (1 à 6/6)", detail_md=(
                "| Grade | Description |\n"
                "|-------|-------------|\n"
                "| **1/6** | Très faible |\n"
                "| **2/6** | Faible mais entendu immédiatement |\n"
                "| **3/6** | Fort |\n"
                "| **4/6** | Avec **thrill** ou entendu avec rebord du stéthoscope |\n"
                "| **5/6** | Entendu à distance du thorax avec stéthoscope |\n"
                "| **6/6** | Entendu à distance du thorax sans stéthoscope |"
            )),
            FicheRow(concept="◆ Orientation diagnostique selon les caractéristiques", detail_md=(
                "- Souffle variable dans le temps et avec la position : presque toujours innocent "
                "(caractère inconstant)\n"
                "- Souffles innocents : irradient peu\n"
                "- Souffle bruyant, irradiant largement : a priori organique\n"
                "- Souffle **diastolique** ou **double souffle** : toujours organique\n"
                "  - Souffles innocents : presque toujours systoliques, parfois systolodiastoliques "
                "(souffle « veineux » du cou)\n"
                "- Souffle **frémissant** : toujours organique\n"
                "- Souffle innocent : toujours bref dans la systole"
            )),
            FicheRow(concept="◆ Topographie et orientation", detail_md=(
                "- Cou + sus-sternal (entendu/frémissant) : **obstacle aortique** probable\n"
                "- Dos : **obstacle pulmonaire**\n"
                "- Panradiant (toutes directions) à partir de la région mésocardiaque : "
                "**communication interventriculaire (CIV)**"
            )),
            FicheRow(concept="", detail_md=(
                "- Tout souffle **diastolique, double, frémissant ou panradiant** est organique "
                "jusqu'à preuve du contraire."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Signes associés", rows=[
            FicheRow(concept="◆ Cyanose", detail_md=(
                "- Cyanose discrète si **SpO2 transcutanée > 80-85 %** : diagnostic difficile\n"
                "- Cyanose clinique apparaît quand **SpO2 < 85 %**\n"
                "- À rechercher : ongles, lèvres, muqueuse buccale\n"
                "- **Hypoxie cardiaque** = réfractaire à l'O2 (non modifiée par O2 à 100 %)\n"
                "- **Hypoxie bronchopulmonaire** = sensible à l'oxygénothérapie"
            )),
            FicheRow(concept="◆ Insuffisance cardiaque", detail_md=(
                "- Moins typique que chez l'adulte\n"
                "- Signes chez le nourrisson :\n"
                "  - Respiratoires : polypnée, tirage, toux\n"
                "  - Digestifs : difficultés alimentaires, vomissements postprandiaux, stagnation pondérale\n"
                "  - ⚠ Peuvent égarer vers une pathologie bronchopulmonaire ou gastro-intestinale\n"
                "- Examen : polypnée de repos, tachycardie, **hépatomégalie** (signe majeur)"
            )),
            FicheRow(concept="Retard staturopondéral", detail_md=(
                "- Lié aux difficultés alimentaires, mauvaise prise des biberons, dyspnée, sueurs\n"
                "- Fréquent dans les larges shunts du nourrisson\n"
                "- Croissance pondérale = paramètre clinique important"
            )),
            FicheRow(concept="◆ Anomalies de l'examen physique", detail_md=(
                "- **HTA + absence de pouls fémoraux** : oriente vers **coarctation aortique**\n"
                "  - Mesure de PA avec brassard pédiatrique adapté, membre sup ET inf\n"
                "- Palpation des pouls : présence et amplitude, comparer MS (huméraux) et MI (fémoraux)\n"
                "- **Frémissement (thrill)** précordial ou sus-sternal = toujours pathologique\n"
                "- FC diminue avec l'âge : un rythme rapide au repos peut signer une IC"
            )),
            FicheRow(concept="◆ Autres anomalies auscultatoires", detail_md=(
                "- **DB2 fixe et invariable** : anormal\n"
                "- **Éclat de B2** : élévation anormale de la pression pulmonaire\n"
                "- **Clic protosystolique** : bruit anormal d'ouverture valvulaire\n"
                "- Galop avec B3"
            )),
            FicheRow(concept="", detail_md=(
                "- La présence d'un seul de ces signes suffit à adresser au spécialiste qui réalise "
                "une **échocardiographie systématique**, un ECG, et rarement une RxT."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Examens complémentaires (RxT, ECG, ETT)", rows=[
            FicheRow(concept="◆ Radiographie de thorax", detail_md=(
                "- **Cardiomégalie** : oriente vers cardiopathie (malformative > cardiomyopathie / myocardite)\n"
                "  - ⚠ Attention aux fausses cardiomégalies par superposition du thymus\n"
                "- Saillie de l'arc moyen gauche : dilatation du tronc de l'AP → **shunt G-D**\n"
                "- Arc moyen gauche concave : hypoplasie de la voie pulmonaire proximale → **tétralogie de Fallot**\n"
                "- Pédicule vasculaire étroit : anomalie de position des gros vaisseaux\n"
                "- Hypervascularisation pulmonaire : hyperdébit = **shunt G-D**\n"
                "- Hypovascularisation pulmonaire : **obstacle pulmonaire**"
            )),
            FicheRow(concept="◆ Électrocardiogramme", detail_md=(
                "- ECG différent de l'adulte, varie avec l'âge : **toujours interpréter selon l'âge**\n"
                "- FC d'autant plus rapide que l'enfant est jeune\n"
                "- Axe QRS plus droit que chez l'adulte, PR plus court\n"
                "- Ondes T : positives en précordiales droites à la naissance, se négativent fin de "
                "1re semaine, restent négatives de V1 à V4 pendant l'enfance\n"
                "- Arythmie sinusale respiratoire = banale chez l'enfant"
            )),
            FicheRow(concept="◆ Échocardiographie cardiaque", detail_md=(
                "- **Examen clé du diagnostic** : permet de porter un diagnostic précis\n"
                "- Qualité constamment bonne chez l'enfant\n"
                "- Réalisation parfois difficile (agitation du patient)\n"
                "- Conditions indispensables :\n"
                "  - Appareillage performant\n"
                "  - Capteurs pédiatriques spécifiques\n"
                "  - Opérateur expérimenté, formé aux cardiopathies congénitales"
            )),
            FicheRow(concept="Autres examens paracliniques", detail_md=(
                "- Épreuve d'effort : tapis roulant (petit) ou bicyclette ergométrique\n"
                "- Holter ECG : troubles du rythme idiopathiques ou postopératoires\n"
                "- IRM cardiaque : très performante, surtout pour les gros vaisseaux intrathoraciques\n"
                "- Scanner : bonne résolution spatiale mais irradiant\n"
                "- Cathétérisme cardiaque :\n"
                "  - Indications limitées chez l'enfant pour le diagnostic\n"
                "  - Sous **anesthésie générale avant 10 ans**\n"
                "  - Réservé au bilan préopératoire des cardiopathies complexes ou en "
                "cathétérisme interventionnel"
            )),
        ]),
    ])

    # ── PARTIE V : CARDIOPATHIES SELON L'ÂGE ──
    partie_v = Partie(numero="V", titre="Principales cardiopathies selon l'âge", sous_parties=[
        SousPartie(lettre="A", titre="Nouveau-né (0-2 mois)", rows=[
            FicheRow(concept="◆ Souffle isolé chez le nouveau-né", detail_md=(
                "- Souffle en période néonatale, même asymptomatique = **toujours potentiellement pathologique**\n"
                "- **Échocardiographie obligatoire avant la sortie de maternité**\n"
                "- Bilan à réaliser :\n"
                "  - Examen clinique complet\n"
                "  - Échographie cardiaque systématique\n"
                "  - ECG (souvent)\n"
                "  - Radiographie pulmonaire de face (souvent)"
            )),
            FicheRow(concept="◆ Coarctation aortique", detail_md=(
                "- Sténose de l'**isthme de l'aorte**\n"
                "- Symptômes dès les premiers jours de vie à la fermeture du canal artériel\n"
                "- **Pouls fémoraux abolis**\n"
                "- Tableau bruyant, **chirurgie urgente**\n"
                "- Souffle systolique, doux, sous-claviculaire gauche, irradiant en interscapulaire dans le dos"
            )),
            FicheRow(concept="◆ Cardiopathies avec cyanose néonatale", detail_md=(
                "- **Transposition des gros vaisseaux (TGV)** :\n"
                "  - Cause la plus classique de cyanose néonatale\n"
                "  - **Pas de souffle cardiaque**\n"
                "  - Urgence cardiologique néonatale type\n"
                "- **Obstacle sur la voie pulmonaire** (sténose valvulaire pulmonaire serrée) :\n"
                "  - Shunt droite-gauche par FOP\n"
                "  - Souffle systolique râpeux au foyer pulmonaire avec clic protosystolique "
                "(si sténose valvulaire)\n"
                "- **Cardiopathies complexes** :\n"
                "  - Ventricule unique, tronc artériel commun, etc.\n"
                "  - Cyanose + défaillance cardiaque variables\n"
                "  - Souffle absent ou faible"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La **TGV est cyanogène SANS souffle** : ne pas écarter le diagnostic devant "
                "l'absence d'auscultation pathologique."
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Nourrisson (2 mois à la marche)", rows=[
            FicheRow(concept="◆ Cardiopathies avec insuffisance cardiaque (shunts G-D)", detail_md=(
                "- Shunts gauche-droite : les plus fréquents\n"
                "- **Communication interventriculaire (CIV)** :\n"
                "  - Si petite, restrictive : souffle holosystolique, râpeux, intense, parasternal G, "
                "irradiant en rayons de roue\n"
                "  - Si large : souffle faible + B1 fort à la pointe\n"
                "- **Persistance du canal artériel (PCA)** : souffle continu au bord G du sternum, "
                "crescendo en systole et decrescendo en diastole\n"
                "- **Canal atrioventriculaire (CAV)** : chez le patient trisomique 21"
            )),
            FicheRow(concept="◆ Risque d'HTAP irréversible", detail_md=(
                "- **Risque d'HTAP irréversible** si shunt opéré trop tard\n"
                "- Opérer tôt les nourrissons porteurs de larges shunts (surtout CIV)\n"
                "- En général dans la **1re année de vie**"
            )),
            FicheRow(concept="◆ Tétralogie de Fallot", detail_md=(
                "- **Cardiopathie cyanogène la plus fréquente**\n"
                "- Cyanose retardée (forme régulière) : apparaît après quelques semaines ou mois\n"
                "- Souffle systolique, râpeux, au foyer pulmonaire, sans clic protosystolique\n"
                "- **Correction chirurgicale entre 6 mois et 1 an**\n"
                "- Cardiopathies complexes : généralement déjà diagnostiquées en néonatal ou anténatal"
            )),
            FicheRow(concept="", detail_md=(
                "- **CIV** = malformation la plus fréquente chez le nourrisson ; **Fallot** = cyanogène la "
                "plus fréquente."
            ), kind="mnemo"),
        ]),
        SousPartie(lettre="C", titre="Deuxième enfance (2-16 ans)", rows=[
            FicheRow(concept="◆ Communication interatriale (CIA)", detail_md=(
                "- Cardiopathie en général bien tolérée\n"
                "- Souffle systolique au foyer pulmonaire (lié à l'hyperdébit)\n"
                "- **Dédoublement fixe et constant de B2** (retard de fermeture de la valve pulmonaire)"
            )),
            FicheRow(concept="◆ Coarctation aortique (forme progressive)", detail_md=(
                "- Signe d'appel : **HTA + diminution des pouls fémoraux**\n"
                "- Gradient tensionnel MS/MI\n"
                "- Souffle systolique, doux, sous-claviculaire gauche irradiant en interscapulaire dans le dos"
            )),
            FicheRow(concept="Sténose valvulaire pulmonaire", detail_md=(
                "- Diagnostiquée à différents âges selon sa sévérité\n"
                "- Peut se traduire par une dyspnée d'effort chez le grand enfant"
            )),
        ]),
    ])

    # ── PARTIE VI : SOUFFLES ANORGANIQUES ──
    partie_vi = Partie(numero="VI", titre="Souffles anorganiques (innocents)", sous_parties=[
        SousPartie(lettre="A", titre="Caractéristiques sémiologiques", rows=[
            FicheRow(concept="◆ Épidémiologie", detail_md=(
                "- Fréquents : concernent **1/3 à 1/2 des enfants** à un moment de l'enfance\n"
                "- Surtout chez l'enfant d'âge scolaire\n"
                "- Rares chez le nourrisson et le nouveau-né\n"
                "- **Aucun substrat organique** : cœur parfaitement sain\n"
                "- Disparaissent avec l'âge, mais peuvent persister chez de jeunes adultes"
            )),
            FicheRow(concept="◆ Caractéristiques du souffle innocent", detail_md=(
                "- Isolé ou asymptomatique (sans signe associé)\n"
                "- **Systolique** (jamais diastolique) ou parfois continu\n"
                "- Proto ou mésosystolique (jamais télésystolique)\n"
                "- Éjectionnel, généralement bref (1er tiers de la systole)\n"
                "- **Faible intensité, < 3/6**\n"
                "- Souvent d'intensité variable avec la position\n"
                "- Doux, parfois musical\n"
                "- **Sans irradiation ni frémissement**"
            )),
            FicheRow(concept="◆ Bruits du cœur et examen", detail_md=(
                "- Pas de modification de B1 ni B2 (DB2 variable possible)\n"
                "- Reste de l'examen clinique normal : pouls fémoraux perçus, PA normale, etc.\n"
                "- Cœur normal à la RxT, à l'ECG et à l'ETT"
            )),
            FicheRow(concept="◆ Conduite à tenir si critères réunis", detail_md=(
                "- **Aucun examen complémentaire indiqué** si toutes les caractéristiques sont réunies\n"
                "- Échocardiographie pratiquée uniquement en cas de doute"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Un souffle diastolique, frémissant, bruyant ou avec irradiation "
                "**n'est jamais innocent** : référer au cardiopédiatre."
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Circonstances favorisantes et conduite à tenir", rows=[
            FicheRow(concept="◆ Circonstances favorisantes", detail_md=(
                "- Causes d'augmentation du débit cardiaque :\n"
                "  - Fièvre\n"
                "  - Effort\n"
                "  - Émotion\n"
                "  - Anémie\n"
                "  - Hyperthyroïdie\n"
                "- Anomalies morphologiques :\n"
                "  - Dos droit / dos plat\n"
                "  - Thorax en entonnoir\n"
                "  - Scolioses"
            )),
            FicheRow(concept="◆ Conduite à tenir et information", detail_md=(
                "- **Aucune thérapeutique, surveillance ni restriction d'activité**\n"
                "- Vie strictement normale : ces enfants ne sont pas malades\n"
                "- **Tous les sports autorisés**, y compris en compétition\n"
                "- Inutile de revoir l'enfant en consultation\n"
                "- Conclusion ferme et précise dès le 1er examen pour rassurer la famille"
            )),
            FicheRow(concept="Pourquoi entend-on un souffle fonctionnel ?", detail_md=(
                "- Bruit normal du flux sanguin lors de l'éjection du sang\n"
                "- Entendu car :\n"
                "  - Distance cœur-stéthoscope plus faible\n"
                "  - Cavités cardiaques de plus petite taille\n"
                "- Disparaît à l'âge adulte\n"
                "- **Avant 3 mois** : peut être lié à une accélération du flux sur les branches pulmonaires "
                "(différence de calibre tronc/branches pulmonaires)"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant un souffle innocent typique : **rassurer fermement**, **aucun suivi**, "
                "**aucune restriction sportive**, **pas de revoyure**."
            ), kind="a_retenir"),
        ]),
    ])

    tableaux = [
        TableauSynthese(titre="Organique vs anorganique : critères différentiels", markdown=(
            "| Caractéristique | Organique | Innocent (anorganique) |\n"
            "|-----------------|-----------|------------------------|\n"
            "| Temps | Systolique, diastolique, continu, double | Systolique (parfois continu) |\n"
            "| Durée | Variable, parfois holosystolique | **Bref**, 1er tiers de systole |\n"
            "| Intensité | Souvent ≥ 3/6 | **< 3/6** |\n"
            "| Frémissement (thrill) | Possible (toujours pathologique) | **Jamais** |\n"
            "| Irradiation | Large possible | **Peu ou pas** |\n"
            "| Variabilité position | Inconstante | **Souvent variable** |\n"
            "| Caractère | Râpeux, panradiant | Doux, musical |\n"
            "| Signes associés | Cyanose, IC, anomalies pouls, DB2 fixe | **Aucun** |\n"
            "| ECG / RxT / ETT | Anormaux | **Normaux** |"
        )),
        TableauSynthese(titre="Principales cardiopathies par âge", markdown=(
            "| Tranche d'âge | Principales cardiopathies | Souffle caractéristique |\n"
            "|---------------|---------------------------|--------------------------|\n"
            "| Nouveau-né | **Coarctation aortique** | Systolique doux sous-claviculaire G, irradiant dos |\n"
            "| Nouveau-né | **TGV** | **Pas de souffle** (cyanose) |\n"
            "| Nouveau-né | Sténose pulmonaire serrée | Systolique râpeux foyer pulmonaire + clic |\n"
            "| Nouveau-né | Cardiopathies complexes (ventricule unique, TAC) | Variable ou absent |\n"
            "| Nourrisson | **CIV restrictive** | Holosystolique râpeux parasternal G, rayons de roue |\n"
            "| Nourrisson | **CIV large** | Souffle faible + B1 fort apex |\n"
            "| Nourrisson | **PCA** | Continu, crescendo-decrescendo, bord G sternum |\n"
            "| Nourrisson | **CAV** (T21) | — |\n"
            "| Nourrisson | **Tétralogie de Fallot** | Systolique râpeux foyer pulmonaire, sans clic |\n"
            "| 2e enfance | **CIA** | Systolique foyer pulmonaire + **DB2 fixe** |\n"
            "| 2e enfance | Coarctation progressive | Systolique doux sous-claviculaire G, dos |\n"
            "| 2e enfance | Sténose valvulaire pulmonaire | Dyspnée d'effort |"
        )),
        TableauSynthese(titre="Signes d'examen orientant vers une cardiopathie", markdown=(
            "| Signe | Évoque |\n"
            "|-------|--------|\n"
            "| **Cyanose réfractaire à l'O2** | Cardiopathie cyanogène |\n"
            "| **Hépatomégalie** | Insuffisance cardiaque (signe majeur du nourrisson) |\n"
            "| **Absence pouls fémoraux + HTA** | Coarctation aortique |\n"
            "| **Thrill précordial / sus-sternal** | Toujours pathologique |\n"
            "| **DB2 fixe et large** | CIA, bloc de branche droit |\n"
            "| **Éclat de B2** | HTAP |\n"
            "| **Clic protosystolique** | Sténose valvulaire (aorte / AP) |\n"
            "| **Clic mésosystolique apexien** | Prolapsus mitral |\n"
            "| **Galop B3** | Insuffisance cardiaque |\n"
            "| Œdèmes MI | Exceptionnels chez l'enfant |"
        )),
        TableauSynthese(titre="Syndromes génétiques associés aux cardiopathies congénitales", markdown=(
            "| Syndrome | Anomalie génétique |\n"
            "|----------|--------------------|\n"
            "| Trisomie 21 | Trisomie chromosome 21 |\n"
            "| Syndrome de DiGeorge | **Microdélétion 22q11** |\n"
            "| Syndrome de Turner | **45, X0** |\n"
            "| Syndrome de Williams-Beuren | Microdélétion chromosome 7 |\n"
            "| Syndrome de Noonan | — |\n"
            "| Syndrome CHARGE | Coloboma, heart defect, atresia choanae, growth retard, génital, oreille |\n"
            "| Syndrome de Marfan | — |"
        )),
        TableauSynthese(titre="Échelle d'intensité du souffle (1-6/6)", markdown=(
            "| Grade | Définition |\n"
            "|-------|-----------|\n"
            "| 1/6 | Très faible |\n"
            "| 2/6 | Faible mais entendu immédiatement |\n"
            "| 3/6 | Fort |\n"
            "| 4/6 | Avec **thrill** ou rebord du stéthoscope |\n"
            "| 5/6 | À distance du thorax **avec** stéthoscope |\n"
            "| 6/6 | À distance du thorax **sans** stéthoscope |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Cardiopathie congénitale à la naissance | **1 %** | Prévalence |\n"
        "| Souffles organiques chez le nourrisson | **90 %** | Orientation selon l'âge |\n"
        "| Souffles fonctionnels en âge scolaire | **> 75 %** | Orientation selon l'âge |\n"
        "| Enfants avec souffle innocent | **1/3 à 1/2** | Enfants d'âge scolaire |\n"
        "| B3 physiologique à l'apex | **50 %** | Auscultation pédiatrique |\n"
        "| Cyanose clinique visible | SpO2 **< 85 %** | Seuil détection |\n"
        "| Cyanose discrète difficile | SpO2 **80-85 %** | Diagnostic difficile |\n"
        "| Intensité d'un souffle innocent | **< 3/6** | Critère essentiel |\n"
        "| Échelle d'intensité | **1 à 6/6** | Sémiologie auscultatoire |\n"
        "| Négativation des ondes T en V1-V4 | Fin **1re semaine** | ECG pédiatrique |\n"
        "| Cathétérisme cardiaque sous AG | Avant **10 ans** | Conditions |\n"
        "| Correction chirurgicale Fallot | **6 mois - 1 an** | Calendrier |\n"
        "| Opération des larges shunts (CIV) | Dans la **1re année** | Prévention HTAP |\n"
        "| CIV large : diamètre | **8 mm** (exemple iconographie) | Repère |"
    ))

    points_cles = [
        "Souffle de l'enfant : **organique** (anomalie anatomique) vs **anorganique / innocent**",
        "**90 %** des souffles du nourrisson organiques ; **> 75 %** en âge scolaire fonctionnels",
        "Auscultation pédia : tachycardie, **DB2 variable**, **B3 apex (50 %)** physiologiques",
        "**Pas de parallélisme** entre intensité du souffle et gravité de la cardiopathie",
        "Tout souffle néonatal = potentiellement pathologique → **ETT avant sortie maternité**",
        "Signes d'alerte : **cyanose réfractaire O2**, **hépatomégalie**, **pouls fémoraux abolis**, **thrill**",
        "**ETT** = examen clé du diagnostic ; ECG et RxT seulement en orientation",
        "Syndromes (T21, DiGeorge, Turner, Marfan...) → **échocardiographie systématique**",
        "Cardiopathies : néonatal = **coarctation/TGV** ; nourrisson = **CIV/Fallot** ; 2e enfance = **CIA**",
        "Innocent : **systolique, < 3/6, bref, sans irradiation** → aucun suivi ni restriction sportive",
    ]

    fiche_eclair_md = (
        "**Définition** : organique (anatomique) vs anorganique (innocent). 1 % cardiopathies congénitales.\n\n"
        "**Orientation âge** : 90 % organiques chez nourrisson, > 75 % fonctionnels en âge scolaire.\n\n"
        "**Auscultation pédia** : tachycardie, arythmie sinusale resp, DB2 variable, B3 apex 50 %. "
        "DB2 fixe = CIA/BBD. Éclat B2 = HTAP. Pas de parallélisme intensité-gravité.\n\n"
        "**Toujours organique** : diastolique, double, frémissant, panradiant.\n\n"
        "**Souffle innocent** : systolique bref, < 3/6, doux, sans irradiation ni frémissement, "
        "examen normal. Aucun examen, aucun traitement, aucune restriction sportive.\n\n"
        "**Signes IC enfant** : hépatomégalie = signe majeur. Œdèmes MI exceptionnels. Cyanose réfractaire "
        "à l'O2 (SpO2 < 85 %).\n\n"
        "**Nouveau-né** : coarctation (pouls fémoraux abolis), TGV (cyanose SANS souffle), sténose pulmonaire. "
        "ETT avant sortie maternité.\n\n"
        "**Nourrisson** : shunts G-D (CIV, PCA, CAV chez T21). Fallot = cyanogène la plus fréquente. "
        "Opérer CIV large dans la 1re année (HTAP).\n\n"
        "**2e enfance** : CIA + DB2 fixe, coarctation progressive (HTA + pouls fémoraux ↓).\n\n"
        "**Examens** : ETT = examen clé. Cathétérisme sous AG avant 10 ans.\n\n"
        "**Syndromes** : T21, DiGeorge 22q11, Turner, Williams-Beuren, Noonan, CHARGE, Marfan."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 238 - Souffle cardiaque chez l'enfant",
        annee="2025-2026",
        item="Item 238",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 238",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-238_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

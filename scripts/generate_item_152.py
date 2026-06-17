"""Génère la fiche de l'Item 152 - Endocardite infectieuse (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Généralités, épidémiologie et physiopathologie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition"),
            PlanSousPartie(lettre="B", titre="Épidémiologie"),
            PlanSousPartie(lettre="C", titre="Micro-organismes en cause"),
            PlanSousPartie(lettre="D", titre="Physiopathologie et lésions"),
        ]),
        PlanPartie(numero="II", titre="Groupes à risque et prise en charge multidisciplinaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Patients à haut risque"),
            PlanSousPartie(lettre="B", titre="Patients à risque intermédiaire"),
            PlanSousPartie(lettre="C", titre="Équipe endocardite"),
        ]),
        PlanPartie(numero="III", titre="Diagnostic clinique et paraclinique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Signes cliniques"),
            PlanSousPartie(lettre="B", titre="Identification microbiologique"),
            PlanSousPartie(lettre="C", titre="Imagerie cardiaque"),
            PlanSousPartie(lettre="D", titre="Autres examens complémentaires"),
        ]),
        PlanPartie(numero="IV", titre="Formes cliniques et critères diagnostiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="EI du cœur droit"),
            PlanSousPartie(lettre="B", titre="EI sur prothèses valvulaires"),
            PlanSousPartie(lettre="C", titre="Critères diagnostiques ESC 2023"),
        ]),
        PlanPartie(numero="V", titre="Complications et pronostic", sous_parties=[
            PlanSousPartie(lettre="A", titre="Mortalité et complications"),
            PlanSousPartie(lettre="B", titre="Facteurs de mauvais pronostic"),
        ]),
        PlanPartie(numero="VI", titre="Traitement médical et chirurgical", sous_parties=[
            PlanSousPartie(lettre="A", titre="Principes de l'antibiothérapie"),
            PlanSousPartie(lettre="B", titre="Surveillance du traitement"),
            PlanSousPartie(lettre="C", titre="Indications chirurgicales"),
        ]),
        PlanPartie(numero="VII", titre="Prévention", sous_parties=[
            PlanSousPartie(lettre="A", titre="Mesures non spécifiques d'éducation"),
            PlanSousPartie(lettre="B", titre="Antibioprophylaxie"),
        ]),
    ]

    # ── PARTIE I : GÉNÉRALITÉS, ÉPIDÉMIOLOGIE ET PHYSIOPATHOLOGIE ──
    partie_i = Partie(numero="I", titre="Généralités, épidémiologie et physiopathologie", sous_parties=[
        SousPartie(lettre="A", titre="Définition", rows=[
            FicheRow(concept="◆ Définition de l'EI", detail_md=(
                "- **Endocardite infectieuse (EI)** : infection de l'endocarde\n"
                "  - Touche le plus souvent une ou plusieurs valves cardiaques natives\n"
                "  - Peut aussi atteindre l'endocarde pariétal ou tout matériel intracardiaque implanté :\n"
                "    - Prothèses valvulaires\n"
                "    - Sondes de stimulateurs ou défibrillateurs\n"
                "    - Assistances ventriculaires\n"
                "    - Cathéter veineux central\n"
                "- Agent causal : **bactérie** (le plus souvent) ou plus rarement un **champignon** (agent fongique)"
            )),
            FicheRow(concept="Endocardites non infectieuses (rares)", detail_md=(
                "- Endocardites **marastiques** : liées aux cancers\n"
                "- Maladies auto-immunes :\n"
                "  - **Lupus** (lésions de **Libman-Sacks**)\n"
                "  - Syndrome des anticorps antiphospholipides"
            )),
            FicheRow(concept="", detail_md=(
                "- L'EI peut toucher des valves natives ET du matériel intracardiaque implanté\n"
                "- L'agent causal est presque toujours une **bactérie**, rarement un champignon"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Épidémiologie", rows=[
            FicheRow(concept="◆ Évolution épidémiologique", detail_md=(
                "- Incidence de l'EI **n'a pas diminué** au cours des dernières décennies\n"
                "- Profil des patients et répartition des micro-organismes modifiés car :\n"
                "  - Vieillissement de la population\n"
                "  - Progrès médicaux\n"
                "  - Modification des modes de vie\n"
                "  - Régression des valvulopathies post-rhumatismales\n"
                "- Patients désormais plus âgés avec d'autres situations à risque"
            )),
            FicheRow(concept="Situations exposant à l'EI", detail_md=(
                "- **Valvulopathies dégénératives** : fibrose, prolapsus mitral\n"
                "- Procédures de soins à risque en augmentation :\n"
                "  - Chirurgie cardiaque sous circulation extracorporelle\n"
                "  - Implantation de dispositifs médicaux par voie percutanée (valves percutanées, clips valvulaires, fermeture de shunt, exclusion de l'auricule gauche)\n"
                "  - Assistance ventriculaire, cœur artificiel\n"
                "  - Cathéters veineux, cathétérisme cardiaque\n"
                "  - Hémodialyse\n"
                "  - Implantation de stimulateur/défibrillateur cardiaque\n"
                "  - Ponction articulaire\n"
                "  - Chambre implantable sous-cutanée\n"
                "- **Toxicomanie intraveineuse**"
            )),
        ]),
        SousPartie(lettre="C", titre="Micro-organismes en cause", rows=[
            FicheRow(concept="◆ Micro-organismes les plus fréquents", detail_md=(
                "- Bactéries (le plus souvent) ; champignons (rarement)\n"
                "- Infection à partir d'une porte d'entrée infectieuse\n"
                "- Cocci Gram positif prédominants :\n"
                "  - En amas : *Staphylococcus aureus* et staphylocoques coagulase-négative\n"
                "  - En chaînettes : streptocoques et entérocoques\n"
                "- ◆ ***Staphylococcus aureus*** = cause la plus fréquente actuellement"
            )),
            FicheRow(concept="Portes d'entrée selon le germe", detail_md=(
                "| Germe | Porte d'entrée |\n"
                "|-------|----------------|\n"
                "| Staphylocoques, *Candida* | **Cutanée** |\n"
                "| Streptocoques oraux, HACEK | **Buccodentaire** |\n"
                "| Streptocoques D (*S. gallolyticus*) | **Digestive (coloscopie)** |\n"
                "| Entérocoques | **Digestive, urinaire** |"
            )),
            FicheRow(concept="Groupe HACEK", detail_md=(
                "- **HACEK** = micro-organismes à croissance lente :\n"
                "  - ***H****aemophilus* spp.\n"
                "  - ***A****ggregatibacter actinomycetemcomitans*\n"
                "  - ***C****ardiobacterium hominis*\n"
                "  - ***E****ikenella corrodens*\n"
                "  - ***K****ingella kingae*"
            )),
        ]),
        SousPartie(lettre="D", titre="Physiopathologie et lésions", rows=[
            FicheRow(concept="Séquence physiopathologique", detail_md=(
                "- **1) Bactériémie/fongémie** importante et/ou répétée à partir d'une porte d'entrée\n"
                "- **2) Colonisation** de lésions endocardiques préexistantes par les micro-organismes\n"
                "  - 2 groupes de patients à risque (haut / intermédiaire)\n"
                "  - **50 % des cas** : lésions non connues ou absentes avant l'EI\n"
                "  - Si germe très virulent (ex : *S. aureus*) : infection possible sur endocarde sain\n"
                "- **3) Apparition** de lésions infectieuses endocardiques et systémiques"
            )),
            FicheRow(concept="◆ Lésions endocardiques caractéristiques", detail_md=(
                "- **Végétations** : lésions élémentaires proliférantes\n"
                "  - Amas de fibrine, plaquettes, cellules inflammatoires et micro-organismes\n"
                "  - Sources d'embolies : accidents ischémiques systémiques (EI gauche), embolies pulmonaires septiques (EI droite), foyers infectieux à distance\n"
                "  - Rarement : obstruction de l'orifice valvulaire\n"
                "- **Destructions valvulaires** : mutilations, perforations, ruptures de cordages ou de sigmoïdes de bioprothèse\n"
                "  - Responsables de régurgitations (fuites) aiguës et d'insuffisance cardiaque\n"
                "- **Abcès** : collection de pus\n"
                "  - Peut créer un **BAV** si localisé près des voies de conduction (abcès septal des EI aortiques)\n"
                "  - Peut se rompre et créer un faux anévrisme ou une fistule intracardiaque\n"
                "- **Désinsertions de prothèses** valvulaires avec fuite paraprothétique"
            )),
            FicheRow(concept="Phénomènes systémiques", detail_md=(
                "- Choc septique\n"
                "- **Anévrismes infectieux (mycotiques)** : risque hémorragique\n"
                "- Glomérulonéphrite (immunologique)\n"
                "- Purpura vasculaire\n"
                "- Lésions cutanéomuqueuses et ophtalmiques :\n"
                "  - **Faux panaris d'Osler**\n"
                "  - **Placards de Janeway**\n"
                "  - **Taches rétiniennes de Roth**\n"
                "- Présence de facteurs rhumatoïdes et éventuellement de cryoglobulinémie"
            )),
            FicheRow(concept="", detail_md=(
                "- Les **3 lésions cardinales** de l'EI : végétations, destructions valvulaires, abcès\n"
                "- L'abcès septal d'une EI aortique = cause classique de **BAV**"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE II : GROUPES À RISQUE ET PRISE EN CHARGE MULTIDISCIPLINAIRE ──
    partie_ii = Partie(numero="II", titre="Groupes à risque et prise en charge multidisciplinaire", sous_parties=[
        SousPartie(lettre="A", titre="Patients à haut risque", rows=[
            FicheRow(concept="★ ◆ Critères du groupe à haut risque", detail_md=(
                "- **Antécédent d'endocardite infectieuse**\n"
                "- **Prothèses valvulaires** :\n"
                "  - Implantées par voie chirurgicale\n"
                "  - Implantées par voie percutanée (**TAVI** inclus)\n"
                "  - Tout matériau utilisé pour la réparation des valves\n"
                "- Dispositifs particuliers (haut risque pendant les **6 premiers mois**) :\n"
                "  - Dispositifs de fermeture de CIV et d'auricule gauche\n"
                "  - Prothèses vasculaires\n"
                "  - Filtres de la veine cave\n"
                "  - Shunts ventriculoatriaux\n"
                "- **Cardiopathie congénitale cyanogène** non traitée ou réparée avec matériel prothétique\n"
                "  - **6 mois** si correction chirurgicale sans prothèse\n"
                "- **Dispositif d'assistance ventriculaire**"
            )),
        ]),
        SousPartie(lettre="B", titre="Patients à risque intermédiaire", rows=[
            FicheRow(concept="Critères du groupe à risque intermédiaire", detail_md=(
                "- Valvulopathies dégénératives\n"
                "- Valvulopathies congénitales (ex : **bicuspidie aortique**)\n"
                "- Cardiopathie post-rhumatismale\n"
                "- Cardiomyopathie hypertrophique\n"
                "- Stimulateur et défibrillateur cardiaque implantables"
            )),
            FicheRow(concept="", detail_md=(
                "- Les 2 groupes à risque (haut/intermédiaire) déterminent les indications de l'**antibioprophylaxie**\n"
                "- Seul le **groupe à haut risque** bénéficie de l'antibioprophylaxie\n"
                "- Dans **50 % des cas**, la cardiopathie à risque n'était pas connue ou était absente"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Équipe endocardite", rows=[
            FicheRow(concept="◆ Composition minimale de l'équipe", detail_md=(
                "- Diagnostic et traitement de l'EI complexes nécessitant plusieurs spécialistes\n"
                "- L'intégration d'une **équipe endocardite** améliore le pronostic\n"
                "- Composition minimale :\n"
                "  - Cardiologues\n"
                "  - Chirurgiens cardiaques\n"
                "  - Infectiologues\n"
                "  - Microbiologistes\n"
                "- Au sein d'un centre de prise en charge des valvulopathies\n"
                "- Possibilité d'ajouter des experts en imagerie cardiovasculaire"
            )),
            FicheRow(concept="Indications de consultation", detail_md=(
                "- L'équipe doit être systématiquement consultée :\n"
                "  - Soit en lui adressant les patients les plus complexes et graves\n"
                "  - Soit en l'impliquant à distance dans la prise en charge"
            )),
        ]),
    ])

    # ── PARTIE III : DIAGNOSTIC CLINIQUE ET PARACLINIQUE ──
    partie_iii = Partie(numero="III", titre="Diagnostic clinique et paraclinique", sous_parties=[
        SousPartie(lettre="A", titre="Signes cliniques", rows=[
            FicheRow(concept="◆ Tableaux cliniques évocateurs", detail_md=(
                "- L'EI est une maladie systémique à présentation polymorphe\n"
                "- L'association d'un syndrome infectieux + signes d'atteinte endocardique est très évocatrice\n"
                "- **5 tableaux cliniques évoquant l'EI** :\n"
                "  - Cardiopathie à risque d'EI + fièvre\n"
                "  - Souffle cardiaque + fièvre\n"
                "  - Accident ischémique + fièvre\n"
                "  - Purpura + fièvre\n"
                "  - Lombalgie + fièvre"
            )),
            FicheRow(concept="Syndrome infectieux", detail_md=(
                "- Fièvre\n"
                "- Altération de l'état général\n"
                "- Splénomégalie (**20-30 %** des cas)"
            )),
            FicheRow(concept="★ ◆ Signes cardiaques", detail_md=(
                "- **Souffle cardiaque** :\n"
                "  - Devant un syndrome infectieux inexpliqué, valeur diagnostique considérable\n"
                "  - La plus grande valeur : apparition d'un nouveau souffle ou modification d'un souffle connu\n"
                "  - L'absence de souffle n'élimine pas le diagnostic\n"
                "- **Insuffisance cardiaque** : toute IC fébrile doit faire évoquer l'EI\n"
                "- Syncopes, lipothymies : secondaires à un **BAV** lié à un abcès septal interrompant les voies de conduction"
            )),
            FicheRow(concept="Signes extracardiaques", detail_md=(
                "- Neurologiques : AVC (ischémique ou hémorragique), méningite, hémorragie méningée, abcès cérébral\n"
                "- Pulmonaires : signes d'IC gauche (**OAP**) ou d'embolie pulmonaire septique (pneumopathies récidivantes abcédées)\n"
                "- Articulaires : arthrite périphérique ou **spondylodiscite** (foyer infectieux à distance)\n"
                "- Cutanéomuqueux (rares, **5-15 %**) :\n"
                "  - Purpura\n"
                "  - **Nodosités d'Osler** (« faux panaris ») — pathognomoniques\n"
                "  - Hémorragies sous-unguéales et sous-conjonctivales\n"
                "  - **Placards de Janeway** (érythémateux palmoplantaires)\n"
                "- Ophtalmiques : **taches de Roth** au fond d'œil (exsudats hémorragiques rétiniens)\n"
                "- Rénaux : hématurie (et/ou protéinurie) ⇒ glomérulonéphrite immunologique ou infarctus rénal"
            )),
            FicheRow(concept="", detail_md=(
                "- **Ne pas évoquer l'EI** devant l'association d'une fièvre et d'un souffle cardiaque "
                "ou d'une cardiopathie à risque = notion **inacceptable**\n"
                "- De même devant : souffle + fièvre, AVC + fièvre, lombalgie + fièvre, purpura + fièvre"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Identification microbiologique", rows=[
            FicheRow(concept="★ ◆ Hémocultures (pilier diagnostique)", detail_md=(
                "- Isolent le micro-organisme responsable dans **90 % des cas**\n"
                "- **10 % d'EI à hémocultures négatives**\n"
                "- Modalités :\n"
                "  - **3 prélèvements** sanguins veineux en moyenne\n"
                "  - À au moins **30 minutes d'intervalle**\n"
                "  - **AVANT toute antibiothérapie**\n"
                "  - Mise en culture aéroanaérobie\n"
                "  - **NE PAS** prélever sur un cathéter en place\n"
                "- À répéter durant **2-3 jours** si négatives initialement\n"
                "  - Surtout si antibiothérapie préalable\n"
                "- Signaler la suspicion d'EI au labo : germes à croissance lente possibles (HACEK, *Brucella*, streptocoques déficients, levures)"
            )),
            FicheRow(concept="★ ◆ Causes d'EI à hémocultures négatives", detail_md=(
                "- **Antibiothérapie préalable** aux hémocultures\n"
                "- Micro-organismes à croissance lente ou difficile :\n"
                "  - Streptocoques déficients\n"
                "  - Groupe **HACEK**\n"
                "  - *Brucella*\n"
                "  - Champignons (agents fongiques)\n"
                "- Micro-organismes intracellulaires :\n"
                "  - ***Coxiella burnetii*** (agent de la **fièvre Q**)\n"
                "  - *Chlamydia*\n"
                "  - *Bartonella*\n"
                "  - ***Tropheryma whipplei*** (maladie de **Whipple**)\n"
                "  - *Mycoplasma*\n"
                "  - *Legionella*\n"
                "- Endocardites non infectieuses (lupus, SAPL, cancer/marastiques)"
            )),
            FicheRow(concept="Méthodes complémentaires si hémocultures négatives", detail_md=(
                "- Techniques spéciales d'hémocultures\n"
                "- Sérologies\n"
                "- **Amplification génique (PCR)**"
            )),
            FicheRow(concept="Analyse de la pièce chirurgicale", detail_md=(
                "- Si patient opéré : analyse des fragments de valves, végétations, abcès, matériel intracardiaque\n"
                "- **3 analyses** :\n"
                "  - Histologique (anatomopathologie)\n"
                "  - Mise en culture\n"
                "  - Amplification génique (PCR)"
            )),
            FicheRow(concept="", detail_md=(
                "- **Débuter les antibiotiques AVANT les hémocultures** en cas de suspicion d'EI = "
                "notion **inacceptable** (sauf sepsis grave ou indication chirurgicale urgente)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Imagerie cardiaque", rows=[
            FicheRow(concept="★ ◆ Échographie cardiaque (pilier diagnostique)", detail_md=(
                "- **ETT** (transthoracique) : systématique en **1re intention** dans tous les cas\n"
                "- **ETO** (transœsophagienne) : meilleure sensibilité que l'ETT, systématique si :\n"
                "  - ETT positive\n"
                "  - ETT négative avec forte suspicion\n"
                "  - En cas de matériel intracardiaque (prothèses, stimulateurs, défibrillateurs)\n"
                "- Permet la mise en évidence des lésions d'EI :\n"
                "  - Végétations\n"
                "  - Destructions valvulaires (mutilations, perforations, ruptures de cordages)\n"
                "  - Abcès, fistules, pseudo-anévrismes\n"
                "  - Désinsertions de prothèses, fuites paraprothétiques\n"
                "- Évaluation de la sévérité des régurgitations et de leur retentissement\n"
                "- **Une échographie normale n'élimine PAS le diagnostic** : à répéter après **7-10 jours**"
            )),
            FicheRow(concept="Scanner cardiaque injecté", detail_md=(
                "- Peut mettre en évidence abcès ou végétations non vus à l'échographie\n"
                "- Particulièrement utile en cas de **prothèses valvulaires**"
            )),
            FicheRow(concept="◆ TEP-scan au 18F-FDG et scintigraphie aux leucocytes marqués", detail_md=(
                "- Mettent en évidence une **hyperfixation** du traceur en cas d'infection\n"
                "- Indications actuelles :\n"
                "  - Suspicion d'EI sur **prothèses valvulaires**\n"
                "  - Suspicion d'EI sur stimulateurs/défibrillateurs implantables\n"
                "  - Quand le diagnostic reste douteux\n"
                "- Si réalisés sur l'ensemble du corps : objectivent des localisations septiques secondaires\n"
                "- Le 18FDG s'accumule dans les zones d'hypermétabolisme (inflammation, cancers)"
            )),
        ]),
        SousPartie(lettre="D", titre="Autres examens complémentaires", rows=[
            FicheRow(concept="Examens biologiques", detail_md=(
                "- NFS, plaquettes : hyperleucocytose à PNN, anémie inflammatoire ou hémolytique, thrombopénie\n"
                "- **CRP** : élévation en faveur d'un syndrome inflammatoire\n"
                "- Facteur rhumatoïde : témoin d'une réaction immunologique\n"
                "- Ionogramme, créatininémie, hématurie, protéinurie : complications rénales\n"
                "- Troponine : si suspicion d'embolie coronarienne"
            )),
            FicheRow(concept="Examens cardiaques et d'imagerie", detail_md=(
                "- **ECG** : anomalies de la conduction (**BAV**), ischémie myocardique (embolies coronariennes)\n"
                "- Radiographie thoracique : signes d'OAP (EI gauche) ou de pneumopathies (EI droite)\n"
                "- Scanner cérébral et thoraco-abdomino-pelvien :\n"
                "  - Recherche de localisations septiques secondaires (encéphale, rate, rein, foie, vertèbres)\n"
                "  - Recherche d'anévrismes infectieux (mycotiques)\n"
                "  - Avec injection si fonction rénale le permet\n"
                "- **IRM cérébrale** : meilleure sensibilité que le scanner mais moins disponible\n"
                "- Angiographie cérébrale : si suspicion d'anévrisme mycotique\n"
                "- Coronarographie : si suspicion d'embolie coronarienne"
            )),
            FicheRow(concept="◆ Recherche de la porte d'entrée", detail_md=(
                "- La porte d'entrée n'est identifiée que dans **50 % des cas**\n"
                "- Dépend du micro-organisme identifié :\n"
                "  - Buccodentaire : panoramique dentaire + consultation stomatologique\n"
                "  - Digestive : **coloscopie** à la recherche d'une tumeur colique si EI à *Streptococcus gallolyticus* (ex-*S. bovis*) ou à entérocoques\n"
                "  - Urinaire : ECBU, échographie ou scanner des voies urinaires"
            )),
        ]),
    ])

    # ── PARTIE IV : FORMES CLINIQUES ET CRITÈRES DIAGNOSTIQUES ──
    partie_iv = Partie(numero="IV", titre="Formes cliniques et critères diagnostiques", sous_parties=[
        SousPartie(lettre="A", titre="EI du cœur droit", rows=[
            FicheRow(concept="◆ Populations concernées", detail_md=(
                "- **Toxicomanes intraveineux** (++)\n"
                "- Porteurs de stimulateurs ou défibrillateurs cardiaques\n"
                "- Porteurs de voies veineuses centrales\n"
                "- Cardiopathies congénitales avec atteinte droite"
            )),
            FicheRow(concept="Présentation clinique", detail_md=(
                "- Signes respiratoires au premier plan\n"
                "- **Pneumopathies infectieuses récidivantes et abcédées**\n"
                "- Secondaires aux embolies pulmonaires septiques provenant des végétations du cœur droit"
            )),
            FicheRow(concept="Germes responsables", detail_md=(
                "- **Staphylocoques** = les plus fréquents chez :\n"
                "  - Le toxicomane IV\n"
                "  - Le porteur de stimulateur/défibrillateur cardiaque"
            )),
            FicheRow(concept="◆ Particularité thérapeutique", detail_md=(
                "- Les EI du cœur droit nécessitent le **retrait du matériel** le cas échéant\n"
                "- En plus des antibiotiques\n"
                "- En cas d'EI sur stimulateur, défibrillateur ou cathéter central : "
                "**tout le matériel doit être extrait** (souvent par voie percutanée) "
                "et réimplanté à distance"
            )),
        ]),
        SousPartie(lettre="B", titre="EI sur prothèses valvulaires", rows=[
            FicheRow(concept="◆ EI précoces vs tardives", detail_md=(
                "| Type | Délai | Origine |\n"
                "|------|-------|---------|\n"
                "| **EI précoces** | Dans l'année qui suit l'implantation | Souvent contamination périopératoire |\n"
                "| **EI tardives** | > 1 an après l'implantation | Bactériémie classique |"
            )),
            FicheRow(concept="Particularités", detail_md=(
                "- Risque d'EI identique sur prothèses biologiques et mécaniques\n"
                "- **Pronostic plus sévère** que les EI sur valves natives"
            )),
            FicheRow(concept="", detail_md=(
                "- Les EI sur **prothèses** et les EI à **staphylocoques** sont les plus graves"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Critères diagnostiques ESC 2023", rows=[
            FicheRow(concept="◆ Classification du diagnostic", detail_md=(
                "- Compte tenu du caractère polymorphe de la maladie, critères diagnostiques établis\n"
                "- 3 catégories : « **certain** », « **possible** », « **exclu** »\n"
                "- Adaptés des recommandations européennes **ESC 2023**"
            )),
            FicheRow(concept="EI certaine", detail_md=(
                "- Critères histologiques :\n"
                "  - Mise en évidence d'un micro-organisme sur la culture d'une valve ou d'un fragment d'embole\n"
                "  - OU mise en évidence d'une végétation ou d'un abcès avec infection active à l'examen anatomopathologique (si chirurgie)\n"
                "- Critères cliniques :\n"
                "  - **2 critères majeurs**\n"
                "  - OU **1 majeur + 3 mineurs**\n"
                "  - OU **5 critères mineurs**"
            )),
            FicheRow(concept="EI possible et EI exclue", detail_md=(
                "- **EI possible** :\n"
                "  - **1 majeur + 1 ou 2 mineurs**\n"
                "  - OU **3 critères mineurs**\n"
                "- **EI exclue** : absence de critères d'EI certaine et possible"
            )),
            FicheRow(concept="★ ◆ Critères majeurs (2)", detail_md=(
                "- **1) Hémocultures positives pour l'EI** :\n"
                "  - **≥ 2 hémocultures** à micro-organisme typique d'EI : *S. aureus*, streptocoques oraux, *S. gallolyticus*, *E. faecalis*, HACEK\n"
                "  - OU ≥ 2 hémocultures positives à plus de **12 heures d'intervalle**\n"
                "  - OU 3 ou ≥ 4 hémocultures distinctes (1re et dernière à ≥ 1 heure d'intervalle) à germe typique\n"
                "  - OU ≥ 1 hémoculture positive ou sérologie positive à ***Coxiella burnetii*** (**IgG phase I > 1/800**)\n"
                "- **2) Imagerie positive** pour les lésions d'EI :\n"
                "  - Échocardiographie (ETT ou ETO)\n"
                "  - Scanner cardiaque\n"
                "  - TEP-scanner cardiaque au 18FDG\n"
                "  - Scintigraphie cardiaque aux leucocytes marqués"
            )),
            FicheRow(concept="★ ◆ Critères mineurs (5)", detail_md=(
                "- **1)** Patient à haut risque ou risque intermédiaire d'EI OU toxicomanie IV\n"
                "- **2) Fièvre** : T° **> 38 °C**\n"
                "- **3) Phénomènes vasculaires** (asymptomatiques inclus) :\n"
                "  - Embolies artérielles systémiques ou pulmonaires\n"
                "  - Anévrismes infectieux (mycotiques)\n"
                "  - Hémorragies\n"
                "  - **Placards de Janeway**\n"
                "- **4) Phénomènes immunologiques** :\n"
                "  - Glomérulonéphrite\n"
                "  - **Nodosités d'Osler**\n"
                "  - **Taches de Roth**\n"
                "  - Facteurs rhumatoïdes\n"
                "- **5) Argument microbiologique** n'entrant pas dans la définition d'un critère majeur (hémocultures, sérologies)"
            )),
        ]),
    ])

    # ── PARTIE V : COMPLICATIONS ET PRONOSTIC ──
    partie_v = Partie(numero="V", titre="Complications et pronostic", sous_parties=[
        SousPartie(lettre="A", titre="Mortalité et complications", rows=[
            FicheRow(concept="◆ Mortalité hospitalière", detail_md=(
                "- L'EI est une maladie grave\n"
                "- **Mortalité hospitalière : 15-30 %**\n"
                "- Les principales causes de décès :\n"
                "  - **Insuffisance cardiaque aiguë**\n"
                "  - **Complications neurologiques**"
            )),
            FicheRow(concept="◆ Principales complications", detail_md=(
                "- **Insuffisance cardiaque** (cause principale de décès)\n"
                "- Embolies systémiques\n"
                "- Embolies pulmonaires septiques (EI droite)\n"
                "- Anévrismes infectieux (mycotiques)\n"
                "- Hémorragie (rupture d'anévrisme)\n"
                "- Choc septique\n"
                "- **BAV** (par abcès septal des EI aortiques)\n"
                "- Vascularite\n"
                "- Foyers infectieux à distance : méningite, arthrite, **spondylodiscite**, abcès viscéraux"
            )),
        ]),
        SousPartie(lettre="B", titre="Facteurs de mauvais pronostic", rows=[
            FicheRow(concept="◆ Facteurs de mauvais pronostic", detail_md=(
                "- **Insuffisance cardiaque aiguë**\n"
                "- **Complications neurologiques**\n"
                "- Syndrome infectieux mal maîtrisé\n"
                "- Abcès intracardiaques\n"
                "- **EI sur prothèses**\n"
                "- Végétations volumineuses\n"
                "- Micro-organismes très virulents : ***S. aureus*** et champignons\n"
                "- Terrain fragile (comorbidités) :\n"
                "  - Âge avancé\n"
                "  - Diabète\n"
                "  - Immunodépression\n"
                "  - Insuffisances cardiaque, rénale, respiratoire préexistantes"
            )),
            FicheRow(concept="", detail_md=(
                "- Mortalité hospitalière **15-30 %**\n"
                "- 2 grandes causes de décès : IC aiguë + complications neurologiques\n"
                "- *S. aureus* et champignons = germes les plus défavorables"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE VI : TRAITEMENT MÉDICAL ET CHIRURGICAL ──
    partie_vi = Partie(numero="VI", titre="Traitement médical et chirurgical", sous_parties=[
        SousPartie(lettre="A", titre="Principes de l'antibiothérapie", rows=[
            FicheRow(concept="★ ◆ Principes généraux de l'antibiothérapie", detail_md=(
                "- **Bactéricide**\n"
                "- **Plusieurs molécules synergiques**\n"
                "- **Fortes doses**\n"
                "- **Voie intraveineuse**\n"
                "- **Durée prolongée : 4 à 6 semaines**\n"
                "- Prise en charge par équipes spécialisées (cardiologues, infectiologues, chirurgiens)"
            )),
            FicheRow(concept="◆ Antibiothérapie probabiliste", detail_md=(
                "- Instaurée **après les hémocultures** et avant leur résultat dans 3 situations :\n"
                "  - Forte suspicion\n"
                "  - Sepsis sévère\n"
                "  - Indication chirurgicale urgente\n"
                "- Secondairement adaptée à l'antibiogramme avec l'aide d'un infectiologue"
            )),
            FicheRow(concept="Particularités de la durée", detail_md=(
                "- La durée de traitement est identique même si une intervention chirurgicale est nécessaire\n"
                "- Doses adaptées aux fonctions rénale et hépatique\n"
                "- Adaptées aux concentrations plasmatiques d'aminosides et de vancomycine"
            )),
            FicheRow(concept="◆ Relais oral / ambulatoire (conditions)", detail_md=(
                "- L'antibiothérapie parentérale peut être :\n"
                "  - Poursuivie en ambulatoire\n"
                "  - OU remplacée par voie orale\n"
                "- Conditions cumulatives :\n"
                "  - EI gauche à streptocoques, entérocoques ou staphylocoques\n"
                "  - Antibiothérapie IV appropriée pendant **≥ 10 jours** (ou ≥ 7 jours après chirurgie cardiaque)\n"
                "  - Patient cliniquement stable\n"
                "  - Pas d'abcès ni d'anomalies valvulaires nécessitant une chirurgie sur l'ETO"
            )),
        ]),
        SousPartie(lettre="B", titre="Surveillance du traitement", rows=[
            FicheRow(concept="◆ Critères d'efficacité", detail_md=(
                "- Régression de la fièvre\n"
                "- Régression du syndrome inflammatoire biologique (CRP)\n"
                "- **Stérilisation des hémocultures**\n"
                "- Évolution favorable des lésions à l'échographie\n"
                "- Absence de complications (clinique, imagerie, ECG, biologie)"
            )),
            FicheRow(concept="Surveillance de la tolérance", detail_md=(
                "- Évaluation de la fonction rénale :\n"
                "  - Sous **aminosides** et **vancomycine** (++)\n"
                "  - Mais aussi sous amoxicilline (réactions immunoallergiques, cristalluries)\n"
                "  - Risques : atteintes interstitielles aiguës, nécroses tubulaires aiguës"
            )),
        ]),
        SousPartie(lettre="C", titre="Indications chirurgicales", rows=[
            FicheRow(concept="◆ Chirurgie en phase active (50 % des cas)", detail_md=(
                "- Dans **environ 50 % des cas** : indication chirurgicale en phase active\n"
                "- Présente d'emblée ou apparaissant en cours d'évolution\n"
                "- Dès le diagnostic posé : prévenir le chirurgien cardiaque\n"
                "- Geste : **débridement** des tissus infectés/nécrosés puis :\n"
                "  - Réparation (plastie) valvulaire si possible\n"
                "  - OU remplacement valvulaire (prothèse biologique ou mécanique)"
            )),
            FicheRow(concept="◆ 3 catégories d'indications", detail_md=(
                "- **Hémodynamiques (H)**\n"
                "- **Infectieuses (I)**\n"
                "- **Emboliques (E)**\n"
                "- Délai d'intervention catégorisé en :\n"
                "  - **TU (Très Urgent)** : dans les 24 heures\n"
                "  - **U (Urgent)** : dans les 3 à 5 jours\n"
                "  - **NU (Non Urgent)** : au cours de la même hospitalisation"
            )),
            FicheRow(concept="★ ◆ Indications hémodynamiques (H)", detail_md=(
                "- **(H-TU)** : Insuffisance cardiaque gauche réfractaire ou **choc cardiogénique**\n"
                "- **(H-U)** : Insuffisance cardiaque gauche ou signe échographique de mauvaise tolérance"
            )),
            FicheRow(concept="★ ◆ Indications infectieuses (I)", detail_md=(
                "- **(I-U)** : Infection non contrôlée localement :\n"
                "  - Abcès, fistule, faux anévrisme intracardiaque\n"
                "  - Végétations augmentant de taille\n"
                "  - Désinsertion de prothèse\n"
                "  - **BAV**\n"
                "- **(I-NU)** : EI fongique ou à germes multirésistants\n"
                "- **(I-U)** : EI sur prothèse valvulaire à ***S. aureus*** ou bactéries non HACEK à Gram négatif\n"
                "- **(I-U)** : Hémocultures positives malgré **> 7 jours** d'antibiothérapie (et contrôle des embolies et métastases septiques)"
            )),
            FicheRow(concept="★ ◆ Indications emboliques (E)", detail_md=(
                "- **(E-U)** : Végétations du cœur gauche **≥ 10 mm** persistantes après un ou plusieurs épisodes emboliques malgré antibiothérapie adaptée\n"
                "- **(E-U)** : Végétations du cœur gauche **≥ 10 mm** associées à une autre indication de chirurgie"
            )),
            FicheRow(concept="Chirurgie à distance", detail_md=(
                "- Si la chirurgie n'est pas indiquée en phase active : chirurgie à distance parfois nécessaire\n"
                "- Les indications sont alors celles de toutes les valvulopathies (cf. item 233)"
            )),
            FicheRow(concept="", detail_md=(
                "- **Penser HIE** : indications **H**émodynamiques + **I**nfectieuses + **E**mboliques\n"
                "- 3 niveaux d'urgence : **TU** (24h) / **U** (3-5j) / **NU** (même hospitalisation)\n"
                "- Seuil clé des végétations : **≥ 10 mm** pour les indications emboliques"
            ), kind="mnemo"),
        ]),
    ])

    # ── PARTIE VII : PRÉVENTION ──
    partie_vii = Partie(numero="VII", titre="Prévention", sous_parties=[
        SousPartie(lettre="A", titre="Mesures non spécifiques d'éducation", rows=[
            FicheRow(concept="★ ◆ Mesures d'éducation (tous les patients à risque)", detail_md=(
                "- Concernent **TOUTES** les cardiopathies à risque d'EI\n"
                "- **Hygiène buccodentaire** :\n"
                "  - Consultation dentiste **2 fois/an** si haut risque\n"
                "  - Consultation dentiste **1 fois/an** pour les autres\n"
                "- Désinfecter les plaies\n"
                "- Éradiquer les colonisations bactériennes chroniques (cutanées et urinaires)\n"
                "- Traiter les infections bactériennes locales par antibiotiques\n"
                "- Asepsie stricte lors de procédures à risque de bactériémie\n"
                "- Éviter les effractions cutanées : **tatouages, piercing**\n"
                "- Limiter l'utilisation des voies veineuses et les changer régulièrement\n"
                "- Éviter l'automédication par antibiotiques\n"
                "- Consulter rapidement son médecin en cas de fièvre"
            )),
            FicheRow(concept="", detail_md=(
                "- Oublier les mesures de prévention non médicamenteuses chez les patients à risque = "
                "notion **inacceptable**"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Antibioprophylaxie", rows=[
            FicheRow(concept="★ ◆ Principe et indications", detail_md=(
                "- Administration d'une dose d'antibiotique avant une procédure à risque de bactériémie\n"
                "- **Efficacité jamais prouvée formellement**\n"
                "- Utilisation limitée aux :\n"
                "  - **Patients à haut risque** (cf. groupes à risque)\n"
                "  - Devant recevoir des soins dentaires avec :\n"
                "    - Manipulation de la gencive\n"
                "    - Manipulation de la région périapicale\n"
                "    - OU effraction de la muqueuse"
            )),
            FicheRow(concept="★ ◆ Protocole chez l'adulte", detail_md=(
                "- **30-60 minutes avant la procédure** :\n"
                "  - **Amoxicilline** (ou ampicilline) **2 g PO ou IV**\n"
                "  - OU céfazoline (ou ceftriaxone) **1 g IM ou IV**\n"
                "- En cas d'**allergie à la pénicilline** :\n"
                "  - Céfalexine 2 g PO\n"
                "  - OU azithromycine 500 mg PO\n"
                "  - OU doxycycline 100 mg PO\n"
                "  - OU céfazoline ou ceftriaxone 1 g IM ou IV"
            )),
            FicheRow(concept="", detail_md=(
                "- Prescrire de la **pénicilline en cas d'allergie** = notion **inacceptable**\n"
                "- L'antibioprophylaxie n'est PAS systématique : uniquement chez les patients à haut risque "
                "ET avant soins dentaires invasifs"
            ), kind="piege"),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Groupes à risque d'endocardite infectieuse", markdown=(
            "| Haut risque | Risque intermédiaire |\n"
            "|-------------|----------------------|\n"
            "| Antécédent d'endocardite | Valvulopathies dégénératives |\n"
            "| Prothèses valvulaires (TAVI inclus) et matériels de réparation | Valvulopathies congénitales (bicuspidie) |\n"
            "| Cardiopathie congénitale cyanogène | Cardiopathie post-rhumatismale |\n"
            "| Cardiopathie congénitale réparée avec prothèse (6 mois ou à vie si shunt résiduel) | Cardiomyopathie hypertrophique |\n"
            "| Dispositif d'assistance ventriculaire | Stimulateur/défibrillateur cardiaque |"
        )),
        TableauSynthese(titre="Fréquence des micro-organismes responsables d'EI", markdown=(
            "| Micro-organisme | Fréquence | Porte d'entrée |\n"
            "|-----------------|-----------|----------------|\n"
            "| *Staphylococcus aureus* | 30 % | Cutanée (plaies, KT, toxicomanie IV, peropératoire, stimulateur) |\n"
            "| Streptocoques oraux (*S. sanguis, mitis, salivarius, mutans*) | 20 % | Buccodentaire |\n"
            "| Streptocoques du groupe D (*S. gallolyticus*/bovis) | 13 % | Digestive (cancer, polypes, diverticules coliques) |\n"
            "| Staphylocoques coagulase négative (*S. epidermidis, lugdunensis*) | 10 % | Cutanée |\n"
            "| Entérocoques (*E. faecalis, faecium*) | 10 % | Digestive ou urinaire |\n"
            "| Bactéries du groupe HACEK | 5 % | Buccodentaire |\n"
            "| *Candida* et autres champignons | < 5 % | Cutanée (immunosuppression, KT, toxicomanie IV) |\n"
            "| Autres (*Coxiella, Bartonella, Brucella, Chlamydia, Tropheryma*) | < 5 % | Spécifique à chaque germe |\n"
            "| Non retrouvé par les techniques | 5-10 % | — |"
        )),
        TableauSynthese(titre="Portes d'entrée selon le germe identifié", markdown=(
            "| Germe | Porte d'entrée | Bilan à réaliser |\n"
            "|-------|----------------|------------------|\n"
            "| Staphylocoques, Candida | Cutanée | Examen clinique cutané |\n"
            "| Streptocoques oraux, HACEK | Buccodentaire | Panoramique dentaire + stomatologue |\n"
            "| Streptocoque D (S. gallolyticus) | Digestive | Coloscopie (tumeur colique ?) |\n"
            "| Entérocoques | Digestive ou urinaire | Coloscopie + ECBU + imagerie urinaire |"
        )),
        TableauSynthese(titre="Antibiothérapie ciblée selon le germe (durée, allergie pénicilline)", markdown=(
            "| Micro-organisme en cause | Absence d'allergie | Allergie pénicilline |\n"
            "|--------------------------|--------------------|----------------------|\n"
            "| Probabiliste EI communautaire native ou prothèse ≥ 1 an | Ampicilline + ceftriaxone (ou oxacilline) + gentamicine | Céfazoline ou vancomycine + gentamicine |\n"
            "| Probabiliste EI non communautaire ou prothèse < 1 an | Vancomycine (ou daptomycine) + gentamicine + rifampicine | Idem |\n"
            "| Staph méti-S sur valve native | Cloxacilline (ou céfazoline) 4-6 sem | Céfazoline 4-6 sem |\n"
            "| Staph méti-S sur prothèse | Cloxacilline (ou céfazoline) + rifampicine 6 sem + gentamicine 2 sem | Céfazoline + rifampicine 6 sem + gentamicine 2 sem |\n"
            "| Staph méti-R sur valve native | Vancomycine 4-6 sem | Idem |\n"
            "| Staph méti-R sur prothèse | Vancomycine + rifampicine 6 sem + gentamicine 2 sem | Idem |\n"
            "| Streptocoques oraux et *S. gallolyticus* sur valve native | Pénicilline G (ou amoxicilline ou ceftriaxone) 4 sem (+ gentamicine 2 sem si résistance) | Vancomycine 4 sem |\n"
            "| Entérocoques sur valve native | Amoxicilline (ou ampicilline) + ceftriaxone 6 sem | Vancomycine 6 sem + gentamicine 2 sem |\n"
            "| Entérocoques sur prothèse | Amoxicilline + ceftriaxone 6 sem | Vancomycine 6 sem + gentamicine 2 sem |\n"
            "| Entérocoques résistants gentamicine | Amoxicilline + ceftriaxone 6 sem | Vancomycine 6 sem |\n"
            "| Entérocoques résistants β-lactamines | Vancomycine 6 sem + gentamicine 2 sem | Idem |\n"
            "| Entérocoques résistants vancomycine | Daptomycine + ampicilline (ou fosfomycine) 6 sem | Daptomycine + fosfomycine |"
        )),
        TableauSynthese(titre="Critères diagnostiques ESC 2023 (résumé)", markdown=(
            "| Catégorie | Critères |\n"
            "|-----------|----------|\n"
            "| EI certaine (histologique) | Micro-organisme sur culture de valve/embole ou végétation/abcès avec infection active |\n"
            "| EI certaine (clinique) | 2 majeurs OU 1 majeur + 3 mineurs OU 5 mineurs |\n"
            "| EI possible | 1 majeur + 1 ou 2 mineurs OU 3 mineurs |\n"
            "| EI exclue | Absence de critères d'EI certaine et possible |"
        )),
        TableauSynthese(titre="Indications chirurgicales en phase active (HIE)", markdown=(
            "| Indication | Catégorie | Délai |\n"
            "|------------|-----------|-------|\n"
            "| IC gauche réfractaire ou choc cardiogénique | (H) | TU (24h) |\n"
            "| IC gauche ou mauvaise tolérance échographique | (H) | U (3-5j) |\n"
            "| Infection non contrôlée localement (abcès, fistule, faux anévrisme, BAV, désinsertion) | (I) | U (3-5j) |\n"
            "| EI fongique ou germes multirésistants | (I) | NU |\n"
            "| EI sur prothèse à S. aureus ou BGN non HACEK | (I) | U (3-5j) |\n"
            "| Hémocultures positives > 7 jours d'ATB | (I) | U (3-5j) |\n"
            "| Végétations gauches ≥ 10 mm + embolies persistantes | (E) | U (3-5j) |\n"
            "| Végétations gauches ≥ 10 mm + autre indication | (E) | U (3-5j) |"
        )),
        TableauSynthese(titre="Antibioprophylaxie chez l'adulte à haut risque (soins dentaires invasifs)", markdown=(
            "| Situation | Antibiotique | Posologie |\n"
            "|-----------|--------------|-----------|\n"
            "| Pas d'allergie | Amoxicilline (ou ampicilline) | 2 g PO ou IV |\n"
            "| Pas d'allergie | Céfazoline ou ceftriaxone | 1 g IM ou IV |\n"
            "| Allergie pénicilline | Céfalexine | 2 g PO |\n"
            "| Allergie pénicilline | Azithromycine | 500 mg PO |\n"
            "| Allergie pénicilline | Doxycycline | 100 mg PO |\n"
            "| Délai d'administration | — | 30-60 min avant la procédure |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Mortalité hospitalière de l'EI | **15-30 %** | Maladie grave |\n"
        "| Hémocultures positives | **90 %** des cas | 10 % d'EI à hémocultures négatives |\n"
        "| Délai entre hémocultures | **≥ 30 minutes** | Avant antibiothérapie |\n"
        "| Nombre d'hémocultures initiales | **3 prélèvements** | Veineux périphériques |\n"
        "| Délai pour répéter l'échographie | **7-10 jours** | Si normale mais suspicion |\n"
        "| Durée d'antibiothérapie IV | **4 à 6 semaines** | Bactéricide, synergique, fortes doses |\n"
        "| Durée IV avant relais PO possible | **≥ 10 jours** | Ou ≥ 7 jours post-chirurgie |\n"
        "| Indication chirurgicale en phase active | **~ 50 %** des cas | HIE |\n"
        "| Délai très urgent (TU) | **24 heures** | IC réfractaire, choc cardiogénique |\n"
        "| Délai urgent (U) | **3 à 5 jours** | Infection non contrôlée, embolies |\n"
        "| Seuil chirurgical des végétations | **≥ 10 mm** | Cœur gauche, indication embolique |\n"
        "| Hémocultures positives > | **7 jours** d'ATB | Indication chirurgicale |\n"
        "| Splénomégalie | **20-30 %** | Signe clinique |\n"
        "| Signes cutanéomuqueux | **5-15 %** | Purpura, Osler, Janeway |\n"
        "| Porte d'entrée identifiée | **50 %** des cas | Selon le germe |\n"
        "| Cardiopathie à risque inconnue/absente | **50 %** des cas | Avant le diagnostic d'EI |\n"
        "| Sérologie Coxiella burnetii (fièvre Q) | **IgG phase I > 1/800** | Critère majeur diagnostique |\n"
        "| Fièvre (critère mineur) | **T° > 38 °C** | ESC 2023 |\n"
        "| Cardiopathie congénitale réparée avec prothèse | **6 mois** (ou à vie si shunt) | Définition haut risque |\n"
        "| Amoxicilline (antibioprophylaxie adulte) | **2 g PO ou IV** | 30-60 min avant procédure |\n"
        "| Céfazoline/ceftriaxone (antibioprophylaxie) | **1 g IM ou IV** | 30-60 min avant procédure |\n"
        "| Consultation dentaire (haut risque) | **2 fois/an** | Mesure de prévention |\n"
        "| Consultation dentaire (autres) | **1 fois/an** | Mesure de prévention |"
    ))

    points_cles = [
        "EI = infection de l'endocarde : valves natives ou **matériel implanté** (prothèses, sondes, KT).",
        "***S. aureus*** = germe n°1 (30 %) ; EI sur **prothèses** et à staphylocoques = formes les plus graves.",
        "Dans **50 %** des cas, la cardiopathie à risque n'était pas connue avant le diagnostic.",
        "Évoquer EI devant : fièvre + cardiopathie à risque / souffle / AVC / purpura / lombalgie.",
        "2 piliers Dx : **hémocultures** (3 prélèvements ≥ 30 min, avant ATB, 90 % positives) + **échographie** (ETT puis ETO).",
        "Échographie normale n'élimine **pas** le diagnostic : à répéter à **7-10 jours**.",
        "Critères **ESC 2023** : EI certaine = 2 majeurs / 1 majeur + 3 mineurs / 5 mineurs.",
        "ATB : **IV, bactéricide, synergique, fortes doses, 4-6 semaines**, débutée après les hémocultures.",
        "Chirurgie **HIE** (50 %) : Hémodynamique / Infectieuse / Embolique (végétations ≥ 10 mm). TU 24 h / U 3-5 j / NU.",
        "Mortalité **15-30 %** ; décès = **IC aiguë** + complications neurologiques. Antibioprophylaxie : haut risque seulement.",
    ]

    fiche_eclair_md = (
        "**Définition** : infection de l'endocarde (valves natives ou matériel implanté). *S. aureus* = germe n°1 (30 %).\n\n"
        "**Évocation** : fièvre + cardiopathie à risque / souffle / AVC / purpura / lombalgie.\n\n"
        "**Lésions** : végétations, destructions valvulaires, abcès. Abcès septal aortique = BAV.\n\n"
        "**Signes extracardiaques** : Osler, Janeway, Roth, AVC, OAP, spondylodiscite, hématurie.\n\n"
        "**Piliers Dx** : hémocultures (3 prélèvements ≥ 30 min, avant ATB, 90 % positives) + ETT puis ETO. Normale : répéter à 7-10 j.\n\n"
        "**ESC 2023** : EI certaine = 2 majeurs / 1 majeur + 3 mineurs / 5 mineurs.\n\n"
        "**Hémocultures négatives** (10 %) : ATB préalable, HACEK, *Brucella*, *Coxiella* (IgG I > 1/800), *Bartonella*, Whipple.\n\n"
        "**Haut risque** : ATCD EI, prothèses/TAVI, congénitale cyanogène, assistance ventriculaire.\n\n"
        "**ATB** : IV, bactéricide, synergique, fortes doses, **4-6 semaines**. Relais PO si EI gauche stable ≥ 10 j IV.\n\n"
        "**Chirurgie HIE** (50 %) : H (IC, choc = TU 24 h), I (abcès, BAV, fongique, *S. aureus* prothèse = U 3-5 j), E (végétations ≥ 10 mm = U).\n\n"
        "**EI cœur droit** : toxicomane IV. Staphylocoques. Pneumopathies abcédées. Extraction du matériel.\n\n"
        "**Prévention** : antibioprophylaxie limitée au haut risque avant soins dentaires (amoxicilline 2 g 30-60 min avant).\n\n"
        "**Pronostic** : mortalité **15-30 %**. Décès = IC aiguë + complications neurologiques.\n"
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 152 - Endocardite infectieuse",
        annee="2025-2026",
        item="Item 152",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi, partie_vii],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 152",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-152_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

"""Génère la fiche de l'Item 153 - Surveillance des porteurs de valve et prothèses vasculaires (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Les différents types de prothèses valvulaires", sous_parties=[
            PlanSousPartie(lettre="A", titre="Prothèses mécaniques"),
            PlanSousPartie(lettre="B", titre="Prothèses biologiques (bioprothèses)"),
            PlanSousPartie(lettre="C", titre="Choix du type de prothèse"),
        ]),
        PlanPartie(numero="II", titre="Physiopathologie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Fonctionnement des prothèses valvulaires"),
            PlanSousPartie(lettre="B", titre="Risques spécifiques par type de prothèse"),
        ]),
        PlanPartie(numero="III", titre="Complications des valves cardiaques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Complications thromboemboliques"),
            PlanSousPartie(lettre="B", titre="Complications infectieuses"),
            PlanSousPartie(lettre="C", titre="Complications du traitement anticoagulant"),
            PlanSousPartie(lettre="D", titre="Détérioration structurelle des prothèses"),
            PlanSousPartie(lettre="E", titre="Dysfonction non structurelle de prothèse"),
        ]),
        PlanPartie(numero="IV", titre="Surveillance des porteurs de valve cardiaque", sous_parties=[
            PlanSousPartie(lettre="A", titre="Postopératoire immédiat"),
            PlanSousPartie(lettre="B", titre="Surveillance ultérieure : modalités"),
            PlanSousPartie(lettre="C", titre="Surveillance clinique, radiologique et ECG"),
            PlanSousPartie(lettre="D", titre="Échocardiogramme doppler et surveillance biologique"),
            PlanSousPartie(lettre="E", titre="Situations particulières"),
        ]),
        PlanPartie(numero="V", titre="Points clés et notions indispensables", sous_parties=[
            PlanSousPartie(lettre="A", titre="Points clés"),
            PlanSousPartie(lettre="B", titre="Notions indispensables et inacceptables"),
        ]),
    ]

    # PARTIE I : LES DIFFERENTS TYPES DE PROTHESES VALVULAIRES
    partie_i = Partie(numero="I", titre="Les différents types de prothèses valvulaires", sous_parties=[
        SousPartie(lettre="A", titre="Prothèses mécaniques", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Il existe deux grands types de prothèses valvulaires : **mécaniques** et **biologiques**\n"
                "- Les prothèses, étant par nature des corps étrangers, présentent un risque accru d'**endocardite infectieuse** par rapport aux valves natives\n"
                "- Les prothèses biologiques se divisent en :\n"
                "  - chirurgicales : implantées lors de la chirurgie\n"
                "  - percutanées : implantées par cathétérisme (**TAVI/TAVR**)"
            )),
            FicheRow(concept="◆ Composition des prothèses mécaniques", detail_md=(
                "- Dispositifs artificiels construits actuellement en **titane et carbone** pour la partie mécanique\n"
                "- Collerette en dacron pour la suture sur les tissus\n"
                "- Trois générations de prothèses mécaniques :\n"
                "  - à bille : prothèse de Starr (retirée du marché en 2007)\n"
                "  - monodisque : Björk-Shiley, Medtronic-Hall\n"
                "  - **à double ailette** : Saint-Jude, Sorin Bicarbon, Mira → les plus implantées (bonne hémodynamique, moins thrombogènes)"
            )),
            FicheRow(concept="◆ Anticoagulation des prothèses mécaniques", detail_md=(
                "- Risque de thrombose : nécessitent un traitement anticoagulant définitif par **antivitamine K (AVK)**\n"
                "- Les AVK diminuent mais ne suppriment pas totalement le risque thrombotique\n"
                "- Les **AOD** (anticoagulants oraux directs, antithrombine ou antifacteur X) sont **formellement contre-indiqués** en cas de prothèse mécanique, même de façon transitoire\n"
                "- Relais possible par **héparine non fractionnée** ou **HBPM** si besoin"
            )),
            FicheRow(concept="Durabilité", detail_md=(
                "- Excellente durabilité : prévues pour durer toute la vie du patient\n"
                "- Certains patients opérés il y a plusieurs décennies sont encore porteurs de prothèses d'ancienne génération"
            )),
            FicheRow(concept="", detail_md=(
                "- Les **AOD sont strictement contre-indiqués** en cas de prothèse valvulaire mécanique, même de façon transitoire\n"
                "- Le risque thrombotique persiste malgré l'anticoagulation : nécessité d'un équilibre rigoureux de l'**INR** à vie"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Prothèses biologiques (bioprothèses)", rows=[
            FicheRow(concept="◆ Bioprothèses chirurgicales", detail_md=(
                "- Le plus souvent des **xénogreffes** (origine animale) : Hancock, Carpentier-Edwards, Perimount, Mosaic, Magna Ease, Inspiris Resilia, Avalus\n"
                "- Constituées soit de :\n"
                "  - péricarde (bovin ou équin)\n"
                "  - valves aortiques porcines\n"
                "- Plus rarement : allogreffes/homogreffes (valve aortique de donneur humain) ou autogreffes\n"
                "- Autogreffes :\n"
                "  - **intervention de Ross** : remplacement du culot aortique par le culot pulmonaire du patient, puis implantation d'une homo/xénogreffe en position pulmonaire\n"
                "  - **intervention d'Ozaki** : péricarde postérieur du patient pour créer une bioprothèse aortique à 3 cusps"
            )),
            FicheRow(concept="Armature des bioprothèses", detail_md=(
                "- Le plus souvent montées sur armature métallique (donc relativement encombrantes)\n"
                "- Plus rarement sans armature (**stentless**) :\n"
                "  - meilleure hémodynamique par diminution de l'encombrement\n"
                "  - durabilité potentiellement plus longue\n"
                "  - réintervention difficile (fusion avec paroi aortique, calcifications)\n"
                "  - rarement implantées de nos jours"
            )),
            FicheRow(concept="◆ Anticoagulation des bioprothèses chirurgicales", detail_md=(
                "- Pas d'anticoagulation pour les bioprothèses aortiques\n"
                "- Anticoagulation **jusqu'au 3e mois postopératoire** pour les bioprothèses mitrales si rythme sinusal"
            )),
            FicheRow(concept="◆ Durabilité des bioprothèses", detail_md=(
                "- **Limitée à 10 ans en moyenne**\n"
                "- Dégénérescence parfois plus précoce :\n"
                "  - chez le sujet jeune\n"
                "  - en fonction du type de prothèse"
            )),
            FicheRow(concept="TAVI valve-in-valve", detail_md=(
                "- Implantation par voie percutanée d'une valve type TAVI dans une bioprothèse chirurgicale ou un TAVI dégénéré\n"
                "- Doit être anticipé lors de tout RVA par bioprothèse\n"
                "- Discussion en **Heart Team** (staff multidisciplinaire)\n"
                "- Prothèses favorables au valve-in-valve à préférer (stentées bien visibles à feuillets internes courts) si espérance de vie > 10 ans\n"
                "- Prothèses chirurgicales spécifiquement conçues pour valve-in-valve : Avalus (Medtronic) et Inspiris Resilia (Edwards)"
            )),
            FicheRow(concept="◆ Bioprothèses percutanées (TAVI/TAVR)", detail_md=(
                "- Bioprothèses d'origine animale utilisées pour le remplacement valvulaire aortique percutané\n"
                "- Indications : rétrécissement aortique serré chez :\n"
                "  - patients contre-indiqués à la chirurgie\n"
                "  - haut risque chirurgical ou intermédiaire\n"
                "  - **dès l'âge de 75 ans** (recommandations ESC 2021)\n"
                "- Montées sur armatures métalliques (inspirées des stents coronariens), fixées sur l'anneau aortique calcifié par cathétérisme rétrograde sous anesthésie locale\n"
                "- Deux modes de déploiement :\n"
                "  - par ballon : Sapien 3\n"
                "  - autodéployées : Evolut R, Evolut Pro (recapturables et repositionnables)"
            )),
            FicheRow(concept="Anticoagulation après TAVI", detail_md=(
                "- Pas d'anticoagulation efficace nécessaire\n"
                "- Simple antiagrégation plaquettaire au long cours : **aspirine faible dose** (recommandations ESC 2021)\n"
                "- Si indication anticoagulation efficace (FA, MTE) : **AVK ou AOD** seuls peuvent être poursuivis au long cours"
            )),
            FicheRow(concept="Avenir et limites du TAVI", detail_md=(
                "- Possibilité de remplacer la valve pulmonaire dans certaines cardiopathies congénitales\n"
                "- Développement de TAVI pour valves tricuspide ou mitrale en cours\n"
                "- Risque de dégénérescence existe comme pour toute bioprothèse\n"
                "- Durabilité reste à définir (peu de suivi au-delà de 5 ans)\n"
                "- TAVI **valve-in-valve** entré dans la pratique courante : évite des chirurgies redux à haut risque"
            )),
        ]),
        SousPartie(lettre="C", titre="Choix du type de prothèse", rows=[
            FicheRow(concept="Risques opposés des deux types", detail_md=(
                "- **Mécaniques** : exposent au risque thromboembolique et hémorragique (du fait des AVK)\n"
                "- **Biologiques** : exposent au risque de dégénérescence et donc de réintervention"
            )),
            FicheRow(concept="Critères de sélection", detail_md=(
                "- Choix éclairé du patient, espérance de vie, mode de vie\n"
                "- Balance risque thromboembolique/hémorragique\n"
                "- Risque de dégénérescence"
            )),
            FicheRow(concept="Tableau de choix par âge", detail_md=(
                "| Type | Position aortique | Position mitrale |\n"
                "|------|-------------------|------------------|\n"
                "| **Mécanique** préférée | **< 60 ans** | **< 65 ans** |\n"
                "| **Biologique** indiquée | **> 65 ans** | **> 70 ans** |"
            )),
            FicheRow(concept="◆ Indications du TAVI", detail_md=(
                "- Patients présentant une contre-indication chirurgicale\n"
                "- Haut risque chirurgical ou risque intermédiaire\n"
                "- Patients âgés **> 75 ans** avec comorbidités ou fragiles\n"
                "- Évaluation par **Heart Team** : cardiologues, chirurgiens cardiaques, anesthésistes-réanimateurs, gériatres\n"
                "- Après 75 ans : consensus pour envisager le TAVI en 1re intention si anatomie favorable (ESC 2021)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La durabilité mitrale est inférieure à la durabilité aortique pour les bioprothèses : seuils d'âge différents pour la décision (60 vs 65 ans pour méca, 65 vs 70 ans pour bio)"
            ), kind="piege"),
        ]),
    ])

    # PARTIE II : PHYSIOPATHOLOGIE
    partie_ii = Partie(numero="II", titre="Physiopathologie", sous_parties=[
        SousPartie(lettre="A", titre="Fonctionnement des prothèses valvulaires", rows=[
            FicheRow(concept="Mécanique d'ouverture/fermeture", detail_md=(
                "- Les prothèses fonctionnent comme des valves natives\n"
                "- Jeu de l'élément mobile :\n"
                "  - bille (autrefois)\n"
                "  - disque basculant ou double ailette (de nos jours)\n"
                "  - cusps pour les valves biologiques\n"
                "- Mouvement sous l'effet des variations de pression dans les cavités cardiaques en amont et en aval\n"
                "- Permet le passage du sang dans le sens de la circulation et empêche le reflux/régurgitation"
            )),
        ]),
        SousPartie(lettre="B", titre="Risques spécifiques par type de prothèse", rows=[
            FicheRow(concept="Valves mécaniques", detail_md=(
                "- Risque de thrombose nécessitant une anticoagulation efficace par **AVK**\n"
                "- Risque persistant au-delà de la 1re année"
            )),
            FicheRow(concept="Valves biologiques", detail_md=(
                "- **Risque de dégénérescence** avec :\n"
                "  - développement de calcifications conduisant à une sténose\n"
                "  - risque de déchirure en particulier commissural\n"
                "- Risque faible de thrombose de feuillets (chirurgicales ou TAVI)\n"
                "- Traitement anticoagulant systématique :\n"
                "  - non justifié pour les bioprothèses chirurgicales\n"
                "  - non indiqué pour le TAVI"
            )),
            FicheRow(concept="", detail_md=(
                "- Toutes les prothèses, mécaniques ou biologiques, présentent un risque accru d'**endocardite infectieuse** par rapport aux valves natives"
            ), kind="a_retenir"),
        ]),
    ])

    # PARTIE III : COMPLICATIONS DES VALVES CARDIAQUES
    partie_iii = Partie(numero="III", titre="Complications des valves cardiaques", sous_parties=[
        SousPartie(lettre="A", titre="Complications thromboemboliques", rows=[
            FicheRow(concept="◆ Généralités", detail_md=(
                "- Complications les plus fréquentes des prothèses valvulaires\n"
                "- Beaucoup plus fréquentes avec les **prothèses mécaniques** qu'avec les biologiques\n"
                "- D'où la nécessité absolue d'un **AVK à vie** parfaitement équilibré pour les valves mécaniques\n"
                "- Prédominent dans la 1re année postopératoire (avant endothélialisation de la collerette)\n"
                "- Risque persiste au-delà"
            )),
            FicheRow(concept="◆ Facteurs de risque thromboembolique", detail_md=(
                "- Prothèses mitrales > prothèses aortiques (faibles pressions sur mitrale)\n"
                "- Prothèses anciennes (à billes) > prothèses à double ailette\n"
                "- **Fibrillation atriale (FA)**\n"
                "- Dysfonction ventriculaire gauche\n"
                "- ◆ Principal facteur : **traitement anticoagulant insuffisant** ++"
            )),
            FicheRow(concept="◆ Embolies systémiques", detail_md=(
                "- Dues à la migration d'un thrombus à partir de la prothèse\n"
                "- Le plus souvent **cérébrales (70 %)** : AIT ou AVC constitué, avec séquelles définitives possibles\n"
                "- Plus rarement : ischémie aiguë de membre, infarctus du myocarde (embolie coronarienne), infarctus rénal ou splénique\n"
                "- L'embole peut être secondaire à une thrombose obstructive ou non obstructive\n"
                "- Les thromboses non obstructives : n'empêchent pas le mouvement de l'élément mobile, surviennent surtout sur prothèses mitrales, thrombus sur la face atriale de la prothèse en ETO"
            )),
            FicheRow(concept="Thrombose obstructive de prothèse mécanique - Clinique", detail_md=(
                "- Mouvements de l'élément mobile diminués\n"
                "- Accidents brutaux possibles :\n"
                "  - œdème aigu pulmonaire\n"
                "  - syncope\n"
                "  - état de choc\n"
                "  - **mort subite** ou très rapide\n"
                "- Diagnostic souvent difficile\n"
                "- Modifications auscultatoires :\n"
                "  - diminution de l'amplitude des bruits de prothèse\n"
                "  - apparition/renforcement d'un souffle systolique (prothèse aortique)\n"
                "  - apparition d'un roulement diastolique (prothèse mitrale)\n"
                "- Souvent anticoagulation insuffisante en cause : **vérifier l'INR en urgence**"
            )),
            FicheRow(concept="◆ Thrombose obstructive - Diagnostic", detail_md=(
                "- **Radiocinéma de prothèse** sous amplificateur de brillance : diminution du jeu des éléments mobiles radio-opaques\n"
                "- ETT et ETO :\n"
                "  - gradients transprothétiques anormalement élevés\n"
                "  - surface valvulaire fonctionnelle réduite\n"
                "  - fuite intraprothétique possible (fermeture incomplète)\n"
                "  - recherche du thrombus en ETT/ETO ou au **scanner injecté synchronisé**"
            )),
            FicheRow(concept="◆ Thrombose obstructive - Prise en charge", detail_md=(
                "- Hospitalisation en **USIC**\n"
                "- **Héparine IV** à la seringue + **aspirine** (bolus IV pour efficacité rapide, puis per os)\n"
                "- **Réintervention d'urgence** pour changement de valve si :\n"
                "  - thrombose aiguë de prothèse (**mortalité 30 %**)\n"
                "  - blocage d'ailette non réversible sous héparine-aspirine\n"
                "- En cas de contre-indication chirurgicale ou forme subaiguë résistante : **thrombolyse** (parfois bons résultats)\n"
                "- ⚠ Diagnostic différentiel avec endocardite infectieuse parfois difficile (une fébricule est possible dans les thromboses de prothèse)"
            )),
            FicheRow(concept="Thrombose de prothèse biologique", detail_md=(
                "- Cas décrits, précoces ou tardifs\n"
                "- Surtout sur prothèses percutanées, plus rarement sur chirurgicales\n"
                "- Diagnostic suspecté en **ETT** :\n"
                "  - élévation brutale des gradients (**> 10 mmHg**) pour atteindre un **gradient moyen > 20 mmHg**\n"
                "  - sans anomalie structurelle évidente des cusps (pas de calcification)\n"
                "- Confirmation en **ETO** : image d'addition hypo ou isoéchogène\n"
                "- Scanner injecté synchronisé : image hypodense\n"
                "- Traitement : anticoagulation efficace par **AVK ou AOD**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Thrombose obstructive de prothèse mécanique = **urgence vitale** : mortalité 30 % à la chirurgie d'urgence\n"
                "- ⚠ Toute fièvre + suspicion de thrombose chez un porteur de prothèse doit faire évoquer l'**endocardite infectieuse** associée"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Complications infectieuses", rows=[
            FicheRow(concept="Médiastinite postopératoire", detail_md=(
                "- Survient dans **~1 % des cas**\n"
                "- Cause de mortalité précoce de la chirurgie cardiaque (en particulier coronarienne)\n"
                "- **Mortalité ~20 %** des patients atteints\n"
                "- Contamination par germes du patient, des soignants ou de l'environnement (sternotomie)\n"
                "- Germes en cause : **staphylocoques dorés ou blancs** le plus souvent"
            )),
            FicheRow(concept="◆ Endocardite infectieuse - Généralités", detail_md=(
                "- Complication redoutable chez les porteurs de prothèse\n"
                "- Risque majoré → **prophylaxie draconienne** à vie\n"
                "- Prévention et traitement indispensable de tout foyer infectieux, en particulier **ORL et dentaire** ++"
            )),
            FicheRow(concept="◆ EI précoce vs EI tardive", detail_md=(
                "| Type | EI postopératoire précoce | EI tardive |\n"
                "|------|---------------------------|------------|\n"
                "| **Délai** | Jusqu'à 1 an après chirurgie | > 1 an |\n"
                "| **Mécanisme** | Contamination peropératoire | Comparable à valve native |\n"
                "| **Germes** | Hospitaliers, souvent multirésistants (staphylocoque doré/blanc) | Comparables à valve native, staphylocoque dans 50 % des cas |\n"
                "| **Complications** | Abcès de l'anneau, désinsertion de prothèse | Variables |\n"
                "| **Réintervention** | Précoce le plus souvent nécessaire | Discutée selon critères |\n"
                "| **Mortalité** | **~50 %** | Meilleur pronostic |"
            )),
            FicheRow(concept="Indications de réintervention dans l'EI tardive", detail_md=(
                "- Sepsis non maîtrisé\n"
                "- Risque embolique important sur volumineuses végétations\n"
                "- Dysfonction sévère de prothèse\n"
                "- Atteinte périvalvulaire avec désinsertion notamment"
            )),
            FicheRow(concept="◆ Diagnostic de l'EI sur prothèse", detail_md=(
                "- **Hémocultures** pour identifier le germe\n"
                "- **ETT et ETO ++** pour confirmer l'atteinte de l'endocarde :\n"
                "  - végétations sur la prothèse\n"
                "  - complications : désinsertion avec fuite paraprothétique, abcès\n"
                "- ETO doit être réalisée :\n"
                "  - en cas de forte suspicion d'EI\n"
                "  - également si le diagnostic est confirmé (bilan précis des lésions)\n"
                "- Imagerie en coupes et **TEP-scanner** : place importante dans l'aide au diagnostic d'EI sur prothèse\n"
                "  - zones de fixation intense focale autour de la prothèse et emboles\n"
                "  - intéressant dès la période postopératoire sur tout type de prothèse"
            )),
            FicheRow(concept="◆ Conduite à tenir devant une fièvre", detail_md=(
                "- Indispensable : **hémocultures systématiques** avant toute antibiothérapie\n"
                "- Échocardiographie selon contexte clinique et résultat des hémocultures\n"
                "- Discussion en staff multidisciplinaire (équipe endocardite) pour toute suspicion d'EI"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Prescrire une antibiothérapie à l'aveugle chez un porteur de prothèse fébrile est une **notion inacceptable** → toujours faire les hémocultures d'abord\n"
                "- ⚠ Ne pas penser à une EI devant toute fièvre chez un porteur de prothèse est une **notion inacceptable**"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Complications du traitement anticoagulant", rows=[
            FicheRow(concept="◆ Risque hémorragique des AVK", detail_md=(
                "- Risque hémorragique estimé à **1,2 % par an** (années-patients) pour les porteurs de valves mécaniques\n"
                "- Tout type d'hémorragie :\n"
                "  - cérébrale\n"
                "  - digestive ou hématurie → rechercher une lésion organique sous-jacente\n"
                "  - ménométrorragies\n"
                "  - hématome favorisé par traumatisme\n"
                "- Gravité variable, certaines pouvant aboutir au décès"
            )),
            FicheRow(concept="◆ Conduite en cas d'hémorragie sévère", detail_md=(
                "- Interruption des AVK\n"
                "- Maintien indispensable de l'anticoagulation par **héparine** :\n"
                "  - **TCA = 1,5 à 2 × témoin** si HNF utilisée\n"
                "- Interruption très temporaire parfois nécessaire si pronostic vital engagé (ex : hémorragie intracrânienne)"
            )),
            FicheRow(concept="", detail_md=(
                "- L'anticoagulation par héparine doit être maintenue même en cas d'hémorragie sévère sur prothèse mécanique : risque thrombotique majeur sinon"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Détérioration structurelle des prothèses", rows=[
            FicheRow(concept="◆ Dégénérescence des bioprothèses - Généralités", detail_md=(
                "- Détérioration tissulaire inexorable avec les années\n"
                "- Définition : altération non infectieuse des feuillets valvulaires avec :\n"
                "  - apparition de calcifications\n"
                "  - déchirure\n"
                "  - responsables de sténose et/ou fuites valvulaires → réintervention\n"
                "- Survient en général au bout de **5 à 15 ans**\n"
                "- Dépend de :\n"
                "  - type de substitut\n"
                "  - site d'implantation : mitral > aortique\n"
                "  - âge du patient : jeune > personne âgée"
            )),
            FicheRow(concept="Mécanismes de dégénérescence", detail_md=(
                "- Physiopathologie mal connue, plusieurs mécanismes :\n"
                "  - dégénérescence passive avec accumulation de cristaux phosphocalciques\n"
                "    - prétraitement anticalcique réduit la survenue des calcifications\n"
                "  - mécanisme proche de l'athérosclérose\n"
                "  - mécanisme immunologique de rejet cellulaire (malgré prétraitement par glutaraldéhyde)\n"
                "  - les complications locales (thrombose, endocardite) traitées médicalement peuvent accélérer le processus"
            )),
            FicheRow(concept="◆ Diagnostic de dégénérescence", detail_md=(
                "- Signes évocateurs :\n"
                "  - apparition/modification d'un souffle\n"
                "  - réapparition de symptômes d'effort\n"
                "  - mise en évidence en ETT de calcifications des cusps, prothèse sténosante ou fuyante\n"
                "  - signes d'insuffisance cardiaque si sténose ou fuite importante\n"
                "- Diagnostic fait par **ETT**\n"
                "- Scanner souvent nécessaire pour distinguer la dégénérescence d'une thrombose"
            )),
            FicheRow(concept="Réintervention", detail_md=(
                "- Indiquée en cas de dégénérescence sévère et symptomatique (pronostic vital engagé)\n"
                "- Souvent à risque :\n"
                "  - patients âgés\n"
                "  - comorbidités\n"
                "  - intervention redux\n"
                "- Le **valve-in-valve** percutané ouvre de nouvelles perspectives thérapeutiques"
            )),
            FicheRow(concept="Détérioration structurelle des prothèses mécaniques", detail_md=(
                "- Fracture d'ailette\n"
                "- Phénomène très rare"
            )),
        ]),
        SousPartie(lettre="E", titre="Dysfonction non structurelle de prothèse", rows=[
            FicheRow(concept="◆ Désinsertions de prothèse - Généralités", detail_md=(
                "- Surviennent dans **~5 % des cas**\n"
                "- Surtout durant les premiers mois postopératoires\n"
                "- À l'origine d'une **fuite paraprothétique**\n"
                "- Étiologies :\n"
                "  - spontanées : lâchage de sutures sur tissus fragilisés (interventions multiples, calcifications annulaires)\n"
                "  - dues le plus souvent à une **EI** → à toujours évoquer et rechercher"
            )),
            FicheRow(concept="◆ Diagnostic de désinsertion", detail_md=(
                "- Apparition d'un souffle :\n"
                "  - diastolique pour prothèse aortique\n"
                "  - systolique pour prothèse mitrale\n"
                "- **ETT** : élévation des gradients transprothétiques + flux de régurgitation en doppler couleur\n"
                "- ◆ **Anémie hémolytique** plus ou moins sévère :\n"
                "  - élévation des **LDH** (lactate-déshydrogénases)\n"
                "  - baisse de l'**haptoglobine**\n"
                "  - **schizocytes** = hématies fragmentées (signent le caractère mécanique de l'hémolyse)\n"
                "- Signes d'insuffisance cardiaque si désinsertion importante\n"
                "- Diagnostic fait par ETT et surtout par **ETO** : fuite paraprothétique"
            )),
            FicheRow(concept="Traitement de la désinsertion", detail_md=(
                "- En cas de désinsertion importante symptomatique : **réintervention**\n"
                "- Chirurgie conventionnelle\n"
                "- Ou voie percutanée avec mise en place d'un plug (bouchon) dans la zone de désinsertion"
            )),
            FicheRow(concept="Pannus fibreux", detail_md=(
                "- Tissu conjonctif cicatriciel excessif se développant sur le versant :\n"
                "  - atrial des prothèses mitrales\n"
                "  - ventriculaire des prothèses aortiques\n"
                "- Peut créer une sténose orificielle extravalvulaire\n"
                "- Pas de traitement préventif\n"
                "- Sanction chirurgicale en cas de symptômes"
            )),
            FicheRow(concept="Mismatch (disproportion patient-prothèse)", detail_md=(
                "- Surface valvulaire effective de la prothèse trop petite par rapport à la surface corporelle\n"
                "- Inadéquation entre surface valvulaire et débit cardiaque adapté aux besoins du patient"
            )),
            FicheRow(concept="", detail_md=(
                "- L'apparition d'une **anémie hémolytique** (élévation LDH, baisse haptoglobine, schizocytes) chez un porteur de prothèse doit faire évoquer une **désinsertion**"
            ), kind="a_retenir"),
        ]),
    ])

    # PARTIE IV : SURVEILLANCE
    partie_iv = Partie(numero="IV", titre="Surveillance des porteurs de valve cardiaque", sous_parties=[
        SousPartie(lettre="A", titre="Postopératoire immédiat", rows=[
            FicheRow(concept="◆ Relais AVK postopératoire", detail_md=(
                "- Relais par **AVK** entrepris précocement, dès les premiers jours postopératoires\n"
                "- Maintenu à vie en cas de prothèse mécanique\n"
                "- Parfois utilisé par certaines équipes pour les bioprothèses aortiques\n"
                "- Recommandé pour bioprothèses mitrales dans les **3 premiers mois** si rythme sinusal"
            )),
            FicheRow(concept="◆ Bioprothèses aortiques en rythme sinusal", detail_md=(
                "- Soit anticoagulation par **AOD**\n"
                "- Soit simple traitement antiagrégant pendant au moins **3 mois**"
            )),
            FicheRow(concept="Bioprothèses en cas de FA", detail_md=(
                "- Pour bioprothèse aortique + FA : **AOD** peut être envisagé dès le postopératoire\n"
                "- Pour bioprothèse mitrale + FA : AOD possible en postopératoire immédiat"
            )),
            FicheRow(concept="Réadaptation cardiaque", detail_md=(
                "- Vers le **8e jour postopératoire** : séjour en centre de réadaptation fonctionnelle cardiorespiratoire\n"
                "- Durée : **3 à 4 semaines** (convalescence et réadaptation)"
            )),
            FicheRow(concept="◆ ETT postopératoire", detail_md=(
                "- ETT postopératoire précoce essentielle pour dépister les complications\n"
                "- **ETT du 2e-4e mois postopératoire** = examen de référence\n"
                "  - réalisée après correction de l'anémie et tachycardie postopératoires (qui augmentent le débit cardiaque)"
            )),
        ]),
        SousPartie(lettre="B", titre="Surveillance ultérieure : modalités", rows=[
            FicheRow(concept="◆ Calendrier de suivi", detail_md=(
                "- Suivi à 1 mois, puis **tous les 3 mois** par le médecin traitant :\n"
                "  - vérification de l'état clinique\n"
                "  - équilibre du traitement anticoagulant\n"
                "- Consultation du cardiologue au **2e-4e mois** postopératoire pour ETT de référence\n"
                "- Ensuite : suivi par le cardiologue **1 à 2 fois/an**"
            )),
            FicheRow(concept="◆ Documents indispensables pour le patient", detail_md=(
                "- **Carte de porteur de prothèse** remise à la sortie de chirurgie cardiaque :\n"
                "  - type de prothèse\n"
                "  - diamètre\n"
                "  - numéro de série\n"
                "- **Carnet de surveillance** du traitement anticoagulant :\n"
                "  - INR cible pour les prothèses mécaniques\n"
                "- **Carte d'antibioprophylaxie** pour le dentiste :\n"
                "  - haut risque d'endocardite +++\n"
                "  - tout geste dentaire à risque infectieux (y compris détartrage) sous antibioprophylaxie\n"
                "  - protocole habituel : **amoxicilline 3 g 1 h avant les soins**\n"
                "  - suivi dentaire au moins biannuel"
            )),
        ]),
        SousPartie(lettre="C", titre="Surveillance clinique, radiologique et ECG", rows=[
            FicheRow(concept="◆ Surveillance clinique", detail_md=(
                "- Vérifier l'absence de réapparition de symptômes cardiaques\n"
                "- Une dyspnée ou récidive d'IC doit faire suspecter une **dysfonction de prothèse** → réhospitalisation\n"
                "- Vérification de l'auscultation à chaque consultation\n"
                "- Absence de fièvre ou foyer infectieux à vérifier\n"
                "- Absence de manifestation ischémique ou hémorragique\n"
                "- Régularité du suivi dentaire à l'interrogatoire"
            )),
            FicheRow(concept="◆ Auscultation des prothèses", detail_md=(
                "- **Bioprothèses** : bruits du cœur identiques aux valves natives\n"
                "  - petit souffle éjectionnel systolique aortique pour bioprothèses aortiques\n"
                "- **Prothèses mécaniques** : auscultation très particulière\n"
                "  - bruits d'ouverture et surtout de fermeture intenses, claqués, métalliques\n"
                "  - prothèses récentes à double ailette : moins bruyantes que celles d'ancienne génération\n"
                "- Modifications pathologiques :\n"
                "  - diminution d'intensité ou caractère variable des bruits d'ouverture/fermeture (hors FA)\n"
                "  - apparition/augmentation d'un souffle systolique\n"
                "  - apparition d'un bruit diastolique surajouté : insuffisance aortique (proth. aortique) ou roulement diastolique (proth. mitrale)"
            )),
            FicheRow(concept="Surveillance radiologique", detail_md=(
                "- Cliché de thorax : apprécie les modifications de volume de la silhouette cardiaque\n"
                "  - plus réalisé en routine hors postopératoire précoce\n"
                "- **Radiocinéma de prothèse** : appréciation du jeu de l'élément mobile mécanique\n"
                "  - utilisé seulement en cas de suspicion de dysfonction\n"
                "- Scanner injecté et TEP-scanner :\n"
                "  - en cas de suspicion de thrombose, pannus ou EI"
            )),
            FicheRow(concept="Surveillance ECG", detail_md=(
                "- Réalisé lors de la consultation cardiologique\n"
                "- Surveille le rythme cardiaque\n"
                "- Peut constater la régression d'une HVG ou HVD\n"
                "- N'apporte pas d'élément spécifique pour la prothèse elle-même\n"
                "- ◆ Permet de dépister un passage en **FA** (non exceptionnel, notamment prothèse mitrale)"
            )),
        ]),
        SousPartie(lettre="D", titre="Échocardiogramme doppler et surveillance biologique", rows=[
            FicheRow(concept="◆ ETT - Fréquence", detail_md=(
                "| Type de prothèse | Fréquence ETT |\n"
                "|------------------|---------------|\n"
                "| **Valves mécaniques** | **tous les 1 à 2 ans** (en l'absence de complication) |\n"
                "| **Bioprothèses conventionnelles** | après contrôle à **3 mois et 1 an**, puis **annuelle** |\n"
                "| **Prothèses percutanées / bioprothèses dernière génération** | attention particulière (durabilité moins connue) |"
            )),
            FicheRow(concept="◆ ETT - Paramètres explorés", detail_md=(
                "- Examen bidimensionnel : apprécie le jeu de l'élément mobile\n"
                "- Examen doppler : mesure des **gradients transprothétiques**\n"
                "  - vitesse maximale antérograde\n"
                "  - gradient moyen\n"
                "  - surface fonctionnelle de la prothèse\n"
                "- Doppler continu et couleur : recherche de fuite prothétique (intra ou paraprothétique)\n"
                "- Comparaison d'un examen à l'autre : le patient est sa propre référence\n"
                "- Gradients les plus faibles : bioprothèses et valves mécaniques à double ailette\n"
                "- Plus la prothèse est petite, plus les gradients augmentent et la surface diminue"
            )),
            FicheRow(concept="ETT vs ETO", detail_md=(
                "- ETT et ETO = examens les plus performants pour la surveillance (ETT) et le diagnostic des dysfonctions (ETO)\n"
                "- **ETO** : réalisée seulement en cas de suspicion de dysfonction\n"
                "- ETO systématique en cas de :\n"
                "  - suspicion de thrombose\n"
                "  - endocardite sur prothèse\n"
                "  - désinsertion\n"
                "- ETO particulièrement utile pour la prothèse mitrale"
            )),
            FicheRow(concept="◆ Surveillance biologique des AVK", detail_md=(
                "- Pour les prothèses mécaniques : équilibre rigoureux de l'AVK à vie, surveillance par **INR**\n"
                "- Surveillance de l'INR :\n"
                "  - initialement **1 à 2 fois/semaine** jusqu'à équilibre\n"
                "  - puis **au moins 1 fois/mois** au long cours\n"
                "  - plus souvent si nécessaire\n"
                "- ◆ **INR cible : 2,5 à 4** pour les prothèses mécaniques\n"
                "- Variation maximale tolérée : **0,5 point** de part et d'autre de l'INR cible"
            )),
            FicheRow(concept="◆ Détermination de l'INR cible", detail_md=(
                "- Discuté avec le cardiologue, établi individuellement selon ESC 2021\n"
                "- Prend en compte :\n"
                "  - type de prothèse et risque thrombotique\n"
                "  - position de la prothèse\n"
                "  - facteurs de risque embolique liés au patient\n"
                "  - facteurs de risque hémorragique"
            )),
            FicheRow(concept="Risque thrombotique de la prothèse", detail_md=(
                "| Niveau | Prothèses concernées |\n"
                "|--------|----------------------|\n"
                "| **Faible** | Mécaniques en position aortique : Medtronic Hall (disque), ATS, Saint Jude, On-X, Sorin Bicarbon, Carbomedics (double ailette) |\n"
                "| **Moyen** | Valves à double ailette récentes ou données insuffisantes |\n"
                "| **Élevé** | Björk-Shiley (monodisque), Starr (à bille) |"
            )),
            FicheRow(concept="Facteurs de risque liés au patient", detail_md=(
                "- Prothèse en position mitrale ou tricuspide\n"
                "- Antécédent thromboembolique\n"
                "- **Fibrillation atriale (FA)**\n"
                "- Sténose mitrale associée\n"
                "- **FE < 35 %**\n"
                "- Hypercoagulabilité (en plus dans les recommandations américaines)"
            )),
            FicheRow(concept="Antiagrégants associés et AOD", detail_md=(
                "- En Europe : adjonction d'antiagrégants plaquettaires non recommandée sauf situations spécifiques :\n"
                "  - stent récent (transitoire)\n"
                "  - thromboembolie sous INR efficace (définitive)\n"
                "- ◆ **AOD contre-indiqués** chez les porteurs de valves mécaniques\n"
                "- En cas de bioprothèse :\n"
                "  - AOD autorisés au-delà du **3e mois postopératoire** si indication non valvulaire\n"
                "  - AOD envisagés en postopératoire immédiat si FA + bioprothèse mitrale\n"
                "- HBPM : pas d'AMM mais reconnues comme alternative acceptable à l'HNF (recommandations européennes)\n"
                "- Porteurs de bioprothèses : pas d'anticoagulation au long cours sauf indication (ex. FA)\n"
                "  - au-delà du 3e mois : tous types d'anticoagulants autorisés pour les bioprothèses"
            )),
            FicheRow(concept="◆ Éducation thérapeutique et automesure", detail_md=(
                "- Éducation thérapeutique cruciale\n"
                "- Recours aux cliniques d'anticoagulants si possible\n"
                "- Systèmes d'**automesure INR** (CoaguChek INRange) par bandelette :\n"
                "  - permet l'autoadaptation\n"
                "  - remboursés depuis **2017** uniquement pour les porteurs de prothèses mécaniques\n"
                "  - mise en place possible chez seulement **50 % des patients**"
            )),
        ]),
        SousPartie(lettre="E", titre="Situations particulières", rows=[
            FicheRow(concept="◆ Hémorragie", detail_md=(
                "- Le traitement anticoagulant ne doit théoriquement jamais être interrompu (risque de thrombose)\n"
                "- Exception : hémorragie mettant en jeu le pronostic vital immédiat\n"
                "- Si neutralisation de l'AVK nécessaire :\n"
                "  - **Plasma frais** de préférence\n"
                "  - À la **vitamine K** (0,5 à 2 mg)"
            )),
            FicheRow(concept="◆ Chirurgie non cardiaque", detail_md=(
                "- Extraction dentaire : souvent en ambulatoire avec **INR de 2 à 2,5**\n"
                "- Chirurgies à faible risque hémorragique (ex : cataracte) : réalisables sous AVK\n"
                "- Chirurgie extracardiaque :\n"
                "  - arrêt des AVK pour obtenir **INR < 1,5**\n"
                "  - héparine : TCA = **2 × témoin** dès que INR < 2 (proth. aortique) ou < 2,5 (proth. mitrale)\n"
                "  - héparine interrompue : TCA normal au moment de l'opération\n"
                "  - reprise dès que possible en postopératoire\n"
                "- HBPM : de plus en plus utilisées et tolérées si dose curative (et non préventive)\n"
                "- Seule l'**HNF** possède une AMM chez les porteurs de prothèse en France"
            )),
            FicheRow(concept="◆ Grossesse", detail_md=(
                "- **Mortalité maternelle** estimée à **1-4 %**\n"
                "- Taux d'événement sérieux : **40 %** chez les femmes enceintes porteuses de valves mécaniques\n"
                "- Complications thromboemboliques plus fréquentes sous héparine que sous AVK chez la femme enceinte\n"
                "- Mais AVK comportent un risque tératogène (**6e-12e semaine d'aménorrhée**), surtout si dose élevée\n"
                "- Recommandations européennes actuelles :\n"
                "  - AVK pendant toute la durée de grossesse jusqu'au 3e trimestre\n"
                "  - si dose de warfarine (Coumadine) **< 5 mg** (ou équivalent)\n"
                "  - décision discutée avec la patiente\n"
                "- Attitude classique française :\n"
                "  - héparine durant le 1er trimestre (arrêt AVK de la 5e à la 12e semaine incluse)\n"
                "  - héparine durant les 2 dernières semaines\n"
                "  - AVK entre-temps si dose de warfarine > 5 mg"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Pour la chirurgie extracardiaque : **INR cible < 1,5** avant l'opération, relais par héparine dès INR < 2 (aortique) ou < 2,5 (mitrale)\n"
                "- ⚠ Pour les soins dentaires non invasifs : AVK peuvent être maintenus avec **INR 2-2,5**"
            ), kind="piege"),
        ]),
    ])

    # PARTIE V : POINTS CLES ET NOTIONS INDISPENSABLES
    partie_v = Partie(numero="V", titre="Points clés et notions indispensables", sous_parties=[
        SousPartie(lettre="A", titre="Points clés", rows=[
            FicheRow(concept="Généralités sur les prothèses", detail_md=(
                "- Le remplacement valvulaire est un geste de chirurgie courante\n"
                "- Les prothèses mécaniques à double ailette sont très performantes\n"
                "- Les bioprothèses sont également fiables\n"
                "- Le remplacement valvulaire entraîne généralement une nette amélioration clinique\n"
                "- Les prothèses restent un substitut imparfait des valves natives"
            )),
            FicheRow(concept="Mortalité périopératoire", detail_md=(
                "- N'excède pas **1 à 2 %** pour un remplacement monovalvulaire chez patient jeune en bonne santé\n"
                "- Augmente avec :\n"
                "  - l'âge\n"
                "  - le nombre de gestes à effectuer\n"
                "  - les comorbidités\n"
                "- La survie dépend de la pathologie initiale, de son retentissement cardiaque, des comorbidités et des complications liées aux prothèses"
            )),
            FicheRow(concept="Risques principaux", detail_md=(
                "- **Prothèses mécaniques** : complications thromboemboliques et hémorragiques\n"
                "- **Bioprothèses** : dégénérescence\n"
                "- Toutes prothèses : **endocardite infectieuse**"
            )),
            FicheRow(concept="Outils de surveillance", detail_md=(
                "- Examen clé : **échodoppler transthoracique (ETT)**\n"
                "- Diagnostic des dysfonctions : imagerie multimodale (ETT, ETO, scanner, TEP-scanner, radiocinéma)\n"
                "- Le diagnostic peut être difficile, l'examen nécessite un échographiste entraîné"
            )),
            FicheRow(concept="Contraintes pour les patients", detail_md=(
                "- Observance du traitement anticoagulant à vie pour les porteurs de prothèses mécaniques\n"
                "- Prophylaxie de l'endocardite infectieuse\n"
                "- Pour les mécaniques : la surveillance de l'AVK est l'objectif principal du suivi par le médecin traitant\n"
                "- L'autosurveillance et l'autoadaptation peuvent améliorer la qualité de vie d'environ **50 % des patients**\n"
                "- **AOD contre-indiqués** chez les porteurs de prothèse mécanique et en cas de sténose mitrale"
            )),
            FicheRow(concept="Avenir du remplacement valvulaire", detail_md=(
                "- Dégénérescence inéluctable des bioprothèses (10-15 ans), conduisant à discuter une nouvelle intervention\n"
                "- Remplacement valvulaire percutané en plein essor :\n"
                "  - sténose aortique sur valve native\n"
                "  - valve biologique dégénérée (**valve-in-valve**)\n"
                "- Alternative importante à la chirurgie cardiaque dans des indications sélectionnées"
            )),
        ]),
        SousPartie(lettre="B", titre="Notions indispensables et inacceptables", rows=[
            FicheRow(concept="◆ Notions indispensables", detail_md=(
                "- Deux grands types de prothèses : **mécaniques** et **biologiques**\n"
                "- Bioprothèses = chirurgicales ou percutanées (TAVI/TAVR)\n"
                "- Mécaniques : durent à vie, AVK à vie, risques thromboembolique/hémorragique, AOD contre-indiqués\n"
                "- Biologiques : pas d'AC sauf postop précoce, dégénérescence inéluctable, réopération moyenne à 10 ans\n"
                "- TAVI : patients inopérables / risque chirurgical / > 75 ans si anatomie favorable\n"
                "- Prothèses = corps étrangers → risque accru d'**EI** → prophylaxie soigneuse\n"
                "- **ETT** = examen clé de surveillance\n"
                "- Imagerie multimodale en cas de dysfonction (ETO, radiocinéma, scanner)\n"
                "- Suivi minimum annuel par un cardiologue"
            )),
            FicheRow(concept="", detail_md=(
                "- NE PAS prescrire des **AOD** à un porteur de valve mécanique\n"
                "- NE PAS prescrire une antibiothérapie à l'aveugle en cas de fièvre chez un porteur de prothèse\n"
                "- NE PAS oublier l'éducation thérapeutique (prévention EI et anticoagulation)\n"
                "- NE PAS oublier une EI devant toute fièvre\n"
                "- NE PAS oublier de référer à un spécialiste un porteur de prothèse :\n"
                "  - symptomatique\n"
                "  - avec souffle de novo (symptomatique ou non)\n"
                "  - pour son suivi annuel"
            ), kind="piege"),
        ]),
    ])

    # TABLEAUX DE SYNTHESE
    tableaux = [
        TableauSynthese(titre="Comparaison Prothèses mécaniques vs Biologiques", markdown=(
            "| Critère | Mécanique | Biologique chirurgicale | Bioprothèse TAVI |\n"
            "|---------|-----------|------------------------|------------------|\n"
            "| **Matériau** | Titane/carbone + dacron | Xénogreffe (péricarde bovin/équin, valve porcine) | Bioprothèse animale |\n"
            "| **Anticoagulation** | AVK à vie (cible 2,5-4) | Aortique : aucune ou 3 mois ; Mitrale : 3 mois si sinusal | Aspirine faible dose |\n"
            "| **AOD** | **Contre-indiqués** | Possibles après 3 mois si indication non valvulaire | Possibles si FA/MTE |\n"
            "| **Durabilité** | À vie | 10 ans (5-15 selon type) | < 5 ans de recul |\n"
            "| **Risque principal** | Thromboembolique + hémorragique (AVK) | Dégénérescence | Dégénérescence + thrombose feuillets |\n"
            "| **Population cible** | Aortique < 60 ans ; Mitrale < 65 ans | Aortique > 65 ans ; Mitrale > 70 ans | > 75 ans, haut risque chirurgical, CI chirurgie |"
        )),
        TableauSynthese(titre="Complications des prothèses valvulaires", markdown=(
            "| Complication | Fréquence | Mécanisme | Diagnostic clé |\n"
            "|-------------|-----------|-----------|----------------|\n"
            "| **Embolies systémiques** | La plus fréquente | Thrombus à partir de la prothèse | Cérébrales 70 % |\n"
            "| **Thrombose obstructive** | Surtout mécaniques | AVK insuffisant +++ | Radiocinéma + ETT/ETO + scanner injecté |\n"
            "| **Médiastinite postop** | ~1 % | Staph doré/blanc | Postop précoce, mortalité 20 % |\n"
            "| **EI précoce** | Postop < 1 an | Contamination per-op staph | Mortalité 50 %, abcès, désinsertion |\n"
            "| **EI tardive** | > 1 an | Comparable valve native | Hémocultures + ETT/ETO/TEP |\n"
            "| **Hémorragie sous AVK** | 1,2 %/an | Surdosage AVK | Selon site (cérébral, dig, urinaire) |\n"
            "| **Dégénérescence bioprothèse** | Inéluctable | Calcifications, déchirure | 5-15 ans, ETT + scanner |\n"
            "| **Désinsertion** | ~5 % | Lâchage sutures ou EI | ETO : fuite paraprothétique + hémolyse |\n"
            "| **Pannus fibreux** | Rare | Tissu cicatriciel excessif | Sténose orificielle |\n"
            "| **Mismatch** | Variable | Surface prothèse < surface corp. | Gradients élevés sans anomalie |"
        )),
        TableauSynthese(titre="Surveillance ETT selon type de prothèse", markdown=(
            "| Type | Fréquence ETT |\n"
            "|------|---------------|\n"
            "| **Mécanique** | Tous les 1 à 2 ans (sans complication) |\n"
            "| **Bioprothèse chirurgicale** | 3 mois + 1 an, puis annuelle |\n"
            "| **Prothèse percutanée / dernière génération** | Attention particulière (durabilité moins connue) |\n"
            "| **ETO** | Seulement si suspicion de dysfonction (systématique si thrombose / EI / désinsertion) |\n"
            "| **ETT de référence** | 2e-4e mois postopératoire |"
        )),
        TableauSynthese(titre="INR cible selon risque thrombotique de la prothèse et facteurs de risque patient", markdown=(
            "| Risque thrombotique prothèse | 0 FdR patient | ≥ 1 FdR patient |\n"
            "|------------------------------|---------------|-----------------|\n"
            "| **Faible** (Saint Jude, On-X, Carbomedics, Medtronic Hall, Sorin Bicarbon, ATS - position aortique) | **2,5** | **3,0** |\n"
            "| **Moyen** (autres double ailette récentes, données insuffisantes) | **3,0** | **3,5** |\n"
            "| **Élevé** (Björk-Shiley monodisque, Starr à bille) | **3,5** | **4,0** |"
        )),
        TableauSynthese(titre="Anticoagulation selon situation", markdown=(
            "| Situation | Anticoagulation recommandée |\n"
            "|-----------|----------------------------|\n"
            "| Prothèse mécanique aortique faible risque (Saint Jude...) | AVK à vie, INR 2,5 |\n"
            "| Prothèse mécanique mitrale | AVK à vie, INR 3-4 |\n"
            "| Prothèse mécanique + FdR patient | INR cible majoré |\n"
            "| Bioprothèse aortique en sinusal | Aspirine ≥ 3 mois ou AOD |\n"
            "| Bioprothèse aortique + FA | AOD dès postop immédiat |\n"
            "| Bioprothèse mitrale en sinusal | AVK 3 premiers mois |\n"
            "| Bioprothèse mitrale + FA | AOD possible postop immédiat |\n"
            "| TAVI sans indication AC | Aspirine faible dose |\n"
            "| TAVI + FA / MTE | AVK ou AOD seuls |\n"
            "| Bioprothèse > 3 mois + indication non valvulaire | Tous AC autorisés |"
        )),
        TableauSynthese(titre="Conduite à tenir selon situation particulière", markdown=(
            "| Situation | Conduite |\n"
            "|-----------|----------|\n"
            "| Hémorragie sévère | Arrêt AVK, héparine pour TCA 1,5-2 fois témoin |\n"
            "| Hémorragie vitale | Plasma frais + vit K 0,5-2 mg, interruption AC temporaire |\n"
            "| Extraction dentaire | AVK maintenus, INR 2-2,5 |\n"
            "| Chirurgie à faible risque (cataracte) | AVK maintenus |\n"
            "| Chirurgie extracardiaque | Arrêt AVK pour INR < 1,5, relais HNF si INR < 2 (Ao) ou < 2,5 (Mi) |\n"
            "| Grossesse < 5 mg warfarine | AVK 1er-3e trimestre, héparine fin de grossesse |\n"
            "| Grossesse > 5 mg warfarine | Héparine 1er trimestre (S5-S12), AVK, héparine 2 dernières S |"
        )),
    ]

    # CHIFFRES CLES
    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| **Anticoagulation bioprothèse mitrale** | **3 mois** | Si rythme sinusal |\n"
        "| **TAVI** | **≥ 75 ans** | Consensus pour TAVI en 1re intention ESC 2021 |\n"
        "| **Choix mécanique aortique** | **< 60 ans** | Préférée |\n"
        "| **Choix mécanique mitrale** | **< 65 ans** | Préférée |\n"
        "| **Choix bioprothèse aortique** | **> 65 ans** | Indiquée |\n"
        "| **Choix bioprothèse mitrale** | **> 70 ans** | Indiquée |\n"
        "| **Durabilité bioprothèse** | **10 ans** (5-15) | Moyenne |\n"
        "| **Mortalité périopératoire** | **1-2 %** | Patient jeune sain |\n"
        "| **Médiastinite postop** | **1 %** | Mortalité 20 % des cas |\n"
        "| **Mortalité thrombose aiguë** | **30 %** | Chirurgie d'urgence |\n"
        "| **Mortalité EI précoce** | **50 %** | EI postopératoire |\n"
        "| **Embolies cérébrales** | **70 %** | Des embolies systémiques |\n"
        "| **Risque hémorragique annuel AVK** | **1,2 %/an** | Porteur valve mécanique |\n"
        "| **Désinsertions** | **5 %** | Surtout premiers mois postop |\n"
        "| **INR cible prothèse mécanique** | **2,5 à 4** | Tolérance ± 0,5 |\n"
        "| **Variation INR tolérée** | **± 0,5** | Autour de la cible |\n"
        "| **ETT de référence** | **2e-4e mois** | Postopératoire |\n"
        "| **Suivi cardiologue** | **1-2/an** | Après ETT référence |\n"
        "| **Suivi médecin traitant** | **Tous les 3 mois** | Pour AVK |\n"
        "| **Réadaptation cardiaque** | **3-4 sem** | Vers J8 postop |\n"
        "| **Surveillance INR initial** | **1-2/sem** | Jusqu'à équilibre |\n"
        "| **Surveillance INR au long cours** | **≥ 1/mois** | Patient stable |\n"
        "| **Amoxicilline prophylaxie dentaire** | **3 g 1h avant** | Avant geste dentaire |\n"
        "| **Suivi dentaire** | **≥ 2/an** | Biannuel minimum |\n"
        "| **Suivi automesure INR** | **50 % des patients** | Possible (CoaguChek) |\n"
        "| **Remboursement automesure** | **2017** | Uniquement prothèses méca |\n"
        "| **Mortalité maternelle grossesse** | **1-4 %** | Valve mécanique |\n"
        "| **Événements sérieux grossesse** | **40 %** | Valve mécanique |\n"
        "| **Tératogénicité AVK** | **6e-12e SA** | Risque dose-dépendant |\n"
        "| **Seuil warfarine grossesse** | **5 mg** | Choix de stratégie |\n"
        "| **TCA héparine en hémorragie** | **1,5-2 × témoin** | HNF de relais |\n"
        "| **Vitamine K neutralisation** | **0,5-2 mg** | Si AVK à neutraliser |\n"
        "| **INR avant chirurgie** | **< 1,5** | Chirurgie extracardiaque |\n"
        "| **INR extraction dentaire** | **2-2,5** | Sans arrêt AVK |\n"
        "| **Gradient moyen thrombose bio** | **> 20 mmHg** | (élévation > 10 mmHg) |"
    ))

    points_cles = [
        "Deux types de prothèses : **mécaniques** (durables) et **biologiques** (chirurgicales ou TAVI percutanée)",
        "Prothèses mécaniques : **AVK à vie** (INR 2,5-4), **AOD strictement contre-indiqués**",
        "Bioprothèses : **dégénérescence inéluctable** vers 10 ans, pas d'anticoagulation au long cours",
        "TAVI = patients **> 75 ans**, inopérables ou haut risque chirurgical (ESC 2021)",
        "Toute prothèse = risque accru d'**EI** → prophylaxie dentaire (**amoxicilline 3 g** 1h avant)",
        "Complications : **thromboemboliques** (méca), **dégénérescence** (bio), **EI** (toutes)",
        "Fièvre + prothèse → **hémocultures avant ATB** + ETT/ETO + équipe endocardite",
        "**ETT** = examen clé du suivi ; **ETO** si suspicion de dysfonction de prothèse",
        "Désinsertion = **anémie hémolytique** mécanique (LDH↑, haptoglobine↓, schizocytes)",
        "Chirurgie extracardiaque : arrêt AVK pour **INR < 1,5** + relais HNF (TCA 2x témoin)",
    ]

    fiche_eclair_md = (
        "**Types** : mécaniques (double ailette, à vie, AVK à vie) vs biologiques (xénogreffes ou TAVI/TAVR).\n\n"
        "**Choix** : méca aortique < 60 ans, mitrale < 65 ans. Bio aortique > 65 ans, mitrale > 70 ans. TAVI ≥ 75 ans (ESC 2021).\n\n"
        "**Anticoagulation** : méca = AVK INR 2,5-4, AOD CI. Bio mitrale sinusal : AVK 3 mois. TAVI : aspirine faible dose.\n\n"
        "**Thromboemboliques** : embolies cérébrales 70 %. Thrombose obstructive = urgence vitale, mortalité 30 %. Cause : AVK insuffisant. Diag radiocinéma + ETT/ETO + scanner.\n\n"
        "**EI sur prothèse** : précoce (< 1 an, staph, mortalité 50 %) vs tardive. Fièvre = hémocultures avant ATB + ETT/ETO. Prophylaxie : amoxicilline 3 g 1 h avant soin dentaire.\n\n"
        "**Hémorragie AVK** : 1,2 %/an. Arrêt AVK + héparine TCA 1,5-2 × témoin. Vitale : plasma frais + vit K 0,5-2 mg.\n\n"
        "**Dégénérescence bio** : 10 ans (5-15), mitral > aortique. Diag ETT + scanner.\n\n"
        "**Désinsertion** : 5 %, postop précoce. Évoquer EI. Anémie hémolytique (LDH↑, haptoglobine↓, schizocytes). Diag ETO.\n\n"
        "**Surveillance** : MT/3 mois (AVK). Cardio 1-2/an. ETT référence 2-4 mois. Méca : ETT 1-2 ans. Bio : 3 mois + 1 an puis annuelle. INR : 1-2/sem puis ≥ 1/mois.\n\n"
        "**Chirurgie extracardiaque** : INR < 1,5, relais HNF si INR < 2 (Ao) / < 2,5 (Mi). Dentaire : INR 2-2,5 sans arrêt.\n\n"
        "**Grossesse** : mortalité 1-4 %. Tératogénicité AVK S5-S12. Warfarine < 5 mg : AVK ; sinon héparine T1 + 2 dernières semaines.\n\n"
        "**Inacceptable** : AOD sur méca, ATB à l'aveugle si fébrile, oubli prophylaxie EI."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 153 - Surveillance des porteurs de valve et prothèses vasculaires",
        annee="2025-2026",
        item="Item 153",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 153",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-153_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

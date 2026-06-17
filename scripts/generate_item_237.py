"""Génère la fiche de l'Item 237 - Palpitations (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Définition et diagnostic positif", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition"),
            PlanSousPartie(lettre="B", titre="Diagnostic - Interrogatoire"),
        ]),
        PlanPartie(numero="II", titre="Diagnostic de gravité", sous_parties=[
            PlanSousPartie(lettre="A", titre="Anamnèse alarmante"),
            PlanSousPartie(lettre="B", titre="Signes cliniques de gravité"),
            PlanSousPartie(lettre="C", titre="Électrocardiogramme"),
            PlanSousPartie(lettre="D", titre="Autres examens"),
        ]),
        PlanPartie(numero="III", titre="Diagnostic étiologique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Principes"),
            PlanSousPartie(lettre="B", titre="Moyens diagnostiques"),
            PlanSousPartie(lettre="C", titre="Corrélation électroclinique"),
            PlanSousPartie(lettre="D", titre="Autres examens complémentaires"),
        ]),
        PlanPartie(numero="IV", titre="Étiologies les plus fréquentes", sous_parties=[
            PlanSousPartie(lettre="A", titre="Extrasystoles"),
            PlanSousPartie(lettre="B", titre="Tachycardie sinusale"),
            PlanSousPartie(lettre="C", titre="Tachycardies jonctionnelles"),
            PlanSousPartie(lettre="D", titre="Névrose cardiaque"),
            PlanSousPartie(lettre="E", titre="Troubles du rythme SV et V"),
        ]),
        PlanPartie(numero="V", titre="Notions indispensables et inacceptables", sous_parties=[
            PlanSousPartie(lettre="A", titre="Notions indispensables"),
            PlanSousPartie(lettre="B", titre="Notions inacceptables"),
            PlanSousPartie(lettre="C", titre="Réflexes transversaux"),
        ]),
    ]

    # ── PARTIE I : DÉFINITION ET DIAGNOSTIC POSITIF ──
    partie_i = Partie(numero="I", titre="Définition et diagnostic positif", sous_parties=[
        SousPartie(lettre="A", titre="Définition", rows=[
            FicheRow(concept="◆ Définition des palpitations", detail_md=(
                "- Perception anormale d'un rythme ou de battements cardiaques normaux ou anormaux\n"
                "- Sensation que le cœur se débat dans la poitrine\n"
                "- Sensation que le cœur bat trop fort, trop vite ou irrégulièrement"
            )),
            FicheRow(concept="Localisation variable", detail_md=(
                "- Non spécifique, variable selon les patients :\n"
                "  - Latérocervical le long des axes carotidiens\n"
                "  - Précordium\n"
                "  - Latérothoracique\n"
                "  - Médiothoracique"
            )),
            FicheRow(concept="◆ Caractère du symptôme", detail_md=(
                "- Symptôme **très peu spécifique**\n"
                "- Regroupe des situations cliniques au pronostic extrêmement variable :\n"
                "  - De la tachycardie sinusale réflexe sans caractère pathologique\n"
                "  - À la **tachycardie ventriculaire** compromettant la survie du patient\n"
                "- Trouble subjectif témoignant ou non d'une anomalie cardiaque\n"
                "- Souvent anxiogène"
            )),
            FicheRow(concept="", detail_md=(
                "- Les palpitations sont un symptôme subjectif peu spécifique.\n"
                "- L'enjeu majeur = **distinguer une cause bénigne d'une arythmie maligne** "
                "potentiellement létale."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Diagnostic - Interrogatoire", rows=[
            FicheRow(concept="◆ Démarche globale", detail_md=(
                "- Enquête minutieuse indispensable pour établir un diagnostic positif\n"
                "- Le bilan doit :\n"
                "  - Rechercher l'étiologie\n"
                "  - Évaluer la tolérance et le pronostic\n"
                "  - Apprécier le risque d'**arythmie maligne** et de **mort subite**"
            )),
            FicheRow(concept="◆ Caractéristiques de l'épisode", detail_md=(
                "- Durée : secondes, minutes, heures\n"
                "- Facteur déclenchant\n"
                "- **Mode de début et de fin** : brutal ou progressif\n"
                "- Permanent ou paroxystique\n"
                "- Survenue à l'effort ou au repos\n"
                "- Fréquence des crises\n"
                "- Caractère régulier ou irrégulier des sensations\n"
                "- Sensation d'éréthisme"
            )),
            FicheRow(concept="◆ Antécédents à rechercher", detail_md=(
                "- Antécédents cardiovasculaires évocateurs de cardiopathie :\n"
                "  - Infarctus du myocarde, HTA, myocardiopathie, etc.\n"
                "- **Antécédents familiaux de mort subite** :\n"
                "  - Syndrome de **Brugada**\n"
                "  - **QT long**\n"
                "  - Dysplasie arythmogène du ventricule droit (**DAVD**)\n"
                "- Traitements :\n"
                "  - Antiarythmiques\n"
                "  - Traitements **allongeant le QT**"
            )),
            FicheRow(concept="Astuce clinique", detail_md=(
                "- Faire mimer la perception au patient en tapotant avec son doigt "
                "sur le bord d'une table\n"
                "- Permet d'évaluer le rythme (régulier/irrégulier) et la fréquence ressentis"
            )),
            FicheRow(concept="", detail_md=(
                "- L'**interrogatoire** est le temps clé de l'examen clinique.\n"
                "- Il oriente le diagnostic et hiérarchise les hypothèses étiologiques.\n"
                "- Mode début/fin brutal = très évocateur d'une **tachycardie jonctionnelle**."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE II : DIAGNOSTIC DE GRAVITÉ ──
    partie_ii = Partie(numero="II", titre="Diagnostic de gravité", sous_parties=[
        SousPartie(lettre="A", titre="Anamnèse alarmante", rows=[
            FicheRow(concept="⚠ Enjeu pronostique", detail_md=(
                "- Devant toute palpitation : éliminer un diagnostic de gravité "
                "mettant en jeu le **pronostic vital**\n"
                "- Risque d'arythmie ventriculaire potentiellement létale : **TV, FV**"
            )),
            FicheRow(concept="◆ Antécédents personnels alarmants", detail_md=(
                "- Infarctus du myocarde, HTA ou autre cardiopathie\n"
                "- Troubles du rythme connus\n"
                "- Appareillage par stimulateur ou défibrillateur"
            )),
            FicheRow(concept="◆ Antécédents familiaux alarmants", detail_md=(
                "- Mort subite familiale, surtout chez l'enfant ou l'adolescent\n"
                "- Mort subite du nourrisson dans la famille\n"
                "- **Mort subite avant 35 ans** → arythmies de cause génétique\n"
                "- Faire l'arbre généalogique systématiquement\n"
                "- Pathologies génétiques à évoquer :\n"
                "  - Syndrome de **Brugada**\n"
                "  - **QT long**\n"
                "  - Dysplasie arythmogène du ventricule droit"
            )),
            FicheRow(concept="Médicaments à risque", detail_md=(
                "- Antiarythmiques\n"
                "- Traitements allongeant le QT (risque de **torsade de pointe**)"
            )),
        ]),
        SousPartie(lettre="B", titre="Signes cliniques de gravité", rows=[
            FicheRow(concept="⚠ Critères de mauvaise tolérance", detail_md=(
                "- Recherche des signes traduisant une baisse du débit cardiaque "
                "ou une complication de l'arythmie :\n"
                "  - **FC > 150 bpm**\n"
                "  - Hypotension artérielle, signes d'hypoperfusion périphérique\n"
                "  - Angor (parfois fonctionnel)\n"
                "  - Signes d'insuffisance cardiaque (dyspnée)\n"
                "  - Signes neurologiques évocateurs d'un infarctus cérébral "
                "(embolie sur fibrillation atriale)\n"
                "  - Trouble de conscience\n"
                "  - Syncope ou lipothymie"
            )),
            FicheRow(concept="", detail_md=(
                "- Signes de gravité = **mauvaise tolérance hémodynamique** "
                "ou complication (AVC, OAP, choc).\n"
                "- Justifient une prise en charge urgente en milieu spécialisé "
                "(USIC, réanimation)."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Électrocardiogramme", rows=[
            FicheRow(concept="◆ ECG = pierre angulaire diagnostique", detail_md=(
                "- Réalisation systématique même si souvent normal au repos\n"
                "- Peut permettre :\n"
                "  - Le diagnostic si symptômes concomitants\n"
                "  - De suspecter une étiologie\n"
                "- Objectif : obtenir un **ECG en crise** (corrélation électroclinique)"
            )),
            FicheRow(concept="★ ⚠ Urgence absolue à l'ECG", detail_md=(
                "- **Tachycardie régulière à QRS larges = TV jusqu'à preuve du contraire +++**\n"
                "  - Impose de se préparer à réanimer\n"
                "- Autres anomalies ECG graves :\n"
                "  - Anomalies de repolarisation faisant craindre un **SCA**\n"
                "    - Surtout en cas de gêne thoracique\n"
                "    - Mais peut être un angor fonctionnel si **FC > 200 bpm**\n"
                "  - Tachycardie à QRS fins **> 150 bpm** avec signes cliniques de gravité"
            )),
            FicheRow(concept="◆ Manœuvres vagales / Adénosine en crise", detail_md=(
                "- Manœuvres vagales ou injection d'**adénosine** "
                "(Striadyne®, Krénosin®) en flash\n"
                "- ⚠ Contre-indications : **asthme**, **HTA non contrôlée**\n"
                "- Mécanisme : blocage transitoire du nœud atrioventriculaire\n"
                "- 3 effets possibles :\n"
                "  - **Interruption brutale** de la tachycardie → "
                "très évocateur de tachycardie jonctionnelle (réentrée intranodale ou voie accessoire)\n"
                "  - **Ralentissement** de la fréquence ventriculaire → permet de mieux visualiser "
                "l'activité atriale (FA, flutter, tachycardie atriale)\n"
                "  - **Pas d'effet** sur la fréquence ventriculaire en cas de tachycardie ventriculaire"
            )),
            FicheRow(concept="", detail_md=(
                "- Toute **tachycardie à QRS larges = TV jusqu'à preuve du contraire**.\n"
                "- Devant une tachycardie régulière à QRS fins : manœuvres vagales / adénosine "
                "(en respectant les CI) = test diagnostique."
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Autres examens", rows=[
            FicheRow(concept="◆ Échocardiographie transthoracique (ETT)", detail_md=(
                "- **Systématique** pour rechercher une cardiopathie sous-jacente\n"
                "- Analyse :\n"
                "  - Cinétique ventriculaire gauche\n"
                "  - Fraction d'éjection ventriculaire gauche (**FEVG**)\n"
                "  - Recherche de cardiopathie dilatée, hypertrophiée\n"
                "  - Taille des oreillettes"
            )),
            FicheRow(concept="Examens complémentaires selon contexte", detail_md=(
                "- IRM cardiaque\n"
                "- Épreuve d'effort\n"
                "- Coronarographie\n"
                "- Adaptés selon l'étiologie suspectée"
            )),
        ]),
    ])

    # ── PARTIE III : DIAGNOSTIC ÉTIOLOGIQUE ──
    partie_iii = Partie(numero="III", titre="Diagnostic étiologique", sous_parties=[
        SousPartie(lettre="A", titre="Principes", rows=[
            FicheRow(concept="◆ Trois principes fondamentaux", detail_md=(
                "- **1.** Rechercher une cardiopathie sous-jacente\n"
                "  - Si absente → palpitations sur cœur sain\n"
                "- **2.** Rechercher une cause extracardiaque si bilan cardiovasculaire normal\n"
                "- **3.** Établir une **corrélation électroclinique** = "
                "concordance entre symptômes et anomalies ECG"
            )),
            FicheRow(concept="", detail_md=(
                "- **Corrélation électroclinique** = objectif diagnostique central.\n"
                "- Documenter un tracé ECG au moment exact des palpitations."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Moyens diagnostiques", rows=[
            FicheRow(concept="◆ Causes extracardiaques à rechercher", detail_md=(
                "- Excitants : alcool, tabac, cocaïne, amphétamines\n"
                "- Médicaments : sympathomimétiques, hormones thyroïdiennes\n"
                "- **Grossesse**\n"
                "- **Hyperthyroïdie**\n"
                "- Fièvre\n"
                "- Déshydratation\n"
                "- Syndrome d'apnées du sommeil (**SAOS**)"
            )),
            FicheRow(concept="◆ Éléments d'orientation diagnostique", detail_md=(
                "- **Crise polyurique finale** → évoque une tachycardie jonctionnelle\n"
                "- Début brutal + fin brutale → tachycardie jonctionnelle\n"
                "- Démarrage au changement brusque de position → tachycardie jonctionnelle"
            )),
            FicheRow(concept="◆ Examens biologiques de routine", detail_md=(
                "- Ionogramme\n"
                "- NFS\n"
                "- Alcoolémie\n"
                "- **β-hCG**\n"
                "- **TSH**\n"
                "- Autres selon le contexte"
            )),
            FicheRow(concept="Examens complémentaires de 2e intention", detail_md=(
                "- IRM myocardique\n"
                "- Épreuve d'effort : reproduit les palpitations si elles surviennent "
                "exclusivement à l'effort\n"
                "- Coronarographie en cas de doute sur une atteinte ischémique"
            )),
        ]),
        SousPartie(lettre="C", titre="Corrélation électroclinique - ECG percritique", rows=[
            FicheRow(concept="◆ Principe", detail_md=(
                "- Objectif central : obtenir un tracé ECG concomitant des palpitations\n"
                "- Plus la durée d'enregistrement est longue, plus la **sensibilité** est bonne\n"
                "- Adapter le moyen à la fréquence de survenue des crises"
            )),
            FicheRow(concept="ECG 12 dérivations de repos", detail_md=(
                "- Durée : **10 secondes**\n"
                "- Corrélation électroclinique rarement obtenue aux urgences ou en consultation\n"
                "- Signes à rechercher sur ECG de repos :\n"
                "  - Extrasystoles supraventriculaires → rechercher FA, flutter, "
                "tachycardie atriale focale\n"
                "  - Extrasystoles ventriculaires → rechercher TV\n"
                "  - Aspect de syndrome de **Brugada**\n"
                "  - Aspect de cardiopathie ischémique\n"
                "  - Voie accessoire (pré-excitation)\n"
                "  - Syndrome du **QT long** (torsade de pointe)\n"
                "  - Cardiomyopathie hypertrophique\n"
                "  - Repolarisation précoce"
            )),
            FicheRow(concept="◆ Holter ECG", detail_md=(
                "- Durée : **24 à 96 heures**\n"
                "- Intéressant si palpitations fréquentes"
            )),
            FicheRow(concept="◆ ECG ambulatoire de longue durée", detail_md=(
                "- Durée **jusqu'à 21 jours**\n"
                "- Intéressant si palpitations peu fréquentes (**< 1 fois/semaine**)"
            )),
            FicheRow(concept="◆ Holter implantable", detail_md=(
                "- Durée de surveillance : **3 à 5 ans**\n"
                "- Implanté en consultation, position parasternale sous-cutanée\n"
                "- Enregistre asystolies, bradycardies, tachycardies\n"
                "- Moniteur remis au patient pour la corrélation électroclinique\n"
                "- Suivi possible à distance par télécardiologie"
            )),
            FicheRow(concept="Montres connectées / smartphones", detail_md=(
                "- Tracé ECG à partir d'au moins **2 électrodes** sur la montre/smartphone\n"
                "- Tracés de bonne qualité, piste D1\n"
                "- Acquisition automatique ou déclenchée par le patient lors des symptômes\n"
                "- Permet une corrélation électroclinique (cf. items 17 et 18)"
            )),
            FicheRow(concept="", detail_md=(
                "- Hiérarchie d'enregistrement : **ECG 12D → Holter 24-96 h → "
                "ambulatoire 21 j → holter implantable**.\n"
                "- Plus la durée est longue, plus la sensibilité de corrélation est élevée."
            ), kind="mnemo"),
        ]),
        SousPartie(lettre="D", titre="Autres examens complémentaires", rows=[
            FicheRow(concept="◆ Étude électrophysiologique endocavitaire (EEP)", detail_md=(
                "- Intérêt diagnostique :\n"
                "  - Recherche d'une dualité nodale (**TRIN**)\n"
                "  - Recherche d'une **voie accessoire**\n"
                "  - Déclenchement de trouble du rythme supraventriculaire "
                "par stimulation OD\n"
                "  - Déclenchement de trouble du rythme ventriculaire par "
                "**stimulation ventriculaire programmée** (apex + infundibulum pulmonaire)\n"
                "- Intérêt thérapeutique :\n"
                "  - **Ablation** d'arythmie atriale, TRIN, voie accessoire, etc."
            )),
            FicheRow(concept="Épreuve d'effort", detail_md=(
                "- Double intérêt :\n"
                "  - Doute sur un angor\n"
                "  - Documenter des palpitations à l'effort"
            )),
            FicheRow(concept="Autres examens spécialisés", detail_md=(
                "- IRM myocardique\n"
                "- Coronarographie\n"
                "- Tests médicamenteux : isoprénaline, ajmaline\n"
                "- Potentiels tardifs ventriculaires (dysplasie arythmogène du VD)"
            )),
        ]),
    ])

    # ── PARTIE IV : ÉTIOLOGIES LES PLUS FRÉQUENTES ──
    partie_iv = Partie(numero="IV", titre="Étiologies les plus fréquentes", sous_parties=[
        SousPartie(lettre="A", titre="Extrasystoles", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- **Activation prématurée ectopique** par rapport à la fréquence attendue\n"
                "- Peut être supraventriculaire (**ESSV**) ou ventriculaire (**ESV**)"
            )),
            FicheRow(concept="◆ Caractéristiques des extrasystoles", detail_md=(
                "- Repos compensateur (total = double période) OU interpolée "
                "(absence de repos compensateur)\n"
                "- **Monomorphes** (morphologie identique) ou **polymorphes** "
                "(morphologies différentes)\n"
                "- Présentation :\n"
                "  - Isolées\n"
                "  - **Bigéminées** : alternance 1 complexe normal / 1 extrasystole\n"
                "  - **Trigéminées** : alternance 2 complexes normaux / 1 extrasystole"
            )),
            FicheRow(concept="Pronostic général", detail_md=(
                "- Ne sont pas pathologiques en elles-mêmes\n"
                "- Mais doivent faire rechercher :\n"
                "  - Une cardiopathie sous-jacente\n"
                "  - Une pathologie extracardiaque"
            )),
            FicheRow(concept="◆ Causes extracardiaques d'extrasystoles", detail_md=(
                "- Alcoolisation\n"
                "- Électrocution\n"
                "- Pathologies respiratoires\n"
                "- **Hyperthyroïdie**\n"
                "- Anomalies électrolytiques\n"
                "- Anxiété, dépression\n"
                "- **Grossesse**\n"
                "- Syndrome d'apnées du sommeil"
            )),
            FicheRow(concept="◆ Bilan minimal devant une extrasystolie", detail_md=(
                "- ECG de repos : analyse de l'aspect de l'extrasystole + cardiopathie\n"
                "- Échocardiographie transthoracique : morphologie\n"
                "- Épreuve d'effort\n"
                "- Holter ECG :\n"
                "  - Charge en extrasystoles\n"
                "  - Morphologies différentes\n"
                "  - **Couplage court**"
            )),
            FicheRow(concept="◆ ESV et risque de FA", detail_md=(
                "- Chez le patient obèse, diabétique ou hypertendu : "
                "association extrasystoles ↔ **FA**\n"
                "- Répéter les holter ECG pour rechercher une FA à risque thromboembolique"
            )),
            FicheRow(concept="◆ Caractéristiques ECG des ESSV", detail_md=(
                "- Morphologie de l'**onde P'** différente de l'activation sinusale (P)\n"
                "- Permet d'évaluer la position de l'activation ectopique dans l'oreillette\n"
                "- QRS habituellement identique au rythme sinusal "
                "(ou différent si aberration de conduction)\n"
                "- Onde P' bloquée possible si trop précoce "
                "(nœud AV en période réfractaire)"
            )),
            FicheRow(concept="⚠ Couplage court ventriculaire", detail_md=(
                "- ESV très précoces survenant dans la phase initiale ascendante de l'onde T\n"
                "- = **Indicateur majeur de risque rythmique**\n"
                "- Favorise le démarrage d'une arythmie ventriculaire maligne"
            )),
            FicheRow(concept="", detail_md=(
                "- **Couplage court** d'une ESV sur l'onde T (R/T) = "
                "signal d'alerte majeur (risque de TV/FV).\n"
                "- Toute extrasystolie nouvelle = recherche systématique de cardiopathie + "
                "cause extracardiaque."
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Tachycardie sinusale", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- Accélération de la fréquence sinusale au repos **> 100 bpm**\n"
                "- Activité sinusale : onde P de morphologie issue du nœud sinusal\n"
                "- Début et fin progressifs"
            )),
            FicheRow(concept="◆ Causes cardiaques (réponse physiologique adaptée)", detail_md=(
                "- Insuffisance cardiaque\n"
                "- **Embolie pulmonaire**\n"
                "- Épanchement péricardique"
            )),
            FicheRow(concept="◆ Causes extracardiaques adaptatives", detail_md=(
                "- Fièvre, sepsis\n"
                "- Anémie, hypovolémie\n"
                "- Hypoxie\n"
                "- **Hyperthyroïdie**\n"
                "- **Grossesse**\n"
                "- **Alcoolisme**\n"
                "- Hypotension artérielle\n"
                "- **Syndrome d'apnées du sommeil**\n"
                "- Sevrage brutal en β-bloquants\n"
                "- Pathologie psychiatrique, sevrage alcoolique\n"
                "- Médicaments : sympathomimétiques, vasodilatateurs, atropiniques"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Traitement de la cause** : nécessaire et le plus souvent suffisant"
            )),
            FicheRow(concept="◆ Tachycardie sinusale inappropriée", detail_md=(
                "- Forme exceptionnelle, isolée et non adaptative\n"
                "- Contextes : orthostatisme, anxiété"
            )),
            FicheRow(concept="", detail_md=(
                "- **4 causes extracardiaques majeures à retenir** pour la tachycardie sinusale "
                "selon les points clés : "
                "**grossesse, hyperthyroïdie, syndrome d'apnées du sommeil, alcoolisme**."
            ), kind="mnemo"),
        ]),
        SousPartie(lettre="C", titre="Tachycardies jonctionnelles", rows=[
            FicheRow(concept="◆ Définition - Maladie de Bouveret", detail_md=(
                "- Symptômes initialement décrits par Bouveret = **maladie de Bouveret**\n"
                "- Tachycardies incluant la jonction atrioventriculaire :\n"
                "  - Réentrée intranodale (**TRIN**)\n"
                "  - Voies accessoires (**Wolff-Parkinson-White**)"
            )),
            FicheRow(concept="◆ Tachycardie par réentrée intranodale (TRIN) - Terrain", detail_md=(
                "- TJ les **plus fréquentes**\n"
                "- Survenue chez sujets jeunes (adolescents, adultes jeunes)\n"
                "- Cœur sain"
            )),
            FicheRow(concept="◆ Symptômes typiques de TRIN", detail_md=(
                "- Palpitations parfois ressenties avec battements cervicaux\n"
                "- **Début brutal et fin brutale**\n"
                "- Durée variable : quelques minutes à plusieurs heures\n"
                "- **Polyurie en fin d'accès**\n"
                "- Bonne tolérance clinique le plus souvent\n"
                "- Inconfort gênant pour la qualité de vie\n"
                "- Arrêt par manœuvre vagale ou injection d'adénosine / ATP"
            )),
            FicheRow(concept="◆ Mécanisme de la TRIN", detail_md=(
                "- Dissociation au sein du nœud AV en 2 voies :\n"
                "  - Voie rapide antérieure et supérieure : période réfractaire longue\n"
                "  - Voie lente postérieure et inférieure : période réfractaire courte\n"
                "- Réentrée :\n"
                "  - Antérograde par la voie lente\n"
                "  - Rétrograde par la voie rapide\n"
                "- Trigger : extrasystole atriale bloquée dans la voie rapide, "
                "poursuivant dans la voie lente"
            )),
            FicheRow(concept="◆ Caractéristiques ECG de la TRIN", detail_md=(
                "- ECG de repos le plus souvent normal\n"
                "- Fréquence : **130 à 250 bpm** (variable selon patient et âge)\n"
                "- **QRS fins** le plus souvent (sauf aberration de conduction)\n"
                "- Activité atriale rétrograde : **P' négatives en dérivations inférieures**\n"
                "- P' proches de la fin du QRS"
            )),
            FicheRow(concept="◆ Prise en charge de la TRIN", detail_md=(
                "- Dépend de la symptomatologie et de la gêne\n"
                "- Options :\n"
                "  - Abstention\n"
                "  - Pill in the pocket\n"
                "  - **Ablation de la voie lente** = traitement de référence\n"
                "- Risque rare de bloc atrioventriculaire complet après ablation"
            )),
            FicheRow(concept="◆ Syndrome de Wolff-Parkinson-White - Terrain", detail_md=(
                "- TJ sur voie accessoire (ex : **faisceau de Kent**)\n"
                "- Survenue préférentielle chez jeunes patients à cœur sain"
            )),
            FicheRow(concept="◆ Mécanisme - Voie accessoire", detail_md=(
                "- Isolation électrique normale entre oreillettes et ventricules "
                "(massif valvulaire fibreux)\n"
                "- Passage normal uniquement par le nœud AV et le faisceau de His\n"
                "- **Voie accessoire** = bandelette musculaire au travers de "
                "l'isolation fibreuse\n"
                "- Permet une conduction directe oreillettes ↔ ventricules\n"
                "- Involue habituellement avec l'âge"
            )),
            FicheRow(concept="◆ Signes ECG du WPW au repos", detail_md=(
                "- Espace **PR court < 120 ms** sans retour à la ligne isoélectrique\n"
                "- **Onde delta** : aspect triangulaire du début du complexe QRS\n"
                "- **QRS large > 120 ms** dû à l'onde delta\n"
                "- Troubles de la repolarisation\n"
                "- L'aspect de préexcitation :\n"
                "  - Diminue ou disparaît avec l'atropine\n"
                "  - Augmente avec les manœuvres vagales"
            )),
            FicheRow(concept="Voies accessoires occultes", detail_md=(
                "- Voies cachées : conduction uniquement ventricule → oreillette\n"
                "- Voies masquées : majorité de l'influx via la voie nodohissienne\n"
                "- Rendent le diagnostic difficile sur ECG de repos"
            )),
            FicheRow(concept="◆ Tachycardies orthodromiques", detail_md=(
                "- Descente de l'influx par le faisceau de His\n"
                "- Remontée par le faisceau accessoire\n"
                "- ECG : **QRS fins** avec onde P' rétrograde"
            )),
            FicheRow(concept="◆ Tachycardies antidromiques", detail_md=(
                "- Descente de l'influx par le faisceau accessoire\n"
                "- Remontée par le faisceau de His\n"
                "- ECG : **QRS larges** avec aspect de préexcitation + P' rétrograde"
            )),
            FicheRow(concept="⚠ FA sur voie accessoire - Aspect super-Wolff", detail_md=(
                "- Les patients WPW présentent plus d'accès de FA\n"
                "- Risque de lipothymie, syncope, **mort subite** lors d'un épisode de FA "
                "conduisant rapidement aux ventricules\n"
                "- Aspect **super-Wolff** : QRS très élargis, irréguliers\n"
                "- Évolution possible vers **fibrillation ventriculaire**"
            )),
            FicheRow(concept="⚠ Voie accessoire maligne", detail_md=(
                "- Période réfractaire antérograde très courte **< 250 ms**\n"
                "- Expose à un rythme ventriculaire potentiellement très rapide\n"
                "- **Indication formelle d'ablation**"
            )),
            FicheRow(concept="⚠ FA sur voie accessoire - Traitement", detail_md=(
                "- Si hémodynamique instable = **cardioversion en urgence**\n"
                "- Si hémodynamique conservée :\n"
                "  - Antiarythmiques de **classe Ic**\n"
                "  - OU **amiodarone**\n"
                "- ⚠ **CONTRE-INDIQUÉS FORMELLEMENT** :\n"
                "  - Adénosine\n"
                "  - Inhibiteurs calciques\n"
                "  - Bêtabloquants\n"
                "  - Digitaliques\n"
                "- Car ils bloquent la conduction nodale sans ralentir la voie accessoire"
            )),
            FicheRow(concept="◆ Indications d'ablation de la voie accessoire", detail_md=(
                "- Patients symptomatiques avec tachycardies réciproques répétitives\n"
                "- Indication indiscutable chez patients avec :\n"
                "  - **FA rapide** + voie accessoire très perméable (PRA courte)\n"
                "- Complication possible : **BAV** si voie accessoire près des voies nodohissiennes"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant une **FA sur WPW à hémodynamique stable** : "
                "Ic ou amiodarone.\n"
                "- **Adénosine, ICa, BB, digitaliques = FORMELLEMENT CONTRE-INDIQUÉS** "
                "(risque de FV)."
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Névrose cardiaque", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- **Diagnostic d'élimination**, assez fréquent\n"
                "- Parfois auto-entretenu par la prise en charge ou les consultations itératives\n"
                "- Crainte irraisonnée de mourir subitement"
            )),
            FicheRow(concept="◆ Critères diagnostiques", detail_md=(
                "- **ECG strictement normal au moment des palpitations**\n"
                "- Souvent obtenu par monitorage de longue durée\n"
                "- À évoquer quand :\n"
                "  - Examens cliniques et paracliniques tous normaux\n"
                "  - Pas de pathologie extracardiaque identifiée\n"
                "  - Patient présente des signes de dépression ou d'anxiété"
            )),
            FicheRow(concept="◆ Prise en charge", detail_md=(
                "- Stopper les investigations à visée cardiologique\n"
                "- Rassurer le patient\n"
                "- Ne pas tenir un langage inadapté\n"
                "- Ne pas parler de spasmophilie\n"
                "- Avis psychiatrique souhaitable"
            )),
            FicheRow(concept="", detail_md=(
                "- **Diagnostic d'élimination** strict.\n"
                "- Notion inacceptable : s'orienter d'emblée vers une cause psychogène "
                "sans bilan minimal."
            ), kind="piege"),
        ]),
        SousPartie(lettre="E", titre="Troubles du rythme SV et V", rows=[
            FicheRow(concept="Autres causes de palpitations", detail_md=(
                "- **Fibrillation atriale** et **flutter atrial** (cf. item 232)\n"
                "- Troubles du rythme ventriculaire (cf. chapitre 15)\n"
                "- Ces pathologies peuvent toutes donner des palpitations"
            )),
        ]),
    ])

    # ── PARTIE V : NOTIONS INDISPENSABLES ET INACCEPTABLES ──
    partie_v = Partie(numero="V", titre="Notions indispensables et inacceptables", sous_parties=[
        SousPartie(lettre="A", titre="Notions indispensables", rows=[
            FicheRow(concept="◆ 3 notions indispensables", detail_md=(
                "- **Notion électroclinique** : documentation du tracé ECG au moment des symptômes\n"
                "- Existence ou non d'une cardiopathie sous-jacente\n"
                "- Signes de gravité à reconnaître"
            )),
        ]),
        SousPartie(lettre="B", titre="Notions inacceptables", rows=[
            FicheRow(concept="⚠ Notions inacceptables", detail_md=(
                "- ⚠ S'orienter d'emblée vers des causes psychogènes "
                "**sans avoir fait un bilan minimal**"
            )),
        ]),
        SousPartie(lettre="C", titre="Réflexes transversaux", rows=[
            FicheRow(concept="Items à connaître", detail_md=(
                "- **Item 17** - Télémédecine, télésanté et téléservices en santé\n"
                "- **Item 18** - Santé et numérique\n"
                "- **Item 231** - Électrocardiogramme : indications et interprétations\n"
                "- **Item 232** - Fibrillation atriale"
            )),
            FicheRow(concept="", detail_md=(
                "- Les montres connectées et smartphones peuvent désormais "
                "enregistrer des **tracés ECG D1** pour faciliter la corrélation électroclinique."
            ), kind="a_retenir"),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Synthèse - Signes de gravité des palpitations", markdown=(
            "| Type | Élément | Implication |\n"
            "|------|---------|-------------|\n"
            "| **Anamnèse** | ATCD personnel IDM, HTA, cardiopathie | Risque accru |\n"
            "| **Anamnèse** | Trouble du rythme connu, PM/DAI | Risque accru |\n"
            "| **Anamnèse** | ATCD familial de mort subite (< 35 ans) | Maladie génétique |\n"
            "| **Anamnèse** | Traitements antiarythmiques / allongeant le QT | Risque iatrogène |\n"
            "| **Clinique** | FC > 150 bpm | Tachycardie mal tolérée |\n"
            "| **Clinique** | Hypotension, hypoperfusion | Bas débit |\n"
            "| **Clinique** | Angor | Souffrance myocardique |\n"
            "| **Clinique** | Dyspnée / signes d'IC | OAP |\n"
            "| **Clinique** | Signes neurologiques | AVC embolique |\n"
            "| **Clinique** | Trouble de conscience, syncope, lipothymie | Bas débit cérébral |\n"
            "| **ECG** | Tachycardie régulière à QRS larges | **TV jusqu'à preuve du contraire** |\n"
            "| **ECG** | Tachycardie à QRS fins > 150 bpm + gravité | Urgence |\n"
            "| **ECG** | Anomalies de repolarisation + douleur | SCA suspecté |"
        )),
        TableauSynthese(titre="Synthèse - Méthodes de corrélation électroclinique", markdown=(
            "| Méthode | Durée | Indication |\n"
            "|---------|-------|------------|\n"
            "| **ECG 12 dérivations** | **10 secondes** | Systématique mais peu rentable hors crise |\n"
            "| **Holter ECG** | **24 à 96 heures** | Palpitations fréquentes |\n"
            "| **ECG ambulatoire longue durée** | **Jusqu'à 21 jours** | Palpitations < 1/semaine |\n"
            "| **Holter implantable** | **3 à 5 ans** | Crises peu fréquentes |\n"
            "| **Montre connectée / smartphone** | À la demande | Symptômes intermittents |\n"
            "| **EEP endocavitaire** | Acte invasif | Diagnostic + thérapeutique (ablation) |"
        )),
        TableauSynthese(titre="Synthèse - Effets des manœuvres vagales / adénosine", markdown=(
            "| Type de tachycardie | Effet | Implication diagnostique |\n"
            "|----------------------|-------|--------------------------|\n"
            "| **Tachycardie jonctionnelle** (TRIN, voie accessoire) | **Arrêt brutal** | Très évocateur |\n"
            "| **FA, flutter, tachycardie atriale** | **Ralentissement** + démasquage activité atriale | Aide au diagnostic |\n"
            "| **Tachycardie ventriculaire** | **Pas d'effet** | TV confirmée |\n"
            "| **Contre-indications** | Asthme, HTA non contrôlée | À respecter |"
        )),
        TableauSynthese(titre="Synthèse - Tachycardies jonctionnelles : TRIN vs WPW", markdown=(
            "| Critère | TRIN | WPW (voie accessoire) |\n"
            "|---------|------|------------------------|\n"
            "| **Terrain** | Sujet jeune, cœur sain (la plus fréquente) | Sujet jeune, cœur sain |\n"
            "| **Mécanisme** | Réentrée intranodale (voie rapide + voie lente) | Voie accessoire AV (faisceau de Kent) |\n"
            "| **ECG repos** | Normal | PR < 120 ms, onde delta, QRS > 120 ms, troubles repolarisation |\n"
            "| **ECG crise** | QRS fins, P' négatives en inférieur, FC 130-250 bpm | Orthodromique (QRS fins) ou antidromique (QRS larges) |\n"
            "| **Symptômes** | Début/fin brutaux, polyurie finale, battements cervicaux | Tachycardies réciproques, FA fréquentes |\n"
            "| **Manœuvres vagales** | Arrêt brutal | Arrêt brutal |\n"
            "| **Risque grave** | Très faible | **FA sur voie accessoire → super-Wolff → FV** |\n"
            "| **Traitement de référence** | **Ablation de la voie lente** | **Ablation de la voie accessoire** |\n"
            "| **CI majeure** | - | ⚠ **Adénosine, ICa, BB, digitaliques** si FA + WPW |"
        )),
        TableauSynthese(titre="Synthèse - Étiologies des palpitations", markdown=(
            "| Étiologie | Caractéristiques | Bilan |\n"
            "|-----------|------------------|-------|\n"
            "| **Extrasystoles SV / V** | Activation prématurée ectopique, isolées/bigéminées/trigéminées | ECG, ETT, EE, Holter |\n"
            "| **Tachycardie sinusale** | FC > 100 bpm, P sinusale, début/fin progressifs | Cause adaptative ou inappropriée |\n"
            "| **TRIN (Bouveret)** | Sujet jeune, cœur sain, début/fin brutaux + polyurie | ECG percritique, EEP |\n"
            "| **WPW** | Voie accessoire (Kent), PR court + onde delta | ECG, EEP, ablation |\n"
            "| **FA / Flutter** | Cf. item 232 | ETT, anticoagulation |\n"
            "| **TV** | Tachycardie à QRS larges | **Urgence**, réanimation |\n"
            "| **Névrose cardiaque** | Diagnostic d'élimination, ECG normal en crise | Avis psychiatrique |"
        )),
        TableauSynthese(titre="Synthèse - Causes extracardiaques à connaître", markdown=(
            "| Catégorie | Cause | Mécanisme principal |\n"
            "|-----------|-------|---------------------|\n"
            "| **Excitants** | Alcool, tabac, cocaïne, amphétamines | Stimulation sympathique |\n"
            "| **Médicaments** | Sympathomimétiques, vasodilatateurs, atropiniques, hormones thyroïdiennes | Stimulation directe |\n"
            "| **Endocrinien** | **Hyperthyroïdie** | Stimulation sympathique |\n"
            "| **Physiologique** | **Grossesse** | Hyperdébit |\n"
            "| **Infection** | Fièvre, sepsis | Tachycardie adaptative |\n"
            "| **Hématologie** | Anémie, hypovolémie | Tachycardie compensatrice |\n"
            "| **Pulmonaire** | Hypoxie, embolie pulmonaire | Tachycardie réflexe |\n"
            "| **SAOS** | **Syndrome d'apnées du sommeil** | Hyperactivité sympathique nocturne |\n"
            "| **Psychogène** | Anxiété, dépression, sevrage alcoolique | Hyperréactivité sympathique |\n"
            "| **Iatrogène** | Sevrage brutal en β-bloquants | Rebond adrénergique |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| **FC seuil de gravité** | **> 150 bpm** | Mauvaise tolérance |\n"
        "| **FC angor fonctionnel** | **> 200 bpm** | À distinguer du SCA |\n"
        "| **ECG 12 dérivations** | **10 secondes** | Examen standard |\n"
        "| **Holter ECG** | **24 à 96 heures** | Palpitations fréquentes |\n"
        "| **ECG ambulatoire longue durée** | **Jusqu'à 21 jours** | Palpitations < 1/semaine |\n"
        "| **Seuil palpitations rares** | **< 1 fois/semaine** | Indication ambulatoire longue durée |\n"
        "| **Holter implantable** | **3 à 5 ans** | Surveillance prolongée |\n"
        "| **Mort subite familiale - seuil âge** | **< 35 ans** | Évoquer maladie génétique |\n"
        "| **Tachycardie sinusale - seuil** | **> 100 bpm au repos** | Définition |\n"
        "| **TRIN - fréquence** | **130 à 250 bpm** | Variable selon patient/âge |\n"
        "| **WPW - PR court** | **< 120 ms** | Critère ECG |\n"
        "| **WPW - QRS large** | **> 120 ms** | Onde delta |\n"
        "| **Voie accessoire maligne** | **PRA < 250 ms** | Indication formelle d'ablation |\n"
        "| **SVP - sites de stimulation** | **2 sites** | Apex VD + infundibulum pulmonaire |\n"
        "| **Montre connectée** | **≥ 2 électrodes** | Piste D1 |"
    ))

    points_cles = [
        "Palpitations = symptôme subjectif peu spécifique ; enjeu = éliminer une **arythmie maligne**",
        "Tachycardie régulière à **QRS larges = TV** jusqu'à preuve du contraire ; se préparer à réanimer",
        "Signes de gravité : **FC > 150 bpm**, hypotension, angor, IC, signes neuro, syncope",
        "ATCD familial de **mort subite < 35 ans** = évoquer Brugada, QT long, DAVD",
        "**Corrélation électroclinique** = ECG au moment exact des palpitations = objectif central",
        "Bilan : **ETT systématique** + iono, NFS, alcoolémie, **β-hCG**, **TSH**",
        "Tachycardie sinusale : 4 causes = **grossesse, hyperthyroïdie, SAOS, alcoolisme**",
        "**TRIN (Bouveret)** : sujet jeune, début/fin brutaux, polyurie finale ; ablation voie lente",
        "**WPW** : PR < 120 ms + onde delta + QRS > 120 ms ; PRA < 250 ms = ablation formelle",
        "**FA sur WPW** : Ic ou amiodarone si stable ; **CI : adénosine, ICa, BB, digitaliques**",
    ]

    fiche_eclair_md = (
        "**Palpitations** : perception anormale des battements. Symptôme subjectif peu spécifique. Enjeu = éliminer arythmie maligne.\n\n"
        "**Interrogatoire** : durée, mode début/fin (brutal = TJ), polyurie finale (TJ), ATCD cardiopathie, ATCD familial mort subite < 35 ans (Brugada, QT long, DAVD), antiarythmiques.\n\n"
        "**Gravité** : FC > 150 bpm, hypotension, angor, IC, signes neuro (AVC sur FA), syncope.\n\n"
        "**ECG** : pierre angulaire. Tachycardie régulière à QRS larges = **TV jusqu'à preuve du contraire**.\n\n"
        "**Manoeuvres vagales / adénosine** : arrêt brutal = TJ, ralentissement = FA/flutter, pas d'effet = TV. CI : asthme, HTA non contrôlée.\n\n"
        "**ETT systématique** : FEVG, oreillettes. Recherche cardiopathie sous-jacente.\n\n"
        "**Corrélation électroclinique** = objectif. ECG 12D 10 s -> Holter 24-96 h -> ambulatoire 21 j -> holter implantable 3-5 ans -> EEP.\n\n"
        "**Bilan bio** : iono, NFS, alcoolémie, beta-hCG, TSH.\n\n"
        "**Causes extracardiaques tachycardie sinusale** : grossesse, hyperthyroïdie, SAOS, alcoolisme.\n\n"
        "**Extrasystoles** : SV ou V. Couplage court ESV/T = alerte (TV/FV). Recherche FA si obèse/diabétique/HTA.\n\n"
        "**TRIN (Bouveret)** : sujet jeune coeur sain. Début/fin brutaux, polyurie, battements cervicaux. ECG : QRS fins, P' négatives en inférieur, 130-250 bpm. Traitement = **ablation voie lente**.\n\n"
        "**WPW (Kent)** : **PR < 120 ms, onde delta, QRS > 120 ms**. Orthodromique QRS fins, antidromique QRS larges. **Voie maligne PRA < 250 ms** -> ablation.\n\n"
        "**FA sur WPW** : risque mort subite (super-Wolff -> FV). Instable = cardioversion. Stable = Ic ou amiodarone. **CI : adénosine, ICa, BB, digitaliques**.\n\n"
        "**Névrose cardiaque** : diagnostic d'élimination (ECG normal en crise + bilan normal + anxiété). Avis psychiatrique.\n\n"
        "**Inacceptable** : conclure cause psychogène sans bilan minimal."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 237 - Palpitations",
        annee="2025-2026",
        item="Item 237",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 237",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-237_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

"""Génère la fiche exhaustive d'Ophtalmologie à partir du PDF source et des annales."""

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


def build_ophtalmologie_fiche() -> FicheData:
    plan = [
        PlanPartie(numero="I", titre="Altérations de la fonction visuelle — BAV brutale", sous_parties=[
            PlanSousPartie(lettre="A", titre="BAV avec oeil rouge et douloureux"),
            PlanSousPartie(lettre="B", titre="BAV avec oeil blanc et indolore — FO non visible"),
            PlanSousPartie(lettre="C", titre="BAV avec oeil blanc et indolore — FO visible et anormal"),
            PlanSousPartie(lettre="D", titre="BAV avec oeil blanc et indolore — FO visible et normal"),
            PlanSousPartie(lettre="E", titre="Anomalies transitoires de la vision"),
        ]),
        PlanPartie(numero="II", titre="BAV progressive et altérations du champ visuel", sous_parties=[
            PlanSousPartie(lettre="A", titre="Cataracte et glaucome chronique"),
            PlanSousPartie(lettre="B", titre="Affections rétiniennes"),
            PlanSousPartie(lettre="C", titre="Altérations du champ visuel"),
        ]),
        PlanPartie(numero="III", titre="Examen ophtalmologique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Anatomie de l'oeil et annexes"),
            PlanSousPartie(lettre="B", titre="Interrogatoire et mesure de l'acuité visuelle"),
            PlanSousPartie(lettre="C", titre="Examen du segment antérieur et mesure de la PIO"),
            PlanSousPartie(lettre="D", titre="Fond d'oeil et lésions élémentaires"),
            PlanSousPartie(lettre="E", titre="Examens complémentaires"),
        ]),
        PlanPartie(numero="IV", titre="Oeil rouge et/ou douloureux", sous_parties=[
            PlanSousPartie(lettre="A", titre="Oeil rouge non douloureux sans BAV"),
            PlanSousPartie(lettre="B", titre="Oeil rouge douloureux sans BAV — Conjonctivites"),
            PlanSousPartie(lettre="C", titre="Oeil rouge douloureux sans BAV — Syndrome sec et sclérite"),
            PlanSousPartie(lettre="D", titre="Oeil rouge douloureux avec BAV — Kératites"),
            PlanSousPartie(lettre="E", titre="Glaucome aigu par fermeture de l'angle"),
        ]),
        PlanPartie(numero="V", titre="Pathologies des paupières", sous_parties=[
            PlanSousPartie(lettre="A", titre="Orgelet et chalazion"),
            PlanSousPartie(lettre="B", titre="Malformations palpébrales"),
            PlanSousPartie(lettre="C", titre="Tumeurs et traumatismes palpébraux"),
        ]),
    ]

    # ── PARTIE I : BAV BRUTALE ──
    partie_i = Partie(numero="I", titre="Altérations de la fonction visuelle — BAV brutale", sous_parties=[
        SousPartie(lettre="A", titre="BAV avec oeil rouge et douloureux", rows=[
            FicheRow(concept="Orientation diagnostique", detail_md=(
                "- Affection aiguë du **segment antérieur** :\n"
                "  - **Kératite aiguë**\n"
                "  - **Glaucome aigu par fermeture de l'angle** (GAFA)\n"
                "  - **Uvéite antérieure**\n"
                "- Triade : oeil rouge + douleur + BAV = **urgence ophtalmologique**"
            )),
            FicheRow(concept="", detail_md=(
                "- Toute BAV brutale avec oeil rouge et douloureux impose un **examen ophtalmologique en urgence**\n"
                "- Les 3 diagnostics à évoquer systématiquement : kératite, GAFA, uvéite antérieure"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="BAV avec oeil blanc et indolore — FO non visible", rows=[
            FicheRow(concept="Hémorragie intravitréenne", detail_md=(
                "- Signes fonctionnels :\n"
                "  - Impression de « **pluie de suie** »\n"
                "  - BAV variable selon importance de l'hémorragie (myodésopsies à simple PL)\n"
                "- Si hémorragie massive avec rétine invisible : **échographie mode B** pour éliminer un DR\n"
                "- Principales causes :\n"
                "  - **RD proliférante**\n"
                "  - OVCR/OBVCR de forme **ischémique**\n"
                "  - Déchirure rétinienne +/- DR\n"
                "  - **Syndrome de Terson** : hémorragie intravitréenne uni/bilatérale + hémorragie méningée "
                "par rupture d'anévrisme/traumatique"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Devant une hémorragie intravitréenne massive avec rétine invisible, "
                "toujours réaliser une **échographie mode B** pour éliminer un **décollement de rétine**"
            ), kind="piege"),
            FicheRow(concept="Hyalite", detail_md=(
                "- Trouble inflammatoire du vitré au cours des **uvéites intermédiaires/postérieures**\n"
                "- BAV d'installation rapidement progressive (quelques jours)\n"
                "- LAF : trouble du vitré avec présence de **cellules inflammatoires**"
            )),
        ]),
        SousPartie(lettre="C", titre="BAV avec oeil blanc et indolore — FO visible et anormal", rows=[
            FicheRow(concept="Étiologies principales", detail_md=(
                "- **OACR/OABCR** (occlusion artère centrale/branche de la rétine)\n"
                "- **OVCR/OBVCR** (occlusion veine centrale/branche de la rétine)\n"
                "- **DMLA** compliquée de néovaisseaux choroïdiens maculaires\n"
                "- **DR rhegmatogène** (décollement de rétine)\n"
                "- **NOIA** (neuropathie optique ischémique antérieure)\n"
                "- Toxoplasmose oculaire"
            )),
            FicheRow(concept="DR rhegmatogène", detail_md=(
                "- DR secondaire à une **déchirure rétinienne**\n"
                "- Étiologies principales :\n"
                "  - Idiopathique, ++ sujet âgé\n"
                "  - **Myopie forte** > -6 dioptries\n"
                "  - Chirurgie de la cataracte\n"
                "- Signes fonctionnels (séquence typique) :\n"
                "  - **Myodésopsies** → **phosphènes** → amputation du **champ visuel périphérique** → BAV"
            )),
            FicheRow(concept="◆ FO et traitement du DR", detail_md=(
                "- FO : rétine en relief, mobile, formant de volumineux plis\n"
                "- Recherche de la **déchirure causale**\n"
                "- Examen rétine périphérique oeil controlatéral : recherche déchirures non compliquées "
                "et lésions prédisposantes (**dégénérescence palissadique**)\n"
                "  - Traitement préventif par **photocoagulation au laser** (risque bilatéralisation > **10%**)\n"
                "- Évolution spontanée : très péjorative avec extension et **cécité en quelques semaines**\n"
                "- Traitement : **chirurgical en semi-urgence** (obturation déchirure rétinienne)\n"
                "- Pronostic d'autant meilleur que la prise en charge est **précoce**"
            )),
            FicheRow(concept="", detail_md=(
                "- Le DR rhegmatogène est une **urgence chirurgicale** : cécité en quelques semaines sans traitement\n"
                "- Toujours examiner l'oeil controlatéral à la recherche de lésions prédisposantes"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="BAV avec oeil blanc et indolore — FO visible et normal", rows=[
            FicheRow(concept="NORB", detail_md=(
                "- **Neuropathie optique rétrobulbaire**\n"
                "- FO normal (atteinte en arrière de la papille)\n"
                "- Évoque une **sclérose en plaques**"
            )),
            FicheRow(concept="Atteinte des voies optiques", detail_md=(
                "- Atteinte chiasmatique : **hémianopsie bitemporale**\n"
                "- Atteinte rétrochiasmatique : hémianopsie latérale homonyme"
            )),
        ]),
        SousPartie(lettre="E", titre="Anomalies transitoires de la vision", rows=[
            FicheRow(concept="Amaurose fugace (CMT)", detail_md=(
                "- Disparition **totale** de la vision d'apparition aiguë, durant quelques minutes, "
                "spontanément résolutive\n"
                "- Correspond à un **accident ischémique rétinien transitoire**\n"
                "- **Urgence diagnostique** : risque de survenue d'une OACR constituée ou d'un **AVC ischémique**\n"
                "- Doit faire rechercher : **athérome carotidien** et **cardiopathie emboligène**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ L'amaurose fugace est un **équivalent d'AIT rétinien** : bilan vasculaire urgent obligatoire\n"
                "- Ne pas banaliser une cécité transitoire monoculaire"
            ), kind="piege"),
            FicheRow(concept="Autres anomalies transitoires", detail_md=(
                "| Anomalie | Caractéristiques | Étiologie |\n"
                "|----------|-----------------|----------|\n"
                "| Insuffisance vertébro-basilaire | Amaurose transitoire **bilatérale**, brève | Ischémie territoire vertébro-basilaire |\n"
                "| Éclipses visuelles | Flou visuel aux changements de position, quelques secondes | **Oedème papillaire** de l'HTIC |\n"
                "| Scotome scintillant | Bilatéral, flashs colorés, extension à un hémichamp | **Migraine ophtalmique** |\n"
            )),
            FicheRow(concept="◆ Scotome scintillant", detail_md=(
                "- S'étend progressivement à un hémichamp visuel\n"
                "- Régresse en **15-20 minutes** laissant place à une **céphalée pulsatile** "
                "hémicranienne et controlatérale\n"
                "- Peut être isolé, sans céphalée"
            )),
        ]),
    ])

    # ── PARTIE II : BAV PROGRESSIVE ET CHAMP VISUEL ──
    partie_ii = Partie(numero="II", titre="BAV progressive et altérations du champ visuel", sous_parties=[
        SousPartie(lettre="A", titre="Cataracte et glaucome chronique", rows=[
            FicheRow(concept="Cataracte", detail_md=(
                "- Opacification du **cristallin**\n"
                "- Cause la plus fréquente de BAV progressive\n"
                "- 1re cause de cécité dans le monde"
            )),
            FicheRow(concept="Glaucome chronique à angle ouvert", detail_md=(
                "- BAV progressive par atteinte du **nerf optique**\n"
                "- Associé à une **hypertonie oculaire** (> 22 mmHg)\n"
                "- Altération progressive du **champ visuel**\n"
                "- Diagnostic et suivi par **OCT** et périmétrie statique"
            )),
        ]),
        SousPartie(lettre="B", titre="Affections rétiniennes", rows=[
            FicheRow(concept="◆ Dégénérescences héréditaires", detail_md=(
                "| Type | Atteinte | Présentation | FO |\n"
                "|------|----------|-------------|----|\n"
                "| Hérédo-dégénérescence centrale (Stargardt) | **Cônes** | BAV progressive très sévère dès l'enfance (AR) | Macula en « **oeil de boeuf** » |\n"
                "| Rétinopathie pigmentaire | **Bâtonnets** | **Héméralopie** + rétrécissement progressif du CV dès l'enfance | Image en **ostéoblaste** |\n"
            )),
            FicheRow(concept="Rétinopathie diabétique", detail_md=(
                "- Complication microvasculaire du diabète\n"
                "- BAV progressive, souvent longtemps **asymptomatique**\n"
                "- Surveillance ophtalmologique **annuelle** obligatoire chez tout diabétique"
            )),
            FicheRow(concept="Membrane prémaculaire et trou maculaire", detail_md=(
                "- **Membrane prémaculaire** :\n"
                "  - Membrane fibreuse face interne de la rétine maculaire\n"
                "  - Fréquent chez le sujet âgé\n"
                "  - BAV et **métamorphopsies** d'installation lente\n"
                "  - Traitement : ablation chirurgicale par **vitrectomie**\n"
                "- **Trou maculaire** :\n"
                "  - Trou fovéolaire de formation brutale\n"
                "  - BAV brutale + scotome + métamorphopsies\n"
                "  - Traitement chirurgical pour obturer le trou fovéolaire"
            )),
            FicheRow(concept="DMLA", detail_md=(
                "- **Dégénérescence maculaire liée à l'âge**\n"
                "- Cause majeure de BAV progressive chez le sujet âgé\n"
                "- Formes atrophique (sèche) et exsudative (néovaisseaux)"
            )),
            FicheRow(concept="Oedèmes maculaires", detail_md=(
                "- Étiologies :\n"
                "  - Rétinopathie diabétique\n"
                "  - OVCR/OBVCR\n"
                "  - Chirurgie de la cataracte\n"
                "  - Uvéites postérieures"
            )),
            FicheRow(concept="⚠ Maculopathie toxique aux APS", detail_md=(
                "- Survient à partir d'une posologie cumulée de **250 g**\n"
                "- Deux phases :\n"
                "  - **Périfovéolopathie** (asymptomatique) : scotome annulaire, dyschromatopsie axe bleu-jaune, "
                "altération EOG → arrêt du traitement **stoppe** l'évolution\n"
                "  - **Maculopathie englobant fovéola** : BAV progressive **irréversible** malgré arrêt des APS, "
                "FO en « oeil de boeuf »\n"
                "- Surveillance systématique tous les **6-18 mois** : AV, périmétrie statique, vision chromatique, EOG, FO"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La maculopathie aux APS est **irréversible** une fois la fovéola atteinte\n"
                "- La surveillance ophtalmologique régulière est **obligatoire** sous APS"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Altérations du champ visuel", rows=[
            FicheRow(concept="Atteintes rétiniennes", detail_md=(
                "- Atteinte rétine centrale (respect périphérie) : **scotome**\n"
                "- Atteintes rétiniennes périphériques : **déficits périphériques**"
            )),
            FicheRow(concept="Atteinte du nerf optique", detail_md=(
                "| Type d'atteinte | Conséquence |\n"
                "|-----------------|------------|\n"
                "| Atteinte totale du nerf optique | **Cécité unilatérale** |\n"
                "| Atteinte fibres maculaires | **Scotome central/caeco-central** |\n"
                "| Atteinte faisceau de fibres papillaires | **Déficit fasciculaire** |\n"
            )),
            FicheRow(concept="◆ Neuropathies optiques", detail_md=(
                "- **NORB** (neuropathie optique rétrobulbaire)\n"
                "- **NOIA** (neuropathie optique ischémique antérieure)\n"
                "- Neuropathie optique **éthylique** (tabac ++ associé) : scotome caeco-central bilatéral, "
                "aboutit à une atrophie optique\n"
                "- Neuropathie optique **médicamenteuse** : antituberculeux (**éthambutol**, isoniazide), "
                "dyschromatopsie axe rouge-vert\n"
                "  - Surveillance : examen du CV et vision des couleurs\n"
                "- Neuropathies optiques tumorales : tumeurs intra-orbitaires (gliome, méningiome) "
                "→ atrophie optique + exophtalmie"
            )),
            FicheRow(concept="Lésions du chiasma optique", detail_md=(
                "- **Hémianopsie bitemporale**\n"
                "- Étiologies :\n"
                "  - **Adénomes hypophysaires**\n"
                "  - Méningiome du tubercule de la selle\n"
                "  - Anévrisme de la carotide interne\n"
                "  - Craniopharyngiome\n"
                "  - Gliome du chiasma (maladie de **Recklinghausen**)"
            )),
            FicheRow(concept="Lésions rétrochiasmatiques", detail_md=(
                "| Étiologie | Mode d'installation |\n"
                "|-----------|--------------------|\n"
                "| **Vasculaire** | HLH d'apparition **brutale** |\n"
                "| **Tumorale** | HLH d'apparition **progressive** |\n"
                "| **Traumatique** | HLH contemporaine du traumatisme |\n\n"
                "HLH = Hémianopsie/quadranopsie latérale homonyme"
            )),
            FicheRow(concept="◆ Cécité corticale", detail_md=(
                "- Atteinte des deux lobes occipitaux, ++ **AVC** territoire vertébro-basilaire\n"
                "- Caractérisée par :\n"
                "  - Cécité **bilatérale** brutale\n"
                "  - FO **normal**\n"
                "  - Conservation du **RPM**\n"
                "  - DTS, hallucinations, **anosognosie**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Cécité corticale : FO normal + RPM conservé malgré une cécité bilatérale\n"
                "- Ne pas confondre avec une atteinte oculaire"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE III : EXAMEN OPHTALMOLOGIQUE ──
    partie_iii = Partie(numero="III", titre="Examen ophtalmologique", sous_parties=[
        SousPartie(lettre="A", titre="Anatomie de l'oeil et annexes", rows=[
            FicheRow(concept="Globe oculaire — Contenant", detail_md=(
                "- **Membrane externe** : coque cornéo-sclérale\n"
                "  - Cornée : 5 couches (d'avant en arrière) → épithélium, membrane de Bowman, "
                "stroma cornéen, membrane de Descemet, endothélium cornéen\n"
                "- **Membrane intermédiaire** : uvée\n"
                "  - Choroïde : nutrition épithélium pigmentaire et couches externes de la rétine\n"
                "  - Corps ciliaires : procès ciliaires (sécrétion humeur aqueuse) + muscles ciliaires (accommodation)\n"
                "- **Membrane interne** : rétine\n"
                "  - Rétine neurosensorielle : photorécepteurs (**cônes** = vision détails/couleurs dans la macula ; "
                "**bâtonnets** = vision périphérique/nocturne en périphérie), cellules bipolaires, cellules ganglionnaires\n"
                "  - Épithélium pigmentaire : couche monostratifiée contre la face externe"
            )),
            FicheRow(concept="Globe oculaire — Contenu", detail_md=(
                "- Milieux transparents permettant le passage de la lumière :\n"
                "  - **Humeur aqueuse** : évacuée via trabéculum dans le **canal de Schlemm** "
                "au niveau de l'angle irido-cornéen\n"
                "  - **Cristallin** : amarré aux procès ciliaires par la zonule\n"
                "  - **Corps vitré** : gel transparent (4/5 du globe), entouré par membrane hyaloïde\n"
                "- Globe divisé en 2 régions :\n"
                "  - **Segment antérieur** : cornée, iris, chambre antérieure, angle irido-cornéen, cristallin, corps ciliaires\n"
                "  - **Segment postérieur** : sclère, choroïde, rétine, corps vitré"
            )),
            FicheRow(concept="◆ Nerfs oculomoteurs", detail_md=(
                "| Nerf | Muscles innervés | Remarques |\n"
                "|------|-----------------|----------|\n"
                "| **III** (oculomoteur commun) | Droits supérieur, inférieur, médial + oblique inférieur + releveur paupière | RPM et accommodation (atteinte RPM = III **intrinsèque**) |\n"
                "| **IV** (pathétique) | Oblique supérieur | |\n"
                "| **VI** (moteur oculaire externe) | Droit externe | |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Atteinte voie efférente sympathique → **syndrome de Claude Bernard-Horner** : "
                "myosis + ptosis + énophtalmie"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Interrogatoire et mesure de l'acuité visuelle", rows=[
            FicheRow(concept="Signes fonctionnels", detail_md=(
                "| Signe | Description |\n"
                "|-------|------------|\n"
                "| BAV | De près et/ou de loin |\n"
                "| Fatigue visuelle | Difficultés d'attention + céphalées sus-orbitaires en fin de journée |\n"
                "| **Myodésopsies** | Sensation de mouches volantes / corps flottants |\n"
                "| **Phosphènes** | Sensation d'éclairs lumineux |\n"
                "| **Métamorphopsies** | Déformations des lignes droites → ondulées |\n"
                "| **Héméralopie** | Gêne en vision crépusculaire |\n"
                "| Scotome | Tache sombre (partiel) ou noire (complet) + BAV |\n"
            )),
            FicheRow(concept="Douleurs oculaires", detail_md=(
                "- **Superficielles** : minimes (grains de sable) ou intenses (photophobie + blépharospasme)\n"
                "- **Profondes** : modérées à intenses"
            )),
            FicheRow(concept="Diplopie", detail_md=(
                "- **Monoculaire** : ne disparaît pas à l'occlusion de l'autre oeil (cause oculaire)\n"
                "- **Binoculaire** : disparaît à l'occlusion d'un oeil (cause neurologique)"
            )),
            FicheRow(concept="Mesure de l'acuité visuelle", detail_md=(
                "- AV = pouvoir de discrimination de l'oeil (plus petite distance entre 2 points)\n"
                "- Paramètre propre de la **macula** (avec vision des couleurs et vision des reliefs)\n"
                "- **De loin** : échelle de **Monoyer** à 5 m (1 à 10/10)\n"
                "- **De près** : échelle de **Parinaud** à 33 cm (P14 à P1,5 ; normale = P2)\n"
                "- AV toujours mesurée **sans puis avec correction**"
            )),
            FicheRow(concept="◆ Étude de la réfraction", detail_md=(
                "- Mauvaise AV due à :\n"
                "  - Atteinte oeil/voies optiques : AV **non améliorable**\n"
                "  - Anomalie de réfraction : AV **améliorable**\n"
                "- Moyens : réfractomètres automatiques, verres sphériques/cylindriques\n"
                "- Enfant : **skiascopie sous cycloplégie** (paralyser l'accommodation)"
            )),
        ]),
        SousPartie(lettre="C", titre="Examen du segment antérieur et mesure de la PIO", rows=[
            FicheRow(concept="Examen à la LAF", detail_md=(
                "- **Conjonctive** :\n"
                "  - Rougeur localisée/diffuse, associée à des sécrétions\n"
                "  - Cercle péri-kératique (rougeur prédominant autour du limbe scléro-cornéen)\n"
                "  - **Chémosis** : oedème conjonctival\n"
                "- **Cornée** :\n"
                "  - Diminution de transparence : diffuse (**oedème**) ou localisée (**ulcération**)\n"
                "  - Recherche d'ulcère : instillation de **fluorescéine** + lumière bleue → ulcère apparaît **vert**"
            )),
            FicheRow(concept="Chambre antérieure", detail_md=(
                "| Signe | Description |\n"
                "|-------|------------|\n"
                "| **Tyndall** | Cellules inflammatoires + protéines dans la chambre antérieure |\n"
                "| **Précipités rétro-cornéens** | Dépôts de cellules inflammatoires face postérieure de la cornée |\n"
                "| **Synéchies irido-cristalliniennes** | Adhérences inflammatoires iris-cristallin |\n"
                "| **Hypopion** | Pus dans la chambre antérieure |\n"
                "| **Hyphéma** | Sang dans la chambre antérieure |\n"
            )),
            FicheRow(concept="Mesure de la PIO", detail_md=(
                "- Méthodes : palpation bidigitale, tonomètre à aplanation sur LAF, "
                "tonomètre à air pulsé ++\n"
                "- **Normale** : **10-20 mmHg**\n"
                "- **Hypertonie oculaire** : > **22 mmHg**"
            )),
            FicheRow(concept="Gonioscopie", detail_md=(
                "- Examen de l'**angle irido-cornéen** par LAF avec verre de contact à miroir\n"
                "- Apprécie les éléments de l'angle irido-cornéen\n"
                "- Indispensable pour distinguer glaucome à angle **ouvert** vs **fermé**"
            )),
        ]),
        SousPartie(lettre="D", titre="Fond d'oeil et lésions élémentaires", rows=[
            FicheRow(concept="Méthodes d'examen du FO", detail_md=(
                "- **Ophtalmoscopie directe** : le plus aisé\n"
                "- **Ophtalmoscopie indirecte** : image inversée, lentille tenue à la main\n"
                "- **Biomicroscopie du FO**"
            )),
            FicheRow(concept="Lésions élémentaires du FO", detail_md=(
                "| Lésion | Description |\n"
                "|--------|------------|\n"
                "| **Microanévrismes** | Points rouges petite taille sur capillaires rétiniens (se remplissent de fluorescéine) |\n"
                "| Hémorragies intravitréennes | Masquent le FO |\n"
                "| Hémorragies prérétiniennes | Masquent les vaisseaux rétiniens |\n"
                "| Hémorragies intrarétiniennes | Punctiformes, en flammèche, ou profondes « en tache » |\n"
                "| **Nodules cotonneux** | Lésions blanches superficielles = occlusion artérioles précapillaires |\n"
                "| **Exsudats profonds** | Dépôts jaunâtres = accumulation de lipoprotéines dans la rétine |\n"
                "| **Oedème papillaire** | Papille hyperhémiée à bords flous |\n"
            )),
        ]),
        SousPartie(lettre="E", titre="Examens complémentaires", rows=[
            FicheRow(concept="Champ visuel", detail_md=(
                "- Champ visuel = portion de l'espace embrassée par l'oeil regardant droit devant lui\n"
                "- **Périmétrie cinétique** (Goldman) : point lumineux de la périphérie vers le centre → isoptères\n"
                "  - Adaptée aux **déficits périphériques** : hémianopsies, quadranopsies\n"
                "  - Tache aveugle physiologique = **tache de Mariotte** (papille)\n"
                "- **Périmétrie statique** (Humphrey/Octopus) : test lumineux fixe\n"
                "  - Adaptée au **CV central** : pathologie du nerf optique et **glaucome**"
            )),
            FicheRow(concept="Vision des couleurs", detail_md=(
                "- Anomalie congénitale : planches d'**Ishihara**\n"
                "- Affection acquise : test de **Farnsworth**"
            )),
            FicheRow(concept="Angiographie du FO", detail_md=(
                "- Clichés du FO après injection IV d'un colorant fluorescent :\n"
                "  - **Fluorescéine** : étude dynamique de la vascularisation rétinienne\n"
                "  - **Vert d'indocyanine** : visualisation des vaisseaux choroïdiens pathologiques\n"
                "- Préparation anti-allergique de **3 jours** si ATCD allergiques"
            )),
            FicheRow(concept="Explorations électrophysiologiques", detail_md=(
                "- **ERG** (électrorétinogramme)\n"
                "- **PEV** (potentiels évoqués visuels)\n"
                "- **EOG** (électro-oculogramme)"
            )),
            FicheRow(concept="Échographie et OCT", detail_md=(
                "- **Échographie mode A** : longueur du globe → déterminer puissance implant (chirurgie cataracte)\n"
                "- **Échographie mode B** :\n"
                "  - Dépister un DR lors d'un trouble des milieux ++\n"
                "  - Localiser un CEIO\n"
                "  - Diagnostic tumeur intraoculaire/orbitaire\n"
                "- **OCT** (tomographie en cohérence optique) :\n"
                "  - Coupes de la rétine de précision supérieure à l'échographie\n"
                "  - Applications : affections maculaires, dépistage et suivi du **glaucome chronique**"
            )),
        ]),
    ])

    # ── PARTIE IV : OEIL ROUGE ET/OU DOULOUREUX ──
    partie_iv = Partie(numero="IV", titre="Oeil rouge et/ou douloureux", sous_parties=[
        SousPartie(lettre="A", titre="Oeil rouge non douloureux sans BAV", rows=[
            FicheRow(concept="Hémorragie sous-conjonctivale", detail_md=(
                "- Rougeur conjonctivale **localisée, en nappe**\n"
                "- Fréquente, banale, unilatérale, indolore\n"
                "- Régresse spontanément en quelques semaines\n"
                "- Doit faire rechercher : **HTA** et **trouble de la coagulation**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Devant une hémorragie sous-conjonctivale : ne pas méconnaitre un **CEIO** (corps étranger intraoculaire)"
            ), kind="piege"),
            FicheRow(concept="Épisclérite", detail_md=(
                "- Inflammation sclérale **superficielle**\n"
                "- Rougeur en secteur, peu/pas douloureux\n"
                "- Vision conservée, segment antérieur normal\n"
                "- Rougeur disparaît après instillation de **néosynéphrine** (vasoconstricteur)\n"
                "- Bilan étiologique si récidivant (maladie de système)\n"
                "- Traitement : **corticothérapie locale**"
            )),
        ]),
        SousPartie(lettre="B", titre="Oeil rouge douloureux sans BAV — Conjonctivites", rows=[
            FicheRow(concept="Conjonctivite bactérienne", detail_md=(
                "- Clinique :\n"
                "  - Bilatérale ++ (+/- intervalle libre)\n"
                "  - Rougeur conjonctivale diffuse, prédominant cul-de-sac inférieur\n"
                "  - Douleurs superficielles modérées (grains de sable)\n"
                "  - Sécrétions **muco-purulentes** collant les paupières au réveil\n"
                "  - AV conservée\n"
                "- Étiologie : Gram + ++ (streptocoques, staphylocoques)\n"
                "- Traitement probabiliste sans prélèvement :\n"
                "  - Hygiène des mains\n"
                "  - Lavages fréquents au **sérum physiologique**\n"
                "  - Collyre ATB large spectre (**rifampicine/gentamycine**) 4-6/j\n"
                "  - +/- Pommade ATB le soir\n"
                "- Guérison sans séquelle"
            )),
            FicheRow(concept="Conjonctivite virale à Adénovirus", detail_md=(
                "- Très fréquente et **contagieuse** (épidémies)\n"
                "- Bilatérale en deux temps (auto-contamination)\n"
                "- Sécrétions **claires**\n"
                "- **ADP prétragienne** évocatrice\n"
                "- Traitement : lavages sérum physiologique + collyre antiseptique 3-4/j\n"
                "- Évolution favorable en **15 jours** mais risque de kérato-conjonctivite à Adénovirus"
            )),
            FicheRow(concept="Conjonctivite allergique", detail_md=(
                "- Terrain allergique/atopique, ++ saisonnière\n"
                "- Bilatérale et récidivante\n"
                "- Volumineuses papilles conjonctivales\n"
                "- **Prurit** évocateur, chémosis, sécrétions claires\n"
                "- Traitement :\n"
                "  - Éviction allergène, désensibilisation\n"
                "  - Lavages sérum physiologique\n"
                "  - Crise : collyre **antiH1**\n"
                "  - Fond : collyre **anti-dégranulant mastocytaire**"
            )),
            FicheRow(concept="◆ Conjonctivites à Chlamydia", detail_md=(
                "- **Conjonctivite à inclusions de l'adulte** : IST (+/- urétrite/vaginite), "
                "traitement par **azithromycine monodose**\n"
                "- **Trachome** (C. trachomatis) :\n"
                "  - Très fréquent dans les pays en développement\n"
                "  - Néovascularisation cornéenne, fibrose du tarse, entropion\n"
                "  - Complications cornéennes très sévères : **2e cause de cécité mondiale** (après cataracte)"
            )),
            FicheRow(concept="Conjonctivites néonatales", detail_md=(
                "- **Conjonctivite gonococcique** : disparue grâce à l'instillation systématique de collyre "
                "antiseptique à la naissance (très mauvais pronostic si survenue)\n"
                "- **Conjonctivite à Chlamydia** : secondaire à une infection maternelle génito-urinaire\n"
                "- **Imperforation du canal lacrymo-nasal** : conjonctivites à répétition du nouveau-né"
            )),
        ]),
        SousPartie(lettre="C", titre="Oeil rouge douloureux sans BAV — Syndrome sec et sclérite", rows=[
            FicheRow(concept="Syndrome sec oculaire", detail_md=(
                "- Lié à une insuffisance de la sécrétion lacrymale\n"
                "- Clinique : rougeur oculaire + douleurs superficielles (grains de sable)\n"
                "- Diagnostic positif :\n"
                "  - Quantitatif : test de **Schirmer**\n"
                "  - Qualitatif : **break-up time** (BUT)\n"
                "  - Surface conjonctivale : instillation de **vert de lissamine** (colore cellules mortes)\n"
                "- Étiologies :\n"
                "  - Involution sénile des glandes lacrymales\n"
                "  - **Syndrome de Gougerot-Sjögren**\n"
                "  - Traitements parasympathomimétiques par voie générale (ADT)\n"
                "- Traitement : substituts de larmes (+/- cyclosporine), éviction facteurs irritants, "
                "occlusion des points lacrymaux"
            )),
            FicheRow(concept="◆ Sclérite", detail_md=(
                "- Inflammation **localisée** de la sclère\n"
                "- Douleurs oculaires importantes augmentées à la **mobilisation du globe**\n"
                "- Rougeur en secteur qui **ne disparaît PAS** à l'instillation de néosynéphrine "
                "(contrairement à l'épisclérite)\n"
                "- Recherche de maladie de système : SPA, PR, LED, **Wegener**, **Behçet**, "
                "tuberculose, sarcoïdose\n"
                "- Traitement par **AINS voie générale**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Distinguer sclérite et épisclérite par le test à la **néosynéphrine** :\n"
                "  - Épisclérite : rougeur **disparaît** → bénin\n"
                "  - Sclérite : rougeur **persiste** → rechercher une maladie de système"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Oeil rouge douloureux avec BAV — Kératites", rows=[
            FicheRow(concept="Signes communs des kératites", detail_md=(
                "- BAV variable selon localisation par rapport à l'axe visuel\n"
                "- Douleurs oculaires superficielles **importantes**\n"
                "- Larmoiement, photophobie, blépharospasme\n"
                "- Examen : diminution de la transparence cornéenne, **cercle péri-kératique**\n"
                "- Instillation de **fluorescéine** + lumière bleue : ulcérations **vertes** → "
                "aspect oriente vers l'étiologie"
            )),
            FicheRow(concept="Kératite à Adénovirus", detail_md=(
                "- Kérato-conjonctivite épidémique, **contagieuse** ++\n"
                "- Peut compliquer une conjonctivite à Adénovirus\n"
                "- Petites ulcérations disséminées : **KPS fluo +**\n"
                "- Évolution toujours favorable mais infiltrats sous-épithéliaux possibles "
                "(BAV longue à récupérer)\n"
                "- Traitement : idem conjonctivite à Adénovirus"
            )),
            FicheRow(concept="Kératite herpétique", detail_md=(
                "- Ulcération **dendritique** ++ ou « en carte de géographie »\n"
                "- Traitement :\n"
                "  - **Antiviraux** par voie générale +/- locaux (collyres ou pommades)\n"
                "  - Durée : 1-2 semaines\n"
                "- Évolution ++ favorable sous traitement\n"
                "- Complications : récidives, kératite profonde (BAV définitive)"
            )),
            FicheRow(concept="", detail_md=(
                "- **CI ABSOLUE** : corticoïdes locaux dans la kératite herpétique "
                "(risque de **perforation cornéenne**)"
            ), kind="a_retenir"),
            FicheRow(concept="Kératites zostériennes", detail_md=(
                "- Kératite superficielle bénigne : contemporaine de l'épisode aigu (atteinte virale directe)\n"
                "- Kératite neuro-paralytique **grave** : secondaire, dystrophique par **anesthésie cornéenne**\n"
                "- Traitement : **valaciclovir** dans les 3 premiers jours + protecteurs cornéens locaux"
            )),
            FicheRow(concept="Kératites bactériennes et amibiennes", detail_md=(
                "- Surinfection bactérienne d'une ulcération traumatique ou sous **lentille de contact**\n"
                "- Examen : plages blanches d'infiltration cornéenne +/- **hypopion**\n"
                "- Prélèvement abcès pour examen direct, culture et ATBG\n"
                "- Traitement :\n"
                "  - Formes peu sévères : collyres ATB plusieurs fois/j\n"
                "  - Abcès importants : hospitalisation + **collyres fortifiés 1/heure**\n"
                "- Complications : endophtalmie, perforation cornéenne, taie cornéenne cicatricielle\n"
                "- Suspicion kératite amibienne si : tableau atypique, survenue sous lentilles, "
                "résistance au traitement → prélèvements en milieu hospitalier"
            )),
            FicheRow(concept="Kérato-conjonctivite sèche", detail_md=(
                "- Kératite par **inocclusion palpébrale**\n"
                "- ++ Paralysies faciales, exophtalmie\n"
                "- Prévention : protecteurs cornéens +/- **tarsorraphie**"
            )),
        ]),
        SousPartie(lettre="E", titre="Glaucome aigu par fermeture de l'angle", rows=[
            FicheRow(concept="Terrain et circonstances", detail_md=(
                "- Terrain prédisposant :\n"
                "  - Sujets **hypermétropes**\n"
                "  - Chambre antérieure et angle irido-cornéen **étroits**\n"
                "  - Augmentation du volume du cristallin (cataracte, vieillissement)\n"
                "- Circonstances de survenue (mydriase + blocage pupillaire) :\n"
                "  - Passage à l'obscurité\n"
                "  - Anesthésie générale, stress\n"
                "  - Collyres mydriatiques\n"
                "  - Médicaments **parasympatholithiques** (ADT) / **sympathomimétiques** (neuroleptiques)"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- Douleurs très profondes irradiant vers le **territoire du trijumeau**\n"
                "- Nausées/vomissements\n"
                "- **BAV brutale et massive**\n"
                "- Examen :\n"
                "  - Oeil rouge, cercle péri-kératique\n"
                "  - Oedème cornéen **diffus** (buée épithéliale)\n"
                "  - **Semi-mydriase aréflective** (ischémie sphincter irien)\n"
                "  - Chambre antérieure **étroite**, angle irido-cornéen **fermé**\n"
                "  - TO > **50 mmHg** (souvent > 80 mmHg)\n"
                "  - Oeil sain : chambre antérieure et angle **étroits**"
            )),
            FicheRow(concept="", detail_md=(
                "- Le patient peut décrire des épisodes transitoires antérieurs "
                "(fermetures incomplètes spontanément résolutives)\n"
                "- Évolution sans traitement : **cécité en quelques jours** (atrophie optique)"
            ), kind="piege"),
            FicheRow(concept="Traitement du GAFA", detail_md=(
                "- **Hospitalisation en urgence** en ophtalmologie, pose VVP\n"
                "- Arrêt du médicament favorisant\n"
                "- **Acétazolamide IV** + supplémentation potassique\n"
                "- **Mannitol 20% IV** (soluté hyperosmolaire)\n"
                "- Collyres hypotonisants\n"
                "- Collyre **pilocarpine** (parasympathomimétique myotique) 1/heure oeil touché ET oeil sain\n"
                "- Surveillance : ionogramme, glycémie, urée, créatinine, BHC, ECG\n"
                "- Dès crise jugulée (TO normal) : **iridotomie périphérique au laser Yag** des **deux yeux**\n"
                "  - Si échec : iridectomie chirurgicale\n"
                "- Après iridotomie/iridectomie : plus de CI médicamenteuses"
            )),
            FicheRow(concept="", detail_md=(
                "- Le GAFA est une **urgence ophtalmologique absolue** : cécité irréversible sans traitement\n"
                "- L'iridotomie au laser doit être réalisée sur les **deux yeux** (prophylaxie de l'oeil sain)"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Glaucome néovasculaire (GNV)", detail_md=(
                "- Tableau clinique similaire au GAFA + **néovascularisation irienne** et de l'angle\n"
                "- Étiologies : RD compliquée, OVCR ischémique, drépanocytose\n"
                "- Traitement : identique au GAFA + photocoagulation des territoires ischémiques rétiniens\n"
                "- Pronostic **très sévère**"
            )),
        ]),
    ])

    # ── PARTIE V : PATHOLOGIES DES PAUPIÈRES ──
    partie_v = Partie(numero="V", titre="Pathologies des paupières", sous_parties=[
        SousPartie(lettre="A", titre="Orgelet et chalazion", rows=[
            FicheRow(concept="Orgelet", detail_md=(
                "- Furoncle du bord libre de la paupière centré sur le follicule pilo-sébacé d'un cil\n"
                "- Infection bactérienne ++ à **S. aureus**\n"
                "- Se développe en quelques jours\n"
                "- Clinique : douleur vive, tuméfaction rouge centrée par un **point blanc** au bord libre\n"
                "- Traitement :\n"
                "  - Ablation du cil\n"
                "  - Collyre/pommade ATB 8 jours\n"
                "  - Si échec/forme enkystée : incision au bord libre sous AL"
            )),
            FicheRow(concept="Chalazion", detail_md=(
                "- **Granulome inflammatoire** développé sur une glande de Meibomius engorgée au sein du tarse\n"
                "- Tuméfaction douloureuse de la paupière **sans communication avec le bord libre**\n"
                "- Sécrétions purement sébacées, peut durer plusieurs semaines\n"
                "- Traitement :\n"
                "  - Pommade corticoïde locale (**Sterdex**)\n"
                "  - Soins de paupière : humidification eau chaude + massage du rebord orbitaire vers le bord libre\n"
                "  - Si échec/enkystement : incision de la glande de Meibomius par voie **conjonctivale** "
                "sous AL (sans suture) + collyre antiseptique 8 jours"
            )),
            FicheRow(concept="", detail_md=(
                "| | Orgelet | Chalazion |\n"
                "|--|---------|----------|\n"
                "| Structure atteinte | Follicule pilo-sébacé du **cil** | Glande de **Meibomius** (tarse) |\n"
                "| Localisation | **Bord libre** de la paupière | Paupière, **sans** communication bord libre |\n"
                "| Germe | S. aureus | Non infectieux (granulome) |\n"
                "| Traitement 1re intention | ATB local | **Corticoïde** local + soins paupière |\n"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Malformations palpébrales", rows=[
            FicheRow(concept="Entropion et ectropion", detail_md=(
                "| | Entropion | Ectropion |\n"
                "|--|----------|----------|\n"
                "| Définition | Bascule paupière **vers la conjonctive** | Bascule paupière **vers l'extérieur** |\n"
                "| Étiologies | Sénile, cicatriciel (SJS) | Sénile, cicatriciel, **paralytique** (PF) |\n"
                "| Conséquences | Oeil rouge/douloureux chronique, trichiasis | Exposition cornéenne, larmoiement |\n"
            )),
            FicheRow(concept="Ptosis", detail_md=(
                "- Position trop basse du bord libre de la paupière supérieure\n"
                "- Étiologies :\n"
                "  - **Neurogène** :\n"
                "    - Paralysie sympathique cervicale : **syndrome de CBH** (myosis + ptosis + énophtalmie)\n"
                "    - Paralysie du III (anévrisme intracrânien / dissection carotidienne)\n"
                "  - **Myogène** : myasthénie, ptosis congénital\n"
                "  - Sénile\n"
                "  - Traumatique (rupture de l'aponévrose du releveur)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Un ptosis d'apparition récente doit faire rechercher en priorité une cause **neurogène** :\n"
                "  - Paralysie du III (anévrisme) ou syndrome de CBH (dissection carotidienne)"
            ), kind="piege"),
            FicheRow(concept="Lagophtalmie", detail_md=(
                "- **Inocclusion palpébrale**\n"
                "- Entraîne une kératite d'exposition\n"
                "- Étiologies : anesthésie générale, coma prolongé, **paralysie faciale**"
            )),
        ]),
        SousPartie(lettre="C", titre="Tumeurs et traumatismes palpébraux", rows=[
            FicheRow(concept="Tumeurs palpébrales", detail_md=(
                "- ++ Sujet âgé\n"
                "- **Tumeurs bénignes** (traitement chirurgical conservateur) :\n"
                "  - Papillome\n"
                "  - Hydrocystome (kyste lacrymal)\n"
                "  - **Xanthélasma**\n"
                "- **Tumeurs malignes** :\n"
                "  - Tumeurs épithéliales : **CBC**, CE\n"
                "  - Mélanome malin\n"
                "  - Autres : carcinomes sébacés, lymphomes du MALT"
            )),
            FicheRow(concept="Traumatismes palpébraux", detail_md=(
                "- ++ Enfants\n"
                "- Lors de la prise en charge, rechercher systématiquement :\n"
                "  - Atteinte du **septum orbitaire** → si oui : exploration radiologique et/ou chirurgicale\n"
                "  - **Globe oculaire intact**\n"
                "  - **Canalicules lacrymaux arrachés** → si oui : réparation sous AG en **urgence**\n"
                "  - Atteinte du **muscle releveur** de la paupière supérieure"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Orientation diagnostique — BAV brutale", markdown=(
            "| Aspect de l'oeil | FO | Étiologies principales |\n"
            "|------------------|-----|----------------------|\n"
            "| Rouge + douloureux | Non nécessaire | Kératite, GAFA, uvéite antérieure |\n"
            "| Blanc + indolore | Non/mal visible | Hémorragie intravitréenne, hyalite |\n"
            "| Blanc + indolore | Visible et anormal | OACR, OVCR, DMLA, DR, NOIA |\n"
            "| Blanc + indolore | Visible et normal | NORB, atteinte chiasmatique/rétrochiasmatique |\n"
        )),
        TableauSynthese(titre="Conjonctivites — Comparaison", markdown=(
            "| Type | Sécrétions | Signes associés | Traitement |\n"
            "|------|-----------|-----------------|------------|\n"
            "| Bactérienne | **Muco-purulentes** | Paupières collées au réveil | Collyre ATB large spectre |\n"
            "| Virale (Adénovirus) | **Claires** | ADP prétragienne, contagieux | Collyre antiseptique |\n"
            "| Allergique | **Claires** | Prurit, papilles, chémosis | AntiH1 + anti-dégranulant |\n"
            "| Chlamydia (inclusion) | Variables | IST associée | Azithromycine monodose |\n"
        )),
        TableauSynthese(titre="Kératites — Étiologies et particularités", markdown=(
            "| Étiologie | Aspect cornéen | Particularité | Traitement |\n"
            "|-----------|---------------|---------------|------------|\n"
            "| Herpès | Ulcération **dendritique** | CI ABSOLUE corticoïdes locaux | Antiviraux 1-2 sem |\n"
            "| Adénovirus | KPS disséminées | Contagieux, infiltrats résiduels | Antiseptique |\n"
            "| Zona | Superficielle/neuro-paralytique | Anesthésie cornéenne | Valaciclovir J1-J3 |\n"
            "| Bactérienne | Infiltrats blancs +/- hypopion | Lentilles de contact ++ | ATB fortifiés si sévère |\n"
            "| Amibienne | Atypique, résistant | Lentilles ++ | Milieu hospitalier |\n"
        )),
        TableauSynthese(titre="Oeil rouge — Arbre diagnostique", markdown=(
            "| BAV | Douleur | Étiologies |\n"
            "|-----|---------|------------|\n"
            "| Non | Non | Hémorragie sous-conjonctivale, épisclérite |\n"
            "| Non | Oui | Conjonctivites, syndrome sec, sclérite |\n"
            "| Oui | Oui | Kératite, uvéite antérieure, GAFA |\n"
        )),
        TableauSynthese(titre="Anomalies du champ visuel selon la topographie lésionnelle", markdown=(
            "| Siège de la lésion | Type d'atteinte |\n"
            "|-------------------|----------------|\n"
            "| Rétine centrale | Scotome |\n"
            "| Rétine périphérique | Déficits périphériques |\n"
            "| Nerf optique (total) | Cécité unilatérale |\n"
            "| Nerf optique (fibres maculaires) | Scotome central/caeco-central |\n"
            "| Chiasma | Hémianopsie **bitemporale** |\n"
            "| Rétrochiasmatique | HLH (hémianopsie latérale homonyme) |\n"
            "| Cortex occipital bilatéral | Cécité corticale (FO normal, RPM conservé) |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| PIO normale | **10-20 mmHg** | Tonomètre |\n"
        "| Hypertonie oculaire | > **22 mmHg** | Seuil diagnostique |\n"
        "| TO dans le GAFA | > **50 mmHg** (souvent > 80) | Urgence ophtalmologique |\n"
        "| Myopie forte et DR | > **-6 dioptries** | FDR de DR rhegmatogène |\n"
        "| Bilatéralisation DR | > **10%** | Justifie laser préventif |\n"
        "| AV normale de près | **P2** | Échelle de Parinaud |\n"
        "| AV normale de loin | **10/10** | Échelle de Monoyer |\n"
        "| Toxicité APS (dose cumul.) | **250 g** | Maculopathie aux APS |\n"
        "| Surveillance APS | 1/**6-18 mois** | Examen ophtalmo |\n"
        "| Scotome scintillant | Régresse en **15-20 min** | Migraine ophtalmique |\n"
        "| Préparation anti-allergique | **3 jours** | Avant angiographie FO |\n"
        "| PNO iatrogène ponction | **3%** | Contrôle post-ponction |\n"
    ))

    points_cles = [
        "BAV brutale + oeil rouge + douleur = kératite, GAFA ou uvéite antérieure en urgence",
        "Le DR rhegmatogène est une urgence chirurgicale : cécité en quelques semaines sans traitement",
        "L'amaurose fugace est un AIT rétinien : bilan vasculaire urgent (athérome carotidien, cardiopathie emboligène)",
        "CI ABSOLUE des corticoïdes locaux dans la kératite herpétique (risque de perforation cornéenne)",
        "Le GAFA est une urgence : iridotomie au laser Yag des DEUX yeux une fois la crise jugulée",
        "PIO normale = 10-20 mmHg ; hypertonie > 22 mmHg ; GAFA > 50 mmHg",
        "Distinguer sclérite (néosynéphrine : rougeur persiste) et épisclérite (rougeur disparaît)",
        "Un ptosis récent impose la recherche d'une cause neurogène (III, CBH)",
        "La maculopathie aux APS est irréversible une fois la fovéola atteinte : surveillance obligatoire sous APS",
        "Cécité corticale : cécité bilatérale + FO normal + RPM conservé (atteinte occipitale bilatérale)",
    ]

    fiche_eclair_md = (
        "**BAV brutale** : oeil rouge/douloureux → kératite, GAFA, uvéite antérieure. "
        "Oeil blanc/indolore FO anormal → OACR, OVCR, DR, DMLA, NOIA. "
        "FO normal → NORB. Amaurose fugace = AIT rétinien → bilan vasculaire urgent.\n\n"
        "**BAV progressive** : cataracte (1re cause), GCAO, RD, DMLA, maculopathie APS "
        "(irréversible si fovéola atteinte, surveiller tous les 6-18 mois). "
        "DR rhegmatogène : myodésopsies → phosphènes → amputation CV → chirurgie semi-urgente.\n\n"
        "**Champ visuel** : nerf optique = scotome/cécité unilatérale. Chiasma = HBT. "
        "Rétrochiasmatique = HLH. Cécité corticale = FO normal + RPM conservé.\n\n"
        "**Examen ophtalmo** : AV Monoyer (loin) + Parinaud (près). PIO 10-20 mmHg. "
        "Fluorescéine + lumière bleue = ulcère vert. Tyndall/hypopion/hyphéma = inflammation CA. "
        "OCT = coupes rétiniennes de précision.\n\n"
        "**Oeil rouge** : sans BAV/douleur = hémorragie sous-conjonctivale, épisclérite. "
        "Douloureux sans BAV = conjonctivites (bactérienne = muco-purulent, virale = ADP prétragienne, "
        "allergique = prurit), syndrome sec (Schirmer, BUT), sclérite (néosynéphrine ne marche pas).\n\n"
        "**Kératites** : herpétique = dendritique, CI corticoïdes locaux. "
        "Bactérienne/amibienne = lentilles, collyres fortifiés si sévère. "
        "GAFA : hypermétrope, TO > 50, semi-mydriase → acétazolamide + mannitol + pilocarpine → "
        "iridotomie laser 2 yeux.\n\n"
        "**Paupières** : orgelet = S. aureus (bord libre), ATB. "
        "Chalazion = Meibomius (tarse), corticoïde local. "
        "Ptosis neurogène = III ou CBH (urgence). "
        "Traumatisme = vérifier globe, canalicules lacrymaux, septum."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Ophtalmologie",
        annee="2025-2026",
        item="Items 79, 80, 81, 84",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v],
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        usage=UsageStats(),
    )


def _make_analyzed_image(path: Path, desc: str, concept: str,
                         section: str, fig_num: int,
                         img_type: str = "schema") -> AnalyzedImage:
    """Crée un AnalyzedImage à partir d'un fichier image source."""
    from PIL import Image as PILImage
    data = path.read_bytes()
    pil = PILImage.open(path)
    w, h = pil.size
    source = ExtractedImage(
        data=data, ext="png", page=0, index=fig_num,
        width=w, height=h, sha="",
    )
    return AnalyzedImage(
        source=source, description=desc, concept_lie=concept,
        pertinence=9, type=img_type, section_suggeree=section,
        saved_path=path, figure_number=fig_num,
    )


_SOURCE_IMAGES: list[dict] = []


def _place_source_images(fiche: FicheData, figures_dir: Path) -> None:
    """Place les images sélectionnées du cours source dans les sous-parties."""
    all_images: list[AnalyzedImage] = []
    for i, entry in enumerate(_SOURCE_IMAGES):
        path = figures_dir / entry["file"]
        if not path.exists():
            print(f"  [SKIP] {entry['file']} not found")
            continue
        img = _make_analyzed_image(
            path, entry["desc"], entry["concept"],
            entry["desc"], fig_num=i + 1, img_type=entry.get("type", "schema"),
        )
        all_images.append(img)
        pi, si = entry["partie"], entry["sp"]
        if pi < len(fiche.parties) and si < len(fiche.parties[pi].sous_parties):
            fiche.parties[pi].sous_parties[si].images.append(img)
    fiche.images = all_images


def main():
    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(exist_ok=True)
    figures_dir = output_dir / "figures"
    figures_dir.mkdir(exist_ok=True)

    fiche = build_ophtalmologie_fiche()

    print("Placing source images from course PDF...")
    _place_source_images(fiche, figures_dir)
    print(f"  {len(fiche.images)} source images placed")

    docx_path = output_dir / "Medecine_generale_ophtalmologie_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Medecine_generale_ophtalmologie_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path}")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

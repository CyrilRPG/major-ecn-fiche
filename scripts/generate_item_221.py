"""Génère la fiche de l'Item 221 - Athérome : épidémiologie et physiopathologie (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Épidémiologie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Mortalité cardiovasculaire"),
            PlanSousPartie(lettre="B", titre="Incidence et prévalence"),
            PlanSousPartie(lettre="C", titre="Perspectives évolutives"),
        ]),
        PlanPartie(numero="II", titre="Mécanismes de l'athérosclérose", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition et formation de la plaque"),
            PlanSousPartie(lettre="B", titre="Évolution des plaques et des sténoses"),
            PlanSousPartie(lettre="C", titre="Anévrismes"),
        ]),
        PlanPartie(numero="III", titre="Points d'impact des thérapeutiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Prévention de l'athérome"),
            PlanSousPartie(lettre="B", titre="Prise en charge des complications"),
        ]),
        PlanPartie(numero="IV", titre="Localisations préférentielles", sous_parties=[
            PlanSousPartie(lettre="A", titre="Topographie des plaques"),
            PlanSousPartie(lettre="B", titre="Territoires principaux"),
        ]),
        PlanPartie(numero="V", titre="Évolution naturelle et FDR", sous_parties=[
            PlanSousPartie(lettre="A", titre="Évolution et complications"),
            PlanSousPartie(lettre="B", titre="Facteurs de risque d'athérome"),
        ]),
        PlanPartie(numero="VI", titre="Le malade polyathéromateux", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition et prévalence"),
            PlanSousPartie(lettre="B", titre="Bilan d'extension"),
            PlanSousPartie(lettre="C", titre="Thérapeutiques communes"),
            PlanSousPartie(lettre="D", titre="Prise en charge spécifique et suivi"),
        ]),
    ]

    # ── PARTIE I : ÉPIDÉMIOLOGIE ──
    partie_i = Partie(numero="I", titre="Épidémiologie", sous_parties=[
        SousPartie(lettre="A", titre="Mortalité cardiovasculaire", rows=[
            FicheRow(concept="◆ Données générales", detail_md=(
                "- Maladies **cardiovasculaires (CV)** = **1re cause de mortalité mondiale**\n"
                "- En France, mortalité CV passée à la 2e place derrière les cancers "
                "(baisse importante depuis 30 ans)\n"
                "- Reste la **1re cause de mortalité chez les femmes**"
            )),
            FicheRow(concept="Variations géographiques", detail_md=(
                "- Mortalité CV plus élevée dans le nord et l'est de l'Europe\n"
                "- Intermédiaire en Amérique du Nord\n"
                "- Plus faible en Europe du Sud et au Japon\n"
                "- France classée pays à faible niveau de risque CV selon l'**ESC** "
                "(Société européenne de cardiologie)"
            )),
            FicheRow(concept="Transition épidémiologique", detail_md=(
                "- Augmentation de la prévalence et de l'incidence des maladies athéromateuses "
                "dans les pays en voie de développement\n"
                "- Liée à la diversité des facteurs environnementaux et habitudes alimentaires "
                "plutôt qu'aux différences génétiques\n"
                "  - Ex : augmentation du risque CV chez les descendants de migrants asiatiques aux États-Unis"
            )),
        ]),
        SousPartie(lettre="B", titre="Incidence et prévalence", rows=[
            FicheRow(concept="◆ Incidence", detail_md=(
                "- Incidence **3 à 5 fois plus fréquente** chez l'homme que chez la femme\n"
                "- Augmentation des syndromes coronariens aigus chez les femmes jeunes "
                "(augmentation du tabagisme)\n"
                "- La différence d'incidence entre sexes diminue avec l'âge"
            )),
            FicheRow(concept="Prévalence", detail_md=(
                "- Augmente avec l'âge de la population"
            )),
        ]),
        SousPartie(lettre="C", titre="Perspectives évolutives", rows=[
            FicheRow(concept="Tendances actuelles", detail_md=(
                "- Baisse de la mortalité CV (progrès dans la prise en charge et la prévention)\n"
                "- Augmentation de la prévalence des maladies CV "
                "(vieillissement des populations, réduction de la mortalité)"
            )),
            FicheRow(concept="Perspectives mondiales", detail_md=(
                "- Fort accroissement de l'incidence des maladies CV attendu, lié à :\n"
                "  - Habitudes alimentaires\n"
                "  - Sédentarité\n"
                "  - Obésité\n"
                "  - Diabète"
            )),
            FicheRow(concept="", detail_md=(
                "- En France : tendance à la baisse de la mortalité CV mais hausse de la prévalence "
                "(vieillissement) et de l'incidence chez les **femmes jeunes** (tabac)"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE II : MÉCANISMES DE L'ATHÉROSCLÉROSE ──
    partie_ii = Partie(numero="II", titre="Mécanismes de l'athérosclérose", sous_parties=[
        SousPartie(lettre="A", titre="Définition et formation de la plaque", rows=[
            FicheRow(concept="◆ Définition de l'athérome", detail_md=(
                "- Remaniements de l'**intima** des artères de gros et moyen calibre\n"
                "- Accumulation focale de :\n"
                "  - Lipides\n"
                "  - Glucides complexes\n"
                "  - Sang et produits sanguins\n"
                "  - Tissu fibreux\n"
                "  - Dépôts calcaires\n"
                "- Accompagnée de modifications de la média"
            )),
            FicheRow(concept="◆ Étapes de formation de la plaque", detail_md=(
                "- Accumulation des **LDL** (low density lipoproteins) dans l'intima\n"
                "- Oxydation des LDL par les radicaux libres\n"
                "- Expression de molécules d'adhérence → attraction et transfert des monocytes "
                "dans la paroi → transformation en macrophages puis **cellules spumeuses**\n"
                "- Rôle des récepteurs scavengers (éboueurs) pour capter les LDL oxydées\n"
                "- **Dysfonction endothéliale** (favorisée par tabagisme et LDL oxydées) : "
                "diminution des capacités vasodilatatrices et antithrombotiques\n"
                "- Réaction inflammatoire auto-entretenue : sécrétion de métalloprotéases "
                "destructrices de la matrice extracellulaire\n"
                "- Migration des cellules musculaires lisses de la média vers la néo-intima\n"
                "- Sécrétion de facteurs de croissance, de collagène et de matrice extracellulaire\n"
                "- **Centre lipidique** : organisation des cellules spumeuses (stries lipidiques) "
                "dans un tissu inflammatoire\n"
                "- **Chape fibreuse** tardive recouvrant le centre lipidique"
            )),
            FicheRow(concept="Séquence chronologique", detail_md=(
                "- Stries lipidiques : retrouvées dès le jeune âge (autopsies)\n"
                "- Constitution progressive d'une véritable plaque d'athérome avec :\n"
                "  - Centre lipidique\n"
                "  - Chape fibreuse de couverture"
            )),
            FicheRow(concept="", detail_md=(
                "- **Plaque stable** : centre lipidique + cellules spumeuses, musculaires et "
                "inflammatoires + chape fibreuse de couverture\n"
                "- **Plaque instable** : très lipidique et inflammatoire, vulnérable à la rupture"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Évolution des plaques et des sténoses", rows=[
            FicheRow(concept="◆ Rupture de plaque", detail_md=(
                "- Complication brutale → accidents cliniques aigus (**SCA**, **AVC**)\n"
                "- Mécanisme : érosion ou déchirure de la chape fibreuse\n"
                "- Formation immédiate d'un **thrombus** → réduction ou obstruction de la lumière "
                "→ fragmentation possible avec embolies\n"
                "- Rupture d'autant plus probable que la plaque est jeune, riche en lipides "
                "et cellules inflammatoires, avec une **chape fibreuse fine**\n"
                "- Concerne souvent des plaques peu sténosantes\n"
                "- De nombreuses ruptures restent asymptomatiques"
            )),
            FicheRow(concept="Progression de la plaque", detail_md=(
                "- Réduction de la lumière du vaisseau par augmentation de volume\n"
                "- Augmentation de la composante lipidique et de la matrice\n"
                "- Progression possible mais surtout par poussées lors d'accidents aigus "
                "(incorporation de matériel thrombotique)\n"
                "- Évolution lente vers un tissu fibreux et calcifié\n"
                "- **Hémorragie intraplaque** : augmentation brusque du volume pouvant rompre la chape\n"
                "- Régression observée expérimentalement chez l'animal, difficilement démontrable chez l'homme"
            )),
            FicheRow(concept="Remodelage artériel", detail_md=(
                "- **Remodelage compensateur** : élargissement du diamètre pour préserver la lumière\n"
                "- **Remodelage constrictif** : réduction du diamètre du vaisseau, "
                "majore la sténose en regard de la plaque\n"
                "- Aggravation possible :\n"
                "  - Progressive (croissance de la plaque)\n"
                "  - Brutale (rupture/érosion + thrombus → réduction de lumière voire occlusion)"
            )),
            FicheRow(concept="", detail_md=(
                "- Une rupture de plaque peut concerner une plaque **peu sténosante** : "
                "la gravité de l'accident n'est pas proportionnelle à l'ancienneté ou à l'étendue de l'athérome"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Anévrismes", rows=[
            FicheRow(concept="Développement des anévrismes", detail_md=(
                "- L'athérome altère la structure pariétale et détruit la matrice extracellulaire\n"
                "- → Dilatations anévrismales\n"
                "- ⚠ Tous les anévrismes ne sont **pas** liés à l'athérome"
            )),
        ]),
    ])

    # ── PARTIE III : POINTS D'IMPACT DES THÉRAPEUTIQUES ──
    partie_iii = Partie(numero="III", titre="Points d'impact des thérapeutiques", sous_parties=[
        SousPartie(lettre="A", titre="Prévention de l'athérome", rows=[
            FicheRow(concept="◆ Diminution de la dysfonction endothéliale", detail_md=(
                "- Suppression ou traitement de tous les **facteurs de risque modifiables**\n"
                "  - Arrêt du tabac\n"
                "  - Lutte contre la sédentarité"
            )),
            FicheRow(concept="Diminution de l'accumulation des LDL", detail_md=(
                "- Régime alimentaire\n"
                "- **Statines** et autres hypolipémiants"
            )),
            FicheRow(concept="◆ Stabilisation des plaques", detail_md=(
                "- Diminution du risque de rupture\n"
                "- Propriété des **statines**"
            )),
            FicheRow(concept="Régression du volume des plaques", detail_md=(
                "- Statines à fortes doses\n"
                "- Si besoin associées à l'**ézétimibe**\n"
                "- Ou aux **anti-PCSK9**"
            )),
            FicheRow(concept="Diminution de l'inflammation", detail_md=(
                "- Aspirine\n"
                "- Statines"
            )),
            FicheRow(concept="Diminution des contraintes mécaniques", detail_md=(
                "- Traitements **antihypertenseurs**"
            )),
        ]),
        SousPartie(lettre="B", titre="Prise en charge des complications", rows=[
            FicheRow(concept="Diminution des extensions de thromboses (rupture de plaque)", detail_md=(
                "- **Antiplaquettaires** (aspirine, clopidogrel)\n"
                "- **Héparines** en urgence"
            )),
            FicheRow(concept="Retentissement des sténoses", detail_md=(
                "- Traitement de l'insuffisance coronarienne stable et de l'ischémie\n"
                "- Sténoses serrées des carotides (segment extracrânien)\n"
                "- Sténoses des artères rénales (HTA, insuffisance rénale)\n"
                "- **AOMI** (artériopathie oblitérante des membres inférieurs)\n"
                "- Sténoses des artères digestives"
            )),
            FicheRow(concept="Complications CV aiguës", detail_md=(
                "- Traitement des **syndromes coronariens aigus**\n"
                "- AVC\n"
                "- Dissections de l'aorte\n"
                "- Ischémies aiguës des membres inférieurs"
            )),
            FicheRow(concept="Traitement des lésions menaçantes", detail_md=(
                "- Angioplastie ou pontage coronaire\n"
                "- Chirurgie ou angioplastie carotidienne\n"
                "- Cure chirurgicale des anévrismes (ou endoprothèses)\n"
                "- Angioplastie ou pontage des artères des membres inférieurs"
            )),
        ]),
    ])

    # ── PARTIE IV : LOCALISATIONS PRÉFÉRENTIELLES ──
    partie_iv = Partie(numero="IV", titre="Localisations préférentielles des lésions d'athérosclérose", sous_parties=[
        SousPartie(lettre="A", titre="Topographie des plaques", rows=[
            FicheRow(concept="◆ Sites préférentiels", detail_md=(
                "- L'athérome se développe à proximité des **flux artériels turbulents** :\n"
                "  - Ostium\n"
                "  - Bifurcation\n"
                "  - Zones de contrainte mécanique\n"
                "- Atteinte des artères de gros et moyen calibre : aorte et ses branches\n"
                "- Extension à plusieurs territoires habituelle"
            )),
        ]),
        SousPartie(lettre="B", titre="Territoires principaux", rows=[
            FicheRow(concept="◆ Localisations principales", detail_md=(
                "- Plaques carotidiennes → **AVC**\n"
                "- Plaques coronariennes → cardiopathies ischémiques\n"
                "- Plaques de la crosse de l'aorte → AVC\n"
                "- Lésions de l'aorte terminale → favorisent les anévrismes de l'aorte abdominale\n"
                "- Sténoses des artères rénales → HTA et insuffisance rénale\n"
                "- Sténoses des artères digestives → ischémie mésentérique\n"
                "- Sténoses des artères des MI → **AOMI**\n"
                "- Atteinte polyvasculaire : patient polyathéromateux (cf. partie VI)"
            )),
            FicheRow(concept="Tableau récapitulatif", detail_md=(
                "| Territoire | Complication clinique |\n"
                "|------------|----------------------|\n"
                "| Carotides | AVC |\n"
                "| Coronaires | Cardiopathie ischémique, SCA |\n"
                "| Crosse de l'aorte | AVC |\n"
                "| Aorte abdominale | Anévrisme |\n"
                "| Artères rénales | HTA, insuffisance rénale |\n"
                "| Artères digestives | Ischémie mésentérique |\n"
                "| Artères des MI | AOMI |"
            )),
            FicheRow(concept="", detail_md=(
                "- **Quatre principaux territoires** de la maladie athéromateuse à connaître : "
                "coronaire, carotide, artères des MI, aorte abdominale"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE V : ÉVOLUTION NATURELLE ET FDR ──
    partie_v = Partie(numero="V", titre="Évolution naturelle de la maladie athéromateuse", sous_parties=[
        SousPartie(lettre="A", titre="Évolution et complications", rows=[
            FicheRow(concept="◆ Caractéristiques évolutives", detail_md=(
                "- Début très précoce, **dès l'enfance**\n"
                "- Vitesse de progression dépendante des facteurs de risque et du vieillissement\n"
                "- Aggravation par étapes silencieuses (développement intermittent des plaques)"
            )),
            FicheRow(concept="Réduction progressive de la lumière", detail_md=(
                "- → Tableaux d'**ischémie chronique stable** :\n"
                "  - Angor d'effort\n"
                "  - Claudication intermittente (membres inférieurs)\n"
                "  - Claudication digestive (douleurs postprandiales)"
            )),
            FicheRow(concept="Rupture de plaque", detail_md=(
                "- → **Complications aiguës** selon le territoire :\n"
                "  - SCA ST+ (thrombose occlusive)\n"
                "  - AVC ischémique\n"
                "  - Ischémie aiguë de membre inférieur"
            )),
            FicheRow(concept="Érosion de plaque", detail_md=(
                "- Contraintes de cisaillement importantes\n"
                "- Possibilité de thrombose superficielle + embolisation distale\n"
                "- Ex : **SCA non ST+** (sans sus-décalage du ST)"
            )),
            FicheRow(concept="", detail_md=(
                "- La gravité d'un accident aigu n'est pas proportionnelle à l'ancienneté ou "
                "à l'étendue de l'athérome\n"
                "- Une plaque jeune rompue peut donner un **infarctus** ou une **mort subite**\n"
                "- À l'inverse, une occlusion chronique peut être asymptomatique "
                "(développement de **collatéralité** suppléant le territoire)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Facteurs de risque d'athérome", rows=[
            FicheRow(concept="◆ FDR non modifiables", detail_md=(
                "- Âge\n"
                "- Sexe masculin\n"
                "- Antécédents familiaux"
            )),
            FicheRow(concept="◆ FDR modifiables principaux", detail_md=(
                "- **Tabagisme**\n"
                "- **HTA**\n"
                "- **Dyslipidémies**\n"
                "- **Diabète**"
            )),
            FicheRow(concept="Facteurs prédisposants", detail_md=(
                "- Obésité\n"
                "- Sédentarité\n"
                "- Stress et conditions psychosociales (terrain dépressif, niveau socioéducationnel bas)\n"
                "- Facteurs environnementaux : pollution atmosphérique"
            )),
            FicheRow(concept="Facteurs propres chez la femme", detail_md=(
                "- **Ménopause précoce**"
            )),
            FicheRow(concept="Marqueurs de risque", detail_md=(
                "- Éléments associés à une augmentation du risque CV, sans lien de causalité établi\n"
                "- Marqueurs biologiques : **CRP**\n"
                "- Marqueurs vasculaires : témoins du développement de l'athérome avant le stade clinique\n"
                "  - Ex : plaques carotidiennes à l'échographie comme marqueur de risque coronarien"
            )),
            FicheRow(concept="Prévention", detail_md=(
                "- **Prévention primaire** : avant développement clinique\n"
                "- **Prévention secondaire** : après présentation clinique (chronique ou aiguë)\n"
                "- Les lésions sévères asymptomatiques (ex : sténose carotidienne serrée) → "
                "stratégie équivalente à la prévention secondaire"
            )),
            FicheRow(concept="", detail_md=(
                "- **FDR modifiables principaux** : Tabagisme, HTA, Dyslipidémies, Diabète (THDD)"
            ), kind="mnemo"),
        ]),
    ])

    # ── PARTIE VI : LE MALADE POLYATHÉROMATEUX ──
    partie_vi = Partie(numero="VI", titre="Le malade polyathéromateux (ou polyvasculaire)", sous_parties=[
        SousPartie(lettre="A", titre="Définition et prévalence", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- Atteinte athéromateuse d'**au moins 2 territoires artériels différents**\n"
                "- Atteinte symptomatique OU asymptomatique mais significative\n"
                "  - Ex : sténose carotidienne 50 % asymptomatique chez un patient AOMI clinique\n"
                "- ⚠ Une simple plaque non sténosante (< 50 %) et non compliquée ne suffit **pas** "
                "à qualifier un patient de polyvasculaire"
            )),
            FicheRow(concept="◆ Prévalence selon la première localisation", detail_md=(
                "| Premier territoire | Autre atteinte | Prévalence |\n"
                "|--------------------|----------------|------------|\n"
                "| Coronarien | AOMI | 20 % |\n"
                "| Coronarien | Sténose carotidienne | 20 % |\n"
                "| Coronarien | Sténose artères rénales | 20 % |\n"
                "| AOMI / Sténose carotidienne / AAA | Atteinte coronarienne | 40-50 % |\n"
                "- Les patients **AOMI** sont ceux ayant le plus souvent une atteinte polyvasculaire associée"
            )),
            FicheRow(concept="Dépistage systématique", detail_md=(
                "- Dépister les autres territoires dès découverte d'une lésion athéromateuse, et "
                "tout au long du suivi\n"
                "- Dépistage utile **seulement s'il modifie la prise en charge**\n"
                "- Ne pas oublier la recherche de dysfonction érectile "
                "(indicateur de maladie artérielle)"
            )),
        ]),
        SousPartie(lettre="B", titre="Bilan d'extension des lésions", rows=[
            FicheRow(concept="Évaluation des FDR", detail_md=(
                "- Évaluation des FDR communs à tous les territoires\n"
                "- Calcul du **risque CV global**"
            )),
            FicheRow(concept="◆ Bilan clinique systématique", detail_md=(
                "- Interrogatoire et examen clinique de tous les territoires\n"
                "- Pression artérielle brachiale bilatérale : "
                "différence > **15 mmHg** entre les 2 bras (sur plusieurs mesures) → "
                "suspecter une **sténose subclavière unilatérale**"
            )),
            FicheRow(concept="◆ Explorations complémentaires", detail_md=(
                "- **ECG** systématique\n"
                "- Mesure de l'**IPS** (index de pression systolique) aux MI\n"
                "- Dépistage d'**AAA** notamment chez les hommes après 65 ans\n"
                "- Sélection des examens selon :\n"
                "  - Le bilan clinique\n"
                "  - Le risque CV global\n"
                "  - La prévalence d'atteinte d'un autre territoire\n"
                "  - La nécessité d'un geste invasif"
            )),
        ]),
        SousPartie(lettre="C", titre="Thérapeutiques communes à tous les polyvasculaires", rows=[
            FicheRow(concept="◆ Prise en charge intensive des FDR modifiables", detail_md=(
                "- Arrêt du tabac\n"
                "- Diététique et éducation thérapeutique\n"
                "- Activité physique régulière"
            )),
            FicheRow(concept="◆ Médicaments réduisant la morbimortalité", detail_md=(
                "- **Antiagrégant plaquettaire** :\n"
                "  - Aspirine systématique (**75 à 325 mg/j**), CI rares (intolérance gastrique, allergie)\n"
                "  - Clopidogrel (Plavix®) si intolérance à l'aspirine ou atteinte polyvasculaire "
                "compliquée (notamment AOMI)\n"
                "- **Statines** systématiques, objectifs de prévention secondaire\n"
                "- **IEC** (ou **ARA2**) : recommandés pour diminuer le risque d'infarctus, d'AVC et "
                "freiner l'altération de la fonction rénale"
            )),
            FicheRow(concept="Bêtabloquants : place limitée", detail_md=(
                "- Efficacité prouvée **uniquement après un IDM**, notamment en cas d'altération de la FEVG\n"
                "- Bénéfice à distance de l'IDM chez FEVG normale remis en cause\n"
                "- Pas d'efficacité montrée en maladie coronarienne stable ou chez le polyvasculaire"
            )),
            FicheRow(concept="", detail_md=(
                "- Ne **JAMAIS oublier** l'**aspirine** et les **statines** en prévention secondaire"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Prise en charge spécifique et suivi", rows=[
            FicheRow(concept="◆ Seuils d'intervention sur lésions asymptomatiques", detail_md=(
                "| Lésion | Seuil de geste invasif |\n"
                "|--------|------------------------|\n"
                "| Anévrisme aorte abdominale | Diamètre >= 55 mm (50 mm chez la femme) ou croissance >= 5 mm/an |\n"
                "| Sténose carotidienne asymptomatique | > 60 % (souvent > 80 %), si espérance de vie > 5 ans |\n"
                "| Sténose coronaire après SCA | Revascularisation si sténose > 70 % significative |"
            )),
            FicheRow(concept="Revascularisation myocardique non systématique", detail_md=(
                "- En ischémie silencieuse ou angor stable, indications limitées :\n"
                "  - Patient symptomatique malgré traitement médical\n"
                "  - FEVG altérée\n"
                "  - Faible seuil d'ischémie au test d'effort\n"
                "  - Ischémie étendue documentée (scintigraphie, ETT, IRM de stress)\n"
                "  - Nécessité d'une chirurgie à haut risque (ex : aorte abdominale)\n"
                "  - **FFR <= 0,8** (fractional flow reserve : sténose hémodynamiquement significative)"
            )),
            FicheRow(concept="Stratégie de revascularisation multi-territoires", detail_md=(
                "- Évaluation du risque et recherche d'une lésion cliniquement instable\n"
                "- En urgence : revascularisation de la lésion coupable sans prolonger le dépistage\n"
                "- En dehors de l'urgence : décision au cas par cas en réunion pluridisciplinaire"
            )),
            FicheRow(concept="Éducation thérapeutique", detail_md=(
                "- Apprentissage de l'intensité et de la régularité de l'activité physique "
                "et des mesures hygiénodiététiques\n"
                "- Apprentissage de l'observance, de l'efficacité et de la tolérance des traitements\n"
                "- Évaluation régulière du respect des objectifs de prévention secondaire\n"
                "- Connaissance des **signes d'appel** de complications "
                "(douleur thoracique, déficit neurologique, etc.)"
            )),
            FicheRow(concept="Bilan clinique annuel", detail_md=(
                "- Examen clinique de tous les territoires artériels\n"
                "- Choix des explorations complémentaires nécessaires"
            )),
        ]),
    ])

    tableaux = [
        TableauSynthese(titre="Synthèse - Formation et évolution de la plaque", markdown=(
            "| Étape | Mécanisme | Conséquence |\n"
            "|-------|-----------|-------------|\n"
            "| 1. Accumulation LDL | Pénétration dans l'intima + oxydation | Initiation |\n"
            "| 2. Recrutement monocytes | Molécules d'adhérence, diapédèse | Macrophages → cellules spumeuses |\n"
            "| 3. Inflammation | Cytokines, métalloprotéases | Destruction matrice |\n"
            "| 4. Migration CML | Néo-intima, collagène | Chape fibreuse |\n"
            "| 5. Stries lipidiques | Dès le jeune âge | Lésion réversible |\n"
            "| 6. Plaque mature | Centre lipidique + chape fibreuse | Stable ou instable |\n"
            "| 7. Rupture/érosion | Thrombose | Accident aigu (SCA, AVC) |"
        )),
        TableauSynthese(titre="Synthèse - Plaque stable vs plaque instable", markdown=(
            "| Caractère | Plaque stable | Plaque instable |\n"
            "|-----------|---------------|-----------------|\n"
            "| Centre lipidique | Modéré | Important, riche en lipides |\n"
            "| Inflammation | Faible | Forte (cellules inflammatoires) |\n"
            "| Chape fibreuse | Épaisse | Fine, vulnérable |\n"
            "| Sténose | Souvent significative | Souvent peu sténosante |\n"
            "| Évolution | Ischémie chronique | Rupture brutale → thrombose aiguë |"
        )),
        TableauSynthese(titre="Synthèse - Facteurs de risque d'athérome", markdown=(
            "| Catégorie | FDR / Marqueurs |\n"
            "|-----------|------------------|\n"
            "| Non modifiables | Âge, sexe masculin, ATCD familiaux |\n"
            "| Modifiables principaux | Tabagisme, HTA, Dyslipidémies, Diabète |\n"
            "| Prédisposants | Obésité, sédentarité, stress, pollution |\n"
            "| Femme | Ménopause précoce |\n"
            "| Marqueurs biologiques | CRP |\n"
            "| Marqueurs vasculaires | Plaques carotidiennes à l'échographie |"
        )),
        TableauSynthese(titre="Synthèse - Cibles thérapeutiques de l'athérosclérose", markdown=(
            "| Cible | Moyens thérapeutiques |\n"
            "|-------|------------------------|\n"
            "| Dysfonction endothéliale | Arrêt tabac, lutte sédentarité |\n"
            "| Accumulation LDL | Régime, statines, ézétimibe, anti-PCSK9 |\n"
            "| Stabilisation des plaques | Statines |\n"
            "| Inflammation | Aspirine, statines |\n"
            "| Contraintes mécaniques | Antihypertenseurs |\n"
            "| Thrombose post-rupture | Antiplaquettaires, héparines |\n"
            "| Lésions menaçantes | Angioplastie, pontage, chirurgie |"
        )),
        TableauSynthese(titre="Synthèse - Bilan polyvasculaire et thérapeutiques admises", markdown=(
            "| Élément | Mesure |\n"
            "|---------|--------|\n"
            "| Examen clinique | Tous les territoires + PA bilatérale |\n"
            "| Différence de PA bras | > 15 mmHg → sténose subclavière |\n"
            "| ECG | Systématique |\n"
            "| IPS | Systématique aux MI |\n"
            "| Dépistage AAA | Hommes > 65 ans |\n"
            "| Traitement de fond | Aspirine ou clopidogrel + statine + IEC/ARA2 |\n"
            "| Mesures non médicamenteuses | Arrêt tabac, diététique, activité physique |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Mortalité CV | 1re cause mondiale, 2e en France | 1re chez les femmes en France |\n"
        "| Incidence H/F | 3-5 × | Plus fréquente chez l'homme |\n"
        "| Coronarien avec autre atteinte | 20 % | AOMI / carotide / artère rénale |\n"
        "| AOMI / carotide / AAA → coronaire | 40-50 % | Atteinte coronarienne associée |\n"
        "| Aspirine | 75-325 mg/j | Antiagrégant systématique |\n"
        "| Différence PA bras | > 15 mmHg | Sténose subclavière unilatérale |\n"
        "| Dépistage AAA | Hommes > 65 ans | Polyvasculaire |\n"
        "| Indication chirurgie AAA | Diamètre >= 55 mm (50 mm femme) | Ou croissance >= 5 mm/an |\n"
        "| Sténose carotidienne asymptomatique | > 60 % (souvent > 80 %) | Si espérance de vie > 5 ans |\n"
        "| Sténose coronaire significative | > 70 % | Revascularisation post-SCA |\n"
        "| FFR significatif | <= 0,8 | Sténose hémodynamiquement significative |"
    ))

    points_cles = [
        "L'athérome est la **1re cause de mortalité mondiale** ; 2e en France (1re chez les femmes)",
        "Hausse de l'incidence chez les **femmes jeunes** (tabac) ; H/F = 3-5×",
        "**Plaque stable** : chape fibreuse épaisse ; **plaque instable** : chape fine, riche en lipides",
        "**Rupture/érosion** de plaque → thrombus → SCA, AVC, ischémie aiguë de membre",
        "Gravité de l'accident **non corrélée** à l'ancienneté ni à la sténose de la plaque",
        "**FDR modifiables (THDD)** : Tabac, HTA, Dyslipidémies, Diabète ; ménopause précoce chez la femme",
        "**4 territoires principaux** : coronaires, carotides, MI (AOMI), aorte abdominale (AAA)",
        "**Polyvasculaire** = >= 2 territoires significatifs ; **AOMI** = plus pourvoyeur",
        "Traitement de fond : **aspirine** (ou clopidogrel) + **statines** + **IEC/ARA2**",
        "**Ne JAMAIS oublier** aspirine + statines en prévention secondaire (inacceptable)",
    ]

    fiche_eclair_md = (
        "**Définition** : remaniements de l'intima des artères de gros et moyen calibre. "
        "Accumulation lipides, fibrose, calcaire.\n\n"
        "**Épidémio** : 1re cause mortalité mondiale. 2e en France (1re chez les femmes). "
        "H/F = 3-5×. Hausse chez femmes jeunes (tabac).\n\n"
        "**Plaque** : LDL → oxydation → cellules spumeuses → centre lipidique + chape fibreuse. "
        "Stable = chape épaisse. Instable = chape fine, peu sténosante, rupture.\n\n"
        "**Aigu** : rupture/érosion → thrombus → SCA, AVC, ischémie aiguë de membre. "
        "Gravité non corrélée à la sténose.\n\n"
        "**FDR modifiables (THDD)** : Tabac, HTA, Dyslipidémies, Diabète. "
        "**Non modifiables** : âge, sexe M, ATCD. Femme : ménopause précoce.\n\n"
        "**4 territoires** : coronaires (SCA), carotides (AVC), MI (AOMI), aorte abdominale (AAA).\n\n"
        "**Polyvasculaire** : >= 2 territoires significatifs. AOMI = plus pourvoyeur. "
        "Dépister dysfonction érectile.\n\n"
        "**Bilan** : PA bilatérale (> 15 mmHg = subclavière) + ECG + IPS + AAA chez H > 65 ans.\n\n"
        "**Traitement** : arrêt tabac + activité physique + aspirine 75-325 mg/j (ou clopidogrel) "
        "+ statines + IEC/ARA2. Bêtabloquants : post-IDM avec FEVG altérée.\n\n"
        "**Seuils invasifs** : AAA >= 55 mm (50 mm femme). Carotide asympto > 60 %. "
        "Coronaire > 70 % ou FFR <= 0,8.\n\n"
        "**Inacceptable** : oublier aspirine + statines en prévention secondaire."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 221 - Athérome : épidémiologie et physiopathologie",
        annee="2025-2026",
        item="Item 221",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 221",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-221_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

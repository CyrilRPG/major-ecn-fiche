"""Génère la fiche de l'Item 224 - Hypertension artérielle de l'adulte et de l'enfant (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Définition et confirmation diagnostique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Mesure de la pression artérielle"),
            PlanSousPartie(lettre="B", titre="Définition et stratégie diagnostique"),
        ]),
        PlanPartie(numero="II", titre="Épidémiologie, physiopathologie et conséquences", sous_parties=[
            PlanSousPartie(lettre="A", titre="Épidémiologie"),
            PlanSousPartie(lettre="B", titre="Physiopathologie"),
            PlanSousPartie(lettre="C", titre="Complications et organes cibles"),
        ]),
        PlanPartie(numero="III", titre="Prise en charge initiale du patient hypertendu", sous_parties=[
            PlanSousPartie(lettre="A", titre="Circonstances de découverte"),
            PlanSousPartie(lettre="B", titre="Interrogatoire et examen clinique"),
            PlanSousPartie(lettre="C", titre="Examens complémentaires et atteinte infraclinique"),
            PlanSousPartie(lettre="D", titre="Stratification du risque et consultation d'annonce"),
        ]),
        PlanPartie(numero="IV", titre="Traitement", sous_parties=[
            PlanSousPartie(lettre="A", titre="Stratégie thérapeutique et cibles"),
            PlanSousPartie(lettre="B", titre="Mesures hygiénodiététiques"),
            PlanSousPartie(lettre="C", titre="Traitement médicamenteux"),
            PlanSousPartie(lettre="D", titre="Sujet âgé et éducation thérapeutique"),
        ]),
        PlanPartie(numero="V", titre="Suivi du patient hypertendu et HTA résistante", sous_parties=[
            PlanSousPartie(lettre="A", titre="Cible atteinte"),
            PlanSousPartie(lettre="B", titre="Cible non atteinte et HTA résistante"),
        ]),
        PlanPartie(numero="VI", titre="HTA secondaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Dépistage et bilan"),
            PlanSousPartie(lettre="B", titre="Causes rénales et rénovasculaires"),
            PlanSousPartie(lettre="C", titre="Causes endocriniennes"),
            PlanSousPartie(lettre="D", titre="Coarctation, SAOS, iatrogénie"),
        ]),
        PlanPartie(numero="VII", titre="Urgences hypertensives et HTA maligne", sous_parties=[
            PlanSousPartie(lettre="A", titre="Urgence hypertensive"),
            PlanSousPartie(lettre="B", titre="HTA maligne"),
        ]),
    ]

    # ── PARTIE I : DÉFINITION ET CONFIRMATION DIAGNOSTIQUE ──
    partie_i = Partie(numero="I", titre="Définition et confirmation diagnostique", sous_parties=[
        SousPartie(lettre="A", titre="Mesure de la pression artérielle", rows=[
            FicheRow(concept="◆ PA de consultation : méthode", detail_md=(
                "- Appareil électronique validé et recalibré, méthode oscillométrique au bras "
                "(site de référence : www.stridebp.org/fr)\n"
                "- Méthode auscultatoire abandonnée sauf en cas de **fibrillation atriale**\n"
                "- **Brassard adapté** : 3 tailles (obèse / standard / enfant), à hauteur du cœur\n"
                "- Sujet assis depuis **> 5 min**, environnement calme, repos physique et psychique\n"
                "- À distance d'effort, café ou cigarette (> 30 min), vessie vide, dos calé"
            )),
            FicheRow(concept="◆ PA de consultation : nombre de mesures", detail_md=(
                "- **≥ 3 mesures** espacées de 1 à 2 min, moyenne des 2 dernières\n"
                "- Si écart > 10 mmHg sur PAS entre les 2 premières → mesures supplémentaires\n"
                "- Mesure aux deux bras à la 1re consultation (asymétrie → sténose subclavière)\n"
                "  - Si asymétrie : retenir le bras avec les valeurs les plus élevées\n"
                "- FC par palpation du pouls **≥ 30 secondes** (recherche d'arythmie)"
            )),
            FicheRow(concept="◆ Recherche d'hypotension orthostatique", detail_md=(
                "- Fréquente chez sujet âgé, fragile, diabétique, dysautonomie\n"
                "- Mesure PA et FC après 5 min en position allongée ou assise\n"
                "- Puis en position debout après 1 min et 3 min\n"
                "- **Diagnostic** : baisse **≥ 20 mmHg PAS** et/ou **≥ 10 mmHg PAD** à 1 et/ou 3 min"
            )),
            FicheRow(concept="⚠ Pseudo-HTA et rigidité artérielle", detail_md=(
                "- Sujet âgé, diabétique, hémodialysé → calcifications vasculaires → artères incompressibles\n"
                "- Surestimation de la PA par le brassard de 20 mmHg (parfois 40-50 mmHg)\n"
                "- **Manœuvre d'Osler** : pouls radial perçu alors que brassard gonflé > PAS\n"
                "- Cordon induré huméral ou radial possible\n"
                "- **Pression pulsée > 65 mmHg** = marqueur de rigidité artérielle"
            )),
            FicheRow(concept="◆ Automesure tensionnelle (AMT)", detail_md=(
                "- Mesure de la PA par le patient à domicile\n"
                "- Examen recommandé en France pour confirmer le diagnostic d'HTA\n"
                "- Appareil semi-automatique avec brassard huméral (poignet déconseillé)\n"
                "- Éducation du patient nécessaire\n"
                "- Améliore la prédiction du risque CV et l'adhésion thérapeutique"
            )),
            FicheRow(concept="Règle des 3 (SFHTA/HAS)", detail_md=(
                "- 3 mesures le matin (20 min après le lever, avant petit-déjeuner et médicaments)\n"
                "- 3 mesures le soir (dans l'heure avant le coucher)\n"
                "- 3 jours consécutifs = **18 mesures au total**\n"
                "- Après 5 min de repos, 3 mesures espacées de 1-2 min en position assise\n"
                "- Le patient note PAS, PAD, FC et calcule la moyenne des 2 dernières mesures"
            )),
            FicheRow(concept="MAPA — Mesure Ambulatoire de la PA", detail_md=(
                "- Utilisée si AMT impossible ou non fiable (anxiété, manipulation)\n"
                "- Meilleure prédiction du risque CV (PA nocturne > PA diurne pour pronostic)\n"
                "- Très corrélée à l'atteinte des organes cibles\n"
                "- Réalisée sur **24h** en période d'activité habituelle\n"
                "- Diurne : 1 mesure / 15-30 min\n"
                "- Nocturne : 1 mesure / 30-60 min\n"
                "- Patient remplit un journal d'activité (heures coucher/lever, symptômes)"
            )),
            FicheRow(concept="Indications spécifiques de la MAPA", detail_md=(
                "- Confirmer le diagnostic d'**HTA résistante**\n"
                "- Rechercher des épisodes d'hypotension symptomatique (asthénie, lipothymies)\n"
                "- Mieux évaluer la PA en cas de forte variabilité des mesures\n"
                "- Explorer la PA nocturne"
            )),
            FicheRow(concept="", detail_md=(
                "- **Règle des 3** : 3 matin + 3 soir × 3 jours = **18 mesures**\n"
                "- Brassard adapté + 3 mesures espacées + moyenne des 2 dernières pour la PA de consultation"
            ), kind="a_retenir"),
            FicheRow(concept="", detail_md=(
                "- Ne JAMAIS retenir la PA de la 1re mesure seule (effet blouse blanche, anxiété)\n"
                "- Brassard trop petit → surestimation de la PA"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Définition et stratégie diagnostique", rows=[
            FicheRow(concept="Classification ESC 2024 (3 catégories)", detail_md=(
                "- La distribution des PA dans la population est continue et la progression graduelle\n"
                "- **PA non élevée** : PAS < 120 et PAD < 70 mmHg (en consultation ou AMT)\n"
                "- **PA élevée** : PAS 120-139 et/ou PAD 70-89 mmHg en consultation (AMT 120-134/70-84)\n"
                "- **HTA** : PAS ≥ 140 et/ou PAD ≥ 90 mmHg en consultation (AMT ≥ 135/85)"
            )),
            FicheRow(concept="◆ Définition de l'HTA selon la méthode", detail_md=(
                "| Méthode | Seuil HTA (mmHg) |\n"
                "|---------|------------------|\n"
                "| **Consultation** | PAS ≥ 140 et/ou PAD ≥ 90 |\n"
                "| **AMT** | PAS ≥ 135 et/ou PAD ≥ 85 |\n"
                "| **MAPA sur 24h** | PAS ≥ 130 et/ou PAD ≥ 80 |\n"
                "| **MAPA diurne** | PAS ≥ 135 et/ou PAD ≥ 85 |\n"
                "| **MAPA nocturne** | PAS ≥ 120 et/ou PAD ≥ 70 |"
            )),
            FicheRow(concept="Pourquoi la PA élevée importe", detail_md=(
                "- Notion importante : évaluation du risque CV global\n"
                "- Utilisation des scores **SCORE2, SCORE2-OP, SCORE-Diabetes**\n"
                "- Situations d'emblée à haut risque : maladie CV connue, IRC, hypercholestérolémie familiale\n"
                "- Possibilité d'introduction d'un antihypertenseur si risque suffisamment élevé"
            )),
            FicheRow(concept="◆ Grades de sévérité de l'HTA (consultation)", detail_md=(
                "| Grade | PAS (mmHg) | PAD (mmHg) |\n"
                "|-------|-----------|------------|\n"
                "| **Grade 1** | 140-159 | et/ou 90-99 |\n"
                "| **Grade 2** | 160-179 | et/ou 100-109 |\n"
                "| **Grade 3** | ≥ 180 | et/ou ≥ 110 |"
            )),
            FicheRow(concept="Délais de confirmation par mesure ambulatoire", detail_md=(
                "- HTA grade 1 ou 2 : confirmation en mesure ambulatoire dans le mois\n"
                "- HTA grade 3 sans urgence : confirmation dans la semaine\n"
                "- HTA grade 3 → toujours rechercher une **urgence hypertensive**\n"
                "- HTA confirmée par concordance consultation + ambulatoire (AMT ou MAPA)"
            )),
            FicheRow(concept="◆ HTA blouse blanche", detail_md=(
                "- **15-20 %** de la population adulte\n"
                "- PA consultation > 140/90 mais mesures ambulatoires NORMALES\n"
                "- **Pas d'indication à un traitement médicamenteux**\n"
                "- Mesures hygiénodiététiques proposées\n"
                "- Surveillance régulière (risque évolutif vers HTA confirmée)"
            )),
            FicheRow(concept="◆ HTA masquée", detail_md=(
                "- **10-15 %** de la population adulte\n"
                "- PA consultation < 140/90 mais mesures ambulatoires confirment l'HTA (AMT > 135/85)\n"
                "- Souvent : PA consultation proche des seuils + risque CV élevé\n"
                "- Même risque d'événements CV que les formes habituelles d'HTA\n"
                "- Prise en charge identique à une HTA confirmée\n"
                "- Mesures ambulatoires privilégiées pour le suivi"
            )),
            FicheRow(concept="", detail_md=(
                "- HTA confirmée = **2 méthodes concordantes** : consultation + AMT (ou MAPA)\n"
                "- HTA masquée doit être traitée comme une HTA classique\n"
                "- HTA blouse blanche : pas de médicaments, surveillance + RHD"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE II : ÉPIDÉMIOLOGIE, PHYSIOPATHOLOGIE ET CONSÉQUENCES ──
    partie_ii = Partie(numero="II", titre="Épidémiologie, physiopathologie et conséquences", sous_parties=[
        SousPartie(lettre="A", titre="Épidémiologie", rows=[
            FicheRow(concept="◆ Prévalence et fardeau mondial", detail_md=(
                "- HTA = maladie chronique la plus fréquente en France et dans le monde\n"
                "- > 1,5 milliard de personnes affectées dans le monde\n"
                "- **1re cause de mortalité mondiale** : > 10 millions de décès / an\n"
                "- En France : **17 millions d'adultes hypertendus** en 2023\n"
                "- 1,6 million de nouveaux patients traités chaque année"
            )),
            FicheRow(concept="Étude ESTEBAN (France, années 2010)", detail_md=(
                "- 30 % de la population adulte (18-74 ans) hypertendue\n"
                "- 50 % des hypertendus non traités ou non diagnostiqués\n"
                "- 50 % des hypertendus traités n'atteignent pas les objectifs\n"
                "- **Seuls 25 %** des hypertendus français diagnostiqués + traités + contrôlés\n"
                "- Prévalence > 60 % après 70 ans, > 70 % après 80 ans"
            )),
            FicheRow(concept="Facteurs favorisants", detail_md=(
                "- Autres facteurs de risque CV associés\n"
                "- Surpoids, populations défavorisées\n"
                "- Consommation d'alcool, sédentarité, stress répétés\n"
                "- Trait partiellement héritable : enfants de parents hypertendus (surtout HTA précoce) plus à risque"
            )),
            FicheRow(concept="◆ Impact en santé publique (France)", detail_md=(
                "- 1re maladie chronique\n"
                "- 1er facteur de risque CV de mortalité\n"
                "- 2e facteur de risque d'années de vie perdues en bonne santé\n"
                "- Facteur de risque majeur de **maladie athéromateuse**"
            )),
            FicheRow(concept="◆ Augmentation du risque CV chez l'hypertendu", detail_md=(
                "| Complication | Risque vs normotendu |\n"
                "|--------------|----------------------|\n"
                "| **AVC** | × 7 |\n"
                "| **Insuffisance cardiaque** | × 4 |\n"
                "| **Insuffisance coronarienne** (SCA) | × 3 |\n"
                "| **AOMI** | × 2 |\n"
                "| **Mortalité CV globale** | × 2 |\n"
                "| **Mort subite** | × 3 |"
            )),
            FicheRow(concept="◆ Bénéfices du traitement", detail_md=(
                "- Méta-analyse 2015 : PAD -5-6 mmHg + PAS -10 mmHg pendant 5 ans :\n"
                "  - AVC : -1/3\n"
                "  - Insuffisance coronarienne : -1/6\n"
                "  - Insuffisance cardiaque : -46 %\n"
                "- Réversibilité du risque meilleure pour les AVC que pour les coronariens"
            )),
            FicheRow(concept="◆ Recommandations de dépistage (ESC 2024)", detail_md=(
                "- Dépistage de la PA élevée et de l'HTA :\n"
                "  - Tous les 3 ans avant 40 ans\n"
                "  - Au moins 1 fois / an à partir de 40 ans"
            )),
            FicheRow(concept="", detail_md=(
                "- HTA = 1re cause de mortalité mondiale, 1re maladie chronique en France\n"
                "- **17 millions** d'hypertendus français, 25 % seulement contrôlés\n"
                "- Risque d'**AVC × 7** chez l'hypertendu"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Physiopathologie", rows=[
            FicheRow(concept="Régulation de la PA — court terme", detail_md=(
                "- Médiée par le système sympathique via le baroréflexe carotidien et aortique\n"
                "- Tronc cérébral (centre vasopresseur) → chaînes sympathiques latérovertébrales → médullosurrénales\n"
                "- α1-adrénergiques vasoconstricteurs / β2-adrénergiques vasodilatateurs"
            )),
            FicheRow(concept="Régulation moyen et long terme", detail_md=(
                "- **Moyen terme** : SRAA + peptides natriurétiques (ANP, BNP)\n"
                "- **Long terme** : natriurèse de pression + système arginine-vasopressine"
            )),
            FicheRow(concept="◆ HTA secondaire vs essentielle", detail_md=(
                "- **10 % HTA secondaire** : cause spécifique (toxique, iatrogène, rénale, rénovasculaire, endocrinienne)\n"
                "  - Traitement ciblé peut améliorer le contrôle voire guérir\n"
                "- **90 % HTA essentielle** : combinaison de facteurs génétiques + environnementaux"
            )),
            FicheRow(concept="Facteurs favorisant l'HTA essentielle", detail_md=(
                "- Génétiques (héritabilité du niveau de PA)\n"
                "- FdR CV : tabagisme, diabète\n"
                "- Comportements alimentaires : riche en sodium, pauvre en potassium / F&L\n"
                "- Surpoids, alcool, sédentarité, absence d'activité physique\n"
                "- Vieillissement"
            )),
            FicheRow(concept="Mécanismes physiopathologiques de l'HTA essentielle", detail_md=(
                "- Dysfonction de plusieurs systèmes de régulation :\n"
                "  - Tonus vasculaire des petites artères (artères de résistance)\n"
                "  - Balance hydrosodée\n"
                "  - Système arginine-vasopressine\n"
                "  - **SRAA**\n"
                "  - Système sympathique (baroréflexe)\n"
                "  - Insulinorésistance (chez sujet en surpoids)"
            )),
            FicheRow(concept="Conséquences mécaniques", detail_md=(
                "- Augmentation de la réactivité des vaisseaux de résistance (vasoconstriction)\n"
                "- Anomalies structurelles des artérioles : fibrose de la média, hyperplasie cellules musculaires lisses\n"
                "- Augmentation de la rigidité artérielle de l'aorte et de ses branches\n"
                "- Rétention hydrosodée (inadéquation PA / excrétion sodée)"
            )),
            FicheRow(concept="HTA essentielle familiale", detail_md=(
                "- 15 % des HTA essentielles sont familiales\n"
                "- Début précoce **avant 30 ans**, profil identique chez un ou les deux parents\n"
                "- Composante génétique forte mais polygénique → pas d'indication de test génétique\n"
                "- De très rares formes monogéniques liées à des anomalies de l'homéostasie rénale"
            )),
        ]),
        SousPartie(lettre="C", titre="Complications et organes cibles", rows=[
            FicheRow(concept="◆ Principe général", detail_md=(
                "- Relation continue et positive entre PA et incidence des complications :\n"
                "  - **Cardiaques** : insuffisance cardiaque, cardiopathie ischémique, FA\n"
                "  - **Neurovasculaires** : AVC, démence\n"
                "  - **Rénales** : néphropathie"
            )),
            FicheRow(concept="◆ Insuffisance cardiaque", detail_md=(
                "- **IC à FEVG altérée** :\n"
                "  - Atteinte ischémique (maladie coronarienne ± IDM)\n"
                "  - HTA elle-même (postcharge augmentée) → HVG excentrique (cœur dilaté + hypertrophié)\n"
                "- **IC à FEVG préservée** :\n"
                "  - Trouble de la compliance et de la relaxation\n"
                "  - Liée à l'HVG ± fibrose VG, cœur hypertrophié non dilaté"
            )),
            FicheRow(concept="Cardiopathie ischémique", detail_md=(
                "- Angor, SCA ST+ ou ST-\n"
                "- L'angor de l'hypertendu peut être lié à :\n"
                "  - Maladie coronarienne athéromateuse\n"
                "  - HTA elle-même (↓ réserve coronarienne par HVG)\n"
                "  - Les deux"
            )),
            FicheRow(concept="◆ Fibrillation atriale", detail_md=(
                "- **HTA = 1re cause de FA** (70 % des sujets en FA sont hypertendus)\n"
                "- Mécanisme : HVG → ↑ pression diastolique VG → dilatation OG\n"
                "- HTA = facteur thromboembolique au cours de la FA → 1 point dans **CHA2DS2-VASc**\n"
                "- Maladie athéromateuse : AOMI, sténose carotidienne, anévrisme aorte abdominale"
            )),
            FicheRow(concept="Mortalité CV chez l'hypertendu", detail_md=(
                "- Multipliée par 5 chez l'homme\n"
                "- Multipliée par 3 chez la femme"
            )),
            FicheRow(concept="◆ Complications neurovasculaires", detail_md=(
                "- AIT et **AVC ischémique** (80 % des AVC dans l'HTA)\n"
                "- **Hémorragie cérébrale** (20 % des AVC dans l'HTA) :\n"
                "  - Intraparenchymateuse (rupture de microanévrisme ou nécrose fibrinoïde)\n"
                "  - Hémorragie méningée (souvent malformation vasculaire associée)\n"
                "- Encéphalopathie hypertensive : surtout HTA s'aggravant rapidement\n"
                "- Lacune cérébrale, démence vasculaire\n"
                "- Rétinopathie hypertensive : stade 4 = œdème papillaire + hémorragie rétinienne"
            )),
            FicheRow(concept="◆ Complications rénales", detail_md=(
                "- **Néphroangiosclérose** :\n"
                "  - Conséquence d'HTA chronique non contrôlée\n"
                "  - Altère séquentiellement artérioles → glomérules → tubules → tissu interstitiel\n"
                "  - Évolue vers l'IR par réduction néphronique qui aggrave l'HTA\n"
                "  - **Microalbuminurie** = signe précoce (glomérulopathie)\n"
                "- IR sur maladie athéromateuse des artères rénales : sténose, emboles de cholestérol\n"
                "- **IRA iatrogène** :\n"
                "  - Diurétiques → déshydratation extracellulaire\n"
                "  - **IEC/ARA2 sur sténose bilatérale** ou rein unique"
            )),
            FicheRow(concept="", detail_md=(
                "- HTA = 1re cause de FA (70 % des FA sont hypertendus)\n"
                "- Microalbuminurie = signe précoce de néphroangiosclérose\n"
                "- Risque d'**IRA** sous IEC/ARA2 en cas de sténose bilatérale des artères rénales"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE III : PRISE EN CHARGE INITIALE ──
    partie_iii = Partie(numero="III", titre="Prise en charge initiale du patient hypertendu", sous_parties=[
        SousPartie(lettre="A", titre="Circonstances de découverte", rows=[
            FicheRow(concept="◆ HTA souvent latente", detail_md=(
                "- Le plus souvent totalement latente = découverte d'examen systématique\n"
                "- Symptômes non spécifiques parfois rapportés :\n"
                "  - Céphalées occipitales : battantes, matinales, résistantes aux antalgiques, cèdent au lever\n"
                "  - Fatigabilité, nervosité, insomnie\n"
                "  - Phosphènes\n"
                "  - Épistaxis"
            )),
            FicheRow(concept="Limites des symptômes", detail_md=(
                "- Causalité pas certaine entre HTA et ces symptômes\n"
                "- Le diagnostic ne peut pas être affirmé sur leur présence\n"
                "- Rechercher d'autres causes\n"
                "- Ces symptômes ne justifient pas à eux seuls un traitement antihypertenseur immédiat"
            )),
            FicheRow(concept="◆ Dépistage systématique", detail_md=(
                "- Le médecin généraliste doit mesurer régulièrement la PA\n"
                "- Autres acteurs : médecin spécialiste, médecin du travail, infirmier, pharmacien, IPA\n"
                "- PA ≥ 140/90 au cabinet → suspicion d'HTA → confirmer hors cabinet par AMT ou MAPA\n"
                "- Sauf en cas d'**urgence hypertensive**"
            )),
        ]),
        SousPartie(lettre="B", titre="Interrogatoire et examen clinique", rows=[
            FicheRow(concept="◆ Objectifs de l'évaluation initiale", detail_md=(
                "- Préciser le niveau de la PA\n"
                "- Évaluer le risque CV global (FdR associés)\n"
                "- Rechercher une atteinte clinique ou infraclinique des organes cibles : vasculaire, cardiaque, cérébrale, rénale\n"
                "- Rechercher des facteurs aggravants\n"
                "- Rechercher des arguments pour une **HTA secondaire**\n"
                "- Se termine par une consultation d'annonce"
            )),
            FicheRow(concept="Interrogatoire — antécédents", detail_md=(
                "- Ancienneté de l'HTA et valeurs antérieures\n"
                "- **FdR CV** : dyslipidémie, diabète, tabagisme, ATCD familiaux CV précoces\n"
                "- Facteurs aggravants : alimentation riche en graisses animales/sel, alcool, sédentarité, surpoids, SAOS\n"
                "- ATCD de grossesse compliquée : HTA/diabète gravidique, prééclampsie, prématurité, fausse couche, MFIU"
            )),
            FicheRow(concept="Symptômes d'atteinte des organes cibles", detail_md=(
                "- **Cardiaque** : palpitations, douleur thoracique, dyspnée, œdèmes\n"
                "- **Neurovasculaire** : céphalées, vertiges, troubles visuels, déficit, troubles cognitifs (MMSE)\n"
                "- **Rénal** : soif, polyurie, nycturie, hématurie, œdèmes\n"
                "- **Artériel périphérique** : extrémités froides, claudication intermittente"
            )),
            FicheRow(concept="◆ Symptômes évocateurs d'HTA secondaire", detail_md=(
                "- ATCD familial : polykystose, polyendocrinopathies (cancers endocriniens)\n"
                "- Infections urinaires répétées, hématurie, maladie rénale connue\n"
                "- **Médicaments** : contraceptifs oraux, vasoconstricteurs nasaux, corticoïdes, AINS, EPO, ciclosporine, tacrolimus, ergot de seigle, anti-VEGF, inhibiteurs tyrosine-kinase\n"
                "- **Toxiques** : réglisse, cannabis, cocaïne, amphétamines, alcool"
            )),
            FicheRow(concept="◆ Triade de Ménard (phéochromocytome)", detail_md=(
                "- **Céphalées + sueurs + palpitations**\n"
                "- Symptômes survenant par crises brutales sans facteur déclenchant\n"
                "- À évoquer chez tout hypertendu avec poussées paroxystiques"
            )),
            FicheRow(concept="Signes orientant vers une endocrinopathie", detail_md=(
                "- Hypokaliémie + troubles neuromusculaires (asthénie, crampes, tétanie, constipation) → **hyperaldostéronisme**\n"
                "- Signes d'hypercatabolisme (ecchymoses), hyperandrogénie (oligoaménorrhée) → **syndrome de Cushing**"
            )),
            FicheRow(concept="Examen clinique — atteinte des organes cibles", detail_md=(
                "- **Neurovasculaire** : souffles carotidiens, déficit moteur ou sensitif\n"
                "- **Cardiaque** : tachycardie, arythmie, galop, OMI, signes d'IC droite/gauche\n"
                "- **Artériel périphérique** : asymétrie, abolition des pouls, souffle abdominal, masse abdominale battante, lésions cutanées ischémiques"
            )),
            FicheRow(concept="◆ Examen clinique — orientation vers HTA secondaire", detail_md=(
                "- Souffle précordial + abolition des pouls fémoraux → **coarctation aortique**\n"
                "- Souffle aortique abdominal → HTA rénovasculaire\n"
                "- Gros reins palpables → polykystose\n"
                "- Neurofibromatose cutanée → phéochromocytome\n"
                "- **Cushing** : vergetures pourpres et larges, érythrose faciale, amyotrophie proximale (signe du tabouret), bosse de bison, hirsutisme"
            )),
            FicheRow(concept="Évaluation de l'obésité viscérale", detail_md=(
                "- Poids, IMC\n"
                "- Périmètre abdominal en position debout"
            )),
            FicheRow(concept="", detail_md=(
                "- Hypokaliémie + HTA = penser **hyperaldostéronisme**\n"
                "- Triade de Ménard (céphalées + sueurs + palpitations) = penser **phéochromocytome**\n"
                "- Pouls fémoraux abolis = penser **coarctation aortique**"
            ), kind="mnemo"),
        ]),
        SousPartie(lettre="C", titre="Examens complémentaires et atteinte infraclinique", rows=[
            FicheRow(concept="◆ Bilan paraclinique systématique", detail_md=(
                "- Glycémie à jeun, **HbA1c**\n"
                "- Cholestérol total, HDL-C, triglycérides, calcul du LDL-C\n"
                "- Natrémie et kaliémie (éventuellement sans garrot)\n"
                "- Hémoglobine et hématocrite\n"
                "- **Créatininémie + DFG (CKD-EPI)**\n"
                "- Protéinurie sur échantillon : rapport protéinurie/créatininurie (idéalement matin)\n"
                "- **ECG de repos**"
            )),
            FicheRow(concept="Examens non systématiques (selon contexte)", detail_md=(
                "- Échocardiographie : si anomalies ECG ou symptômes (dyspnée)\n"
                "- IPS + échodoppler troncs supra-aortiques et MI : si souffle vasculaire / symptômes AOMI\n"
                "- Fond d'œil : si HTA grade 2/3 avec suspicion d'HTA maligne\n"
                "- β-hCG si suspicion de grossesse (CI de certains antihypertenseurs)"
            )),
            FicheRow(concept="◆ Anomalies ECG à rechercher", detail_md=(
                "- **HVG électrique** : indices de **Sokolow, Cornell, Lewis**\n"
                "  - ECG peu sensible : présence de signes = HVG marquée\n"
                "- Séquelle d'IDM passé inaperçu (non exceptionnel)\n"
                "- Anomalies de la repolarisation (ischémie ou HVG/surcharge)\n"
                "- Troubles du rythme, notamment **FA**\n"
                "- ECG initial normal sert de référence pour l'avenir"
            )),
            FicheRow(concept="Échocardiographie (atteinte cardiaque infraclinique)", detail_md=(
                "- À ne pas réaliser chez sujet asymptomatique avec ECG normal\n"
                "- Sensible pour dépister une HVG et prédire le risque CV\n"
                "- Améliore la stratification du risque (HVG concentrique ou remodelage concentrique)\n"
                "- Aide au choix thérapeutique"
            )),
            FicheRow(concept="◆ Définition échographique de l'HVG", detail_md=(
                "- **Masse VG > 115 g/m²** chez l'homme\n"
                "- **Masse VG > 95 g/m²** chez la femme\n"
                "- Ou remodelage concentrique du VG"
            )),
            FicheRow(concept="Apport de l'échocardiographie", detail_md=(
                "- Recherche d'**HVG** ou remodelage concentrique VG\n"
                "- Fonction VG : dysfonction systolique (cinétique segmentaire, FEVG globale) et/ou diastolique (remplissage ± dilatation OG)\n"
                "- Recherche d'anévrisme aorte ascendante / abdominale, coarctation, dilatation OG"
            )),
            FicheRow(concept="Atteinte vasculaire infraclinique", detail_md=(
                "- IPS + échodoppler des troncs supra-aortiques ou des artères MI\n"
                "- À ne pas réaliser chez sujet asymptomatique\n"
                "- Recherche de maladie athéromateuse → reclassifie le risque CV"
            )),
            FicheRow(concept="◆ Atteinte rénale infraclinique", detail_md=(
                "- ↑ créatinine ou ↓ clairance = ↓ DFG (CKD-EPI)\n"
                "- **IR si DFG < 60 mL/min/1,73 m²**\n"
                "- Protéinurie : rapport albuminurie/créatinurie (RAC)\n"
                "  - > 300 mg/g = protéinurie\n"
                "  - > 30 mg/g déjà pathologique\n"
                "- Microalbuminurie : recherche systématique uniquement chez le diabétique"
            )),
            FicheRow(concept="Fond d'œil", detail_md=(
                "- Recommandé en cas d'HTA grade 3\n"
                "- Stade 3 : hémorragies ou exsudats → risque CV accru\n"
                "- **Stade 4** : œdème papillaire → diagnostic d'**HTA maligne** (urgence)"
            )),
            FicheRow(concept="◆ Indications d'avis spécialisé d'emblée", detail_md=(
                "- HTA sévère d'emblée (grade 3)\n"
                "- HTA avant 40 ans (sauf si obésité → dépistage SAOS au préalable)\n"
                "- **HTA résistante**\n"
                "- Situations cliniques/biologiques évocatrices d'HTA secondaire (HTA + hypokaliémie)"
            )),
            FicheRow(concept="", detail_md=(
                "- Bilan minimal systématique : glycémie, bilan lipidique, iono, créat + DFG, protéinurie, ECG\n"
                "- HVG échographique : ♂ > 115 g/m², ♀ > 95 g/m²\n"
                "- Protéinurie pathologique > 300 mg/g (anormale dès 30 mg/g)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Stratification du risque et consultation d'annonce", rows=[
            FicheRow(concept="◆ Patients d'emblée à risque CV élevé", detail_md=(
                "- ATCD de maladie coronarienne, AVC, AIT, AOMI\n"
                "- Insuffisance cardiaque\n"
                "- IR modérée ou sévère\n"
                "- Atteinte d'organe cible cardiaque ou vasculaire\n"
                "- Hypercholestérolémie familiale"
            )),
            FicheRow(concept="Diabétiques hypertendus", detail_md=(
                "- La majorité est à risque CV élevé d'emblée\n"
                "- Pour les plus jeunes (40-69 ans) : calculer le **SCORE2-Diabetes** pour évaluer le risque à 10 ans\n"
                "- Adaptation des objectifs thérapeutiques"
            )),
            FicheRow(concept="Autres patients", detail_md=(
                "- Évaluation par les scores **SCORE2** ou **SCORE2-OP**\n"
                "- Score de risque sur 10 ans d'événement CV"
            )),
            FicheRow(concept="◆ Consultation d'annonce", detail_md=(
                "- Réalisée une fois l'HTA confirmée et le bilan initial fait\n"
                "- Informer sur la maladie et les risques de complications aiguës/chroniques\n"
                "- Expliquer les bénéfices du traitement sur la réduction du risque\n"
                "- Présenter les mesures thérapeutiques médicamenteuses et non médicamenteuses\n"
                "- Fixer les objectifs (dont la cible de PA)\n"
                "- Établir un plan de soins court et long terme\n"
                "- Recueillir le point de vue du patient → **décision médicale partagée**"
            )),
        ]),
    ])

    # ── PARTIE IV : TRAITEMENT ──
    partie_iv = Partie(numero="IV", titre="Traitement", sous_parties=[
        SousPartie(lettre="A", titre="Stratégie thérapeutique et cibles", rows=[
            FicheRow(concept="◆ Objectif principal du traitement", detail_md=(
                "- Réduire la mortalité CV et rénale sur le long terme\n"
                "- Bénéfices documentés :\n"
                "  - **AVC** : -20-30 %\n"
                "  - **SCA et IC** : -10-20 %\n"
                "- Aucune limite d'âge pour envisager un traitement antihypertenseur"
            )),
            FicheRow(concept="◆ 4 piliers du traitement", detail_md=(
                "- Mesures hygiénodiététiques\n"
                "- Traitement des FdR associés\n"
                "- Traitement médicamenteux\n"
                "- Éducation thérapeutique\n"
                "- Consultation mensuelle jusqu'à atteinte de la cible (idéalement à 3 mois)"
            )),
            FicheRow(concept="◆ Cible tensionnelle ESC 2024", detail_md=(
                "- **PAS 120-129** et **PAD 70-79 mmHg** pour tous les hypertendus\n"
                "- Cible idéale 120/70 mmHg si possible\n"
                "- À adapter d'emblée si : hypotension orthostatique, fragilité, âge > 85 ans avec espérance de vie limitée\n"
                "- Si impossibilité : viser **< 140/90 mmHg**"
            )),
            FicheRow(concept="◆ Stratégie selon le niveau de PA", detail_md=(
                "| Situation | RHD | Traitement médicamenteux |\n"
                "|-----------|-----|--------------------------|\n"
                "| PAS 120-129 | Oui | Non |\n"
                "| PAS 130-139 sans risque CV élevé | Oui | Non, surveillance annuelle |\n"
                "| PAS 130-139 avec risque CV élevé | Oui | Après **3 mois de RHD** si cible non atteinte |\n"
                "| HTA confirmée | Oui | **Oui, immédiat** chez tous |"
            )),
        ]),
        SousPartie(lettre="B", titre="Mesures hygiénodiététiques", rows=[
            FicheRow(concept="◆ Effet attendu", detail_md=(
                "- Réduction moyenne de la **PAS de 5 à 10 mmHg**\n"
                "- Contrôle d'autres FdR / pathologies\n"
                "- Réduction du nombre et de la dose des antihypertenseurs\n"
                "- Initiées chez **TOUS** les patients avec PA élevée ou HTA"
            )),
            FicheRow(concept="◆ Activité physique", detail_md=(
                "- Régulière, adaptée aux possibilités du patient\n"
                "- Combiner aérobie (endurance) + résistance dynamique (squat, pompes) et/ou isométrique (planche, chaise)\n"
                "- Éviter la sédentarité"
            )),
            FicheRow(concept="◆ Poids et alcool", detail_md=(
                "- Perte de poids si surcharge : cible **IMC 20-25 kg/m²**\n"
                "- Périmètre abdominal : **< 94 cm ♂**, **< 80 cm ♀**\n"
                "- Alcool : suppression ou réduction, cible **< 10 unités / semaine**"
            )),
            FicheRow(concept="◆ Sel et potassium", detail_md=(
                "- Apport sodé : cible **5-6 g de sel/jour** = natriurèse 24h ~ 100 mmol/j\n"
                "  - Rappel : 1 g NaCl = 17 mmol Na\n"
                "- Augmenter le potassium : substituts de sel ou fruits et légumes\n"
                "  - Sauf si maladie rénale chronique avancée"
            )),
            FicheRow(concept="Tabac et alimentation", detail_md=(
                "- **Arrêt du tabagisme**\n"
                "- Alimentation de type méditerranéen : F&L, peu de graisses saturées\n"
                "- Limiter sucre et boissons sucrées (sodas, jus de fruit)\n"
                "- Café non limité (boissons taurine + caféine déconseillées)"
            )),
            FicheRow(concept="", detail_md=(
                "- Sel : **5-6 g/j** (natriurèse ~100 mmol/j)\n"
                "- IMC cible 20-25, périmètre < 94 cm ♂ / < 80 cm ♀\n"
                "- Alcool < 10 unités/semaine, arrêt tabac, type méditerranéen"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Traitement médicamenteux", rows=[
            FicheRow(concept="◆ 5 classes thérapeutiques avec preuves d'efficacité", detail_md=(
                "- **Inhibiteurs calciques (IC)** : dihydropyridine ou non dihydropyridine\n"
                "- **IEC** (inhibiteurs de l'enzyme de conversion)\n"
                "- **ARA2** (antagonistes des récepteurs à l'angiotensine 2)\n"
                "- **Bêtabloquants**\n"
                "- **Diurétiques thiazidiques** ou apparentés (indapamide)\n"
                "- Réduction de la mortalité et morbidité CV : AVC, SCA, IC"
            )),
            FicheRow(concept="◆ Particularités des bêtabloquants", detail_md=(
                "- Moins efficaces que les 4 autres classes pour la prévention des AVC\n"
                "- Persistance (poursuite du traitement) :\n"
                "  - Meilleure : ARA2, IEC\n"
                "  - Moindre : IC\n"
                "  - Plus faible : diurétiques thiazidiques et bêtabloquants"
            )),
            FicheRow(concept="◆ Bithérapie d'emblée — règle générale", detail_md=(
                "- Sauf cas particulier, **bithérapie d'emblée** recommandée\n"
                "- Faible dose en association fixe (2 principes dans 1 comprimé) en monoprise quotidienne\n"
                "- Choisir des molécules à demi-vie longue\n"
                "- Bithérapie basée sur 4 classes : IEC, ARA2, diurétique thiazidique, IC"
            )),
            FicheRow(concept="◆ Associations recommandées", detail_md=(
                "- **IEC ou ARA2 + IC dihydropyridine**\n"
                "- **IEC ou ARA2 + diurétique thiazidique** (ou apparenté)\n"
                "- **Ne jamais associer IEC + ARA2**\n"
                "- Bloqueur du SRAA (IEC ou ARA2) dès le début\n"
                "- Bêtabloquants non utilisés à l'initiation sauf autre indication"
            )),
            FicheRow(concept="◆ Monothérapie initiale — indications", detail_md=(
                "- PA élevée (120-139/70-89) avec indication de traitement pharmacologique\n"
                "- Fragilité modérée ou sévère\n"
                "- Hypotension orthostatique avant initiation\n"
                "- **Âge ≥ 85 ans**\n"
                "- Choix : IEC, ARA2, diurétique thiazidique, IC dihydropyridine\n"
                "- Pas de bêtabloquant en monothérapie"
            )),
            FicheRow(concept="◆ Comorbidités orientant le choix", detail_md=(
                "| Comorbidité | Classe(s) à privilégier |\n"
                "|-------------|--------------------------|\n"
                "| Diabète + microalbuminurie / IR | **IEC ou ARA2** (+ SGLT2) |\n"
                "| IR ± protéinurie | **IEC ou ARA2** |\n"
                "| ATCD AVC | **IC** |\n"
                "| ATCD IDM / angor | **BB** (et autres selon contexte) |\n"
                "| IC à FEVG altérée | **IEC** (ou ARA2) + **BB** + **diurétique** |"
            )),
            FicheRow(concept="⚠ Contre-indications des antihypertenseurs", detail_md=(
                "| Classe | CI absolues | CI relatives |\n"
                "|--------|-------------|--------------|\n"
                "| **Thiazidiques** | Hypercalcémie, hypokaliémie, goutte, grossesse | — |\n"
                "| **Bêtabloquants** | Asthme, BAV 2 et 3 | Bradycardie, Raynaud |\n"
                "| **IC dihydropyridines** | IC non contrôlée | — |\n"
                "| **IC non dihydropyridines** | BAV 2 et 3, IC à FEVG altérée | Bradycardie, troubles de conduction |\n"
                "| **IEC** | Grossesse, œdème angioneurotique sous IEC | Hyperkaliémie, femme en âge de procréer sans contraception, sténose bilatérale des artères rénales, IR sévère |\n"
                "| **ARA2** | Grossesse | Hyperkaliémie, femme sans contraception, sténose bilatérale des artères rénales, IR sévère |"
            )),
            FicheRow(concept="◆ Effets indésirables des antihypertenseurs", detail_md=(
                "| Classe | Effets indésirables fréquents |\n"
                "|--------|-------------------------------|\n"
                "| **Diurétiques thiazidiques** | Hypokaliémie, hyponatrémie, hyperglycémie, hyperuricémie, IR fonctionnelle |\n"
                "| **Bêtabloquants** | Asthénie, bradycardie, acrosyndrome, hypoglycémie, dysfonction érectile, prise de poids |\n"
                "| **IC dihydropyridines** | OMI, céphalées, vertiges, flushs |\n"
                "| **IC non dihydropyridines** | Bradycardie, troubles de conduction, constipation, OMI, céphalées |\n"
                "| **IEC** | Toux, hyperkaliémie, IR fonctionnelle |\n"
                "| **ARA2** | Hyperkaliémie, IR fonctionnelle |"
            )),
            FicheRow(concept="", detail_md=(
                "- **Jamais IEC + ARA2** (double blocage du SRAA = risque hyperkaliémie + IR)\n"
                "- Pas de bêtabloquant en monothérapie ni en initiation sauf autre indication\n"
                "- Thiazidiques contre-indiqués si goutte (hyperuricémie)\n"
                "- IEC/ARA2 contre-indiqués pendant la **grossesse**"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Sujet âgé et éducation thérapeutique", rows=[
            FicheRow(concept="◆ Évaluation du sujet âgé", detail_md=(
                "- L'âge seul ne suffit pas à guider le traitement\n"
                "- Rechercher : fragilité modérée/sévère et arguments pour espérance de vie limitée\n"
                "- Risque d'**hypotension orthostatique** systématiquement dépisté\n"
                "- Risque de iatrogénie majoré"
            )),
            FicheRow(concept="Sujets < 85 ans non fragiles", detail_md=(
                "- Sans facteurs limitant l'espérance de vie\n"
                "- Pas d'indication à adapter la prise en charge"
            )),
            FicheRow(concept="Patient hypertendu traité atteignant 85 ans", detail_md=(
                "- Pas d'indication systématique à arrêter ou diminuer le traitement\n"
                "- Si bien toléré cliniquement et paracliniquement → poursuite"
            )),
            FicheRow(concept="◆ Patients à adapter (≥ 1 critère)", detail_md=(
                "- Fragilité modérée ou sévère\n"
                "- **Âge ≥ 85 ans**\n"
                "- **Espérance de vie < 3 ans**"
            )),
            FicheRow(concept="◆ Adaptations chez le sujet âgé fragile", detail_md=(
                "- **Initier en monothérapie**\n"
                "- 1re intention : IC dihydropyridines et/ou IEC/ARA2\n"
                "- 2e intention : diurétiques thiazidiques à faible dose\n"
                "- Éviter bêtabloquants (sauf autre indication) et alphabloquants\n"
                "- **Ne pas dépasser une trithérapie**\n"
                "- Cible de PA individualisée : adaptée à la tolérance, absence d'hypotension orthostatique"
            )),
            FicheRow(concept="◆ Éducation thérapeutique", detail_md=(
                "- Promotion de l'AMT (règle des 3)\n"
                "- Facilitation de l'observance (piluliers, adaptation des horaires)\n"
                "- **Arrêt transitoire** de certains traitements si risque d'hypovolémie (diarrhée, vomissements, déshydratation, fièvre, canicule) :\n"
                "  - Diurétiques, IEC, ARA2 surtout chez le sujet âgé\n"
                "  - Bilan : ionogramme + créatinine + DFG\n"
                "- Renforcement des messages de la consultation d'annonce\n"
                "- ETP spécifique sur le tabac, l'alcool, l'alimentation, l'activité physique"
            )),
            FicheRow(concept="Surveillance des traitements", detail_md=(
                "- AMT 1 mois après chaque adaptation et avant chaque consultation de suivi\n"
                "- Après chaque ajustement d'IEC/ARA2 ou diurétique : ionogramme + créatinine + DFGe\n"
                "- Recherche d'hypotension orthostatique (sujet âgé, IR, diabétique)\n"
                "- Recherche d'effets indésirables → changement de molécule si besoin\n"
                "- En cas de mauvaise tolérance : adapter la cible (la plus basse tolérée)"
            )),
            FicheRow(concept="◆ Conduite si objectif non atteint à 1 mois", detail_md=(
                "- Évaluer et renforcer l'adhésion aux RHD\n"
                "- Évaluer et renforcer l'observance médicamenteuse\n"
                "- **Majoration : passer en trithérapie** (IEC/ARA2 + IC + diurétique thiazidique) avant de majorer les doses\n"
                "- Revoir le patient à 1 mois avec une AMT"
            )),
        ]),
    ])

    # ── PARTIE V : SUIVI DU PATIENT HYPERTENDU ET HTA RÉSISTANTE ──
    partie_v = Partie(numero="V", titre="Suivi du patient hypertendu et HTA résistante", sous_parties=[
        SousPartie(lettre="A", titre="Cible atteinte", rows=[
            FicheRow(concept="◆ Rythme des consultations", detail_md=(
                "- Patients à faible risque ou HTA grade 1 : consultation tous les 6 mois\n"
                "- Patients à risque CV élevé ou sous RHD seules : consultation tous les 3 mois"
            )),
            FicheRow(concept="◆ Objectifs de la consultation de suivi", detail_md=(
                "- Rechercher des symptômes\n"
                "- Vérifier l'équilibre tensionnel (cabinet + AMT/MAPA)\n"
                "- Évaluer observance et tolérance du traitement\n"
                "- S'assurer du contrôle des FdR et de l'adhésion aux RHD\n"
                "- Rechercher une **hypotension orthostatique** (diabète, Parkinson, sujet âgé)"
            )),
            FicheRow(concept="◆ Surveillance paraclinique", detail_md=(
                "- Biologie annuelle : natrémie, kaliémie, créatininémie, protéinurie\n"
                "  - Plus fréquente chez le sujet âgé\n"
                "- En l'absence de diabète/dyslipidémie : glycémie à jeun + bilan lipidique tous les 3 ans\n"
                "- ECG tous les 3 à 5 ans en l'absence de cardiopathie ou symptômes cardiaques"
            )),
            FicheRow(concept="Adaptation du traitement", detail_md=(
                "- Hypotension orthostatique et/ou fragilité apparue\n"
                "- Interactions médicamenteuses : bradycardisants + BB, **AINS + IEC/ARA2**"
            )),
        ]),
        SousPartie(lettre="B", titre="Cible non atteinte et HTA résistante", rows=[
            FicheRow(concept="◆ CAT si cible non atteinte sous trithérapie", detail_md=(
                "- Vérifier l'équilibre par AMT ou MAPA\n"
                "- Réévaluer observance et tolérance\n"
                "- Rechercher des facteurs de résistance : sel excessif, prise de poids, alcool, dépression, médicaments hypertensiogènes (AINS, corticoïdes, vasoconstricteurs, œstrogènes), cannabis, cocaïne, amphétamines, SAOS\n"
                "- Vérifier que la trithérapie est optimale : IEC/ARA2 + IC + diurétique thiazidique tous à doses optimales\n"
                "- HTA résistante évoquée **uniquement si diurétique thiazidique** dans la trithérapie"
            )),
            FicheRow(concept="★ ◆ Définition de l'HTA résistante", detail_md=(
                "- Persistance de valeurs de PA supérieures à la cible\n"
                "- Malgré mesures hygiénodiététiques\n"
                "- ET **≥ 3 classes médicamenteuses** dont un **diurétique thiazidique** ou apparenté\n"
                "- Tous à dose optimale\n"
                "- AMT (et souvent MAPA) doivent confirmer les chiffres"
            )),
            FicheRow(concept="◆ HTA faussement résistante à éliminer", detail_md=(
                "- HTA blouse blanche, brassard inadapté\n"
                "- Doses insuffisantes des antihypertenseurs, absence de diurétique\n"
                "- Mauvaise observance\n"
                "- RHD non suivies : sel excessif, prise de poids, alcool"
            )),
            FicheRow(concept="★ Causes d'HTA résistante à rechercher", detail_md=(
                "- Médicaments ou substances hypertensiogènes\n"
                "- **SAOS**\n"
                "- HTA secondaire méconnue\n"
                "- Surcharge volémique : traitement diurétique insuffisant, IR"
            )),
            FicheRow(concept="◆ Traitement après bilan d'HTA résistante", detail_md=(
                "- En l'absence de cause spécifique :\n"
                "  - Ajouter un antagoniste des récepteurs aux minéralocorticoïdes :\n"
                "    - **Spironolactone** en 1re intention\n"
                "    - **Éplérénone** si spironolactone mal tolérée\n"
                "  - Puis bêtabloquant (s'il n'était pas déjà prescrit)\n"
                "  - Éventuellement alphabloquants, antihypertenseurs centraux\n"
                "  - Dans certains cas : dénervation rénale à discuter"
            )),
            FicheRow(concept="", detail_md=(
                "- HTA résistante = trithérapie incluant **un diurétique** à dose optimale\n"
                "- Sans diurétique → on ne peut pas parler d'HTA résistante\n"
                "- 1re intention en plus de la trithérapie : **spironolactone**"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE VI : HTA SECONDAIRE ──
    partie_vi = Partie(numero="VI", titre="HTA secondaire", sous_parties=[
        SousPartie(lettre="A", titre="Dépistage et bilan", rows=[
            FicheRow(concept="★ ◆ Indications du dépistage d'une HTA secondaire", detail_md=(
                "- HTA sévère : PA > 180/110 mmHg, apparition brutale ou aggravation rapide\n"
                "- **HTA résistante**\n"
                "- **Âge ≤ 40 ans**\n"
                "- **HTA + hypokaliémie**\n"
                "- Autre point d'appel : interrogatoire, examen clinique, biologie"
            )),
            FicheRow(concept="Recours à un avis spécialisé", detail_md=(
                "- Recommandé pour réaliser les explorations complémentaires\n"
                "- Bilan adapté aux points d'appel identifiés"
            )),
            FicheRow(concept="◆ Bilan paraclinique d'HTA secondaire", detail_md=(
                "- Polygraphie ventilatoire nocturne (SAOS)\n"
                "- Échographie rénale + échodoppler artères rénales (néphropathie, sténose)\n"
                "- Angioscanner abdominal (néphropathie, lésion surrénalienne, sténose)\n"
                "- Recueil urinaire 24h : natriurèse, kaliurèse, créatininurie, protéinurie, **dérivés méthoxylés des catécholamines**, **cortisol libre**, aldostéronurie\n"
                "- Dosages hormonaux sanguins : **rénine + aldostérone** (conditions de prélèvement spécifiques), dérivés méthoxylés plasmatiques, test de freinage minute (suspicion d'hypercorticisme)"
            )),
        ]),
        SousPartie(lettre="B", titre="Causes rénales et rénovasculaires", rows=[
            FicheRow(concept="◆ Néphropathies parenchymateuses", detail_md=(
                "- **Glomérulopathies chroniques** et **polykystose rénale** = causes rénales les plus fréquentes d'HTA secondaire\n"
                "- Diagnostic évoqué chez adolescent ou adulte jeune\n"
                "- Masses abdominales bilatérales à la palpation → polykystose\n"
                "- Protéinurie, hématurie, IR orientent\n"
                "- Échographie abdominale : taille des reins, contours, épaisseur corticale, obstacle, tumeurs\n"
                "- Prise en charge adaptée au type de néphropathie"
            )),
            FicheRow(concept="★ ◆ HTA rénovasculaire — 2 causes principales", detail_md=(
                "- **Sténose athéromateuse** des artères rénales (la plus fréquente)\n"
                "  - Touche ostium et tiers proximal de l'artère\n"
                "  - Autre localisation athéromateuse ou FdR fréquemment associés\n"
                "- **Dysplasie fibromusculaire** (plus rare)\n"
                "  - Touche la femme jeune\n"
                "  - Deux tiers distaux de l'artère"
            )),
            FicheRow(concept="◆ Présentation clinique de l'HTA rénovasculaire", detail_md=(
                "- Souffle abdominal latéralisé\n"
                "- OAP récidivant sans cause cardiaque\n"
                "- Hypokaliémie + hyperaldostéronisme secondaire (↑ rénine et aldostérone plasmatiques)\n"
                "- IR, parfois après introduction d'IEC/ARA2\n"
                "- Diminution de la taille du rein concerné\n"
                "- Confirmation : échodoppler artères rénales + angioscanner abdominal"
            )),
            FicheRow(concept="Traitement de l'HTA rénovasculaire", detail_md=(
                "- RHD + aspirine + statine (si athéromateuse) + antihypertenseurs\n"
                "- **Sténose athéromateuse** : revascularisation par angioplastie avec endoprothèse si :\n"
                "  - HTA résistante, dégradation de la fonction rénale, protéinurie importante\n"
                "  - Et rein suffisamment fonctionnel\n"
                "- **Fibrodysplasie** : angioplastie sans endoprothèse plus largement utilisée"
            )),
        ]),
        SousPartie(lettre="C", titre="Causes endocriniennes", rows=[
            FicheRow(concept="◆ Phéochromocytome — généralités", detail_md=(
                "- Tumeur rare de la médullosurrénale, le plus souvent bénigne\n"
                "- Sécrétion par pics de catécholamines\n"
                "- **HTA dans 70 % des cas**\n"
                "- Contextes familiaux : **NEM2**, von Hippel-Lindau, neurofibromatose 1, paragangliomes familiaux"
            )),
            FicheRow(concept="◆ Présentation du phéochromocytome", detail_md=(
                "- HTA permanente ou paroxystique\n"
                "- En cas de paroxysmes : **triade de Ménard** (céphalées + sueurs + palpitations)\n"
                "- Troubles du rythme possibles\n"
                "- Parfois révélé par une cardiomyopathie de stress"
            )),
            FicheRow(concept="◆ Diagnostic et traitement du phéochromocytome", detail_md=(
                "- **Diagnostic** : dosage urinaire et/ou sanguin des **dérivés méthoxylés des catécholamines** (métanéphrines et normétanéphrines)\n"
                "- **Localisation** : scanner + scintigraphie à la **MIBG**\n"
                "  - Localise tumeur (parfois extrasurrénalienne)\n"
                "  - Confirmation fonctionnelle\n"
                "- **Traitement** : exérèse chirurgicale de la tumeur\n"
                "  - Préparation par α-bloquants à petites doses puis bêtabloquants\n"
                "  - Limite les complications opératoires (poussée hypertensive, déplétion volémique)"
            )),
            FicheRow(concept="◆ Hyperaldostéronisme primaire (Conn)", detail_md=(
                "- Adénome surrénalien : 30 % (adénome de Conn)\n"
                "- Hyperplasie bilatérale des surrénales : 70 %\n"
                "- Rarement : corticosurrénalome malin\n"
                "- Évoqué chez l'hypertendu avec **hypokaliémie < 3,7 mmol/L** (non systématique)\n"
                "- HTA sévère, résistante, du sujet jeune, atteinte d'organes cibles disproportionnée, nodule surrénalien fortuit"
            )),
            FicheRow(concept="◆ Diagnostic biologique du Conn", detail_md=(
                "- **↑ aldostéronémie**, **↓ rénine plasmatique**\n"
                "- Rapport aldostérone/rénine très élevé\n"
                "- Conditions de prélèvement : matin, 2h après le lever, normokaliémie, apports sodés larges\n"
                "- Arrêt des antagonistes des récepteurs aux minéralocorticoïdes depuis **6 semaines**\n"
                "- Arrêt des IEC, ARA2, diurétiques et β-bloquants depuis **2 semaines**"
            )),
            FicheRow(concept="Imagerie et traitement du Conn", detail_md=(
                "- Scanner : lésion unilatérale (adénome ou incidentalome) ou hyperplasie bilatérale\n"
                "- Cathétérisme des veines surrénaliennes si lésion unilatérale et patient demandeur de chirurgie → confirme la latéralisation\n"
                "- **Traitement** :\n"
                "  - Lésion unilatérale + chirurgie souhaitée : surrénalectomie\n"
                "  - Autres cas : **spironolactone** en 1re intention"
            )),
            FicheRow(concept="Autres étiologies endocriniennes", detail_md=(
                "- Syndrome de Cushing (hypercortisolisme)\n"
                "- Acromégalie\n"
                "- Hyperthyroïdie"
            )),
        ]),
        SousPartie(lettre="D", titre="Coarctation, SAOS, iatrogénie", rows=[
            FicheRow(concept="◆ Coarctation aortique", detail_md=(
                "- Observée chez enfant et adulte jeune\n"
                "- Fermeture anormale du canal artériel → sténose au niveau de l'isthme aortique\n"
                "- **Clinique** :\n"
                "  - Souffle mésosystolique parasternal gauche et dans le dos\n"
                "  - **Pouls fémoraux absents**\n"
                "  - HTA aux MS + PA basse aux MI\n"
                "- Diagnostic : échocardiographie + IRM\n"
                "- Traitement : chirurgical ou endoluminal (dilatation + endoprothèse)"
            )),
            FicheRow(concept="◆ Syndrome d'apnées du sommeil (SAOS)", detail_md=(
                "- Évoqué chez patients obèses, surtout si HTA résistante\n"
                "- Patients \"non dippers\" (absence de baisse nocturne de la PA en MAPA)\n"
                "- **Diagnostic** : polygraphie ou polysomnographie ventilatoire nocturne\n"
                "- **Traitement** : **PPC** (masque de pression positive nocturne)"
            )),
            FicheRow(concept="◆ Médicaments / substances augmentant la PA", detail_md=(
                "- Antiangiogéniques\n"
                "- Alcool\n"
                "- Ciclosporine, tacrolimus\n"
                "- Cocaïne, amphétamines\n"
                "- Contraceptifs oraux\n"
                "- Corticoïdes\n"
                "- Érythropoïétine\n"
                "- Herbes (ephedra, ma huang)\n"
                "- IRSN (inhibiteurs recapture sérotonine-noradrénaline)\n"
                "- Réglisse, sympathomimétiques"
            )),
            FicheRow(concept="◆ Substances interférant avec les antihypertenseurs", detail_md=(
                "- **AINS**\n"
                "- Antirétroviraux\n"
                "- Inhibiteurs du CYP17A1 : jus de pamplemousse, macrolides, antifongiques azolés"
            )),
            FicheRow(concept="", detail_md=(
                "- **Polykystose** = masses abdominales bilatérales chez l'adulte jeune\n"
                "- **Dysplasie fibromusculaire** = femme jeune, tiers distaux des artères rénales\n"
                "- **Phéochromocytome** : 70 % d'HTA, triade de Ménard, métanéphrines urinaires + MIBG\n"
                "- **Conn** : hypokaliémie + aldostérone↑ / rénine↓\n"
                "- **Coarctation** : pouls fémoraux absents + HTA aux MS"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE VII : URGENCES HYPERTENSIVES ET HTA MALIGNE ──
    partie_vii = Partie(numero="VII", titre="Urgences hypertensives et HTA maligne", sous_parties=[
        SousPartie(lettre="A", titre="Urgence hypertensive", rows=[
            FicheRow(concept="⚠ Ne pas confondre urgence hypertensive et crise hypertensive", detail_md=(
                "- **Crise hypertensive** = HTA grade 3 SANS souffrance viscérale → n'est PAS une urgence\n"
                "- **Urgence hypertensive** = HTA (souvent sévère) + atteinte AIGUË des organes cibles\n"
                "- Pronostic vital engagé"
            )),
            FicheRow(concept="◆ Risque d'une baisse trop brutale", detail_md=(
                "- Anomalies de l'autorégulation de la PA chez l'hypertendu\n"
                "- Baisse trop rapide → hypoperfusion cérébrale, ischémie myocardique ou rénale\n"
                "- Traitement précoce mais chute progressive"
            )),
            FicheRow(concept="◆ Principales urgences hypertensives", detail_md=(
                "- HTA + SCA ST+ ou ST-\n"
                "- HTA + OAP (IVG aiguë)\n"
                "- HTA + dissection aortique\n"
                "- Encéphalopathie hypertensive (HTA + hypertension intracrânienne)\n"
                "- **PRES** (encéphalopathie postérieure réversible) : cécité centrale, lésions occipitales\n"
                "- HTA + hémorragie méningée ou AVC\n"
                "- HTA du phéochromocytome\n"
                "- HTA toxique : amphétamines, LSD, cocaïne, ecstasy\n"
                "- Prééclampsie sévère ou éclampsie → extraction fœtale en urgence"
            )),
            FicheRow(concept="◆ Diagnostic et examens", detail_md=(
                "- Diagnostic clinique : PA souvent **> 180/110 mmHg** + point d'appel d'atteinte viscérale\n"
                "- Biologie : créatinine, protéinurie, plaquettes, coagulation (CIVD), troponine, toxiques (cocaïne), NFS, schizocytes, bilirubine libre, haptoglobine, LDH\n"
                "- ECG : SCA\n"
                "- Radio thorax : surcharge (OAP)\n"
                "- Échocardiographie : fonction VG, cinétique, pressions de remplissage\n"
                "- Fond d'œil : occlusion veine centrale, rétinopathie stade 4\n"
                "- Scanner cérébral si suspicion hémorragie/AVC\n"
                "- Imagerie aortique (ETT, scanner, ETO) si suspicion de dissection"
            )),
            FicheRow(concept="◆ Prise en charge initiale", detail_md=(
                "- **Hospitalisation en USI** adaptée à la souffrance viscérale ou réanimation\n"
                "- Surveillance PA / 15 min\n"
                "- Si point d'appel neurologique : **scanner indispensable AVANT** traitement antihypertenseur\n"
                "- **Cas général** : baisse de PA de **20-25 % en 2 heures** pour atteindre **160/110 mmHg en 2 à 6 heures**\n"
                "- Éviter baisse brutale et hypotension (risque aggravation cérébrale, rénale, cardiaque)"
            )),
            FicheRow(concept="◆ Cas particuliers de PEC tensionnelle", detail_md=(
                "- **Dissection aortique** : objectif **PAS < 120 mmHg** le plus rapidement possible\n"
                "- **Hémorragie intracérébrale** (ESC 2024) : baisse immédiate de la PA dans les 6h, cible PAS 140-160 mmHg\n"
                "  - Éviter une baisse > 70 mmHg de PAS (risque d'IRA et de détérioration neurologique)\n"
                "- **AVC ischémique aigu sans reperfusion** : pas de baisse active sauf si PA > 220/120 mmHg → baisse modérée 10-15 % sur quelques heures\n"
                "- **AVC ischémique + thrombolyse IV** :\n"
                "  - PA < 185/110 mmHg avant traitement\n"
                "  - PA < 180/105 mmHg pendant 24h après traitement\n"
                "- **AVC ischémique + thrombectomie mécanique** : PA < 180/105 mmHg avant et 24h après"
            )),
            FicheRow(concept="◆ Traitements médicamenteux des urgences hypertensives", detail_md=(
                "- **1re intention (cas général)** : **uradipil IV** (alphabloquant) et/ou **nicardipine IV** (inhibiteur calcique)\n"
                "  - Nicardipine contre-indiquée dans l'insuffisance cardiaque\n"
                "- **Phéochromocytome** : **labétalol IV** (alpha + bêtabloquant)\n"
                "- **SCA / OAP** : **dérivés nitrés IV** en 1re intention\n"
                "- Après stabilisation et AVC ischémique aigu : si HTA persiste (≥ 140/90) ≥ 3 jours après → réintroduire ou initier un antihypertenseur"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant un point d'appel neurologique : **TDM cérébral AVANT** tout traitement antihypertenseur\n"
                "- **Dissection aortique** : PAS < 120 mmHg ASAP (à l'inverse du cas général)\n"
                "- AVC ischémique non thrombolysé : pas de baisse sauf > 220/120 mmHg"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="HTA maligne", rows=[
            FicheRow(concept="★ ◆ Définition de l'HTA maligne", detail_md=(
                "- Pas de valeur seuil mais souvent HTA grade 3\n"
                "- + **Œdème papillaire** au fond d'œil (rétinopathie stade 4)\n"
                "- Peut se compliquer d'atteintes d'organes cibles aiguës"
            )),
            FicheRow(concept="★ ◆ Complications de l'HTA maligne", detail_md=(
                "- **Cardiaques** : IVG, ischémie myocardique\n"
                "- **Rénales** : IRA avec élévation de la créatinine, protéinurie abondante, hématurie fréquente\n"
                "- **Neurologique** : PRES, encéphalopathie hypertensive, coma\n"
                "- **Microangiopathie thrombotique** : anémie hémolytique mécanique + thrombopénie"
            )),
            FicheRow(concept="Signes généraux associés", detail_md=(
                "- Asthénie, amaigrissement, altération de l'état général sur quelques semaines\n"
                "- Troubles digestifs : douleurs abdominales, nausées, vomissements\n"
                "- Soif et signes de déshydratation"
            )),
            FicheRow(concept="◆ Évolution sans traitement", detail_md=(
                "- Évolution particulièrement rapide\n"
                "- En quelques mois : **IR sévère irréversible et mortelle**\n"
                "- Urgence absolue de prise en charge"
            )),
            FicheRow(concept="", detail_md=(
                "- **HTA maligne** = HTA + œdème papillaire (FO stade 4) ± atteintes d'organes cibles aiguës\n"
                "- Évolue vers IR sévère irréversible et mortelle en quelques mois sans traitement\n"
                "- Microangiopathie thrombotique = anémie hémolytique mécanique + thrombopénie"
            ), kind="a_retenir"),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Définition de l'HTA selon la méthode de mesure", markdown=(
            "| Méthode | PA non élevée | PA élevée | HTA |\n"
            "|---------|---------------|-----------|-----|\n"
            "| **Consultation** | < 120 et < 70 | 120-139 et/ou 70-89 | ≥ 140 et/ou ≥ 90 |\n"
            "| **AMT** | < 120 et < 70 | 120-134 et/ou 70-84 | ≥ 135 et/ou ≥ 85 |\n"
            "| **MAPA 24h** | < 115 et < 65 | 115-130 et/ou 65-79 | ≥ 130 et/ou ≥ 80 |\n"
            "| **MAPA diurne** | < 120 et < 70 | 120-134 et/ou 70-84 | ≥ 135 et/ou ≥ 85 |\n"
            "| **MAPA nocturne** | < 110 et < 60 | 110-119 et/ou 60-69 | ≥ 120 et/ou ≥ 70 |"
        )),
        TableauSynthese(titre="Grades de l'HTA en consultation", markdown=(
            "| Grade | PAS (mmHg) | PAD (mmHg) | Délai de confirmation ambulatoire |\n"
            "|-------|-----------|------------|-----------------------------------|\n"
            "| **Grade 1** | 140-159 | et/ou 90-99 | Dans le mois |\n"
            "| **Grade 2** | 160-179 | et/ou 100-109 | Dans le mois |\n"
            "| **Grade 3** | ≥ 180 | et/ou ≥ 110 | Dans la semaine (rechercher urgence) |"
        )),
        TableauSynthese(titre="Comorbidités orientant le choix d'antihypertenseur", markdown=(
            "| Comorbidité | IEC | ARA2 | IC | BB | Diurétique |\n"
            "|-------------|-----|------|----|----|------------|\n"
            "| Diabète + microalbuminurie/IR | X | X | | | |\n"
            "| IR ± protéinurie | X | X | | | |\n"
            "| ATCD AVC | | | X | | |\n"
            "| ATCD IDM / angor | | | | X | |\n"
            "| IC à FEVG altérée | X | X (si intolérance IEC) | | X | X |"
        )),
        TableauSynthese(titre="Contre-indications des classes antihypertensives", markdown=(
            "| Classe | CI absolues | CI relatives |\n"
            "|--------|-------------|--------------|\n"
            "| **Thiazidiques** | Hypercalcémie, hypokaliémie, goutte, grossesse | — |\n"
            "| **Bêtabloquants** | Asthme, BAV 2-3 | Bradycardie, Raynaud |\n"
            "| **IC dihydropyridines** | IC non contrôlée | — |\n"
            "| **IC non dihydropyridines** | BAV 2-3, IC à FEVG altérée | Bradycardie, troubles de conduction |\n"
            "| **IEC** | Grossesse, œdème angioneurotique | Hyperkaliémie, sténose bilatérale des artères rénales, IR sévère |\n"
            "| **ARA2** | Grossesse | Hyperkaliémie, sténose bilatérale des artères rénales, IR sévère |"
        )),
        TableauSynthese(titre="Effets indésirables fréquents des antihypertenseurs", markdown=(
            "| Classe | Effets indésirables |\n"
            "|--------|---------------------|\n"
            "| **Diurétiques thiazidiques** | Hypokaliémie, hyponatrémie, hyperglycémie, hyperuricémie, IR fonctionnelle |\n"
            "| **Bêtabloquants** | Asthénie, bradycardie, acrosyndrome, hypoglycémie, dysfonction érectile, prise de poids |\n"
            "| **IC dihydropyridines** | OMI, céphalées, vertiges, flushs |\n"
            "| **IC non dihydropyridines** | Bradycardie, troubles de conduction, constipation, OMI, céphalées |\n"
            "| **IEC** | Toux, hyperkaliémie, IR fonctionnelle |\n"
            "| **ARA2** | Hyperkaliémie, IR fonctionnelle |"
        )),
        TableauSynthese(titre="Stratégie thérapeutique ESC 2024 selon le niveau de PA", markdown=(
            "| Situation | RHD | Médicaments |\n"
            "|-----------|-----|-------------|\n"
            "| PAS 120-129 | Oui | Non |\n"
            "| PAS 130-139 sans risque CV élevé | Oui | Non (surveillance annuelle) |\n"
            "| PAS 130-139 avec risque CV élevé | Oui | Après 3 mois de RHD si cible non atteinte |\n"
            "| HTA confirmée | Oui | Oui, immédiat |"
        )),
        TableauSynthese(titre="Urgences hypertensives — cibles tensionnelles particulières", markdown=(
            "| Situation | Cible / vitesse |\n"
            "|-----------|------------------|\n"
            "| **Cas général** | Baisse 20-25 % en 2h → 160/110 mmHg en 2-6h |\n"
            "| **Dissection aortique** | PAS < 120 mmHg ASAP |\n"
            "| **Hémorragie intracérébrale** | PAS 140-160 dans les 6h (éviter ↓ > 70 mmHg) |\n"
            "| **AVC ischémique sans reperfusion** | Pas de baisse sauf PA > 220/120 → -10-15 % |\n"
            "| **AVC + thrombolyse IV** | < 185/110 avant, < 180/105 pendant 24h |\n"
            "| **AVC + thrombectomie** | < 180/105 avant et 24h après |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Seuil HTA en consultation | ≥ 140/90 mmHg | Définition ESC 2024 |\n"
        "| Seuil HTA en AMT | ≥ 135/85 mmHg | Confirmation diagnostique |\n"
        "| Seuil HTA en MAPA 24h | ≥ 130/80 mmHg | Diagnostic alternatif |\n"
        "| Seuil HTA MAPA nocturne | ≥ 120/70 mmHg | Pronostic CV |\n"
        "| PA élevée en consultation | 120-139/70-89 mmHg | Catégorie ESC 2024 |\n"
        "| HTA grade 1 | 140-159/90-99 mmHg | — |\n"
        "| HTA grade 2 | 160-179/100-109 mmHg | — |\n"
        "| HTA grade 3 | ≥ 180/110 mmHg | Rechercher urgence |\n"
        "| Cible thérapeutique générale | 120-129/70-79 mmHg | Idéale 120/70 |\n"
        "| Cible si intolérance | < 140/90 mmHg | Plan B |\n"
        "| Hypotension orthostatique | ↓ ≥ 20 mmHg PAS et/ou ≥ 10 mmHg PAD | À 1 et/ou 3 min debout |\n"
        "| Pression pulsée (rigidité) | > 65 mmHg | Marqueur |\n"
        "| Règle des 3 (AMT) | 18 mesures | 3 × 3 × 3 jours |\n"
        "| Prévalence HTA en France | 30 % | 18-74 ans |\n"
        "| Hypertendus français | 17 millions | 2023 |\n"
        "| HTA blouse blanche | 15-20 % | Population adulte |\n"
        "| HTA masquée | 10-15 % | Population adulte |\n"
        "| HTA secondaire | 10 % | Toutes étiologies |\n"
        "| HTA essentielle | 90 % | — |\n"
        "| HTA familiale (essentielle) | 15 % | Forme polygénique |\n"
        "| Risque AVC chez l'hypertendu | × 7 | vs normotendu |\n"
        "| Risque IC chez l'hypertendu | × 4 | vs normotendu |\n"
        "| Risque insuf. coronarienne | × 3 | vs normotendu |\n"
        "| Risque AOMI | × 2 | vs normotendu |\n"
        "| Mortalité CV (homme) | × 5 | chez l'hypertendu |\n"
        "| Mortalité CV (femme) | × 3 | chez l'hypertendu |\n"
        "| FA chez l'hypertendu | 70 % | HTA = 1re cause |\n"
        "| Bénéfice traitement sur AVC | - 20-30 % | Méta-analyse |\n"
        "| Bénéfice traitement SCA/IC | - 10-20 % | — |\n"
        "| HVG échographique homme | > 115 g/m² | Masse VG |\n"
        "| HVG échographique femme | > 95 g/m² | Masse VG |\n"
        "| IR | DFG < 60 mL/min/1,73 m² | CKD-EPI |\n"
        "| Protéinurie pathologique | RAC > 300 mg/g | (>30 mg/g déjà anormal) |\n"
        "| Apport sodé cible | 5-6 g de sel/j | ~ 100 mmol Na/j |\n"
        "| IMC cible | 20-25 kg/m² | — |\n"
        "| Périmètre abdominal homme | < 94 cm | Position debout |\n"
        "| Périmètre abdominal femme | < 80 cm | Position debout |\n"
        "| Alcool cible | < 10 unités/semaine | — |\n"
        "| Diminution PAS attendue avec RHD | 5-10 mmHg | Bonne adhésion |\n"
        "| Phéochromocytome avec HTA | 70 % | — |\n"
        "| Conn - répartition adénome | 30 % | Adénome de Conn |\n"
        "| Conn - répartition hyperplasie | 70 % | Bilatérale |\n"
        "| Kaliémie évoquant Conn | < 3,7 mmol/L | Hypokaliémie |\n"
        "| Arrêt antagonistes minéralocorticoïdes avant dosage | 6 semaines | Conditions de prélèvement |\n"
        "| Arrêt IEC/ARA2/diurétiques/BB avant dosage | 2 semaines | Conditions de prélèvement |\n"
        "| Urgence hypertensive (cas général) | Baisse 20-25 % en 2h | Cible 160/110 en 2-6h |\n"
        "| Dissection aortique | PAS < 120 mmHg ASAP | À l'inverse du cas général |\n"
        "| Hémorragie intracérébrale | PAS 140-160 dans 6h | Éviter ↓ > 70 mmHg |\n"
        "| AVC ischémique sans reperfusion | Traiter si PA > 220/120 | Baisse 10-15 % |\n"
        "| AVC + thrombolyse IV | < 185/110 avant, < 180/105 pdt 24h | — |\n"
        "| Dépistage PA < 40 ans | Tous les 3 ans | ESC 2024 |\n"
        "| Dépistage PA ≥ 40 ans | Au moins 1 fois/an | ESC 2024 |"
    ))

    points_cles = [
        "HTA = consultation **≥ 140/90** ; confirmer par **AMT ≥ 135/85** ou **MAPA 24h ≥ 130/80**",
        "AMT **règle des 3** : 3 mesures × 2/j × 3 jours = **18 mesures**, moyenne des 2 dernières",
        "Grades : G1 140-159/90-99 ; G2 160-179/100-109 ; **G3 ≥ 180/110** → chercher urgence HT",
        "Bilan minimal : **glycémie, lipides, iono, créat + DFG, protéinurie, ECG**",
        "Cible : **PAS 120-129 / PAD 70-79** ; individualiser si ≥ 85 ans, fragile, EV < 3 ans",
        "RHD pour TOUS : **sel 5-6 g/j**, IMC 20-25, alcool < 10 U/sem, activité, arrêt tabac",
        "Bithérapie d'emblée : **IEC/ARA2 + IC** ou **+ thiazidique** ; **jamais IEC + ARA2**",
        "**HTA résistante** = trithérapie incluant **un diurétique** → ajouter **spironolactone**",
        "Dépister **HTA secondaire** si : sévère, < 40 ans, résistante, **hypokaliémie**, point d'appel",
        "**Urgence HT** = HTA + atteinte aiguë organe : USI, baisse 20-25 % en 2h → 160/110 en 2-6h",
    ]

    fiche_eclair_md = (
        "**Définition** : HTA = consultation ≥ 140/90 ; AMT ≥ 135/85 ; MAPA 24h ≥ 130/80. Mesure : ≥ 3 prises, moyenne des 2 dernières, repos > 5 min.\n\n"
        "**Confirmation** : AMT règle des 3 (18 mesures/3j) ou MAPA. Blouse blanche 15-20 % (RHD). Masquée 10-15 % (traiter).\n\n"
        "**Grades** : G1 140-159/90-99 ; G2 160-179/100-109 ; G3 ≥ 180/110 → rechercher urgence.\n\n"
        "**Épidémio** : 17 M en France, 25 % contrôlés. AVC ×7, IC ×4, SCA ×3. HTA = 1re cause de FA. 90 % essentielle / 10 % secondaire.\n\n"
        "**Bilan** : glycémie, lipides, iono, créat + DFG, protéinurie/créat, ECG. HVG : ♂ > 115, ♀ > 95 g/m².\n\n"
        "**Cible** : 120-129/70-79 mmHg. Individualiser si ≥ 85 ans, fragile, espérance < 3 ans.\n\n"
        "**RHD** : sel 5-6 g/j, IMC 20-25, périmètre < 94/80, alcool < 10 U/sem, activité physique, arrêt tabac.\n\n"
        "**Médicaments** : bithérapie d'emblée IEC/ARA2 + IC ou diurétique. Jamais IEC + ARA2. BB seulement si autre indication.\n\n"
        "**Résistante** : trithérapie + diurétique à dose optimale → ajouter spironolactone.\n\n"
        "**Secondaire** : rénovasculaire (athérome ostium / dysplasie fibromusculaire femme jeune), phéo (Ménard, métanéphrines, MIBG), Conn (hypoK + aldo↑/rénine↓), SAOS (PPC), coarctation (pouls fémoraux abolis).\n\n"
        "**Urgence HT** : HTA + atteinte aiguë organe cible. USI. Baisse 20-25 % en 2h → 160/110. Uradipil/nicardipine IV. TDM AVANT si neuro.\n\n"
        "**Cas particuliers** : dissection PAS < 120 ASAP ; AVC ischémique non thrombolysé si > 220/120 ; SCA/OAP nitrés IV.\n\n"
        "**HTA maligne** : HTA + œdème papillaire (FO stade 4). IR sévère mortelle si non traitée."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 224 - Hypertension artérielle de l'adulte et de l'enfant",
        annee="2025-2026",
        item="Item 224",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi, partie_vii],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 224",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-224_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

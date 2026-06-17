"""Génère la fiche de l'Item 222 - Facteurs de risque cardiovasculaire et prévention (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Définitions", sous_parties=[
            PlanSousPartie(lettre="A", titre="Facteur de risque vs marqueur de risque"),
            PlanSousPartie(lettre="B", titre="Prévention cardiovasculaire : individuelle et collective"),
        ]),
        PlanPartie(numero="II", titre="Facteurs de risque cardiovasculaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Facteurs non modifiables (âge, sexe, hérédité)"),
            PlanSousPartie(lettre="B", titre="Tabagisme"),
            PlanSousPartie(lettre="C", titre="Hypercholestérolémie"),
            PlanSousPartie(lettre="D", titre="Hypertension artérielle"),
            PlanSousPartie(lettre="E", titre="Diabète, syndrome métabolique, obésité"),
        ]),
        PlanPartie(numero="III", titre="Évaluation du risque cardiovasculaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Risque cardiovasculaire global et scores SCORE2"),
            PlanSousPartie(lettre="B", titre="Catégories de risque et place de l'IRC"),
            PlanSousPartie(lettre="C", titre="Autres éléments d'évaluation"),
        ]),
        PlanPartie(numero="IV", titre="Prévention secondaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Principes et acronyme BASIC"),
            PlanSousPartie(lettre="B", titre="Hypocholestérolémiant, PA, glycémie"),
            PlanSousPartie(lettre="C", titre="Sevrage tabagique, activité physique, enquête familiale"),
        ]),
        PlanPartie(numero="V", titre="Prévention primaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Stratégie selon le niveau de risque"),
            PlanSousPartie(lettre="B", titre="Pression artérielle et cholestérolémie"),
            PlanSousPartie(lettre="C", titre="Sevrage tabagique"),
            PlanSousPartie(lettre="D", titre="Alimentation et activité physique (PNNS)"),
        ]),
        PlanPartie(numero="VI", titre="Notions indispensables et inacceptables", sous_parties=[
            PlanSousPartie(lettre="A", titre="Notions indispensables"),
            PlanSousPartie(lettre="B", titre="Notions inacceptables"),
        ]),
    ]

    # ── PARTIE I : DÉFINITIONS ──
    partie_i = Partie(numero="I", titre="Définitions", sous_parties=[
        SousPartie(lettre="A", titre="Facteur de risque vs marqueur de risque", rows=[
            FicheRow(concept="◆ Facteur de risque", detail_md=(
                "- Définition : élément clinique ou biologique associé à une augmentation du risque "
                "de développer une maladie, avec une **relation de causalité** entre le facteur et la maladie\n"
                "- **5 critères de causalité** à réunir :\n"
                "  - le facteur précède la maladie\n"
                "  - relation dose-effet\n"
                "  - caractère universel\n"
                "  - plausibilité physiopathologique\n"
                "  - liaison forte et indépendante"
            )),
            FicheRow(concept="◆ Marqueur de risque", detail_md=(
                "- Pas de responsabilité causale démontrée dans la survenue de la maladie\n"
                "- Son taux varie en parallèle avec l'aggravation/amélioration de la maladie "
                "sans influencer son évolution\n"
                "- C'est un **simple témoin** de la maladie"
            )),
            FicheRow(concept="Conséquence pratique", detail_md=(
                "- Suppression/diminution d'un **facteur de risque** → baisse de l'incidence "
                "de la maladie ou de ses complications\n"
                "- Diminution d'un **marqueur** → ne modifie pas l'évolution de la maladie"
            )),
            FicheRow(concept="", detail_md=(
                "- **Facteur de risque** = cause modifiable de la maladie ; **marqueur** = simple témoin : "
                "ne pas confondre car les implications thérapeutiques sont radicalement différentes."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Prévention cardiovasculaire : individuelle et collective", rows=[
            FicheRow(concept="Définition de la prévention CV", detail_md=(
                "- Supprimer ou baisser au maximum l'ensemble des facteurs de risque "
                "afin de diminuer le risque de survenue d'événements cardiovasculaires\n"
                "- Peut s'appliquer spécifiquement à chaque individu (**prévention individuelle**) "
                "ou à l'ensemble de la population (**prévention collective**)"
            )),
            FicheRow(concept="Prévention individuelle", detail_md=(
                "- L'effet d'un programme de prévention est d'autant plus important que le risque "
                "de la maladie est élevé\n"
                "- Dépend pour chaque patient de son **risque cardiovasculaire global**\n"
                "- Calcul à partir de l'évaluation de l'ensemble des facteurs de risque"
            )),
            FicheRow(concept="Prévention collective", detail_md=(
                "- Mesures de prévention communautaires simples\n"
                "- Effets modérés individuellement mais impact important sur l'ensemble de "
                "la population, compte tenu du grand nombre d'individus bénéficiaires"
            )),
        ]),
    ])

    # ── PARTIE II : FACTEURS DE RISQUE CARDIOVASCULAIRE ──
    partie_ii = Partie(numero="II", titre="Facteurs de risque cardiovasculaire", sous_parties=[
        SousPartie(lettre="A", titre="Facteurs non modifiables (âge, sexe, hérédité)", rows=[
            FicheRow(concept="Cadre général", detail_md=(
                "- Les facteurs de risque sont multiples, ce qui fait de l'athérosclérose une "
                "**maladie plurifactorielle**\n"
                "- Classification : facteurs non modifiables vs facteurs modifiables"
            )),
            FicheRow(concept="Âge et sexe", detail_md=(
                "- Nombre absolu de décès CV plus important chez la femme (54 %) que chez l'homme\n"
                "- Avant **65 ans**, mortalité CV des hommes 3 à 4 fois supérieure à celle des femmes\n"
                "- En pratique, accidents CV en moyenne **10 ans plus tôt** chez l'homme "
                "que chez la femme"
            )),
            FicheRow(concept="◆ Hérédité", detail_md=(
                "- Évaluation reposant sur la notion d'événements précoces chez les parents/fratrie :\n"
                "  - **< 55 ans** chez les hommes\n"
                "  - **< 65 ans** chez les femmes\n"
                "- Peut être liée à :\n"
                "  - la transmission génétique de facteurs modifiables "
                "(hypercholestérolémie familiale, HTA, diabète, etc.)\n"
                "  - des facteurs environnementaux familiaux défavorables (tabagisme, "
                "alimentation déséquilibrée, sédentarité)"
            )),
            FicheRow(concept="Étude Interheart : 9 facteurs = 90 % des IDM", detail_md=(
                "- Étude cas-témoins d'IDM incluant toutes les régions du monde\n"
                "- **9 facteurs expliquent 90 % des IDM**, dans toutes les classes d'âge et "
                "les 2 sexes\n"
                "- **6 FDR** : tabagisme, hypercholestérolémie, HTA, diabète, "
                "obésité abdominale, facteurs psychosociaux\n"
                "- Facteurs « protecteurs » : fruits/légumes, activité physique, "
                "consommation légère d'alcool"
            )),
        ]),
        SousPartie(lettre="B", titre="Tabagisme", rows=[
            FicheRow(concept="◆ Première cause de mortalité évitable", detail_md=(
                "- **5 millions de décès/an** dans le monde, soit 13 500 décès/jour\n"
                "- Responsable de 1 décès sur 5 chez les hommes, 1 sur 20 chez les femmes\n"
                "- En France : **73 000 décès/an** (> 10 % de la totalité des décès), dont "
                "~2 000 par tabagisme passif\n"
                "- 1/4 de ces décès sont des décès cardiovasculaires"
            )),
            FicheRow(concept="◆ Mécanismes physiopathologiques", detail_md=(
                "- Abaissement du **HDL-cholestérol** → facilitation des lésions athéroscléreuses\n"
                "- Majoration du risque thrombotique : ↑ agrégation plaquettaire, ↑ fibrinogène, "
                "↑ viscosité sanguine\n"
                "- Altération de la vasomotricité endothélium-dépendante → spasme coronarien\n"
                "- Augmentation du CO circulant → altération du transport d'oxygène par "
                "l'hémoglobine"
            )),
            FicheRow(concept="Rôle de la nicotine", detail_md=(
                "- Pas de rôle spécifique dans les complications cardiovasculaires du tabagisme\n"
                "- Essentiellement responsable de la **dépendance**\n"
                "- Effets hémodynamiques mineurs (FC, PAS) par stimulation adrénergique, "
                "absents avec les substituts nicotiniques quelles que soient la dose et la voie"
            )),
            FicheRow(concept="Données Interheart sur le tabagisme", detail_md=(
                "- **2e FDR d'IDM** (juste derrière les dyslipidémies)\n"
                "- Risque proportionnel à la consommation, **pas de seuil** sans risque "
                "(effet-dose non linéaire)\n"
                "- Risque identique quel que soit le type : cigarettes avec/sans filtre, pipe, "
                "cigare, narguilé, tabac à mâcher\n"
                "- Part attribuable d'autant plus importante que les sujets sont jeunes "
                "(facteur essentiel et souvent isolé des accidents coronariens aigus du sujet jeune)"
            )),
            FicheRow(concept="◆ Tabagisme passif", detail_md=(
                "- **+24 %** de risque d'IDM pour une exposition de 1 à 7 h/semaine\n"
                "- **+62 %** de risque pour une exposition > 22 h/semaine"
            )),
            FicheRow(concept="Autres atteintes athéromateuses", detail_md=(
                "- Rôle majeur dans la survenue et l'évolution de l'**AOMI** : "
                "90 % des patients sont fumeurs\n"
                "- Risque significativement augmenté d'**anévrisme de l'aorte abdominale**\n"
                "- Corrélation entre consommation de tabac et risque d'**AVC** (homme et femme)"
            )),
            FicheRow(concept="", detail_md=(
                "- **Pas de seuil** de tabagisme sans risque. Même une exposition très faible "
                "(tabagisme passif léger) augmente significativement le risque d'IDM."
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Hypercholestérolémie (cf. item 223)", rows=[
            FicheRow(concept="◆ Facteur de risque coronarien majeur", detail_md=(
                "- **FDR le plus important** pour la maladie coronarienne\n"
                "- Cholestérolémie totale corrélée positivement et de façon exponentielle "
                "avec le risque coronarien"
            )),
            FicheRow(concept="◆ LDL-cholestérol = facteur déterminant", detail_md=(
                "- Au niveau individuel, niveau élevé de **LDL-C** = facteur déterminant du risque "
                "(« mauvais » cholestérol)\n"
                "- Niveau bas d'**HDL-C** = facteur de risque indépendant\n"
                "- Niveau élevé d'HDL-C = protecteur (non valable pour des valeurs > 1 g/L) "
                "(« bon » cholestérol)"
            )),
            FicheRow(concept="◆ Exploration d'une anomalie lipidique (EAL)", detail_md=(
                "- À réaliser **à jeun**\n"
                "- Comprend : cholestérol total (CT), HDL-C, triglycérides (TG)\n"
                "- LDL-C calculé par la **formule de Friedewald** :\n"
                "  - **LDL-C (g/L) = CT − HDL-C − TG/5**\n"
                "  - Valable uniquement si **TG < 3,5 g/L**"
            )),
            FicheRow(concept="Hypercholestérolémie familiale hétérozygote", detail_md=(
                "- Fréquence : **1 individu/500**\n"
                "- Mutation : LDL-récepteur (surtout), apoB ou PCSK9 (rare)\n"
                "- **LDL-C entre 2 et 4 g/L**\n"
                "- Dépôts cliniques évocateurs :\n"
                "  - **Xanthomes tendineux** (tendon calcanéen surtout, extenseurs des MS)\n"
                "  - **Arc cornéen** (iris)\n"
                "  - **Xanthélasma** (paupières)\n"
                "- Complications coronariennes : à partir de la quarantaine sans traitement "
                "(voire plus tôt si autres FDR)"
            )),
            FicheRow(concept="Hypercholestérolémie familiale homozygote", detail_md=(
                "- Exceptionnelle : **1 individu/1 000 000**\n"
                "- **LDL-C > 5 g/L**\n"
                "- Dépôts cutanés importants dès le plus jeune âge\n"
                "- **Complications coronariennes avant 20 ans**"
            )),
            FicheRow(concept="Hypercholestérolémie polygénique", detail_md=(
                "- Forme **majoritaire**\n"
                "- Interaction entre prédisposition génétique et environnement "
                "(alimentation riche en acides gras saturés surtout)"
            )),
        ]),
        SousPartie(lettre="D", titre="Hypertension artérielle (cf. item 224)", rows=[
            FicheRow(concept="◆ Épidémiologie de l'HTA", detail_md=(
                "- **20 à 30 %** de la population française adulte\n"
                "- Rare avant 35 ans (< 5 %)\n"
                "- Prévalence dépasse **60 % après 65 ans**"
            )),
            FicheRow(concept="◆ Définition de l'HTA", detail_md=(
                "- Consultation médicale : PA **≥ 140/90 mmHg**, persistant dans le temps\n"
                "- Automesure (AMT) : PA **≥ 135/85 mmHg**\n"
                "- MAPA 24 h : PA **≥ 130/80 mmHg**"
            )),
            FicheRow(concept="◆ PA élevée (ESC 2024)", detail_md=(
                "- **PA > 120/70 mmHg** en consultation et/ou en mesure ambulatoire\n"
                "- Mais n'atteint pas les critères diagnostiques d'HTA\n"
                "- Plus la PA augmente, plus le risque CV croît, même pour des valeurs inférieures "
                "à la « normale »\n"
                "- Nécessite évaluation SCORE2/SCORE2-OP et discussion d'un traitement si "
                "risque élevé"
            )),
            FicheRow(concept="Classification des stades d'HTA", detail_md=(
                "| Catégorie | PAS (mmHg) | PAD (mmHg) |\n"
                "|-----------|------------|------------|\n"
                "| HTA stade 1 | 140-159 | 90-99 |\n"
                "| HTA stade 2 | 160-179 | 100-109 |\n"
                "| HTA stade 3 | ≥ 180 | ≥ 110 |\n"
                "| HTA systolique isolée | ≥ 140 | < 90 |"
            )),
            FicheRow(concept="Retentissement organique de l'HTA", detail_md=(
                "- HTA le plus souvent silencieuse (peu ou pas de symptômes)\n"
                "- Retentissement sur 3 organes principaux :\n"
                "  - **Cœur** : insuffisance coronarienne, insuffisance cardiaque\n"
                "  - **Cerveau** : risque d'AVC\n"
                "  - **Reins** : insuffisance rénale"
            )),
            FicheRow(concept="Étiologies de l'HTA", detail_md=(
                "- **HTA essentielle** (majorité) : pas de cause identifiable, favorisée par :\n"
                "  - facteurs génétiques\n"
                "  - facteurs environnementaux (surpoids, sédentarité, alcool excessif, "
                "consommation excessive de sel)\n"
                "- **HTA secondaire (10 %)** : maladie rénale, cause hormonale "
                "(en particulier surrénalienne), médicaments ou toxiques"
            )),
            FicheRow(concept="◆ Diagnostic : mesures répétées", detail_md=(
                "- Pas de diagnostic sur une seule mesure (grande variabilité physiologique)\n"
                "- **Mesures répétées** sur > 1 visite sauf si HTA sévère\n"
                "- Appareils semi-automatiques au cabinet pour limiter l'effet « blouse blanche »\n"
                "- Mesure au stéthoscope plus recommandée en 1re intention "
                "(sauf en cas de fibrillation atriale)\n"
                "- Confirmation hors cabinet (**AMT** ou **MAPA**) recommandée"
            )),
            FicheRow(concept="MAPA et AMT", detail_md=(
                "- **MAPA** : documente le profil tensionnel sur 24 h\n"
                "  - Confirme le diagnostic d'HTA\n"
                "  - Confirme l'effet « blouse blanche »\n"
                "  - Identifie une **HTA masquée** (HTA non présente au cabinet, confirmée en MAPA)\n"
                "  - Confirme une **HTA résistante**\n"
                "  - Recherche d'hypotension chez diabétique ou âgé\n"
                "- **AMT** : également recommandée pour confirmer le diagnostic et l'efficacité du "
                "traitement"
            )),
        ]),
        SousPartie(lettre="E", titre="Diabète, syndrome métabolique, obésité", rows=[
            FicheRow(concept="◆ Épidémiologie du diabète", detail_md=(
                "- **3 millions** de sujets diabétiques en France (5 % de la population)\n"
                "- **DT1** (insulinodépendant d'emblée, début souvent avant 20 ans) : ~5 % des cas\n"
                "- **DT2** (initialement non insulinodépendant) : ~95 % des cas"
            )),
            FicheRow(concept="◆ Définitions glycémiques", detail_md=(
                "- Diabète : glycémie à jeun **> 1,26 g/L (7 mmol/L)** à 2 reprises, "
                "ou glycémie **> 2 g/L (11,1 mmol/L)** à n'importe quel moment\n"
                "- Hyperglycémie à jeun non diabétique : glycémie entre **1,00 et 1,26 g/L**"
            )),
            FicheRow(concept="Contexte typique de DT2", detail_md=(
                "- Dépistage systématique le plus souvent\n"
                "- Sujet > 50 ans, sédentaire, en surcharge pondérale, asymptomatique\n"
                "- Hérédité familiale de diabète fréquente\n"
                "- S'intègre volontiers dans un **syndrome métabolique**"
            )),
            FicheRow(concept="◆ Risque CV du diabète", detail_md=(
                "- **Risque CV × 2 à 3** dans les 2 types de diabète\n"
                "- DT2 dominant dans le risque CV (prévalence importante et croissante)\n"
                "- **Complications microvasculaires** : rétinopathie, néphropathie, neuropathie\n"
                "- **Complications macrovasculaires** : maladie coronarienne, AVC, AOMI"
            )),
            FicheRow(concept="◆ Évaluation de la surcharge pondérale (IMC)", detail_md=(
                "- **IMC = P (kg) / T² (m²)**\n"
                "- Maigreur : IMC < 18,5\n"
                "- Normal : 18,5 à 25\n"
                "- Surpoids : 25 à 29,9\n"
                "- **Obésité : IMC ≥ 30**"
            )),
            FicheRow(concept="◆ Périmètre ombilical", detail_md=(
                "- Reflète la graisse viscérale abdominale\n"
                "- **Mieux corrélé au risque CV que l'IMC**\n"
                "- Élément du diagnostic du syndrome métabolique"
            )),
            FicheRow(concept="◆ Syndrome métabolique (FID 2005)", detail_md=(
                "- Obésité centrale : périmètre abdominal **≥ 94 cm (H), ≥ 80 cm (F)**\n"
                "- + au moins 2 des facteurs suivants :\n"
                "  - TG > 1,50 g/L\n"
                "  - HDL-C < 0,40 g/L (H), < 0,50 g/L (F)\n"
                "  - PA ≥ 130/85 mmHg\n"
                "  - Hyperglycémie > 1 g/L ou DT2"
            )),
            FicheRow(concept="Contexte sociétal", detail_md=(
                "- 20 millions de Français en surpoids, dont 6 millions obèses\n"
                "- Touche aussi enfants et adolescents\n"
                "- Influence majeure sur la précocité et l'ampleur des perturbations métaboliques "
                "et le risque d'événements CV"
            )),
        ]),
    ])

    # ── PARTIE III : ÉVALUATION DU RISQUE CARDIOVASCULAIRE ──
    partie_iii = Partie(numero="III", titre="Évaluation du risque cardiovasculaire", sous_parties=[
        SousPartie(lettre="A", titre="Risque cardiovasculaire global et scores SCORE2", rows=[
            FicheRow(concept="◆ Risque cardiovasculaire global", detail_md=(
                "- Cumul des facteurs = **multiplication des risques** propres à chacun\n"
                "- Probabilité pour un individu de développer une MCV dans un temps donné "
                "(habituellement **10 ans**)\n"
                "- Calculé à partir d'équations de risque issues de données épidémiologiques "
                "prospectives (Framingham, SCORE européen)"
            )),
            FicheRow(concept="Historique : SCORE (ESC 2016)", detail_md=(
                "- Évaluait le risque de mortalité CV à 10 ans\n"
                "- Paramètres : sexe, âge (40-65 ans), tabagisme, PAS, cholestérol total\n"
                "- Non adapté pour : HTA sévère (≥ 180/110), diabète, IRC, hypercholestérolémie "
                "familiale\n"
                "- En prévention secondaire (MCV documentée) : risque d'emblée très élevé"
            )),
            FicheRow(concept="◆ SCORE2 (ESC 2021)", detail_md=(
                "- Estime le risque sur 10 ans d'événements **mortels ET non mortels** "
                "(IDM, AVC)\n"
                "- Population : **40-69 ans**, apparemment en bonne santé, FDR "
                "non traités ou stables depuis longtemps\n"
                "- Reflète mieux la charge totale des pathologies cardiovasculaires que "
                "l'ancien SCORE\n"
                "- France : groupe des pays à faible risque"
            )),
            FicheRow(concept="◆ SCORE2-OP (Old Person)", detail_md=(
                "- Pour personnes **≥ 70 ans** apparemment en bonne santé\n"
                "- Estime les événements CV mortels et non mortels à 5 ans et 10 ans\n"
                "- Ajusté aux risques concurrents de mortalité non liée aux MCV\n"
                "- Évite la surestimation du risque et du bénéfice du traitement chez le sujet âgé"
            )),
            FicheRow(concept="◆ SCORE2-Diabetes (ESC 2023)", detail_md=(
                "- Pour personnes atteintes de **DT2** sans MCV athérosclérotique ni lésion grave "
                "d'organe cible\n"
                "- Intègre au SCORE2 des facteurs prédictifs additionnels :\n"
                "  - Âge au diagnostic du diabète\n"
                "  - HbA1c\n"
                "  - DFG estimé"
            )),
            FicheRow(concept="Paramètres pris en compte par les scores", detail_md=(
                "| Paramètre | SCORE2 | SCORE2-OP | SCORE2-Diabetes |\n"
                "|-----------|--------|-----------|------------------|\n"
                "| Région européenne | + | + |  |\n"
                "| Sexe H/F | + | + | + |\n"
                "| Âge (ans) | 40-69 | ≥ 70 | 40-69 |\n"
                "| Tabagisme actif | + | + | + |\n"
                "| Pression artérielle systolique | + | + | + |\n"
                "| Cholestérol total | + | + | + |\n"
                "| Cholestérol HDL | + | + | + |\n"
                "| DFG estimé | NA | NA | + |\n"
                "| Âge au diagnostic du diabète | NA | NA | + |\n"
                "| HbA1c | NA | NA | + |"
            )),
        ]),
        SousPartie(lettre="B", titre="Catégories de risque et place de l'IRC", rows=[
            FicheRow(concept="Catégories de risque ESC", detail_md=(
                "- **3 catégories** : « faible à modéré », « élevé », « très élevé »\n"
                "- Seuils différents selon l'âge pour éviter sous-traitement (jeunes) et "
                "surtraitement (âgés)\n"
                "- En prévention secondaire (MCV documentée) : d'emblée **très élevé**"
            )),
            FicheRow(concept="◆ Seuils SCORE2/SCORE2-OP par âge (%)", detail_md=(
                "| Catégorie | < 50 ans | 50-69 ans | ≥ 70 ans |\n"
                "|-----------|----------|-----------|----------|\n"
                "| Faible à modéré (traitement non indiqué) | < 2,5 | < 5 | < 7,5 |\n"
                "| Élevé (traitement le plus souvent indiqué) | 2,5 à < 7,5 | 5 à < 10 | 7,5 à < 15 |\n"
                "| Très élevé (traitement généralement indiqué) | ≥ 7,5 | ≥ 10 | ≥ 15 |"
            )),
            FicheRow(concept="Catégories de risque chez le DT2", detail_md=(
                "- Faible : < 5 %\n"
                "- Modéré : 5 à < 10 %\n"
                "- Élevé : 10 à < 20 %\n"
                "- **Très élevé** : ≥ 20 % OU MCV athérosclérotique OU lésion grave "
                "d'organe cible (IRC, protéinurie, microalbuminurie, rétinopathie isolée ou associée)"
            )),
            FicheRow(concept="◆ DT2 et risque CV", detail_md=(
                "- DT2 = risque **× 2 à 4** de développer MCV au cours de la vie : "
                "coronaropathie, AVC, HTA, FA, artériopathie périphérique\n"
                "- Nombreux patients avec MCV ont un DT2 non diagnostiqué\n"
                "- Très important de dépister le DT2 chez les patients ayant une MCV\n"
                "- En cas de diabète : évaluer le risque CV et rechercher une atteinte CV et rénale"
            )),
            FicheRow(concept="Insuffisance rénale chronique (IRC)", detail_md=(
                "- Morbi-mortalité CV disproportionnée chez les patients IRC\n"
                "- Sévérité de l'IRC évaluée par : **DFG estimé** + rapport albuminurie/créatinurie "
                "(RAC, mg/g)\n"
                "- Plus le DFGe diminue et la protéinurie augmente, plus le risque d'aggravation "
                "rénale et CV augmente\n"
                "- Les SCORE2 / SCORE2-OP ne prennent pas en compte la fonction rénale\n"
                "- En cas d'IRC : patient considéré d'emblée à **haut ou très haut risque**\n"
                "- Le DFGe est pris en compte dans SCORE2-Diabetes"
            )),
            FicheRow(concept="Scores non applicables", detail_md=(
                "- Les SCORE2 / SCORE2-OP ne s'appliquent pas aux personnes :\n"
                "  - MCV documentée\n"
                "  - Diabète\n"
                "  - Hypercholestérolémie familiale ou atteintes génétiques rares\n"
                "  - Insuffisance rénale\n"
                "  - Femme enceinte"
            )),
        ]),
        SousPartie(lettre="C", titre="Autres éléments d'évaluation", rows=[
            FicheRow(concept="◆ Antécédents familiaux et facteurs psychosociaux", detail_md=(
                "- Antécédents familiaux d'accidents CV prématurés :\n"
                "  - **< 55 ans** chez le père ou un frère\n"
                "  - **< 65 ans** chez la mère ou une sœur\n"
                "- Facteurs psychosociaux : dépression, troubles psychiques, catégorie sociale "
                "défavorisée, isolement social\n"
                "- Non pris en compte dans les équations de risque (limite des scores)\n"
                "- Mais significativement associés au risque CV"
            )),
            FicheRow(concept="Anomalies d'imagerie sur organes cibles", detail_md=(
                "- **Non recommandées en routine**\n"
                "- Exemples :\n"
                "  - Épaisseur intima-média artérielle (échographie carotidienne)\n"
                "  - Score calcique coronarien (TDM)\n"
                "  - Hypertrophie ventriculaire gauche dans l'HTA (échographie)"
            )),
            FicheRow(concept="◆ Marqueurs d'atteinte rénale", detail_md=(
                "- **Microalbuminurie** : marqueur précoce de néphropathie dans le diabète et l'HTA\n"
                "- Prédit le risque d'IRC ET le risque de MCV, indépendamment du DFGe\n"
                "- Dépistage de l'IRC chez le diabétique recommandé au moins **1 fois/an**\n"
                "- Mesure du RAC sur échantillon ponctuel d'urine (mg/g)"
            )),
            FicheRow(concept="Autres marqueurs biologiques", detail_md=(
                "- Facteurs de thrombose, CRP us (ultrasensible), hyperhomocystéinémie\n"
                "- Pas de valeur ajoutée suffisante démontrée pour être utilisés en pratique\n"
                "- Ne guident pas l'adaptation du traitement médical"
            )),
            FicheRow(concept="", detail_md=(
                "- En prévention primaire chez le sujet en bonne santé apparente : utiliser **SCORE2** "
                "(40-69 ans) ou **SCORE2-OP** (≥ 70 ans) ; en cas de DT2 : **SCORE2-Diabetes** ; "
                "en cas de MCV documentée, diabète compliqué, IRC ou HF : risque d'emblée très élevé, "
                "scores inutiles."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE IV : PRÉVENTION SECONDAIRE ──
    partie_iv = Partie(numero="IV", titre="Prévention secondaire", sous_parties=[
        SousPartie(lettre="A", titre="Principes et acronyme BASIC", rows=[
            FicheRow(concept="Cadre général", detail_md=(
                "- Recommandations HAS : 4 grands FDR = dyslipidémies, HTA, "
                "diabète, tabagisme\n"
                "- Prévention secondaire : « dans les suites d'un accident vasculaire » "
                "ou « en présence de lésions vasculaires documentées »\n"
                "- Objectif : réduire le risque de récidives et ralentir la progression "
                "des lésions"
            )),
            FicheRow(concept="◆ Caractéristiques de la prévention secondaire", detail_md=(
                "- **Systématique** : tout sujet avec accident vasculaire ou atteinte athéroscléreuse\n"
                "- **Multirisque** : prise en compte de tous les facteurs de risque\n"
                "- **Intensive** : prise en charge optimale pour chacun des facteurs\n"
                "- **Médicalisée** : médicaments + suivi médicalisé régulier"
            )),
            FicheRow(concept="◆ Acronyme BASIC (prévention secondaire coronarienne)", detail_md=(
                "- **B** = Bêtabloquant (post-IDM)\n"
                "- **A** = Antiagrégant\n"
                "- **S** = Statine\n"
                "- **I** = IEC\n"
                "- **C** = Contrôle optimal des facteurs de risque :\n"
                "  - arrêt du tabagisme\n"
                "  - contrôle de la pression artérielle\n"
                "  - contrôle de la glycémie\n"
                "  - lutte contre la sédentarité"
            )),
            FicheRow(concept="", detail_md=(
                "- Chacune des 4 classes médicamenteuses (**BASI**) diminue la mortalité totale de "
                "**~25 %** après un IDM."
            ), kind="a_retenir"),
            FicheRow(concept="", detail_md=(
                "- Oublier le **BASIC** (bêtabloquant, antiagrégant, statine, IEC + contrôle des FDR) "
                "après un accident coronarien = **notion inacceptable** aux ECN."
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Hypocholestérolémiant, PA, glycémie", rows=[
            FicheRow(concept="◆ Traitement hypocholestérolémiant", detail_md=(
                "- **Statine systématique** en prévention secondaire\n"
                "- Réduction démontrée de la mortalité totale et de la morbi-mortalité coronarienne\n"
                "- Indépendamment de l'âge, du sexe, des FDR, des traitements associés et du "
                "niveau initial de cholestérolémie\n"
                "- Cible thérapeutique : **LDL-C < 0,55 g/L**"
            )),
            FicheRow(concept="◆ Contrôle de la pression artérielle", detail_md=(
                "- Objectif HAS : PA **≤ 140/90 mmHg**\n"
                "- Privilégier les mesures hygiénodiététiques : contrôle du poids, activité "
                "physique, diminution de l'alcool et du sodium\n"
                "- Traitement médicamenteux si :\n"
                "  - PA ≥ 160/100 mmHg d'emblée\n"
                "  - PA ≥ 140/90 mmHg persistant après 3 mois de MHD"
            )),
            FicheRow(concept="◆ Objectifs ESC 2021 (sous traitement)", detail_md=(
                "- 1re étape : PA **< 140/90 mmHg** chez tous les patients (au cabinet)\n"
                "- Si bien toléré : cibles autour de **130/80 mmHg** pour la majorité\n"
                "- < 70 ans : PAS **120-129 mmHg**\n"
                "- ≥ 70 ans : PAS **130-139 mmHg** (ou jusqu'à 130 si bonne tolérance)\n"
                "- PAD < 80 mmHg pour tous les patients"
            )),
            FicheRow(concept="◆ Contrôle glycémique", detail_md=(
                "- Diabète **× 2 à 3** le risque d'événements cardiaques graves après IDM\n"
                "- Le bénéfice d'un équilibre glycémique au long cours sur la morbi-mortalité "
                "coronarienne n'a pas été formellement démontré après IDM\n"
                "- En revanche, le diabète est un argument supplémentaire pour corriger de "
                "façon agressive les autres facteurs de risque"
            )),
        ]),
        SousPartie(lettre="C", titre="Sevrage tabagique, activité physique, enquête familiale", rows=[
            FicheRow(concept="◆ Bénéfices du sevrage tabagique", detail_md=(
                "- **−36 %** de risque de décès\n"
                "- **−32 %** de risque de récidive d'IDM dans les années suivant un accident coronarien\n"
                "- Bénéfice important également après pontage coronarien ou angioplastie"
            )),
            FicheRow(concept="◆ Modalités du sevrage post-coronarien", detail_md=(
                "- Forte dépendance + brutalité de la demande → rechutes fréquentes et précoces\n"
                "- Aide médicalisée et suivi indispensables\n"
                "- **Substitution nicotinique** : sécurité d'utilisation démontrée\n"
                "  - HAS 2014 : « recommandée chez le patient coronarien fumeur, bien tolérée, "
                "pas d'aggravation de la maladie coronarienne ni de troubles du rythme »\n"
                "- Thérapies comportementales et cognitives également utiles\n"
                "- Éviter toute exposition au tabagisme passif"
            )),
            FicheRow(concept="◆ Activité physique chez le coronarien", detail_md=(
                "- Effets physiologiques favorables multiples :\n"
                "  - Antiagrégant plaquettaire\n"
                "  - Anti-inflammatoire\n"
                "  - ↑ VO2 max et capacité fonctionnelle à l'effort\n"
                "  - Action favorable sur la fonction endothéliale\n"
                "  - Recul du seuil ischémique\n"
                "  - Antiarythmique (amélioration de la variabilité sinusale)\n"
                "- **Réduction de la mortalité totale et coronarienne de 20 à 25 %** (méta-analyse)\n"
                "- Pas de réduction significative du risque de récidive d'IDM non mortel\n"
                "- Améliore qualité de vie, anxiété/dépression, réinsertion professionnelle"
            )),
            FicheRow(concept="◆ Enquête familiale", detail_md=(
                "- À engager devant tout patient coronarien, surtout s'il est jeune :\n"
                "  - **< 55 ans** pour un homme\n"
                "  - **< 65 ans** pour une femme\n"
                "- Dépister la présence de FDR chez :\n"
                "  - les collatéraux\n"
                "  - les enfants\n"
                "- Objectif : prise en charge précoce de prévention primaire adaptée au risque "
                "individuel"
            )),
        ]),
    ])

    # ── PARTIE V : PRÉVENTION PRIMAIRE ──
    partie_v = Partie(numero="V", titre="Prévention primaire", sous_parties=[
        SousPartie(lettre="A", titre="Stratégie selon le niveau de risque", rows=[
            FicheRow(concept="Définition de la prévention primaire", detail_md=(
                "- Vise à réduire l'incidence de la maladie\n"
                "- En dépistant et contrôlant les FDR « en amont de tout "
                "accident vasculaire »\n"
                "- **Prévention primosecondaire** : patients indemnes de pathologie cliniquement "
                "décelable mais ayant des lésions athéromateuses infracliniques"
            )),
            FicheRow(concept="◆ Approche en consultation", detail_md=(
                "- Toute consultation = opportunité d'aborder la prévention\n"
                "- Recueil systématique dans le dossier médical :\n"
                "  - Tabagisme\n"
                "  - Pression artérielle\n"
                "  - Poids, taille, périmètre abdominal\n"
                "  - Antécédents familiaux\n"
                "- Analyse du mode d'alimentation et de l'activité physique\n"
                "- **Bilan biologique de référence** à jeun : glycémie + bilan lipidique complet"
            )),
            FicheRow(concept="◆ Adaptation au niveau de risque", detail_md=(
                "- Profil de risque favorable : encourager la poursuite des comportements "
                "protecteurs\n"
                "- Risque faible ou modéré : conseils de prévention collective\n"
                "- **Haut risque** : prise en charge médicalisée spécifique de prévention primaire"
            )),
            FicheRow(concept="Démarche éducative", detail_md=(
                "- Reposent sur modifications de comportements (tabac, alimentation, AP)\n"
                "- Succès dépend de la qualité du dialogue patient-médecin\n"
                "- **Éducation thérapeutique** : « convaincre sans contraindre »\n"
                "- Conjuguer les objectifs médicaux avec ceux exprimés par le patient\n"
                "- Analyse des freins et leviers pour modification durable"
            )),
        ]),
        SousPartie(lettre="B", titre="Pression artérielle et cholestérolémie", rows=[
            FicheRow(concept="◆ Stratégie sur la PA", detail_md=(
                "- L'évaluation prend en compte le niveau de PA + FDR associés\n"
                "- SCORE2/SCORE2-OP recommandés chez les patients avec PA élevée ou HTA non "
                "déjà à risque élevé/très élevé\n"
                "- Pas de limite d'âge pour envisager un traitement antihypertenseur "
                "(ESC 2024)\n"
                "- Traitement repose sur **4 piliers** :\n"
                "  - Mesures hygiénodiététiques\n"
                "  - Traitement des FDR associés\n"
                "  - Traitement médicamenteux\n"
                "  - Éducation thérapeutique"
            )),
            FicheRow(concept="◆ Objectifs PA en prévention primaire (ESC 2024)", detail_md=(
                "- Cible recommandée : **PAS 120-129 mmHg** et **PAD 70-79 mmHg**\n"
                "- À adapter d'emblée chez certains patients :\n"
                "  - Hypotension orthostatique\n"
                "  - Fragilité\n"
                "  - Âge > 85 ans\n"
                "  - Espérance de vie limitée\n"
                "- Cible idéalement atteinte à 3 mois du début du traitement, par "
                "automesures"
            )),
            FicheRow(concept="◆ Stratégie sur le LDL-C", detail_md=(
                "- LDL-C = principal objectif thérapeutique (preuves de bénéfice CV)\n"
                "- **1re intention** = modification du mode de vie si LDL-C > objectif :\n"
                "  - Seule si risque faible ou modéré\n"
                "  - Associée à un hypolipémiant si risque élevé ou très élevé "
                "(par étapes)\n"
                "- **2e intention** : si objectif non atteint après 3 mois d'intervention bien "
                "suivie → instaurer ou intensifier un hypolipémiant"
            )),
        ]),
        SousPartie(lettre="C", titre="Sevrage tabagique", rows=[
            FicheRow(concept="◆ Objectif du sevrage", detail_md=(
                "- **Arrêt total et définitif** de la consommation de tabac\n"
                "- Le plus tôt possible\n"
                "- Les médecins doivent connaître et utiliser les méthodes modernes de sevrage"
            )),
            FicheRow(concept="◆ Conseil minimum", detail_md=(
                "- L'arrêt est le fruit d'un lent processus de maturation\n"
                "- Motivation faible chez le « fumeur heureux »\n"
                "- Aborder systématiquement, même brièvement la question du tabagisme = "
                "**conseil minimum**\n"
                "- Peut **doubler le taux de sevrage** dans un délai d'1 an\n"
                "- Exemple : « le fait d'arrêter de fumer est une décision importante que vous "
                "pouvez prendre pour votre santé. Je peux vous y aider »"
            )),
            FicheRow(concept="◆ Évaluation initiale", detail_md=(
                "- Niveau de motivation\n"
                "- Niveau de dépendance physique : **test de Fagerström**\n"
                "- Autres dépendances : alcool, cannabis, anxiolytiques, etc.\n"
                "- Prise de poids moyenne de **5 kg** à l'arrêt, mais bénéfices >> risques "
                "de prise de poids"
            )),
            FicheRow(concept="◆ Substituts nicotiniques", detail_md=(
                "- Évitent le syndrome de sevrage\n"
                "- **Doublent les chances de sevrage**\n"
                "- Associer patchs + formes orales (gommes, comprimés sublinguaux, "
                "spray buccal, inhalateur)\n"
                "- Ajuster la dose individuellement, durée **≥ 3 mois**, souvent plus prolongée\n"
                "- Ne contre-indiquent pas la prise de cigarette (sevrage progressif possible)\n"
                "- Autorisés chez la femme enceinte avec accompagnement médical"
            )),
            FicheRow(concept="Autres traitements médicamenteux", detail_md=(
                "- **Bupropion** et **varénicline** : peuvent être utilisés"
            )),
            FicheRow(concept="Cigarette électronique", detail_md=(
                "- N'est pas un dispositif médical de sevrage tabagique\n"
                "- Avec nicotine : peut être utile au sevrage (réduction du risque tabagique)\n"
                "- **2e intention**, associée aux autres méthodes notamment substituts nicotiniques"
            )),
            FicheRow(concept="Autres approches", detail_md=(
                "- Prise en charge de l'anxiété/dépression si nécessaire\n"
                "- Thérapies comportementales et cognitives (autocontrôle, gestion du stress, "
                "affirmation de soi) : efficacité démontrée\n"
                "- Consultations spécialisées de tabacologie pour formes sévères de dépendance "
                "ou rechutes"
            )),
            FicheRow(concept="Mesures de santé publique", detail_md=(
                "- Mesures législatives d'interdiction de fumer dans les lieux publics\n"
                "- Effet démontré significatif et rapide sur l'incidence des IDM"
            )),
        ]),
        SousPartie(lettre="D", titre="Alimentation et activité physique (PNNS)", rows=[
            FicheRow(concept="◆ 4 messages essentiels du PNNS", detail_md=(
                "- **PNNS** = Programme national nutrition santé (France, lancé en 2001)\n"
                "- 1. Fruits et légumes : objectif **5/jour**\n"
                "- 2. Poisson : **2 fois/semaine**\n"
                "- 3. Limitation des graisses saturées, produits sucrés et sel\n"
                "- 4. Activité physique : au moins **30 min × 5 j/semaine**"
            )),
            FicheRow(concept="◆ Recommandations d'activité physique", detail_md=(
                "- **150 à 300 min/sem** d'AP aérobie d'intensité modérée "
                "(course, natation, vélo)\n"
                "- OU **75 à 150 min/sem** d'activités plus intenses\n"
                "- Éventuellement associées à des activités de résistance\n"
                "- 1h30/semaine d'AP modérée (3 à 5 séances) réduit déjà la survenue de MCV "
                "et la mortalité CV chez l'adulte en bonne santé\n"
                "- Plus la pratique est élevée, plus les bénéfices sont importants "
                "(sauf comorbidités : > 5h/semaine peut être à risque)"
            )),
            FicheRow(concept="◆ Alimentation méditerranéenne (étude PREDIMED)", detail_md=(
                "- Bénéfices CV et métaboliques scientifiquement établis\n"
                "- Caractéristiques :\n"
                "  - Richesse en fruits et légumes\n"
                "  - Acides gras insaturés (**huile d'olive**)\n"
                "  - Produits de la mer\n"
                "  - Faible consommation de viande rouge au profit de volaille et poisson"
            )),
            FicheRow(concept="◆ Bénéfices généraux de l'AP", detail_md=(
                "- Améliore la qualité de vie (anxiété, dépression, sommeil)\n"
                "- Maintient l'autonomie\n"
                "- Place dans la prévention primaire, secondaire et tertiaire de nombreuses "
                "pathologies chroniques\n"
                "- Diminue la mortalité et l'incidence : MCV, DT2, cancers\n"
                "- Bénéfices >> risques pour la majorité des adultes"
            )),
            FicheRow(concept="◆ Évaluation médicale avant AP intense", detail_md=(
                "- **Q-AAP+** (Questionnaire sur l'aptitude à l'activité physique pour tous) : "
                "le plus utilisé\n"
                "- **QS-SPORT** : questionnaire de santé officiel pour le renouvellement d'une "
                "licence sportive (Cerfa 15699)\n"
                "- Bilan médical minimal si :\n"
                "  - Q-AAP+ positif\n"
                "  - Âge > 45 ans, inactif\n"
                "  - AP envisagée d'intensité très élevée\n"
                "  - Suspicion de maladie cardiaque, pulmonaire, métabolique ou rénale"
            )),
            FicheRow(concept="Recommandations EE avant AP > 6 MET", detail_md=(
                "| Statut | Risque CV faible | Risque CV modéré | Risque CV élevé ou très élevé |\n"
                "|---------|------------------|-------------------|--------------------------------|\n"
                "| Inactif | EE non préconisée | EE peut être réalisée | EE recommandée |\n"
                "| Actif | EE non recommandée | EE non préconisée | EE recommandée |"
            )),
            FicheRow(concept="◆ Place de l'ECG de repos", detail_md=(
                "- Pas un préalable indispensable avant AP de loisir\n"
                "- Peu performant pour dépister une maladie coronarienne chez l'asymptomatique\n"
                "- **Indispensable** + avis cardiologique pour une pratique intensive chez "
                "l'adulte avec ATCD personnels ou familiaux CV (cardiomyopathies, maladies rythmiques "
                "héréditaires, mort subite)"
            )),
            FicheRow(concept="◆ Approches connectées", detail_md=(
                "- Smartphones, montres connectées, traqueurs, dispositifs de télésurveillance\n"
                "- Pour favoriser l'adhésion ou l'observance : rappels, questionnaires, monitorage "
                "(pas, escaliers, lever) ou paramètres biologiques (glycémie, PA, FC, arythmies, poids)\n"
                "- Pas toutes certifiées ni évaluées scientifiquement en prévention primaire\n"
                "- Doivent être couplées à une évaluation précise et un accompagnement personnalisé\n"
                "- Études : le podomètre favorise ↑ AP, ↓ IMC et ↓ PA"
            )),
            FicheRow(concept="Importance pédiatrique", detail_md=(
                "- Comportements de prévention collective à adopter dès l'enfance et l'adolescence\n"
                "- Plus difficiles à acquérir à l'âge adulte\n"
                "- Choisir de ne pas fumer, bien s'alimenter, combattre la sédentarité"
            )),
            FicheRow(concept="", detail_md=(
                "- En prévention primaire, l'adhésion au traitement est souvent difficile : "
                "prise en charge **personnalisée**, **éducation thérapeutique**, **entretiens "
                "motivationnels** et prise en charge pluridisciplinaire sont nécessaires."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE VI : NOTIONS INDISPENSABLES ET INACCEPTABLES ──
    partie_vi = Partie(numero="VI", titre="Notions indispensables et inacceptables", sous_parties=[
        SousPartie(lettre="A", titre="Notions indispensables", rows=[
            FicheRow(concept="◆ Connaissances fondamentales", detail_md=(
                "- Connaître les **6 FDR cardiovasculaire modifiables** :\n"
                "  - Tabac\n"
                "  - Diabète\n"
                "  - HTA\n"
                "  - Dyslipidémie\n"
                "  - Facteurs psychosociaux\n"
                "  - Obésité\n"
                "- Connaître les facteurs « protecteurs » : alimentation, activité physique\n"
                "- Connaître la notion de **risque cardiovasculaire global**\n"
                "- Connaître les outils **SCORE2**, **SCORE2-OP** et **SCORE2-Diabetes**\n"
                "- Connaître les principaux conseils nutritionnels et le rôle bénéfique de l'AP"
            )),
        ]),
        SousPartie(lettre="B", titre="Notions inacceptables", rows=[
            FicheRow(concept="⚠ À ne jamais oublier", detail_md=(
                "- Oublier le **BASIC** après un accident coronarien :\n"
                "  - **B** = Bêtabloquant\n"
                "  - **A** = Antiagrégant\n"
                "  - **S** = Statine\n"
                "  - **I** = IEC\n"
                "  - **C** = Contrôle des facteurs de risque\n"
                "- Ne pas connaître la cible **LDL-C < 0,55 g/L** chez les sujets à très haut "
                "risque ou en prévention secondaire"
            )),
            FicheRow(concept="", detail_md=(
                "- Cible **LDL-C < 0,55 g/L** en prévention secondaire et chez le très haut risque "
                "= valeur à retenir absolument pour les ECN."
            ), kind="mnemo"),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Facteurs de risque non modifiables vs modifiables", markdown=(
            "| Non modifiables | Modifiables | Protecteurs |\n"
            "|------------------|-------------|--------------|\n"
            "| Âge | Tabagisme | Fruits et légumes |\n"
            "| Sexe (H > F avant 65 ans) | Hypercholestérolémie (LDL-C élevé) | Activité physique |\n"
            "| Hérédité (< 55 H / < 65 F) | HTA | Consommation légère d'alcool |\n"
            "|  | Diabète (DT2 +++) |  |\n"
            "|  | Obésité abdominale / syndrome métabolique |  |\n"
            "|  | Facteurs psychosociaux |  |"
        )),
        TableauSynthese(titre="Classification des stades d'HTA (mmHg)", markdown=(
            "| Catégorie | PAS | PAD |\n"
            "|-----------|-----|-----|\n"
            "| HTA stade 1 | 140-159 | 90-99 |\n"
            "| HTA stade 2 | 160-179 | 100-109 |\n"
            "| HTA stade 3 | ≥ 180 | ≥ 110 |\n"
            "| HTA systolique isolée | ≥ 140 | < 90 |"
        )),
        TableauSynthese(titre="Catégories de risque SCORE2/SCORE2-OP (% à 10 ans)", markdown=(
            "| Catégorie | < 50 ans | 50-69 ans | ≥ 70 ans |\n"
            "|-----------|----------|-----------|----------|\n"
            "| Faible à modéré (traitement non indiqué) | < 2,5 | < 5 | < 7,5 |\n"
            "| Élevé (traitement le plus souvent indiqué) | 2,5 à < 7,5 | 5 à < 10 | 7,5 à < 15 |\n"
            "| Très élevé (traitement généralement indiqué) | ≥ 7,5 | ≥ 10 | ≥ 15 |"
        )),
        TableauSynthese(titre="Critères du syndrome métabolique (FID 2005)", markdown=(
            "| Critère | Homme | Femme |\n"
            "|---------|-------|--------|\n"
            "| Périmètre abdominal (obligatoire) | ≥ 94 cm | ≥ 80 cm |\n"
            "| + au moins 2 critères parmi : |  |  |\n"
            "| Triglycérides | > 1,50 g/L | > 1,50 g/L |\n"
            "| HDL-C | < 0,40 g/L | < 0,50 g/L |\n"
            "| Pression artérielle | ≥ 130/85 mmHg | ≥ 130/85 mmHg |\n"
            "| Glycémie à jeun | > 1 g/L ou DT2 | > 1 g/L ou DT2 |"
        )),
        TableauSynthese(titre="Acronyme BASIC en prévention secondaire coronarienne", markdown=(
            "| Lettre | Classe | Précision |\n"
            "|--------|--------|-----------|\n"
            "| B | Bêtabloquant | Post-IDM |\n"
            "| A | Antiagrégant plaquettaire | Systématique |\n"
            "| S | Statine | Cible LDL-C < 0,55 g/L |\n"
            "| I | IEC | Systématique |\n"
            "| C | Contrôle des FDR | Tabac, PA, glycémie, sédentarité |"
        )),
        TableauSynthese(titre="Paramètres des scores SCORE2 / SCORE2-OP / SCORE2-Diabetes", markdown=(
            "| Paramètre | SCORE2 | SCORE2-OP | SCORE2-Diabetes |\n"
            "|-----------|--------|-----------|------------------|\n"
            "| Région européenne | + | + |  |\n"
            "| Sexe H/F | + | + | + |\n"
            "| Âge (ans) | 40-69 | ≥ 70 | 40-69 |\n"
            "| Tabagisme actif | + | + | + |\n"
            "| PAS | + | + | + |\n"
            "| Cholestérol total | + | + | + |\n"
            "| Cholestérol HDL | + | + | + |\n"
            "| DFG estimé | NA | NA | + |\n"
            "| Âge au diagnostic du DT | NA | NA | + |\n"
            "| HbA1c | NA | NA | + |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Mortalité CV France (tabac) | 73 000 décès/an | Dont ~2 000 par tabagisme passif |\n"
        "| Tabagisme passif | +24 % d'IDM (1-7 h/sem), +62 % (> 22 h/sem) | Étude Interheart |\n"
        "| Sevrage tabagique | -36 % décès, -32 % récidive IDM | Prévention secondaire |\n"
        "| ATCD familiaux d'accidents précoces (H) | < 55 ans | Père ou frère |\n"
        "| ATCD familiaux d'accidents précoces (F) | < 65 ans | Mère ou sœur |\n"
        "| Définition HTA en consultation | ≥ 140/90 mmHg | Persistant dans le temps |\n"
        "| Définition HTA en AMT | ≥ 135/85 mmHg | Automesure |\n"
        "| Définition HTA en MAPA 24 h | ≥ 130/80 mmHg | Mesure ambulatoire |\n"
        "| PA élevée (ESC 2024) | > 120/70 mmHg | Sans atteindre seuil HTA |\n"
        "| Cible PA en prévention primaire | PAS 120-129, PAD 70-79 mmHg | ESC 2024 |\n"
        "| Cible PA prévention secondaire (1re étape) | < 140/90 mmHg | Au cabinet |\n"
        "| Cible PA prévention secondaire (majorité) | ≈ 130/80 mmHg | Si bien toléré |\n"
        "| PAS < 70 ans (cible) | 120-129 mmHg | ESC 2021 |\n"
        "| PAS ≥ 70 ans (cible) | 130-139 mmHg (ou jusqu'à 130) | ESC 2021 |\n"
        "| Diabète à jeun | > 1,26 g/L (7 mmol/L) à 2 reprises | Diagnostic |\n"
        "| Diabète aléatoire | > 2 g/L (11,1 mmol/L) | Diagnostic |\n"
        "| Hyperglycémie non diabétique | 1,00-1,26 g/L | À jeun |\n"
        "| Risque CV majoré (diabète) | × 2 à 3 | Toutes formes |\n"
        "| IMC normal | 18,5 à 25 kg/m² | Adulte |\n"
        "| Surpoids | 25 à 29,9 kg/m² | IMC |\n"
        "| Obésité | ≥ 30 kg/m² | IMC |\n"
        "| Périmètre abdominal (syndrome métabolique) | ≥ 94 cm (H), ≥ 80 cm (F) | FID 2005 |\n"
        "| Hypercholestérolémie familiale hétérozygote | LDL-C 2-4 g/L | 1/500 |\n"
        "| Hypercholestérolémie familiale homozygote | LDL-C > 5 g/L | 1/1 000 000 |\n"
        "| Formule de Friedewald | LDL-C = CT − HDL-C − TG/5 | Si TG < 3,5 g/L |\n"
        "| Cible LDL-C prévention secondaire / très haut risque | < 0,55 g/L | Statine systématique |\n"
        "| AOMI et tabagisme | 90 % des patients sont fumeurs | Localisation athéroscléreuse |\n"
        "| AP recommandée (PNNS) | ≥ 30 min × 5 j/sem | Prévention CV |\n"
        "| AP modérée (semaine) | 150 à 300 min/sem | Aérobie |\n"
        "| AP intense (semaine) | 75 à 150 min/sem | Intensité élevée |\n"
        "| Fruits et légumes (objectif PNNS) | 5/jour | Prévention CV |\n"
        "| Poisson | 2 fois/semaine | PNNS |\n"
        "| Bénéfice statine post-IDM (mortalité) | -25 % | Idem pour B, A, I |\n"
        "| Prise de poids moyenne sevrage tabac | 5 kg | Mais bénéfice net favorable |\n"
        "| Conseil minimum (sevrage) | × 2 du taux de sevrage à 1 an | Phrase brève systématique |\n"
        "| Substituts nicotiniques | × 2 chances de sevrage | Patch + forme orale, ≥ 3 mois |"
    ))

    points_cles = [
        "**Facteur de risque** = causalité prouvée (5 critères) ; **marqueur** = simple témoin sans valeur causale",
        "**Interheart** : 9 facteurs = 90 % des IDM (tabac, LDL-C, HTA, diabète, obésité abdo, psychosociaux + 3 protecteurs)",
        "**LDL-C** = facteur déterminant du risque coronarien ; cible **< 0,55 g/L** en prévention secondaire",
        "**HTA** : ≥ **140/90** consultation, ≥ **135/85** AMT, ≥ **130/80** MAPA ; PA élevée ESC 2024 > 120/70",
        "**DT2** (95 % des diabètes) : risque CV **× 2 à 3** ; impose correction agressive des autres FDR",
        "**SCORE2** (40-69 ans), **SCORE2-OP** (≥ 70 ans), **SCORE2-Diabetes** ; non applicables si MCV, HF, IRC, grossesse",
        "**Prévention secondaire = BASIC** : Bêtabloquant, Antiagrégant, Statine, IEC, Contrôle des FDR (−25 % mortalité chacun)",
        "**Sevrage tabagique** : **−36 %** décès, **−32 %** récidive IDM ; substituts nicotiniques sûrs chez le coronarien",
        "**PNNS** : 5 fruits/légumes/j, poisson 2×/sem, ↓ graisses saturées et sel, **30 min × 5 j/sem** d'AP",
        "Coronarien jeune (H < 55, F < 65) : **enquête familiale** pour dépister les FDR chez collatéraux et enfants",
    ]

    fiche_eclair_md = (
        "**Définitions** : FDR = causalité prouvée (5 critères). Marqueur = simple témoin. Athérosclérose = "
        "maladie plurifactorielle.\n\n"
        "**Interheart** : 9 facteurs = 90 % des IDM. 6 FDR (tabac, LDL-C, HTA, diabète, obésité abdo, "
        "psychosociaux) + 3 protecteurs (fruits/légumes, AP, alcool léger). Hérédité = H < 55, F < 65.\n\n"
        "**Tabagisme** : 1re cause mortalité évitable. 73 000 décès/an France. Pas de seuil. Passif : "
        "+24 % IDM (1-7 h/sem), +62 % (> 22 h). AOMI : 90 % fumeurs.\n\n"
        "**Hypercholestérolémie** : LDL-C = facteur déterminant. Friedewald = CT − HDL − TG/5 "
        "(si TG < 3,5). HF hétérozygote 1/500, LDL 2-4 ; homozygote 1/10⁶, LDL > 5, IDM < 20 ans.\n\n"
        "**HTA** : ≥ 140/90 consult., ≥ 135/85 AMT, ≥ 130/80 MAPA. PA élevée (ESC 2024) > 120/70. "
        "10 % secondaires.\n\n"
        "**Diabète** : glycémie > 1,26 à 2 reprises ou > 2 aléatoire. DT2 = 95 %, risque CV × 2-4. "
        "Syndrome métabolique : périmètre ≥ 94 H / 80 F + 2 critères (TG > 1,50 ; HDL < 0,40 H / 0,50 F ; "
        "PA ≥ 130/85 ; glycémie > 1).\n\n"
        "**Obésité** : IMC ≥ 30 (surpoids 25-29,9). Périmètre abdo mieux corrélé que IMC.\n\n"
        "**SCORE2** 40-69 ans, **SCORE2-OP** ≥ 70 ans, **SCORE2-Diabetes** DT2. Seuils élevé 2,5/5/7,5 % ; "
        "très élevé 7,5/10/15 %. Non applicables si MCV, HF, IRC, grossesse (d'emblée très haut risque).\n\n"
        "**Prévention secondaire = BASIC** : Bêtabloquant, Antiagrégant, Statine, IEC, Contrôle FDR. "
        "Chacune −25 % mortalité. Cible LDL-C < 0,55 g/L. PA < 140/90 puis ≈ 130/80. Sevrage tabac : "
        "−36 % décès, −32 % récidive. AP : −20-25 % mortalité.\n\n"
        "**Prévention primaire** : PA cible ESC 2024 = 120-129 / 70-79. LDL-C : MHD si faible/modéré, "
        "+ hypolipémiant si élevé. Conseil minimum × 2 le sevrage. Substituts ≥ 3 mois.\n\n"
        "**PNNS** : 5 fruits/légumes/j, poisson 2×/sem, ↓ graisses saturées + sel, AP 30 min × 5 j/sem. "
        "Alimentation méditerranéenne (PREDIMED).\n\n"
        "**Inacceptable** : oublier BASIC post-IDM ; ignorer cible LDL-C < 0,55 g/L au très haut risque."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 222 - Facteurs de risque cardiovasculaire et prévention",
        annee="2025-2026",
        item="Item 222",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 222",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-222_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

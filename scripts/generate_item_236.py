"""Génère la fiche de l'Item 236 - Troubles de la conduction intracardiaque (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Définitions et anatomophysiologie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Rappel anatomique des voies de conduction"),
            PlanSousPartie(lettre="B", titre="Physiopathologie et terminologie"),
            PlanSousPartie(lettre="C", titre="Hiérarchie des fréquences d'échappement"),
        ]),
        PlanPartie(numero="II", titre="Dysfonction sinusale", sous_parties=[
            PlanSousPartie(lettre="A", titre="Physiopathologie et mécanismes"),
            PlanSousPartie(lettre="B", titre="Présentation clinique"),
            PlanSousPartie(lettre="C", titre="Étiologies"),
            PlanSousPartie(lettre="D", titre="Diagnostic ECG"),
            PlanSousPartie(lettre="E", titre="Évaluation et urgence"),
        ]),
        PlanPartie(numero="III", titre="Blocs atrioventriculaires (BAV)", sous_parties=[
            PlanSousPartie(lettre="A", titre="Physiopathologie et mécanismes"),
            PlanSousPartie(lettre="B", titre="Présentation clinique"),
            PlanSousPartie(lettre="C", titre="Étiologies"),
            PlanSousPartie(lettre="D", titre="Diagnostic ECG"),
            PlanSousPartie(lettre="E", titre="Formes cliniques et évaluation"),
        ]),
        PlanPartie(numero="IV", titre="Blocs de branche", sous_parties=[
            PlanSousPartie(lettre="A", titre="Physiopathologie et clinique"),
            PlanSousPartie(lettre="B", titre="Étiologies"),
            PlanSousPartie(lettre="C", titre="Diagnostic ECG"),
            PlanSousPartie(lettre="D", titre="Formes cliniques et prise en charge"),
        ]),
        PlanPartie(numero="V", titre="Thérapeutique et suivi du patient", sous_parties=[
            PlanSousPartie(lettre="A", titre="Urgences et signes de gravité"),
            PlanSousPartie(lettre="B", titre="Moyens thérapeutiques"),
            PlanSousPartie(lettre="C", titre="Indications de stimulation définitive"),
            PlanSousPartie(lettre="D", titre="Traitement des blocs de branche"),
            PlanSousPartie(lettre="E", titre="Éducation et surveillance du patient appareillé"),
        ]),
    ]

    # ── PARTIE I : DÉFINITIONS ET ANATOMOPHYSIOLOGIE ──
    partie_i = Partie(numero="I", titre="Définitions et anatomophysiologie", sous_parties=[
        SousPartie(lettre="A", titre="Rappel anatomique des voies de conduction", rows=[
            FicheRow(concept="◆ Trois étages des voies de conduction", detail_md=(
                "- Les voies de conduction intracardiaques sont organisées en **trois étages** :\n"
                "  - Étage nodal sinusal : **nœud sinusal (NS)** dans l'atrium droit\n"
                "  - Étage nodal atrioventriculaire : **nœud atrioventriculaire (NAV)**\n"
                "  - Étage hissien et infrahissien : **faisceau de His**, branches, réseau de Purkinje"
            )),
            FicheRow(concept="Conduction atriale", detail_md=(
                "- Au sein de l'oreillette : pas de structure de conduction bien définie\n"
                "- Existence de voies de conduction préférentielles : faisceau internodal "
                "antérieur, moyen et postérieur\n"
                "- Le **faisceau de Bachmann** naît du tissu internodal antérieur, dépolarise "
                "l'oreillette gauche à travers le septum interatrial"
            )),
            FicheRow(concept="Conduction intraventriculaire", detail_md=(
                "- N'est pas l'exclusivité du réseau de Purkinje\n"
                "- Se fait également au sein du myocarde ventriculaire (y compris septal) "
                "de proche en proche, mais lentement\n"
                "- Peut entraîner un allongement de la durée du QRS en cas de pathologie "
                "myocardique → **blocs intraventriculaires non systématisés**"
            )),
        ]),
        SousPartie(lettre="B", titre="Physiopathologie et terminologie", rows=[
            FicheRow(concept="◆ Dysfonction sinusale", detail_md=(
                "- Pathologie qui touche au fonctionnement du **nœud sinusal (NS)**\n"
                "- Comprend :\n"
                "  - les troubles de l'automatisme sinusal\n"
                "  - le **bloc sinoatrial (BSA)**"
            )),
            FicheRow(concept="◆ Bloc atrioventriculaire (BAV)", detail_md=(
                "- Défini par une atteinte de la jonction atrioventriculaire "
                "et/ou une atteinte bilatérale des branches de division du faisceau de His"
            )),
            FicheRow(concept="◆ Blocs de branche / hémiblocs", detail_md=(
                "- Atteinte systématisée d'une ou des branches du faisceau de His"
            )),
            FicheRow(concept="Distinction tissu nodal / His-Purkinje", detail_md=(
                "| Caractère | Tissu nodal (NS, NAV) | His-Purkinje |\n"
                "|---|---|---|\n"
                "| Conduction | **Lente, décrémentielle** | **Rapide, tout ou rien** |\n"
                "| Système nerveux autonome | Fortement influencé | Pas influencé |\n"
                "| Composition | NS + NAV | Faisceau His + branches + Purkinje |"
            )),
            FicheRow(concept="◆ Distinction suprahissien / hissien-infrahissien", detail_md=(
                "- Dans les BAV, séparer pour des raisons de gravité :\n"
                "  - **Atteinte nodale (suprahissienne)** : NAV\n"
                "  - **Atteinte hissienne ou infrahissienne** : faisceau de His et au-delà"
            )),
            FicheRow(concept="", detail_md=(
                "- Les troubles **suprahissiens** (dysfonction sinusale, bloc nodal) ont un "
                "rythme d'échappement plus stable et plus rapide.\n"
                "- Les troubles **hissiens ou infrahissiens** ont un rythme d'échappement "
                "instable et plus lent → plus graves."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Hiérarchie des fréquences d'échappement", rows=[
            FicheRow(concept="◆ Hiérarchie décroissante des échappements", detail_md=(
                "| Structure | Fréquence | QRS | Stabilité |\n"
                "|---|---|---|---|\n"
                "| **NAV** | **40-60 bpm** | Fins | Stable |\n"
                "| **Faisceau de His** | **35-45 bpm** | Fins | Instable |\n"
                "| **Infrahissien** | **< 40 bpm** | Larges | Instable |"
            )),
            FicheRow(concept="", detail_md=(
                "- Plus la **lésion est distale** dans le tissu de conduction, plus le rythme "
                "d'échappement est instable et lent, et plus le tableau est **grave**."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE II : DYSFONCTION SINUSALE ──
    partie_ii = Partie(numero="II", titre="Dysfonction sinusale", sous_parties=[
        SousPartie(lettre="A", titre="Physiopathologie et mécanismes", rows=[
            FicheRow(concept="Anatomie du nœud sinusal", detail_md=(
                "- Structure en forme de croissant mesurant **1 à 2 cm**\n"
                "- Situé dans l'atrium droit, à la jonction avec la veine cave supérieure\n"
                "- Cellules dotées d'un automatisme produisant cycliquement l'activité électrique "
                "qui initie chaque battement (rythme sinusal entre **50 et 100 bpm**)\n"
                "- **Pacemaker naturel du cœur**\n"
                "- Non enregistrable sur l'ECG de surface (amplitude trop faible)"
            )),
            FicheRow(concept="Vascularisation du nœud sinusal", detail_md=(
                "- Vascularisé par une branche de l'**artère coronaire droite** "
                "ou de l'**artère circonflexe**"
            )),
            FicheRow(concept="◆ Deux mécanismes de la dysfonction sinusale", detail_md=(
                "- Anomalies de l'**automatisme sinusal**\n"
                "- Troubles de conduction : perte de la transmission de l'activité "
                "électrique à l'atrium droit par **bloc sinoatrial (BSA)**"
            )),
            FicheRow(concept="◆ Épidémiologie", detail_md=(
                "- Le plus souvent associée au **vieillissement** (fibrose)\n"
                "- Affecte **0,03 %** de la population\n"
                "- Prévalence augmente avec l'âge\n"
                "- Souvent associée à une atteinte plus globale de l'oreillette et à la "
                "**fibrillation atriale (FA)** : maladie rythmique atriale ou "
                "syndrome bradycardie-tachycardie"
            )),
            FicheRow(concept="Influences extrinsèques", detail_md=(
                "- Système nerveux autonome :\n"
                "  - **Sympathique** : augmente la fréquence\n"
                "  - **Parasympathique** : la diminue\n"
                "- Dysfonction sinusale possible uniquement de mécanisme vagal\n"
                "- Peut suivre la prise d'un médicament bradycardisant"
            )),
            FicheRow(concept="Rythme de secours", detail_md=(
                "- En cas de dysfonction sinusale permanente ou avec pauses prolongées\n"
                "- Un rythme d'échappement peut naître du **NAV** (rythme de secours)"
            )),
        ]),
        SousPartie(lettre="B", titre="Présentation clinique", rows=[
            FicheRow(concept="◆ Tableaux cliniques possibles", detail_md=(
                "- Asymptomatique pendant de nombreuses années (forme latente)\n"
                "- Signes liés à la baisse du débit sanguin cérébral (bradycardie/pauses) :\n"
                "  - Lipothymies, **syncopes à l'emporte-pièce (Adams-Stokes)**\n"
                "  - Pseudovertiges (symptômes trompeurs)\n"
                "- Signes liés à la réduction du débit cardiaque :\n"
                "  - Réduction de la capacité à l'effort, dyspnée d'effort, asthénie\n"
                "  - Angor, insuffisance cardiaque\n"
                "- Palpitations ou embolie artérielle (si FA associée, maladie rythmique atriale)\n"
                "- Sujet âgé : peut se révéler par une **détérioration des fonctions cognitives**"
            )),
            FicheRow(concept="", detail_md=(
                "- Chez le sujet âgé : signes trompeurs (**chutes à répétition**, "
                "**déclin cognitif**) à toujours évoquer.\n"
                "- Toujours rechercher la prise de **bradycardisants** y compris collyres "
                "(bêtabloquants)."
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Étiologies", rows=[
            FicheRow(concept="Causes intrinsèques (souvent permanentes)", detail_md=(
                "- **Âge, vieillissement** (fibrose)\n"
                "- Maladie coronarienne chronique et aiguë : ischémie, infarctus\n"
                "- Cardiomyopathies, myocardites, cardiopathies congénitales, tumeurs cardiaques\n"
                "- Maladies infiltratives : **sarcoïdose**, **amylose**, **hémochromatose**\n"
                "- Maladies systémiques : connectivites\n"
                "- Post-chirurgicales : chirurgie valvulaire, cure de CIA, transplantation\n"
                "- Troubles conductifs héréditaires, cardiomyopathies ou dystrophies neuromusculaires héréditaires"
            )),
            FicheRow(concept="Causes extrinsèques (souvent réversibles)", detail_md=(
                "- Prise médicamenteuse :\n"
                "  - Bêtabloquants, inhibiteurs calciques bradycardisants\n"
                "  - Amiodarone ou autres antiarythmiques, ivabradine\n"
                "  - Digitalique, clonidine\n"
                "- Origine vagale :\n"
                "  - **Hypertonie vagale** (athlète)\n"
                "  - Réflexe vagal (malaise vasovagal), **hypersensibilité sinocarotidienne**\n"
                "- Atteinte du SNC : HTIC, syndromes méningés\n"
                "- Troubles hydroélectrolytiques : **hyperkaliémie**\n"
                "- Hypoxie, hypercapnie, acidose sévère, **SAOS**\n"
                "- Hypothermie, hypothyroïdie, ictère rétentionnel sévère"
            )),
        ]),
        SousPartie(lettre="D", titre="Diagnostic ECG", rows=[
            FicheRow(concept="◆ Critères ECG de dysfonction sinusale", detail_md=(
                "- Bradycardie sinusale inappropriée en éveil :\n"
                "  - **< 50 bpm le jour**\n"
                "  - **< 40 bpm la nuit** chez l'adulte\n"
                "- Absence d'accélération de la FC à l'effort : **incompétence chronotrope**\n"
                "- Pauses sinusales sans onde P pathologiques **> 3 secondes**\n"
                "- BSA du 2ᵉ ou 3ᵉ degré\n"
                "- Syndrome bradycardie-tachycardie ou pauses post-réductionnelles\n"
                "- Pause sinusale symptomatique **> 3 s** au massage sinocarotidien ou au tilt-test"
            )),
            FicheRow(concept="Pause ou arrêt sinusal", detail_md=(
                "- Mécanisme : anomalie d'automatisme sinusal ou (le plus souvent) "
                "**BSA du 3ᵉ degré paroxystique**\n"
                "- ECG : pause cardiaque sans onde P visible (asystolie) s'interrompant par :\n"
                "  - Une activité atriale ≠ onde P sinusale (échappement atrial)\n"
                "  - Ou un complexe QRS jonctionnel non précédé d'onde P (échappement jonctionnel)"
            )),
            FicheRow(concept="◆ Bloc sinoatrial du 1ᵉʳ degré", detail_md=(
                "- Allongement du temps de conduction entre nœud sinusal et oreillette\n"
                "- **Pas de traduction ECG**"
            )),
            FicheRow(concept="◆ BSA du 2ᵉ degré", detail_md=(
                "- Blocage intermittent de la conduction entre NS et oreillette\n"
                "- **Type I (Wenckebach sinoatrial)** : ondes P irrégulières jusqu'à survenue "
                "d'une pause < double du cycle sinusal le plus court\n"
                "- **Type II** : pauses inopinées ou régulières dont le cycle correspond à un "
                "multiple du cycle sinusal (2/1, 3/1)"
            )),
            FicheRow(concept="◆ BSA du 3ᵉ degré", detail_md=(
                "- Bradycardie à échappement jonctionnel (QRS fins)\n"
                "- Sans activité atriale sinusale visible (activité atriale rétrograde parfois visible)"
            )),
            FicheRow(concept="◆ Insuffisance chronotrope", detail_md=(
                "- Incapacité à accélérer la fréquence sinusale à l'effort\n"
                "- Seuil pathologique : **FC max < 75 % de la FC max théorique**\n"
                "- Holter : courbe de fréquence aplatie"
            )),
            FicheRow(concept="Bradycardie sinusale inappropriée", detail_md=(
                "- Bradycardie sinusale marquée **< 50 bpm le jour**\n"
                "- En absence de causes extrinsèques\n"
                "- En général bien tolérée, symptômes possibles avec l'âge"
            )),
            FicheRow(concept="◆ Maladie rythmique de l'oreillette", detail_md=(
                "- **Syndrome brady/tachy** : dysfonction sinusale + troubles du rythme atrial coexistants\n"
                "- **Pauses post-réductionnelles** : pauses sinusales à l'arrêt du trouble "
                "du rythme atrial (sidération du nœud sinusal)"
            )),
        ]),
        SousPartie(lettre="E", titre="Évaluation et urgence", rows=[
            FicheRow(concept="Méthodes diagnostiques", detail_md=(
                "- **ECG 12 dérivations** ou monitorage / enregistrement holter\n"
                "- Corrélation symptômes/anomalies indispensable (journal des symptômes au holter)\n"
                "- Si symptômes peu fréquents : enregistreur externe longue durée "
                "ou **moniteur cardiaque implantable**\n"
                "- Test d'effort : utile pour les insuffisances chronotropes\n"
                "- **Massage sinocarotidien** : démasque les pauses dans l'hypersensibilité sinocarotidienne\n"
                "- **Tilt-test** : si mécanisme vagal suspecté (pauses sinusales / BSA d'origine vagale)\n"
                "- Exploration électrophysiologique endocavitaire (EEP) : "
                "non recommandée systématiquement ; envisagée pour exploration de syncope "
                "(reco ESC 2018, classe IIb)"
            )),
            FicheRow(concept="Enquête étiologique", detail_md=(
                "- Au minimum si dysfonction sinusale sévère symptomatique :\n"
                "  - **Échocardiographie**\n"
                "  - Bilan biologique : ionogramme sanguin, créatinine, **troponine**\n"
                "  - Recherche clinique de causes extrinsèques\n"
                "- Autres examens sur signe d'appel"
            )),
            FicheRow(concept="◆ Degré d'urgence", detail_md=(
                "- **Hospitalisation en urgence** si :\n"
                "  - **BSA du 3ᵉ degré**\n"
                "  - Syncope avec dysfonction sinusale à l'ECG\n"
                "- Autres cas : gestion différée ambulatoire"
            )),
            FicheRow(concept="", detail_md=(
                "- Dysfonction sinusale par **hypervagotonie** (athlète d'endurance) : "
                "il ne faut pas traiter.\n"
                "- Dysfonction sinusale **dégénérative liée à l'âge** : il faut souvent traiter, "
                "souvent associée à FA et à des troubles conductifs du NAV (fibrose étendue)."
            ), kind="mnemo"),
        ]),
    ])

    # ── PARTIE III : BLOCS ATRIOVENTRICULAIRES ──
    partie_iii = Partie(numero="III", titre="Blocs atrioventriculaires (BAV)", sous_parties=[
        SousPartie(lettre="A", titre="Physiopathologie et mécanismes", rows=[
            FicheRow(concept="Anatomie du NAV et du faisceau de His", detail_md=(
                "- **NAV** : oreillette droite, en avant et en haut de l'ostium du sinus coronaire\n"
                "- **Faisceau de His** : seule communication entre oreillettes et ventricules\n"
                "- Chemine dans le septum membraneux sous la racine de l'aorte"
            )),
            FicheRow(concept="Conduction nodale vs hissienne", detail_md=(
                "- Cellules nodales : conduction **décrémentielle lente**, dépendante du "
                "courant entrant de calcium\n"
                "  - **Phénomène de Wenckebach** : allongement progressif de la conduction dans le "
                "NAV quand fréquence de stimulation atriale ↑, jusqu'à atteindre la période réfractaire\n"
                "- His-Purkinje : conduction rapide, loi du **tout ou rien**"
            )),
            FicheRow(concept="Système nerveux autonome", detail_md=(
                "- NAV : sous étroite dépendance du SNA (≠ His-Purkinje)\n"
                "  - Sympathique : ↑ vitesse de conduction\n"
                "  - Parasympathique : ↓ vitesse de conduction"
            )),
            FicheRow(concept="Vascularisation", detail_md=(
                "- NAV : branche de l'**artère coronaire droite** (artère du NAV) "
                "naissant de la croix des sillons\n"
                "- Faisceau de His et branches : **première branche septale de l'IVA** + "
                "artère du NAV"
            )),
            FicheRow(concept="◆ Pronostic du BAV complet selon le siège", detail_md=(
                "| Siège | Échappement | Fréquence | Pronostic |\n"
                "|---|---|---|---|\n"
                "| **BAV nodal** | Nodohissien haut | **40-60/min** | Stable |\n"
                "| **BAV infranodaux** | Bas | **15-40/min** | Instable, lent, grave |"
            )),
            FicheRow(concept="Épidémiologie", detail_md=(
                "- **Vieillissement** : cause la plus fréquente\n"
                "- Prévalence **4/10 000** dans la population adulte\n"
                "- Augmente avec l'âge"
            )),
        ]),
        SousPartie(lettre="B", titre="Présentation clinique", rows=[
            FicheRow(concept="◆ Tableaux cliniques d'un BAV", detail_md=(
                "- Totalement asymptomatique : BAV du 1ᵉʳ degré, plupart des BAV du 2ᵉ degré\n"
                "- Signes de baisse du débit cérébral (bradycardie/pauses) :\n"
                "  - Lipothymies, **syncopes à l'emporte-pièce (Adams-Stokes)**, pseudovertiges\n"
                "- Signes de réduction du débit cardiaque (BAV chronique avec bradycardie permanente) :\n"
                "  - Réduction des capacités à l'effort, dyspnée, asthénie chronique, "
                "angor, insuffisance cardiaque\n"
                "  - Plus rarement avec BAV du 1ᵉʳ degré et PR très long\n"
                "- **BAV « fréquence-dépendant »** (siège intra/infrahissien) : symptômes "
                "à l'effort uniquement (dyspnée, angor, blocpnée d'effort)\n"
                "- Sujet âgé : détérioration des fonctions cognitives"
            )),
            FicheRow(concept="◆ Complication grave : torsade de pointes", detail_md=(
                "- BAV peut se révéler ou s'accompagner de **fibrillation ventriculaire** "
                "consécutive à une **torsade de pointes**\n"
                "- Favorisée par :\n"
                "  - Bradycardie\n"
                "  - Allongement de l'intervalle QT\n"
                "- Traitement : **isoprénaline** ± stimulation cardiaque pour accélérer la FC"
            )),
        ]),
        SousPartie(lettre="C", titre="Étiologies", rows=[
            FicheRow(concept="Causes intrinsèques", detail_md=(
                "- Âge : causes dégénératives avec fibrose ± calcifications, "
                "**maladie de Lenègre**\n"
                "- Maladie coronarienne chronique\n"
                "- Infarctus du myocarde :\n"
                "  - **IDM inférieur** : siège nodal, bon pronostic, souvent régressif\n"
                "  - **IDM antérieur** : siège hissien/infrahissien, très mauvais pronostic "
                "(infarctus étendu, insuffisance cardiaque, choc)\n"
                "- Angor spastique\n"
                "- Cardiomyopathies, malformations, tumeurs cardiaques\n"
                "- Maladies infiltratives : sarcoïdose, amylose, hémochromatose, maladie de Fabry\n"
                "- Maladies systémiques (connectivites)\n"
                "- Post-chirurgicales : chirurgie valvulaire / **TAVI**, "
                "cardiopathies congénitales, myomectomie septale\n"
                "- Traumatique : cathétérisme, ablation par radiofréquence\n"
                "- Troubles conductifs héréditaires, maladies neuromusculaires héréditaires\n"
                "- Radique post-radiothérapie\n"
                "- Infectieuses : endocardites bactériennes (abcès de l'anneau), "
                "**maladie de Lyme** (myocardite), myocardites virales\n"
                "- Rétrécissement aortique calcifié dégénératif\n"
                "- BAV congénital"
            )),
            FicheRow(concept="Causes extrinsèques", detail_md=(
                "- Prise médicamenteuse : bêtabloquant, inhibiteurs calciques bradycardisants, "
                "amiodarone ou autre antiarythmique, digitalique\n"
                "- Hypertonie vagale (athlète) ou réflexe vagal (vasovagal)\n"
                "- Troubles hydroélectrolytiques : **hyperkaliémie**"
            )),
            FicheRow(concept="◆ Particularité du His-Purkinje", detail_md=(
                "- Faible sensibilité aux facteurs extrinsèques\n"
                "- Siège plus fréquent de **BAV dégénératifs** (paroxystiques ou permanents)\n"
                "- BAV permanents ou paroxystiques\n"
                "- Toujours rechercher une cause aiguë réversible : "
                "ischémique, métabolique, infectieuse, inflammatoire, médicamenteuse"
            )),
        ]),
        SousPartie(lettre="D", titre="Diagnostic ECG", rows=[
            FicheRow(concept="◆ Critères de description d'un BAV", detail_md=(
                "- **Type de bloc** : 1ᵉʳ, 2ᵉ ou 3ᵉ degré\n"
                "- Caractère : paroxystique vs permanent ; congénital vs acquis\n"
                "- **Siège** ++ : nodal ou infranodal"
            )),
            FicheRow(concept="◆ Caractéristiques des blocs nodaux", detail_md=(
                "- BAV du 1ᵉʳ degré, BAV du 2ᵉ degré Mobitz 1, "
                "BAV complet à **échappement nodohissien stable QRS fins 40-60 bpm**\n"
                "- Améliorés par : **atropine**, **isoprénaline**, effort\n"
                "- Aggravés par : massage sinocarotidien"
            )),
            FicheRow(concept="◆ Caractéristiques des blocs hissiens / infrahissiens", detail_md=(
                "- Surviennent au préalable sur des blocs de branche\n"
                "- Responsables de **BAV du 2ᵉ degré Mobitz 2** et **BAV du 3ᵉ degré à échappement infranodal**\n"
                "- BAV complet : rythme d'échappement inconstant, instable, lent **< 35-40 bpm**\n"
                "- Risque de décès par **asystolie et torsades de pointes**\n"
                "- Améliorés par : massage sinocarotidien, isoprénaline\n"
                "- Aggravés par : atropine, effort"
            )),
            FicheRow(concept="★ ◆ BAV du 1ᵉʳ degré", detail_md=(
                "- Allongement fixe et constant de l'intervalle **PR > 200 ms**"
            )),
            FicheRow(concept="★ ◆ BAV du 2ᵉ degré Mobitz 1 (Luciani-Wenckebach)", detail_md=(
                "- **Allongement progressif de l'intervalle PR** jusqu'à observation d'une "
                "seule onde P bloquée\n"
                "- Suivie d'une onde P conduite avec un PR plus court\n"
                "- Parfois associé à un BAV 2/1\n"
                "- En règle nodal, **QRS fins < 120 ms** le plus souvent"
            )),
            FicheRow(concept="★ ◆ BAV du 2ᵉ degré Mobitz 2", detail_md=(
                "- Survenue inopinée d'une seule onde P bloquée\n"
                "- **Pas d'allongement du PR** précédant l'onde P bloquée\n"
                "- Évolution fréquente vers le BAV complet\n"
                "- En règle infranodal, le plus souvent QRS larges"
            )),
            FicheRow(concept="◆ BAV de haut degré (assimilé Mobitz 2)", detail_md=(
                "- Plusieurs ondes P bloquées consécutives\n"
                "- Ou conduction rythmée : ex. BAV 3:1 (2 ondes P bloquées + 1 conduite)\n"
                "- Évolution fréquente vers le BAV complet\n"
                "- En règle infranodal, QRS larges"
            )),
            FicheRow(concept="◆ BAV 2/1 (inclassable Mobitz 1 ou 2)", detail_md=(
                "- 2 ondes P pour un QRS\n"
                "- Largeur du QRS = orientation du siège :\n"
                "  - **QRS larges** : siège infranodal\n"
                "  - QRS fins : en faveur du siège nodal"
            )),
            FicheRow(concept="★ ◆ BAV du 3ᵉ degré ou complet", detail_md=(
                "- Aucune onde P conduite\n"
                "- **Activités atriale et ventriculaire dissociées**\n"
                "- Battements ventriculaires < battements atriaux\n"
                "- Échappement de fréquence variable selon le siège\n"
                "- Siège orienté par la durée du QRS et la fréquence de l'échappement\n"
                "- QT susceptible de s'allonger : **risque de torsades de pointes**"
            )),
            FicheRow(concept="BAV complet + FA/flutter atrial", detail_md=(
                "- Bradycardie au lieu de la tachycardie habituelle de la FA\n"
                "- Rythme ventriculaire régulier au lieu des irrégularités liées à la FA\n"
                "- QRS fins ou larges selon le siège du bloc"
            )),
            FicheRow(concept="", detail_md=(
                "- Une durée de **QRS < 120 ms** est très en faveur d'un bloc nodal.\n"
                "- ⚠ Les **BAV intrahissiens** sont rares mais constituent un piège "
                "(QRS souvent fins)."
            ), kind="piege"),
        ]),
        SousPartie(lettre="E", titre="Formes cliniques et évaluation", rows=[
            FicheRow(concept="BAV dégénératif du sujet âgé", detail_md=(
                "- Forme clinique la plus fréquente\n"
                "- Symptômes parfois atypiques : activité réduite, bas débit cérébral\n"
                "- Toujours évoquer une cause iatrogène associée (médicaments)\n"
                "- Largeur du QRS = indication du siège"
            )),
            FicheRow(concept="★ ◆ BAV complet sur IDM inférieur", detail_md=(
                "- **2-5 %** des cas\n"
                "- Plus fréquent en IDM inférieur qu'antérieur\n"
                "- Siège **nodal** (> 90 %)\n"
                "- Progressif : précédé de BAV du 1ᵉʳ puis 2ᵉ degré QRS fins, parfois asymptomatiques\n"
                "- Échappement le plus souvent QRS fins\n"
                "- Mécanisme vagal (précoce) ou ischémique\n"
                "- Atteinte de l'artère du NAV\n"
                "- **Bon pronostic en soi** (surmortalité liée à dégâts myocardiques)\n"
                "- ⚠ Favorisé par les bêtabloquants ou la reperfusion\n"
                "- **CI aux bêtabloquants en aigu** si BAV\n"
                "- En règle régressif, bonne réponse à l'atropine\n"
                "- **Isoprénaline CONTRE-INDIQUÉE** dans l'IDM aigu\n"
                "- Stimulation temporaire si mal toléré\n"
                "- Non régressif à **J5** : discuter stimulateur définitif"
            )),
            FicheRow(concept="◆ BAV complet sur IDM antérieur", detail_md=(
                "- Beaucoup plus rare, siège **infranodal**\n"
                "- Témoigne d'un IDM étendu\n"
                "- Survenue brutale, souvent précédé d'un bloc de branche\n"
                "- Mortalité importante liée à l'étendue de la nécrose\n"
                "- Stimulation temporaire le plus souvent nécessaire\n"
                "- **Isoprénaline CI** dans l'IDM aigu\n"
                "- Stimulation définitive plus fréquente en cas de non-régression"
            )),
            FicheRow(concept="◆ BAV congénital", detail_md=(
                "- **3-5 % des BAV**\n"
                "- Filles ++ (60 %)\n"
                "- **1/20 000 naissances**\n"
                "- Le plus souvent immunologique : passage transplacentaire d'**anticorps "
                "anti-Ro/SSA** maternels (lupus, syndrome de Gougerot-Sjögren)\n"
                "- Parfois génétique\n"
                "- Diagnostic possible : bradycardie fœtale ou néonatale"
            )),
            FicheRow(concept="BAV chez les patients en FA permanente", detail_md=(
                "- = **Bradyarythmie** (≠ maladie rythmique atriale qui associe FA souvent "
                "paroxystique + dysfonction sinusale)\n"
                "- FA permanente lente avec :\n"
                "  - **Pauses pathologiques > 3 s**\n"
                "  - Rythme lent régulier = BAV du 3ᵉ degré\n"
                "  - Rythme lent irrégulier = BAV du 2ᵉ degré"
            )),
            FicheRow(concept="Méthodes diagnostiques", detail_md=(
                "- ECG suffit si le bloc est permanent\n"
                "- Holter ou moniteur cardiaque implantable si BAV non permanent\n"
                "- **EEP** indiquée si :\n"
                "  - Bilan de syncope avec troubles conductifs intraventriculaires (BB ou bifasciculaire)\n"
                "  - Mesure de l'intervalle HV : **HV ≥ 70 ms** = pathologique, signant une "
                "atteinte infrahissienne\n"
                "  - Bloc intrahissien : H dédoublé (H1-H2), plus rare"
            )),
            FicheRow(concept="Enquête étiologique", detail_md=(
                "- Rechercher cause aiguë curable / réversible :\n"
                "  - SCA (territoire inférieur ++)\n"
                "  - Médicament bradycardisant\n"
                "  - **Hyperkaliémie**\n"
                "  - Myocardite\n"
                "- Au minimum : ionogramme, **échocardiographie**, troponine\n"
                "- Sujet jeune < 50 ans ou contexte évocateur : bilan approfondi\n"
                "  - Myocardite (inflammatoire/infectieuse) : **IRM cardiaque**\n"
                "  - Cause génétique"
            )),
            FicheRow(concept="◆ Degré d'urgence", detail_md=(
                "- **Hospitalisation** si :\n"
                "  - BAV du 3ᵉ degré\n"
                "  - BAV du 2ᵉ degré Mobitz 2\n"
                "  - BAV de haut degré\n"
                "- Autres cas : différée et ambulatoire"
            )),
        ]),
    ])

    # ── PARTIE IV : BLOCS DE BRANCHE ──
    partie_iv = Partie(numero="IV", titre="Blocs de branche", sous_parties=[
        SousPartie(lettre="A", titre="Physiopathologie et clinique", rows=[
            FicheRow(concept="Anatomie des branches du faisceau de His", detail_md=(
                "- Le faisceau de His se divise en :\n"
                "  - **Branche droite**\n"
                "  - **Branche gauche** qui se subdivise en fascicules :\n"
                "    - Hémibranche antérieure fine\n"
                "    - Hémibranche postérieure épaisse\n"
                "- Ramifications en réseau de Purkinje (même nature histologique)"
            )),
            FicheRow(concept="◆ Propriétés des branches", detail_md=(
                "- Peu sensibles aux effets du système nerveux autonome\n"
                "- Cellules peu sensibles à l'ischémie\n"
                "- Quasiment dépourvues d'activité mécanique\n"
                "- Un bloc de branche = ralentissement ou interruption de la "
                "conduction dans une branche"
            )),
            FicheRow(concept="◆ Présentation clinique", detail_md=(
                "- **Bloc de branche isolé = TOUJOURS asymptomatique**\n"
                "- Découverte :\n"
                "  - Fortuite (ECG de contrôle)\n"
                "  - Au cours du suivi d'une maladie cardiovasculaire\n"
                "- Accompagné de **lipothymies / syncopes** = valeur de gravité immédiate :\n"
                "  - Présence d'une cardiopathie (surtout BBG)\n"
                "  - BAV paroxystique suspecté"
            )),
        ]),
        SousPartie(lettre="B", titre="Étiologies", rows=[
            FicheRow(concept="◆ Bloc de branche droit (BBD)", detail_md=(
                "- BBD isolé peut être **bénin = variante de la normale** "
                "(qu'il soit complet ou incomplet)\n"
                "- Mais peut témoigner d'une cardiopathie sous-jacente, surtout du ventricule droit\n"
                "- BBD quasi systématique dans :\n"
                "  - Cardiopathies congénitales touchant le VD\n"
                "  - Pathologie pulmonaire avec retentissement cardiaque (HTAP, "
                "séquelle d'embolie pulmonaire)"
            )),
            FicheRow(concept="◆ Bloc de branche gauche (BBG)", detail_md=(
                "- **N'est JAMAIS considéré comme bénin**\n"
                "- Soit dégénératif, soit associé à une cardiopathie"
            )),
            FicheRow(concept="BB sur syndrome coronarien aigu", detail_md=(
                "- Au cours d'un SCA : apparition possible d'un BBD ou BBG\n"
                "- **IDM antérieur + BBG** = atteinte infrahissienne de mauvais pronostic "
                "(lésions étendues, insuffisance cardiaque, choc cardiogénique)"
            )),
            FicheRow(concept="Autres causes", detail_md=(
                "- Identiques aux BAV :\n"
                "  - Électrolytiques : **hyperkaliémie** ++\n"
                "  - Médicaments bloquant le courant sodique : antiarythmiques de classe I "
                "(ex. **flécaïnide**), **antidépresseurs tricycliques**\n"
                "- Blocs de branche fréquence-dépendants : apparaissent quand la fréquence "
                "ventriculaire augmente"
            )),
        ]),
        SousPartie(lettre="C", titre="Diagnostic ECG", rows=[
            FicheRow(concept="◆ Précision du type", detail_md=(
                "- Incomplet si **QRS ≤ 120 ms** (peu de valeur sémiologique ou clinique)\n"
                "- Complet si **QRS > 120 ms**\n"
                "- Distinguer :\n"
                "  - Branche droite : QRS positif en V1\n"
                "  - Branche gauche : QRS négatif en V1\n"
                "  - Bifasciculaire ou trifasciculaire\n"
                "- Vérifier que le rythme est sinusal au préalable (BB peut être associé "
                "à une tachycardie supraventriculaire)"
            )),
            FicheRow(concept="◆ BBD complet", detail_md=(
                "- **QRS > 120 ms**\n"
                "- Axe normal\n"
                "- **V1** : QRS positif avec aspect **rsR'**\n"
                "- V6 : aspect qRs, onde S traînante souvent arrondie\n"
                "- aVR : aspect qR\n"
                "- Ondes T négatives en V1-V2 parfois V3\n"
                "- ⚠ Ne pas évoquer à tort une ischémie myocardique"
            )),
            FicheRow(concept="◆ BBG complet", detail_md=(
                "- **QRS > 120 ms**\n"
                "- Axe normal ou gauche\n"
                "- **V1** : QRS négatif aspect **rS ou QS**\n"
                "- aVR : aspect QS\n"
                "- D1, V6 : R avec notch\n"
                "- Ondes T négatives en D1, aVL, V5-V6\n"
                "- ⚠ Ne pas évoquer à tort une ischémie myocardique\n"
                "- Léger sus-décalage de ST V1-V2-V3 possible (≤ 1 mm le plus souvent)\n"
                "- ⚠ Ne pas évoquer à tort un SCA ST+\n"
                "- Diagnostic d'IDM gêné par le BBG : prise en charge comme **SCA ST+**"
            )),
            FicheRow(concept="◆ Hémibloc antérieur gauche (HBAG)", detail_md=(
                "- Déviation axiale gauche au-delà de **–45°** (négativité en D2)\n"
                "- **QRS < 120 ms**\n"
                "- D1-aVL : aspect qR\n"
                "- D2, D3, aVF : aspect rS (mnémo : **S3 > S2**)\n"
                "- V6 : onde S"
            )),
            FicheRow(concept="◆ Hémibloc postérieur gauche (HBPG)", detail_md=(
                "- Déviation axiale droite **> +90°** (négativité en D1, aspect S1Q3)\n"
                "- En l'absence de pathologie du ventricule droit ou de morphologie longiligne\n"
                "- **QRS < 120 ms**\n"
                "- D1-aVL : aspect RS ou Rs\n"
                "- D2, D3, aVF : aspect qR\n"
                "- Mnémotechnique : **S1Q3** (onde S en D1 et onde Q en D3)\n"
                "- Plus rare et potentiellement plus grave que HBAG"
            )),
            FicheRow(concept="◆ Blocs bifasciculaires", detail_md=(
                "- La sémiologie s'additionne :\n"
                "  - **BBD + HBAG**\n"
                "  - **BBD + HBPG**"
            )),
        ]),
        SousPartie(lettre="D", titre="Formes cliniques et prise en charge", rows=[
            FicheRow(concept="Bloc bifasciculaire avec perte de connaissance", detail_md=(
                "- Le plus souvent : **BBD + HBAG** (plus rarement BBD + HBPG)\n"
                "- BAV du 1ᵉʳ degré associé possible\n"
                "- Rechercher une cardiopathie sous-jacente\n"
                "- **EEP** indiquée pour mesurer la conduction infrahissienne\n"
                "- Si **HV ≥ 70 ms** : stimulateur cardiaque"
            )),
            FicheRow(concept="Blocs de branche de l'IDM antérieur", detail_md=(
                "- **10 % des cas**\n"
                "- Uni, bi ou trifasciculaire\n"
                "- Préexistant ou acquis pendant l'infarctus\n"
                "- Si acquis : nécrose septale étendue avec **risque de BAV complet brutal** "
                "+ asystolie + troubles du rythme ventriculaire"
            )),
            FicheRow(concept="◆ Bloc alternant", detail_md=(
                "- Association successive de BBD complet et BBG complet\n"
                "- Ou alternance HBAG / HBPG associée à un BBD complet\n"
                "- = **Bloc trifasciculaire** et équivalent de BAV complet paroxystique "
                "de siège infrahissien\n"
                "- Grave, nécessite un **appareillage**"
            )),
            FicheRow(concept="◆ Situations à risque vital (hospitalisation)", detail_md=(
                "- Blocs alternants = équivalent BAV de haut degré\n"
                "- Syncopes typiques + troubles conductifs à l'ECG\n"
                "- Autres cas : différé en ambulatoire"
            )),
            FicheRow(concept="Bloc de branche + syncope", detail_md=(
                "- En l'absence de documentation de BAV du 2ᵉ ou 3ᵉ degré : **EEP**\n"
                "- Si EEP normale : **moniteur cardiaque implantable**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Une syncope chez un patient porteur d'une cardiopathie + bloc de branche "
                "**ne suffit PAS** à attribuer la PC à un BAV paroxystique.\n"
                "- Évoquer également une **tachycardie ventriculaire**."
            ), kind="piege"),
            FicheRow(concept="◆ Constatation d'un BBG ou BBD - bilan", detail_md=(
                "- BBG : rechercher **HTA méconnue**, cardiopathie sous-jacente ; "
                "à défaut = bloc dégénératif\n"
                "- BBD : rechercher pathologie pulmonaire ou ventriculaire droite\n"
                "- **Échographie cardiaque** systématique\n"
                "- BBD typique chez le sujet jeune asymptomatique = variante de la normale"
            )),
        ]),
    ])

    # ── PARTIE V : THÉRAPEUTIQUE ──
    partie_v = Partie(numero="V", titre="Thérapeutique et suivi du patient", sous_parties=[
        SousPartie(lettre="A", titre="Urgences et signes de gravité", rows=[
            FicheRow(concept="◆ Tolérance hémodynamique - mauvaise tolérance", detail_md=(
                "- Lipothymie / syncope\n"
                "- Angor\n"
                "- Insuffisance cardiaque\n"
                "- Signes de choc : hypotension artérielle, oligurie, signes "
                "neurologiques de bas débit\n"
                "- **Torsade de pointes**"
            )),
            FicheRow(concept="◆ Troubles conductifs à risque vital (hospitalisation USIC)", detail_md=(
                "- BAV du 3ᵉ degré\n"
                "- BAV du 2ᵉ degré Mobitz 2\n"
                "- BAV de haut degré\n"
                "- Blocs alternants\n"
                "- BSA du 3ᵉ degré\n"
                "- Syncopes typiques avec troubles conductifs à l'ECG"
            )),
            FicheRow(concept="◆ Hiérarchie de gravité", detail_md=(
                "- **Bradycardie par BAV complet > bradycardie par dysfonction sinusale**\n"
                "- Risque plus élevé de torsades de pointes et asystolie dans le BAV"
            )),
            FicheRow(concept="Prise en charge initiale en USIC", detail_md=(
                "- Transfert USIC\n"
                "- Scope ECG : surveillance du rythme\n"
                "- Surveillance paramètres vitaux : pouls, PA, FR, saturation, diurèse\n"
                "- Thérapeutique urgente pour restaurer une fréquence ventriculaire adaptée"
            )),
            FicheRow(concept="◆ Causes aiguës réversibles à rechercher", detail_md=(
                "- **IDM ST+** : sus-décalage de ST, douleur thoracique, troponine\n"
                "  - ⚠ BBG ou BAV 3ᵉ avec QRS larges = **ECG NON informatif** : "
                "discuter coronarographie urgente si suspicion clinique\n"
                "- Médicaments bradycardisants : à arrêter\n"
                "- **Hyperkaliémie** : à rechercher (insuffisance rénale, médicament hyperkaliémiant)\n"
                "  - Ondes T amples et pointues à l'ECG"
            )),
            FicheRow(concept="Échocardiographie", detail_md=(
                "- Recherche cardiopathie associée\n"
                "- Évaluation de la fonction ventriculaire gauche"
            )),
            FicheRow(concept="◆ Prévention de la torsade de pointes", detail_md=(
                "- Éviter les molécules allongeant le QT\n"
                "- Corriger une hypokaliémie\n"
                "- Survenue d'une torsade de pointes = signe de gravité"
            )),
            FicheRow(concept="Réanimation et stimulation", detail_md=(
                "- Être prêt à : réanimation cardio-respiratoire\n"
                "- Stimulation cardiaque temporaire :\n"
                "  - Sonde d'entraînement percutanée\n"
                "  - Stimulation externe transthoracique\n"
                "- En cas d'échec des médicaments ou de trouble du rythme ventriculaire"
            )),
        ]),
        SousPartie(lettre="B", titre="Moyens thérapeutiques", rows=[
            FicheRow(concept="◆ Atropine", detail_md=(
                "- Substance **tachycardisante** (effets chronotrope et dromotrope positifs)\n"
                "- Prescrite en **bolus IV**\n"
                "- Action transitoire\n"
                "- Exclusivement sur les **BAV nodaux ou la dysfonction sinusale**"
            )),
            FicheRow(concept="◆ Isoprénaline (= isoprotérénol)", detail_md=(
                "- Substance tachycardisante en perfusion continue\n"
                "- Action prolongée\n"
                "- Efficace sur l'ensemble des troubles conductifs en général\n"
                "- ⚠ **CONTRE-INDIQUÉE dans l'IDM aigu**"
            )),
            FicheRow(concept="Stimulation cardiaque temporaire", detail_md=(
                "- Percutanée :\n"
                "  - Sonde d'entraînement électrosystolique\n"
                "  - Stimulateur externe temporaire\n"
                "- Externe transthoracique : douloureuse, solution de secours\n"
                "- En cas de non-réponse à l'isoprénaline + mauvaise tolérance hémodynamique\n"
                "- ⚠ Complications sonde : **tamponnade**, **thrombose**"
            )),
            FicheRow(concept="◆ Traitement spécifique torsade de pointes", detail_md=(
                "- Accélérer la FC : **isoprénaline** ou stimulation percutanée\n"
                "- Corriger hypomagnésémie / hypokaliémie\n"
                "- Arrêter tout médicament allongeant le QT"
            )),
            FicheRow(concept="◆ Stimulateur cardiaque définitif - types", detail_md=(
                "- Indiqué en cas de trouble conductif symptomatique ou de haut degré "
                "sans cause aiguë réversible\n"
                "- Implantation par voie subclavière en règle générale\n"
                "- Trois types :\n"
                "  - **Simple chambre** : stimule le ventricule (électrode VD) en mode **VVI**\n"
                "  - **Double chambre** : stimule oreillette + ventricule en mode **DDD**\n"
                "  - **Biventriculaire** : VD + VG (sonde supplémentaire dans branche veineuse "
                "latérale gauche du sinus coronaire) = **resynchronisation**"
            )),
            FicheRow(concept="Innovations en stimulation", detail_md=(
                "- Stimulation physiologique de l'aire de la branche gauche : "
                "alternative émergente, QRS stimulés plus fins\n"
                "- **Stimulateurs sans sonde** : capsule implantée par voie veineuse fémorale "
                "dans le ventricule droit (stimule uniquement le VD)\n"
                "- Stimulateurs double chambre sans sonde en développement"
            )),
            FicheRow(concept="◆ Code de programmation à 4 lettres", detail_md=(
                "| Lettre | Signification | Codes |\n"
                "|---|---|---|\n"
                "| **1ʳᵉ** | Cavité stimulée | **A** (oreillette), **V** (ventricule), **D** (double) |\n"
                "| **2ᵉ** | Cavité où l'activité électrique est détectée | A, V, D (même code) |\n"
                "| **3ᵉ** | Mode de fonctionnement | **I** (inhibé), **T** (triggered), **D** (mixte) |\n"
                "| **4ᵉ** | Asservissement (accélération avec activité physique) | **R** |"
            )),
            FicheRow(concept="Pose du stimulateur", detail_md=(
                "- Geste effectué sous anesthésie locale ou sous sédation\n"
                "- Au bloc opératoire\n"
                "- Consentement éclairé du patient\n"
                "- Asepsie rigoureuse (risques infectieux)"
            )),
        ]),
        SousPartie(lettre="C", titre="Indications de stimulation définitive", rows=[
            FicheRow(concept="◆ Indications dans la dysfonction sinusale", detail_md=(
                "- Uniquement si **symptomatique** avec preuve du lien de causalité "
                "bradycardie/symptômes et absence de cause réversible\n"
                "- Exception : nécessité de maintenir des médicaments bradycardisants "
                "(contrôle FA rapide / pathologie cardiaque sous-jacente : bêtabloquants)\n"
                "- **Syncopes avec pauses sinusales > 3 s**\n"
                "- **Pauses > 6 s** même asymptomatiques\n"
                "- Syndrome du sinus carotidien documenté chez sujet **> 40 ans**\n"
                "- Parfois : bradycardies sévères diurnes < 40 bpm à symptômes modestes\n"
                "- Insuffisances chronotropes symptomatiques"
            )),
            FicheRow(concept="◆ Indications dans les BAV", detail_md=(
                "- **BAV du 3ᵉ degré** : en l'absence de cause curable ou réversible\n"
                "- BAV du 2ᵉ degré :\n"
                "  - Évocateurs d'un siège infrahissien\n"
                "  - Ou symptomatiques quel que soit leur siège\n"
                "- Blocs alternants\n"
                "- Bloc infranodal à l'EEP avec **HV ≥ 70 ms** en cas de syncope"
            )),
            FicheRow(concept="◆ Choix du type de stimulateur", detail_md=(
                "- Dysfonction sinusale ou BAV : **stimulateur double chambre**\n"
                "- Bradyarythmie (BAV sur FA permanente) : **stimulateur simple chambre VVI**\n"
                "- BAV + FEVG basse (< 50 %) :\n"
                "  - Stimulateur biventriculaire avec **resynchronisation**\n"
                "  - Ou stimulateur double chambre avec stimulation physiologique de l'aire "
                "de la branche gauche"
            )),
            FicheRow(concept="Référentiel", detail_md=(
                "- Recommandations européennes **ESC 2021** sur la stimulation cardiaque et la "
                "resynchronisation"
            )),
        ]),
        SousPartie(lettre="D", titre="Traitement des blocs de branche", rows=[
            FicheRow(concept="Principes généraux", detail_md=(
                "- La plupart des blocs de branche sont acquis et non réversibles "
                "(dégénératif / cardiopathie)\n"
                "- Rechercher une cause ou facteur aggravant réversible "
                "(**hyperkaliémie**, médicament à stopper)\n"
                "- Pas de traitement spécifique en général"
            )),
            FicheRow(concept="◆ Indications de stimulateur", detail_md=(
                "- Syncope + EEP avec **HV ≥ 70 ms** = stimulateur cardiaque\n"
                "- Si EEP normale : moniteur cardiaque implantable "
                "(recherche de BAV de haut degré paroxystique)\n"
                "- **Bloc de branche alternant** = équivalent BAV de haut degré, appareillage"
            )),
            FicheRow(concept="◆ Indication de resynchronisation", detail_md=(
                "- **BBG ≥ 130 ms** chez le patient insuffisant cardiaque\n"
                "- + **FEVG ≤ 35 %**\n"
                "- Discuter resynchronisation par stimulateur (ou défibrillateur selon les cas) "
                "biventriculaire"
            )),
            FicheRow(concept="Surveillance", detail_md=(
                "- En l'absence d'indication de stimulateur : surveillance clinique et ECG\n"
                "- L'atteinte du tissu de conduction peut être évolutive\n"
                "- Sauf BBD typique sur cœur sain (pas évolutif)"
            )),
        ]),
        SousPartie(lettre="E", titre="Éducation et surveillance du patient appareillé", rows=[
            FicheRow(concept="Suivi technique post-implantation", detail_md=(
                "- Radiographie de thorax : vérifier la position des sondes\n"
                "- Contrôle des paramètres avec un programmateur dédié\n"
                "- Suivi à **1-3 mois**, puis annuel au sein du centre implanteur\n"
                "  - Vérification télémétrique (usure de la pile, intégrité des sondes)\n"
                "  - Consultation des mémoires embarquées, reprogrammation si besoin"
            )),
            FicheRow(concept="◆ Information patient", detail_md=(
                "- Carnet / carte avec caractéristiques techniques de la prothèse\n"
                "- Interférences possibles avec champs électromagnétiques de forte puissance\n"
                "- Modalités IRM\n"
                "- Surveillance de l'état cutané (rougeur, écoulement) et douleur au niveau du boîtier\n"
                "- Consulter si : signes locaux, fièvre inexpliquée, infections respiratoires à répétition\n"
                "- Contrôles annuels au centre d'implantation\n"
                "- Télésurveillance complémentaire possible\n"
                "- Changement du boîtier en fin de vie : **tous les 8 à 12 ans**"
            )),
            FicheRow(concept="◆ IRM et stimulateur", detail_md=(
                "- Contre-indication absolue en cours de disparition\n"
                "- Plupart des dispositifs récents : **IRM-conditionnels**\n"
                "- Réglage particulier en mode IRM avant l'examen\n"
                "- Reprogrammation après l'IRM (sauf certains modèles)"
            )),
            FicheRow(concept="Item 17 - Télémédecine", detail_md=(
                "- Dispositifs de télésurveillance des prothèses cardiaques implantables : "
                "stimulateurs, défibrillateurs, moniteurs cardiaques implantables\n"
                "- Transmission automatique des éléments pertinents au médecin\n"
                "- Évite des déplacements inutiles, réaction plus rapide en cas de dysfonctionnement / trouble du rythme\n"
                "- Téléconsultations de suivi et téléalertes programmées\n"
                "- Tous les dispositifs récents en sont équipés : manuelle (patient) ou automatique"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Hiérarchie des troubles conductifs et échappements", markdown=(
            "| Type | Siège | Échappement | Fréquence | QRS | Stabilité | Gravité |\n"
            "|---|---|---|---|---|---|---|\n"
            "| Dysfonction sinusale | Suprahissien (NS) | NAV | 40-60 bpm | Fins | Stable | Moindre |\n"
            "| BAV nodal | Suprahissien | Nodohissien | 40-60 bpm | Fins | Stable | Moindre |\n"
            "| BAV hissien | Hissien | Faisceau de His | 35-45 bpm | Fins | Instable | Élevée |\n"
            "| BAV infrahissien | Infrahissien | Branches / ventricules | < 40 bpm | Larges | Instable | Élevée ++ |"
        )),
        TableauSynthese(titre="Comparaison BAV Mobitz 1 vs Mobitz 2", markdown=(
            "| Critère | Mobitz 1 (Luciani-Wenckebach) | Mobitz 2 |\n"
            "|---|---|---|\n"
            "| Intervalle PR | **Allongement progressif** puis blocage | **Pas d'allongement**, blocage inopiné |\n"
            "| Siège | **Nodal** | **Infranodal** |\n"
            "| QRS | Le plus souvent fins (< 120 ms) | Le plus souvent larges |\n"
            "| Évolution vers BAV complet | Rare | **Fréquente** |\n"
            "| Pronostic | Plutôt bénin | **Grave** |\n"
            "| Indication stimulateur | Si symptomatique | **Oui** (haut risque) |"
        )),
        TableauSynthese(titre="Classification complète des BAV : degré, siège, QRS, symptômes", markdown=(
            "| Degré | Siège | QRS | Symptômes |\n"
            "|---|---|---|---|\n"
            "| **BAV 1ᵉʳ degré** | Généralement nodal, exceptionnellement infrahissien | QRS fins sauf BB associé | Non (sauf PR très long) |\n"
            "| **BAV 2ᵉ Mobitz 1** | Toujours nodal | QRS fins sauf BB associé | ± |\n"
            "| **BAV 2ᵉ Mobitz 2** | Toujours hissien ou infrahissien | QRS fins (intrahissien) ou plus souvent larges | ± |\n"
            "| **BAV haut degré** | Hissien ou infrahissien, rarement nodal | QRS larges (fins si nodal/intrahissien sauf BB) | **Oui** |\n"
            "| **BAV 3ᵉ degré (complet)** | Nodal, hissien ou infrahissien | Échappement QRS fins si nodal/intrahissien, larges si infrahissien | **Oui** |"
        )),
        TableauSynthese(titre="Caractéristiques ECG des principaux blocs de branche", markdown=(
            "| Critère | BBD complet | BBG complet | HBAG | HBPG |\n"
            "|---|---|---|---|---|\n"
            "| Durée QRS | > 120 ms | > 120 ms | < 120 ms | < 120 ms |\n"
            "| Axe | Normal | Normal ou gauche | < –45° | > +90° |\n"
            "| V1 | rsR' (positif) | rS ou QS (négatif) | – | – |\n"
            "| V6 | qRs (S traînante) | R avec notch | onde S | – |\n"
            "| D1 / D2 / D3 | – | – | qR en D1-aVL, rS en D2-3 (**S3 > S2**) | RS en D1, qR en D2-3 (**S1Q3**) |\n"
            "| Bénin possible | Oui si isolé | **NON, jamais** | – | Plus grave |"
        )),
        TableauSynthese(titre="Effets des manœuvres et médicaments sur les BAV", markdown=(
            "| Action | BAV nodaux | BAV hissien / infrahissien |\n"
            "|---|---|---|\n"
            "| **Atropine** | **Améliore** | Aggrave |\n"
            "| **Isoprénaline** | Améliore | **Améliore** |\n"
            "| **Effort** | Améliore | Aggrave |\n"
            "| **Massage sinocarotidien** | Aggrave | **Améliore** |"
        )),
        TableauSynthese(titre="Choix du type de stimulateur cardiaque définitif", markdown=(
            "| Situation | Type de stimulateur |\n"
            "|---|---|\n"
            "| Dysfonction sinusale | **Double chambre (DDD)** |\n"
            "| BAV (rythme sinusal) | **Double chambre (DDD)** |\n"
            "| Bradyarythmie (BAV sur FA permanente) | **Simple chambre VVI** |\n"
            "| BAV + FEVG < 50 % | **Biventriculaire (resynchronisation)** ou DDD + stimulation physiologique branche G |\n"
            "| BBG ≥ 130 ms + IC + FEVG ≤ 35 % | **Resynchronisation** (stimulateur ou défibrillateur biventriculaire) |"
        )),
    ]

    # ── CHIFFRES CLÉS ──
    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|---|---|---|\n"
        "| Rythme sinusal normal | **50-100 bpm** | Fréquence physiologique |\n"
        "| Bradycardie sinusale en éveil | **< 50 bpm** | Critère dysfonction sinusale |\n"
        "| Bradycardie sinusale nuit (adulte) | **< 40 bpm** | Critère dysfonction sinusale |\n"
        "| Pause sinusale pathologique | **> 3 secondes** | Au holter |\n"
        "| Pause sinusale tilt / MSC | **> 3 s symptomatique** | Hypersensibilité sinocarotidienne |\n"
        "| Insuffisance chronotrope | **FC max < 75 % FC max théorique** | Test d'effort |\n"
        "| Échappement nodohissien (NAV) | **40-60 bpm**, QRS fins, stable | BAV nodal complet |\n"
        "| Échappement faisceau de His | **35-45 bpm**, QRS fins, instable | BAV hissien |\n"
        "| Échappement infrahissien | **15-40 bpm** (souvent < 40), QRS larges, instable | BAV infrahissien |\n"
        "| Taille du nœud sinusal | **1 à 2 cm** | Forme en croissant |\n"
        "| Prévalence dysfonction sinusale | **0,03 %** | Population générale |\n"
        "| Prévalence des BAV | **4/10 000** | Population adulte |\n"
        "| BAV complet sur IDM | **2-5 %** | Plus fréquent en IDM inférieur |\n"
        "| BAV congénital | **3-5 % des BAV** ; **1/20 000** naissances ; 60 % filles | Anti-Ro/SSA maternels |\n"
        "| Bloc de branche dans IDM antérieur | **10 %** | Uni/bi/trifasciculaire |\n"
        "| PR pathologique (BAV 1) | **> 200 ms** | Allongement fixe et constant |\n"
        "| QRS normal | **≤ 120 ms** | Bloc incomplet si ≤ 120 ms |\n"
        "| QRS de bloc complet | **> 120 ms** | BBD ou BBG complet |\n"
        "| HV pathologique | **≥ 70 ms** | Atteinte infrahissienne à l'EEP |\n"
        "| BBG indication resynchronisation | **≥ 130 ms** | + IC + FEVG ≤ 35 % |\n"
        "| FEVG seuil resynchronisation | **≤ 35 %** | Indication BIVR |\n"
        "| FEVG seuil pacing biventriculaire en cas de BAV | **< 50 %** | Sélection du type de stim. |\n"
        "| Pause asymptomatique indication PM | **> 6 secondes** | Pauses sinusales |\n"
        "| Pause symptomatique indication PM | **> 3 secondes** | Avec syncope |\n"
        "| Sinus carotidien (PM) | **> 40 ans** documenté | Indication |\n"
        "| Bradycardie sévère diurne | **< 40 bpm** symptomatique modeste | Parfois indication PM |\n"
        "| BAV non régressif IDM inf. | **J5** | Discuter stimulateur |\n"
        "| Durée de vie batterie PM | **8 à 12 ans** | Changement de boîtier |\n"
        "| Suivi PM | **1-3 mois puis annuel** | Centre implanteur |\n"
        "| Déviation axiale HBAG | **< –45°** | Négativité en D2 |\n"
        "| Déviation axiale HBPG | **> +90°** | S1Q3 |"
    ))

    # ── POINTS CLÉS ──
    points_cles = [
        "Trois cadres : **dysfonction sinusale**, **BAV**, **blocs de branche**",
        "Plus la lésion est **distale**, plus l'échappement est lent/instable et plus le tableau est **grave**",
        "**BAV 1** : PR > 200 ms fixe ; **Mobitz 1** : PR croissant, nodal ; **Mobitz 2** : inopiné, infranodal",
        "**BAV complet** : QRS larges + bradycardie = **infranodal grave** ; QRS fins 40-60 = nodal stable",
        "**HBAG** fréquent (axe < -45°, S3>S2) ; **HBPG** rare et plus grave (axe > +90°, S1Q3)",
        "Causes aiguës : **SCA (IDM ST+)**, **bradycardisants**, **hyperkaliémie**. Vagales = bénignes",
        "Cause chronique la plus fréquente : **maladie de Lenègre** (fibrose dégénérative liée à l'âge)",
        "Examens : **holter** (DS) ; **EEP avec HV ≥ 70 ms** si syncope + bloc de branche",
        "**USIC** : BAV 3°, Mobitz 2, haut degré, blocs alternants, BSA 3°, syncope + trouble conductif",
        "**Stimulation définitive** : DS symptomatique sans cause réversible ; BAV Mobitz 2, 3°, haut degré",
    ]

    # ── FICHE ÉCLAIR ──
    fiche_eclair_md = (
        "**Hiérarchie** : NAV 40-60 fins stable / His 35-45 fins instable / infrahissien < 40 "
        "larges instable. Plus distal = plus grave.\n\n"
        "**Dysfonction sinusale** : bradycardie < 50 jour ou < 40 nuit, pauses > 3 s, BSA 1-2-3°, "
        "insuffisance chronotrope. Hypervagotonie athlète : pas de traitement.\n\n"
        "**BAV 1** : PR > 200 ms fixe. **Mobitz 1** : PR ↗ progressif, nodal, QRS fins. "
        "**Mobitz 2** : blocage inopiné, infranodal, QRS larges, évolue vers BAV complet. "
        "**BAV 3°** : dissociation AV, risque torsade de pointes.\n\n"
        "**Étiologies BAV** : Lenègre (âge), IDM inf. (nodal, bon pronostic) vs ant. "
        "(infranodal, mauvais), TAVI, sarcoïdose/Lyme, BAV congénital (filles, anti-Ro/SSA).\n\n"
        "**Blocs de branche** : isolé = asymptomatique. BBD V1 rsR' (peut être bénin). "
        "BBG V1 rS/QS, JAMAIS bénin, gêne IDM (traiter SCA ST+). HBAG axe < –45° S3 > S2. "
        "HBPG axe > +90° S1Q3. Bloc alternant = équivalent BAV complet = appareillage.\n\n"
        "**Bilan** : ECG, holter, EEP si BB + syncope (HV ≥ 70 ms pathologique), écho, IRM si "
        "sujet jeune.\n\n"
        "**Urgences USIC** : BAV 3°, Mobitz 2, haut degré, blocs alternants, BSA 3°, syncope + "
        "trouble conductif. Causes aiguës : IDM ST+, bradycardisants, hyperkaliémie.\n\n"
        "**Traitement aigu** : atropine (BAV nodaux/DS). Isoprénaline (tous, CI IDM). "
        "Stimulation temporaire si échec.\n\n"
        "**PM (ESC 2021)** : DS symptomatique ; pauses > 6 s ou > 3 s + syncope ; BAV 3°, "
        "Mobitz 2, blocs alternants, HV ≥ 70 ms + syncope. DDD (BAV/DS), VVI (bradyarythmie FA), "
        "biventriculaire (FEVG < 50 %). Resynchronisation : BBG ≥ 130 ms + IC + FEVG ≤ 35 %. "
        "Batterie 8-12 ans, dispositifs IRM-conditionnels."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 236 - Troubles de la conduction intracardiaque",
        annee="2025-2026",
        item="Item 236",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 236",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-236_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

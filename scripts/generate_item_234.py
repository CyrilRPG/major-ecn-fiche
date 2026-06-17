"""Génère la fiche de l'Item 234 - Insuffisance cardiaque de l'adulte (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Généralités", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition"),
            PlanSousPartie(lettre="B", titre="Épidémiologie"),
            PlanSousPartie(lettre="C", titre="Physiopathologie et mécanismes compensateurs"),
            PlanSousPartie(lettre="D", titre="IC à FE diminuée, légèrement diminuée, préservée"),
            PlanSousPartie(lettre="E", titre="Désynchronisation et arythmies"),
        ]),
        PlanPartie(numero="II", titre="Diagnostic positif", sous_parties=[
            PlanSousPartie(lettre="A", titre="Signes fonctionnels"),
            PlanSousPartie(lettre="B", titre="Signes physiques"),
            PlanSousPartie(lettre="C", titre="ECG et radiographie thoracique"),
            PlanSousPartie(lettre="D", titre="Peptides natriurétiques (BNP / NT-proBNP)"),
            PlanSousPartie(lettre="E", titre="Échocardiographie et examens complémentaires"),
        ]),
        PlanPartie(numero="III", titre="Diagnostic étiologique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Cardiopathies ischémiques et HTA"),
            PlanSousPartie(lettre="B", titre="Cardiomyopathies (CMD, CMH, restrictives)"),
            PlanSousPartie(lettre="C", titre="Valvulopathies, troubles du rythme, péricarde"),
            PlanSousPartie(lettre="D", titre="IC droite et IC à débit augmenté"),
        ]),
        PlanPartie(numero="IV", titre="Formes cliniques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Insuffisance cardiaque aiguë et OAP"),
            PlanSousPartie(lettre="B", titre="Choc cardiogénique et facteurs déclenchants"),
            PlanSousPartie(lettre="C", titre="IC chronique et IC à FE préservée"),
        ]),
        PlanPartie(numero="V", titre="Évolution, complications, pronostic", sous_parties=[
            PlanSousPartie(lettre="A", titre="Histoire naturelle"),
            PlanSousPartie(lettre="B", titre="Principales complications"),
            PlanSousPartie(lettre="C", titre="Facteurs pronostiques et comorbidités"),
        ]),
        PlanPartie(numero="VI", titre="Traitement de l'IC chronique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Étiologique, préventif et hygiénodiététique"),
            PlanSousPartie(lettre="B", titre="Médicamenteux de l'IC à FE diminuée"),
            PlanSousPartie(lettre="C", titre="Traitement électrique (DAI, CRT)"),
            PlanSousPartie(lettre="D", titre="IC à FE préservée et IC terminale"),
        ]),
        PlanPartie(numero="VII", titre="Traitement de l'IC aiguë", sous_parties=[
            PlanSousPartie(lettre="A", titre="Œdème aigu pulmonaire"),
            PlanSousPartie(lettre="B", titre="Poussée d'IC sans OAP franc"),
            PlanSousPartie(lettre="C", titre="Choc cardiogénique et CHAMPIT"),
        ]),
    ]

    # ── PARTIE I : GÉNÉRALITÉS ──
    partie_i = Partie(numero="I", titre="Généralités", sous_parties=[
        SousPartie(lettre="A", titre="Définition", rows=[
            FicheRow(concept="◆ Définition physiopathologique", detail_md=(
                "- Incapacité du cœur à délivrer un **débit adapté** aux besoins de l'organisme\n"
                "- Et/ou à fonctionner avec des **pressions de remplissage normales**\n"
                "- Toutes les pathologies cardiovasculaires non dépistées/traitées à temps peuvent y conduire"
            )),
            FicheRow(concept="◆ Définition clinique (ESC 2021)", detail_md=(
                "- **Syndrome** associant :\n"
                "  - symptômes (dyspnée, œdème des chevilles, fatigue)\n"
                "  - parfois associés à des signes cliniques (tachycardie, crépitants, turgescence jugulaire)\n"
                "  - causés par une anomalie de structure ou de fonction du cœur\n"
                "- Entraînant un débit cardiaque insuffisant et/ou une augmentation des pressions intracardiaques à l'effort ou au repos\n"
                "- Origines possibles : myocardique, valvulaire, péricardique, anomalie du rythme ou de la conduction"
            )),
            FicheRow(concept="", detail_md=(
                "- Le diagnostic est difficile : les symptômes ne sont pas spécifiques, "
                "les signes ne sont pas sensibles (la rétention hydrosodée peut disparaître rapidement sous traitement).\n"
                "- Une **phase asymptomatique** (systolique ou diastolique) peut précéder l'apparition des signes : "
                "son dépistage permet l'instauration d'un traitement et l'amélioration du pronostic en cas de dysfonctionnement systolique."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Épidémiologie", rows=[
            FicheRow(concept="◆ Prévalence", detail_md=(
                "- **1 à 2 %** dans la population générale\n"
                "- Augmentation avec l'âge : âge moyen au diagnostic en Europe **75-80 ans**\n"
                "- Prévalence en augmentation (vieillissement de la population, meilleure prise en charge)\n"
                "- L'incidence standardisée sur l'âge tend à diminuer"
            )),
        ]),
        SousPartie(lettre="C", titre="Physiopathologie et mécanismes compensateurs", rows=[
            FicheRow(concept="Rappels hémodynamiques", detail_md=(
                "- **DC = VES × FC** (débit cardiaque = volume d'éjection systolique × fréquence cardiaque)\n"
                "- VES dépend de la précharge (remplissage VG / étirement des fibres en fin de diastole), "
                "de la postcharge (forces s'opposant à l'éjection) et de la contractilité (inotropie)\n"
                "- VES = VTD − VTS (volume télédiastolique − volume télésystolique)\n"
                "- **FE = (VTD − VTS) / VTD** : paramètre clé de la fonction systolique"
            )),
            FicheRow(concept="Conséquences du dysfonctionnement", detail_md=(
                "- Baisse du débit cardiaque ou incapacité à l'augmenter à l'effort\n"
                "- Augmentation des pressions de remplissage intraventriculaires :\n"
                "  - VG → OG → veines pulmonaires → capillaires → artères pulmonaires → cavités droites\n"
                "  - VD → OD → circulation veineuse systémique (stase hépatique, jugulaire)\n"
                "- **PCAP ≥ 25 mmHg** : passage de transsudat dans les alvéoles = **OAP cardiogénique**"
            )),
            FicheRow(concept="⚠ OAP cardiogénique vs lésionnel", detail_md=(
                "- OAP cardiogénique : **transsudat** par augmentation de la PCAP\n"
                "- OAP lésionnel (non cardiogénique) : **exsudat** par atteinte de la membrane alvéolocapillaire\n"
                "- Ne pas confondre — étiologies et traitements différents"
            )),
            FicheRow(concept="★ ◆ Mécanismes cardiaques compensateurs", detail_md=(
                "- **Remodelage cardiaque** : changements de la géométrie cardiaque\n"
                "  - Dilatation ventriculaire (hypertrophie excentrique) en cas d'altération de la FE — "
                "ex : IDM, CMD. Effet délétère : ↑ contrainte pariétale (proportionnelle au rayon)\n"
                "  - Hypertrophie des parois (hypertrophie concentrique) en cas de surcharge de pression (HTA, RA). "
                "**Loi de Laplace** : Contrainte = P × Rayon / Épaisseur. Effet délétère : ↑ travail cardiaque et rigidité\n"
                "- **Loi de Starling** : étirement des fibres ↑ inotropie jusqu'à une limite\n"
                "- Tachycardie sympathique : maintient le DC (DC = VES × FC). Effet délétère : ↑ MVO2"
            )),
            FicheRow(concept="★ ◆ Mécanismes extracardiaques compensateurs", detail_md=(
                "- Vasoconstriction (système sympathique + SRA) : maintient la pression de perfusion ; "
                "inhomogène (épargne cérébrale et coronaire, déficitaire en cutané, muscle, rein)\n"
                "- Rétention hydrosodée (↓ perfusion rénale + activation SRA) : ↑ volume circulant et précharge\n"
                "- Activation neurohormonale : système sympathique + **SRAA** (rénine-angiotensine-aldostérone)\n"
                "- Effets délétères : ↑ travail cardiaque, effets proarythmiques, "
                "toxicité directe des catécholamines sur les myocytes, signes congestifs (œdèmes, épanchements)"
            )),
            FicheRow(concept="", detail_md=(
                "- Les mécanismes compensateurs sont bénéfiques à court terme "
                "(maintien du DC et des pressions de perfusion) mais délétères à long terme "
                "(↑ travail et consommation d'O₂ du cœur, hypertrophie, fibrose) — "
                "c'est sur ces voies que reposent les traitements modernes (bêtabloquants, IEC/ARA2, antialdostérones)."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="IC à FE diminuée, légèrement diminuée, préservée", rows=[
            FicheRow(concept="★ ◆ Classification selon la FEVG", detail_md=(
                "| Type | FEVG | Mécanisme | Terrain |\n"
                "|------|------|-----------|---------|\n"
                "| **IC à FE diminuée** (HFrEF) | **≤ 40 %** | Défaut de **contraction et d'éjection**, VG dilaté | Toutes étiologies |\n"
                "| **IC à FE légèrement diminuée** (HFmrEF) | **41-49 %** | Forme intermédiaire (proche de l'HFrEF) | — |\n"
                "| **IC à FE préservée** (HFpEF) | **≥ 50 %** | Problème de **remplissage** ; VG souvent **non dilaté, parois épaissies, rigides** | Sujet âgé, femme, HTA, obésité |"
            )),
            FicheRow(concept="", detail_md=(
                "- L'IC à FE préservée représente **≥ 50 % des causes d'IC**, "
                "en particulier chez la femme et le sujet âgé.\n"
                "- La distinction a surtout des implications thérapeutiques : les essais médicamenteux "
                "ont inclus les patients sur des critères de FE."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="E", titre="Désynchronisation et arythmies", rows=[
            FicheRow(concept="Désynchronisation cardiaque", detail_md=(
                "- Tous les segments myocardiques ne se contractent pas de manière synchrone\n"
                "- Le plus souvent par trouble de conduction (typiquement **bloc de branche gauche**)\n"
                "- Dépolarisation de proche en proche : septum → paroi latérale (contraction latérale retardée)\n"
                "- Peut aggraver une IC → justifie la **resynchronisation (CRT)**"
            )),
            FicheRow(concept="Arythmies dans l'IC", detail_md=(
                "- **Fibrillation atriale** : favorisée par la dilatation atriale ; "
                "la perte de la systole atriale aggrave l'IC et augmente le risque d'AVC\n"
                "- Troubles du rythme ventriculaires (ESV, TV, FV) : favorisés par les plages de fibrose "
                "(réentrées), anomalies du couplage calcique, stimulation sympathique\n"
                "- **TV/FV** = origine de la plupart des morts subites → intérêt du **DAI**"
            )),
        ]),
    ])

    # ── PARTIE II : DIAGNOSTIC ──
    partie_ii = Partie(numero="II", titre="Diagnostic positif", sous_parties=[
        SousPartie(lettre="A", titre="Signes fonctionnels", rows=[
            FicheRow(concept="◆ Symptômes respiratoires", detail_md=(
                "- **Dyspnée d'effort** : fréquente mais peu spécifique, souvent révélatrice. "
                "Quantifiée par la **classification NYHA**\n"
                "- **Orthopnée** : dyspnée de décubitus (obligeant à dormir tête surélevée) — plus spécifique. "
                "Liée à la redistribution sanguine vers le thorax\n"
                "- **Dyspnée paroxystique nocturne** : réveille le patient, oblige à se lever — début d'OAP, plus spécifique"
            )),
            FicheRow(concept="Classification NYHA", detail_md=(
                "| Classe | Description |\n"
                "|--------|-------------|\n"
                "| **I** | Aucune limitation, pas de dyspnée pour les efforts ordinaires |\n"
                "| **II** | Limitation modérée : dyspnée pour les efforts importants |\n"
                "| **III** | Limitation importante : dyspnée pour les efforts modérés/quotidiens |\n"
                "| **IV** | Dyspnée de repos ou pour le moindre effort |"
            )),
            FicheRow(concept="⚠ Symptômes respiratoires trompeurs", detail_md=(
                "- **Asthme cardiaque** : bradypnée expiratoire avec respiration sifflante "
                "→ peut faire évoquer une cause pulmonaire à tort\n"
                "- Toux à l'effort ou au décubitus → évoquer l'IC\n"
                "- Hémoptysies (rarement isolées) : traduisent une hypertension veineuse pulmonaire"
            )),
            FicheRow(concept="OAP : présentation clinique", detail_md=(
                "- Crise d'étouffement obligeant à la position assise\n"
                "- Anxiété, sueurs, grésillement laryngé\n"
                "- Toux avec expectoration mousseuse\n"
                "- Forme spontanément résolutive = **subœdème pulmonaire**"
            )),
            FicheRow(concept="Autres symptômes", detail_md=(
                "- Fatigue de repos (hypotension) ou à l'effort\n"
                "- Prise de poids associée à des œdèmes\n"
                "- Faiblesse musculaire (rechercher une myopathie associée en cas de CMD)\n"
                "- Palpitations"
            )),
            FicheRow(concept="IC sévère ou terminale", detail_md=(
                "- **Respiration de Cheyne-Stokes** (syndrome d'apnées du sommeil, prévalence ↑ dans l'IC)\n"
                "- Troubles neurologiques : confusion par bas débit cérébral\n"
                "- Troubles digestifs : douleurs abdominales, nausées, vomissements"
            )),
            FicheRow(concept="◆ IC droite : hépatalgie", detail_md=(
                "- **Hépatalgie d'effort ou de repos** : pesanteur douloureuse de l'hypocondre droit\n"
                "- Secondaire à la distension de la capsule hépatique\n"
                "- Peut s'associer aux signes d'IC gauche → **IC globale**"
            )),
        ]),
        SousPartie(lettre="B", titre="Signes physiques", rows=[
            FicheRow(concept="Auscultation cardiaque", detail_md=(
                "- Choc de pointe dévié vers l'aisselle (dilatation VG)\n"
                "- Tachycardie modérée (souvent absente sous bêtabloquants)\n"
                "- Rythme irrégulier : FA, flutter, ESA/ESV\n"
                "- **Bruit de galop B3 protodiastolique** (difficile à rechercher par le non-spécialiste)\n"
                "- Éclat du B2 au foyer pulmonaire : HTAP\n"
                "- Souffles : IM ou IT fonctionnelle ; valvulopathie organique (IM, IA, RA, RM)"
            )),
            FicheRow(concept="Auscultation pulmonaire", detail_md=(
                "- Râles crépitants ou sous-crépitants, le plus souvent bilatéraux\n"
                "- Épanchement pleural : confirmé par RX, transsudat à la ponction "
                "(**protides < 30 g/L**)"
            )),
            FicheRow(concept="◆ Examen artériel", detail_md=(
                "- Pouls rapide (signe souvent absent sous bêtabloquants)\n"
                "- PAS variable : normale, basse ou élevée\n"
                "- **PAS < 100 mmHg** = facteur de gravité (↓ VES ou effet hypotenseur des médicaments)\n"
                "- OAP hypertensif : PA élevée contemporaine d'un OAP en cas d'IC hypertensive"
            )),
            FicheRow(concept="◆ Signes périphériques d'IC droite", detail_md=(
                "- **Turgescence jugulaire** : dilatation anormale de la jugulaire en position demi-assise — "
                "très spécifique (difficile chez l'obèse)\n"
                "- **Reflux hépatojugulaire** : turgescence après compression manuelle du foie\n"
                "- Hépatomégalie régulière, ferme, douloureuse — expansion systolique si IT volumineuse\n"
                "- Œdèmes périphériques : mous, blancs, indolores, prenant le godet, déclives "
                "(MI, région lombaire si alitement)\n"
                "- Ascite : tardive sauf atteinte tricuspidienne organique ou péricardite constrictive ; "
                "peut faire évoquer à tort une cause hépatique\n"
                "- Anasarque : forme évoluée"
            )),
            FicheRow(concept="Stade très avancé", detail_md=(
                "- Pouls alternant\n"
                "- Oligurie\n"
                "- Fonte musculaire / cachexie (perte d'appétit, déconditionnement, malabsorption, hypoperfusion mésentérique)\n"
                "- **Dyspnée de Cheyne-Stokes** (↓ sensibilité des centres respiratoires au CO₂)"
            )),
        ]),
        SousPartie(lettre="C", titre="ECG et radiographie thoracique", rows=[
            FicheRow(concept="ECG", detail_md=(
                "- Peu contributif pour le diagnostic positif\n"
                "- Peut orienter étiologiquement : ondes Q de nécrose, troubles du rythme\n"
                "- HVG/HVD ou hypertrophie atriale selon étiologie\n"
                "- ⚠ **Bloc de branche gauche (QRS > 120 ms)** : élément important "
                "(implications thérapeutiques = resynchronisation)"
            )),
            FicheRow(concept="◆ Radiographie thoracique : silhouette cardiaque", detail_md=(
                "- **Cardiomégalie : RCT > 0,5** (rapport cardiothoracique)\n"
                "- Absence de cardiomégalie ne remet pas en cause le diagnostic "
                "(fréquente dans l'IC à FE préservée)"
            )),
            FicheRow(concept="◆ Signes radiologiques de stase pulmonaire (par gravité croissante)", detail_md=(
                "- 1) Redistribution vasculaire des bases vers les sommets\n"
                "- 2) Œdème interstitiel : **lignes B de Kerley**, aspect flou des gros vaisseaux hilaires, "
                "images réticulonodulaires basales\n"
                "- 3) Œdème alvéolaire : opacités floconneuses à contours flous, hiles → périphérie, "
                "aspect en **« ailes de papillon »** ; bilatérales (formes unilatérales trompeuses possibles)\n"
                "- Épanchements pleuraux uni- ou bilatéraux"
            )),
        ]),
        SousPartie(lettre="D", titre="Peptides natriurétiques (BNP / NT-proBNP)", rows=[
            FicheRow(concept="◆ Indication et physiologie", detail_md=(
                "- Dosage recommandé en 1ʳᵉ intention pour le diagnostic d'IC, avec une **bonne VPN**\n"
                "- Synthétisés par les myocytes cardiaques étirés (augmentation de pression intracavitaire)"
            )),
            FicheRow(concept="★ ◆ Seuils pour ÉLIMINER une IC", detail_md=(
                "| Présentation | BNP | NT-proBNP |\n"
                "|--------------|-----|-----------|\n"
                "| Dyspnée aiguë (urgences) | **< 100 pg/mL** | **< 300 pg/mL** |\n"
                "| Présentation chronique (consultation) | **< 35 pg/mL** | **< 125 pg/mL** |"
            )),
            FicheRow(concept="◆ Seuils en faveur d'une origine cardiaque (dyspnée aiguë)", detail_md=(
                "| Âge | NT-proBNP en faveur de l'IC |\n"
                "|-----|------------------------------|\n"
                "| < 50 ans | **> 450 pg/mL** |\n"
                "| 50 à 75 ans | **> 900 pg/mL** |\n"
                "| > 75 ans | **> 1 800 pg/mL** |\n"
                "\n"
                "BNP en faveur de l'IC : **> 300 pg/mL** (dyspnée aiguë)"
            )),
            FicheRow(concept="Recommandations ESC 2021", detail_md=(
                "- Patient avec facteurs de risque d'IC + symptômes/signes/ECG anormal → doser les peptides natriurétiques\n"
                "- Si **BNP ≥ 35 pg/mL** ou **NT-proBNP ≥ 125 pg/mL** ou IC fortement suspectée "
                "ou peptides indisponibles → échocardiographie"
            )),
            FicheRow(concept="★ ⚠ Facteurs modifiant les valeurs", detail_md=(
                "- Augmentent le BNP/NT-proBNP : âge, insuffisance rénale, fibrillation atriale\n"
                "- Diminuent le BNP/NT-proBNP : obésité\n"
                "- L'interprétation doit toujours tenir compte des données cliniques"
            )),
        ]),
        SousPartie(lettre="E", titre="Échocardiographie et examens complémentaires", rows=[
            FicheRow(concept="★ ◆ ETT couplée au Doppler : examen clé", detail_md=(
                "- **Indispensable** en cas d'IC ou de suspicion\n"
                "- Définit le type d'IC selon la FEVG (≤ 40, 41-49, ≥ 50 %)\n"
                "- Recherche une étiologie curable\n"
                "- Renseigne sur les conséquences hémodynamiques et oriente le traitement"
            )),
            FicheRow(concept="ETT : éléments évalués", detail_md=(
                "- Taille du VG : diamètres ou volumes (VTD, VTS)\n"
                "- Fonction systolique : **FEVG = (VTD − VTS)/VTD** (valeurs normales > 50-60 %)\n"
                "- Taille et fonction du VD, taille de la VCI\n"
                "- Taille des atriums\n"
                "- Aspect des valves\n"
                "- Pressions de remplissage (semi-qualitatif)\n"
                "- Indices hémodynamiques : débit cardiaque, pressions pulmonaires"
            )),
            FicheRow(concept="ETT : orientation étiologique", detail_md=(
                "- Anomalie de cinétique segmentaire → cardiopathie ischémique\n"
                "- Valvulopathie organique (IM, IA, RM, RA)\n"
                "- Hypertrophie symétrique → cardiopathie hypertensive\n"
                "- Hypertrophie asymétrique (septum interventriculaire) → **CMH**"
            )),
            FicheRow(concept="Examens biologiques standards (ESC 2021)", detail_md=(
                "- Natrémie, kaliémie, créatininémie\n"
                "- BNP / NT-proBNP\n"
                "- Glycémie à jeun, HbA1c\n"
                "- Bilan lipidique\n"
                "- Bilan hépatique\n"
                "- TSHus\n"
                "- NFS\n"
                "- Ferritinémie + CST (coefficient de saturation de la transferrine)"
            )),
            FicheRow(concept="Coroscanner et coronarographie", detail_md=(
                "- **Coroscanner** : à privilégier si probabilité faible ou intermédiaire "
                "de coronaropathie, ou si tests d'ischémie non concluants\n"
                "- **Coronarographie** : si angor, probabilité intermédiaire/haute, ou ischémie documentée "
                "et patient candidat à la revascularisation\n"
                "- En cas de FEVG basse + coronaires normales → orientation vers **CMD**"
            )),
            FicheRow(concept="IRM cardiaque", detail_md=(
                "- Mesure de la FEVG si patient non échogène\n"
                "- Orientation étiologique : myocardite, DAVD, CMP primitive, sarcoïdose, amylose\n"
                "- Cardiopathie ischémique : **rehaussement tardif sous-endocardique** = séquelle d'IDM\n"
                "- Évaluation de la viabilité myocardique\n"
                "- Pronostic CMD : rehaussement tardif = marqueur de fibrose"
            )),
            FicheRow(concept="Autres examens", detail_md=(
                "- Scintigraphie isotopique : FE chez le non échogène, ischémie, viabilité, "
                "**amylose à transthyrétine** (technétium)\n"
                "- Holter 24 h ou plus : ESV, TV non soutenue, FA, troubles de conduction AV\n"
                "- Épreuve d'effort avec VO2 : capacité fonctionnelle, valeur pronostique "
                "(VO2 très abaissée → indication de **greffe cardiaque**)\n"
                "- Cathétérisme droit : mesure des pressions pulmonaires et du débit (thermodilution). "
                "**HTAP = PAPm > 25 mmHg**. Précieux avant greffe (résistances pulmonaires)"
            )),
            FicheRow(concept="Cathétérisme droit : valeurs normales", detail_md=(
                "| Paramètre | Valeur normale |\n"
                "|-----------|----------------|\n"
                "| Pression OD | **< 5 mmHg** |\n"
                "| Pression VD | **25/0 mmHg** |\n"
                "| PCAP / PAPO | **< 15 mmHg** |\n"
                "| HTAP | **PAPm > 25 mmHg** |\n"
                "| Débit cardiaque | **5 L/min** |\n"
                "| Index cardiaque | **3 L/min/m²** |\n"
                "| Résistances pulmonaires (CI greffe) | **> 5 unités Wood** |"
            )),
        ]),
    ])

    # ── PARTIE III : DIAGNOSTIC ÉTIOLOGIQUE ──
    partie_iii = Partie(numero="III", titre="Diagnostic étiologique", sous_parties=[
        SousPartie(lettre="A", titre="Cardiopathies ischémiques et HTA", rows=[
            FicheRow(concept="◆ Cardiopathies ischémiques", detail_md=(
                "- **1ʳᵉ cause d'IC**\n"
                "- Le plus souvent par infarctus du myocarde (un ou plusieurs) : perte de myocytes, "
                "fibrose, perte de contractilité segmentaire → baisse de la FEVG\n"
                "- Parfois ischémie chronique sans IDM constitué — la revascularisation peut restaurer la FE "
                "(**viabilité myocardique**)"
            )),
            FicheRow(concept="◆ HTA : mécanismes vers l'IC", detail_md=(
                "- Hypertrophie cardiaque + fibrose → altération diastolique → **IC à FE préservée** "
                "(>50 % des formes du sujet âgé)\n"
                "- Athérosclérose coronaire → IDM ou atteinte des petites artères\n"
                "- Intrication des deux mécanismes\n"
                "- Augmentation chronique de la postcharge → baisse de la FEVG avec hypertrophie pariétale"
            )),
        ]),
        SousPartie(lettre="B", titre="Cardiomyopathies (CMD, CMH, restrictives)", rows=[
            FicheRow(concept="Cardiomyopathies : définition", detail_md=(
                "- Maladies du muscle cardiaque\n"
                "- Diagnostic d'élimination : cause ischémique, valvulaire, congénitale, HTA exclues"
            )),
            FicheRow(concept="◆ Cardiomyopathie dilatée (CMD)", detail_md=(
                "- Atteinte du muscle → dilatation + baisse FEVG\n"
                "- **1ʳᵉ cause d'IC et de transplantation chez le sujet jeune**\n"
                "- 25 % familiale : maladie monogénique, transmission le plus souvent AD, "
                "pénétrance variable (augmente avec l'âge) ; gènes du sarcomère, cytosquelette, lamine\n"
                "- Toxiques : alcool, amphétamines, cocaïne\n"
                "- Myocardites virales (coxsackie, CMV, HHV-6, VIH) ou bactériennes (brucellose, borréliose), "
                "maladie de Chagas\n"
                "- Auto-immunes : sarcoïdose, Churg-Strauss, sclérodermie, lupus\n"
                "- Endocrines : dysthyroïdie, phéochromocytome, hypocalcémie d'hypoparathyroïdie\n"
                "- Nutritionnelles : carence en carnitine, thiamine, sélénium\n"
                "- Cardiomyopathie du péripartum\n"
                "- Médicamenteuses/chimio : chloroquine, clozapine, **anthracyclines**, **trastuzumab**\n"
                "- Cardiomyopathie de stress (**takotsubo**)"
            )),
            FicheRow(concept="★ ◆ Cardiomyopathie hypertrophique (CMH)", detail_md=(
                "- **Hypertrophie asymétrique du SIV**, cavité de taille normale ou petite, "
                "FE conservée, trouble du remplissage\n"
                "- 25 % ont une obstruction sous-aortique en systole = **CMH obstructive** "
                "(gradient VG-aorte)\n"
                "- Maladie familiale monogénique, transmission AD, mutations des protéines du sarcomère "
                "(chaîne lourde bêta de la myosine, protéine C cardiaque)\n"
                "- Autres rares : maladie de Fabry (glycogénose, déficit en alpha-galactosidase)\n"
                "- Variabilité clinique : asymptomatique ↔ IC, FA, mort subite\n"
                "- ◆ **1ʳᵉ cause de mort subite chez le jeune athlète**"
            )),
            FicheRow(concept="Cardiomyopathie restrictive", detail_md=(
                "- Plus rare\n"
                "- **Amylose cardiaque** : dépôts amyloïdes → infiltration extracellulaire, épaississement diffus, "
                "rigidité, difficulté de remplissage. Fonction systolique atteinte tardivement\n"
                "- Pronostic sévère dès l'apparition de l'IC"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant une IC à FEVG abaissée, toujours penser à éliminer une origine ischémique "
                "par la réalisation d'une coronarographie "
                "(ou coroscanner chez le sujet jeune)."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Valvulopathies, troubles du rythme, péricarde", rows=[
            FicheRow(concept="Valvulopathies gauches", detail_md=(
                "- Toutes peuvent se compliquer d'IC (IM, IA, RM, RA)\n"
                "- Tournant évolutif grave justifiant souvent une prise en charge radicale "
                "(remplacement, plastie, percutané)\n"
                "- ⚠ Particularité : le **RM** peut entraîner un **OAP** alors que le VG est non atteint"
            )),
            FicheRow(concept="Troubles du rythme ou de la conduction", detail_md=(
                "- Tachycardie rapide ou bradycardie extrême : peuvent causer ou déclencher l'IC\n"
                "- FA rapide permanente prolongée → **tachycardiomyopathie**\n"
                "- ESV fréquentes peuvent altérer la fonction\n"
                "- Le traitement du trouble du rythme guérit souvent l'IC"
            )),
            FicheRow(concept="Causes péricardiques", detail_md=(
                "- Épanchement péricardique abondant\n"
                "- Tamponnade\n"
                "- Péricardite chronique constrictive"
            )),
        ]),
        SousPartie(lettre="D", titre="IC droite et IC à débit augmenté", rows=[
            FicheRow(concept="◆ Étiologies d'IC droite", detail_md=(
                "- Cause la plus fréquente : **IC gauche** (→ ↑ pressions pulmonaires) = **IC globale**\n"
                "- IC droite isolée :\n"
                "  - Pathologies pulmonaires : hypoxémie → vasoconstriction artérielle pulmonaire = "
                "**cœur pulmonaire** (aigu = EP aiguë ; chronique = séquelles d'EP, BPCO)\n"
                "  - HTAP primitive ou secondaire (sclérodermie)\n"
                "  - DAVD (dysplasie arythmogène du VD)\n"
                "  - Pathologies tricuspidiennes isolées : IT post-traumatique, "
                "IT post-endocarditique chez le toxicomane, IT du syndrome carcinoïde\n"
                "  - Infarctus du VD\n"
                "  - Péricardite chronique constrictive"
            )),
            FicheRow(concept="◆ IC à débit augmenté", detail_md=(
                "- Augmentation permanente du débit → surcharge en volume → IC\n"
                "- Étiologies : anémies chroniques, fistules artério-veineuses "
                "(hémodialyse, Rendu-Osler), hyperthyroïdie, carence en thiamine (béribéri), "
                "maladie de Paget (rare)"
            )),
        ]),
    ])

    # ── PARTIE IV : FORMES CLINIQUES ──
    partie_iv = Partie(numero="IV", titre="Formes cliniques", sous_parties=[
        SousPartie(lettre="A", titre="Insuffisance cardiaque aiguë et OAP", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Apparition rapide de symptômes/signes d'altération de la pompe cardiaque\n"
                "- De novo chez un patient sans cardiopathie connue, ou aggravation chez un IC connu\n"
                "- **Hospitalisation** le plus souvent nécessaire (traitement IV)"
            )),
            FicheRow(concept="★ ◆ OAP cardiogénique : tableau clinique", detail_md=(
                "- **Une des grandes urgences cardiovasculaires**\n"
                "- Détresse respiratoire aiguë par inondation alvéolaire (transsudat capillaire → alvéoles)\n"
                "- Polypnée, orthopnée (position assise obligatoire)\n"
                "- Sueurs, cyanose\n"
                "- Grésillement laryngé\n"
                "- Toux avec **expectoration mousseuse saumonée**\n"
                "- Tirage sus-claviculaire et intercostal\n"
                "- **« Marée montante des râles crépitants »** : remontent d'autant plus haut que sévère\n"
                "- Poussée hypertensive parfois associée"
            )),
            FicheRow(concept="OAP : examens complémentaires", detail_md=(
                "- Ne doivent pas retarder le traitement\n"
                "- BNP/NT-proBNP : valeurs basses → remettent en cause l'origine cardiogénique\n"
                "- Troponine : élévation modérée possible sans coronaropathie aiguë\n"
                "- RX thorax : opacités floconneuses péri-hilaires bilatérales\n"
                "- GDS artériels : **hypoxie + hypocapnie**\n"
                "- ETT : cardiopathie sous-jacente, FEVG, pressions intracardiaques"
            )),
            FicheRow(concept="◆ Diagnostics différentiels d'une dyspnée aiguë", detail_md=(
                "| Étiologie | Éléments d'orientation |\n"
                "|-----------|------------------------|\n"
                "| **Pneumopathie aiguë** | Fièvre, foyer de crépitants localisé, opacité systématisée, BNP normal/peu ↑ |\n"
                "| **Embolie pulmonaire** | Contexte favorisant, auscultation souvent normale |\n"
                "| **Exacerbation BPCO** | ATCD, ronchi, sibilants, expectoration |\n"
                "| **Crise d'asthme** | ATCD, dyspnée expiratoire, sibilants |"
            )),
            FicheRow(concept="◆ Facteurs déclenchants d'une IC aiguë", detail_md=(
                "- **Rupture / mauvaise observance** du traitement (1ʳᵉ cause)\n"
                "- Écarts de régime (sel)\n"
                "- Surinfection bronchique\n"
                "- Troubles du rythme (notamment **FA**)\n"
                "- Anémie\n"
                "- Embolie pulmonaire\n"
                "- Dysthyroïdie (amiodarone)\n"
                "- Iatrogènes : antiarythmiques dépresseurs, bêtabloquants, **AINS**, "
                "**inhibiteurs calciques (diltiazem, vérapamil)**, ↓ excessive de précharge "
                "(diurétiques, vasodilatateurs)\n"
                "- Poussée hypertensive\n"
                "- Syndrome coronarien aigu, ischémie myocardique"
            )),
        ]),
        SousPartie(lettre="B", titre="Choc cardiogénique et facteurs déclenchants", rows=[
            FicheRow(concept="◆ Choc cardiogénique : définition", detail_md=(
                "- Tableau ultime d'une défaillance aiguë sévère\n"
                "- Baisse du débit → anoxie tissulaire\n"
                "- **Mauvais pronostic**"
            )),
            FicheRow(concept="◆ Choc cardiogénique : signes cliniques", detail_md=(
                "- **PAS < 90 mmHg** ou chute > 30 mmHg par rapport à la base, pendant ≥ 30 minutes\n"
                "- Troubles de la perfusion périphérique : extrémités froides, cyanosées, marbrées\n"
                "- **Oligurie < 20 mL/h**\n"
                "- Sueurs\n"
                "- Altération de la conscience : agitation, confusion\n"
                "- Diminution du débit mesuré à l'ETT"
            )),
            FicheRow(concept="Autres formes d'IC aiguë", detail_md=(
                "- Aggravation progressive de la dyspnée + signes congestifs (œdèmes)\n"
                "- IC droite isolée\n"
                "- IC aiguë au cours d'un syndrome coronarien aigu (double prise en charge)"
            )),
        ]),
        SousPartie(lettre="C", titre="IC chronique et IC à FE préservée", rows=[
            FicheRow(concept="IC chronique", detail_md=(
                "- État du patient en dehors d'une décompensation\n"
                "- Ambulatoire, gêne fonctionnelle variable\n"
                "- Traitement per os"
            )),
            FicheRow(concept="★ ◆ IC à FE préservée (HFpEF) : critères diagnostiques", detail_md=(
                "- **≥ 50 % des causes d'IC** (femme, sujet âgé)\n"
                "- 1) Symptômes/signes d'IC\n"
                "- 2) **FEVG ≥ 50 %** (en l'absence de valvulopathie significative, "
                "anomalie rythme/conduction, péricarde)\n"
                "- 3) Augmentation BNP/NT-proBNP\n"
                "- 4) Arguments pour ↑ des pressions de remplissage à l'ETT OU **HVG** OU **dilatation OG**"
            )),
            FicheRow(concept="HVG et dilatation OG : seuils ETT", detail_md=(
                "| Paramètre | Homme | Femme |\n"
                "|-----------|-------|-------|\n"
                "| Masse VG indexée (HVG) | **≥ 115 g/m²** | **≥ 95 g/m²** |\n"
                "| Volume OG indexé (dilatation) | **> 34 mL/m²** | **> 34 mL/m²** |"
            )),
        ]),
    ])

    # ── PARTIE V : ÉVOLUTION, COMPLICATIONS, PRONOSTIC ──
    partie_v = Partie(numero="V", titre="Évolution, complications, pronostic", sous_parties=[
        SousPartie(lettre="A", titre="Histoire naturelle", rows=[
            FicheRow(concept="Délais d'apparition", detail_md=(
                "- Très variable : minutes (infarctus étendu, IM aiguë, endocardite) → années (HTA)\n"
                "- Dépend de l'importance et du caractère progressif/soudain de l'agression\n"
                "- Dépend de la capacité d'adaptation de la pompe"
            )),
            FicheRow(concept="◆ Évolution typique", detail_md=(
                "- **Phase asymptomatique** (remodelage cardiaque)\n"
                "- **Phase symptomatique** : alternance stabilité / décompensations aiguës "
                "(souvent déclenchées par un facteur favorisant)\n"
                "- Remodelage inverse possible : sous traitement de l'IC ou de son étiologie "
                "(arrêt d'un toxique, guérison d'une myocardite, traitement d'HTA/arythmie), "
                "la fonction peut s'améliorer voire se normaliser"
            )),
        ]),
        SousPartie(lettre="B", titre="Principales complications", rows=[
            FicheRow(concept="◆ Mortalité", detail_md=(
                "- **50 % à 5 ans** en moyenne\n"
                "- **40-50 % par an** en cas d'IC grave (NYHA IV)\n"
                "- Décès principalement : mort subite (TV/FV) ou IC réfractaire"
            )),
            FicheRow(concept="Hospitalisations pour décompensation", detail_md=(
                "- IC = **1ʳᵉ cause d'hospitalisation après 65 ans**\n"
                "- Traitement par diurétiques IV ± inotropes en cas de bas débit\n"
                "- Une hospitalisation pour décompensation représente toujours un facteur de gravité"
            )),
            FicheRow(concept="Autres complications", detail_md=(
                "- Troubles du rythme : ventriculaires (ESV, TV) ou supraventriculaires (FA)\n"
                "- Thromboemboliques : AVC par thrombus cavitaire (FA, bas débit), EP (alitement)\n"
                "- Hypotension (souvent aggravée par les médicaments)\n"
                "- Troubles hydroélectrolytiques : dyskaliémie, hyponatrémie, insuffisance rénale\n"
                "- Anémie, carence martiale, syndrome d'apnées du sommeil"
            )),
        ]),
        SousPartie(lettre="C", titre="Facteurs pronostiques et comorbidités", rows=[
            FicheRow(concept="◆ Facteurs pronostiques", detail_md=(
                "- Cliniques : NYHA III/IV vs I/II, hospitalisations répétées, étiologie ischémique, "
                "hypotension, tachycardie, troubles du rythme ventriculaire\n"
                "- Hémodynamiques : FE basse, débit cardiaque diminué, pressions pulmonaires élevées\n"
                "- ECG : **QRS > 120 ms** (BBG)\n"
                "- Biologiques : hyponatrémie, ↑ BNP/NT-proBNP\n"
                "- Métaboliques : ↓ pic de VO2 à l'effort"
            )),
            FicheRow(concept="Comorbidités à prendre en charge", detail_md=(
                "- Cardiaques : HTA, maladie coronaire, FA, valvulopathies\n"
                "- Non cardiaques : diabète, obésité, pathologies respiratoires, "
                "insuffisance rénale, dyskaliémies, goutte, SAOS, carence martiale, anémie\n"
                "- Neurocognitives : démences, troubles cognitifs, AVC, troubles de l'humeur\n"
                "- Gériatriques : anorexie, sarcopénie, fragilité\n"
                "- Impact : ↓ tolérance aux traitements, erreurs médicamenteuses, effets indésirables"
            )),
            FicheRow(concept="", detail_md=(
                "- La prise en charge des comorbidités est essentielle pour améliorer la qualité de vie, "
                "réduire les réhospitalisations et augmenter la survie — elles sont aussi des causes "
                "fréquentes de décompensation cardiaque."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE VI : TRAITEMENT DE L'IC CHRONIQUE ──
    partie_vi = Partie(numero="VI", titre="Traitement de l'IC chronique", sous_parties=[
        SousPartie(lettre="A", titre="Étiologique, préventif et hygiénodiététique", rows=[
            FicheRow(concept="◆ Traitement étiologique et préventif", detail_md=(
                "- Contrôle HTA, correction d'une valvulopathie (chirurgie ou percutané)\n"
                "- Statines chez patients à haut risque CV ou MCV avérée\n"
                "- Diabète : privilégier les **gliflozines** chez les patients à haut risque CV\n"
                "- Reperfusion précoce à la phase aiguë de l'IDM ; revascularisation d'un muscle ischémique\n"
                "- Éviction des toxiques : alcool, cocaïne, tabac\n"
                "- Prévention de l'obésité, sédentarité\n"
                "- Surveillance des chimiothérapies cardiotoxiques\n"
                "- Contrôle des troubles du rythme"
            )),
            FicheRow(concept="◆ Régime hyposodé", detail_md=(
                "- **5 à 6 g/j de sel maximum**\n"
                "- Bannir la salière, ne pas saler l'eau de cuisson\n"
                "- Liste détaillée des aliments riches en sel à éviter\n"
                "- Éviter les sels de régime (contiennent du potassium)\n"
                "- Diététicien si dénutrition possible\n"
                "- ⚠ Écart de régime : augmenter la dose de diurétique le jour même ou le lendemain"
            )),
            FicheRow(concept="◆ Surveillance du poids et signes d'alerte", detail_md=(
                "- Pesée régulière ; consulter si **prise de 2-3 kg en 2-3 jours**\n"
                "- Perte de poids progressive sans œdème → dénutrition = mauvais pronostic\n"
                "- Signes d'alerte à connaître : ↑ dyspnée, orthopnée, œdème des MI, météorisme"
            )),
            FicheRow(concept="Alcool, tabac, activité physique", detail_md=(
                "- Arrêt total de l'alcool dans la CMD éthylique (régression partielle/totale possible)\n"
                "- Arrêt du tabac impératif (a fortiori si coronaropathie)\n"
                "- Activité physique régulière encouragée (marche, ne pas essouffler)\n"
                "- Pas de repos strict : le déconditionnement aggrave les symptômes\n"
                "- Réadaptation cardiaque recommandée"
            )),
            FicheRow(concept="Travail, vaccinations, contraception", detail_md=(
                "- Proscrire efforts physiques importants, transport en commun, horaires décalés ; "
                "invalidité possible si forme grave\n"
                "- Vaccinations : antigrippale, anti-Covid-19, antipneumococcique\n"
                "- Contraception : grossesse à risque ; contraceptifs minidosés en œstrogènes ou DIU"
            )),
        ]),
        SousPartie(lettre="B", titre="Médicamenteux de l'IC à FE diminuée", rows=[
            FicheRow(concept="★ ◆ Les 4 classes pronostiques (IC FE ≤ 40 % : I, A)", detail_md=(
                "Réduisent la mortalité et les hospitalisations :\n"
                "- **IEC** ou **ARNI** (sacubitril/valsartan) ou **ARA2**\n"
                "- **Bêtabloquants**\n"
                "- **Antagonistes des récepteurs aux minéralocorticoïdes (ARM)**\n"
                "- **Inhibiteurs du SGLT2 (gliflozines)**\n"
                "\nDans l'IC à FE 41-49 % : mêmes traitements mais **IIb, C**\n"
                "\nS'y ajoutent les **diurétiques de l'anse** pour contrôler la rétention hydrosodée"
            )),
            FicheRow(concept="★ ◆ Inhibiteurs de l'enzyme de conversion (IEC)", detail_md=(
                "- Tous patients FE diminuée, quelle que soit la NYHA\n"
                "- ↓ symptômes, mortalité, hospitalisations\n"
                "- Doses cibles : **énalapril 20 mg**, **captopril 150 mg**, **ramipril 10 mg**\n"
                "- Effets indésirables : hypotension, insuffisance rénale, toux"
            )),
            FicheRow(concept="◆ IEC : procédures d'introduction et surveillance", detail_md=(
                "- Commencer à faibles doses\n"
                "- Surveillance PA, créatinine, kaliémie une semaine après introduction et après chaque ↑\n"
                "- ↓ posologie ou arrêt si hypotension symptomatique ou **↑ créatinine > 20-30 %**\n"
                "- Vigilance : sujet âgé, déshydraté, fortes doses de diurétiques, "
                "diabétique, insuffisance rénale, **PAS < 100 mmHg**\n"
                "- Éviter l'association initiale IEC + antialdostérone\n"
                "- **AINS à proscrire**\n"
                "- **CI** : sténose bilatérale des artères rénales, ATCD d'**angio-œdème**, "
                "grossesse, hyperkaliémie"
            )),
            FicheRow(concept="ARA2 (recommandation I, B)", detail_md=(
                "- Bloquent le récepteur AT1 de l'angiotensine 2\n"
                "- Mieux tolérés (moins de toux)\n"
                "- Efficacité comparable aux IEC\n"
                "- Réservés aux intolérants aux IEC\n"
                "- Mêmes règles de prescription"
            )),
            FicheRow(concept="◆ Sacubitril/valsartan (ARNI)", detail_md=(
                "- Inhibe le SRA (via AT1) + la **néprilysine** (dégradation des peptides natriurétiques)\n"
                "- ↑ peptides natriurétiques → potentialise vasodilatation et natriurèse\n"
                "- Supérieur à l'énalapril : ↓ mortalité et hospitalisations pour IC aiguë (FE basse)\n"
                "- En 1ʳᵉ intention (IIb, B) ou en remplacement des IEC chez les patients restant symptomatiques (I, B)"
            )),
            FicheRow(concept="★ ◆ Bêtabloquants", detail_md=(
                "- IC symptomatique avec FE diminuée (et en post-IDM si FE basse même asymptomatique)\n"
                "- 4 molécules validées : **carvédilol, métoprolol, bisoprolol, nébivolol**\n"
                "- ↓ symptômes, mortalité, hospitalisations, mort subite par arythmie\n"
                "- ⚠ En cas de poussée aiguë : introduction uniquement chez patient stabilisé "
                "(introduction immédiate = **faute**)\n"
                "- Chez patient déjà traité, ne pas arrêter sauf difficulté de réponse ou choc cardiogénique"
            )),
            FicheRow(concept="◆ Bêtabloquants : procédures d'introduction", detail_md=(
                "- Patient stabilisé sans signe de décompensation "
                "(possible au décours d'une poussée avant sortie)\n"
                "- Très faibles doses (1/8ᵉ de la dose max) : ex. **carvédilol 3,125 mg × 2/j** ou **bisoprolol 1,25 mg/j**\n"
                "- Augmentation par paliers hebdomadaires : carvédilol max 25 mg × 2/j ou bisoprolol max 10 mg/j\n"
                "- Surveillance FC et PA\n"
                "- **CI** : asthme/BPCO sévère, bradycardie ou hypotension symptomatique, **BAV2 ou 3**"
            )),
            FicheRow(concept="★ ◆ Antialdostérones (spironolactone, éplérénone)", detail_md=(
                "- Diurétiques épargneurs potassiques (classés à part)\n"
                "- Tous patients IC FE basse en NYHA II à IV\n"
                "- ↓ mortalité et épisodes de décompensation\n"
                "- Éplérénone post-IDM étendu (FE < 40 % et/ou IC) : "
                "↓ mortalité, mort subite, récidives d'IC\n"
                "- Risques : **hyperkaliémie**, insuffisance rénale (surtout en association avec IEC)\n"
                "- **CI** : hyperkaliémie, insuffisance rénale\n"
                "- Spironolactone : gynécomastie, impuissance"
            )),
            FicheRow(concept="◆ Gliflozines (iSGLT2)", detail_md=(
                "- Empagliflozine, dapagliflozine\n"
                "- Efficaces chez l'IC FE basse, diabétique ou non\n"
                "- ↓ mortalité CV et hospitalisations pour IC\n"
                "- Peu hypotensives, protectrices rénales au long cours\n"
                "- EI : infections génitales, **acidocétose** (surtout chez diabétique), "
                "discrète altération initiale de la fonction rénale"
            )),
            FicheRow(concept="◆ Diurétiques de l'anse", detail_md=(
                "- Traitement des signes congestifs (pas d'effet sur la mortalité)\n"
                "- **Furosémide (Lasilix®)**, **bumétanide (Burinex®)**\n"
                "- Furosémide PO : 20 mg/j (forme légère) → 500 mg/j voire 1 g/j (forme sévère)\n"
                "- Patient éduqué : adapte la posologie à ses apports sodés\n"
                "- Thiazidiques (hydrochlorothiazide) : formes graves, résistance aux diurétiques de l'anse "
                "(association au furosémide)"
            )),
            FicheRow(concept="Traitements de 2ᵉ intention", detail_md=(
                "- **Ivabradine** : bloque le courant If, ↓ FC. NYHA II-IV, rythme sinusal, "
                "FC > 70-75/min malgré bêtabloquant ou intolérance/CI aux BB ; ↓ hospitalisations\n"
                "- **Digoxine** : peut améliorer les symptômes, neutre sur la survie, "
                "marge thérapeutique étroite, proarythmogène, réservée aux IC résistantes ; "
                "garde sa place en cas de FA (ralentir la FC). Dosage plasmatique\n"
                "- Dérivés nitrés : vasodilatateurs veineux d'appoint si pressions de remplissage élevées"
            )),
            FicheRow(concept="Autres traitements associés", detail_md=(
                "- **Amiodarone** : pas d'effet sur la mortalité ; seul antiarythmique utilisable "
                "dans l'IC FE basse ; troubles du rythme ventriculaires graves ou maintien post-FA\n"
                "- Antiagrégants : aspirine si cardiopathie ischémique stable ; "
                "bithérapie post-SCA/stent\n"
                "- Anticoagulants : **AOD privilégiés** (rivaroxaban, apixaban, dabigatran) sur AVK en cas de FA. "
                "Évaluation par scores **CHA2DS2-VA** et **HAS-BLED**\n"
                "- Anticoagulation aussi si thrombus intracavitaire ou AVC embolique"
            )),
            FicheRow(concept="⚠ Traitements contre-indiqués dans l'IC à FE altérée", detail_md=(
                "- Inhibiteurs calciques bradycardisants : **vérapamil, diltiazem** (effet inotrope négatif)\n"
                "- Dihydropyridines (félodipine, amlodipine) : neutres sur la mortalité, "
                "possibles si indication associée (angor, HTA)\n"
                "- Antiarythmiques de classe I (**flécaïnide**)\n"
                "- **AINS** : à éviter (risque de rétention hydrosodée)"
            )),
            FicheRow(concept="", detail_md=(
                "- Notions inacceptables : méconnaître les CI dans l'IC FE altérée "
                "(**vérapamil, diltiazem**, antiarythmiques de classe I comme la **flécaïnide**), "
                "ne pas savoir que les **AINS** doivent être évités, oublier les conseils de régime pauvre en sel."
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Traitement électrique (DAI, CRT)", rows=[
            FicheRow(concept="★ ◆ Resynchronisation ventriculaire (CRT)", detail_md=(
                "- IC symptomatique NYHA II à IV\n"
                "- **FEVG ≤ 35 %**\n"
                "- **Durée du QRS ≥ 130 ms**\n"
                "- 3 sondes : OD, VD, paroi latérale du VG (via le sinus coronaire)\n"
                "- D'autant plus efficace : **BBG**, QRS ≥ 150 ms, cardiopathie non ischémique"
            )),
            FicheRow(concept="★ ◆ Défibrillateur automatique implantable (DAI)", detail_md=(
                "- **Prévention secondaire** : après arrêt cardiaque par FV récupéré ou TV symptomatique\n"
                "- **Prévention primaire** : symptomatiques NYHA II-III, **FEVG ≤ 35 %** :\n"
                "  - Cardiopathie ischémique : à distance d'une revascularisation ou d'un IDM "
                "(au moins **6 semaines après**)\n"
                "  - Cardiopathie non ischémique : après au moins **3 mois** de traitement médical bien conduit\n"
                "- Probabilité de survie > 1 an requise (donc pas NYHA IV sauf en attente de greffe/assistance)\n"
                "- Possibilité de dispositif combiné (CRT-D : resynchronisation + défibrillation)\n"
                "- Complications : infections de sonde, chocs inappropriés"
            )),
            FicheRow(concept="Traitement percutané de la fuite mitrale", detail_md=(
                "- IM importante secondaire à l'IC, malgré traitement optimal\n"
                "- Discussion multidisciplinaire, critères échographiques précis\n"
                "- Clip mitral percutané possible si IC non trop avancée\n"
                "- Traitement percutané possible aussi pour les IT fonctionnelles (en cours d'évaluation)"
            )),
        ]),
        SousPartie(lettre="D", titre="IC à FE préservée et IC terminale", rows=[
            FicheRow(concept="◆ IC à FE préservée : moyen mnémotechnique « ABCDEFG »", detail_md=(
                "- **A** : éviter et traiter **A**rythmies/tachycardie (BB ou inhibiteur calcique ralentisseur, "
                "allonge la diastole)\n"
                "- **B** : contrôler la **B**lood pressure (IEC/ARA2, antialdostérones — finérénone non disponible en France)\n"
                "- **C** : traiter les **C**omorbidités (FA, ischémie, valvulopathie, diabète, dysthyroïdie)\n"
                "- **D** : **D**iurétiques de fond (thiazidiques ou de l'anse) si congestion ; "
                "surveillance fonction rénale\n"
                "- **E** : **E**xercice physique régulier\n"
                "- **F** : **F**ollow-up régulier\n"
                "- **G** : **G**liflozines (dapagliflozine, empagliflozine) — **I, A**"
            )),
            FicheRow(concept="◆ Amylose cardiaque à transthyrétine", detail_md=(
                "- Traitement spécifique : **tafamidis**\n"
                "- Autres traitements en cours de développement"
            )),
            FicheRow(concept="◆ Transplantation cardiaque", detail_md=(
                "- IC sévère, symptômes invalidants, mauvais pronostic, "
                "aucune alternative thérapeutique (traitement médical et non médical optimal)\n"
                "- Patient motivé, capable de suivre l'immunosuppression\n"
                "- Principal obstacle : nombre limité de greffons\n"
                "- **CI** : âge (rarement > 65-70 ans), pathologie limitant l'espérance de vie (cancer), "
                "infection active, insuffisance rénale, **HTAP fixée (résistances > 5 unités Wood)**, "
                "atteinte artérielle périphérique diffuse\n"
                "- Complications : rejet, EI des immunosuppresseurs (infections, cancers, HTA, IR), "
                "maladie coronarienne du greffon"
            )),
            FicheRow(concept="Assistance ventriculaire", detail_md=(
                "- Courte durée : **ECMO** (extracorporeal membrane oxygenation)\n"
                "- Longue durée : assistance mono ou biventriculaire\n"
                "- En attente de greffe ou traitement définitif chez patient non éligible à la greffe"
            )),
            FicheRow(concept="Parcours de soins, télésurveillance, soins palliatifs", detail_md=(
                "- Suivi cardiologue + médecin généraliste, éducation thérapeutique\n"
                "- IPA ou infirmiers formés : suivi des patients stabilisés "
                "(prescription sous responsabilité médicale)\n"
                "- Réadaptation cardiaque quand possible\n"
                "- Télésurveillance : surveillance des symptômes + paramètres simples (PA, FC, poids) — "
                "dépistage précoce des décompensations, remboursée\n"
                "- Soins palliatifs si IC avancée non éligible à la greffe/assistance"
            )),
        ]),
    ])

    # ── PARTIE VII : TRAITEMENT DE L'IC AIGUË ──
    partie_vii = Partie(numero="VII", titre="Traitement de l'IC aiguë", sous_parties=[
        SousPartie(lettre="A", titre="Œdème aigu pulmonaire", rows=[
            FicheRow(concept="◆ OAP : prise en charge au domicile", detail_md=(
                "- **Urgence**\n"
                "- Position assise ou demi-assise\n"
                "- **Furosémide IV : 1 mg/kg**, à répéter si besoin\n"
                "- Dérivés nitrés sublinguaux si **PAS > 100 mmHg**\n"
                "- Appel du Samu selon la gravité, hospitalisation"
            )),
            FicheRow(concept="◆ OAP : prise en charge hospitalière (USIC/Samu)", detail_md=(
                "- Position assise, voie veineuse périphérique (G5 %)\n"
                "- Monitorage : FC, PA, oxymétrie, scope\n"
                "- Bilan : ECG, RX thoracique, bilan sanguin, ± échographie pulmonaire, bilan urinaire\n"
                "- Oxygénothérapie si **SaO₂ < 90 %** (objectif **SaO₂ > 90 %**), précautions si risque d'hypercapnie\n"
                "- ECG\n"
                "- **Furosémide 1 mg/kg IV** (adapté à la diurèse)\n"
                "- **Trinitrine IV : 1 mg/h** si **PAS ≥ 110 mmHg** (adaptée à la PA)\n"
                "- Morphine IV : non systématique, réservée à l'anxiété importante ou douleur thoracique\n"
                "- Traitement du facteur déclenchant : digoxine IV et anticoagulation efficace si FA rapide, "
                "**nicardipine IV (1 à 5 mg/h)** si poussée hypertensive\n"
                "- **HBPM préventive systématique**"
            )),
            FicheRow(concept="◆ OAP : non-réponse au traitement", detail_md=(
                "- FR > 25/min ou SaO₂ < 90 % persistants → **CPAP** "
                "(continuous positive airway pressure) : améliore symptômes et saturation\n"
                "- Détresse respiratoire persistante / épuisement → **intubation + ventilation invasive**"
            )),
            FicheRow(concept="⚠ Bêtabloquants et IEC en aigu", detail_md=(
                "- Bêtabloquants : **ne pas introduire** pendant une poussée. "
                "Si le patient en prend déjà → arrêter ou diminuer\n"
                "- IEC, ARA2, sacubitril/valsartan : introduits secondairement après la poussée"
            )),
        ]),
        SousPartie(lettre="B", titre="Poussée d'IC sans OAP franc", rows=[
            FicheRow(concept="Prise en charge", detail_md=(
                "- Hospitalisation fréquente mais non systématique chez un IC chronique connu "
                "(parfois ↑ des diurétiques PO suffit)\n"
                "- Diurétiques IV (cure)\n"
                "- Rééquilibration du traitement PO (IEC, associations)\n"
                "- Recherche de la cause de la déstabilisation"
            )),
        ]),
        SousPartie(lettre="C", titre="Choc cardiogénique et CHAMPIT", rows=[
            FicheRow(concept="◆ Choc cardiogénique : traitement", detail_md=(
                "- Critères : **PA < 90 mmHg**, hypoperfusion périphérique "
                "(PA pincée, oligurie, marbrures, extrémités froides, obnubilation)\n"
                "- Inotropes : **dobutamine IV**, ou inhibiteurs des phosphodiestérases "
                "(milrinone, énoximone si patient sous bêtabloquant)\n"
                "- **Lévosimendan** : sensibilisateur des protéines contractiles au calcium "
                "(inotrope + vasodilatateur) — pour sevrage des inotropes\n"
                "- Sonde urinaire systématique\n"
                "- Monitorage invasif de la PA (cathéter radial)\n"
                "- Si non-réponse : assistance circulatoire (ECMO, mono/biventriculaire), "
                "cœur artificiel ou greffe en urgence"
            )),
            FicheRow(concept="◆ Causes à rechercher en urgence : CHAMPIT", detail_md=(
                "Devant une IC aiguë (OAP, choc), rechercher systématiquement :\n"
                "- **C** : Syndrome **C**oronarien aigu\n"
                "- **H** : Urgence **H**ypertensive\n"
                "- **A** : **A**rythmie\n"
                "- **M** : Cause **M**écanique lors d'un SCA (rupture, CIV, IM aiguë)\n"
                "- **P** : Embolie **P**ulmonaire\n"
                "- **I** : **I**nfections\n"
                "- **T** : **T**amponnade"
            )),
            FicheRow(concept="", detail_md=(
                "- L'**OAP** est une urgence cardiovasculaire dont la prise en charge doit être parfaitement connue\n"
                "- Devant toute IC aiguë : rechercher un facteur favorisant (CHAMPIT et autres : rupture de traitement, FA, anémie, EP, dysthyroïdie, iatrogènes)\n"
                "- Ne jamais oublier les comorbidités dans la prise en charge"
            ), kind="a_retenir"),
        ]),
    ])

    # ── SYNTHÈSE : TABLEAUX ──
    tableaux = [
        TableauSynthese(titre="Classification NYHA des stades fonctionnels", markdown=(
            "| Classe | Définition |\n"
            "|--------|-------------|\n"
            "| **I** | Aucune limitation, pas de dyspnée pour les efforts ordinaires |\n"
            "| **II** | Limitation modérée : dyspnée pour les efforts importants |\n"
            "| **III** | Limitation importante : dyspnée pour les efforts modérés du quotidien |\n"
            "| **IV** | Dyspnée de repos ou pour le moindre effort |"
        )),
        TableauSynthese(titre="Classification de l'IC selon la FEVG", markdown=(
            "| Type | FEVG | Mécanisme | Terrain typique |\n"
            "|------|------|-----------|------------------|\n"
            "| **IC à FE diminuée** (HFrEF) | ≤ 40 % | Défaut de contraction, VG dilaté | Toutes étiologies |\n"
            "| **IC à FE légèrement diminuée** (HFmrEF) | 41-49 % | Forme intermédiaire | Proche de l'HFrEF |\n"
            "| **IC à FE préservée** (HFpEF) | ≥ 50 % | Trouble du remplissage, VG rigide | Femme, sujet âgé, HTA, obésité |"
        )),
        TableauSynthese(titre="Seuils BNP / NT-proBNP", markdown=(
            "| Situation | BNP | NT-proBNP |\n"
            "|-----------|-----|-----------|\n"
            "| **Éliminer IC, dyspnée aiguë** | < 100 pg/mL | < 300 pg/mL |\n"
            "| **Éliminer IC, présentation chronique** | < 35 pg/mL | < 125 pg/mL |\n"
            "| **En faveur de l'IC (dyspnée aiguë)** | > 300 pg/mL | > 450 (< 50 ans) / > 900 (50-75) / > 1800 (> 75) pg/mL |\n"
            "| ↑ : âge, IR, FA | — | — |\n"
            "| ↓ : obésité | — | — |"
        )),
        TableauSynthese(titre="Traitements de l'IC à FE diminuée — les 5 piliers", markdown=(
            "| Classe | Effet pronostique | Particularités |\n"
            "|--------|-------------------|----------------|\n"
            "| **IEC** (ou ARNI, ou ARA2 si intolérance) | ↓ mortalité, ↓ hospitalisations | Surveillance créat/K+, AINS proscrits |\n"
            "| **Bêtabloquants** (carvédilol, métoprolol, bisoprolol, nébivolol) | ↓ mortalité, ↓ mort subite | Patient stabilisé, doses très progressives |\n"
            "| **Antialdostérones** (spironolactone, éplérénone) | ↓ mortalité, ↓ décompensation | Risque hyperK+, IR |\n"
            "| **Gliflozines** (dapagliflozine, empagliflozine) | ↓ mortalité CV, ↓ hospitalisations | Diabétique ou non ; effet rénal protecteur |\n"
            "| **Diurétiques de l'anse** (furosémide) | Symptomatique (signes congestifs) | Adaptés aux apports sodés |"
        )),
        TableauSynthese(titre="DAI : indications principales", markdown=(
            "| Indication | Critère |\n"
            "|------------|---------|\n"
            "| **Prévention secondaire** | Arrêt cardiaque par FV récupéré ou TV symptomatique |\n"
            "| **Prévention primaire, cardiopathie ischémique** | NYHA II-III, FEVG ≤ 35 %, ≥ 6 semaines après IDM/revascularisation |\n"
            "| **Prévention primaire, cardiopathie non ischémique** | NYHA II-III, FEVG ≤ 35 %, ≥ 3 mois de traitement optimal |\n"
            "| **Probabilité de survie** | > 1 an requise (donc pas NYHA IV sauf en attente de greffe/assistance) |"
        )),
        TableauSynthese(titre="CHAMPIT : causes d'une IC aiguë à rechercher", markdown=(
            "| Lettre | Cause |\n"
            "|--------|-------|\n"
            "| **C** | Syndrome **C**oronarien aigu |\n"
            "| **H** | Urgence **H**ypertensive |\n"
            "| **A** | **A**rythmie |\n"
            "| **M** | Cause **M**écanique (rupture, CIV, IM aiguë lors d'un SCA) |\n"
            "| **P** | Embolie **P**ulmonaire |\n"
            "| **I** | **I**nfections |\n"
            "| **T** | **T**amponnade |"
        )),
    ]

    # ── CHIFFRES-CLÉS ──
    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Prévalence IC (population générale) | 1 à 2 % | Augmente avec l'âge |\n"
        "| Âge moyen au diagnostic | 75 à 80 ans | Europe |\n"
        "| Mortalité à 5 ans | ≈ 50 % | Pronostic global |\n"
        "| Mortalité annuelle IC grave (NYHA IV) | 40 à 50 %/an | — |\n"
        "| PCAP entraînant un OAP | ≥ 25 mmHg | Passage de transsudat |\n"
        "| FEVG : IC à FE diminuée (HFrEF) | ≤ 40 % | Classification |\n"
        "| FEVG : IC à FE légèrement diminuée (HFmrEF) | 41-49 % | Classification |\n"
        "| FEVG : IC à FE préservée (HFpEF) | ≥ 50 % | Classification |\n"
        "| FEVG normale | > 50-60 % | ETT |\n"
        "| Proportion HFpEF | ≥ 50 % des cas | Femme, sujet âgé |\n"
        "| Prise de poids alarmante | 2-3 kg en 2-3 jours | Signe d'alerte |\n"
        "| Régime hyposodé (objectif) | 5 à 6 g/j de sel | Mesure HD |\n"
        "| Rapport cardiothoracique (RX) | > 0,5 | Cardiomégalie |\n"
        "| BNP éliminer IC (aigu) | < 100 pg/mL | Dyspnée aiguë |\n"
        "| NT-proBNP éliminer IC (aigu) | < 300 pg/mL | Dyspnée aiguë |\n"
        "| BNP éliminer IC (chronique) | < 35 pg/mL | Consultation |\n"
        "| NT-proBNP éliminer IC (chronique) | < 125 pg/mL | Consultation |\n"
        "| BNP en faveur de l'IC (aigu) | > 300 pg/mL | Dyspnée aiguë |\n"
        "| NT-proBNP en faveur IC, < 50 ans | > 450 pg/mL | Dyspnée aiguë |\n"
        "| NT-proBNP en faveur IC, 50-75 ans | > 900 pg/mL | Dyspnée aiguë |\n"
        "| NT-proBNP en faveur IC, > 75 ans | > 1800 pg/mL | Dyspnée aiguë |\n"
        "| HVG : masse VG indexée homme | ≥ 115 g/m² | ETT |\n"
        "| HVG : masse VG indexée femme | ≥ 95 g/m² | ETT |\n"
        "| Dilatation OG : volume indexé | > 34 mL/m² | ETT |\n"
        "| Protides épanchement pleural (transsudat IC) | < 30 g/L | Ponction pleurale |\n"
        "| Bloc de branche gauche (durée QRS) | > 120 ms | Facteur pronostique |\n"
        "| CRT : QRS requis | ≥ 130 ms | Indication |\n"
        "| CRT : FEVG requise | ≤ 35 % | NYHA II-IV |\n"
        "| DAI prévention primaire : FEVG | ≤ 35 % | NYHA II-III |\n"
        "| DAI post-IDM : délai | ≥ 6 semaines | Prévention primaire |\n"
        "| DAI cardiopathie non ischémique : délai | ≥ 3 mois de traitement optimal | Prévention primaire |\n"
        "| Choc cardiogénique : PAS | < 90 mmHg | Ou chute > 30 mmHg ≥ 30 min |\n"
        "| Choc cardiogénique : oligurie | < 20 mL/h | Hypoperfusion |\n"
        "| Pression OD (cathétérisme droit) | < 5 mmHg | Normal |\n"
        "| Pression VD (cathétérisme droit) | 25/0 mmHg | Normal |\n"
        "| PCAP normale | < 15 mmHg | Cathétérisme droit |\n"
        "| HTAP (PAPm) | > 25 mmHg | Cathétérisme droit |\n"
        "| Débit cardiaque normal | 5 L/min | Cathétérisme droit |\n"
        "| Index cardiaque normal | 3 L/min/m² | Cathétérisme droit |\n"
        "| CI greffe : résistances pulmonaires | > 5 unités Wood | HTAP fixée |\n"
        "| Furosémide IV (OAP) | 1 mg/kg | À répéter si besoin |\n"
        "| Trinitrine IV (OAP) | 1 mg/h | Si PAS ≥ 110 mmHg |\n"
        "| Dérivés nitrés SL (OAP domicile) | Si PAS > 100 mmHg | Prise en charge initiale |\n"
        "| Nicardipine IV (poussée HTA) | 1 à 5 mg/h | Facteur déclenchant |\n"
        "| Oxygène (OAP) : objectif | SaO₂ > 90 % | — |\n"
        "| CPAP (OAP) : critères | FR > 25/min ou SaO₂ < 90 % | Non-réponse |\n"
        "| Ivabradine : FC seuil | > 70-75/min | Rythme sinusal, sous BB |\n"
        "| Carvédilol : dose initiale | 3,125 mg × 2/j | 1/8ᵉ dose max |\n"
        "| Carvédilol : dose max | 25 mg × 2/j | Titration |\n"
        "| Bisoprolol : dose initiale | 1,25 mg/j | 1/8ᵉ dose max |\n"
        "| Bisoprolol : dose max | 10 mg/j | Titration |\n"
        "| Énalapril : dose cible | 20 mg/j | — |\n"
        "| Captopril : dose cible | 150 mg/j | — |\n"
        "| Ramipril : dose cible | 10 mg/j | — |\n"
        "| Furosémide PO : range | 20 mg à 1 g/j | Selon sévérité |\n"
        "| ↑ créatinine sous IEC (action) | > 20-30 % | ↓ dose ou arrêt |\n"
        "| CMD familiale | 25 % | Mutation monogénique, transmission AD le plus souvent |\n"
        "| CMH obstructive | 25 % des CMH | Gradient sous-aortique |"
    ))

    points_cles = [
        "IC = syndrome (dyspnée, œdèmes) + anomalie cardiaque ; **1-2 %** population, **50 % mortalité à 5 ans**",
        "Classification **FEVG** : HFrEF **≤ 40 %** | HFmrEF **41-49 %** | HFpEF **≥ 50 %** (femme, sujet âgé)",
        "Diagnostic : **ETT** = examen clé ; **BNP/NT-proBNP** avec excellente **VPN** ; ECG, RX thorax",
        "Étiologies : **cardiopathie ischémique (1ʳᵉ cause)**, HTA, CMD/CMH, valvulopathies ; éliminer ischémie si FEVG basse",
        "**OAP** = urgence : assis, **furosémide IV 1 mg/kg**, trinitrine si PAS ≥ 110, **CPAP** si non-réponse",
        "IC aiguë : rechercher facteur déclenchant **CHAMPIT** (SCA, HTA, arythmie, mécanique, EP, infection, tamponnade)",
        "**Choc cardiogénique** : PAS < 90, oligurie < 20 mL/h → dobutamine ± milrinone ; échec → **ECMO/greffe**",
        "IC FE diminuée — **5 piliers** : diurétique de l'anse, **IEC/ARNI**, **bêtabloquants**, **ARM**, **gliflozines**",
        "**CI absolues** IC FE altérée : **vérapamil, diltiazem, flécaïnide, AINS** ; BB jamais introduits en aigu",
        "**CRT** si NYHA II-IV + FEVG ≤ 35 % + QRS ≥ 130 ms ; **DAI** prévention 1ʳᵉ si FEVG ≤ 35 % post-traitement optimal",
    ]

    fiche_eclair_md = (
        "**IC** : syndrome — symptômes (dyspnée, œdèmes, fatigue) + signes éventuels (crépitants, turgescence) "
        "par anomalie cardiaque structurelle/fonctionnelle. Prévalence 1-2 %, âge moyen 75-80 ans, mortalité 50 % à 5 ans. "
        "1ʳᵉ cause d'hospitalisation après 65 ans.\n\n"
        "**Classification FEVG** : HFrEF ≤ 40 % | HFmrEF 41-49 % | HFpEF ≥ 50 %. HFpEF = ≥ 50 % des cas (femme, sujet âgé, HTA, obésité).\n\n"
        "**Diagnostic positif** : dyspnée NYHA I-IV, orthopnée, DPN, hépatalgie. Signes droits : turgescence jugulaire, RHJ, hépatomégalie, œdèmes godet. "
        "ECG (BBG si QRS > 120 ms), RX (RCT > 0,5, lignes Kerley, ailes papillon).\n\n"
        "**BNP/NT-proBNP** : éliminer IC en aigu < 100 / < 300 pg/mL ; en chronique < 35 / < 125. "
        "En faveur (aigu) : BNP > 300 ; NT-proBNP > 450/900/1800 selon âge. Augmentent : âge, IR, FA. Diminuent : obésité.\n\n"
        "**ETT** = examen clé : FEVG, étiologie, pressions, hémodynamique. Cathétérisme droit : HTAP = PAPm > 25 mmHg, CI greffe si résistances > 5 UW.\n\n"
        "**Étiologies** : ischémique (1ʳᵉ), HTA, cardiomyopathies (CMD jeune, CMH = mort subite athlète, restrictives → amylose), valvulopathies, "
        "rythme/conduction, péricarde. IC droite isolée : cœur pulmonaire, HTAP, DAVD, IT, IDM VD. IC à débit augmenté : anémie, FAV, hyperthyroïdie, béribéri.\n\n"
        "**IC aiguë / OAP** : urgence. Polypnée, orthopnée, expectoration mousseuse, marée crépitants. "
        "PEC : assis, O2 SpO2 > 90 %, furosémide IV 1 mg/kg, trinitrine 1 mg/h si PAS ≥ 110 mmHg, HBPM préventive. "
        "CPAP si FR > 25 ou SpO2 < 90 %, puis intubation. BB jamais en aigu ; IEC/ARNI secondairement.\n\n"
        "**CHAMPIT** : Coronarien aigu, Hypertension, Arythmie, Mécanique (SCA), embolie Pulmonaire, Infections, Tamponnade.\n\n"
        "**Choc cardiogénique** : PAS < 90 mmHg, oligurie < 20 mL/h, marbrures. Dobutamine ± milrinone (sous BB), lévosimendan. Si échec : ECMO, greffe urgence.\n\n"
        "**Traitement IC chronique FE diminuée — 5 piliers** : "
        "1) diurétique de l'anse (furosémide, signes congestifs) ; "
        "2) IEC ou sacubitril/valsartan (ou ARA2 si intolérance) — surveillance créat/K+ ; "
        "3) bêtabloquants (carvédilol, métoprolol, bisoprolol, nébivolol) à faibles doses ; "
        "4) antialdostérones (spironolactone, éplérénone) NYHA II-IV ; "
        "5) gliflozines (dapa/empagliflozine).\n\n"
        "**CI absolues IC FE altérée** : vérapamil, diltiazem, antiarythmiques classe I (flécaïnide), AINS. "
        "2ᵉ intention : ivabradine (FC > 70/min, rythme sinusal), digoxine (si FA), dérivés nitrés.\n\n"
        "**Traitement électrique** : CRT si NYHA II-IV + FEVG ≤ 35 % + QRS ≥ 130 ms (max si BBG, QRS ≥ 150 ms). "
        "DAI : 2ᵉ prévention (FV/TV récupérée) ou 1ʳᵉ prévention (FEVG ≤ 35 %, ≥ 6 sem post-IDM ou ≥ 3 mois CMD).\n\n"
        "**Mesures HD** : régime hyposodé 5-6 g/j, arrêt alcool/tabac, activité physique, vaccinations (grippe, Covid, pneumocoque). "
        "Alerte : prise 2-3 kg en 2-3 jours.\n\n"
        "**IC FE préservée (ABCDEFG)** : Arythmies, Blood pressure, Comorbidités, Diurétiques, Exercice, Follow-up, Gliflozines (I, A). Amylose : tafamidis.\n\n"
        "**IC terminale** : transplantation (CI : âge, cancer, IR, HTAP fixée > 5 UW). Assistance (ECMO court ; mono/bi long terme). Soins palliatifs sinon."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 234 - Insuffisance cardiaque de l'adulte",
        annee="2025-2026",
        item="Item 234",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi, partie_vii],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 234",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-234_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

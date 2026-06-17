"""Génère la fiche exhaustive de Pharmacologie à partir du PDF source."""

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


def build_pharmacologie_fiche() -> FicheData:
    plan = [
        PlanPartie(numero="I", titre="Méthodologie de la prescription", sous_parties=[
            PlanSousPartie(lettre="A", titre="Justification d'une thérapeutique : DICTIAS"),
            PlanSousPartie(lettre="B", titre="Ordonnances et règles de prescription"),
            PlanSousPartie(lettre="C", titre="Iatrogénie et interactions médicamenteuses"),
        ]),
        PlanPartie(numero="II", titre="Diurétiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Diurétiques de l'anse"),
            PlanSousPartie(lettre="B", titre="Diurétiques thiazidiques"),
            PlanSousPartie(lettre="C", titre="Diurétiques épargneurs de potassium"),
            PlanSousPartie(lettre="D", titre="Inhibiteurs de l'anhydrase carbonique et gliflozines"),
        ]),
        PlanPartie(numero="III", titre="Inhibiteurs du SRAA", sous_parties=[
            PlanSousPartie(lettre="A", titre="Inhibiteurs de l'enzyme de conversion (IEC)"),
            PlanSousPartie(lettre="B", titre="Antagonistes des récepteurs de l'angiotensine 2 (ARA2)"),
        ]),
        PlanPartie(numero="IV", titre="Hypolipémiants et risque cardiovasculaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Statines et fibrates"),
            PlanSousPartie(lettre="B", titre="Explorations des anomalies lipidiques"),
            PlanSousPartie(lettre="C", titre="Traitement de la cardiopathie ischémique"),
        ]),
        PlanPartie(numero="V", titre="Anti-inflammatoires et immunosuppresseurs", sous_parties=[
            PlanSousPartie(lettre="A", titre="Corticothérapie au long cours"),
            PlanSousPartie(lettre="B", titre="Méthotrexate"),
            PlanSousPartie(lettre="C", titre="Salazopyrine et léflunomide"),
            PlanSousPartie(lettre="D", titre="Biothérapies et nomenclature"),
        ]),
        PlanPartie(numero="VI", titre="Situations cliniques intégrées", sous_parties=[
            PlanSousPartie(lettre="A", titre="Insuffisance rénale aiguë et néphrotoxicité"),
            PlanSousPartie(lettre="B", titre="Équilibre acido-basique et toxiques dialysables"),
            PlanSousPartie(lettre="C", titre="Anticoagulants et gestion des accidents hémorragiques"),
            PlanSousPartie(lettre="D", titre="Anti-infectieux : fluoroquinolones, macrolides, antipaludéens"),
        ]),
    ]

    # ── PARTIE I : MÉTHODOLOGIE DE LA PRESCRIPTION ──
    partie_i = Partie(numero="I", titre="Méthodologie de la prescription", sous_parties=[
        SousPartie(lettre="A", titre="Justification d'une thérapeutique : DICTIAS", rows=[
            FicheRow(concept="Mnémo DICTIAS", detail_md=(
                "- **D**iagnostic ?\n"
                "- **I**ndication ?\n"
                "- **C**ontre-indication ?\n"
                "- **T**olérance ?\n"
                "- **I**nteractions ?\n"
                "- **A**ssociés (traitements) ?\n"
                "- **S**econdaires (effets) ?"
            )),
            FicheRow(concept="", detail_md=(
                "- Toute prescription doit être **justifiée** par le raisonnement DICTIAS\n"
                "- Ce schéma est la base de tout dossier de pharmacologie aux EVC"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Ordonnances et règles de prescription", rows=[
            FicheRow(concept="◆ Types d'ordonnances", detail_md=(
                "- **Ordonnance standard** : prescription classique\n"
                "- **Ordonnance sécurisée** : stupéfiants, substances vénéneuses (papier filigrané, "
                "posologie en toutes lettres)\n"
                "- **Ordonnance pour médicaments d'exception** : cerfa spécifique, critères d'AMM stricts"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours vérifier le type d'ordonnance requis avant de prescrire\n"
                "- Les stupéfiants nécessitent une ordonnance sécurisée avec durée limitée"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Iatrogénie et interactions médicamenteuses", rows=[
            FicheRow(concept="Facteurs de risque d'iatrogénie", detail_md=(
                "- **Âge** : risque majoré chez le sujet âgé\n"
                "- **Polymédication** : majore le risque d'interactions\n"
                "- **Insuffisance rénale** et **insuffisance hépatique**\n"
                "- Automédication (AINS, aspirine en vente libre)"
            )),
            FicheRow(concept="◆ Concepts clés", detail_md=(
                "- **Under-use** : sous-prescription d'un traitement indiqué\n"
                "- **Over-use** : prescription excessive ou non indiquée\n"
                "- **Mis-use** : mauvais usage d'un traitement indiqué\n"
                "- Recherche systématique d'une **hypotension orthostatique** chez le sujet âgé polymédiqué"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Chez le sujet âgé, toujours réévaluer le rapport bénéfice/risque\n"
                "- ⚠ L'automédication par AINS est une cause fréquente d'IRA fonctionnelle"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE II : DIURÉTIQUES ──
    partie_ii = Partie(numero="II", titre="Diurétiques", sous_parties=[
        SousPartie(lettre="A", titre="Diurétiques de l'anse", rows=[
            FicheRow(concept="Molécules", detail_md=(
                "- **FUROSÉMIDE** ; BUMÉTANIDE ; PIRÉTANIDE"
            )),
            FicheRow(concept="Indication", detail_md=(
                "- **Déplétion hydrosodée** : insuffisance cardiaque, insuffisance rénale, "
                "insuffisance hépatique"
            )),
            FicheRow(concept="Effets indésirables", detail_md=(
                "- **Hypokaliémie** +++\n"
                "- **Hyponatrémie**\n"
                "- **Hyperuricémie**\n"
                "- **IRA** fonctionnelle\n"
                "- Plus rares : hypomagnésémie, hypocalcémie, hypertriglycéridémie"
            )),
            FicheRow(concept="", detail_md=(
                "- Les diurétiques de l'anse sont **hypokaliémiants** et **hypocalcémiants**\n"
                "- Surveillance systématique du ionogramme sous traitement"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Diurétiques thiazidiques", rows=[
            FicheRow(concept="Molécule", detail_md=(
                "- **HYDROCHLOROTHIAZIDE** (Esidrex)"
            )),
            FicheRow(concept="Indication", detail_md=(
                "- **Hypertension artérielle** (1re intention)\n"
                "- Déplétion hydrosodée"
            )),
            FicheRow(concept="Effets indésirables", detail_md=(
                "- **Hyponatrémie** +++\n"
                "- **Hypokaliémie**\n"
                "- **IRA** fonctionnelle\n"
                "- Plus rares : **hypercalcémie**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Les thiazidiques sont **hypercalcémiants** (inverse des diurétiques de l'anse)\n"
                "- ⚠ Risque d'hyponatrémie sévère chez le sujet âgé"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Diurétiques épargneurs de potassium", rows=[
            FicheRow(concept="Molécules", detail_md=(
                "- **Spironolactone** (anti-aldostérone)\n"
                "- **Éplérénone**\n"
                "- **Amiloride**"
            )),
            FicheRow(concept="Indication", detail_md=(
                "- **Hypertension artérielle**\n"
                "- **Insuffisance cardiaque**"
            )),
            FicheRow(concept="Effets indésirables", detail_md=(
                "- **Hyperkaliémie** +++\n"
                "- **Gynécomastie** (spironolactone)\n"
                "- **IRA**"
            )),
            FicheRow(concept="", detail_md=(
                "- Les épargneurs de potassium sont **hyperkaliémiants**\n"
                "- Association dangereuse avec les IEC/ARA2 (double risque d'hyperkaliémie)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Inhibiteurs de l'anhydrase carbonique et gliflozines", rows=[
            FicheRow(concept="Inhibiteurs de l'anhydrase carbonique", detail_md=(
                "- Classe : **ACÉTAZOLAMIDE**\n"
                "- Indication : glaucome, alcalose métabolique\n"
                "- Effet : acidose métabolique hyperchlorémique"
            )),
            FicheRow(concept="Gliflozines (iSGLT2)", detail_md=(
                "- Exemple : **DAPAGLIFLOZINE**, empagliflozine\n"
                "- Indications :\n"
                "  - **Insuffisance cardiaque**\n"
                "  - **Diabète de type 2**\n"
                "  - **Maladie rénale chronique**\n"
                "- Mécanisme : inhibition du co-transporteur sodium-glucose 2 au niveau rénal"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Les gliflozines peuvent favoriser une **IRA fonctionnelle** en situation de déshydratation\n"
                "- ⚠ Arrêt impératif en cas de diarrhées/vomissements (risque d'IRA)"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE III : INHIBITEURS DU SRAA ──
    partie_iii = Partie(numero="III", titre="Inhibiteurs du SRAA", sous_parties=[
        SousPartie(lettre="A", titre="Inhibiteurs de l'enzyme de conversion (IEC)", rows=[
            FicheRow(concept="Molécules", detail_md=(
                "- **RAMIPRIL** ; **ÉNALAPRIL** ; **CAPTOPRIL**"
            )),
            FicheRow(concept="Indications", detail_md=(
                "- **Hypertension artérielle**\n"
                "- **Insuffisance rénale chronique** : néphroprotection\n"
                "- **Cardioprotection** (post-ischémique)\n"
                "- **Vasculoprotection** (AOMI)\n"
                "- **Insuffisance cardiaque**"
            )),
            FicheRow(concept="Contre-indications", detail_md=(
                "- **Grossesse** (tératogène)\n"
                "- **Sténose bilatérale des artères rénales**\n"
                "- **Angioedèmes aux IEC**"
            )),
            FicheRow(concept="Effets indésirables", detail_md=(
                "- **Hyperkaliémie**\n"
                "- **Insuffisance rénale aiguë** (fonctionnelle)\n"
                "- **Toux sèche** (spécifique des IEC, bradykinine)"
            )),
            FicheRow(concept="", detail_md=(
                "- Les IEC sont **néphroprotecteurs** au long cours mais peuvent provoquer une **IRA fonctionnelle** "
                "en situation de déshydratation\n"
                "- La **toux** est un effet spécifique des IEC (pas des ARA2) lié à l'accumulation de bradykinine"
            ), kind="a_retenir"),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours suspendre les IEC en cas de déshydratation (diarrhées, vomissements, fièvre)\n"
                "- ⚠ Contrôle créatinine + kaliémie 7-15 jours après introduction"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Antagonistes des récepteurs de l'angiotensine 2 (ARA2)", rows=[
            FicheRow(concept="Molécules", detail_md=(
                "- **CANDÉSARTAN** ; **LOSARTAN**"
            )),
            FicheRow(concept="Indications", detail_md=(
                "- **Hypertension artérielle**\n"
                "- **Insuffisance rénale chronique** : néphroprotection\n"
                "- **Cardioprotection** post-ischémique\n"
                "- **Vasculoprotection** (AOMI)"
            )),
            FicheRow(concept="Contre-indications", detail_md=(
                "- **Grossesse**\n"
                "- **Sténose bilatérale des artères rénales**"
            )),
            FicheRow(concept="Effets indésirables", detail_md=(
                "- **Hyperkaliémie**\n"
                "- **Insuffisance rénale aiguë**"
            )),
            FicheRow(concept="", detail_md=(
                "- Les ARA2 ont les mêmes indications et CI que les IEC\n"
                "- Avantage : **pas de toux** (pas d'accumulation de bradykinine)\n"
                "- Alternative si toux sous IEC"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE IV : HYPOLIPÉMIANTS ET RISQUE CARDIOVASCULAIRE ──
    partie_iv = Partie(numero="IV", titre="Hypolipémiants et risque cardiovasculaire", sous_parties=[
        SousPartie(lettre="A", titre="Statines et fibrates", rows=[
            FicheRow(concept="Objectif des hypolipémiants", detail_md=(
                "- Baisse de la **morbi-mortalité cardiovasculaire** à moyen et long terme"
            )),
            FicheRow(concept="Indications", detail_md=(
                "- **Hypercholestérolémie** : prévention primaire\n"
                "- **Prévention secondaire** : objectif LDLc < **0,55 g/L**\n"
                "- Stratégie :\n"
                "  - Hypercholestérolémie isolée : **statines** en 1re intention\n"
                "  - Hypertriglycéridémie isolée : **fibrates** en 1re intention\n"
                "  - Hypercholestérolémie + hypertriglycéridémie : **statines**"
            )),
            FicheRow(concept="◆ Statines", detail_md=(
                "- Mécanisme : inhibition de l'HMG-CoA réductase\n"
                "- Effets indésirables : **myalgies**, **rhabdomyolyse** (rare), cytolyse hépatique\n"
                "- Surveillance : CPK si myalgies, transaminases"
            )),
            FicheRow(concept="◆ Fibrates", detail_md=(
                "- Indication principale : hypertriglycéridémie > **5 g/L**\n"
                "- Si triglycérides 1,5-5 g/L : RHD d'abord"
            )),
        ]),
        SousPartie(lettre="B", titre="Explorations des anomalies lipidiques", rows=[
            FicheRow(concept="Valeurs normales", detail_md=(
                "- **LDL-C** < 1,6 g/L\n"
                "- **HDL-C** > 0,4 g/L\n"
                "- **Triglycérides** < 1,5 g/L\n"
                "- Bilan lipidique tous les **5 ans** chez l'adulte"
            )),
            FicheRow(concept="Causes secondaires d'hypertriglycéridémie", detail_md=(
                "- Mnémo **ADORABLE** :\n"
                "  - **A**lcool\n"
                "  - **D**iabète\n"
                "  - **O**estrogènes\n"
                "  - **R**étinoïdes\n"
                "  - **A**ntirétroviraux\n"
                "  - **B**-bloquants\n"
                "  - **L**asilix (diurétiques)\n"
                "  - **E**lévation de la créatinine"
            ), kind="mnemo"),
            FicheRow(concept="Causes secondaires d'hypercholestérolémie", detail_md=(
                "- Mnémo **CHIC** :\n"
                "  - **C**holestase\n"
                "  - **H**ypothyroïdie\n"
                "  - **I**RC\n"
                "  - **C**iclosporine / Syndrome néphrotique"
            ), kind="mnemo"),
            FicheRow(concept="◆ Règles hygiéno-diététiques", detail_md=(
                "- **Régime méditerranéen** +++\n"
                "- Acides gras poly-insaturés oméga-3\n"
                "- Suppression des acides gras trans\n"
                "- Limitation des AG saturés\n"
                "- Augmentation des fibres alimentaires, céréales et légumes\n"
                "- Statines si persistance à 3 mois"
            )),
        ]),
        SousPartie(lettre="C", titre="Traitement de la cardiopathie ischémique", rows=[
            FicheRow(concept="Traitement minimal post-SCA", detail_md=(
                "- **B**-Bloquants\n"
                "- **A**spirine\n"
                "- **S**tatines\n"
                "- **I**nhibiteurs de l'enzyme de conversion\n"
                "- **C**lopidogrel (double antiagrégation plaquettaire) : à discuter"
            )),
            FicheRow(concept="", detail_md=(
                "- Le traitement post-infarctus repose sur **BASIC** : B-bloquant, Aspirine, Statine, IEC, Clopidogrel\n"
                "- Tous ces traitements sont indiqués au long cours"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE V : ANTI-INFLAMMATOIRES ET IMMUNOSUPPRESSEURS ──
    partie_v = Partie(numero="V", titre="Anti-inflammatoires et immunosuppresseurs", sous_parties=[
        SousPartie(lettre="A", titre="Corticothérapie au long cours", rows=[
            FicheRow(concept="Indications", detail_md=(
                "- Maladies **inflammatoires** : artérite à cellules géantes, PPR, sarcoïdose\n"
                "- Maladies **dys-immunitaires** : vascularites, connectivites\n"
                "- Effets recherchés : **anti-inflammatoire** et **immunosuppresseur**"
            )),
            FicheRow(concept="Effets indésirables", detail_md=(
                "- **Prise de poids**\n"
                "- **Hypertension artérielle**\n"
                "- **Diabète cortico-induit**\n"
                "- **Ostéoporose**\n"
                "- **Atrophie cutanée**, retard de cicatrisation\n"
                "- **Cataracte**\n"
                "- **Risques infectieux**\n"
                "- **Amyotrophie**\n"
                "- **Insomnie**\n"
                "- **Insuffisance surrénalienne** à l'arrêt"
            )),
            FicheRow(concept="Mesures associées à la corticothérapie", detail_md=(
                "- **Supplémentation vitamino-calcique** selon les apports\n"
                "- **Biphosphonates** dès que ≥ 7,5 mg/j d'équivalent prednisone pendant 3 mois\n"
                "- Adaptation des **apports potassiques**\n"
                "- Discussion d'un **IPP** (inhibiteur de la pompe à protons)\n"
                "- **Déparasitage** si risque d'anguillulose maligne\n"
                "- **Mise à jour vaccinale**\n"
                "- **Prise matinale** (respecte le cycle nycthéméral du cortisol)"
            )),
            FicheRow(concept="◆ Règles hygiéno-diététiques", detail_md=(
                "- Régime hyposodé, pauvre en sucres rapides\n"
                "- **Activité physique** régulière\n"
                "- Surveillance glycémique, tensionnelle, ostéodensitométrique"
            )),
            FicheRow(concept="", detail_md=(
                "- La **PPR** (pseudo-polyarthrite rhizomélique) est très corticosensible à **0,2-0,3 mg/kg/j**\n"
                "- L'artérite à cellules géantes (Horton) nécessite des doses plus élevées : **0,7-1 mg/kg/j**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Méthotrexate", rows=[
            FicheRow(concept="Mécanisme", detail_md=(
                "- Inhibiteur de la **tétrahydrofolate réductase**"
            )),
            FicheRow(concept="Indications", detail_md=(
                "- **Polyarthrite rhumatoïde** (1re ligne)\n"
                "- Épargne cortisonique dans de nombreuses pathologies\n"
                "- **Sarcoïdose**\n"
                "- **Psoriasis**"
            )),
            FicheRow(concept="Contre-indications", detail_md=(
                "- Hypersensibilité au méthotrexate\n"
                "- **Insuffisance hépatique ou rénale** (CI si bilirubine > 5 mg/L)\n"
                "- **Alcoolisme**\n"
                "- **Infections sévères** : tuberculose, VIH\n"
                "- Ulcères de la cavité buccale, maladie ulcéreuse gastro-intestinale\n"
                "- **Grossesse**, allaitement"
            )),
            FicheRow(concept="Effets indésirables", detail_md=(
                "- **Macrocytose**\n"
                "- **Ulcères cutanés**\n"
                "- **Altération du bilan hépatique**\n"
                "- **Pneumopathie interstitielle diffuse** (potentiellement grave)"
            )),
            FicheRow(concept="Mesures associées", detail_md=(
                "- **Acide folique 48h après** la prise de méthotrexate"
            )),
            FicheRow(concept="◆ Bilan pré-thérapeutique", detail_md=(
                "- Systématique : NFS, IUC, BHC, albuminémie, EPPS, Rx de thorax, sérologies virales\n"
                "- À discuter : EFR, Fibroscan"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ **BACTRIM** (triméthoprime-sulfaméthoxazole) est contre-indiqué avec le méthotrexate "
                "(même mécanisme antifolique, risque de pancytopénie)\n"
                "- ⚠ Prise **hebdomadaire** (pas quotidienne) : erreur fréquente et potentiellement fatale"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Salazopyrine et léflunomide", rows=[
            FicheRow(concept="Salazopyrine (sulfasalazine)", detail_md=(
                "- Indications : **rectocolite hémorragique**, **polyarthrite rhumatoïde**\n"
                "- Contre-indications : allergie aux **sulfamides** et aux **salicylés**, déficit en G6PD, "
                "porphyrie, prématuré/nouveau-né, allaitement\n"
                "- Effets indésirables : **cytolyse hépatique**, pancréatite\n"
                "- Bilan pré-thérapeutique : NFS, IUC, BHC, Rx de thorax, sérologies virales"
            )),
            FicheRow(concept="Léflunomide", detail_md=(
                "- Mécanisme : inhibition de la **dihydro-orotate déshydrogénase** (DHODH), "
                "action antiprolifératrice\n"
                "- Indications : **polyarthrite rhumatoïde**, **psoriasis**\n"
                "- Contre-indications : insuffisance hépatique et/ou rénale modérée, grossesse, allaitement\n"
                "- Effets indésirables : **cytolyse hépatique**\n"
                "- Bilan pré-thérapeutique : NFS, IUC, BHC, Rx de thorax, sérologies virales"
            )),
        ]),
        SousPartie(lettre="D", titre="Biothérapies et nomenclature", rows=[
            FicheRow(concept="Nomenclature des biothérapies", detail_md=(
                "- Suffixe **-MAB** : anticorps monoclonal (Monoclonal AntiBody)\n"
                "- Suffixe **-CEPT** : protéine de fusion (récepteur)\n"
                "- Pré-suffixes :\n"
                "  - **MO-MAB** : anticorps murin\n"
                "  - **XI-MAB** : anticorps chimérique\n"
                "  - **ZU-MAB** : anticorps humanisé\n"
                "  - **MU-MAB** : anticorps humain"
            )),
            FicheRow(concept="◆ Pré-suffixes de cible", detail_md=(
                "- **TU** : tumoral (rituximab)\n"
                "- **LI / I** : maladies auto-immunes (golimumab, infliximab, adalimumab)\n"
                "- **KIN** : cytokines (anakinra = anti-IL1)\n"
                "- **OS** : visée osseuse (dénosumab)"
            )),
            FicheRow(concept="Anti-TNF-alpha", detail_md=(
                "- Molécules : **INFLIXIMAB**, **ADALIMUMAB**, **GOLIMUMAB**, **CERTOLIZUMAB**, **ÉTANERCEPT**\n"
                "- Mécanisme : inhibition du **TNF-alpha**\n"
                "- Indications : polyarthrite rhumatoïde, psoriasis, sarcoïdose, Takayasu\n"
                "- CI : **tuberculose active**, infections graves, **insuffisance cardiaque** NYHA III/IV\n"
                "- EI : cytolyse hépatique, infections opportunistes"
            )),
            FicheRow(concept="◆ Bilan pré-thérapeutique anti-TNF", detail_md=(
                "- NFS, EPPS, ASAT/ALAT\n"
                "- Rx de thorax\n"
                "- **IDR ou QuantiFERON** (sauf si négatif < 2 ans)\n"
                "- Sérologies hépatites B, C et VIH (avec accord du patient)\n"
                "- Anticorps anti-nucléaires"
            )),
            FicheRow(concept="Anti-CD20 (anti-B)", detail_md=(
                "- Molécules : **RITUXIMAB**, OBINUTUZUMAB, OFATUMUMAB\n"
                "- Mécanisme : inhibition du CD19/CD20, mort des lymphocytes B\n"
                "- Indications : vascularite à ANCA, sclérose en plaques, polyarthrite rhumatoïde, hémopathies\n"
                "- CI : tuberculose active, infections graves, insuffisance cardiaque NYHA III/IV\n"
                "- EI : **hypogammaglobulinémie**, réaction anaphylactoïde\n"
                "- Bilan : NFS, IUC, BHC, TP, TCA, fibrinogène, CRP, EPPS, dosage pondéral, "
                "sérologies VIH/VHB/VHC"
            )),
            FicheRow(concept="Dénosumab", detail_md=(
                "- **Anticorps monoclonal** humain anti-RANK-L\n"
                "- Indication : **ostéoporose** (notamment cortico-induite)\n"
                "- Nécessite un **bilan odontologique** avant mise en route\n"
                "- Thérapie ciblée, pas un anticorps chimérique"
            )),
            FicheRow(concept="", detail_md=(
                "- Avant toute biothérapie : **dépistage tuberculose** (IDR/QuantiFERON + Rx thorax) "
                "et **sérologies virales** obligatoires\n"
                "- Mise à jour vaccinale impérative (vaccins vivants CI sous biothérapie)"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE VI : SITUATIONS CLINIQUES INTÉGRÉES ──
    partie_vi = Partie(numero="VI", titre="Situations cliniques intégrées", sous_parties=[
        SousPartie(lettre="A", titre="Insuffisance rénale aiguë et néphrotoxicité", rows=[
            FicheRow(concept="Définition de l'IRA", detail_md=(
                "- Majoration de la créatinine > **50% en 7 jours** ou > **3 mg/L**\n"
                "- Ou chute de la diurèse < **0,5 mL/kg/h** pendant > 6h"
            )),
            FicheRow(concept="Raisonnement étiologique", detail_md=(
                "- **1. Caractérisation/gravité** : créatinine actuelle vs antérieure, urée, kaliémie, "
                "natrémie, ECG\n"
                "- **2. Bilan étiologique** :\n"
                "  - Éliminer une part **obstructive** : imagerie des voies urinaires\n"
                "  - Éliminer une part **fonctionnelle** :\n"
                "    - Clinique : perte de poids, diarrhées, IEC/ARA2, diurétiques, oligurie\n"
                "    - Biologie : Na_u < 20, Na/K < 1, FeNa < 1%, FeU < 35%, "
                "Créat_U/S > 30, Urée_U/S > 10\n"
                "  - Envisager une part **organique** : vasculaire, interstitielle, tubulaire, glomérulaire"
            )),
            FicheRow(concept="Médicaments néphrotoxiques fréquents", detail_md=(
                "| Médicament | Classe | Mécanisme de l'IRA |\n"
                "|------------|--------|-------------------|\n"
                "| ÉNALAPRIL | IEC | IRA fonctionnelle |\n"
                "| HYDROCHLOROTHIAZIDE | Thiazidique | IRA fonctionnelle |\n"
                "| DAPAGLIFLOZINE | iSGLT2 | IRA fonctionnelle |\n"
                "| FUROSÉMIDE | Diurétique de l'anse | IRA fonctionnelle |\n"
                "| AINS (ibuprofène) | Anti-inflammatoire | IRA fonctionnelle |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- En cas de déshydratation (diarrhées, vomissements), **suspendre** : IEC/ARA2, "
                "diurétiques, AINS, metformine, iSGLT2\n"
                "- Mnémo des médicaments à suspendre : **SAID** (SRAA-bloqueurs, AINS, iSGLT2, Diurétiques)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Équilibre acido-basique et toxiques dialysables", rows=[
            FicheRow(concept="Interprétation d'une acidose", detail_md=(
                "- **Acidose** : pH < **7,38**\n"
                "- **Métabolique** : HCO3- < 20 mmol/L\n"
                "- **Respiratoire** : PaCO2 > 45 mmHg\n"
                "- Compensation respiratoire attendue : PaCO2 = (HCO3- x 1,5) + 8 +/- 2"
            )),
            FicheRow(concept="Trou anionique", detail_md=(
                "- Formule : TA = (Na+ + K+) - (HCO3- + Cl-)\n"
                "- Normal : **12-20 mmol/L**\n"
                "- TA augmenté → excès d'anion indosé"
            )),
            FicheRow(concept="Acidose métabolique à TA augmenté", detail_md=(
                "- Mnémo **KUSMALE** :\n"
                "  - **K**etosis (acidocétose)\n"
                "  - **U**remia (insuffisance rénale)\n"
                "  - **S**alicylates\n"
                "  - **M**ethanol (Antigel)\n"
                "  - **A**ntigel\n"
                "  - **L**actates\n"
                "  - **E**thylène glycol"
            ), kind="mnemo"),
            FicheRow(concept="Hyperkaliémie : GISADRE", detail_md=(
                "- **G**luconate de calcium (10 mL/10%) : stabilisateur de membrane\n"
                "- **I**nsuline-glucose (10 UI dans G10 500 mL) : transfert intracellulaire\n"
                "- **S**albutamol (20 mg en nébulisation) : transfert intracellulaire\n"
                "- **A**lcalinisation : uniquement si acidose métabolique à TA normal\n"
                "- **D**iurétiques : déplétion\n"
                "- **R**ésines échangeuses : efficacité en quelques heures\n"
                "- **E**puration extra-rénale"
            ), kind="mnemo"),
            FicheRow(concept="Toxiques dialysables : MAMEL", detail_md=(
                "- **M**etformine\n"
                "- **A**spirine\n"
                "- **M**éthanol\n"
                "- **E**thylène glycol\n"
                "- **L**ithium"
            ), kind="mnemo"),
            FicheRow(concept="◆ Indications de l'EER en aigu", detail_md=(
                "- Gestion des **volumes** : anurie, OAP\n"
                "- Gestion des **toxiques** : urémie, toxiques médicamenteux\n"
                "- Gestion **hydroélectrolytique** : hyperkaliémie menaçante, "
                "hyponatrémie < 120 mmol/L"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La **metformine** provoque une acidose lactique en cas d'accumulation (IRA)\n"
                "- La metformine est **dialysable** : l'hémodialyse est le traitement de l'intoxication"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Anticoagulants et gestion des accidents hémorragiques", rows=[
            FicheRow(concept="Embolie pulmonaire : traitement", detail_md=(
                "- **Anticoagulation curative** : héparine (HNF, HBPM) ou AOD\n"
                "- ⚠ **AVK** non autorisés à la phase initiale\n"
                "- EP non grave à risque intermédiaire : **APIXABAN** (après dose de charge)\n"
                "- EP grave (instabilité hémodynamique) : thrombolyse à discuter"
            )),
            FicheRow(concept="Angioscanner thoracique", detail_md=(
                "- Examen de référence pour le diagnostic d'EP\n"
                "- **PCI autorisé** jusqu'à clairance **30 mL/min**\n"
                "- Recherche de signes de gravité : dilatation VD, rapport VD/VG > 1"
            )),
            FicheRow(concept="Accident hémorragique sous AOD", detail_md=(
                "- **Hématome du psoas** : complication classique sous anticoagulant\n"
                "  - Clinique : lombalgie + atteinte du psoas (flexion hanche) + anémie sans extériorisation\n"
                "- Conduite à tenir :\n"
                "  - 2 VVP, mise à jeun\n"
                "  - **Arrêt et dosage** du taux sanguin d'AOD\n"
                "  - Bilan pré-transfusionnel : 2 déterminations groupe sanguin + RAI + phénotypage\n"
                "  - **Transfusion** de CGR\n"
                "  - Antagonisation par **concentré de complexe prothrombinique** (CCP) à discuter\n"
                "  - Hospitalisation, antalgie, surveillance rapprochée"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ L'association **aspirine + anticoagulant** majore le risque hémorragique\n"
                "- ⚠ Un hématome profond sous anticoagulant peut être révélé par une **anémie isolée** "
                "sans saignement extériorisé"
            ), kind="piege"),
            FicheRow(concept="◆ OAP post-transfusionnel", detail_md=(
                "- Contexte : transfusion chez patient insuffisant cardiaque ou sujet âgé\n"
                "- Clinique : dyspnée, HTA, tachycardie, crépitants bilatéraux\n"
                "- Traitement **LMNOP** :\n"
                "  - **L**asilix (déplétion, surveillance K+)\n"
                "  - **M**orphine (visée eupnéisante)\n"
                "  - **N**itrés dérivés (sauf si PAS < 100 mmHg)\n"
                "  - **O**xygénothérapie (SpO2 > 90%)\n"
                "  - **P**osition demi-assise\n"
                "- Arrêt de la transfusion + déclaration d'hémovigilance"
            )),
            FicheRow(concept="", detail_md=(
                "- Chez le sujet âgé : ne pas transfuser **trop rapidement** les CGR\n"
                "- Le seuil transfusionnel dépend du **terrain** (comorbidités), pas de l'âge\n"
                "- Seuil de 8 g/dL si antécédents cardiovasculaires, 7 g/dL sinon"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Anti-infectieux : fluoroquinolones, macrolides, antipaludéens", rows=[
            FicheRow(concept="Fluoroquinolones (ciprofloxacine)", detail_md=(
                "- Indication : **pyélonéphrite** (en probabiliste), infections urinaires compliquées\n"
                "- Effets indésirables : **tendinopathie** (rupture du tendon d'Achille), photosensibilité, "
                "allongement du QT, neuropathie périphérique\n"
                "- Adaptation antibiothérapie après antibiogramme : switch vers **amoxicilline** "
                "si E. coli multisensible"
            )),
            FicheRow(concept="◆ Macrolides", detail_md=(
                "- Indication : **légionellose** (avec fluoroquinolones)\n"
                "- Alternative aux bêta-lactamines en cas d'allergie"
            )),
            FicheRow(concept="◆ Antipaludéens : quinine", detail_md=(
                "- Indication : paludisme grave si **artésunate** non disponible\n"
                "- Effets indésirables : **hypoglycémie**, **allongement du QT**, "
                "cinchonisme (acouphènes, vertiges), thrombopénie"
            )),
            FicheRow(concept="Traitement de la goutte", detail_md=(
                "- Crise : **colchicine** OU AINS OU corticoïdes\n"
                "- ⚠ AINS CI si allergie (angioedème de Quincke), insuffisance cardiaque, IRC\n"
                "- Traitement de fond : **allopurinol** (1re intention), **fébuxostat** (2e intention)\n"
                "- Association colchicine + allopurinol + RHD si crise + fond"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ AINS et allergie croisée : un angioedème à l'ibuprofène contre-indique "
                "TOUS les AINS (dont naproxène)\n"
                "- ⚠ Le fébuxostat est contre-indiqué en cas de cardiopathie ischémique"
            ), kind="piege"),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Comparaison des classes de diurétiques", markdown=(
            "| Classe | Molécule | Indication | EI principaux | Effet sur K+ | Effet sur Ca2+ |\n"
            "|--------|----------|-----------|---------------|-------------|---------------|\n"
            "| Anse | Furosémide | Déplétion (IC, IR, IH) | HypoK, HypoNa, IRA | HypoK | HypoCa |\n"
            "| Thiazidique | HCTZ | HTA, déplétion | HypoNa, HypoK, IRA | HypoK | HyperCa |\n"
            "| Épargneurs K+ | Spironolactone | HTA, IC | HyperK, gynécomastie | HyperK | - |\n"
            "| iSGLT2 | Dapagliflozine | IC, DT2, MRC | IRA fonctionnelle | - | - |\n"
        )),
        TableauSynthese(titre="IEC vs ARA2", markdown=(
            "| Critère | IEC | ARA2 |\n"
            "|---------|-----|------|\n"
            "| Exemples | Ramipril, Énalapril | Candésartan, Losartan |\n"
            "| Toux sèche | Oui (bradykinine) | Non |\n"
            "| Hyperkaliémie | Oui | Oui |\n"
            "| IRA fonctionnelle | Oui | Oui |\n"
            "| CI grossesse | Oui | Oui |\n"
            "| CI sténose art. rénale bilat. | Oui | Oui |\n"
            "| Angioedème | Risque spécifique | Moindre |\n"
        )),
        TableauSynthese(titre="Traitements de fond de la polyarthrite rhumatoïde", markdown=(
            "| Ligne | Traitements |\n"
            "|-------|------------|\n"
            "| 1re ligne | **MTX** / Léflunomide / Salazopyrine |\n"
            "| 2e ligne | Anti-TNF-alpha, anti-IL6-R, anti-CD20 |\n"
            "| 3e ligne | Inhibiteurs de JAK |\n"
        )),
        TableauSynthese(titre="Bilan pré-thérapeutique des immunosuppresseurs", markdown=(
            "| Traitement | Bilan systématique |\n"
            "|------------|-------------------|\n"
            "| Méthotrexate | NFS, IUC, BHC, albuminémie, EPPS, Rx thorax, sérologies virales |\n"
            "| Salazopyrine | NFS, IUC, BHC, Rx thorax, sérologies virales |\n"
            "| Léflunomide | NFS, IUC, BHC, Rx thorax, sérologies virales |\n"
            "| Anti-TNF | NFS, EPPS, ASAT/ALAT, Rx thorax, IDR/QTF, sérologies VHB/VHC/VIH, AAN |\n"
            "| Anti-CD20 | NFS, IUC, BHC, TP/TCA, CRP, EPPS, dosage Ig, sérologies VIH/VHB/VHC |\n"
        )),
        TableauSynthese(titre="IRA fonctionnelle vs organique", markdown=(
            "| Paramètre | IRA fonctionnelle | IRA organique |\n"
            "|-----------|------------------|---------------|\n"
            "| Na urinaire | < 20 mmol/L | > 40 mmol/L |\n"
            "| Na/K urinaire | < 1 | > 1 |\n"
            "| Fe Na+ | < 1% | > 1% |\n"
            "| Fe Urée | < 35% | > 35% |\n"
            "| Créat U/S | > 30 | < 30 |\n"
            "| Urée U/S | > 10 | < 10 |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| IRA : majoration créatinine | > **50%** en 7j ou > **3 mg/L** | Définition |\n"
        "| IRA : diurèse | < **0,5 mL/kg/h** pendant > 6h | Critère d'oligurie |\n"
        "| Trou anionique normal | **12-20 mmol/L** | TA = (Na+K) - (HCO3+Cl) |\n"
        "| Acidose : pH | < **7,38** | Définition |\n"
        "| LDL-C cible prévention 2aire | < **0,55 g/L** | Post-événement CV |\n"
        "| Triglycérides : seuil fibrates | > **5 g/L** | RHD si 1,5-5 g/L |\n"
        "| Biphosphonates sous CTC | ≥ **7,5 mg/j** pendant 3 mois | Équivalent prednisone |\n"
        "| PCI : clairance limite | > **30 mL/min** | Angioscanner autorisé |\n"
        "| Hyponatrémie sévère dialysable | < **120 mmol/L** | Indication EER |\n"
        "| Seuil transfusionnel (CV+) | **8 g/dL** | 7 g/dL sans ATCD CV |\n"
        "| PPR : dose CTC | **0,2-0,3 mg/kg/j** | Très corticosensible |\n"
        "| Horton : dose CTC | **0,7-1 mg/kg/j** | Dose d'attaque |\n"
    ))

    points_cles = [
        "Toute prescription doit suivre le raisonnement **DICTIAS** : Diagnostic, Indication, CI, Tolérance, Interactions, Associés, Secondaires",
        "Les IEC sont **néphroprotecteurs** au long cours mais provoquent une **IRA fonctionnelle** en situation de déshydratation ; la **toux** est spécifique des IEC (pas des ARA2)",
        "Les diurétiques de l'anse sont **hypokaliémiants** et **hypocalcémiants** ; les thiazidiques sont **hypokaliémiants** et **hypercalcémiants**",
        "En cas de déshydratation : **suspendre** IEC/ARA2, diurétiques, AINS, metformine, gliflozines",
        "Traitement post-SCA = **BASIC** : B-bloquant, Aspirine, Statine, IEC, Clopidogrel",
        "Avant toute biothérapie : **dépistage tuberculose** (IDR/QTF + Rx thorax) et sérologies virales obligatoires",
        "Le méthotrexate nécessite une supplémentation en **acide folique 48h après** ; CI absolue avec le **Bactrim**",
        "L'hyperkaliémie se traite par **GISADRE** ; les toxiques dialysables sont regroupés dans **MAMEL**",
    ]

    fiche_eclair_md = (
        "**DICTIAS** : raisonnement systématique pour justifier toute prescription "
        "(Diagnostic, Indication, CI, Tolérance, Interactions, Associés, Secondaires).\n\n"
        "**Diurétiques** : Anse (furosémide) = hypoK + hypoCa. Thiazidiques (HCTZ) = hypoK + hyperCa. "
        "Épargneurs K+ = hyperK + gynécomastie.\n\n"
        "**IEC** (ramipril, énalapril) : HTA, IC, néphroprotection. CI = grossesse, sténose bilatérale "
        "artères rénales. EI = hyperK, IRA, toux. ARA2 = même profil sans toux.\n\n"
        "**Hypolipémiants** : Statines en 1re ligne hypercholestérolémie. Fibrates si TG > 5 g/L. "
        "Cible LDLc < 0,55 g/L en prévention 2aire. Post-SCA = BASIC.\n\n"
        "**Corticothérapie** : mesures associées = vitamino-calcique, biphosphonates si >= 7,5 mg/j "
        "x 3 mois, IPP, déparasitage, vaccins, prise matinale.\n\n"
        "**MTX** : antifolique, 1re ligne PR. Acide folique 48h après. CI Bactrim. "
        "EI = macrocytose, PID, cytolyse. Biothérapies : bilan TB + sérologies pré-requis.\n\n"
        "**IRA** : fonctionnelle (Na_u < 20, FeNa < 1%) vs organique. "
        "Suspendre SAID en déshydratation. HyperK = GISADRE. Acidose métabolique à TA augmenté = KUSMALE.\n\n"
        "**Anticoagulants** : AVK CI à la phase initiale EP. Accident hémorragique sous AOD = "
        "arrêt + dosage + CCP + transfusion. OAP post-transfusionnel = LMNOP.\n\n"
        "**Toxiques dialysables** = MAMEL (Metformine, Aspirine, Méthanol, Éthylène glycol, Lithium)."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Pharmacologie",
        annee="2025-2026",
        item="Items 326, 330, 264, 220, 196, 198, 199, 217, 343",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        usage=UsageStats(),
    )


def main():
    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(exist_ok=True)

    fiche = build_pharmacologie_fiche()

    docx_path = output_dir / "Medecine_generale_Pharmacologie_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Medecine_generale_Pharmacologie_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path}")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

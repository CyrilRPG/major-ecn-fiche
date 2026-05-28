"""Génère la fiche exhaustive de Pneumologie à partir du PDF source et des annales."""

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


def build_pneumologie_fiche() -> FicheData:
    plan = [
        PlanPartie(numero="I", titre="Asthme", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et physiopathologie"),
            PlanSousPartie(lettre="B", titre="Tableau clinique"),
            PlanSousPartie(lettre="C", titre="Examens complémentaires et diagnostic"),
            PlanSousPartie(lettre="D", titre="Diagnostic différentiel"),
            PlanSousPartie(lettre="E", titre="Prise en charge"),
            PlanSousPartie(lettre="F", titre="Situations d'urgence : exacerbations et AAG"),
            PlanSousPartie(lettre="G", titre="Asthme de l'enfant et facteurs de risque de décès"),
        ]),
        PlanPartie(numero="II", titre="BPCO", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et facteurs de risque"),
            PlanSousPartie(lettre="B", titre="Tableau clinique"),
            PlanSousPartie(lettre="C", titre="Diagnostic positif : EFR"),
            PlanSousPartie(lettre="D", titre="Évaluation et prise en charge"),
            PlanSousPartie(lettre="E", titre="Exacerbations de BPCO"),
        ]),
        PlanPartie(numero="III", titre="Sémiologie et urgences respiratoires", sous_parties=[
            PlanSousPartie(lettre="A", titre="Douleur thoracique aiguë et chronique"),
            PlanSousPartie(lettre="B", titre="Dyspnée aiguë et chronique"),
            PlanSousPartie(lettre="C", titre="Hémoptysie"),
        ]),
        PlanPartie(numero="IV", titre="Épanchement pleural et pneumothorax", sous_parties=[
            PlanSousPartie(lettre="A", titre="Épanchement pleural"),
            PlanSousPartie(lettre="B", titre="Pneumothorax"),
        ]),
        PlanPartie(numero="V", titre="Imagerie et EFR", sous_parties=[
            PlanSousPartie(lettre="A", titre="Interprétation de la radiographie thoracique"),
            PlanSousPartie(lettre="B", titre="Explorations fonctionnelles respiratoires"),
        ]),
        PlanPartie(numero="VI", titre="Pathologies spécifiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Syndrome d'apnées obstructives du sommeil"),
            PlanSousPartie(lettre="B", titre="Tabagisme"),
            PlanSousPartie(lettre="C", titre="Toux aiguë et chronique"),
        ]),
    ]

    # ── PARTIE I : ASTHME ──
    partie_i = Partie(numero="I", titre="Asthme", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et physiopathologie", rows=[
            FicheRow(concept="★ Épidémiologie", detail_md=(
                "- **Prévalence** : adulte 5-7%, enfant 8%\n"
                "- **Mortalité** : ~1 000 décès/an en France\n"
                "- **FDR** : ATCD familiaux asthme, infections virales, sensibilisation aux pneumallergènes, "
                "exposition au tabac, pollution intérieure (biocombustibles), polluants atmosphériques (diesel)"
            )),
            FicheRow(concept="★ Définition", detail_md=(
                "- **Asthme** : maladie inflammatoire chronique des voies aériennes associant :\n"
                "  - Symptômes respiratoires paroxystiques (dyspnée, sifflements, oppression thoracique, toux)\n"
                "  - Obstruction des voies aériennes\n"
                "  - Variabilité des symptômes et de l'obstruction au cours du temps\n"
                "- **Hyper-réactivité bronchique** : bronchoconstriction exagérée lors exposition à divers stimuli (air sec, pollution)"
            )),
            FicheRow(concept="Physiopathologie", detail_md=(
                "- Inflammation caractérisée par réaction immunitaire **Th2**\n"
                "- Modifications structurales (remodelage)\n"
                "- Hyper-réactivité bronchique\n"
                "- Conséquence : **obstruction des voies aériennes**"
            )),
        ]),
        SousPartie(lettre="B", titre="Tableau clinique", rows=[
            FicheRow(concept="★ Terrain", detail_md=(
                "- ATCD familiaux d'asthme\n"
                "- ATCD personnels : **rhinite allergique**, rhino-sinusite chronique, **eczéma atopique**\n"
                "- Souvent diagnostic antérieur de « bronchites à répétition »"
            )),
            FicheRow(concept="★ Signes fonctionnels", detail_md=(
                "- Oppression thoracique\n"
                "- ★ **Sifflements expiratoires** transitoires\n"
                "- Dyspnée\n"
                "- Toux déclenchée par l'effort +/- sifflements\n"
                "- Symptômes de durée brève (quelques minutes à 20 min), **paroxystiques** et **récidivants**\n"
                "- Épisodes d'exacerbations et AAG : dyspnée aiguë type **bradypnée expiratoire**, sibilants, "
                "amélioration sous bronchodilatateurs"
            )),
            FicheRow(concept="◆ Histoire de la maladie", detail_md=(
                "- Association de **plusieurs symptômes**\n"
                "- Aggravation la **nuit** et au réveil\n"
                "- Caractère paroxystique et récidivant\n"
                "- Variabilité d'intensité\n"
                "- Déclenchement par : infections virales, exercice, allergènes, irritants, rire"
            )),
        ]),
        SousPartie(lettre="C", titre="Examens complémentaires et diagnostic", rows=[
            FicheRow(concept="★ EFR — Spirométrie", detail_md=(
                "- Courbe débit-volume : aspect **concave** avec diminution de l'ensemble des débits\n"
                "- ★ **Diagnostic positif** :\n"
                "  - **TVO** : VEMS/CVF < **0,7**\n"
                "  - **Réversibilité significative** après BDCA ou corticothérapie systémique 2 semaines :\n"
                "    - Augmentation VEMS > **200 mL** par rapport à la valeur initiale **ET**\n"
                "    - Augmentation > **12%** par rapport à la valeur initiale\n"
                "  - **Réversibilité complète** : normalisation VEMS/CVF > 0,7 **ET** normalisation VEMS"
            )),
            FicheRow(concept="⚠ Test de provocation", detail_md=(
                "- **Indications** : suspicion d'asthme à l'interrogatoire MAIS absence de TVO à l'état basal\n"
                "- ⚠ **Hyper-réactivité bronchique** : diminution VEMS > **20%** après inhalation de métacholine "
                "ou stimulation par air sec\n"
                "- ⚠ Piège : ne pas confondre réversibilité significative et complète"
            )),
            FicheRow(concept="DEP", detail_md=(
                "- Débit maximal instantané mesuré lors d'une expiration forcée\n"
                "- Moins fiable que le VEMS\n"
                "- Utile : urgences, diagnostic asthme professionnel, auto-surveillance"
            )),
            FicheRow(concept="RXT F+P", detail_md=(
                "- Indiquée lors de la **première consultation** et lors des **exacerbations graves**\n"
                "- Non recommandée pour le suivi\n"
                "- But : éliminer les diagnostics différentiels"
            )),
            FicheRow(concept="★ Bilan allergologique", detail_md=(
                "- **Indications** : bilan initial, contrôle non acquis malgré traitement\n"
                "- Par **prick-tests** vis-à-vis des pneumallergènes\n"
                "- Dosage IgE spécifiques si discordance clinique/prick-tests"
            )),
            FicheRow(concept="", detail_md=(
                "- Diagnostics différentiels **sans TVO** : syndrome de toux des VAS, dysfonction des cordes vocales, "
                "syndrome d'hyperventilation\n"
                "- Diagnostics différentiels **avec TVO non réversible** : **BPCO** (ACOS), bronchectasies, "
                "mucoviscidose, dysplasie bronchopulmonaire, bronchiolite obstructive, corps étranger, "
                "trachéobronchomalacie, insuffisance cardiaque"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Prise en charge au long cours", rows=[
            FicheRow(concept="★ Facteurs favorisants", detail_md=(
                "- **Rhinite** : antiH1 +/- corticoïde local\n"
                "- **Allergies respiratoires** : éviction allergènes +/- immunothérapie spécifique (DEP > 70%)\n"
                "- **Irritants bronchiques** : sevrage tabagique, éviction polluants\n"
                "- ⚠ **Médicaments** : CI absolue BB-, CI AINS/aspirine si ATCD d'intolérance\n"
                "- **Vaccinations** : anti-grippale (tous asthmatiques), anti-pneumococcique si IRC\n"
                "- Facteurs psychologiques, RGO (recherche systématique), obésité"
            )),
            FicheRow(concept="★ Paliers thérapeutiques", detail_md=(
                "| Palier | Traitement de fond | Traitement de crise |\n"
                "|--------|-------------------|--------------------|\n"
                "| 1 | Aucun | BDCA à la demande |\n"
                "| 2 | **CSI faible dose** | BDCA |\n"
                "| 3 | CSI faible dose + **BDLA** ou CSI moyenne/forte dose | BDCA |\n"
                "| 4 | CSI moyenne/forte dose + BDLA + AL/théophylline | BDCA |\n"
                "| 5 | Palier 4 + corticostéroïdes PO / **anti-IgE** si asthme sévère non contrôlé | BDCA |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Le traitement de fond dans l'asthme doit **TOUJOURS** comporter un **corticostéroïde inhalé**\n"
                "- Mise en place immédiate sans attendre les résultats des examens complémentaires\n"
                "- Commencer en général par palier 2 (ou 3 si mal contrôlé)"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Contrôle de l'asthme", detail_md=(
                "- **Asthme contrôlé** : symptômes contrôlés, exacerbations rares (< 2 cures CTC/an), "
                "VEMS > 80%\n"
                "- Contrôlé ≥ 3 mois : diminuer jusqu'à dose minimale efficace\n"
                "- Non contrôlé : majorer traitement (palier supérieur)\n"
                "- Réévaluation après **1 à 3 mois**"
            )),
            FicheRow(concept="◆ Sévérité", detail_md=(
                "- Évaluée quand asthme contrôlé > 6 mois avec dose minimale :\n"
                "  - Palier 1 → **intermittent**\n"
                "  - Palier 2 → **persistant léger**\n"
                "  - Palier 3 → **persistant modéré**\n"
                "  - Palier 4 → **persistant sévère**\n"
                "  - Palier 5 → **asthme sévère**"
            )),
            FicheRow(concept="★ Éducation thérapeutique", detail_md=(
                "- Plan d'action : reconnaissance exacerbation, modalités traitement, accès aux soins\n"
                "- 4 étapes : diagnostic éducatif → contrat éducatif → activités éducatives → évaluation\n"
                "- Processus continu, réactualisé régulièrement\n"
                "- CI plongée sous-marine en scaphandre"
            )),
        ]),
        SousPartie(lettre="E", titre="Situations d'urgence : exacerbations et AAG", rows=[
            FicheRow(concept="★ Définition", detail_md=(
                "- **Exacerbation** : augmentation progressive des symptômes sans retour à la normale "
                "et diminution progressive de la fonction respiratoire"
            )),
            FicheRow(concept="★ FDR exacerbation", detail_md=(
                "- Symptômes non contrôlés\n"
                "- Absence de CSI (non-prescription, non-observance, mauvaise technique)\n"
                "- ⚠ Utilisation excessive BDCA : > **1 flacon/mois**\n"
                "- VEMS < **60%**\n"
                "- Problèmes psychologiques/socio-économiques\n"
                "- Exposition tabac/allergènes\n"
                "- Comorbidités : obésité, rhinosinusite, allergie alimentaire\n"
                "- Éosinophilie sanguine/dans les crachats\n"
                "- Grossesse\n"
                "- ATCD intubation/hospitalisation USI"
            )),
            FicheRow(concept="★ Classification", detail_md=(
                "| Signes | Exacerbation modérée | Exacerbation sévère |\n"
                "|--------|---------------------|--------------------|\n"
                "| Parole | Phrases | Mots |\n"
                "| Position | Assis | Penché en avant |\n"
                "| Agitation | Non | Oui |\n"
                "| FR | Augmentée | > 30/min |\n"
                "| Muscles accessoires | Non | Oui |\n"
                "| FC | > 100 bpm | > 120 bpm |\n"
                "| SpO2 | < 95% AA | < 90% AA |\n"
                "| DEP | > 50% meilleure valeur | < 50% meilleure valeur |\n"
            )),
            FicheRow(concept="★ Traitement exacerbation modérée", detail_md=(
                "- **BDCA** B2-mimétiques inhalés : 4-10 bouffées chambre d'inhalation /20 min × 1h\n"
                "  - En milieu médicalisé : nébulisation 5 mg sur 10-15 min /20 min\n"
                "- **Corticothérapie PO** prednisolone/prednisone 5-7 jours :\n"
                "  - Adulte : 0,5-1 mg/kg/j (max **60 mg/j**)\n"
                "  - Enfant : 2 mg/kg/j (max **40 mg/j**)\n"
                "- **O2** : objectif SpO2 93-95% (adulte), 94-98% (enfant)\n"
                "- Si aggravation/non amélioration après 1h → transfert USI"
            )),
            FicheRow(concept="★ Traitement exacerbation sévère", detail_md=(
                "- Transfert médicalisé en **USI**\n"
                "- O2 (objectif SpO2 93-95%)\n"
                "- BDCA B2-mimétiques + **anticholinergique (ipratropium)** nébulisés\n"
                "- Si échec : B2-mimétiques **injectables** :\n"
                "  - Domicile : terbutaline 0,5 mg SC\n"
                "  - SAMU/hôpital : salbutamol **IVSE** 0,25-0,5 mg/h sous scope\n"
                "- Corticoïdes **IV** : 0,5-1 mg/kg/j (max **80 mg/j**)\n"
                "- Ventilation mécanique si signes de gravité extrême"
            )),
            FicheRow(concept="", detail_md=(
                "- **Critères de gravité extrême** : cyanose, respiration paradoxale, pauses respiratoires, "
                "silence auscultatoire, bradycardie, collapsus, troubles de conscience"
            ), kind="piege"),
        ]),
        SousPartie(lettre="F", titre="Asthme de l'enfant < 36 mois", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Tout épisode dyspnéique avec râles sibilants, produit **au moins 3 fois** depuis la naissance\n"
                "- Diagnostic positif : symptômes récidivants à prédominance nocturne, normalité RXT, "
                "efficacité du traitement antiasthmatique, signes d'atopie personnels/familiaux"
            )),
            FicheRow(concept="★ FDR décès par asthme", detail_md=(
                "- ATCD d'exacerbation sévère (intubation, USI)\n"
                "- Non-observance, mauvaise technique d'inhalation\n"
                "- Utilisation excessive de BDCA\n"
                "- Absence de CSI\n"
                "- Comorbidités psychiatriques\n"
                "- Problèmes socio-économiques"
            )),
        ]),
    ])

    # ── PARTIE II : BPCO ──
    partie_ii = Partie(numero="II", titre="BPCO", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et facteurs de risque", rows=[
            FicheRow(concept="★ Définition", detail_md=(
                "- **BPCO** : maladie respiratoire chronique définie par une obstruction **permanente** "
                "et **progressive** des voies aériennes\n"
                "- **Prévalence** : ~7,5% de la population > 40 ans\n"
                "- Incidence se stabilise chez l'homme, augmente chez la femme"
            )),
            FicheRow(concept="★ FDR", detail_md=(
                "- ★ **Tabac+++** (> 15 PA femme, > 20 PA homme), cannabis\n"
                "- Exposition aéro-contaminants professionnels\n"
                "- Pollution"
            )),
            FicheRow(concept="◆ Entités cliniques", detail_md=(
                "- **Bronchite chronique** (définition clinique) : toux productive quotidienne > **3 mois/an** "
                "pendant > **2 années consécutives**\n"
                "  - 50% des fumeurs, peut être simple (sans TVO) ou obstructive (avec TVO = BPCO)\n"
                "- **Emphysème** : élargissement permanent des espaces aériens distaux avec destruction parois "
                "alvéolaires, sans fibrose\n"
                "  - Centro-lobulaire ou pan-lobulaire\n"
                "  - Radio : zones d'hypodensité (raréfaction parenchyme)"
            )),
        ]),
        SousPartie(lettre="B", titre="Tableau clinique", rows=[
            FicheRow(concept="Signes fonctionnels", detail_md=(
                "- **Dyspnée** : initialement à l'effort, évaluée par échelle **mMRC**\n"
                "- Toux, expectoration"
            )),
            FicheRow(concept="★ Signes physiques", detail_md=(
                "- Stades croissants : ronchi → allongement temps expiratoire → diminution MV → "
                "distension thoracique (thorax en tonneau)\n"
                "- ★ **Signe de Hoover** : diminution paradoxale du diamètre transversal thoracique inférieur "
                "à l'inspiration (distension sévère)\n"
                "- Posture du **tripode** : assis, penché en avant, appui mains sur cuisses\n"
                "- Exacerbations : muscles respiratoires accessoires (SCM++), expiration abdominale active"
            )),
            FicheRow(concept="Phénotypes", detail_md=(
                "| | Blue bloater | Pink puffer |\n"
                "|--|-------------|------------|\n"
                "| Prédominance | Voies aériennes | Emphysème |\n"
                "| Morphotype | Corpulent | Maigre, distendu |\n"
                "| Hypoxémie | Franche, cyanose | Modérée |\n"
                "| ICD | Fréquente | Absente |\n"
            )),
        ]),
        SousPartie(lettre="C", titre="Diagnostic positif : EFR", rows=[
            FicheRow(concept="★ Spirométrie", detail_md=(
                "- ★ **TVO persistant** (non complètement réversible) : **VEMS/CVF < 0,7** après BD\n"
                "- Réversibilité significative possible dans la BPCO\n"
                "- ⚠ **Réversibilité complète** (VEMS/CVF > 0,7 + normalisation VEMS) → **exclut la BPCO**"
            )),
            FicheRow(concept="◆ Sévérité GOLD", detail_md=(
                "| Stade | VEMS post-BD |\n"
                "|-------|-------------|\n"
                "| GOLD 1 (léger) | ≥ 80% |\n"
                "| GOLD 2 (modéré) | 50-79% |\n"
                "| GOLD 3 (sévère) | 30-49% |\n"
                "| GOLD 4 (très sévère) | < 30% |\n"
            )),
            FicheRow(concept="Pléthysmographie", detail_md=(
                "- Mesure volumes statiques : **VR**, CRF, CPT\n"
                "- Distension pulmonaire : augmentation VR avec VR/CPT élevé"
            )),
            FicheRow(concept="Transfert du CO", detail_md=(
                "- Reflète la surface d'échanges gazeux disponible\n"
                "- Pathologique : **DLCO < 70%** valeur prédite\n"
                "- Évalue la destruction alvéolaire (emphysème)"
            )),
        ]),
        SousPartie(lettre="D", titre="Évaluation et prise en charge", rows=[
            FicheRow(concept="★ Bilan initial", detail_md=(
                "- EFR + score **GOLD**\n"
                "- NFS (polyglobulie → IRC), ionogramme, créatinine\n"
                "- Bilan nutritionnel (dénutrition = mauvais pronostic)\n"
                "- **GDS** : recherche d'insuffisance respiratoire\n"
                "- RXT (pas d'intérêt pour le diagnostic positif, recherche cancer/anomalies)\n"
                "- TDM thoracique non systématique\n"
                "- ECG + ETT si signes cardiaques (cœur pulmonaire chronique)"
            )),
            FicheRow(concept="★ Mesures générales", detail_md=(
                "- ★ **Sevrage tabagique** +++ : seule mesure interrompant la progression de l'obstruction\n"
                "- ALD si PaO2 < 60 mmHg et/ou PaCO2 > 50 mmHg ou VEMS < 50%\n"
                "- Activité physique régulière, alimentation équilibrée"
            )),
            FicheRow(concept="★ Vaccinations", detail_md=(
                "- Anti-grippale **tous les ans**\n"
                "- Anti-pneumococcique **tous les 5 ans**"
            )),
            FicheRow(concept="★ Traitement pharmacologique", detail_md=(
                "- **BDLA inhalés** : B2-mimétiques LDA et/ou anticholinergiques LDA\n"
                "  - Anticholinergiques LDA plus efficaces pour réduire les exacerbations\n"
                "- Traitements CDA « à la demande » si dyspnée\n"
                "- ⚠ **CSI seuls** et **corticothérapie orale** : **PAS indiqués** dans la BPCO\n"
                "- CSI en association avec BDLA si VEMS < 70% + exacerbations fréquentes (> 2/an)\n"
                "- Ne pas prescrire d'antitussifs"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Ne jamais prescrire de CSI seul dans la BPCO (contrairement à l'asthme)\n"
                "- ⚠ Ne jamais prescrire de corticothérapie orale au long cours dans la BPCO"
            ), kind="piege"),
            FicheRow(concept="◆ Réhabilitation respiratoire", detail_md=(
                "- Recommandée dès le **stade II** si dyspnée/diminution tolérance exercice\n"
                "- Approche multidisciplinaire : optimisation traitement, éducation, kinésithérapie "
                "(drainage, renforcement musculaire, endurance), prise en charge psychosociale et nutritionnelle"
            )),
            FicheRow(concept="★ Stade IV", detail_md=(
                "- **Oxygénothérapie longue durée** si IRC\n"
                "- **VNI nocturne** si SAS associé ou IRC hypercapnique grave\n"
                "- < 65 ans : penser à la **transplantation**"
            )),
        ]),
        SousPartie(lettre="E", titre="Exacerbations de BPCO", rows=[
            FicheRow(concept="★ Définition", detail_md=(
                "- Événement aigu : aggravation > **24h** des symptômes respiratoires → modification thérapeutique\n"
                "- Critères d'**Anthonisen** : augmentation volume/purulence expectoration, augmentation dyspnée"
            )),
            FicheRow(concept="★ Étiologie", detail_md=(
                "- **Infectieuse** le plus souvent : H. influenzae, S. pneumoniae, Moraxella catarrhalis\n"
                "- Pseudomonas aeruginosa si VEMS < 50% ou séjour hospitalier\n"
                "- Cause environnementale (pollution)\n"
                "- Non identifiée fréquemment"
            )),
            FicheRow(concept="◆ Traitement", detail_md=(
                "- **Bronchodilatateurs** CDA inhalés (B2-mimétiques +/- anticholinergiques)\n"
                "- **O2** : objectif SpO2 **88-92%** (⚠ différent de l'asthme !)\n"
                "- **ATB** si : expectoration purulente, BPCO très sévère (VEMS < 30%), signes de gravité\n"
                "  - Molécules : amoxicilline +/- acide clavulanique, pristinamycine (5-7 jours)\n"
                "- **Corticothérapie systémique** :\n"
                "  - Domicile : 2e intention si pas d'amélioration après 48h\n"
                "  - Hôpital : < 40 mg/j pendant max 5 jours\n"
                "- Kinésithérapie si encombrement, prophylaxie thrombose\n"
                "- **VNI** en 1re intention si acidose respiratoire ; intubation si troubles de conscience"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Objectif SpO2 dans la BPCO : **88-92%** (et non 93-95% comme dans l'asthme)\n"
                "- Risque d'aggraver une hypercapnie si O2 trop généreux"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE III : SÉMIOLOGIE ET URGENCES RESPIRATOIRES ──
    partie_iii = Partie(numero="III", titre="Sémiologie et urgences respiratoires", sous_parties=[
        SousPartie(lettre="A", titre="Douleur thoracique aiguë et chronique", rows=[
            FicheRow(concept="★ Interrogatoire", detail_md=(
                "- ATCD familiaux/personnels, FDRCV, traitements\n"
                "- Analyse sémiologique de la douleur\n"
                "- Signes associés"
            )),
            FicheRow(concept="★ Examens initiaux", detail_md=(
                "- **RXT** face en inspiration\n"
                "- **ECG** 12 dérivations + V3R, V4R, V7, V8, V9\n"
                "- Si bradypnée/tachypnée ou SpO2 < 95% : **GDS**\n"
                "- Selon orientation : troponine Ic, D-dimères"
            )),
            FicheRow(concept="★ Urgences vitales", detail_md=(
                "- **SCA** (1/3 des douleurs thoraciques aux urgences)\n"
                "- **Embolie pulmonaire**\n"
                "- **Dissection aortique**\n"
                "- **Tamponnade**\n"
                "- Rupture de l'œsophage\n"
                "- Pneumothorax"
            )),
            FicheRow(concept="Douleurs rythmées par la respiration", detail_md=(
                "- Post-traumatiques (fractures de côtes)\n"
                "- Pneumonies infectieuses +/- pleurésie\n"
                "- Épanchement pleural, infarctus pulmonaire\n"
                "- Trachéobronchite aiguë : brûlure respiratoire, cortège viral\n"
                "- Atteintes musculo-squelettiques : reproductible à la palpation"
            )),
            FicheRow(concept="Douleurs non rythmées", detail_md=(
                "- Causes cardiaques : angor d'effort, RA serré, FA, myocardiopathie obstructive, péricardite\n"
                "- ★ **Cocaïne** : à rechercher systématiquement (SCA, PNO)\n"
                "- Zona thoracique\n"
                "- Affections digestives : RGO, spasmes œsophagiens, pancréatite, cholécystite\n"
                "- Douleurs psychogènes (1/4 des douleurs aux urgences) : diagnostic d'élimination"
            )),
        ]),
        SousPartie(lettre="B", titre="Dyspnée aiguë et chronique", rows=[
            FicheRow(concept="★ Interrogatoire", detail_md=(
                "- Chronologie : aiguë (heures/jours) vs chronique (semaines/mois)\n"
                "- Cycle respiratoire : inspiratoire vs expiratoire\n"
                "- Position : **orthopnée** (IC, dysfonction diaphragme), **antépnée**, **platypnée** (MAV)"
            )),
            FicheRow(concept="★ Échelle mMRC", detail_md=(
                "| Stade | Description |\n"
                "|-------|------------|\n"
                "| 0 | Essoufflé pour effort important |\n"
                "| 1 | Essoufflé en se dépêchant à plat / pente légère |\n"
                "| 2 | Marche plus lentement / s'arrête à son pas à plat |\n"
                "| 3 | S'arrête après 90 m à plat |\n"
                "| 4 | Trop essoufflé pour quitter la maison |\n"
            )),
            FicheRow(concept="★ Signes de gravité", detail_md=(
                "- **Détresse respiratoire** : cyanose, sueurs, polypnée > 30/min, tirage, "
                "respiration abdominale paradoxale\n"
                "- **Hémodynamique** : tachycardie > 110/min, choc, PAS < 90 mmHg, IVD aiguë\n"
                "- **Neurologique** : agitation, torpeur, asterixis, coma"
            )),
            FicheRow(concept="◆ Dyspnée aiguë — étiologies", detail_md=(
                "- **Temps inspiratoire allongé** (obstruction VAS) : corps étranger, œdème de Quincke, "
                "laryngite sous-glottique\n"
                "- **Temps expiratoire allongé** (atteinte bronchique) : exacerbation asthme/BPCO, OAP\n"
                "- **Sans allongement** : EP, pneumothorax, pneumonie, OAP"
            )),
            FicheRow(concept="Dyspnée chronique — étiologies", detail_md=(
                "- **Pulmonaires** : BPCO, asthme, PID, pneumoconioses\n"
                "- **Cardiaques** : IC, constriction péricardique\n"
                "- **HTP**\n"
                "- Autres : anémie, acidose métabolique, causes neuro-musculaires, hyperventilation"
            )),
        ]),
        SousPartie(lettre="C", titre="Hémoptysie", rows=[
            FicheRow(concept="★ Définition", detail_md=(
                "- Saignement extériorisé (ou non) des voies respiratoires basses\n"
                "- ⚠ Éliminer : hématémèse, épistaxis déglutie, saignement ORL"
            )),
            FicheRow(concept="★ Étiologies", detail_md=(
                "- **Cancer bronchique** +++\n"
                "- Tuberculose (active ou séquellaire)\n"
                "- Bronchectasies\n"
                "- Aspergillome\n"
                "- EP avec infarctus pulmonaire\n"
                "- Pneumonies nécrosantes\n"
                "- Corps étranger\n"
                "- Causes cardiovasculaires : RM, IC, MAV"
            )),
            FicheRow(concept="◆ Bilan", detail_md=(
                "- **Scanner thoracique** injecté : recherche lésion responsable\n"
                "- **Fibroscopie bronchique** : localise le saignement, biopsies\n"
                "- NFS, bilan d'hémostase, groupe sanguin"
            )),
            FicheRow(concept="★ PEC urgente", detail_md=(
                "- Hospitalisation, position demi-assise\n"
                "- O2, voie veineuse, bilan pré-transfusionnel\n"
                "- Si hémoptysie massive : **artériographie bronchique + embolisation**\n"
                "- Vasoconstricteurs IV (terlipressine)\n"
                "- Intubation sélective si détresse"
            )),
        ]),
    ])

    # ── PARTIE IV : ÉPANCHEMENT PLEURAL ET PNEUMOTHORAX ──
    partie_iv = Partie(numero="IV", titre="Épanchement pleural et pneumothorax", sous_parties=[
        SousPartie(lettre="A", titre="Épanchement pleural", rows=[
            FicheRow(concept="Physiopathologie", detail_md=(
                "- Espace pleural : cavité virtuelle, pression négative\n"
                "- Production 5-20 cc/j de liquide pleural\n"
                "- Anomalie « mécanique » → **transsudat**\n"
                "- Agression inflammatoire/infectieuse/néoplasique → **exsudat**"
            )),
            FicheRow(concept="★ Clinique", detail_md=(
                "- Dyspnée, douleur latéro-thoracique (majorée par respiration/toux)\n"
                "- Toux sèche au changement de position → caractère non cloisonné\n"
                "- ★ **Syndrome pleural liquidien** :\n"
                "  - Abolition du MV\n"
                "  - **Matité** à la percussion\n"
                "  - Abolition des vibrations vocales\n"
                "  - Souffle pleurétique (doux, lointain, expiratoire)"
            )),
            FicheRow(concept="★ Imagerie", detail_md=(
                "- **RXT** : opacité dense, homogène, non systématisée, ligne de **Damoiseau** "
                "(concave en haut et en dedans)\n"
                "- **Échographie** : image anéchogène, épanchements cloisonnés, guide ponctions\n"
                "- **TDM** : en urgence si EP/hémothorax suspecté"
            )),
            FicheRow(concept="★ Ponction pleurale", detail_md=(
                "- **Systématique** sauf si : < 10 mm échographie, ou IC gauche suspectée "
                "(sauf si atypique ou résistant au traitement)\n"
                "- En urgence si : épanchement fébrile, suspicion hémothorax, mauvaise tolérance\n"
                "- Bord supérieur de la côte inférieure de l'EIC\n"
                "- RXT/échographie post-contrôle systématique (PNO iatrogène 3%)"
            )),
            FicheRow(concept="★ Transsudat vs exsudat", detail_md=(
                "| | Transsudat | Exsudat |\n"
                "|--|-----------|--------|\n"
                "| Leucocytes | < 1 000/µL | > 1 000/µL |\n"
                "| Protéines | < 30 g/L (Light) | > 30 g/L |\n"
                "| PNN | | Parapneumonique, EP |\n"
                "| Lymphocytes | | BK, cancers, sarcoïdose |\n"
                "| Éosinophiles | | Hémothorax, PNO, médicaments |\n\n"
                "**Transsudats** : ICG (bilatéral), cirrhose, SN, dialyse\n\n"
                "**Exsudats** : cancers, infections, EP, tuberculose, collagénoses"
            )),
        ]),
        SousPartie(lettre="B", titre="Pneumothorax", rows=[
            FicheRow(concept="★ Définition et types", detail_md=(
                "- Présence d'air dans la cavité pleurale\n"
                "- **PNO spontané primaire** : sujet jeune, longiligne, sans pathologie pulmonaire\n"
                "- **PNO spontané secondaire** : sur poumon pathologique (BPCO, emphysème, fibrose)\n"
                "- **PNO traumatique** : fractures costales, iatrogène (ponction, ventilation)"
            )),
            FicheRow(concept="★ Clinique", detail_md=(
                "- Douleur thoracique brutale, type « coup de poignard », latéralisée\n"
                "- Dyspnée variable\n"
                "- ★ **Syndrome pleural aérien** :\n"
                "  - Abolition du MV\n"
                "  - **Tympanisme** à la percussion\n"
                "  - Abolition des vibrations vocales"
            )),
            FicheRow(concept="★ Imagerie", detail_md=(
                "- **RXT** inspiration : hyperclarté avasculaire périphérique, ligne de rétraction\n"
                "- ⚠ TDM si doute diagnostique ou PNO secondaire"
            )),
            FicheRow(concept="★ PEC", detail_md=(
                "- **PNO spontané primaire petit** (< 2 cm) : surveillance, repos\n"
                "- **PNO modéré/symptomatique** : exsufflation à l'aiguille\n"
                "- **PNO complet/récidivant** : drainage thoracique\n"
                "- **PNO suffocant** (compressif) : **URGENCE** → exsufflation immédiate"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ PNO compressif = urgence vitale → exsufflation sans attendre l'imagerie\n"
                "- Signes : détresse respiratoire + déviation trachée + turgescence jugulaire + "
                "tympanisme unilatéral"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE V : IMAGERIE ET EFR ──
    partie_v = Partie(numero="V", titre="Imagerie et EFR", sous_parties=[
        SousPartie(lettre="A", titre="Interprétation de la radiographie thoracique", rows=[
            FicheRow(concept="★ Critères qualité", detail_md=(
                "- **Face** : debout, inspiration profonde, rayon postéro-antérieur\n"
                "- Vérifier : identité, date, centrage (épineuses entre clavicules), "
                "inspiration (6 arcs costaux antérieurs visibles), pénétration (rachis visible derrière cœur)"
            )),
            FicheRow(concept="Cliché de profil", detail_md=(
                "- Profil gauche de préférence\n"
                "- Repères : cyphose dorsale, clarté rétro-sternale et rétro-cardiaque"
            )),
            FicheRow(concept="★ Syndromes radiologiques", detail_md=(
                "- **Syndrome alvéolaire** : opacités floconneuses, confluentes, bronchogramme aérien, "
                "systématisé\n"
                "- **Syndrome interstitiel** : réticulations, lignes de Kerley, images en verre dépoli, "
                "rayon de miel\n"
                "- **Syndrome pleural** : ligne de Damoiseau (liquide), hyperclarté (air)\n"
                "- **Syndrome médiastinal** : élargissement médiastin, déplacement trachée\n"
                "- **Atélectasie** : opacité rétractile, déviation médiastin vers l'atélectasie"
            )),
        ]),
        SousPartie(lettre="B", titre="EFR — Synthèse", rows=[
            FicheRow(concept="★ TVO", detail_md=(
                "- **VEMS/CVF < 0,7** (rapport de Tiffeneau)\n"
                "- Causes : asthme, BPCO, bronchectasies, mucoviscidose"
            )),
            FicheRow(concept="TVR", detail_md=(
                "- **CPT < 80%** de la valeur prédite\n"
                "- Causes : PID, pathologies neuro-musculaires, obésité, déformations thoraciques"
            )),
            FicheRow(concept="Trouble mixte", detail_md=(
                "- Association TVO + TVR\n"
                "- Ex : BPCO évoluée avec composante restrictive"
            )),
        ]),
    ])

    # ── PARTIE VI : PATHOLOGIES SPÉCIFIQUES ──
    partie_vi = Partie(numero="VI", titre="Pathologies spécifiques", sous_parties=[
        SousPartie(lettre="A", titre="SAOS", rows=[
            FicheRow(concept="★ Définition", detail_md=(
                "- **SAOS** : survenue pendant le sommeil d'épisodes récurrents d'obstruction "
                "complète (apnée) ou incomplète (hypopnée) des VAS\n"
                "- **IAH** (index apnée-hypopnée) :\n"
                "  - Léger : **5-14**/h\n"
                "  - Modéré : **15-29**/h\n"
                "  - Sévère : ≥ **30**/h"
            )),
            FicheRow(concept="★ Clinique", detail_md=(
                "- Symptômes nocturnes : ronflements, apnées constatées, réveils avec sensation d'étouffement\n"
                "- Symptômes diurnes : **somnolence diurne excessive** (échelle d'Epworth), "
                "céphalées matinales, troubles de concentration\n"
                "- ★ Complications CV : **HTA** ++ (diastolique et résistante), troubles du rythme, "
                "AVC, IDM, insuffisance cardiaque"
            )),
            FicheRow(concept="★ Diagnostic", detail_md=(
                "- **Polysomnographie** (examen de référence) ou polygraphie ventilatoire nocturne\n"
                "- EFR et GDS normaux dans le SAOS isolé\n"
                "- Bilan des comorbidités : ECG, ETT, bilan métabolique"
            )),
            FicheRow(concept="★ Traitement", detail_md=(
                "- **PPC** (pression positive continue) : traitement de référence si IAH ≥ 15/h "
                "ou IAH 5-14/h avec symptômes\n"
                "- **Orthèse d'avancée mandibulaire** si IAH entre 5 et 29/h ou refus/échec PPC\n"
                "- Mesures hygiéno-diététiques : perte de poids, éviction alcool/sédatifs le soir, "
                "position latérale\n"
                "- Chirurgie ORL dans certains cas (amygdalectomie, UPPP)"
            )),
        ]),
        SousPartie(lettre="B", titre="Tabagisme", rows=[
            FicheRow(concept="★ Épidémiologie", detail_md=(
                "- **1re cause de mortalité prématurée** évitable en France\n"
                "- ~75 000 décès/an\n"
                "- FDR : cancer bronchique, BPCO, maladies cardiovasculaires\n"
                "- Lien établi troubles anxio-dépressifs et tabagisme"
            )),
            FicheRow(concept="★ Évaluation", detail_md=(
                "- **Test de Fagerström** : évalue la dépendance nicotinique\n"
                "- Questions clés : délai première cigarette au réveil, nombre de cigarettes/jour\n"
                "- Évaluer la motivation : modèle de **Prochaska** (précontemplation → contemplation → "
                "préparation → action → maintien)"
            )),
            FicheRow(concept="★ Sevrage tabagique", detail_md=(
                "- **TNS** (traitement nicotinique substitutif) : patchs, gommes, pastilles\n"
                "  - En 1re intention, peut être combiné\n"
                "- **Varénicline** : agoniste partiel récepteurs nicotiniques\n"
                "- **Bupropion** : antidépresseur, 2e intention\n"
                "- Accompagnement psychologique, TCC\n"
                "- ⚠ Syndrome de sevrage : irritabilité, anxiété, troubles du sommeil, "
                "prise de poids, constipation, céphalées"
            )),
            FicheRow(concept="Cigarette électronique", detail_md=(
                "- Non recommandée officiellement comme outil de sevrage\n"
                "- Peut être utilisée en réduction des risques si le patient le souhaite"
            )),
        ]),
        SousPartie(lettre="C", titre="Toux aiguë et chronique", rows=[
            FicheRow(concept="Définitions", detail_md=(
                "- **Toux aiguë** : < 3 semaines\n"
                "- **Toux chronique** : > **8 semaines**\n"
                "- Toux subaiguë : 3-8 semaines"
            )),
            FicheRow(concept="★ Toux aiguë — étiologies", detail_md=(
                "- Infections VAS : rhinopharyngite, sinusite, laryngite\n"
                "- Infections VAI : bronchite aiguë, pneumonie\n"
                "- Exacerbation asthme/BPCO\n"
                "- EP, IC, pneumothorax\n"
                "- Corps étranger (enfant ++)"
            )),
            FicheRow(concept="★ Toux chronique — étiologies", detail_md=(
                "- **3 causes principales** (80% des cas) :\n"
                "  - ★ **Rhinorrhée postérieure** (jetage postérieur)\n"
                "  - ★ **Asthme** (toux-équivalent d'asthme)\n"
                "  - ★ **RGO**\n"
                "- Toux médicamenteuse : **IEC** +++ (toux sèche, arrêt ≥ 4 semaines pour résolution)\n"
                "- Autres : tabagisme, BPCO, cancer bronchique, PID, IC, coqueluche, tuberculose"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours rechercher IEC dans les traitements avant d'explorer une toux chronique\n"
                "- ⚠ RXT systématique devant toute toux chronique"
            ), kind="piege"),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Asthme vs BPCO — Comparaison", markdown=(
            "| Critère | Asthme | BPCO |\n"
            "|---------|--------|------|\n"
            "| Âge de début | Souvent jeune | > 40 ans |\n"
            "| Tabac | Non obligatoire | Quasi-constant |\n"
            "| TVO | Réversible | Persistant |\n"
            "| VEMS/CVF après BD | Normalisation possible | Reste < 0,7 |\n"
            "| CSI seul | Traitement de base | NON indiqué |\n"
            "| O2 en urgence | SpO2 93-95% | SpO2 88-92% |\n"
            "| Inflammation | Th2, éosinophiles | Neutrophiles |\n"
        )),
        TableauSynthese(titre="Paliers thérapeutiques de l'asthme", markdown=(
            "| Palier | Traitement de fond | Crise |\n"
            "|--------|-------------------|-------|\n"
            "| 1 | Aucun | BDCA |\n"
            "| 2 | CSI faible dose | BDCA |\n"
            "| 3 | CSI faible dose + BDLA ou CSI moyenne/forte dose | BDCA |\n"
            "| 4 | CSI moyenne/forte + BDLA + AL/théophylline | BDCA |\n"
            "| 5 | Palier 4 + CTC PO / Anti-IgE | BDCA |\n"
        )),
        TableauSynthese(titre="Stades GOLD de la BPCO", markdown=(
            "| Stade | Sévérité | VEMS post-BD |\n"
            "|-------|----------|-------------|\n"
            "| GOLD 1 | Léger | ≥ 80% |\n"
            "| GOLD 2 | Modéré | 50-79% |\n"
            "| GOLD 3 | Sévère | 30-49% |\n"
            "| GOLD 4 | Très sévère | < 30% |\n"
        )),
        TableauSynthese(titre="Épanchement pleural — Transsudat vs Exsudat", markdown=(
            "| Critère | Transsudat | Exsudat |\n"
            "|---------|-----------|--------|\n"
            "| Protéines | < 30 g/L | > 30 g/L |\n"
            "| LDH | Bas | Élevé |\n"
            "| Leucocytes | < 1 000/µL | > 1 000/µL |\n"
            "| Étiologies | ICG, cirrhose, SN | Cancers, infections, EP, BK |\n"
        )),
        TableauSynthese(titre="Orientation étiologique des dyspnées aiguës", markdown=(
            "| Type | Caractéristique | Étiologies principales |\n"
            "|------|----------------|----------------------|\n"
            "| Inspiratoire | Obstruction VAS, cornage | Corps étranger, œdème de Quincke, laryngite |\n"
            "| Expiratoire | Atteinte bronchique, sibilants | Asthme, BPCO, OAP |\n"
            "| Sans allongement | Polypnée | EP, pneumothorax, pneumonie |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Précision |\n"
        "|-----------|--------|----------|\n"
        "| TVO (asthme et BPCO) | VEMS/CVF < **0,7** | Rapport de Tiffeneau |\n"
        "| Réversibilité significative | > 200 mL **ET** > 12% | Après BD ou CTC |\n"
        "| Hyper-réactivité bronchique | Chute VEMS > **20%** | Test à la métacholine |\n"
        "| BDCA excessif | > **1 flacon/mois** | FDR exacerbation asthme |\n"
        "| CTC PO exacerbation asthme adulte | 0,5-1 mg/kg/j | Max 60 mg/j (7 jours) |\n"
        "| CTC PO exacerbation asthme enfant | 2 mg/kg/j | Max 40 mg/j |\n"
        "| CTC IV exacerbation sévère | 0,5-1 mg/kg/j | Max 80 mg/j |\n"
        "| SpO2 cible asthme | **93-95%** | Adulte (94-98% enfant) |\n"
        "| SpO2 cible BPCO | **88-92%** | Risque d'hypercapnie |\n"
        "| Bronchite chronique | > 3 mois/an, > 2 ans | Définition clinique |\n"
        "| DLCO pathologique | < **70%** | Destruction alvéolaire |\n"
        "| O2 longue durée | PaO2 < **60 mmHg** | Ou PaCO2 > 50 mmHg |\n"
        "| SAOS sévère | IAH ≥ **30/h** | Indication PPC formelle |\n"
        "| Toux chronique | > **8 semaines** | Définition |\n"
        "| Ponction pleurale | > **10 mm** écho | En dessous : abstention |\n"
        "| PNO iatrogène post-ponction | **3%** | Contrôle systématique |\n"
    ))

    points_cles = [
        "★ L'asthme est une maladie inflammatoire chronique avec TVO **réversible** ; la BPCO a un TVO **persistant**",
        "★ Le traitement de fond de l'asthme comporte **toujours** un CSI ; les CSI seuls sont **contre-indiqués** dans la BPCO",
        "★ Objectif SpO2 en urgence : **93-95%** (asthme) vs **88-92%** (BPCO)",
        "★ La réversibilité complète du TVO (VEMS/CVF > 0,7 + normalisation VEMS) **exclut** la BPCO",
        "★ Devant toute toux chronique : rechercher **IEC**, **rhinorrhée postérieure**, **asthme** et **RGO**",
        "★ Le sevrage tabagique est la **seule mesure** ralentissant la progression de l'obstruction dans la BPCO",
        "★ L'hémoptysie nécessite un **scanner injecté** et une **fibroscopie** ; si massive → **embolisation**",
        "★ Syndrome pleural liquidien : abolition MV + **matité** + abolition VV ; aérien : abolition MV + **tympanisme**",
        "★ Le SAOS se complique d'**HTA résistante**, troubles du rythme, AVC ; traitement de référence = **PPC**",
        "★ PNO compressif = **urgence vitale** → exsufflation immédiate sans attendre l'imagerie",
    ]

    fiche_eclair_md = (
        "**Asthme** : inflammation chronique Th2, TVO réversible, VEMS/CVF < 0,7 "
        "avec réversibilité > 200 mL et > 12%. Traitement par paliers (toujours CSI). "
        "Exacerbation modérée : BDCA + CTC PO 5-7j. Sévère : USI + ipratropium + CTC IV. "
        "Cible SpO2 93-95%.\n\n"
        "**BPCO** : TVO persistant post-BD. Tabac > 20 PA. Stades GOLD (VEMS post-BD). "
        "Sevrage tabagique = seule mesure efficace. Pas de CSI seul. "
        "Exacerbation : BDCA + O2 cible 88-92% + ATB si purulent. "
        "Stade IV : O2 longue durée, VNI.\n\n"
        "**Douleur thoracique** : 5 urgences vitales (SCA, EP, dissection, tamponnade, rupture œsophage). "
        "ECG 18 dérivations + RXT + troponine/D-dimères.\n\n"
        "**Dyspnée** : inspiratoire (VAS) vs expiratoire (bronches) vs sans allongement (EP, PNO). "
        "Échelle mMRC pour chronique. Signes de gravité : cyanose, tirage, respiration paradoxale.\n\n"
        "**Hémoptysie** : scanner injecté + fibroscopie. Cancer >> BK >> bronchectasies. "
        "Massive → embolisation.\n\n"
        "**Épanchement pleural** : matité + abolition MV/VV. "
        "Ponction systématique si > 10 mm. Transsudat (ICG, cirrhose) vs exsudat (cancer, infection).\n\n"
        "**PNO** : tympanisme + abolition MV/VV. Compressif = urgence vitale → exsufflation.\n\n"
        "**SAOS** : IAH ≥ 5/h. HTA résistante. PPC si IAH ≥ 15 ou symptômes.\n\n"
        "**Tabac** : 1re cause mortalité prématurée. Fagerström + Prochaska. TNS en 1re intention.\n\n"
        "**Toux chronique** (> 8 sem) : IEC > rhinorrhée > asthme > RGO. RXT systématique."
    )

    return FicheData(
        matiere="Pneumologie",
        nom_cours="Pneumologie",
        annee="2025-2026",
        item="Items 184, 205, 209, 202, 200, 354, 356, 108, 73, 75",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
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


_SOURCE_IMAGES: list[dict] = [
    # I. Asthme
    {"file": "source_02_p2.png", "partie": 0, "sp": 2, "desc": "Courbe débit-volume : TVO réversible", "concept": "EFR asthme", "type": "schema"},
    {"file": "source_04_p5.png", "partie": 0, "sp": 4, "desc": "Algorithme PEC exacerbation d'asthme", "concept": "Exacerbation asthme", "type": "schema"},
    {"file": "source_05_p5.png", "partie": 0, "sp": 5, "desc": "Algorithme du nourrisson siffleur", "concept": "Asthme enfant", "type": "schema"},
    # II. BPCO
    {"file": "source_07_p7.png", "partie": 1, "sp": 0, "desc": "Emphysème centrolobulaire vs panlobulaire", "concept": "Types d'emphysème", "type": "schema"},
    {"file": "source_08_p7.png", "partie": 1, "sp": 1, "desc": "BPCO : thorax en tonneau (clinique + radio)", "concept": "Distension thoracique BPCO", "type": "photo_clinique"},
    {"file": "source_11_p7.png", "partie": 1, "sp": 0, "desc": "Emphysème et obstruction bronchique : histologie", "concept": "Physiopathologie BPCO", "type": "schema"},
    {"file": "source_12_p8.png", "partie": 1, "sp": 2, "desc": "Classification GOLD et évaluation ABCD", "concept": "Stades GOLD BPCO", "type": "schema"},
    {"file": "source_16_p10.png", "partie": 1, "sp": 3, "desc": "Algorithme de traitement de la BPCO", "concept": "Traitement BPCO", "type": "schema"},
    {"file": "source_17_p11.png", "partie": 1, "sp": 4, "desc": "Antibiothérapie des exacerbations de BPCO", "concept": "ATB exacerbation BPCO", "type": "schema"},
    # III. Sémiologie et urgences
    {"file": "source_19_p13.png", "partie": 2, "sp": 0, "desc": "Algorithme d'orientation devant une douleur thoracique", "concept": "Douleur thoracique", "type": "schema"},
    {"file": "source_20_p16.png", "partie": 2, "sp": 1, "desc": "Orientation diagnostique devant une dyspnée chronique", "concept": "Dyspnée chronique", "type": "schema"},
    {"file": "source_21_p16.png", "partie": 2, "sp": 1, "desc": "Orientation diagnostique devant une dyspnée aiguë", "concept": "Dyspnée aiguë", "type": "schema"},
    {"file": "source_42_p27.png", "partie": 2, "sp": 0, "desc": "Score de Wells et Score de Genève révisé", "concept": "Probabilité clinique EP", "type": "tableau"},
    {"file": "source_45_p28.png", "partie": 2, "sp": 0, "desc": "Algorithme diagnostique de l'embolie pulmonaire", "concept": "Diagnostic EP", "type": "schema"},
    {"file": "source_50_p30.png", "partie": 2, "sp": 0, "desc": "Stratification du risque de l'EP (PESI/sPESI)", "concept": "Stratification risque EP", "type": "schema"},
    # IV. Épanchement pleural et pneumothorax
    {"file": "source_22_p17.png", "partie": 3, "sp": 0, "desc": "Radiographie : épanchement pleural gauche", "concept": "Épanchement pleural imagerie", "type": "imagerie"},
    {"file": "source_26_p21.png", "partie": 3, "sp": 1, "desc": "Radiographie et TDM de pneumothorax", "concept": "Pneumothorax imagerie", "type": "imagerie"},
    # V. Imagerie et EFR
    {"file": "source_28_p24.png", "partie": 4, "sp": 0, "desc": "Arcs pulmonaires : repères radiographiques de face", "concept": "Anatomie radiologique thorax", "type": "imagerie"},
    {"file": "source_29_p24.png", "partie": 4, "sp": 0, "desc": "Cliché thoracique de profil annoté", "concept": "Radio thorax profil", "type": "imagerie"},
    {"file": "source_33_p25.png", "partie": 4, "sp": 0, "desc": "Bronchogramme aérique : schéma", "concept": "Syndrome alvéolaire", "type": "schema"},
    {"file": "source_27_p22.png", "partie": 4, "sp": 1, "desc": "Algorithme diagnostique devant une hypoxémie (EFR)", "concept": "Hypoxémie EFR", "type": "schema"},
    # VI. Pathologies spécifiques
    {"file": "source_52_p33.png", "partie": 5, "sp": 0, "desc": "Échelle de somnolence d'Epworth", "concept": "SAOS évaluation", "type": "tableau"},
    {"file": "source_53_p34.png", "partie": 5, "sp": 0, "desc": "Algorithme diagnostique du SAOS", "concept": "Diagnostic SAOS", "type": "schema"},
    {"file": "source_54_p37.png", "partie": 5, "sp": 1, "desc": "Statut tabagique en France (2016-2017)", "concept": "Épidémiologie tabagisme", "type": "schema"},
    {"file": "source_55_p38.png", "partie": 5, "sp": 1, "desc": "Test de Fagerström simplifié (2 questions)", "concept": "Dépendance nicotinique", "type": "tableau"},
    {"file": "source_59_p41.png", "partie": 5, "sp": 2, "desc": "Orientation diagnostique de la toux chez l'enfant", "concept": "Toux enfant", "type": "tableau"},
    {"file": "source_60_p42.png", "partie": 5, "sp": 2, "desc": "Algorithme de prise en charge de la toux chronique", "concept": "Toux chronique", "type": "schema"},
    {"file": "source_62_p44.png", "partie": 5, "sp": 2, "desc": "Histoire naturelle de la tuberculose (BK)", "concept": "Tuberculose", "type": "schema"},
    {"file": "source_66_p45.png", "partie": 5, "sp": 2, "desc": "Tuberculose : radiographie et TDM thoracique", "concept": "Tuberculose imagerie", "type": "imagerie"},
]


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

    fiche = build_pneumologie_fiche()

    print("Placing source images from course PDF...")
    _place_source_images(fiche, figures_dir)
    print(f"  {len(fiche.images)} source images placed")

    docx_path = output_dir / "Pneumologie_Pneumologie_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Pneumologie_Pneumologie_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path}")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

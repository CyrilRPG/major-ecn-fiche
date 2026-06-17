"""Génère la fiche exhaustive de Neurologie à partir du PDF source."""

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


def build_fiche() -> FicheData:
    plan = [
        PlanPartie(numero="I", titre="AVC : Généralités et AIC", sous_parties=[
            PlanSousPartie(lettre="A", titre="Épidémiologie et classification"),
            PlanSousPartie(lettre="B", titre="AIC : Clinique selon le territoire"),
            PlanSousPartie(lettre="C", titre="AIC : Étiologies"),
            PlanSousPartie(lettre="D", titre="AIC : Prise en charge à la phase aiguë"),
            PlanSousPartie(lettre="E", titre="AIT et prévention secondaire"),
        ]),
        PlanPartie(numero="II", titre="Hémorragies intraparenchymateuses et TVC", sous_parties=[
            PlanSousPartie(lettre="A", titre="Hémorragies intraparenchymateuses"),
            PlanSousPartie(lettre="B", titre="Thrombophlébites cérébrales"),
        ]),
        PlanPartie(numero="III", titre="Céphalées", sous_parties=[
            PlanSousPartie(lettre="A", titre="Démarche diagnostique"),
            PlanSousPartie(lettre="B", titre="Céphalées secondaires à début brutal"),
            PlanSousPartie(lettre="C", titre="Migraine"),
            PlanSousPartie(lettre="D", titre="Céphalées de tension et CCQ"),
            PlanSousPartie(lettre="E", titre="Algies de la face"),
        ]),
        PlanPartie(numero="IV", titre="Épilepsie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et types de crises"),
            PlanSousPartie(lettre="B", titre="Syndromes épileptiques"),
            PlanSousPartie(lettre="C", titre="Bilan et prise en charge"),
            PlanSousPartie(lettre="D", titre="État de mal épileptique"),
        ]),
        PlanPartie(numero="V", titre="Pathologies neurologiques spécifiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Sclérose en plaques"),
            PlanSousPartie(lettre="B", titre="Démences"),
            PlanSousPartie(lettre="C", titre="Compression médullaire non traumatique"),
            PlanSousPartie(lettre="D", titre="Myasthénie"),
        ]),
        PlanPartie(numero="VI", titre="Sémiologie neurologique et atteintes focales", sous_parties=[
            PlanSousPartie(lettre="A", titre="Comas non traumatiques"),
            PlanSousPartie(lettre="B", titre="Paralysie faciale"),
            PlanSousPartie(lettre="C", titre="Radiculalgies et NCB"),
        ]),
    ]

    # ── PARTIE I : AVC GÉNÉRALITÉS ET AIC ──
    partie_i = Partie(numero="I", titre="AVC : Généralités et AIC", sous_parties=[
        SousPartie(lettre="A", titre="Épidémiologie et classification", rows=[
            FicheRow(concept="★ Épidémiologie", detail_md=(
                "- **150 000 AVC/an** en France\n"
                "- **1re cause** de handicap moteur acquis de l'adulte\n"
                "- **3e cause** de décès (après maladies CV et cancers)\n"
                "- **2e cause** de démence (après Alzheimer)\n"
                "- Déficit neurologique focal d'apparition **brutale**"
            )),
            FicheRow(concept="FDR", detail_md=(
                "- **Âge > 65 ans** (75% des cas)\n"
                "- **HTA** ++ (principal FDR modifiable)\n"
                "- Tabac, hypercholestérolémie, diabète\n"
                "- Alcoolisme chronique, migraine\n"
                "- Contraception orale\n"
                "- Obésité, syndrome métabolique, SAOS"
            )),
            FicheRow(concept="Classification", detail_md=(
                "| Type | Fréquence |\n"
                "|------|----------|\n"
                "| AIC + AIT | **80%** |\n"
                "| Hémorragies cérébrales non traumatiques | **20%** |\n"
                "| Thrombophlébites cérébrales | Rares |\n"
            )),
            FicheRow(concept="Pronostic", detail_md=(
                "- Récupération essentielle dans les **6 mois**, se poursuit jusqu'à 2 ans\n"
                "- Bon pronostic si : âge jeune, petit infarctus, peu sévère, entourage aidant\n"
                "- Complications : récidive (30% à 5 ans), démence vasculaire, dépression post-AVC, "
                "spasticité, épilepsie secondaire"
            )),
        ]),
        SousPartie(lettre="B", titre="AIC : Clinique selon le territoire", rows=[
            FicheRow(concept="Circulation antérieure", detail_md=(
                "| Artère | Sémiologie |\n"
                "|--------|------------|\n"
                "| **Ophtalmique** | Cécité monoculaire |\n"
                "| **Cérébrale antérieure** | Déficit moteur à prédominance **crurale**, syndrome frontal |\n"
                "| **Cérébrale moyenne superficielle** | Déficit moteur à prédominance **brachiofaciale**, aphasie ou héminégligence |\n"
                "| **Cérébrale moyenne profonde** | Hémiplégie **proportionnelle** |\n"
            )),
            FicheRow(concept="Circulation postérieure", detail_md=(
                "| Artère | Sémiologie |\n"
                "|--------|------------|\n"
                "| **Cérébrale postérieure** | HLH, hémianesthésie |\n"
                "| **Vertébrobasilaire** | Syndrome alterne (Wallenberg), syndrome cérébelleux |\n"
            )),
            FicheRow(concept="◆ Lacunes", detail_md=(
                "- Petit infarctus profond (< **15 mm**)\n"
                "- Occlusion artériole profonde par **lipohyalinose** (FDR principal : HTA)\n"
                "- Tableaux évocateurs :\n"
                "  - Hémiplégie motrice pure\n"
                "  - Hémianesthésie pure\n"
                "  - Dysarthrie + main malhabile\n"
                "  - Hémiparésie + hémi-ataxie"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Correspondance anatomo-clinique : un déficit brachiofacial = artère cérébrale moyenne superficielle, "
                "un déficit crural = artère cérébrale antérieure"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="AIC : Étiologies", rows=[
            FicheRow(concept="Athérosclérose (30%)", detail_md=(
                "- Sténose > **50%** d'une artère en amont de l'infarctus\n"
                "- Mécanismes : **thromboembolique** (+++) > thrombotique > hémodynamique\n"
                "- Présence de FDR vasculaires"
            )),
            FicheRow(concept="Dissection artérielle", detail_md=(
                "- **1re cause** d'AIC du sujet **jeune** (~20%)\n"
                "- Hématome dans la paroi artérielle : sténose/occlusion\n"
                "- Post-traumatique ou spontanée\n"
                "- Rechercher : **cervicalgies**, céphalées, **syndrome de Claude Bernard Horner** "
                "(myosis, ptosis, énophtalmie)"
            )),
            FicheRow(concept="Cardiopathie emboligène (20%)", detail_md=(
                "- **FA** = cardiopathie emboligène la plus fréquente (50% des cas)\n"
                "- Score **CHA2DS2-VASc** pour évaluer le risque embolique\n"
                "- Autres : prothèse valvulaire mécanique, RM + FA, thrombus intracavitaire, "
                "endocardite, myxome\n"
                "- Évoquer si AIC dans des **territoires artériels différents**"
            )),
            FicheRow(concept="Lacunes (20%)", detail_md=(
                "- Microangiopathie par lipohyalinose\n"
                "- FDR principal : **HTA**\n"
                "- Infarctus profond < 15 mm"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Sujet jeune + cervicalgies + Claude Bernard Horner = penser à la **dissection carotidienne**"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="AIC : Prise en charge à la phase aiguë", rows=[
            FicheRow(concept="★ Imagerie cérébrale", detail_md=(
                "- **IRM** = examen de référence :\n"
                "  - **Diffusion** : hypersignal très précoce (quelques min), ADC diminué\n"
                "  - **T2/FLAIR** : positive à partir de ~6h\n"
                "  - **T2*** (écho de gradient) : lésion hémorragique\n"
                "  - **3D-TOF** (ARM) : occlusion artérielle\n"
                "- **Scanner sans injection** si IRM non accessible :\n"
                "  - Souvent normal dans les premières heures\n"
                "  - Signes précoces : artère sylvienne hyperdense, effacement des sillons, "
                "dédifférenciation SB/SG"
            )),
            FicheRow(concept="Mise en condition", detail_md=(
                "- Alitement avec redressement tête à **30%**\n"
                "- Prévention attitudes vicieuses, mise au fauteuil après 48h\n"
                "- VVP, libération VAS\n"
                "- **Kinésithérapie motrice précoce**\n"
                "- Bas de contention dès l'entrée"
            )),
            FicheRow(concept="Lutte ACSOS", detail_md=(
                "- Hyperthermie : paracétamol si T > **37,5 C**\n"
                "- Hypoxémie : O2 si SaO2 < **95%**\n"
                "- Hyperglycémie : insuline si glycémie > **1,8 g/L**\n"
                "- Hypoglycémie : G30% si glycémie < **0,5 g/L**\n"
                "- Troubles de la déglutition +++\n"
                "- Hyponatrémie, oedème cérébral (+/- mannitol 20%)"
            )),
            FicheRow(concept="Pression artérielle", detail_md=(
                "- **Respect** de la poussée tensionnelle (maintien débit sanguin cérébral)\n"
                "- Nicardipine IVSE si :\n"
                "  - AIC sans thrombolyse : PA > **220/120** mmHg\n"
                "  - AIC avec thrombolyse : PA > **185/110** mmHg"
            )),
            FicheRow(concept="★ Thrombolyse et thrombectomie", detail_md=(
                "| Délai | Traitement | Objectif TA |\n"
                "|-------|-----------|-------------|\n"
                "| < **4h30** | TIV +/- thrombectomie | 185/110 mmHg |\n"
                "| 4h30-6h | Thrombectomie seule | 185/110 mmHg |\n"
                "| > 6h | Ni TIV ni thrombectomie | 220/120 mmHg |\n\n"
                "- Thrombectomie extensible jusqu'à **24h** si mismatch clinico-radiologique\n"
                "- Aspirine 300 mg + HBPM préventif : immédiat si pas de thrombolyse IV, "
                "à **24h** après TIV (scanner de controle avant)"
            )),
            FicheRow(concept="", detail_md=(
                "- L'**IRM de diffusion** est l'examen le plus sensible pour le diagnostic précoce d'AIC\n"
                "- Les 4 séquences IRM d'urgence : diffusion, FLAIR, T2*, 3D-TOF"
            ), kind="a_retenir"),
            FicheRow(concept="Bilan étiologique", detail_md=(
                "- Biologie : bilan standard + **LDLc**, **HbA1c**\n"
                "- **EDTSA** systématique +/- angioscanner/angio-IRM\n"
                "- Cardiologie : **ECG** + **ETT** + **holter ECG** (minimum)\n"
                "- Selon contexte : scope ECG, ETO (sujet jeune ++), reveal implantable"
            )),
        ]),
        SousPartie(lettre="E", titre="AIT et prévention secondaire", rows=[
            FicheRow(concept="Définition AIT", detail_md=(
                "- Épisode bref (< **1 heure**) de déficit neurologique\n"
                "- Dû à une ischémie focale cérébrale ou rétinienne\n"
                "- **Sans lésion** cérébrale identifiable en imagerie"
            )),
            FicheRow(concept="AIT probable", detail_md=(
                "- Installation rapide (< 2 min) d'un ou plusieurs :\n"
                "  - Cécité monoculaire\n"
                "  - Aphasie\n"
                "  - Troubles moteurs/sensitifs unilatéraux (face/membres)\n"
                "  - HLH"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Ne sont **PAS** évocateurs d'AIT : perte de connaissance, confusion, "
                "amnésie aiguë, faiblesse généralisée transitoire"
            ), kind="piege"),
            FicheRow(concept="◆ Score ABCD2", detail_md=(
                "- AIT = **syndrome de menace cérébrale** (30% des AIC précédés d'AIT)\n"
                "- Risque maximal dans les **premiers jours**\n"
                "- Score ABCD2 : Age, Blood pressure, Clinique, Durée, Diabète\n"
                "- Plus le score est élevé, plus le risque de récidive est important"
            )),
            FicheRow(concept="Prévention secondaire", detail_md=(
                "- **FDR CV** : sevrage tabac, TA < **140/90**, LDLc < **0,7 g/L**, diabète selon HbA1c\n"
                "- **Sténose carotidienne** : endartériectomie dans les **15 jours** si > 70%\n"
                "- **Dissection** : aspirine ou AVK pendant 3-6 mois\n"
                "- **Cardiopathie emboligène** : anticoagulation\n"
                "- **Sans cause** : antiagrégant plaquettaire au long cours"
            )),
        ]),
    ])

    # ── PARTIE II : HÉMORRAGIES ET TVC ──
    partie_ii = Partie(numero="II", titre="Hémorragies intraparenchymateuses et TVC", sous_parties=[
        SousPartie(lettre="A", titre="Hémorragies intraparenchymateuses", rows=[
            FicheRow(concept="Clinique", detail_md=(
                "- Installation **brutale**, céphalées associées +++ (+/- nausées/vomissements)\n"
                "- Signes déficitaires focaux ne répondant **pas** à une systématisation artérielle\n"
                "- Troubles de vigilance fréquents\n"
                "- Signes de gravité = **HTIC** : céphalées, nausées, vomissements, troubles de conscience "
                "=> risque d'engagement cérébral"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "| Cause | Fréquence | Terrain/caractéristiques |\n"
                "|-------|-----------|-------------------------|\n"
                "| **HTA chronique** | **50%** | > 50 ans, hématome profond (capsulo-thalamique) |\n"
                "| Malformation vasculaire | 5-10% | Sujet jeune, lobaire, HSA associée |\n"
                "| Troubles hémostase | 10% | Congénitaux ou acquis |\n"
                "| Tumeurs cérébrales | 5-10% | Tumeurs malignes, IRM controle à 3 mois |\n"
                "| **Angiopathie amyloide** | 5% | Sujet âgé, lobaire, microbleeds, récidives |\n"
                "| Inconnue | 20% | |\n"
            )),
            FicheRow(concept="Imagerie", detail_md=(
                "- **Scanner sans injection** en urgence : **hyperdensité spontanée** arrondie\n"
                "- Recherche signes de gravité : effet de masse, hydrocéphalie\n"
                "- **IRM** : hyposignal en séquence **T2***\n"
                "- IRM de controle à **3 mois** pour rechercher étiologie"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- Hospitalisation urgente en **UNV**\n"
                "- **Arrêt** antiagrégants/anticoagulants\n"
                "- **Réversion** des anticoagulants (vitamine K si AVK, PPSB/Praxbind selon NACO)\n"
                "- Controle TA strict < **140/90** mmHg (Nicardipine IVSE)\n"
                "- Mise en condition : alitement 30, VVP, VAS, lutte ACSOS\n"
                "- HBPM préventive à J2 si hémorragie stable au scanner\n"
                "- Chirurgie rare : sujet jeune avec HTIC, localisation cérébelleuse + hydrocéphalie"
            )),
            FicheRow(concept="", detail_md=(
                "- Scanner sans injection : **hyperdensité** = hémorragie, **hypodensité** = ischémie\n"
                "- L'objectif tensionnel est différent de l'AIC : < 140/90 mmHg d'emblée pour les hémorragies"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Thrombophlébites cérébrales", rows=[
            FicheRow(concept="Clinique", detail_md=(
                "- **Céphalées** (HTIC) : isolées dans 25% des cas, +/- oedème papillaire\n"
                "- **Crises épileptiques** : partielles ou généralisées, "
                "hémicorporelles à bascule (évocateur)\n"
                "- **Déficits neurologiques focaux** variables selon localisation\n"
                "- Troubles de conscience possibles"
            )),
            FicheRow(concept="◆ Étiologies", detail_md=(
                "| Causes générales | Causes locales |\n"
                "|-----------------|----------------|\n"
                "| Post-partum +++ | Otite, mastoïdite, sinusite |\n"
                "| **Contraception orale** | Infection intracrânienne |\n"
                "| Thrombophilie (PC, PS, AT III) | Traumatisme crânien |\n"
                "| Affections hématologiques | Neurochirurgie |\n"
                "| Cancers, Behcet | Hypotension intracrânienne |\n"
            )),
            FicheRow(concept="Diagnostic", detail_md=(
                "- **IRM avec ARM veineuse** = référence\n"
                "- Absence de flux dans le sinus occlus\n"
                "- **Signe du delta** après injection de gadolinium\n"
                "- Scanner : hyperdensité spontanée du thrombus"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Anticoagulation curative** immédiate par héparine IVSE, "
                "**même si** infarctus hémorragique\n"
                "- Relais **AVK** minimum 6 mois\n"
                "- Traitement étiologique (arrêt contraception, éradication foyer infectieux)\n"
                "- Traitement symptomatique : antiépileptique si crises, mannitol si HTIC"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ L'anticoagulation est indiquée même en cas de remaniement hémorragique "
                "(contrairement aux hémorragies intraparenchymateuses)"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE III : CÉPHALÉES ──
    partie_iii = Partie(numero="III", titre="Céphalées", sous_parties=[
        SousPartie(lettre="A", titre="Démarche diagnostique", rows=[
            FicheRow(concept="Interrogatoire", detail_md=(
                "- Mode d'installation : **soudain** vs progressif\n"
                "- Durée : aiguë (heures/jours) vs chronique (mois/années)\n"
                "- Céphalée nouvelle ou habituelle ?\n"
                "- Évolution depuis installation : aggravation, stabilité, amélioration\n"
                "- Signes d'urgence : syndrome méningé, signes d'**HTIC**"
            )),
            FicheRow(concept="Examen clinique", detail_md=(
                "- Général : TA, T, auscultation cardiaque, examen cutané (purpura)\n"
                "- Neurologique : raideur méningée, signes de focalisation, pupilles, "
                "AV, champ visuel, FO\n"
                "- Locorégional : palpation artères temporales (> 50 ans), auscultation cervicale, "
                "examen sinus"
            )),
            FicheRow(concept="", detail_md=(
                "- Toute céphalée **récente et inhabituelle** doit être explorée\n"
                "- Un scanner normal n'élimine pas : 5-10% des HSA, 30% des TVC, "
                "les dissections cervicales, les méningites"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Examens complémentaires", detail_md=(
                "- **Scanner** sans injection en 1re intention\n"
                "- **IRM** = examen de choix\n"
                "- **PL** : 1re intention si syndrome méningé fébrile ; après scanner normal si "
                "céphalée brutale (HSA, méningite, HTIC)\n"
                "- Biologie : syndrome inflammatoire (Horton)\n"
                "- Examen ophtalmo : oedème papillaire"
            )),
        ]),
        SousPartie(lettre="B", titre="Céphalées secondaires à début brutal", rows=[
            FicheRow(concept="HSA", detail_md=(
                "- Céphalée d'apparition **explosive**, en **coup de tonnerre**\n"
                "- Scanner cérébral en urgence\n"
                "- Si scanner normal : **PL systématique** (LCS hémorragique)"
            )),
            FicheRow(concept="Syndrome de vasoconstriction cérébrale", detail_md=(
                "- Céphalée en coup de tonnerre, +/- déficits focaux, crises épileptiques\n"
                "- Salves durant 1-3 semaines\n"
                "- Contexte : **post-partum**, rapport sexuel, vasoconstricteurs\n"
                "- Angio-IRM : rétrécissements artériels diffus, **réversibles** en 1-3 mois"
            )),
            FicheRow(concept="Hypotension du LCS", detail_md=(
                "- Post-PL ++ (brèche durale)\n"
                "- Céphalées à l'**orthostatisme**, disparaissant en position allongée\n"
                "- IRM : rehaussement méningé après injection, déplacement cranio-caudal\n"
                "- Traitement : **blood-patch** (injection péridurale de sang autologue)"
            )),
            FicheRow(concept="HTIC", detail_md=(
                "- HTIC **bénigne** : jeune femme obèse, corticoides, vitamine A ; "
                "PL pression > **20 cm** d'eau ; traitement par ponction évacuatrice\n"
                "- HTIC secondaire : TVC, processus expansif intracrânien"
            )),
        ]),
        SousPartie(lettre="C", titre="Migraine", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Céphalée primaire la plus fréquente (**10-15%** population)\n"
                "- Terrain : **F > H**, début avant 40 ans (souvent puberté)\n"
                "- Physiopathologie : hyperexcitabilité neuronale"
            )),
            FicheRow(concept="Critères IHS migraine sans aura", detail_md=(
                "- A. Au moins **5 crises** répondant aux critères B-D\n"
                "- B. Durée **4-72 heures** (sans traitement)\n"
                "- C. Au moins 2 parmi : unilatérale, pulsatile, modérée/sévère, "
                "aggravation par effort physique\n"
                "- D. Au moins 1 parmi : nausées/vomissements, phono ET photophobie\n"
                "- E. Non attribuable à autre affection"
            )),
            FicheRow(concept="Critères IHS migraine avec aura", detail_md=(
                "- Au moins **2 crises** avec aura\n"
                "- Aura : signes neurologiques focaux **réversibles**\n"
                "- Installation **progressive** > 5 min (marche migraineuse)\n"
                "- Chaque symptome dure **5-60 min**\n"
                "- Céphalée dans les **60 min** suivant l'aura\n"
                "- Types : visuelle +++ (scotome scintillant), sensitive (chéiro-orale), "
                "langage (rare), motrice (migraine hémiplégique)"
            )),
            FicheRow(concept="Traitement de crise", detail_md=(
                "- Prise la plus **précoce** possible\n"
                "- Crise modérée : **aspirine** +/- métoclopramide ou **AINS** (ibuprofène, kétoprofène)\n"
                "- Crise sévère ou échec AINS à 2h : **triptans** (agonistes 5-HT1B/1D)\n"
                "  - Max 2/jour, max **8 prises/mois**\n"
                "- Triptans : attendre le début de la céphalée (pas pendant l'aura)"
            )),
            FicheRow(concept="Traitement de fond", detail_md=(
                "- Indication : crises fréquentes > **2-3/mois** depuis > 3 mois\n"
                "- 1re intention : **propranolol** ou **métoprolol**\n"
                "- Évaluation efficacité : > 2-3 mois à dose efficace\n"
                "- **Agenda des crises** obligatoire\n"
                "- Arrêt progressif jamais brutal"
            )),
            FicheRow(concept="◆ Cas particuliers", detail_md=(
                "- **État de mal migraineux** : crise > **72h**, sumatriptan SC, "
                "puis hospitalisation + AINS IV\n"
                "- **Migraine cataméniale** : oestradiol percutané 8 jours\n"
                "- **Contraception oestro-progestative CI si migraine avec aura**\n"
                "- Grossesse : paracétamol (AINS CI), triptans au cas par cas"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La migraine avec aura **contre-indique** la contraception oestro-progestative "
                "(risque d'AVC ischémique)\n"
                "- ⚠ Ne pas dépasser 8 prises de triptans/mois (risque de CCQ)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Céphalées de tension et CCQ", rows=[
            FicheRow(concept="Céphalée de tension", detail_md=(
                "- Prévalence **30-80%** (plus fréquente que la migraine)\n"
                "- Bilatérale (barre frontale ou postérieure), type serrement/étau\n"
                "- Intensité légère à modérée\n"
                "- **Pas** de signes digestifs, pas de photophobie/phonophobie significative\n"
                "- Non aggravée par le mouvement\n"
                "- Traitement épisodique : paracétamol/aspirine/AINS (max 8-10 j/mois)\n"
                "- Traitement de fond : **amitriptyline**"
            )),
            FicheRow(concept="CCQ", detail_md=(
                "- Céphalées > **15 j/mois** depuis > **3 mois**\n"
                "- Fréquemment associées à un **abus médicamenteux**\n"
                "- Comorbidité psychiatrique élevée (anxiété, dépression)\n"
                "- Traitement : **sevrage total** en traitement de crise + "
                "amitriptyline ou topiramate\n"
                "- Prévention : traitement de fond chez les migraineux avec crises fréquentes"
            )),
        ]),
        SousPartie(lettre="E", titre="Algies de la face", rows=[
            FicheRow(concept="Algie vasculaire de la face", detail_md=(
                "- Terrain : **homme 20-40 ans** (1/1000)\n"
                "- Crises quotidiennes (2-3/j) durant 2-8 semaines, 1-2x/an\n"
                "- Douleur intense type déchirure, périorbitaire, unilatérale\n"
                "- Signes autonomiques homolatéraux : larmoiement, rhinorrhée, injection conjonctivale\n"
                "- **IRM cérébrale systématique**"
            )),
            FicheRow(concept="Traitement AVF", detail_md=(
                "- Éradication alcool\n"
                "- Crise : **sumatriptan SC** + **O2** 6-15 L/min pendant 15 min\n"
                "- Fond : **vérapamil** en 1re intention"
            )),
            FicheRow(concept="Névralgie essentielle du trijumeau", detail_md=(
                "- Terrain : **femme > 50 ans**\n"
                "- Compression racine du V par artère issue de l'artère basilaire\n"
                "- Douleur toujours **unilatérale** : V2 (40%), V3 (20%), V1 (10%), "
                "parfois 2 branches mais **jamais les 3**\n"
                "- Décharges électriques fulgurantes, brèves, en salves\n"
                "- **Zone gâchette** : déclenchement par mastication, effleurement cutané\n"
                "- Examen clinique **normal** (pas d'hypoesthésie, réflexe cornéen normal)"
            )),
            FicheRow(concept="Traitement névralgie V", detail_md=(
                "- 1re intention : **carbamazépine** (dose minimale efficace)\n"
                "- EI : somnolence, vertiges, syndrome vestibulo-cochléaire\n"
                "- 2e intention : oxcarbazépine, baclofène, gabapentine\n"
                "- Chirurgie si formes rebelles : thermocoagulation du ganglion de Gasser"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Une névralgie du V avec anomalie à l'examen clinique (hypoesthésie, "
                "fond douloureux permanent) est une névralgie **symptomatique** : faire IRM"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE IV : ÉPILEPSIE ──
    partie_iv = Partie(numero="IV", titre="Épilepsie", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et types de crises", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Crise épileptique : manifestations cliniques **brutales**, imprévisibles, "
                "transitoires dues à l'hyperactivité paroxystique d'un réseau neuronal\n"
                "- Prévalence : **0,5%** ; incidence cumulative à 80 ans : 3,1%\n"
                "- Prédominance : enfants (50% avant 10 ans) et > 60 ans"
            )),
            FicheRow(concept="CGTC", detail_md=(
                "- **Phase tonique** (10-20 s) : cri, abolition conscience, chute, "
                "contractions en flexion puis extension, apnée, cyanose, "
                "morsure **latérale** de langue\n"
                "- **Phase clonique** (20-30 s) : secousses rythmiques bilatérales, "
                "s'espaçant progressivement\n"
                "- **Phase résolutive** : coma hypotonique, respiration ample (stertor), "
                "confusion +/- énurésie, amnésie de la crise"
            )),
            FicheRow(concept="Myoclonies bilatérales", detail_md=(
                "- Secousses en éclair, lâchage/projection d'objet\n"
                "- Souvent au **réveil**, provoquées par stimulations lumineuses\n"
                "- Seules crises généralisées **sans** trouble de conscience"
            )),
            FicheRow(concept="Absences", detail_md=(
                "- Rupture de contact avec fixité du regard, quelques secondes\n"
                "- **Typiques** : début/fin brusques, EEG pointes-ondes à **3 Hz**\n"
                "- **Atypiques** : début/fin plus progressifs, pointes-ondes < 3 Hz"
            )),
            FicheRow(concept="Crises partielles (focales)", detail_md=(
                "- **Simples** (pas d'altération de conscience) :\n"
                "  - Motrices : marche bravais-jacksonienne (extension selon somatotopie)\n"
                "  - Sensitives, sensorielles, végétatives, psychiques\n"
                "- **Complexes** (rupture de contact/amnésie) :\n"
                "  - Arrêt moteur, yeux hagards\n"
                "  - Automatismes oro-alimentaires, gestuels\n"
                "- Généralisation secondaire possible"
            )),
            FicheRow(concept="", detail_md=(
                "- La **morsure latérale de la langue** est très évocatrice de CGTC\n"
                "- DD des crises partielles : AIT, migraine avec aura, crise d'angoisse, syncope"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Syndromes épileptiques", rows=[
            FicheRow(concept="Épilepsie-absence de l'enfant", detail_md=(
                "- Terrain : autour de **7 ans**, filles\n"
                "- Absences typiques (> 100/j) avec hyperpnée\n"
                "- CGTC associées dans 50% des cas\n"
                "- Bon pronostic sauf si début tardif > 8 ans ou photosensibilité"
            )),
            FicheRow(concept="Épilepsie myoclonique juvénile", detail_md=(
                "- Âge : **12-18 ans**, génétiquement déterminée\n"
                "- Myoclonies bilatérales prédominant aux MS, au **réveil**\n"
                "- Pas de rupture de contact\n"
                "- Favorisée par alcool\n"
                "- **Récidive dans 90%** à l'arrêt du traitement"
            )),
            FicheRow(concept="Syndrome de West", detail_md=(
                "- Terrain : **2-12 mois**, garcons\n"
                "- Triade : **spasmes infantiles** en flexion + stagnation/régression "
                "psychomotrice + EEG **hypsarythmie** (pathognomonique)\n"
                "- Pronostic favorable si idiopathique et traitement précoce"
            )),
            FicheRow(concept="Syndrome de Lennox-Gastaut", detail_md=(
                "- Âge : **3-5 ans**\n"
                "- Crises toniques nocturnes, atoniques, absences atypiques\n"
                "- Retard intellectuel, troubles caractériels\n"
                "- Pronostic **sévère**"
            )),
            FicheRow(concept="◆ Épilepsie du lobe temporal", detail_md=(
                "- ATCD de convulsions fébriles compliquées\n"
                "- Crise typique : gêne épigastrique ascendante, arrêt psychomoteur, "
                "fixité du regard, mâchonnement, dystonie controlatérale"
            )),
            FicheRow(concept="Épilepsie secondaire", detail_md=(
                "- Causes tumorales, vasculaires (AVC), traumatiques, infectieuses\n"
                "- **Alcool** : ivresse convulsivante, sevrage, épilepsie alcoolique\n"
                "- Médicaments/toxiques : psychotropes, intoxication CO\n"
                "- Métaboliques : **hypoglycémie** ++, hypocalcémie, hyponatrémie"
            )),
        ]),
        SousPartie(lettre="C", titre="Bilan et prise en charge", rows=[
            FicheRow(concept="Bilan de 1re crise", detail_md=(
                "- Examen clinique +++ (souvent normal à distance)\n"
                "- Biologie : NFS, ionogramme, urée, créatinine, glycémie, "
                "alcoolémie, calcémie, BHC\n"
                "- **Scanner** sans et avec injection : **systématique** devant toute 1re crise\n"
                "- **IRM** si scanner normal\n"
                "- **EEG** post-critique : anomalies paroxystiques (peut être normal)"
            )),
            FicheRow(concept="Traitement de fond", detail_md=(
                "- Indication : crises récidivantes OU 1re crise avec facteur prédisposant\n"
                "- Épilepsie généralisée idiopathique : **valproate**, lamotrigine, lévétiracétam\n"
                "- Épilepsie partielle : **lévétiracétam**, lamotrigine, oxcarbazépine\n"
                "- **Monothérapie** initiale, dose minimale efficace\n"
                "- **Jamais d'arrêt brutal** ; arrêt progressif si > 2-3 ans sans crise + EEG normal"
            )),
            FicheRow(concept="Mesures associées", detail_md=(
                "- **Conduite** : déclaration à la préfecture, CI sauf commission médicale "
                "si stabilisation > **1 an** (10 ans pour poids lourds)\n"
                "- CI sports dangereux (plongée, hauteur)\n"
                "- Certaines professions interdites\n"
                "- **Contraception** : attention inducteurs enzymatiques des anti-épileptiques\n"
                "- **Grossesse** : **lamotrigine** ++ ; acide folique **5 mg/j** en pré-conceptionnel "
                "pendant toute la grossesse"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Les anti-épileptiques sont des **inducteurs enzymatiques** pouvant réduire "
                "l'efficacité de la contraception\n"
                "- Le **valproate** est tératogène : à éviter chez la femme en âge de procréer"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="État de mal épileptique", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- EME convulsif : 2 CGTC sans retour à la conscience OU "
                "1 CGTC > **5 minutes**\n"
                "- EME non convulsif : confusion mentale variable, "
                "persistant des heures/jours\n"
                "- Urgence diagnostique et thérapeutique"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- **Hospitalisation en réanimation**\n"
                "- VAS, O2 10 L/min, scope, 2 VVP\n"
                "- Rechercher et traiter **hypoglycémie**\n"
                "- **1re ligne** : diazépam 10 mg en 3 min OU clonazépam 1 mg en 3 min\n"
                "  - Si échec : répéter à 5 min\n"
                "- **2e ligne** (si échec 2e BZD) : fosphénytoïne 20 mg/kg IVSE "
                "OU lévétiracétam 30-60 mg/kg OU valproate 40 mg/kg\n"
                "- **3e ligne** (échec à 30 min) : **sédation** (propofol, midazolam, thiopental) "
                "avec IOT"
            )),
        ]),
    ])

    # ── PARTIE V : PATHOLOGIES NEUROLOGIQUES SPÉCIFIQUES ──
    partie_v = Partie(numero="V", titre="Pathologies neurologiques spécifiques", sous_parties=[
        SousPartie(lettre="A", titre="Sclérose en plaques", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Maladie inflammatoire chronique du **SNC**\n"
                "- Plaques de **démyélinisation** focales dans la substance blanche\n"
                "- Adulte jeune **20-40 ans**, prédominance féminine (70%)\n"
                "- Gradient Nord > Sud, étiologie multifactorielle"
            )),
            FicheRow(concept="Symptômes", detail_md=(
                "- **NORB** révélatrice dans **25%** : BAV unilatérale, scotome, "
                "douleur à la mobilisation, dyschromatopsie rouge/vert\n"
                "- Signes moteurs pyramidaux : paraparésie, troubles de la marche\n"
                "- Troubles sensitifs (20%) : paresthésies, signe de **Lhermitte**\n"
                "- Atteinte du TC, troubles sphinctériens, fatigue, troubles cognitifs"
            )),
            FicheRow(concept="Modes évolutifs", detail_md=(
                "- **Poussée** : nouveau symptôme > 24h (2 poussées séparées de > 1 mois)\n"
                "- **Progression** : aggravation continue > 1 an\n"
                "- **Rémittente récurrente** (85%) : par poussées\n"
                "- **Secondairement progressive** (40-50%)\n"
                "- **Progressive primaire** (15%)"
            )),
            FicheRow(concept="Diagnostic : critères de McDonald", detail_md=(
                "- **Dissémination spatiale** : atteinte de plusieurs zones du SNC\n"
                "- **Dissémination temporelle** : succession d'épisodes dans le temps\n"
                "- **IRM** : hypersignaux T2/FLAIR focaux de la substance blanche\n"
                "  - 4 localisations : périventriculaire ++, juxtacorticale, cérébelleuse, médullaire\n"
                "  - Prise de gadolinium si lésion < 3 mois\n"
                "- **LCS** : bandes oligoclonales (BOC) en immunofixation"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Poussée** : corticoides fortes doses **1 g/j** IV pendant 3 jours\n"
                "- **Fond** (1re intention) : IFN-bêta, acétate de glatiramère, "
                "tériflunomide, diméthyl fumarate\n"
                "- 2e intention (formes sévères) : mitoxantrone, natalizumab, fingolimod\n"
                "- **Symptomatique** : spasticité (baclofène), troubles urinaires "
                "(anticholinergiques), douleurs"
            )),
            FicheRow(concept="", detail_md=(
                "- Aucun traitement de fond n'a prouvé son efficacité dans les formes "
                "**primitivement progressives**\n"
                "- La corticothérapie accélère la récupération de la poussée mais ne "
                "prévient pas les nouvelles poussées"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Démences", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Altération **durable** d'une ou plusieurs fonctions cognitives "
                "et/ou comportementales\n"
                "- Suffisamment sévère pour altérer l'**autonomie**\n"
                "- Évolution **chronique**, hors période confusionnelle"
            )),
            FicheRow(concept="★ Maladie d'Alzheimer", detail_md=(
                "- **1re cause** de démence, 1 million de personnes en France\n"
                "- Âge moyen : 65 ans, sporadique avec prédisposition génétique\n"
                "- 3 anomalies : plaques **amyloides**, dégénérescences neurofibrillaires "
                "(**protéine TAU** hyperphosphorylée), perte neuronale\n"
                "- Phase prodromale : plainte mnésique, oubli à mesure, "
                "**non amélioré par indicage**, anosognosie\n"
                "- Phase d'état : syndrome aphaso-apraxo-agnosique, altération autonomie\n"
                "- Diagnostic : clinique + IRM (**atrophie hippocampique**) + biologie\n"
                "- Formes atypiques : LCS (TAU phosphorylée, bêta-amyloides 42)"
            )),
            FicheRow(concept="◆ Démence à corps de Lewy", detail_md=(
                "- Installation rapide (~1 an)\n"
                "- **Hallucinations visuelles** précoces\n"
                "- Troubles cognitifs **fluctuants** (fonctions exécutives)\n"
                "- **Syndrome parkinsonien**\n"
                "- Fluctuations de vigilance\n"
                "- ⚠ **Neuroleptiques CI**"
            )),
            FicheRow(concept="◆ DLFT (maladie de Pick)", detail_md=(
                "- Sujet < 65 ans, 25% familiales (AD)\n"
                "- Démence par **troubles comportementaux** (contrairement à Alzheimer)\n"
                "- Syndrome frontal : apathie OU désinhibition, troubles du langage, "
                "anosognosie\n"
                "- IRM : atrophie cortex frontal (cornes ventriculaires frontales ballonisées)"
            )),
            FicheRow(concept="Démence vasculaire", detail_md=(
                "- **2e cause** de démence du sujet âgé\n"
                "- Succession de micro-infarctus (lacunes)\n"
                "- Évolution en **marche d'escalier**\n"
                "- IRM : leucopathie, micro-saignements, lacunes"
            )),
            FicheRow(concept="Démences secondaires curables", detail_md=(
                "- **Hypothyroïdie**, carence B12/folates\n"
                "- Hydrocéphalie à pression normale\n"
                "- Hématome sous-dural chronique\n"
                "- Intoxications médicamenteuses chroniques (BZD, anticholinergiques)\n"
                "- Neurosyphilis, maladies à prions"
            )),
        ]),
        SousPartie(lettre="C", titre="Compression médullaire non traumatique", rows=[
            FicheRow(concept="Triade clinique", detail_md=(
                "- **Syndrome lésionnel** (niveau de la compression) :\n"
                "  - Douleurs radiculaires (topographie constante, impulsives à la toux, nocturnes)\n"
                "  - Hypoesthésie en bandes, déficit moteur avec abolition/inversion du réflexe\n"
                "- **Syndrome sous-lésionnel** :\n"
                "  - Syndrome pyramidal : claudication médullaire (indolore), paraplégie spastique\n"
                "  - Troubles sensitifs avec **niveau sensitif net**\n"
                "  - Troubles sphinctériens (tardifs)\n"
                "- **Syndrome rachidien** (inconstant) : douleurs rachidiennes, raideur"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- **IRM médullaire en urgence** systématique (T1, T2, gadolinium)\n"
                "- Myéloscanner si CI formelle à l'IRM\n"
                "- EPP (myélome), bilan infectieux si spondylodiscite"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "| Localisation | Causes principales |\n"
                "|-------------|--------------------|\n"
                "| **Extradurale** | Métastases vertébrales (> 60 ans), myélopathie cervicarthrosique, hernie discale, spondylodiscite |\n"
                "| **Intradurale extramédullaire** | Méningiomes (femme > 50 ans, thoracique), neurinomes (aspect en sablier) |\n"
                "| **Intramédullaire** | Épendymomes, astrocytomes, syringomyélie |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- La compression médullaire est une **urgence** diagnostique et thérapeutique\n"
                "- Métastases : poumon, prostate, rein, sein, thyroide (les plus fréquentes)\n"
                "- Disque intervertébral **toujours respecté** dans les métastases (vs spondylodiscite)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Myasthénie", rows=[
            FicheRow(concept="Clinique", detail_md=(
                "- Déficit moteur variable dans le temps = **fatigabilité** (phénomène myasthénique)\n"
                "- Apparait ou augmente à l'**effort**, augmente en **fin de journée**, "
                "se corrige au **repos**\n"
                "- Muscles oculaires : **ptosis** unilatéral puis bilatéral, **diplopie**\n"
                "- Muscles bulbaires : troubles déglutition, voix nasonnée, mastication\n"
                "- Muscles des membres : atteinte proximale (ceinture scapulaire)\n"
                "- **Gravité** : atteinte muscles respiratoires (décompensation ventilatoire)"
            )),
            FicheRow(concept="Diagnostic paraclinique", detail_md=(
                "- **Ac anti-RAch** (pas de corrélation taux/gravité) ou **Ac anti-MuSK**\n"
                "- **ENMG** : décrément > **10%** en stimulodétection répétitive\n"
                "- **Test aux anticholinestérasiques** (edrophonium IV) : régression du ptosis\n"
                "- Scanner/IRM thoracique : recherche de **thymome**"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Symptomatique** : anticholinestérasiques (pyridostigmine, ambénonium)\n"
                "  - Posologie progressive, durée d'action brève\n"
                "  - ⚠ Surdosage = **crise cholinergique** (hypersécrétion, fasciculations)\n"
                "- **Fond** : corticothérapie (aggravation transitoire 1re semaine), "
                "immunosuppresseur (**azathioprine**), thymectomie\n"
                "- **Poussées** : **IgIV** (1 g/kg sur 5 jours) ou échanges plasmatiques\n"
                "- **Carte de myasthénie** + liste des médicaments contre-indiqués"
            )),
            FicheRow(concept="", detail_md=(
                "- CI absolues : aminosides, bêtabloquants (même locaux), curarisants, "
                "D-pénicillamine, quinine\n"
                "- CI relatives : BZD, carbamazépine, neuroleptiques, vérapamil"
            ), kind="piege"),
            FicheRow(concept="◆ Lambert-Eaton", detail_md=(
                "- Déficit moteur des MI + fatigabilité, ROT faibles/absents\n"
                "- Dysautonomie cholinergique\n"
                "- ENMG : amplitude diminuée avec **incrément > 100%** après stimulation\n"
                "- Ac anti-canaux calcium présynaptiques\n"
                "- Souvent **paranéoplasique** ; traitement : 3,4-diaminopyridine"
            )),
        ]),
    ])

    # ── PARTIE VI : SÉMIOLOGIE ET ATTEINTES FOCALES ──
    partie_vi = Partie(numero="VI", titre="Sémiologie neurologique et atteintes focales", sous_parties=[
        SousPartie(lettre="A", titre="Comas non traumatiques", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Défaillance de la **FRAA** (formation réticulée activatrice ascendante)\n"
                "- Urgence diagnostique et thérapeutique\n"
                "- Souffrance cérébrale diffuse (toxique, métabolique, infectieuse, épileptique) "
                "ou lésion focale"
            )),
            FicheRow(concept="Examen neurologique", detail_md=(
                "- **Pupilles** :\n"
                "  - Mydriase aréactive unilatérale : **engagement temporal**\n"
                "  - Myosis réactif : coma métabolique/toxique\n"
                "  - Mydriase bilatérale aréactive : anoxie, hypothermie, souffrance mésencéphalique\n"
                "- **Déviation oculaire** : ipsilatérale (lésion hémisphérique), "
                "controlatérale (lésion protubérantielle)\n"
                "- **Réponse motrice** : décortication (flexion MS) = souffrance hémisphérique ; "
                "décérébration (extension MS) = souffrance TC"
            )),
            FicheRow(concept="Score de Glasgow", detail_md=(
                "| Composante | Score |\n"
                "|-----------|-------|\n"
                "| Ouverture yeux | 1-4 (4 = spontanée) |\n"
                "| Réponse verbale | 1-5 (5 = orientée) |\n"
                "| Réponse motrice | 1-6 (6 = obéit aux ordres) |\n"
                "| **Total** | **3-15** (coma si < 8) |\n"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **Toxique** ++ : iatrogène, CO (hypertonie, convulsions), "
                "alcool, opiacés (myosis serré bilatéral)\n"
                "- **Métabolique** : hypoglycémie (sueurs, convulsions), troubles ioniques, "
                "anoxie, encéphalopathies (hépatique, Gayet-Wernicke)\n"
                "- **Vasculaire** : hémorragie méningée/intraparenchymateuse, AVC\n"
                "- **Infectieux** : méningoencéphalite, abcès cérébral\n"
                "- **Comitial** : état de mal, coma post-critique"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- Maintien ventilation (intubation si nécessaire), circulation\n"
                "- **Glucose systématique** si coma inexpliqué "
                "(+ vitamine B1 si éthylique/dénutri)\n"
                "- Traitement étiologique dès que suspecté (ATB si purpura fulminans)\n"
                "- Scanner cérébral si pas de cause évidente\n"
                "- Prévention complications de décubitus"
            )),
            FicheRow(concept="DD du coma", detail_md=(
                "- **Locked-in syndrome** : mouvements verticaux des yeux conservés\n"
                "- **Mutisme akinétique** : vigile, yeux ouverts\n"
                "- **Simulation/hystérie** : résistance à l'ouverture des yeux"
            )),
        ]),
        SousPartie(lettre="B", titre="Paralysie faciale", rows=[
            FicheRow(concept="PF centrale vs périphérique", detail_md=(
                "| | PF centrale | PF périphérique |\n"
                "|--|-----------|----------------|\n"
                "| Territoire atteint | **Inférieur** seulement | **Supérieur + Inférieur** |\n"
                "| Dissociation automatico-volontaire | Possible | Absente |\n"
                "| Signe de Charles Bell | Non | **Oui** |\n"
                "| Signes associés | Hémiparésie MS | Oeil sec, agueusie |\n"
            )),
            FicheRow(concept="PFP a frigore", detail_md=(
                "- Étiologie la plus fréquente des PFP\n"
                "- Neuropathie oedémateuse (processus inflammatoire/viral)\n"
                "- Installation brutale (matin, après exposition au froid), maximale en < 48h\n"
                "- Douleurs rétro-auriculaires fréquentes\n"
                "- Paralysie totalement **isolée**\n"
                "- Récupération complète en < 2 mois (5-10% de séquelles)"
            )),
            FicheRow(concept="Traitement PFP a frigore", detail_md=(
                "- **Protection oculaire** : larmes artificielles, pansement occlusif la nuit\n"
                "- **Corticothérapie orale** : 1 mg/kg/j pendant 10 jours, "
                "dans les **72 premières heures**\n"
                "- **Aucun examen complémentaire systématique**"
            )),
            FicheRow(concept="◆ Autres étiologies PFP", detail_md=(
                "- Traumatique : fracture du rocher\n"
                "- Infectieuses : **zona** du ganglion géniculé, otite, Lyme, VIH\n"
                "- Guillain-Barré : diplégie faciale + déficit sensitivo-moteur + aréflexie\n"
                "- AVC vertébrobasilaire (syndrome alterne)\n"
                "- SEP, sarcoïdose (Heerfordt), diabète, tumeurs"
            )),
            FicheRow(concept="Complications PFP", detail_md=(
                "- Kératite et ulcérations cornéennes\n"
                "- Hémispasme facial post-paralytique avec **syncinésies**\n"
                "- Syndrome des **larmes de crocodile** (réinnervation aberrante)"
            )),
        ]),
        SousPartie(lettre="C", titre="Radiculalgies et NCB", rows=[
            FicheRow(concept="★ Sciatique : topographie", detail_md=(
                "| Racine | Trajet | Réflexe aboli |\n"
                "|--------|--------|---------------|\n"
                "| **L5** | Face postéro-externe cuisse, face externe jambe, dos du pied | Aucun |\n"
                "| **S1** | Face postérieure fesse/cuisse/mollet, talon, plante du pied | **Achilléen** |\n"
                "| L4 | Face antéro-externe cuisse, bord antérieur jambe | **Rotulien** |\n"
                "| L3 | Face antéro-interne cuisse (ne dépasse pas le genou) | Rotulien |\n"
            )),
            FicheRow(concept="Signes cliniques", detail_md=(
                "- Signes rachidiens : effacement lordose, limitation flexion "
                "(distance doigts-sol, indice de Schober)\n"
                "- **Signe de Lasègue** : élévation MI en décubitus dorsal reproduit "
                "la douleur radiculaire\n"
                "- **Signe de Léri** : hyperextension cuisse en décubitus ventral "
                "(douleur L3/L4)"
            )),
            FicheRow(concept="Signes de gravité", detail_md=(
                "- **Sciatique paralysante** (déficit moteur) +++\n"
                "- **Syndrome de la queue de cheval** (anesthésie en selle, "
                "troubles vésico-sphinctériens) +++\n"
                "- Sciatique hyperalgique rebelle aux morphiniques\n"
                "- => Transfert urgent en milieu **chirurgical**"
            )),
            FicheRow(concept="◆ Hernie discale", detail_md=(
                "- Terrain : homme 25-40 ans, ATCD lombalgies\n"
                "- Post-effort, douleur impulsive à la toux\n"
                "- **Aucun examen** si lombosciatique typique\n"
                "- Indications imagerie : < 18 ans, > 65 ans, fièvre, déficit neurologique, "
                "hyperalgie résistante, > 6-8 semaines sans amélioration\n"
                "- Traitement médical : antalgiques, AINS, repos minimal (3-5 j)\n"
                "- Chirurgie si signes de gravité ou persistance > 8 semaines"
            )),
            FicheRow(concept="NCB", detail_md=(
                "| Racine | Territoire douloureux |\n"
                "|--------|----------------------|\n"
                "| C6 | Épaule, bras, avant-bras, pouce |\n"
                "| C7 | Face postérieure bras/coude, index-médius |\n"
                "| C8 | Bord interne MS, 2 derniers doigts |\n\n"
                "- Gravité : **myélopathie cervicarthrosique** (signes pyramidaux, Lhermitte, Babinski)\n"
                "- Traitement médical en 1re intention (guérison en 4-6 semaines)\n"
                "- Chirurgie si NCB paralysante ou myélopathie rebelle"
            )),
            FicheRow(concept="◆ Syndromes canalaires", detail_md=(
                "- **Canal carpien** : paresthésies 3 premiers doigts (médian), "
                "signe de Tinel/Phalen, déficit éminence thénar\n"
                "- **Nerf ulnaire au coude** : paresthésies 4e-5e doigts, déficit interosseux\n"
                "- **Nerf radial (gouttière humérale)** : main tombante (déficit extenseurs)\n"
                "- **Nerf fibulaire** : déficit loge antéro-latérale de jambe (steppage)"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="AIC vs Hémorragie intraparenchymateuse", markdown=(
            "| Critère | AIC | Hémorragie |\n"
            "|---------|-----|------------|\n"
            "| Fréquence | 80% | 20% |\n"
            "| Systématisation artérielle | Oui | Non |\n"
            "| Céphalées associées | Rares | Fréquentes +++ |\n"
            "| Scanner sans injection | Hypodensité (retardée) | **Hyperdensité** spontanée |\n"
            "| IRM diffusion | Hypersignal précoce | Hyposignal T2* |\n"
            "| Objectif TA | 220/120 (ou 185/110 si TIV) | < 140/90 |\n"
            "| Antithrombotiques | Aspirine + HBPM | **Arrêt** + réversion |\n"
        )),
        TableauSynthese(titre="Céphalées primaires — Comparaison", markdown=(
            "| | Migraine | Céphalée de tension | AVF |\n"
            "|--|---------|--------------------|---------|\n"
            "| Terrain | F > H | Tous | **H 20-40 ans** |\n"
            "| Durée | 4-72h | Variable | 15 min-3h |\n"
            "| Caractère | Pulsatile, unilatérale | Bilatérale, étau | Déchirure, périorbitaire |\n"
            "| Photo/phonophobie | Oui | Non | Non |\n"
            "| Signes autonomiques | Non | Non | **Oui** |\n"
            "| Fond 1re intention | Propranolol | Amitriptyline | **Vérapamil** |\n"
        )),
        TableauSynthese(titre="Syndromes épileptiques de l'enfant/adolescent", markdown=(
            "| Syndrome | Âge | Type de crise | Particularité |\n"
            "|----------|-----|--------------|---------------|\n"
            "| Épilepsie-absence | ~7 ans | Absences (> 100/j) | Bon pronostic |\n"
            "| Myoclonique juvénile | 12-18 ans | Myoclonies au réveil | 90% récidive à l'arrêt |\n"
            "| **West** | 2-12 mois | Spasmes en flexion | Hypsarythmie (EEG) |\n"
            "| **Lennox-Gastaut** | 3-5 ans | Crises multiples | Pronostic sévère |\n"
        )),
        TableauSynthese(titre="Démences neurodégénératives — Comparaison", markdown=(
            "| | Alzheimer | Corps de Lewy | DLFT |\n"
            "|--|----------|--------------|------|\n"
            "| Début | Progressif | Rapide (~1 an) | < 65 ans |\n"
            "| Trouble dominant | **Mémoire** | Exécutif | **Comportement** |\n"
            "| Hallucinations | Tardives | **Précoces** | Non |\n"
            "| Syndrome parkinsonien | Non | **Oui** | Non |\n"
            "| Neuroleptiques | Possibles | **CI** | Possibles |\n"
            "| IRM | Atrophie hippocampique | Non spécifique | Atrophie frontale |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| AVC en France | **150 000**/an | 1re cause handicap moteur acquis |\n"
        "| AIC | **80%** des AVC | AIT + AIC |\n"
        "| Hémorragies cérébrales | **20%** des AVC | Non traumatiques |\n"
        "| Sténose athéromateuse | > **50%** | Seuil diagnostique |\n"
        "| Thrombolyse IV | < **4h30** | Délai maximal |\n"
        "| Thrombectomie | < **6h** (jusqu'à 24h si mismatch) | Neuroradiologie interventionnelle |\n"
        "| TA si thrombolyse | < **185/110** mmHg | Nicardipine IVSE |\n"
        "| TA si AIC sans TIV | < **220/120** mmHg | Respect poussée tensionnelle |\n"
        "| TA si hémorragie | < **140/90** mmHg | D'emblée |\n"
        "| Endartériectomie | Sténose > **70%** | Dans les 15 jours |\n"
        "| Lacune | < **15 mm** | Infarctus profond |\n"
        "| AIT | < **1 heure** | Sans lésion en imagerie |\n"
        "| Migraine sans aura | > **5 crises**, 4-72h | Critères IHS |\n"
        "| Migraine avec aura | > **2 crises** | Aura 5-60 min |\n"
        "| CCQ | > **15 j/mois**, > 3 mois | Abus médicamenteux |\n"
        "| Triptans max | **8 prises**/mois | Risque CCQ |\n"
        "| EME convulsif | > **5 min** ou 2 crises | Sans retour conscience |\n"
        "| SEP NORB | **25%** révélatrice | BAV unilatérale |\n"
        "| Décrément myasthénie | > **10%** | ENMG répétitif |\n"
        "| Glasgow coma | < **8** | Définition du coma |\n"
    ))

    points_cles = [
        "Les AVC sont la 1re cause de handicap moteur acquis : 80% AIC, 20% hémorragies",
        "L'IRM de diffusion est l'examen le plus sensible pour le diagnostic précoce d'AIC",
        "Thrombolyse IV < 4h30, thrombectomie < 6h (extensible 24h si mismatch) : chaque minute compte",
        "Hémorragie cérébrale : scanner = hyperdensité spontanée, objectif TA < 140/90 mmHg d'emblée",
        "TVC : anticoagulation curative immédiate MÊME en cas de remaniement hémorragique",
        "Migraine avec aura contre-indique la contraception oestro-progestative",
        "EME : BZD en 1re ligne, anti-épileptique en 2e ligne, sédation si échec à 30 min",
        "SEP : dissémination temporospatiale, NORB révélatrice dans 25%, aucun traitement de fond dans les formes progressives primaires",
        "Myasthénie : fatigabilité à l'effort, ptosis, décrément ENMG > 10%, CI aminosides et bêtabloquants",
        "Compression médullaire = urgence : IRM médullaire systématique en urgence",
    ]

    fiche_eclair_md = (
        "**AVC** : 150 000/an, 1re cause handicap moteur. "
        "AIC 80% : IRM diffusion en urgence. Thrombolyse < 4h30, thrombectomie < 6h. "
        "Aspirine 300mg + HBPM. Hémorragie 20% : scanner = hyperdensité, "
        "TA < 140/90, arrêt anticoagulants + réversion.\n\n"
        "**Céphalées** : Brutale = HSA jusqu'à preuve du contraire (scanner + PL si normal). "
        "Migraine : 5 crises de 4-72h, triptans en crise, propranolol en fond. "
        "AVF : homme, sumatriptan SC + O2, vérapamil en fond. "
        "Névralgie V : carbamazépine.\n\n"
        "**Épilepsie** : CGTC (morsure latérale de langue), absences (pointes-ondes 3Hz), "
        "crises partielles (marche jacksonienne). "
        "EME : BZD > anti-épileptique > sédation. "
        "Fond : valproate (généralisée), lévétiracétam (partielle). "
        "Grossesse : lamotrigine + folates.\n\n"
        "**SEP** : démyélinisation SNC, femme 20-40 ans, NORB 25%. "
        "Critères McDonald (dissémination temporo-spatiale). "
        "Poussée : méthylprednisolone 1g/j x3j. "
        "Fond : IFN-bêta, glatiramère.\n\n"
        "**Démences** : Alzheimer (1re cause, amnésie hippocampique, atrophie hippocampique IRM), "
        "Corps de Lewy (hallucinations + parkinsonisme, neuroleptiques CI), "
        "DLFT (troubles comportementaux), "
        "vasculaire (lacunes, marche d'escalier).\n\n"
        "**Myasthénie** : fatigabilité, ptosis, décrément ENMG > 10%, Ac anti-RAch. "
        "Anticholinestérasiques + thymectomie. CI : aminosides, BB.\n\n"
        "**Compression médullaire** : syndrome lésionnel + sous-lésionnel + rachidien. "
        "IRM médullaire en urgence. Métastases (> 60 ans), méningiomes, neurinomes.\n\n"
        "**PFP a frigore** : la plus fréquente, corticothérapie 1mg/kg x10j dans les 72h, "
        "protection oculaire, récupération < 2 mois."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Neurologie",
        annee="2025-2026",
        item="Items 335, 336, 337, 338, 99, 100, 101, 97, 98, 89, 106, 132, 91, 93, 94, 95, 79, 131, 92",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="",
        usage=UsageStats(),
    )


def main():
    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(exist_ok=True)

    fiche = build_fiche()

    # Images : charger depuis image_captions.json si disponible
    captions_file = PROJECT_ROOT / "output" / ".work" / "neurologie" / "image_captions.json"
    if captions_file.exists():
        import json
        try:
            captions = json.loads(captions_file.read_text(encoding="utf-8"))
            print(f"  Loaded {len(captions)} image captions")
        except Exception as e:
            print(f"  Could not load captions: {e}")

    fiches_dir = output_dir / "fiches"
    fiches_dir.mkdir(parents=True, exist_ok=True)

    docx_path = fiches_dir / "Medecine_generale_neurologie_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = fiches_dir / "Medecine_generale_neurologie_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path} ({pdf_path.stat().st_size / 1e6:.1f} MB)")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

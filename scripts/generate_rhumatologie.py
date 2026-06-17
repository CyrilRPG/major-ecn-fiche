"""Génère la fiche exhaustive de Rhumatologie à partir du texte source."""

from __future__ import annotations

import json
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
        PlanPartie(numero="I", titre="Douleur et thérapeutiques antalgiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et évaluation de la douleur"),
            PlanSousPartie(lettre="B", titre="Douleurs neuropathiques"),
            PlanSousPartie(lettre="C", titre="Antalgiques de paliers I, II et III"),
            PlanSousPartie(lettre="D", titre="Douleur chronique et approches non médicamenteuses"),
        ]),
        PlanPartie(numero="II", titre="Douleurs des membres et extrémités", sous_parties=[
            PlanSousPartie(lettre="A", titre="Douleurs de hanche"),
            PlanSousPartie(lettre="B", titre="Douleurs de genou"),
            PlanSousPartie(lettre="C", titre="Douleurs d'épaule et pathologies de la coiffe"),
        ]),
        PlanPartie(numero="III", titre="Polyarthrite rhumatoïde et épanchement articulaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Épanchement articulaire d'évolution récente"),
            PlanSousPartie(lettre="B", titre="Polyarthrite rhumatoïde"),
        ]),
        PlanPartie(numero="IV", titre="Infections ostéo-articulaires", sous_parties=[
            PlanSousPartie(lettre="A", titre="Arthrite septique"),
            PlanSousPartie(lettre="B", titre="Ostéite et ostéomyélite"),
            PlanSousPartie(lettre="C", titre="Spondylodiscite"),
        ]),
        PlanPartie(numero="V", titre="Maladie de Horton et PPR", sous_parties=[
            PlanSousPartie(lettre="A", titre="Pseudo-polyarthrite rhizomélique"),
            PlanSousPartie(lettre="B", titre="Artérite à cellules géantes (Horton)"),
        ]),
        PlanPartie(numero="VI", titre="Ostéoporose, rachialgies et radiculalgies", sous_parties=[
            PlanSousPartie(lettre="A", titre="Ostéoporose"),
            PlanSousPartie(lettre="B", titre="Rachialgies : cervicalgies, dorsalgies, lombalgies"),
            PlanSousPartie(lettre="C", titre="Radiculalgies : lombosciatique et NCB"),
        ]),
        PlanPartie(numero="VII", titre="Arthropathies microcristallines et anti-inflammatoires", sous_parties=[
            PlanSousPartie(lettre="A", titre="Goutte"),
            PlanSousPartie(lettre="B", titre="Chondrocalcinose (rhumatisme à PPCD)"),
            PlanSousPartie(lettre="C", titre="AINS et corticothérapie : modalités et surveillance"),
        ]),
    ]

    # ── PARTIE I : DOULEUR ET THÉRAPEUTIQUES ANTALGIQUES ──
    partie_i = Partie(numero="I", titre="Douleur et thérapeutiques antalgiques", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et évaluation de la douleur", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Douleur** : expérience sensorielle et émotionnelle désagréable, associée à une lésion "
                "tissulaire réelle/potentielle (expérience **subjective**)\n"
                "- Représente **40-60%** des motifs de consultation (85% en rhumatologie)\n"
                "- Absence de parallélisme douleur/lésion anatomique\n"
                "- La non-évaluation de la douleur peut être considérée comme une **faute** : trace écrite obligatoire"
            )),
            FicheRow(concept="Classification temporelle", detail_md=(
                "| Critère | Douleur aiguë | Douleur chronique |\n"
                "|---------|--------------|-------------------|\n"
                "| Durée | **< 3 mois** | **> 3 mois** |\n"
                "| Rôle | Signal d'alarme utile | Inutile, destructrice |\n"
                "| Risque | Limité | **Dépression** |\n"
                "| Évaluation | EVA, EN | Multidimensionnelle (QDSA, HAD) |\n"
            )),
            FicheRow(concept="Types de douleur", detail_md=(
                "- **Nociceptive** : excès de nociception, horaire mécanique\n"
                "- **Neuropathique** : lésion nerveuse, distorsion du message (questionnaire **DN4 > 4/10**)\n"
                "- **Dysfonctionnelle** : sensibilisation centrale (fibromyalgie, colopathie, cystalgie)\n"
                "- **Mixte** : association nociceptive + neuropathique"
            )),
            FicheRow(concept="★ ◆ Outils d'évaluation", detail_md=(
                "- **EVA** / **EN** (à préférer) / EVS\n"
                "- Qualificatifs : **QDSA** (questionnaire de St Antoine)\n"
                "- Anxiété/dépression : **HAD** (> 7 = éléments anxio-dépressifs, > 11 = caractérisé)\n"
                "- Douleur neuropathique : **DN4** (positif si > 4/10)\n"
                "- Sujet âgé : échelle **Algoplus** (5 items), **Doloplus 2**, ECPA"
            )),
            FicheRow(concept="", detail_md=(
                "- Douleur mécanique : augmentée à l'activité, améliorée au repos, dérouillage matinal **< 30 min**\n"
                "- Douleur inflammatoire : réveils nocturnes en 2e partie de nuit, dérouillage matinal **> 30 min**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Douleurs neuropathiques", rows=[
            FicheRow(concept="Caractéristiques", detail_md=(
                "- Liée à une compression/lésion de tronc, racine ou plexus nerveux\n"
                "- Clinique : brûlures, décharges électriques, paresthésies, allodynie, hypoesthésie\n"
                "- Diagnostic : questionnaire **DN4** (positif si score > 4/10)"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "| Classe | Molécule | EI principaux |\n"
                "|--------|----------|---------------|\n"
                "| Antidépresseurs tricycliques | **Amitriptyline** (Laroxyl) | Anticholinergiques : somnolence, bouche sèche, constipation |\n"
                "| IRSNa | Duloxétine, venlafaxine | Idem tricycliques |\n"
                "| Antiépileptiques | **Gabapentine** (Neurontin) | Somnolence, vertiges, ataxie |\n"
                "| Antiépileptiques | **Prégabaline** (Lyrica) | Somnolence, ataxie, prise de poids |\n"
                "| Opioïde faible | Tramadol | Constipation, NV, seuil épileptogène |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ CI amitriptyline : **glaucome à angle fermé**, hypertrophie prostate sévère, IDM récent\n"
                "- ⚠ Introduction gabapentine/prégabaline à **posologie croissante** obligatoire"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Antalgiques de paliers I, II et III", rows=[
            FicheRow(concept="★ Paliers OMS", detail_md=(
                "| Palier | Indication | Molécules principales |\n"
                "|--------|-----------|----------------------|\n"
                "| I | Douleur **< 4/10** | Paracétamol (3-4 g/j), AINS, aspirine |\n"
                "| II | Douleur **4-7/10** ou échec palier I | Codéine, **tramadol**, néfopam |\n"
                "| III | Douleur **> 7/10** ou échec palier II | **Morphine**, oxycodone, fentanyl |\n"
            )),
            FicheRow(concept="◆ Paracétamol", detail_md=(
                "- Analgésique antipyrétique, pic plasmatique 30-60 min\n"
                "- Posologie : **3-4 g/24h** (intervalle min 4h entre prises)\n"
                "- Bonne tolérance ; toxicité hépatique si surdosage → antidote : **N-acétyl-cystéine**\n"
                "- Autorisé chez la **femme enceinte**\n"
                "- Adapter posologie si IRC (moitié de dose)"
            )),
            FicheRow(concept="Tramadol", detail_md=(
                "- Opioïde faible + IRSNa (intéressant si douleur **mixte**)\n"
                "- Action via **CYP2D6** ; dose max **400 mg/j**\n"
                "- EI : constipation, NV, somnolence, **abaissement seuil épileptogène**\n"
                "- CI : épilepsie non contrôlée, association IMAO, insuffisance respiratoire sévère, grossesse"
            )),
            FicheRow(concept="Morphine et opioïdes forts", detail_md=(
                "- Mode d'action : récepteurs opioïdes **mu, delta, kappa**\n"
                "- Morphine LP (Skénan/Moscontin) : 60 mg/j en 2 prises (40 mg si sujet fragile)\n"
                "- Morphine LI (Actiskénan, Sevredol) : titration et inter-doses\n"
                "- Fentanyl transdermique (Durogésic) : patch/72h, titration préalable recommandée\n"
                "- Ordonnance **sécurisée** : durée 28j (7j si injectable), nom en toutes lettres"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Surdosage morphinique : somnolence + **bradypnée < 10/min** → **naloxone** IV\n"
                "- ⚠ Prévention **constipation systématique** dès le début du traitement\n"
                "- ⚠ Fièvre/chaleur augmente le passage du **fentanyl** transdermique"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Douleur chronique et approches non médicamenteuses", rows=[
            FicheRow(concept="◆ Centres spécialisés (CETD)", detail_md=(
                "- Indications : évolution insatisfaisante malgré traitement adapté, doute diagnostique\n"
                "- Modèle **multidimensionnel** : sensori-discriminatif, cognitif, affectif, comportemental\n"
                "- Évaluation : HAD, QDSA, DN4, schéma des zones douloureuses"
            )),
            FicheRow(concept="Approches non médicamenteuses", detail_md=(
                "- **Hypnose** : preuves neurophysiologiques (PET-scanner), enfants adhèrent mieux\n"
                "- **TCC** : agit sur distorsions cognitives (migraine, fibromyalgie)\n"
                "- **TENS** : stimulation électrique transcutanée (principe du gate control)\n"
                "- Neurostimulation médullaire : douleurs neuropathiques rebelles\n"
                "- Ostéopathie, stimulations mécaniques (froid/chaud), acupuncture"
            )),
            FicheRow(concept="◆ Douleur du sujet âgé", detail_md=(
                "- Suspecter devant tout **changement de comportement**\n"
                "- Hétéro-évaluation : Doloplus 2, ECPA, **Algoplus** (5 items)\n"
                "- Recommandations : voie orale, molécules à demi-vie courte, « **start low and go slow** »"
            )),
        ]),
    ])

    # ── PARTIE II : DOULEURS DES MEMBRES ET EXTRÉMITÉS ──
    partie_ii = Partie(numero="II", titre="Douleurs des membres et extrémités", sous_parties=[
        SousPartie(lettre="A", titre="Douleurs de hanche", rows=[
            FicheRow(concept="Clinique", detail_md=(
                "- Siège : **inguinal** ++ (parfois face antérieure cuisse jusque genou)\n"
                "- Intensité augmentée en **appui monopodal**\n"
                "- Horaire mécanique ou inflammatoire\n"
                "- Mobilité normale : flexion 130°, RI/RE 30°, abduction 45°, adduction 30°"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La limitation prédomine initialement sur la **rotation interne** et l'**abduction**\n"
                "- ⚠ Ne pas confondre mobilité de hanche et mobilité du bassin"
            ), kind="piege"),
            FicheRow(concept="◆ Étiologies", detail_md=(
                "| RX normale | RX anormale mécanique | RX anormale inflammatoire |\n"
                "|-----------|----------------------|-------------------------|\n"
                "| Coxarthrose débutante | **Coxarthrose** | Coxite rhumatoïde (PR) |\n"
                "| Ostéonécrose débutante | **Ostéonécrose** | Coxite septique |\n"
                "| Algodystrophie | Coxopathie destructrice rapide | Coxite de spondylarthropathie |\n"
                "| Coxite débutante → IRM | Algodystrophie | Coxite microcristalline |\n"
            )),
            FicheRow(concept="Fausses douleurs de hanche", detail_md=(
                "- Douleurs projetées : radiculaire L3/L4/L5, névralgie fémoro-cutanée\n"
                "- Lésions de voisinage : tendinopathie, bursite, atteinte sacro-iliaque, lésion pubienne"
            )),
        ]),
        SousPartie(lettre="B", titre="Douleurs de genou", rows=[
            FicheRow(concept="Examen clinique", detail_md=(
                "- Morphotype : genu valgum/varum\n"
                "- Épanchement : **choc rotulien**, signe du flot\n"
                "- Mobilités normales : flexion active 140°, passive 160°, extension 5-10°\n"
                "- Examen capsulo-ligamentaire : test de **Lachman** (croisés), bâillements (latéraux)\n"
                "- Ressaut rotatoire : signe de **Lemaire**, jerk test"
            )),
            FicheRow(concept="◆ Imagerie", detail_md=(
                "- RX standard : genoux F **debout en charge**, P en flexion 15°, incidence FP à 30°\n"
                "- Ponction articulaire si épanchement\n"
                "- Éliminer : coxopathie projetée, cruralgie, phlébite, artérite"
            )),
        ]),
        SousPartie(lettre="C", titre="Douleurs d'épaule et pathologies de la coiffe", rows=[
            FicheRow(concept="Examen de l'épaule", detail_md=(
                "- 3 articulations : scapulo-humérale, acromio-claviculaire, costo-claviculaire\n"
                "- Souffrance coiffe : signes de **Neer**, **Yocum**, **Hawkins**\n"
                "- Rupture coiffe : manoeuvre de **Jobe** (supra-épineux), **palm-up test** (long biceps), "
                "**lift-off** de Gerber (sub-scapulaire), manoeuvre de **Patte** (infra-épineux)"
            )),
            FicheRow(concept="Épaule douloureuse simple", detail_md=(
                "- Détérioration dégénérative tendon de la coiffe\n"
                "- Signes de souffrance **positifs**, signes de rupture **négatifs**\n"
                "- PEC : AINS, infiltrations, kinésithérapie pendant **6 mois** → échec : acromioplastie"
            )),
            FicheRow(concept="Calcification de la coiffe", detail_md=(
                "- Dépôts calciques au sein du tendon (++ **supra-épineux**)\n"
                "- Crises hyperalgiques = bursite microcristalline : douleur brutale, impotence totale\n"
                "- RX : calcifications tendineuses ; lors des crises : opacités dans bourse sous-acromiale\n"
                "- Crise aiguë : repos (Dujarier 4-7j), antalgiques, AINS, glaçage, +/- infiltrations"
            )),
            FicheRow(concept="◆ Épaule pseudo-paralytique", detail_md=(
                "- Rupture/perforation des tendons de la coiffe\n"
                "- Perte mobilité **active** sans déficit neurologique, mobilité **passive** conservée\n"
                "- RX : ascension tête humérale, condensation acromion\n"
                "- PEC : rééducation si > 60 ans ; chirurgie si sujet jeune ou échec"
            )),
            FicheRow(concept="Capsulite rétractile (épaule gelée)", detail_md=(
                "- Phase initiale (2-4 sem) : douleurs diffuses, épaule chaude\n"
                "- Phase intermédiaire (4-12 mois) : limitation **active et passive** complète\n"
                "- Arthrographie confirme rétraction capsulaire\n"
                "- PEC : antalgiques, AINS, kinésithérapie prolongée ; échec : arthrodistension"
            )),
        ]),
    ])

    # ── PARTIE III : PR ET ÉPANCHEMENT ARTICULAIRE ──
    partie_iii = Partie(numero="III", titre="Polyarthrite rhumatoïde et épanchement articulaire", sous_parties=[
        SousPartie(lettre="A", titre="Épanchement articulaire d'évolution récente", rows=[
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- Tuméfaction globale de l'articulation, disparition des reliefs anatomiques\n"
                "- Genou : **choc rotulien**, signe du flot\n"
                "- Diagnostics différentiels : hygroma, ténosynovite, érysipèle, lésion tumorale"
            )),
            FicheRow(concept="Ponction articulaire", detail_md=(
                "- Systématique si épanchement articulaire\n"
                "- Guidage échographique si articulation profonde (hanche)\n"
                "- Analyse : cytologique, biochimique, microbiologique, **recherche cristaux systématique**"
            )),
            FicheRow(concept="Interprétation", detail_md=(
                "| Type | Aspect | GB/mm³ | PNN | Protéines | Étiologies |\n"
                "|------|--------|--------|-----|-----------|------------|\n"
                "| Mécanique | Jaune clair, visqueux | **< 1 000** | < 50% | < 40 g/L | Arthrose, lésion méniscale |\n"
                "| Inflammatoire | Clair, fluide | **> 2 000** | > 50% | > 40 g/L | Septique, microcristallin, PR |\n"
                "| Puriforme | Trouble/purulent | **> 10 000** | +++ PNN | Élevées | Septique, goutte, CCA |\n"
                "| Hémorragique | Sanglant | Variable | Variable | Variable | Traumatisme, CCA, tumeur synoviale |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Risque d'**arthrite septique iatrogène** si ponction dans un hygroma/bursite\n"
                "- ⚠ Si tuberculose : liquide **lymphocytaire** (et non PNN)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Polyarthrite rhumatoïde", rows=[
            FicheRow(concept="Épidémiologie", detail_md=(
                "- Rhumatisme inflammatoire chronique le **plus fréquent**\n"
                "- Prévalence : **0,3-0,8%** de la population générale\n"
                "- Début autour de **50 ans**, sex-ratio **3F/1H** avant 60 ans\n"
                "- Cause inconnue : **tabac** +++ sur terrain génétique prédisposant"
            )),
            FicheRow(concept="Diagnostic", detail_md=(
                "- Clinique : douleur inflammatoire + gonflements des **petites articulations distales** "
                "(poignets, mains, avant-pieds) **symétriques**, tendance à la déformation\n"
                "- Biologie : syndrome inflammatoire inconstant, **FR** et **anti-CCP** positifs (inconstant)\n"
                "- Anti-CCP : **très spécifique** +++\n"
                "- FAN pour éliminer lupus"
            )),
            FicheRow(concept="◆ Imagerie", detail_md=(
                "- RX mains/poignets de face, avant-pieds de face et 3/4\n"
                "- Recherche **pincements articulaires** et **érosions**\n"
                "- RX thorax pour diagnostic différentiel (sarcoïdose)"
            )),
            FicheRow(concept="Activité et suivi", detail_md=(
                "- Score **DAS28** : nombre d'articulations douloureuses/gonflées, CRP/VS, EVA patient\n"
                "- Comorbidités : **cardiovasculaire** (morbi-mortalité augmentée), lymphomes (x2 si PR sévère), "
                "infections (liées aux traitements)"
            )),
            FicheRow(concept="Traitement de fond", detail_md=(
                "- **Méthotrexate** = 1re ligne (~15 mg/semaine en une prise)\n"
                "- Bilan pré-MTX : NFS, BHC, albumine, fonction rénale, RX thorax, sérologies VHB/VHC\n"
                "- Supplémentation **acide folique** 24-48h après le MTX\n"
                "- Surveillance : NFS + BHC + créatinine **1/mois** pendant 6 mois puis tous les 2-3 mois\n"
                "- **Tératogène** +++ : contraception efficace obligatoire"
            )),
            FicheRow(concept="", detail_md=(
                "- Si échec MTX : **biothérapies** (anti-TNFα, anti-CD20, CTLA4-Ig, JAKi)\n"
                "- CI biothérapies : infection active, cancer actif\n"
                "- ⚠ Anti-TNFα : risque de **réactivation tuberculose** → dépistage systématique"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Traitement symptomatique", detail_md=(
                "- Corticothérapie faible dose (**~10 mg/j** prednisone) en attendant efficacité du fond\n"
                "- Durée < **6 mois** avec schéma de décroissance\n"
                "- Possibilité d'infiltrations intra-articulaires de corticoïdes"
            )),
        ]),
    ])

    # ── PARTIE IV : INFECTIONS OSTÉO-ARTICULAIRES ──
    partie_iv = Partie(numero="IV", titre="Infections ostéo-articulaires", sous_parties=[
        SousPartie(lettre="A", titre="Arthrite septique", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Prolifération intra-articulaire d'un micro-organisme\n"
                "- Contamination : voie **hématogène** (foyer à distance) ou inoculation directe\n"
                "- Incidence : 5/100 000 hab/an\n"
                "- Germes : **S. aureus 60%**, BGN 20%, streptocoques 15%\n"
                "- FDR : diabète, OH, corticothérapie, immunodépression, prothèse articulaire"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- **Mono-arthrite brutale fébrile** +++\n"
                "- Fièvre, frissons\n"
                "- Douleur majeure de rythme inflammatoire, **impotence fonctionnelle totale**\n"
                "- Attitude antalgique en flexion (flessum)\n"
                "- Oedème, tuméfaction, rougeur\n"
                "- Recherche **porte d'entrée** systématique"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- NFS : hyperleucocytose à PNN, syndrome inflammatoire majeur\n"
                "- **Hémocultures** répétées (aérobies + anaérobies)\n"
                "- **Ponction articulaire** +++ : liquide inflammatoire/purulent, examen direct et culture\n"
                "- Recherche porte d'entrée : ECBU, RX thorax, écouvillonnage plaie"
            )),
            FicheRow(concept="PEC en urgence", detail_md=(
                "- **Hospitalisation** en milieu adapté\n"
                "- ATB : parentérale, large spectre, **double**, synergique, bonne diffusion ostéo-articulaire, "
                "anti-staphylococcique → adaptation à l'antibiogramme\n"
                "- Durée : **4-6 semaines**\n"
                "- Traitement porte d'entrée\n"
                "- Immobilisation antalgique brève puis rééducation précoce\n"
                "- Avis chirurgical si non amélioration à **10 jours** ou arthrite sur matériel"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours suspecter **gonocoque** si : ténosynovite mains/pieds + pustulose péri-articulaire\n"
                "- ⚠ L'imagerie ne doit **pas retarder** le traitement"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Ostéite et ostéomyélite", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Ostéomyélite = contamination **hématogène** ; ostéite = inoculation directe\n"
                "- Germes : **S. aureus 60%**, SBHA, BGN ; salmonelle chez **drépanocytaire**\n"
                "- FDR : idem arthrite septique + drépanocytose"
            )),
            FicheRow(concept="◆ Clinique et diagnostic", detail_md=(
                "- Forme aiguë : douleurs osseuses localisées, signes inflammatoires locaux et généraux\n"
                "- Forme chronique : douleurs intermittentes, +/- abcès, fistulisation\n"
                "- RX normales pendant **3-4 semaines** puis ostéolyse métaphysaire\n"
                "- **IRM** ++ : signal inflammatoire médullaire (plus précoce)\n"
                "- **Biopsie osseuse** systématique : bactériologie + anatomopathologie\n"
                "- ATB adaptés pendant minimum **6 semaines**"
            )),
        ]),
        SousPartie(lettre="C", titre="Spondylodiscite", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Infection disque intervertébral et corps vertébraux adjacents\n"
                "- **30%** des infections ostéo-articulaires\n"
                "- Prédominance masculine, 50-60 ans\n"
                "- Germes : **S. aureus** (hématogène), SCN (inoculation directe) = 50% ; BGN 15%\n"
                "- Toujours évoquer **spondylodiscite tuberculeuse**\n"
                "- Localisation : rachis **lombaire 70%**, thoracique 20%, cervical 10%"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Fièvre élevée, frissons\n"
                "- **Rachialgies segmentaires** de début brutal, permanentes, inflammatoires\n"
                "- Raideur rachidienne quasi constante avec **contracture paravertébrale invincible**\n"
                "- +/- Douleur radiculaire associée\n"
                "- Recherche signes de **compression médullaire/radiculaire**\n"
                "- Recherche porte d'entrée : ECBU, RX thorax, ETT +/- ETO (**endocardite** +++)"
            )),
            FicheRow(concept="Imagerie", detail_md=(
                "- RX : normales pendant 3-4 semaines puis pincement discal, érosion plateaux en miroir\n"
                "- **IRM médullaire** en 1re intention : signal inflammatoire disque + plateaux (hyperT2), "
                "abcès parties molles, épidurité\n"
                "- Ponction-biopsie disco-vertébrale (isolement germe 70-80%) si HC négatives"
            )),
            FicheRow(concept="PEC", detail_md=(
                "- Hospitalisation systématique\n"
                "- ATB IV double, synergique, bonne pénétration osseuse, **durée min 6 semaines**\n"
                "- Repos au lit, corset rigide antalgique (< 15j), rééducation précoce\n"
                "- Chirurgie uniquement si complication (syndrome de la queue de cheval)\n"
                "- Suivi minimum **1 an** (risque de rechute)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours rechercher une **endocardite** associée (ETT +/- ETO)\n"
                "- ⚠ Complication principale : compression médullaire/radiculaire par **abcès épidural**"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE V : MALADIE DE HORTON ET PPR ──
    partie_v = Partie(numero="V", titre="Maladie de Horton et PPR", sous_parties=[
        SousPartie(lettre="A", titre="Pseudo-polyarthrite rhizomélique", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Syndrome clinique : douleurs inflammatoires des **ceintures** (épaules et hanches) "
                "chez patients **> 50 ans**\n"
                "- Fréquent après 60 ans, prédominance féminine (3/1), caucasiens\n"
                "- Peut être isolée ou associée à **Horton** (15% d'emblée, 15-20% secondairement)\n"
                "- Si non traitée : évolue vers Horton dans **20-40%** des cas"
            )),
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- Terrain : femme caucasienne > 50 ans\n"
                "- Arthromyalgies inflammatoires **bilatérales** et **symétriques**\n"
                "- Topographie **rhizomélique** : épaules, rachis cervical, racine des MI\n"
                "- Enraidissement matinal prolongé **> 1 heure**\n"
                "- AEG, +/- fièvre 38°C\n"
                "- VS **> 40 mm**, syndrome inflammatoire biologique"
            )),
            FicheRow(concept="CAT / Horton", detail_md=(
                "- PPR sans signe de Horton : pas de BAT, traitement PPR\n"
                "- PPR avec signes de Horton francs : traitement Horton **en urgence**, BAT à discuter\n"
                "- PPR avec signes douteux : BAT et traitement selon résultat"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- Corticothérapie orale **0,2 mg/kg** (soit 15-20 mg/j)\n"
                "- Mesures adjuvantes à la corticothérapie\n"
                "- **Pas** d'anti-agrégant plaquettaire\n"
                "- Durée du traitement : **18 mois**\n"
                "- Surveillance : score PAS-PPR (CRP, EVA patient, EVA médecin, dérouillage, élévation épaules)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ PPR peut aussi être **paranéoplasique** : toujours y penser\n"
                "- DD : PR, péri-arthrite, polymyosite, néoplasie, ostéomalacie"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Artérite à cellules géantes (Horton)", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Vascularite systémique primitive à **cellules géantes**\n"
                "- Panartérite segmentaire et focale des artères de gros et moyen calibre\n"
                "- Atteinte préférentielle des branches de la **carotide externe**\n"
                "- Prédominance féminine (3/1), survenue **après 50 ans** (la plus fréquente des vascularites > 50 ans)"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Symptômes de **PPR** (50%)\n"
                "- AEG, fièvre\n"
                "- Signes vasculaires crâniens :\n"
                "  - **Céphalées temporales** unilatérales, nocturnes/matinales\n"
                "  - **Claudication mâchoire** (douleur à la mastication)\n"
                "  - Hyperesthésie cuir chevelu (**signe du peigne**)\n"
                "  - Artères temporales indurées, saillantes, diminution pulsatilité"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- Syndrome inflammatoire majeur : VS **> 40 mm**, CRP augmentée, anémie, thrombocytose\n"
                "- BHC : cholestase +/- cytolyse\n"
                "- **BAT** +++ : prélèvement > 1,5-3 cm, peut être réalisée **après** début corticothérapie\n"
                "  - Retrouve : infiltrat lympho-plasmocytaire, destruction limitante élastique interne, "
                "granulomes à cellules géantes\n"
                "  - BAT **négative n'exclut pas** le diagnostic (atteinte segmentaire et focale)"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- Horton non compliqué : prednisone PO **0,7 mg/kg/j** puis décroissance progressive\n"
                "- Signes oculaires/vasculaires : hospitalisation, **bolus méthylprednisolone IV** 500-1000 mg/j "
                "pendant 3 jours puis relais PO **1 mg/kg/j**\n"
                "- Anti-agrégant plaquettaire **systématique** (sauf CI)\n"
                "- Dose minimale efficace maintenue **1-3 ans**\n"
                "- Disparition des symptômes dans **72h** = test thérapeutique"
            )),
            FicheRow(concept="Complications", detail_md=(
                "- **Oculaires** (5-20%) +++ : NOIAA, OACR, NORB → amaurose fugace/**cécité**\n"
                "- Neurologiques : AIT/AVC (5%), poly/multi-neuropathie\n"
                "- Cardio-aortiques : aortite (risque anévrisme/dissection), IDM par coronarite\n"
                "- Atteinte artères pulmonaires, membres, rénale/digestive (nécrose langue/scalp)"
            )),
            FicheRow(concept="", detail_md=(
                "- Les complications oculaires (NOIAA) sont l'**urgence** du Horton → bolus IV immédiat\n"
                "- Rechute possible dans **20-50%** des cas ; récidive jusqu'à 10 ans après"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE VI : OSTÉOPOROSE, RACHIALGIES ET RADICULALGIES ──
    partie_vi = Partie(numero="VI", titre="Ostéoporose, rachialgies et radiculalgies", sous_parties=[
        SousPartie(lettre="A", titre="Ostéoporose", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Maladie généralisée du squelette : densité osseuse basse + altération micro-architecture "
                "→ **fragilité osseuse** avec risque élevé de fracture\n"
                "- Prévalence : femme **39%** à 65 ans, **70%** après 80 ans ; homme 15% après 50 ans"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **Primitive** (femme > 40 ans) : carence oestrogénique (ménopause), tabac, OH, "
                "immobilisation, hérédité, maigreur\n"
                "- **Secondaire** (homme : cause retrouvée dans 50%) :\n"
                "  - Iatrogène : **corticothérapie** > 7,5 mg/j > 3 mois, agonistes LHRH, IPP\n"
                "  - Endocrinienne : hyperthyroïdie, Cushing, hyperparathyroïdie, hypogonadisme\n"
                "  - Autres : malabsorption, PR, anorexie mentale, Lobstein/Marfan"
            )),
            FicheRow(concept="★ Fractures ostéoporotiques", detail_md=(
                "- **Pouteau-Colles** ~60 ans : fracture « sentinelle » (première à apparaître)\n"
                "- **Fracture vertébrale** ~70 ans : douleur mécanique aiguë, perte taille > 3 cm, "
                "RX : diminution hauteur > 20%, pas d'atteinte arc postérieur\n"
                "- **Fracture col fémoral** ~80 ans\n"
                "- Toutes sauf : crâne, rachis cervical, doigts, orteils"
            )),
            FicheRow(concept="DMO (DXA)", detail_md=(
                "- Technique de référence : absorptiométrie biphotonique aux rayons X\n"
                "- Réalisée sur rachis lombaire + hanche\n"
                "- **T-score** (femme ménopausée, homme > 50 ans) :\n"
                "  - Normal : > -1\n"
                "  - Ostéopénie : **-2,5 < T-score ≤ -1**\n"
                "  - Ostéoporose : **T-score ≤ -2,5**\n"
                "- Z-score pour homme jeune et femme non ménopausée\n"
                "- Score **FRAX** : risque fracturaire à 10 ans (systématique si pas de fracture)"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- RHD : apports calciques 1 g/j, vitamine D, éviction tabac/OH, activité physique, "
                "prévention chutes\n"
                "- **Bisphosphonates** en 1re intention : alendronate 70 mg/semaine PO, acide zolédronique "
                "1 perfusion/an IV\n"
                "- Si > 2 FV : **tériparatide** en 1re intention (SC 20 µg/j, 18 mois)\n"
                "- Autres : raloxifène, dénosumab (anti-RANK ligand)\n"
                "- Durée minimale **5 ans** (3 pour acide zolédronique)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Bisphosphonates PO : prise à jeun, grand verre d'eau, **ne pas se coucher 30 min**\n"
                "- ⚠ EI bisphosphonates : ostéonécrose de la **mâchoire**\n"
                "- ⚠ DD : métastases osseuses (douleurs nocturnes, AEG, lyse), myélome, ostéomalacie "
                "(hypocalcémie, fissures de Looser-Milkman)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Rachialgies : cervicalgies, dorsalgies, lombalgies", rows=[
            FicheRow(concept="Orientation", detail_md=(
                "- Toujours éliminer une cause extra-rachidienne\n"
                "- Rechercher les **drapeaux rouges** : contexte infectieux/néoplasique, fièvre, AEG, "
                "douleur inflammatoire, déficit neurologique, immunodépression\n"
                "- Si drapeaux rouges : RX + biologie (NFS, VS, CRP) ; IRM si doute"
            )),
            FicheRow(concept="◆ Cervicalgies", detail_md=(
                "- Aiguë mécanique : torticolis (repos, antalgiques, AINS), NCB, post-traumatique\n"
                "- Chronique : **cervicarthrose** (douleurs irradiant nuque/occiput/épaules, RX : lésions "
                "arthrosiques)\n"
                "- Complications cervicarthrose : **myélopathie cervicarthrosique** (syndrome pyramidal MI, "
                "troubles sensibilité profonde → IRM)"
            )),
            FicheRow(concept="◆ Lombalgies", detail_md=(
                "- **Lumbago aigu** : douleur brutale lors effort, blocage, attitude antalgique\n"
                "  - Si typique < 7 sem, < 50 ans : **aucun examen** complémentaire\n"
                "  - PEC : repos le plus bref possible, antalgiques, AINS, pas de kiné en phase aiguë\n"
                "- **Lombalgie chronique** > 3 mois :\n"
                "  - Discale (30-60 ans) : rééducation +++, antalgiques, TCC\n"
                "  - Articulaire postérieure : femme en surpoids, hyperlordose"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ DD des rachialgies : IDM postérieur, DA, AAA, EP, UGD, pancréatite, "
                "pyélonéphrite, tumeur rénale, zona"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Radiculalgies : lombosciatique et NCB", rows=[
            FicheRow(concept="★ Lombosciatique", detail_md=(
                "- Douleur unilatérale irradiant lombes → fesse → MI\n"
                "- **L4-L5** : face postérieure cuisse, postéro-externe jambe, dos pied, gros orteil ; "
                "déficit marche sur **talon**\n"
                "- **L5-S1** : face postérieure cuisse et jambe, talon, bord externe plante pied ; "
                "déficit marche sur **pointe** ; abolition réflexe **achilléen**"
            )),
            FicheRow(concept="Signes de gravité", detail_md=(
                "- **Sciatique paralysante** (déficit moteur < 3) +++\n"
                "- **Syndrome de la queue de cheval** : sciatique bilatérale, anesthésie en selle, "
                "troubles sphinctériens, abolition achilléens\n"
                "- Sciatique hyperalgique rebelle aux morphiniques\n"
                "- → **Transfert urgent** en milieu chirurgical"
            )),
            FicheRow(concept="Hernie discale", detail_md=(
                "- Terrain : homme 25-40 ans, ATCD lombalgie\n"
                "- Douleur impulsive (toux, éternuement), **signe de Lasègue** positif\n"
                "- Aucun examen si typique ; TDM/IRM si : signes neuro, douleur > 6-8 sem, atypie\n"
                "- PEC : repos bref (3-5j), antalgiques, AINS, orthèse 4-6 sem\n"
                "- Chirurgie si : signes de gravité ou persistance > 8 sem malgré traitement optimal"
            )),
            FicheRow(concept="◆ NCB (névralgie cervico-brachiale)", detail_md=(
                "- Souffrance racine du plexus brachial\n"
                "- Cause mécanique : **arthrose** ++ (douleur augmentée par mouvements cou/port charge)\n"
                "- Signes de gravité : compression médullaire cervicale, NCB paralysante, NCB hyperalgique\n"
                "- PEC : repos, antalgiques, AINS, contention cervicale, rééducation ; chirurgie si paralysie"
            )),
        ]),
    ])

    # ── PARTIE VII : ARTHROPATHIES MICROCRISTALLINES ET ANTI-INFLAMMATOIRES ──
    partie_vii = Partie(numero="VII", titre="Arthropathies microcristallines et anti-inflammatoires", sous_parties=[
        SousPartie(lettre="A", titre="Goutte", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Cristaux d'**urate de sodium** (UMS)\n"
                "- Prévalence > 1% dans pays industrialisés\n"
                "- Terrain : **homme > 35 ans**, femme ménopausée\n"
                "- Hyper-uricémie constante (10% des hyperuricémiques sont goutteux)\n"
                "- Primitive (90%) : génétique + alimentation (purines, OH, bière) + vieillissement rénal"
            )),
            FicheRow(concept="Accès goutteux", detail_md=(
                "- Douleur aiguë inflammatoire de début **brutal**, impotence fonctionnelle totale\n"
                "- Localisation : **MTP du gros orteil** +++ > cheville > genou\n"
                "- Intensité croissante, pulsatile, réveille en **2e partie de nuit**\n"
                "- Facteur déclenchant : excès alimentaire/OH, traumatisme, chirurgie\n"
                "- Articulation tuméfiée, rouge, chaude, peau tendue et luisante"
            )),
            FicheRow(concept="◆ Goutte chronique", detail_md=(
                "- Arthropathie goutteuse chronique : mono/oligo-arthrite asymétrique\n"
                "- **Tophus** : concrétions uratiques sous-cutanées (pavillon oreille, IPP, MCP, "
                "bourses olécrâniennes/rotuliennes)\n"
                "- Lithiases uriques radio-transparentes\n"
                "- Augmentation du **risque cardiovasculaire**"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- Uricémie élevée (mais **peut être normale pendant les crises** +++)\n"
                "- Ponction articulaire : liquide inflammatoire riche en PNN, stérile\n"
                "- Cristaux UMS : **fins, longs, en aiguille**, intra/extra-cellulaires, **réfringents** "
                "en lumière polarisée\n"
                "- RX (goutte chronique) : encoches en « hallebarde », géodes à l'emporte-pièce"
            )),
            FicheRow(concept="Traitement de l'accès", detail_md=(
                "- Repos articulaire, glaçage\n"
                "- **Colchicine** en 1re intention : 1 mg puis 0,5 mg 1h après, maintien 0,5-1 mg/j "
                "pendant **6 mois** si introduction hypo-uricémiant\n"
                "- Réponse rapide en quelques heures = argument diagnostique\n"
                "- EI principal : **diarrhées** +++\n"
                "- 2e intention : AINS ou corticothérapie"
            )),
            FicheRow(concept="Traitement hypo-uricémiant", detail_md=(
                "- Indications : dès le **1er épisode** de goutte, goutte sévère, tophus, lithiase\n"
                "- 1re intention : **allopurinol** 100 mg/j (augmentation progressive), "
                "sous couverture colchicine **6 mois**\n"
                "- 2e intention : **fébuxostat** si échec/intolérance\n"
                "- Objectif : uricémie **< 360 µmol/L** (< 300 si goutte sévère)\n"
                "- **À vie**\n"
                "- RHD : amaigrissement, régime pauvre en purines, arrêt OH/bière/sodas"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Ne jamais débuter allopurinol **pendant** une crise (risque de déclencher une goutte aiguë)\n"
                "- ⚠ EI allopurinol : **DRESS syndrome**, allergies"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Chondrocalcinose (rhumatisme à PPCD)", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Cristaux de **pyrophosphate de calcium dihydraté** (PPCD)\n"
                "- Prévalence : 10% > 50 ans, 20% > 80 ans\n"
                "- Primitive (90%) ; secondaire (10%) : **hyperparathyroïdie primaire**, **hémochromatose**"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- **Asymptomatique** le plus souvent\n"
                "- Accès aigus : monoarthrite pseudo-goutteuse (**genou** > poignet > MCP 2e-3e)\n"
                "- Arthropathie chronique (45%) : douleurs pseudo-arthrosiques (genou, hanche)"
            )),
            FicheRow(concept="Diagnostic", detail_md=(
                "- RX : calcifications cartilages et fibrocartilages : **ménisques genoux**, "
                "**ligament triangulaire du carpe**, **symphyse pubienne**\n"
                "- Ponction : cristaux PPCD : **courts, carrés/rectangulaires**, peu réfringents\n"
                "- Bilan étiologique : calcémie, **CST** (hémochromatose), **PTH** (hyperparathyroïdie)"
            )),
            FicheRow(concept="◆ Traitement", detail_md=(
                "- Accès aigu : repos, glaçage, **AINS** en 1re intention (1-2 sem)\n"
                "- 2e intention : corticothérapie ou colchicine\n"
                "- Infiltration cortisonique si diagnostic certain\n"
                "- Traitement étiologique si forme secondaire"
            )),
        ]),
        SousPartie(lettre="C", titre="AINS et corticothérapie : modalités et surveillance", rows=[
            FicheRow(concept="Corticoïdes — EI principaux", detail_md=(
                "- Hypercorticisme iatrogène : obésité facio-tronculaire, atrophie cutanée, vergetures\n"
                "- **Ostéoporose** cortico-induite, ostéonécrose épiphysaire\n"
                "- Intolérance au glucose, diabète, hyperlipidémie\n"
                "- Risque infectieux (reviviscence infection latente)\n"
                "- Complications oculaires : cataracte postérieure sous-capsulaire, glaucome\n"
                "- Sevrage : syndrome de sevrage, **insuffisance surrénalienne**"
            )),
            FicheRow(concept="Corticoïdes — mesures adjuvantes", detail_md=(
                "- Si durée > 15j et dose > 15 mg/j :\n"
                "  - Restriction sucres rapides, limitation apports sodés, supplémentation K+\n"
                "  - **Vitamine D** (800 UI/j) + calcium\n"
                "  - **Bisphosphonates** si > 3 mois à > 7,5 mg/j\n"
                "- Sevrage : décroissance progressive ; en dessous de **10 mg/j** : risque insuffisance "
                "surrénalienne → paliers mensuels de 1 mg/j\n"
                "- Test au **Synacthène** après arrêt"
            )),
            FicheRow(concept="AINS — EI et CI", detail_md=(
                "- EI : **UGD** (1re complication), néphrotoxicité (IRA si hypo-perfusion + IEC/ARA2), "
                "risque thrombotique CV (IDM, AVC), fermeture prématurée du canal artériel\n"
                "- CI : UGD évolutif, insuffisance rénale/hépatique/cardiaque sévère, grossesse > 6e mois\n"
                "- Coxibs : moindre risque UGD mais CI si insuffisance cardiaque NYHA II-IV, "
                "cardiopathie ischémique\n"
                "- Règle : **dose et durée minimales**, protection gastrique si patient à risque"
            )),
            FicheRow(concept="Infiltrations corticoïdes", detail_md=(
                "- Indications : arthrite inflammatoire, arthrose en poussée, tendinopathie, canal carpien\n"
                "- CI : infection locale/générale, troubles coagulation\n"
                "- Maximum **4 infiltrations/an** par site articulaire\n"
                "- Mise en décharge 24h après le geste\n"
                "- Analyse bactériologique si réaction post-infiltrative > 24h (arthrite septique)"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Goutte vs CCA — Comparaison", markdown=(
            "| Critère | Goutte | CCA (PPCD) |\n"
            "|---------|--------|------------|\n"
            "| Cristaux | UMS : fins, longs, en aiguille | PPCD : courts, carrés/rectangulaires |\n"
            "| Réfringence | Fortement réfringents | Peu réfringents |\n"
            "| Localisation | MTP gros orteil +++ | Genou +++ |\n"
            "| Terrain | Homme > 35 ans | > 50 ans, F > H |\n"
            "| RX | Encoches, géodes | Calcifications ménisques/carpe/pubis |\n"
            "| Causes secondaires | IRC, diurétiques | Hyperparathyroïdie, hémochromatose |\n"
            "| Traitement aigu 1re intention | Colchicine | AINS |\n"
        )),
        TableauSynthese(titre="Épanchement articulaire — Orientation diagnostique", markdown=(
            "| Type | GB/mm³ | Aspect | Étiologies principales |\n"
            "|------|--------|--------|----------------------|\n"
            "| Mécanique | < 1 000 | Jaune clair, visqueux | Arthrose, lésion méniscale |\n"
            "| Inflammatoire | > 2 000 | Clair, fluide | PR, septique, microcristallin |\n"
            "| Puriforme | > 10 000 | Trouble/purulent | Septique, goutte, CCA |\n"
            "| Hémorragique | Variable | Sanglant | Traumatisme, CCA, tumeur synoviale |\n"
        )),
        TableauSynthese(titre="Antalgiques — Paliers OMS", markdown=(
            "| Palier | Douleur | Molécules | Points clés |\n"
            "|--------|---------|-----------|-------------|\n"
            "| I | < 4/10 | Paracétamol, AINS | Paracétamol autorisé grossesse |\n"
            "| II | 4-7/10 | Codéine, tramadol, néfopam | Tramadol si douleur mixte |\n"
            "| III | > 7/10 | Morphine, oxycodone, fentanyl | Ordonnance sécurisée |\n"
        )),
        TableauSynthese(titre="Infections ostéo-articulaires — Comparaison", markdown=(
            "| Critère | Arthrite septique | Spondylodiscite | Ostéomyélite |\n"
            "|---------|------------------|----------------|-------------|\n"
            "| Germe principal | S. aureus 60% | S. aureus 50% | S. aureus 60% |\n"
            "| Durée ATB | 4-6 semaines | Min 6 semaines | Min 6 semaines |\n"
            "| Imagerie clé | Ponction articulaire | IRM médullaire | IRM + biopsie osseuse |\n"
            "| Particularité | Avis chirurgical si J10 | Rechercher endocardite | Drépanocytaire : salmonelle |\n"
        )),
        TableauSynthese(titre="Horton vs PPR — Comparaison", markdown=(
            "| Critère | PPR | Horton |\n"
            "|---------|-----|--------|\n"
            "| Corticothérapie | 0,2 mg/kg/j | 0,7 mg/kg/j (1 si compliqué) |\n"
            "| Durée traitement | 18 mois | 1-3 ans |\n"
            "| BAT | Non obligatoire si PPR isolée | Recommandée +++ |\n"
            "| Anti-agrégant | Non | Oui (systématique) |\n"
            "| Complication principale | Évolution vers Horton | Cécité (NOIAA) |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Douleur aiguë vs chronique | **3 mois** | Seuil de chronicité |\n"
        "| DN4 positif | **> 4/10** | Douleur neuropathique |\n"
        "| HAD dépression | **> 11** | Dépression caractérisée |\n"
        "| Paracétamol max | **3-4 g/j** | Intervalle min 4h |\n"
        "| Tramadol max | **400 mg/j** | Opioïde faible |\n"
        "| Bradypnée morphinique | **< 10/min** | Surdosage → naloxone |\n"
        "| ATB arthrite septique | **4-6 semaines** | Double, parentérale |\n"
        "| ATB spondylodiscite | **Min 6 semaines** | Rechercher endocardite |\n"
        "| S. aureus arthrite | **60%** | Germe le plus fréquent |\n"
        "| Spondylodiscite lombaire | **70%** | Localisation principale |\n"
        "| PPR corticothérapie | **0,2 mg/kg/j** | Soit 15-20 mg/j |\n"
        "| Horton corticothérapie | **0,7 mg/kg/j** | Bolus IV si complication |\n"
        "| T-score ostéoporose | **≤ -2,5** | DXA rachis + hanche |\n"
        "| Bisphosphonates si CTC | > 7,5 mg/j > **3 mois** | Ostéoporose cortico-induite |\n"
        "| Uricémie cible goutte | **< 360 µmol/L** | < 300 si sévère |\n"
        "| Infiltrations max/an | **4/site** | Articulaire ou péri-articulaire |\n"
    ))

    points_cles = [
        "La douleur est une expérience subjective : toujours évaluer et tracer (EVA/EN, DN4, HAD)",
        "Arthrite septique = **mono-arthrite brutale fébrile** : ponction articulaire + ATB en urgence (4-6 sem)",
        "Spondylodiscite : IRM en 1re intention, toujours rechercher une **endocardite** associée",
        "Horton : risque de **cécité** (NOIAA) → bolus IV immédiat si signes oculaires",
        "PPR non traitée évolue vers Horton dans **20-40%** des cas",
        "Ostéoporose : T-score ≤ -2,5, fracture sentinelle = **Pouteau-Colles** ~60 ans",
        "Goutte : cristaux d'UMS en aiguille, colchicine en 1re intention, allopurinol **à distance** de la crise",
        "Lombosciatique L5 = marche sur **talon** impossible ; S1 = marche sur **pointe** impossible",
        "Corticothérapie prolongée : prévention ostéoporose (vitD + Ca + bisphosphonates si > 7,5 mg/j > 3 mois)",
        "AINS : dose et durée **minimales**, CI grossesse > 6e mois, protection gastrique si terrain à risque",
    ]

    fiche_eclair_md = (
        "**Douleur** : aiguë < 3 mois (alarme) vs chronique > 3 mois (maladie). "
        "Nociceptive/neuropathique (DN4 > 4)/mixte. Paliers OMS I-II-III. "
        "Morphine : ordonnance sécurisée, prévention constipation, naloxone si surdosage.\n\n"
        "**Épaule** : coiffe des rotateurs (Neer/Yocum/Hawkins = souffrance ; Jobe/Patte = rupture). "
        "Capsulite rétractile : limitation active ET passive.\n\n"
        "**PR** : anti-CCP très spécifique, MTX en 1re ligne (tératogène+++), biothérapies en 2e. "
        "DAS28 pour le suivi. Risque CV augmenté.\n\n"
        "**Arthrite septique** : S. aureus 60%, mono-arthrite fébrile, ponction + ATB urgentes 4-6 sem. "
        "Spondylodiscite : IRM + rechercher endocardite.\n\n"
        "**Horton** : céphalées temporales + claudication mâchoire. BAT. Corticoïdes 0,7 mg/kg. "
        "NOIAA = urgence → bolus IV. PPR : 0,2 mg/kg, 18 mois.\n\n"
        "**Ostéoporose** : T-score ≤ -2,5. Pouteau-Colles ~60 ans, vertèbre ~70 ans, col fémoral ~80 ans. "
        "Bisphosphonates, tériparatide si > 2 FV. FRAX si pas de fracture.\n\n"
        "**Goutte** : UMS en aiguille, MTP gros orteil, colchicine 1re intention, "
        "allopurinol à distance de la crise, objectif uricémie < 360.\n\n"
        "**CCA** : PPCD courts/carrés, calcifications ménisques/carpe/pubis, AINS en 1re intention.\n\n"
        "**Lombosciatique** : L5 = talon, S1 = pointe. Gravité : paralysante, queue de cheval, hyperalgique. "
        "Chirurgie si signes gravité ou > 8 sem."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Rhumatologie",
        annee="2025-2026",
        item="Items 132, 196, 197, 198, 199, 124, 93, 94, 95, 326, 330, 195",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi, partie_vii],
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()

    # Images : charger depuis image_captions.json si disponible
    captions_file = PROJECT_ROOT / "output" / ".work" / "rhumatologie" / "image_captions.json"
    if captions_file.exists():
        try:
            captions = json.loads(captions_file.read_text(encoding="utf-8"))
            print(f"  Loaded {len(captions)} image captions")
        except Exception as e:
            print(f"  Image captions loading skipped: {e}")

    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Medecine_generale_rhumatologie_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out} ({pdf_out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()

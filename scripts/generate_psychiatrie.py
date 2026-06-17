"""Génère la fiche exhaustive de Psychiatrie à partir du texte source."""

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
from major_ecn.docx_generator import render_docx


def build_fiche() -> FicheData:
    plan = [
        PlanPartie(numero="I", titre="Trouble bipolaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et épidémiologie"),
            PlanSousPartie(lettre="B", titre="Syndrome maniaque"),
            PlanSousPartie(lettre="C", titre="Diagnostic et formes cliniques"),
            PlanSousPartie(lettre="D", titre="Prise en charge"),
            PlanSousPartie(lettre="E", titre="Pronostic et évolution"),
        ]),
        PlanPartie(numero="II", titre="Trouble dépressif", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et étiologies"),
            PlanSousPartie(lettre="B", titre="Sémiologie du syndrome dépressif"),
            PlanSousPartie(lettre="C", titre="Épisode dépressif caractérisé et formes cliniques"),
            PlanSousPartie(lettre="D", titre="Prise en charge"),
            PlanSousPartie(lettre="E", titre="Pronostic et évolution"),
        ]),
        PlanPartie(numero="III", titre="Conduites suicidaires", sous_parties=[
            PlanSousPartie(lettre="A", titre="Épidémiologie et définitions"),
            PlanSousPartie(lettre="B", titre="Facteurs de risque"),
            PlanSousPartie(lettre="C", titre="Crise suicidaire et évaluation"),
            PlanSousPartie(lettre="D", titre="Prise en charge et prévention"),
        ]),
        PlanPartie(numero="IV", titre="Urgences psychiatriques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Crise d'angoisse aiguë et trouble panique"),
            PlanSousPartie(lettre="B", titre="Agitation aiguë"),
        ]),
        PlanPartie(numero="V", titre="Addictions et alcoolisme", sous_parties=[
            PlanSousPartie(lettre="A", titre="Addictions : généralités"),
            PlanSousPartie(lettre="B", titre="Alcoolisme : clinique et biologie"),
            PlanSousPartie(lettre="C", titre="Complications neurologiques de l'alcool"),
            PlanSousPartie(lettre="D", titre="Complications hépatiques et autres"),
            PlanSousPartie(lettre="E", titre="Prise en charge de l'alcoolisme"),
        ]),
        PlanPartie(numero="VI", titre="Psychotropes et TCA", sous_parties=[
            PlanSousPartie(lettre="A", titre="Thymorégulateurs et lithium"),
            PlanSousPartie(lettre="B", titre="Anxiolytiques et hypnotiques"),
            PlanSousPartie(lettre="C", titre="Anorexie mentale"),
            PlanSousPartie(lettre="D", titre="Boulimie et hyperphagie boulimique"),
        ]),
    ]

    # ── PARTIE I : TROUBLE BIPOLAIRE ──
    partie_i = Partie(numero="I", titre="Trouble bipolaire", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et épidémiologie", rows=[
            FicheRow(concept="Épidémiologie", detail_md=(
                "- **Prévalence** : 1-4% population mondiale (jusqu'à 10% avec formes atténuées)\n"
                "- **Âge de début** : classiquement entre **15-25 ans**\n"
                "- **Sex-ratio** : H = F\n"
                "- 60% des sujets avec un 1er épisode maniaque ont déjà présenté un EDM\n"
                "- 90% des patients ayant eu un épisode maniaque présenteront d'autres troubles de l'humeur\n"
                "- **Retard diagnostic** : environ **10 ans**"
            )),
            FicheRow(concept="Étiologie", detail_md=(
                "- Maladie psychiatrique **sévère**, chronique et fréquente\n"
                "- Parmi les 10 maladies les plus invalidantes au plan mondial\n"
                "- Origine **multifactorielle** : facteurs génétiques et environnementaux"
            )),
            FicheRow(concept="", detail_md=(
                "- Le TBP est une maladie **chronique** nécessitant un traitement **thymorégulateur au long cours**\n"
                "- Retard diagnostic moyen de **10 ans** : toujours rechercher des ATCD d'hypomanie devant un EDM"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Syndrome maniaque", rows=[
            FicheRow(concept="Perturbation de l'affectivité", detail_md=(
                "- **Humeur** : gaie, expansive, exaltée, euphorie OU irritabilité\n"
                "- **Psychologie maniaque** :\n"
                "  - Augmentation estime de soi, idées de grandeur, **mégalomanie**\n"
                "  - Optimisme débordant, insouciance, ludisme\n"
                "  - **Désinhibition** comportementale et pulsionnelle :\n"
                "    - Achats pathologiques, voyages pathologiques\n"
                "    - Comportements agressifs, clastiques\n"
                "    - Usage de stupéfiants, comportements à risque\n"
                "- **Émotions** : labilité émotionnelle, hyperréactivité affective, **hypersyntonie**"
            )),
            FicheRow(concept="Accélération psychomotrice", detail_md=(
                "- **Accélération psychique** :\n"
                "  - **Tachypsychie** (accélération des idées)\n"
                "  - Pensée diffluente, fuite des idées\n"
                "  - **Coq-à-l'âne** : changement rapide d'une idée à l'autre sans lien\n"
                "- **Accélération motrice** :\n"
                "  - Agitation motrice, hyperactivité\n"
                "  - **Logorrhée** (augmentation temps de parole)\n"
                "  - **Tachyphémie** (augmentation vitesse de parole)\n"
                "  - Graphorrhée, hypermimie"
            )),
            FicheRow(concept="◆ Signes associés", detail_md=(
                "- **Insomnie** partielle/totale avec **réduction du besoin de sommeil**\n"
                "- Absence de sensation de fatigue, hypersthénie\n"
                "- **Anosognosie** partielle/totale\n"
                "- Hypervigilance, distractibilité, troubles attention\n"
                "- Anorexie/hyperphagie, amaigrissement, déshydratation\n"
                "- **Hypersexualité**, comportements sexuels à risque\n"
                "- Retentissement fonctionnel **majeur**"
            )),
        ]),
        SousPartie(lettre="C", titre="Diagnostic et formes cliniques", rows=[
            FicheRow(concept="Critères DSM-5 épisode maniaque", detail_md=(
                "- Période nettement délimitée avec **humeur élevée/expansive/irritable** + augmentation énergie\n"
                "- Durée > **1 semaine** (ou toute durée si hospitalisation nécessaire)\n"
                "- ≥ **3 symptômes** (ou 4 si humeur seulement irritable) parmi :\n"
                "  - Augmentation estime de soi / idées de grandeur\n"
                "  - Réduction du besoin de sommeil\n"
                "  - Logorrhée\n"
                "  - Fuite des idées\n"
                "  - Distractibilité\n"
                "  - Augmentation activité orientée vers un but / agitation\n"
                "  - Engagement excessif dans activités à risque\n"
                "- Altération marquée du fonctionnement et/ou nécessité hospitalisation\n"
                "- Non attribuable aux effets d'une substance"
            )),
            FicheRow(concept="◆ Syndrome hypomaniaque", detail_md=(
                "- Augmentation pathologique humeur et énergie pendant ≥ **4 jours**\n"
                "- Retentissement et symptomatologie **moins importants** que pour l'accès maniaque\n"
                "- Ne nécessite souvent **pas** d'hospitalisation"
            )),
            FicheRow(concept="Classification TBP", detail_md=(
                "| Type | Définition |\n"
                "|------|------------|\n"
                "| **Type I** | ≥ 1 épisode maniaque |\n"
                "| **Type II** | Épisodes hypomaniaques uniquement (jamais de manie) |\n"
                "| **Type III** | Virage maniaque/hypomaniaque sous antidépresseurs |\n"
            )),
            FicheRow(concept="◆ Formes cliniques particulières", detail_md=(
                "- **Avec caractéristiques psychotiques** : délire mégalomaniaque, mystique, prophétique\n"
                "- **Caractéristiques mixtes** : symptômes dépressifs au cours d'un épisode maniaque\n"
                "  - ⚠ Risque **très augmenté** de suicide\n"
                "- **Caractéristiques anxieuses** : risque augmenté de suicide, non réponse thérapeutique\n"
                "- **Furie maniaque** (rare) : agitation +++, idéation paranoïaque, hétéro-agressivité\n"
                "- **Cycles rapides** : > 4 épisodes en 12 mois, pronostic plus sévère"
            )),
            FicheRow(concept="Diagnostics différentiels", detail_md=(
                "- **Affections médicales** : tumeur cérébrale, SEP, AVC, Cushing, dysthyroïdie, hypoglycémie\n"
                "- **Toxiques** ++ : OH, cannabis, amphétamines, cocaïne, hallucinogènes\n"
                "- **Iatrogéniques** : corticoïdes, antidépresseurs, interféron-alpha\n"
                "- **DD psychiatriques** : trouble unipolaire, TDAH, trouble de la personnalité, schizophrénie"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours **éliminer une cause organique/toxique** avant de retenir un trouble psychiatrique\n"
                "- ⚠ Les **caractéristiques mixtes** (dépression + manie) majorent le risque suicidaire"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Prise en charge", rows=[
            FicheRow(concept="Phase aiguë (épisode maniaque)", detail_md=(
                "- **Hospitalisation en urgence** en psychiatrie milieu fermé sous contrainte (ASPDT)\n"
                "- Réhydratation, recherche systématique prise de toxiques\n"
                "- Éliminer cause médicale non psychiatrique\n"
                "- Recherche systématique MST\n"
                "- **Thymorégulateurs** le plus précocement possible :\n"
                "  - **Lithium** : traitement de référence\n"
                "  - Anticonvulsivant : divalproate de sodium\n"
                "  - Antipsychotique atypique : olanzapine, rispéridone, aripiprazole, quétiapine\n"
                "- Sauvegarde de justice si dépenses/achats excessifs\n"
                "- Prévention et surveillance risque suicidaire et hétéro-agressif"
            )),
            FicheRow(concept="◆ Sismothérapie (ECT)", detail_md=(
                "- Indications :\n"
                "  - Troubles dépressifs sévères/réfractaires\n"
                "  - État catatonique\n"
                "  - Épisode maniaque sévère et prolongé\n"
                "  - CI aux autres traitements\n"
                "  - Mauvaise tolérance des psychotropes"
            )),
            FicheRow(concept="Prise en charge au long cours", detail_md=(
                "- Ambulatoire +/- HDJ/CATTP\n"
                "- Poursuite traitement thymorégulateur **au long cours**\n"
                "- **Psychoéducation**\n"
                "- Psychothérapies : soutien, TCC, thérapies interpersonnelles, familiales\n"
                "- Remédiation cognitive\n"
                "- Prise en charge sociale : ALD 30, curatelle/tutelle selon cas\n"
                "- Suivi : poids, tour de taille, ECG, bilan lipidique, glycémie, ionogramme"
            )),
        ]),
        SousPartie(lettre="E", titre="Pronostic et évolution", rows=[
            FicheRow(concept="◆ Comorbidités", detail_md=(
                "| Comorbidité | Prévalence vie entière |\n"
                "|-------------|----------------------|\n"
                "| Addictions | 40-60% (OH 30-40%, cannabis 10-25%) |\n"
                "| Troubles anxieux | 40% (TP 15-25%, phobie sociale 10-20%) |\n"
                "| TDAH | 30% |\n"
                "| Troubles de la personnalité | 30% (surtout borderline) |\n"
                "| TCA | 15-30% |\n"
                "| TOC | 10-30% |\n"
            )),
            FicheRow(concept="Évolution", detail_md=(
                "- Prise en charge précoce et adaptée : **rémission** symptomatique et fonctionnelle possible\n"
                "- Si non/mal pris en charge :\n"
                "  - Cycles rapides\n"
                "  - **Suicide** (15%)\n"
                "  - Actes médico-légaux\n"
                "  - Désinsertion familiale, professionnelle et sociale"
            )),
        ]),
    ])

    # ── PARTIE II : TROUBLE DÉPRESSIF ──
    partie_ii = Partie(numero="II", titre="Trouble dépressif", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et étiologies", rows=[
            FicheRow(concept="Épidémiologie", detail_md=(
                "- **Prévalence ponctuelle** EDC : 5%\n"
                "- **Prévalence vie entière** : 11% hommes, **22% femmes**\n"
                "- OMS : 100 millions EDC/an dans le monde\n"
                "- Plus fréquent chez la femme à partir de l'adolescence (**2F/1H**)\n"
                "- Premier EDC possible à tout âge, pic juste avant 30 ans\n"
                "- **1re cause d'années de vie perdues** en bonne santé dans le monde"
            )),
            FicheRow(concept="◆ Étiologies secondaires", detail_md=(
                "- **Affections médicales dépressogènes** :\n"
                "  - Neurologiques : démence, Parkinson, SEP, AVC, tumeurs cérébrales\n"
                "  - Endocriniennes : **hypothyroïdie**, hypercorticisme\n"
                "  - Cancers, maladies de système, infections (BK, VIH)\n"
                "- **Iatrogéniques** : immunosuppresseurs (isotrétinoïne, IFN), corticoïdes au long cours, "
                "BB-, L-DOPA, antiHTA\n"
                "- **Toxiques** : OH, cannabis, cocaïne"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours rechercher une cause **organique** (hypothyroïdie, tumeur cérébrale) et "
                "**iatrogène/toxique** devant un EDC\n"
                "- ⚠ Ne pas confondre EDC et tristesse réactionnelle (deuil normal)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Sémiologie du syndrome dépressif", rows=[
            FicheRow(concept="Perturbation de l'affectivité", detail_md=(
                "- **Humeur triste** (symptôme majeur) :\n"
                "  - Sentiment pénible, douloureux, envahissant\n"
                "  - Peu accessible au réconfort\n"
                "  - Prédominance matinale, amélioration dans la journée\n"
                "- **Psychologie dépressive** (modification du contenu des pensées) :\n"
                "  - Passé : reconstruction négative\n"
                "  - Présent : **culpabilité**, dévalorisation, autodépréciation\n"
                "  - Avenir : **pessimisme**, incurabilité\n"
                "- **Émotions** : **anhédonie**, aboulie, anesthésie affective, irritabilité, douleur morale"
            )),
            FicheRow(concept="Ralentissement psychomoteur", detail_md=(
                "- **Ralentissement psychique** :\n"
                "  - **Bradypsychie** (ralentissement des idées)\n"
                "  - Ruminations (piétinement de la pensée)\n"
                "- **Ralentissement moteur** :\n"
                "  - Bradykinésie, **hypomimie**/amimie\n"
                "  - Bradyphémie, prosodie monocorde\n"
                "  - Clinophilie jusqu'à prostration, incurie\n"
                "  - **Aboulie** (incapacité à exécuter actes planifiés) ≠ apragmatisme\n"
                "- Expression la plus intense : **mélancolie stuporeuse** (mutisme + stupeur)\n"
                "- Ou au contraire **agitation** (déambulations, tension interne)"
            )),
            FicheRow(concept="◆ Signes associés", detail_md=(
                "- **Asthénie** : prédominance matinale/permanente\n"
                "- Troubles du sommeil : insomnie à type **réveils précoces** ++ ou hypersomnie\n"
                "- Modifications appétit/poids : anorexie ++ ou augmentation appétit\n"
                "- **Baisse libido**\n"
                "- **Idéation suicidaire** : attrait de la mort quasi constant\n"
                "- Symptômes cognitifs : difficultés de concentration, troubles de la mémoire\n"
                "- Possibles symptômes anxieux, possible délire congruent à l'humeur"
            )),
        ]),
        SousPartie(lettre="C", titre="Épisode dépressif caractérisé et formes cliniques", rows=[
            FicheRow(concept="★ Critères DSM-5 de l'EDC", detail_md=(
                "- Rupture avec état antérieur, ≥ **5 symptômes** sur ≥ **2 semaines** :\n"
                "  - **Humeur dépressive** (1/2 obligatoirement présent)\n"
                "  - **Diminution intérêt/plaisir** (1/2 obligatoirement présent)\n"
                "  - Perte/gain de poids significatif\n"
                "  - Insomnie/hypersomnie\n"
                "  - Agitation/ralentissement psychomoteur\n"
                "  - Fatigue/perte d'énergie\n"
                "  - Sentiment de dévalorisation/culpabilité\n"
                "  - Diminution concentration/indécision\n"
                "  - Pensées de mort récurrentes, idées suicidaires\n"
                "- Détresse cliniquement significative et/ou altération du fonctionnement\n"
                "- Non imputable aux effets d'une substance/affection médicale\n"
                "- Jamais eu d'épisode maniaque/hypomaniaque"
            )),
            FicheRow(concept="Mélancolie", detail_md=(
                "- **Anhédonie** et/ou anesthésie affective + ≥ 1 parmi :\n"
                "  - Humeur dépressive marquée avec désespoir, incurabilité\n"
                "  - **Réveils matinaux précoces**\n"
                "  - Agitation/ralentissement marqué (possible mutisme)\n"
                "  - Perte appétit/poids significative\n"
                "  - **Culpabilité excessive/inappropriée**"
            )),
            FicheRow(concept="◆ EDC avec caractéristiques psychotiques", detail_md=(
                "- Idées délirantes congruentes ou non à l'humeur\n"
                "- **Syndrome de Cotard** : forme particulière de mélancolie délirante :\n"
                "  - Idées de **négation d'organes**\n"
                "  - Négation du temps (immortalité) / négation du monde"
            )),
            FicheRow(concept="Autres formes cliniques", detail_md=(
                "| Forme | Caractéristiques principales |\n"
                "|-------|-----------------------------|\n"
                "| Mixte | Symptômes maniaques associés |\n"
                "| Atypique | Réactivité humeur, hypersomnie, hyperphagie, sensation de lourdeur |\n"
                "| Catatonique | Syndrome catatonique associé |\n"
                "| Anxieuse | Signes d'anxiété au premier plan |\n"
                "| Péri-partum | Début pendant grossesse ou jusqu'à 4 semaines post-partum |\n"
            )),
            FicheRow(concept="◆ Intensité de l'EDC", detail_md=(
                "- **Léger** : symptômes juste suffisants au diagnostic, peu de retentissement\n"
                "- **Moyen** : plus de symptômes que nécessaire, retentissement modéré\n"
                "- **Sévère** : quasiment tous les symptômes, retentissement social majeur\n"
                "- Échelles d'aide : **MADRS**, HDRS"
            )),
            FicheRow(concept="◆ Troubles dépressifs", detail_md=(
                "- **EDC isolé** : présence d'un seul EDC\n"
                "- **Trouble dépressif récurrent** : ≥ 2 EDC séparés par > 2 mois\n"
                "- **Trouble dépressif persistant** (dysthymie) : humeur dépressive la majorité des jours > **2 ans**\n"
                "- Trouble dysphorique prémenstruel\n"
                "- Trouble dépressif induit par substance/médicament"
            )),
        ]),
        SousPartie(lettre="D", titre="Prise en charge", rows=[
            FicheRow(concept="Indications d'hospitalisation", detail_md=(
                "- EDC **sévère**, formes mélancoliques/psychotiques/atypiques\n"
                "- **Risque suicidaire élevé**\n"
                "- Comorbidités psychiatriques (addiction, trouble anxieux sévère)\n"
                "- Isolement sociofamilial\n"
                "- Résistance actuelle/passée au traitement\n"
                "- Âges extrêmes de la vie (sujet jeune, sujet âgé)"
            )),
            FicheRow(concept="Traitement médicamenteux", detail_md=(
                "- **Antidépresseur** : indiqué dans les formes modérées/sévères\n"
                "  - **ISRS en 1re intention**, augmenté progressivement\n"
                "  - Délai d'action : **3-4 semaines**\n"
                "  - Durée : **6 mois-1 an** après rémission (1er EDC)\n"
                "  - Trouble dépressif récurrent : traitement de maintien prolongé\n"
                "  - **Résistance** : échec de 2 antidépresseurs à dose efficace ≥ 6 semaines chacun\n"
                "- +/- BZP transitoire (en attente efficacité antidépresseur)\n"
                "- +/- Antipsychotique si caractéristiques psychotiques"
            )),
            FicheRow(concept="", detail_md=(
                "- Le traitement antidépresseur a un **délai d'action de 3-4 semaines** : ne pas conclure "
                "à un échec avant ce délai\n"
                "- Poursuivre le traitement au minimum **6 mois après rémission** pour prévenir les rechutes"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Psychothérapies", detail_md=(
                "- **Psychothérapie de soutien** : toujours indiquée\n"
                "- En **monothérapie** pour EDC léger\n"
                "- En association au traitement médicamenteux pour EDC moyen/sévère\n"
                "- Options : TCC, psychothérapie d'inspiration psychanalytique, thérapie familiale, "
                "thérapie interpersonnelle"
            )),
            FicheRow(concept="◆ ECT (sismothérapie)", detail_md=(
                "- Formes mélancoliques/psychotiques\n"
                "- Résistance au traitement médicamenteux\n"
                "- CI au traitement médicamenteux\n"
                "- Nombre de séances : **12** (2-3/semaine)\n"
                "- EI principaux : troubles mnésiques ++ réversibles, céphalées"
            )),
        ]),
        SousPartie(lettre="E", titre="Pronostic et évolution", rows=[
            FicheRow(concept="Évolution", detail_md=(
                "- **Guérison** : rémission complète > 4 mois\n"
                "- Récurrence, rémission partielle, chronicisation, résistance\n"
                "- Comorbidités : anxieuses (50-70%), addictives (30%), TCA, troubles de la personnalité"
            )),
            FicheRow(concept="Facteurs de mauvais pronostic", detail_md=(
                "- Sexe féminin, ATCD familiaux de troubles de l'humeur\n"
                "- Âge de début précoce\n"
                "- Nombre d'épisodes passés élevé\n"
                "- Persistance de symptômes résiduels dépressifs\n"
                "- Présence de comorbidités psychiatriques ou non"
            )),
            FicheRow(concept="Mesures sociales", detail_md=(
                "- EDC : arrêt de travail pendant la durée du handicap fonctionnel\n"
                "- Troubles dépressifs récurrents : **ALD 23** avec prise en charge 100%\n"
                "- Éducation du patient"
            )),
        ]),
    ])

    # ── PARTIE III : CONDUITES SUICIDAIRES ──
    partie_iii = Partie(numero="III", titre="Conduites suicidaires", sous_parties=[
        SousPartie(lettre="A", titre="Épidémiologie et définitions", rows=[
            FicheRow(concept="Suicide", detail_md=(
                "- **Incidence** : 10-11 000/an en France, taux 16/100 000\n"
                "- **3e cause de mortalité prématurée** en France\n"
                "- **2e cause de mortalité** chez les 15-34 ans (1re chez 25-30 ans)\n"
                "- Prédominance **masculine** (SR = 3)\n"
                "- Taux maximal pour les **hommes > 85 ans**\n"
                "- Modes (H) : pendaison > armes à feu > IMV > noyade > chute\n"
                "- Modes (F) : IMV et pendaison > noyade > chute > armes à feu"
            )),
            FicheRow(concept="Tentative de suicide", detail_md=(
                "- **Incidence** : 180 000/an\n"
                "- Prévalence vie entière : 5,5%\n"
                "- Prédominance **féminine** (SR = 4)\n"
                "- Prédominance sujets jeunes (15-35 ans)\n"
                "- Mode principal : **IMV** (90%)\n"
                "- **Risque de récidive : 40%** (mortalité dans l'année suivant TS : 1%)"
            )),
            FicheRow(concept="Idées suicidaires", detail_md=(
                "- Prévalence vie entière : **15%**, 3,9% sur 12 derniers mois\n"
                "- Prévalence 15-19 ans : 23% H / 41% F\n"
                "- 40% de passage à l'acte si idées récurrentes"
            )),
        ]),
        SousPartie(lettre="B", titre="Facteurs de risque", rows=[
            FicheRow(concept="FDR primaires (forte valeur prédictive)", detail_md=(
                "- **Trouble psychiatrique** :\n"
                "  - Dépression (**15%** de décès par suicide)\n"
                "  - Schizophrénie (**10%**)\n"
                "  - Alcoolisme, troubles anxieux, personnalités pathologiques\n"
                "- ATCD personnels de TS (10% de décès par suicide si ATCD TS)\n"
                "- ATCD familiaux de TS et suicide\n"
                "- Faible estime de soi\n"
                "- **Impulsivité**, rigidité de pensée, colère, agressivité\n"
                "- Intention suicidaire clairement exprimée"
            )),
            FicheRow(concept="FDR secondaires et tertiaires", detail_md=(
                "- **Secondaires** (faible valeur prédictive seuls) :\n"
                "  - Perte parentale précoce, difficultés financières\n"
                "  - Isolement social, événements de vie négatifs, chômage\n"
                "- **Tertiaires** (pas de valeur prédictive seuls) :\n"
                "  - Sexe masculin\n"
                "  - Périodes à risque (fêtes, période prémenstruelle)\n"
                "  - Adolescent et sujet âgé"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ **Syndrome pré-suicidaire de Ringel** : calme apparent, attitude de retrait, diminution "
                "de la réactivité émotionnelle = envahissement par les idéations suicidaires\n"
                "- ⚠ Ne pas être faussement rassuré par un patient qui semble « aller mieux »"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Crise suicidaire et évaluation", rows=[
            FicheRow(concept="Crise suicidaire", detail_md=(
                "- Crise psychique avec expression d'idées et intentions suicidaires\n"
                "- Ressources adaptatives de l'individu **épuisées**\n"
                "- Caractère **réversible** et **temporaire**\n"
                "- Signes évocateurs : rupture avec état antérieur, verbalisations suicidaires, "
                "détresse, isolement, usage inhabituel d'OH/stupéfiants"
            )),
            FicheRow(concept="Évaluation du risque suicidaire", detail_md=(
                "| Urgence | Caractéristiques |\n"
                "|---------|------------------|\n"
                "| **Faible** | Bonne alliance, recherche solutions, pas de scénario précis |\n"
                "| **Moyenne** | Isolé, exprime désarroi, scénario reporté, équilibre fragile |\n"
                "| **Élevée** | Très isolé, accès direct au moyen, passage à l'acte planifié, coupé de ses émotions |\n"
            )),
            FicheRow(concept="◆ Spécificités selon l'âge", detail_md=(
                "- **Enfant** : verbalisation rare, signes indirects (dessins morbides, plaintes somatiques, "
                "isolement, troubles apprentissage)\n"
                "- **Adolescent** : verbalisation fréquente, fléchissement scolaire, conduites à risque, "
                "anorexie/boulimie, fugues\n"
                "- **Sujet âgé** : verbalisation rare, désinvestissement hobbies, prostration, "
                "refus de s'alimenter, refus de soins"
            )),
        ]),
        SousPartie(lettre="D", titre="Prise en charge et prévention", rows=[
            FicheRow(concept="Entretien psychiatrique", detail_md=(
                "- Endroit calme, en toute confidentialité, en face à face\n"
                "- D'abord laisser libre cours à l'expression des affects\n"
                "- Aborder le sujet des idées suicidaires : questions simples, sans ambiguïté\n"
                "- Évaluation du risque suicidaire immédiat\n"
                "- Examen médical complet\n"
                "- Entretien avec l'entourage"
            )),
            FicheRow(concept="Orientation", detail_md=(
                "- **Hospitalisation** :\n"
                "  - Urgence élevée +++\n"
                "  - Facilement si enfant/adolescent\n"
                "  - Libre ou SPDT\n"
                "  - Mesures de prévention : suppression points d'appui, inventaire des affaires, "
                "retrait objets dangereux\n"
                "  - ⚠ 5% des suicides en établissements de soins\n"
                "- **Ambulatoire** : RDV au bout de quelques jours, entourage proche et disponible"
            )),
            FicheRow(concept="Prévention", detail_md=(
                "- **Primaire** : suppression facteurs de risque et de décompensation\n"
                "- **Secondaire** : dépistage précoce de la crise suicidaire\n"
                "- **Tertiaire** : prise en charge des suicidants\n"
                "- Acteurs : médecine scolaire, médecine du travail, généraliste, spécialiste, "
                "réseaux d'écoute"
            )),
        ]),
    ])

    # ── PARTIE IV : URGENCES PSYCHIATRIQUES ──
    partie_iv = Partie(numero="IV", titre="Urgences psychiatriques", sous_parties=[
        SousPartie(lettre="A", titre="Crise d'angoisse aiguë et trouble panique", rows=[
            FicheRow(concept="Attaque de panique", detail_md=(
                "- **Prévalence vie entière** : 3-5%, SR : 1H/2F, adulte jeune\n"
                "- Début **brutal**, durée 20-30 min, décroissance progressive\n"
                "- **3 types de symptômes** :\n"
                "  - **Physiques** : cardiaques, respiratoires, neurovégétatifs, digestifs\n"
                "  - **Psychiques** : peur intense, pensées catastrophistes, "
                "déréalisation/dépersonnalisation\n"
                "  - **Comportementaux** : agitation à la prostration"
            )),
            FicheRow(concept="Trouble panique", detail_md=(
                "- Répétition d'AP survenant de manière **imprévisible** (sans facteur déclenchant)\n"
                "- Développement d'une **anxiété anticipatoire**\n"
                "- Principale complication (rare mais grave) : **passage à l'acte auto-agressif**"
            )),
            FicheRow(concept="", detail_md=(
                "- Toujours **éliminer une urgence somatique non psychiatrique** +++ (PMZ)\n"
                "- Toujours **éliminer une intoxication** à une substance psychoactive ou un **sevrage**"
            ), kind="a_retenir"),
            FicheRow(concept="PEC en urgence", detail_md=(
                "- **Non pharmacologique** :\n"
                "  - Mise en condition (calme, empathie)\n"
                "  - Réassurance (donner le diagnostic, pas de danger de mort)\n"
                "  - Mesures de contrôle respiratoire\n"
                "  - Éducation thérapeutique et RHD\n"
                "- **Pharmacologique** :\n"
                "  - **BZD PO** (ponctuel, pas au long cours, attention dépendance)\n"
                "  - Ou **hydroxyzine**"
            )),
        ]),
        SousPartie(lettre="B", titre="Agitation aiguë", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- État de tension et hyperactivité physique et psychique\n"
                "- Augmentation brutale, incontrôlée et imprévisible de l'activité motrice\n"
                "- Si bris d'objets : **crise clastique**\n"
                "- Représente **10-15%** des consultations psychiatriques aux urgences"
            )),
            FicheRow(concept="Étiologies selon le terrain", detail_md=(
                "| Terrain | 1re intention | 2e intention |\n"
                "|---------|--------------|-------------|\n"
                "| **Sujet âgé** | Iatrogénie (BZP, ATD, corticoïdes), dysnatrémie, hypercalcémie, "
                "dysthyroïdie, hypoglycémie, AVC, HSD | Infection (urinaire, pulmonaire), "
                "globe vésical, fécalome, intoxication OH |\n"
                "| **Adulte jeune** | Toxiques ++ (OH, cannabis, psychostimulants), "
                "iatrogénie, hypoglycémie, méningo-encéphalite | AP/TP, épisode maniaque, "
                "EDC, trouble psychotique bref |\n"
                "| **ATCD psy** | Iatrogénie (virage sous ATD, syndrome sérotoninergique, "
                "effet paradoxal BZP) | Décompensation trouble psychiatrique connu |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours **éliminer une étiologie non psychiatrique** en priorité, même chez un "
                "patient avec ATCD psychiatriques"
            ), kind="piege"),
            FicheRow(concept="PEC en urgence", detail_md=(
                "- **Hospitalisation** en urgence (libre ou sous contrainte)\n"
                "- Contact verbal, environnement calme\n"
                "- Prévention risque auto/hétéro-agressif\n"
                "- **Contention** en dernier recours :\n"
                "  - Prescription médicale, personnel > 4, matériel homologué\n"
                "  - Accompagnée d'une sédation médicamenteuse\n"
                "  - Si > 24h : **anticoagulation préventive**\n"
                "- Examen clinique complet : constantes, recherche syndrome confusionnel"
            )),
            FicheRow(concept="◆ Examens complémentaires", detail_md=(
                "- **Systématiques** : NFS, glycémie, ionogramme, calcémie\n"
                "- Hémostase si injection IM, **ECG** si neuroleptique sédatif\n"
                "- **Selon contexte** : alcoolémie, toxiques, BHC, TSH, PL, TDM cérébral, EEG"
            )),
            FicheRow(concept="Traitement médicamenteux", detail_md=(
                "- Traitement étiologique si cause non psychiatrique\n"
                "- Toujours **privilégier la voie PO** +++\n"
                "- **BZD demi-vie courte** ou anxiolytique autre : oxazépam, hydroxyzine\n"
                "  - CI en urgence : insuffisance respiratoire, myasthénie\n"
                "  - Si refus PO et voie IM nécessaire : éviter BZP\n"
                "- **Neuroleptiques sédatifs** si agitation très sévère :\n"
                "  - Cyamémazine, lévomépromazine, loxapine\n"
                "  - Toujours privilégier la **monothérapie**"
            )),
        ]),
    ])

    # ── PARTIE V : ADDICTIONS ET ALCOOLISME ──
    partie_v = Partie(numero="V", titre="Addictions et alcoolisme", sous_parties=[
        SousPartie(lettre="A", titre="Addictions : généralités", rows=[
            FicheRow(concept="Abus de substance", detail_md=(
                "- Mode d'utilisation inadéquat entraînant souffrance cliniquement significative\n"
                "- ≥ 1 manifestation parmi :\n"
                "  - Incapacité à remplir des obligations\n"
                "  - Utilisation dans des circonstances physiquement dangereuses\n"
                "  - Problèmes judiciaires liés à la substance\n"
                "  - Utilisation malgré problèmes interpersonnels persistants\n"
                "- ⚠ On ne peut avoir **à la fois** une dépendance et un abus"
            )),
            FicheRow(concept="Dépendance", detail_md=(
                "- ≥ **3 critères** parmi :\n"
                "  - **Tolérance** (besoin de quantités croissantes)\n"
                "  - **Sevrage** (syndrome clinique de sevrage)\n"
                "  - Prise en quantité plus importante que prévu\n"
                "  - Efforts infructueux pour diminuer\n"
                "  - Temps important consacré à se procurer/consommer\n"
                "  - Abandon d'activités sociales/professionnelles/loisirs\n"
                "  - Poursuite malgré connaissance du problème\n"
                "- **Toujours rechercher une co-addiction** systématiquement"
            )),
        ]),
        SousPartie(lettre="B", titre="Alcoolisme : clinique et biologie", rows=[
            FicheRow(concept="Seuils OMS", detail_md=(
                "- **Calcul** : quantité (g) = volume OH (dL) x degré OH x 0,8\n"
                "- **Seuils** :\n"
                "  - Homme : **30 g/j** (< 21 verres/semaine)\n"
                "  - Femme : **20 g/j** (< 14 verres/semaine)\n"
                "  - Pas plus de **40 g en une fois** (< 4 verres/occasion)\n"
                "  - Au moins 1 jour d'abstention/semaine\n"
                "  - Pas d'OH : grossesse, conduite, médicaments"
            )),
            FicheRow(concept="◆ Signes cliniques", detail_md=(
                "- Télangiectasies faciales (pommettes, oreilles, ailes du nez)\n"
                "- Hyperhémie/ictère conjonctival, haleine particulière\n"
                "- Bouffissure du visage, amaigrissement\n"
                "- **Tremblement** (imprégnation et/ou sevrage)\n"
                "- Hypertrophie parotidienne, maladie de **Dupuytren**\n"
                "- Signes de dépendance : tremblement mains + langue, myalgies, sueurs, tachycardie, "
                "HTA, crises convulsives"
            )),
            FicheRow(concept="Marqueurs biologiques", detail_md=(
                "| Marqueur | Spécificité |\n"
                "|----------|------------|\n"
                "| **Gamma-GT** augmentée | 80% |\n"
                "| **CDT** augmentée | **90%** |\n"
                "| **VGM** augmenté | 50% |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- La **CDT** (transferrine désialylée) est le marqueur le plus **spécifique** (90%) "
                "de la consommation chronique d'alcool\n"
                "- Dépistage par tests **AUDIT-C** et **DETA-CAGE**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Complications neurologiques de l'alcool", rows=[
            FicheRow(concept="Intoxication aiguë", detail_md=(
                "- **Ivresse simple** : jovialité, dysarthrie, désinhibition, troubles cérébelleux\n"
                "- **Ivresse pathologique** : agressivité, violences, +/- hallucinations et délire, "
                "suivie d'amnésie lacunaire\n"
                "- **Coma éthylique** (alcoolémie > 3 g/L) :\n"
                "  - Coma calme, hypotonique, sans signes de localisation\n"
                "  - **Mydriase bilatérale** symétrique peu réactive\n"
                "  - Hypothermie, bradycardie, hypotension\n"
                "  - Rechercher : hypoglycémie, acidocétose, hyponatrémie"
            )),
            FicheRow(concept="★ Délirium tremens", detail_md=(
                "- Survient **12-48h** après sevrage\n"
                "- **Pré-DT** : inversion rythme nycthéméral, cauchemars, irritabilité, anxiété, "
                "sueurs, tremblement postural\n"
                "- **DT** :\n"
                "  - **Syndrome confuso-onirique** : propos incohérents, DTS, agitation, "
                "hallucinations visuelles (**zoopsies**), scènes d'agression\n"
                "  - **Syndrome physique** : fièvre, sueurs, tremblements généralisés, "
                "tachycardie, déshydratation\n"
                "  - Crises d'épilepsie possibles"
            )),
            FicheRow(concept="Traitement du DT", detail_md=(
                "- Hydratation adaptée avec surveillance diurèse\n"
                "- **Vitamines B1, B6, PP**\n"
                "- Correction hypokaliémie\n"
                "- **BZD IV** : diazépam 10 mg/h (ou **lorazépam** si IHC)\n"
                "- Correction hyperthermie\n"
                "- Traitement des facteurs favorisants\n"
                "- Disposer d'un antidote des BZP : **flumazénil**"
            )),
            FicheRow(concept="★ Encéphalopathie de Gayet-Wernicke", detail_md=(
                "- Carence en **vitamine B1**, parfois induite par apport glucidique\n"
                "- Triade : **syndrome confusionnel** + **signes oculomoteurs** (paralysie, nystagmus) "
                "+ **syndrome cérébelleux statique**\n"
                "- Diagnostic : dosage vitamine B1 effondré, IRM (hypersignal FLAIR corps mamillaires)\n"
                "- Traitement : **vitamine B1 IV en urgence**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Ne **JAMAIS** administrer de glucose IV chez un patient alcoolique/dénutri sans "
                "avoir donné de la **vitamine B1** au préalable (risque d'encéphalopathie de Gayet-Wernicke)"
            ), kind="piege"),
            FicheRow(concept="★ ◆ Syndrome de Korsakoff", detail_md=(
                "- Conséquence d'une encéphalopathie de Gayet-Wernicke mal/non traitée\n"
                "- **Amnésie antérograde** + fausses reconnaissances + **fabulations** + **anosognosie**\n"
                "- Traitement : vitamines parentérales (peu efficace)"
            )),
            FicheRow(concept="Myélinolyse centropontine", detail_md=(
                "- Favorisée par l'hyponatrémie et sa **correction trop rapide**\n"
                "- Trouble de la vigilance, tétraplégie, signes pseudobulbaires\n"
                "- IRM : hypersignal T2/FLAIR du centre de la protubérance"
            )),
        ]),
        SousPartie(lettre="D", titre="Complications hépatiques et autres", rows=[
            FicheRow(concept="Stéatose hépatique", detail_md=(
                "- Accumulation de lipides (TG) dans les hépatocytes\n"
                "- **Réversible** en quelques semaines après arrêt OH\n"
                "- Souvent **asymptomatique**, +/- HMG à bord inférieur mousse\n"
                "- Échographie : foie hyperéchogène, « **brillant** »\n"
                "- Jamais de PBH pour simple stéatose"
            )),
            FicheRow(concept="Hépatite alcoolique aiguë", detail_md=(
                "- Forme symptomatique : AEG, douleurs HCD, fièvre, ictère\n"
                "- Biologie : hyperleucocytose à PNN, cytolyse modérée avec **ASAT/ALAT > 1**, "
                "augmentation gamma-GT\n"
                "- **Score de Maddrey > 32** = HAA grave : PBH + **corticothérapie** 40 mg/j\n"
                "- Peut se compliquer de **décompensation de cirrhose**"
            )),
            FicheRow(concept="◆ Autres complications", detail_md=(
                "- **Pancréatiques** : PA, PC\n"
                "- **Digestives** : diarrhée, RGO, gastrite\n"
                "- **CV** : TDR, cardiomyopathies\n"
                "- **Métaboliques** : dyslipidémie, diabète, hypoglycémies\n"
                "- **Cancers** : VADS, CE œsophage, CHC\n"
                "- **Génitales** : baisse libido, impuissance, gynécomastie (H), aménorrhée\n"
                "- **Syndrome alcoolique fœtal**"
            )),
        ]),
        SousPartie(lettre="E", titre="Prise en charge de l'alcoolisme", rows=[
            FicheRow(concept="Sevrage", detail_md=(
                "- Entretien motivationnel initial\n"
                "- Ambulatoire ou hospitalier\n"
                "- **Hydratation** 3 L/j PO/IV\n"
                "- **Vitamines B1, B6, PP**\n"
                "- **BZD PO** : diazépam (ou oxazépam si IHC), posologies décroissantes sur 1-2 semaines\n"
                "- Psychothérapie de soutien et entretiens motivationnels"
            )),
            FicheRow(concept="◆ Prise en charge au long cours", detail_md=(
                "- **Médicale** :\n"
                "  - **Acamprosate**\n"
                "  - **Naltrexone** (CI si addiction opiacés)\n"
                "  - Disulfiram (effet antabuse, de moins en moins utilisé)\n"
                "- **Psychologique** :\n"
                "  - Psychothérapie de soutien\n"
                "  - Entretiens motivationnels\n"
                "  - TCC : stratégies de maintien de l'abstinence\n"
                "- **Sociale** : réinsertion sociale et professionnelle, associations, foyers"
            )),
        ]),
    ])

    # ── PARTIE VI : PSYCHOTROPES ET TCA ──
    partie_vi = Partie(numero="VI", titre="Psychotropes et TCA", sous_parties=[
        SousPartie(lettre="A", titre="Thymorégulateurs et lithium", rows=[
            FicheRow(concept="Lithium : pharmacocinétique", detail_md=(
                "- Voie PO, équilibre atteint en **5-8 jours**\n"
                "- Pas de liaison aux protéines\n"
                "- Passage placentaire et dans le lait maternel\n"
                "- Demi-vie : **18-30h**\n"
                "- Excrétion **rénale**\n"
                "- Compétition ions lithium/sodium au niveau du tubule proximal"
            )),
            FicheRow(concept="CI absolues du lithium", detail_md=(
                "- **Insuffisance rénale** (clairance < 85 mL/min)\n"
                "- Déplétion hydrosodée, hyponatrémie, régime sans sel\n"
                "- Coronaropathie sévère, insuffisance cardiaque instable\n"
                "- Association aux **salidiurétiques**\n"
                "- **Allaitement**\n"
                "- CI relative : grossesse (risque **cardiopathie d'Ebstein** au T1)"
            )),
            FicheRow(concept="Interactions médicamenteuses du lithium", detail_md=(
                "| Effet | Médicaments |\n"
                "|-------|------------|\n"
                "| **Majoration lithiémie** | AINS, diurétiques, IEC, métronidazole, cyclines |\n"
                "| **Diminution lithiémie** | Théophylline, corticoïdes, mannitol |\n"
                "| **Neurotoxicité** | Association lithium + halopéridol |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- La lithiémie doit être contrôlée **12h après la dernière prise**\n"
                "- Objectif : forme LI = **0,5-0,8 mEq/L**, forme LP = **0,8-1,2 mEq/L**\n"
                "- Bilan rénal et thyroïdien **1/an**"
            ), kind="a_retenir"),
            FicheRow(concept="◆ EI du lithium", detail_md=(
                "- **Neuropsychiques** : tremblements ++, asthénie, troubles cognitifs\n"
                "- **Endocriniens** : prise de poids, **hypothyroïdie**, goitre\n"
                "- **Rénaux** : syndrome polyuro-polydipsique, syndrome néphrotique (GEM), "
                "néphropathie tubulo-interstitielle\n"
                "- **Digestifs** : nausées, goût métallique, diarrhée\n"
                "- **CV** : troubles de conduction/repolarisation\n"
                "- **Dermatologiques** : acné, psoriasis, alopécie"
            )),
            FicheRow(concept="◆ Anticonvulsivants thymorégulateurs", detail_md=(
                "- **Carbamazépine** : inducteur enzymatique ++\n"
                "- **Valproate**, valpromide\n"
                "- Métabolisme hépatique, passage placentaire\n"
                "- Surveillance : NFS, BHC dont TP"
            )),
        ]),
        SousPartie(lettre="B", titre="Anxiolytiques et hypnotiques", rows=[
            FicheRow(concept="BZD : propriétés", detail_md=(
                "- Agonistes récepteurs **GABA** facilitant la transmission GABAergique\n"
                "- **6 propriétés** : anxiolytiques, sédatives, anticonvulsivantes, myorelaxantes, "
                "amnésiantes, orexigènes"
            )),
            FicheRow(concept="BZD : classification", detail_md=(
                "| Type | Molécule | Nom commercial | Demi-vie |\n"
                "|------|----------|---------------|----------|\n"
                "| Demi-vie courte | Oxazépam | Séresta | 8h |\n"
                "| | Alprazolam | Xanax | 10-20h |\n"
                "| | Lorazépam | Témesta | 10-20h |\n"
                "| Demi-vie intermédiaire | Bromazépam | Lexomil | 20h |\n"
                "| Demi-vie longue | Diazépam | Valium | 47-92h |\n"
                "| | Prazépam | Lysanxia | 30-150h |\n"
            )),
            FicheRow(concept="BZD : CI", detail_md=(
                "- **Absolues** : insuffisance respiratoire sévère, insuffisance hépatique sévère, "
                "syndrome d'apnée du sommeil, **myasthénie**, ATCD réaction paradoxale\n"
                "- **Relatives** : grossesse et allaitement, IH (préférer **oxazépam**), IR, "
                "ATCD toxicomanie, précaution chez le sujet âgé"
            )),
            FicheRow(concept="BZD : EI", detail_md=(
                "| EI | Description |\n"
                "|-----|------------|\n"
                "| **Sédation** | Somnolence diurne, asthénie, altération vigilance (potentialisée par OH) |\n"
                "| **Troubles cognitifs** | Troubles mnésiques, attention, confusion (sujet âgé) |\n"
                "| **Réactions paradoxales** | Agitation, désinhibition, auto/hétéro-agressivité |\n"
                "| **Pharmacodépendance** | Tolérance et dépendance |\n"
                "| Rebond anxiété | À l'arrêt du traitement |\n"
            )),
            FicheRow(concept="RMO anxiolytiques", detail_md=(
                "- Ne pas associer **2 anxiolytiques**\n"
                "- Durée maximale : **4-12 semaines**\n"
                "- Débuter par la posologie la plus faible\n"
                "- Ne pas reconduire systématiquement sans réévaluation\n"
                "- Arrêt **progressif** sur quelques semaines à plusieurs mois"
            )),
            FicheRow(concept="◆ Autres anxiolytiques", detail_md=(
                "- **Hydroxyzine** (Atarax) : antiH1, moins de dépendance que BZD, "
                "effets anticholinergiques, CI : GAFA, adénome prostatique\n"
                "- **Buspirone** : action retardée (1 semaine), pas de dépendance, CI : association IMAO\n"
                "- **BB-** (propranolol) : anxiété de performance, effet périphérique\n"
                "- Apparentés BZD (hypnotiques) : **zopiclone** (Imovane), **zolpidem** (Stilnox)"
            )),
        ]),
        SousPartie(lettre="C", titre="Anorexie mentale", rows=[
            FicheRow(concept="Épidémiologie", detail_md=(
                "- Prévalence : **0,9-1,5%** femmes, 0,2-0,3% hommes (SR = 1H/8F)\n"
                "- Début entre **15-25 ans** (90%)\n"
                "- Populations à risque : adolescentes, mannequins, danseurs, sportifs\n"
                "- Dépistage : tests **SCOFF**, EAT, IDE"
            )),
            FicheRow(concept="Triade diagnostique (DSM)", detail_md=(
                "- **Restriction alimentaire** avec refus de maintenir un poids normal\n"
                "- **Peur intense** de prendre du poids malgré insuffisance pondérale\n"
                "- **Dysmorphophobie** : altération de la perception du corps, déni de la maigreur\n"
                "- Aménorrhée secondaire ≥ 3 cycles (critère DSM-IV, disparu dans DSM-5)"
            )),
            FicheRow(concept="◆ Conduites associées", detail_md=(
                "- **Vomissements provoqués** +++\n"
                "- Prise de laxatifs, diurétiques\n"
                "- Hyperactivité physique, exposition au froid\n"
                "- Potomanie (risque hyponatrémie et convulsions)\n"
                "- Anosognosie, surinvestissement intellectuel"
            )),
            FicheRow(concept="Retentissement somatique", detail_md=(
                "- **Hématologique** : anémie (15%), thrombopénie, leucopénie\n"
                "- **Hydro-électrolytique** : hyponatrémie, **hypokaliémie**, hypocalcémie\n"
                "- **CV** : bradycardie, hypotension, troubles du rythme\n"
                "- **Osseux** : **ostéoporose**\n"
                "- **Digestif** : brûlures œsophagiennes, hypertrophie parotidienne, érosions dentaires\n"
                "- Insuffisance rénale fonctionnelle, hypoglycémie\n"
                "- **Infertilité**"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ **Refeeding syndrome** lors d'une renutrition trop rapide :\n"
                "  - Cytolyse hépatique, troubles de l'hémostase\n"
                "  - **Hypophosphorémie**\n"
                "  - Troubles du rythme cardiaque\n"
                "- Renutrition toujours **prudente et progressive**"
            ), kind="piege"),
            FicheRow(concept="◆ Critères d'hospitalisation (sélection)", detail_md=(
                "- Perte poids > **20%** en 3 mois\n"
                "- Fc < **40 bpm**, hypothermie < **35 C**, TA < 90/60\n"
                "- Hypokaliémie < **3 mEq/L**, hyponatrémie < 125\n"
                "- Hypoglycémie symptomatique < 0,6 g/L\n"
                "- ASAT/ALAT > 10N\n"
                "- Risque suicidaire, comorbidités psychiatriques sévères"
            )),
            FicheRow(concept="Pronostic", detail_md=(
                "- Règle des **1/3** : 1/3 aggravation/décès, 1/3 chronicité, 1/3 évolution favorable\n"
                "- Comorbidités : dépression (60-80%), TOC, phobie sociale, addictions\n"
                "- Facteurs de mauvais pronostic : délai avant PEC, âge tardif, déni persistant, "
                "vomissements, poids très faible, comorbidités psychiatriques"
            )),
        ]),
        SousPartie(lettre="D", titre="Boulimie et hyperphagie boulimique", rows=[
            FicheRow(concept="Boulimie", detail_md=(
                "- **Terrain** : femme jeune (10-19 ans), prévalence 1,5% femmes / 0,5% hommes\n"
                "- **Crise boulimique** :\n"
                "  - Craving initial (sensation irréductible de faim)\n"
                "  - Absorption massive d'aliments hypercaloriques en temps restreint\n"
                "  - Sentiment intense de honte et culpabilité\n"
                "  - Conscience douloureuse du trouble\n"
                "- Vomissements provoqués, prise laxatifs/diurétiques\n"
                "- **Poids souvent normal** (≠ anorexie)\n"
                "- Diagnostic : crises > **2/semaine** pendant > **3 mois** + comportements compensatoires"
            )),
            FicheRow(concept="◆ Hyperphagie boulimique", detail_md=(
                "- Prévalence vie entière : **3-5%**, SR : 1H/2F\n"
                "- 30-50% des obèses en souffrent\n"
                "- Épisodes récurrents d'hyperphagie incontrôlée ≥ 1/semaine pendant ≥ 3 mois\n"
                "- **Pas de comportements compensatoires** (≠ boulimie)\n"
                "- Taux de rémission supérieur à celui de l'anorexie et boulimie"
            )),
            FicheRow(concept="PEC des TCA", detail_md=(
                "- **Psychothérapie** : TCC ++ (1re intention), psychoéducation\n"
                "- +/- ISRS (boulimie)\n"
                "- Rééducation nutritionnelle\n"
                "- Boulimie : comorbidités fréquentes (dépression, addictions 30-40%, "
                "personnalité borderline, kleptomanie)\n"
                "- Boulimie : taux de rémission à 12 ans de **70%**"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Syndrome maniaque vs syndrome dépressif", markdown=(
            "| Critère | Syndrome maniaque | Syndrome dépressif |\n"
            "|---------|------------------|-------------------|\n"
            "| Humeur | Exaltée, euphorie, irritabilité | Triste, douloureuse |\n"
            "| Psychomotricité | Accélération, agitation | Ralentissement, prostration |\n"
            "| Pensée | Tachypsychie, fuite des idées | Bradypsychie, ruminations |\n"
            "| Sommeil | Insomnie sans fatigue | Insomnie avec réveils précoces |\n"
            "| Estime de soi | Mégalomanie | Dévalorisation, culpabilité |\n"
            "| Appétit | Variable | Anorexie ++ |\n"
            "| Risque suicidaire | Présent (++ si mixte) | Élevé +++ |\n"
        )),
        TableauSynthese(titre="Thymorégulateurs : comparaison", markdown=(
            "| Molécule | Indication principale | Surveillance spécifique |\n"
            "|----------|----------------------|----------------------|\n"
            "| **Lithium** | Référence TBP | Lithiémie, fonction rénale, TSH |\n"
            "| **Valproate** | TBP (manie) | NFS, BHC, TP |\n"
            "| **Carbamazépine** | TBP (manie) | NFS, BHC (inducteur enzymatique) |\n"
            "| **Olanzapine** | Manie + prévention | Poids, bilan métabolique |\n"
            "| **Aripiprazole** | Manie + prévention | Poids, bilan métabolique |\n"
        )),
        TableauSynthese(titre="Anorexie vs boulimie vs hyperphagie boulimique", markdown=(
            "| Critère | Anorexie | Boulimie | Hyperphagie |\n"
            "|---------|----------|----------|-------------|\n"
            "| Poids | Dénutrition | Souvent normal | Surpoids/obésité |\n"
            "| Restriction | Majeure | Entre les crises | Absente |\n"
            "| Crises | Absentes | Présentes + purge | Présentes sans purge |\n"
            "| Conscience trouble | Anosognosie | Douloureuse | Présente |\n"
            "| SR | 1H/8F | 1H/3F | 1H/2F |\n"
            "| Pronostic | Règle des 1/3 | Rémission 70% à 12 ans | Meilleur |\n"
        )),
        TableauSynthese(titre="Niveaux d'urgence suicidaire", markdown=(
            "| | Urgence faible | Urgence moyenne | Urgence élevée |\n"
            "|--|---------------|-----------------|---------------|\n"
            "| Alliance | Bonne | Isolé | Très isolé |\n"
            "| Scénario | Pas de scénario précis | Reporté | Planifié dans les jours |\n"
            "| Moyen | Non considéré | Envisagé | Accès direct et immédiat |\n"
            "| État émotionnel | Souffrant mais stable | Fragile | Coupé ou très agité |\n"
        )),
        TableauSynthese(titre="BZD : classification par demi-vie", markdown=(
            "| Demi-vie | Molécule | Durée |\n"
            "|----------|----------|-------|\n"
            "| Courte | Oxazépam (Séresta) | 8h |\n"
            "| Courte | Alprazolam (Xanax) | 10-20h |\n"
            "| Intermédiaire | Bromazépam (Lexomil) | 20h |\n"
            "| Longue | Diazépam (Valium) | 47-92h |\n"
            "| Longue | Prazépam (Lysanxia) | 30-150h |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Prévalence TBP | **1-4%** | Population mondiale |\n"
        "| Retard diagnostic TBP | **10 ans** | Moyenne |\n"
        "| Suicide dans TBP non traité | **15%** | Si non/mal pris en charge |\n"
        "| Prévalence EDC vie entière | 11% H, **22%** F | 2F/1H |\n"
        "| Délai action antidépresseur | **3-4 semaines** | ISRS |\n"
        "| Durée traitement 1er EDC | **6 mois-1 an** | Après rémission |\n"
        "| Suicides/an France | **10-11 000** | 3e cause mortalité prématurée |\n"
        "| TS/an France | **180 000** | Récidive 40% |\n"
        "| Seuil OH homme | **30 g/j** | < 21 verres/semaine |\n"
        "| Seuil OH femme | **20 g/j** | < 14 verres/semaine |\n"
        "| CDT spécificité | **90%** | Meilleur marqueur OH chronique |\n"
        "| DT délai | **12-48h** | Après sevrage |\n"
        "| Lithiémie cible (LI) | **0,5-0,8** mEq/L | Forme libération immédiate |\n"
        "| Lithiémie cible (LP) | **0,8-1,2** mEq/L | Forme libération prolongée |\n"
        "| BZD durée max | **4-12 semaines** | RMO |\n"
        "| Anorexie prévalence F | **0,9-1,5%** | SR = 1H/8F |\n"
        "| Boulimie rémission | **70%** | À 12 ans |\n"
    ))

    points_cles = [
        "Le trouble bipolaire est une maladie chronique avec un retard diagnostic de 10 ans ; "
        "le lithium est le traitement de reference",
        "L'episode depressif caracterise necessite 5 symptomes sur 2 semaines dont humeur depressive "
        "et/ou anhédonie obligatoirement",
        "Les ISRS sont le traitement de 1re intention de l'EDC modere/severe avec un delai d'action "
        "de 3-4 semaines",
        "Le risque suicidaire doit etre systematiquement evalue : le syndrome pre-suicidaire de Ringel "
        "(calme apparent) est un piege classique",
        "L'agitation aigue impose d'eliminer en priorite une cause non psychiatrique, meme chez un "
        "patient psychiatrique connu",
        "Le delirium tremens survient 12-48h apres sevrage : traitement par BZD IV + vitamines B1/B6/PP "
        "+ hydratation",
        "La CDT est le marqueur biologique le plus specifique (90%) de l'alcoolisme chronique",
        "L'anorexie mentale suit la regle des 1/3 ; le refeeding syndrome est un piege de la renutrition "
        "trop rapide",
    ]

    fiche_eclair_md = (
        "**Trouble bipolaire** : prevalence 1-4%, debut 15-25 ans, retard diagnostic 10 ans. "
        "TBP I = manie, TBP II = hypomanie. Lithium = reference. Suicide 15% si non traite.\n\n"
        "**Trouble depressif** : EDC = 5 symptomes/2 semaines (humeur triste + anhedonie). "
        "ISRS en 1re intention, delai 3-4 sem. Melancolie = forme severe. Syndrome de Cotard = "
        "negation d'organes. ECT si resistance.\n\n"
        "**Conduites suicidaires** : 10 000 suicides/an, 180 000 TS/an en France. "
        "FDR primaires = trouble psy + ATCD TS + impulsivite. Syndrome de Ringel = fausse amelioration.\n\n"
        "**Urgences psy** : AP = debut brutal 20-30 min, eliminer organique PMZ. "
        "Agitation = eliminer cause non psy d'abord, BZD PO, contention en dernier recours.\n\n"
        "**Alcoolisme** : CDT spe 90%, gamma-GT spe 80%. DT = 12-48h post-sevrage, "
        "BZD IV + B1/B6/PP. Gayet-Wernicke = B1 en urgence. Korsakoff = amnesie + fabulations.\n\n"
        "**Psychotropes** : Lithium (lithiemie 0,5-0,8/0,8-1,2), CI IRC + depletion sodee. "
        "BZD : 6 proprietes, duree max 4-12 sem, arret progressif.\n\n"
        "**TCA** : Anorexie = restriction + peur poids + dysmorphophobie, regle 1/3. "
        "Boulimie = crises + purge, poids normal, remission 70% a 12 ans. "
        "Hyperphagie = crises sans purge, meilleur pronostic."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Psychiatrie",
        annee="2025-2026",
        item="Items 62, 64, 69, 72, 74, 76-77, 346, 348, 352",
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
    fiche = build_fiche()

    # Images : charger depuis image_captions.json si disponible
    captions_file = PROJECT_ROOT / "output" / ".work" / "psychiatrie" / "image_captions.json"
    if captions_file.exists():
        try:
            captions = json.loads(captions_file.read_text(encoding="utf-8"))
            print(f"Loaded {len(captions)} image captions")
        except Exception as e:
            print(f"Image captions skipped: {e}")

    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    docx_path = output_dir / "Medecine_generale_Psychiatrie_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Medecine_generale_Psychiatrie_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path}")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

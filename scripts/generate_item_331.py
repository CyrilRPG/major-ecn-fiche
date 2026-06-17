"""Génère la fiche de l'Item 331 - Arrêt cardiocirculatoire (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Généralités et définitions", sous_parties=[
            PlanSousPartie(lettre="A", titre="Épidémiologie et pronostic global"),
            PlanSousPartie(lettre="B", titre="Définitions et terminologie"),
            PlanSousPartie(lettre="C", titre="No-flow et low-flow"),
        ]),
        PlanPartie(numero="II", titre="Chaîne de survie et défibrillation", sous_parties=[
            PlanSousPartie(lettre="A", titre="Principe de la chaîne de survie"),
            PlanSousPartie(lettre="B", titre="Défibrillation, FV et asystolie"),
            PlanSousPartie(lettre="C", titre="Massage cardiaque externe"),
        ]),
        PlanPartie(numero="III", titre="Étiologies", sous_parties=[
            PlanSousPartie(lettre="A", titre="Syndromes coronariens aigus inauguraux"),
            PlanSousPartie(lettre="B", titre="Autres étiologies cardiaques et vasculaires"),
            PlanSousPartie(lettre="C", titre="Origines non cardiovasculaires"),
        ]),
        PlanPartie(numero="IV", titre="Diagnostic et conduite à tenir préhospitalière", sous_parties=[
            PlanSousPartie(lettre="A", titre="Diagnostic clinique"),
            PlanSousPartie(lettre="B", titre="Mesures de survie ACD avant l'ambulance"),
        ]),
        PlanPartie(numero="V", titre="Réanimation médicalisée (Smur)", sous_parties=[
            PlanSousPartie(lettre="A", titre="Arrivée de l'équipe médicalisée"),
            PlanSousPartie(lettre="B", titre="Vasoconstricteur : adrénaline"),
            PlanSousPartie(lettre="C", titre="Antiarythmiques (amiodarone, lidocaïne, magnésium)"),
            PlanSousPartie(lettre="D", titre="Bradycardies extrêmes (atropine, isoprénaline)"),
            PlanSousPartie(lettre="E", titre="Agents métaboliques et thrombolyse"),
        ]),
        PlanPartie(numero="VI", titre="Pronostic à la phase préhospitalière", sous_parties=[
            PlanSousPartie(lettre="A", titre="Facteurs pronostiques"),
            PlanSousPartie(lettre="B", titre="Rythme initial et survie"),
        ]),
        PlanPartie(numero="VII", titre="Phase hospitalière et préservation cérébrale", sous_parties=[
            PlanSousPartie(lettre="A", titre="Préservation de la fonction cardiaque"),
            PlanSousPartie(lettre="B", titre="Préservation cérébrale et pronostic neurologique"),
            PlanSousPartie(lettre="C", titre="Aspects éthiques et information de la famille"),
        ]),
    ]

    # ── PARTIE I : GÉNÉRALITÉS ET DÉFINITIONS ──
    partie_i = Partie(numero="I", titre="Généralités et définitions", sous_parties=[
        SousPartie(lettre="A", titre="Épidémiologie et pronostic global", rows=[
            FicheRow(concept="◆ Cadre réglementaire et recommandations", detail_md=(
                "- Recommandations en France basées sur :\n"
                "  - **ERC 2021** (Comité européen de réanimation)\n"
                "  - **ESC 2022** (Société européenne de cardiologie)\n"
                "  - Recommandations américaines 2020\n"
                "- Adoption par la Société française de réanimation et la Société française de médecine d'urgence"
            )),
            FicheRow(concept="◆ Épidémiologie", detail_md=(
                "- **300 000 décès/an** par arrêt cardiaque extrahospitalier aux États-Unis\n"
                "- **500 000 décès/an** en Europe\n"
                "- En France : **40 000 décès/an** par arrêt cardiaque\n"
                "  - Incidence de **0,75 ‰** dans la population générale"
            )),
            FicheRow(concept="◆ Pronostic global", detail_md=(
                "- L'arrêt cardiaque prolongé au-delà de quelques minutes aboutit très rapidement au décès\n"
                "- Au-delà de **5 minutes** d'arrêt : survie de **7 à 8 %**\n"
                "- Au-delà de **10 minutes** : survie **proche de 0**\n"
                "- Probabilité de survie sans séquelle fonctionnelle **nulle après 30 minutes**\n"
                "- Pourcentage de survie peu amélioré dans les 40 dernières années\n"
                "- Survie sans séquelles (notamment neurologiques) : **2 à 4 %**"
            )),
            FicheRow(concept="Arrêt intrahospitalier vs extrahospitalier", detail_md=(
                "- Arrêts intrahospitaliers : survie plus élevée à **40-50 %**\n"
                "- Mortalité globale reste néanmoins importante\n"
                "- Survie globale des AC : **5-20 %** selon les études"
            )),
            FicheRow(concept="", detail_md=(
                "- L'importance du témoin et de l'action immédiate orientée par un régulateur "
                "des urgences est capitale.\n"
                "- Formation aux premiers secours dès le plus jeune âge avec entretien régulier "
                "du niveau de compétences."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Définitions et terminologie", rows=[
            FicheRow(concept="◆ Mort subite (définition OMS)", detail_md=(
                "- Mort instantanée, soudaine, subite correspondant à une maladie aiguë\n"
                "- Symptômes la précédant ne dépassent pas quelques minutes, voire **1 heure au plus**"
            )),
            FicheRow(concept="★ ◆ Arrêt cardiocirculatoire (ACC) / arrêt cardiaque (AC)", detail_md=(
                "- **Cessation de l'activité mécanique cardiaque**\n"
                "- Confirmée par :\n"
                "  - Absence de pouls\n"
                "  - Apnée ou respiration agonique (**gasping**)"
            )),
            FicheRow(concept="◆ Arrêt cardiaque réfractaire", detail_md=(
                "- Absence de récupération d'une circulation spontanée après **30 minutes** de "
                "réanimation médicale bien conduite\n"
                "- Définition française, reste néanmoins discutée"
            )),
            FicheRow(concept="Arrêt cardiaque récupéré (ou réanimé avec succès)", detail_md=(
                "- Récupération d'une hémodynamique stable : pouls et pression artérielle convenables"
            )),
        ]),
        SousPartie(lettre="C", titre="No-flow et low-flow", rows=[
            FicheRow(concept="◆ Délai d'instauration de la réanimation", detail_md=(
                "- Délai entre la survenue de l'arrêt et le début de la réanimation\n"
                "- **Déterminant le plus important pour la survie** selon les experts\n"
                "- Détermine le pronostic immédiat, intermédiaire et à distance"
            )),
            FicheRow(concept="◆ No-flow", detail_md=(
                "- Intervalle de temps sans réanimation, patient en état de « mort apparente »\n"
                "- Correspond à l'absence de mécanique cardiaque efficace\n"
                "- Difficile, voire impossible à établir en l'absence de témoin\n"
                "- **No-flow > 5 minutes** = très mauvais pronostic (décès très élevé, séquelles "
                "fréquentes en cas de survie)\n"
                "- **Au-delà de 10 minutes** : survie quasi nulle, évolution vers une **encéphalopathie "
                "anoxique** (altération irrémédiable des fonctions cérébrales supérieures)\n"
                "- Au-delà de 10 minutes de no-flow → interrogation sur le caractère éthique d'une réanimation"
            )),
            FicheRow(concept="◆ Low-flow", detail_md=(
                "- Temps de réanimation sans rétablissement d'une hémodynamique convenable (pouls "
                "et pression artérielle stables)\n"
                "- Si la période de no-flow est brève, la durée du low-flow est moins déterminante\n"
                "- Une réanimation longue peut s'accompagner d'une récupération fonctionnelle "
                "cardiaque et cérébrale si elle est précoce, bien réalisée et efficace"
            )),
            FicheRow(concept="", detail_md=(
                "- **Tout doit être fait pour réduire le no-flow et le low-flow** : leur durée "
                "influence de manière déterminante le pronostic."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE II : CHAÎNE DE SURVIE ET DÉFIBRILLATION ──
    partie_ii = Partie(numero="II", titre="Chaîne de survie et défibrillation", sous_parties=[
        SousPartie(lettre="A", titre="Principe de la chaîne de survie", rows=[
            FicheRow(concept="◆ Concept de chaîne de survie", detail_md=(
                "- Décrite par Cummins en **1991**\n"
                "- Précise les étapes de la réanimation d'un patient en ACR\n"
                "- La rapidité de mise en œuvre et la complémentarité des maillons sont les "
                "gages de la survie"
            )),
            FicheRow(concept="◆ Les 6 maillons de la chaîne de survie", detail_md=(
                "- **1. Témoin** : alerte précoce (composer le **15**) et début de la RCP sous contrôle\n"
                "- **2. RCP précoce** : massage cardiaque + dégagement des voies aériennes (pas de bouche-à-bouche chez l'adulte)\n"
                "- **3. Défibrillation précoce** : la plus précoce possible si rythme « chocable »\n"
                "- **4. RCP spécialisée** par l'équipe du **Smur** sur place\n"
                "- **5. Prise en charge hospitalière réanimatoire** de haut niveau (traitement de la cause, "
                "hypothermie contrôlée, assistance circulatoire, correction métabolique)\n"
                "- **6. Rétablissement**"
            )),
            FicheRow(concept="Rôle du grand public", detail_md=(
                "- Les 2 premiers maillons relèvent du grand public\n"
                "- En France : seulement **10-15 %** de la population formée à la RCP\n"
                "- Pourcentage en hausse grâce aux initiations dès le plus jeune âge\n"
                "- Importance pour le pronostic vital ET pour prévenir/minimiser les séquelles neurologiques"
            )),
            FicheRow(concept="◆ Défibrillation par les non-médecins", detail_md=(
                "- En France, défibrillation possible par :\n"
                "  - Médecins, infirmiers, secouristes, ambulanciers\n"
                "- Depuis le **décret 97-239 du 27 mars 1998**\n"
                "- Généralisation des **DSA** dans les lieux publics : gares, aéroports, stades, mairies, "
                "centres administratifs, postes, pharmacies, centres commerciaux"
            )),
            FicheRow(concept="Facteurs pronostiques de la chaîne de survie", detail_md=(
                "- Le pronostic dépend de :\n"
                "  - Étiologie\n"
                "  - Lieu de survenue (intra ou extrahospitalier)\n"
                "  - Présence d'un témoin\n"
                "  - Rapidité des mesures immédiates (réduit la durée de no-flow)\n"
                "  - À un moindre degré, durée de la réanimation"
            )),
        ]),
        SousPartie(lettre="B", titre="Défibrillation, FV et asystolie", rows=[
            FicheRow(concept="★ ◆ Fibrillation ventriculaire (FV)", detail_md=(
                "- **Mode électrique initial le plus fréquent** de l'ACC\n"
                "- Le **choc électrique externe (CEE)** est son **seul traitement efficace** et durable\n"
                "- Au moment du début de la RCP : FV observée dans **40 à 70 %** des cas selon la "
                "rapidité de mise en œuvre"
            )),
            FicheRow(concept="◆ Mécanisme du CEE", detail_md=(
                "- Faire passer à travers le cœur un courant électrique\n"
                "- Entraîne la dépolarisation simultanée d'une masse critique de cellules myocardiques\n"
                "- Interrompt les phénomènes de **réentrée** → arrêt de la FV ou TV"
            )),
            FicheRow(concept="◆ Type de défibrillateur", detail_md=(
                "- **Défibrillateurs biphasiques** (CEE jusqu'à **200 J**) : actuels, plus sûrs et plus efficaces\n"
                "- **Défibrillateurs monophasiques** (CEE à **360 J**) : remplacés"
            )),
            FicheRow(concept="◆ Délai de défibrillation et survie", detail_md=(
                "| Délai du CEE après arrêt | Survie en FV |\n"
                "|---|---|\n"
                "| **1 à 3 minutes** | **40-60 %** |\n"
                "| **4 à 6 minutes** | **35 %** |\n"
                "| **7 à 10 minutes** | **25 %** |\n"
                "| **> 10 minutes** | **< 5 %** (survie sans séquelles très rare) |"
            )),
            FicheRow(concept="◆ DSA (défibrillateurs semi-automatiques)", detail_md=(
                "- Permettent d'administrer des CEE avant l'arrivée des équipes médicales\n"
                "- Analysent le rythme cardiaque automatiquement\n"
                "- Portent l'indication de la défibrillation\n"
                "- Délivrent le choc **uniquement si le rythme est « chocable »** (FV, flutter "
                "ventriculaire ou TV à fréquence élevée)\n"
                "- Permettent de gagner un temps précieux"
            )),
            FicheRow(concept="◆ Asystolie", detail_md=(
                "- **Tracé électrique plat**\n"
                "- Témoigne soit d'une étiologie extracardiaque, soit le plus souvent d'une "
                "période de no-flow assez longue\n"
                "- La FV se dégrade progressivement : large maille → petite maille → tracé plat\n"
                "- L'asystolie initiale dès la survenue de l'AC est assez rare mais possible\n"
                "- **Facteur pronostic péjoratif**\n"
                "- En cas d'asystolie : **massage cardiaque, PAS de défibrillation**"
            )),
            FicheRow(concept="◆ Dissociation électromécanique", detail_md=(
                "- Existence d'une activité électrique sans activité mécanique (pouls et pression "
                "artérielle imprenables)\n"
                "- Traduit un cœur agonique sans contractilité efficace\n"
                "- Conduit à **poursuivre le massage** même en présence d'une activité électrique"
            )),
            FicheRow(concept="", detail_md=(
                "- Idéalement, le **premier CEE doit être délivré dans les 3 minutes** suivant l'arrêt "
                "si le diagnostic est rapide et l'accès au défibrillateur simple.\n"
                "- À défaut, débuter immédiatement le MCE."
            ), kind="a_retenir"),
            FicheRow(concept="", detail_md=(
                "- ⚠ Une **asystolie** est un marqueur de temps écoulé entre l'arrêt cardiaque "
                "et le diagnostic : 50 % des FV se dégradent en asystolie entre la 4ᵉ et la 8ᵉ minute."
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Massage cardiaque externe", rows=[
            FicheRow(concept="◆ Objectifs du MCE", detail_md=(
                "- Maintenir transitoirement une mécanique cardiaque et une circulation vers "
                "les organes périphériques, en premier lieu le cerveau\n"
                "- En l'absence de défibrillateur ou d'efficacité de la défibrillation\n"
                "- **Prioritaire** pour limiter le no-flow et améliorer le pronostic"
            )),
            FicheRow(concept="◆ Technique du MCE", detail_md=(
                "- Patient en décubitus dorsal\n"
                "- Talon de la main sur le centre du thorax\n"
                "- **Amplitude** : **4 à 5 cm**\n"
                "- **Fréquence** : **100/min**\n"
                "- Relais toutes les **2 minutes** environ si plusieurs sauveteurs (limite la fatigue, "
                "maintient l'efficacité)"
            )),
        ]),
    ])

    # ── PARTIE III : ÉTIOLOGIES ──
    partie_iii = Partie(numero="III", titre="Étiologies", sous_parties=[
        SousPartie(lettre="A", titre="Syndromes coronariens aigus inauguraux", rows=[
            FicheRow(concept="◆ Pathologie coronarienne : 1ʳᵉ étiologie", detail_md=(
                "- **Principale étiologie** des AC\n"
                "- L'arrêt cardiaque peut être précédé d'une douleur thoracique témoignant de "
                "l'ischémie"
            )),
            FicheRow(concept="◆ Mécanisme lésionnel", detail_md=(
                "- Lésions athéromateuses compliquées par :\n"
                "  - **Rupture de plaque**\n"
                "  - **Thrombose coronarienne**\n"
                "- Mises en évidence fréquemment lors d'autopsies ou de coronarographies après mort subite"
            )),
            FicheRow(concept="◆ Données chiffrées", detail_md=(
                "- Lésions coronariennes : **40 à 77 %** des causes de mort subite\n"
                "- **20 à 40 %** des AC compliquent un infarctus du myocarde\n"
                "- Près de **70 %** des patients réanimés pour AC extrahospitalier présenteraient :\n"
                "  - soit un IDM\n"
                "  - soit une embolie pulmonaire massive"
            )),
        ]),
        SousPartie(lettre="B", titre="Autres étiologies cardiaques et vasculaires", rows=[
            FicheRow(concept="◆ Cardiomyopathies", detail_md=(
                "- **Cardiomyopathie hypertrophique** (CMH) : surtout formes familiales et/ou "
                "obstructives (mort subite à l'effort, mais pas exclusivement)\n"
                "- Cardiomyopathie dilatée\n"
                "- **Dysplasie ventriculaire droite arythmogène (DVDA)**\n"
                "- Cardiopathies valvulaires : rétrécissement aortique essentiellement"
            )),
            FicheRow(concept="◆ Troubles du rythme/conduction sans anomalie structurelle", detail_md=(
                "- FV idiopathique\n"
                "- **Syndrome de Brugada**\n"
                "- Troubles conductifs paroxystiques (notamment sujet âgé)\n"
                "- **Syndromes du QT long** congénitaux ou favorisés par les médicaments\n"
                "- Syndromes du QT court congénitaux\n"
                "- Voies accessoires : syndrome de **Wolff-Parkinson-White**"
            )),
            FicheRow(concept="◆ Autres causes cardiovasculaires", detail_md=(
                "- Myocardite aiguë\n"
                "- Cardiopathies congénitales et malformations vasculaires\n"
                "- **Tamponnade**\n"
                "- **Dissection aortique**\n"
                "- **Embolie pulmonaire massive**\n"
                "- Rupture d'anévrisme"
            )),
            FicheRow(concept="Bradycardies extrêmes", detail_md=(
                "- Bloc atrioventriculaire de haut grade\n"
                "- Asystolies\n"
                "- Constatation initiale variable selon le délai de prise en charge"
            )),
        ]),
        SousPartie(lettre="C", titre="Origines non cardiovasculaires", rows=[
            FicheRow(concept="◆ Origines non cardiovasculaires", detail_md=(
                "- Représentent **5 à 25 %** des cas\n"
                "- Diagnostic généralement plus aisé, orienté par le contexte\n"
                "- Principales :\n"
                "  - Causes toxiques\n"
                "  - Causes traumatiques\n"
                "  - Insuffisances respiratoires aiguës\n"
                "  - Noyades"
            )),
            FicheRow(concept="", detail_md=(
                "- **La cause immédiate la plus fréquente d'ACC est une FV d'étiologie ischémique** : "
                "soit nécrose en cours de constitution, soit trouble du rythme ventriculaire sur "
                "séquelle d'IDM ancien.\n"
                "- Le patient peut avoir une FV d'emblée ou une TV qui se dégrade secondairement "
                "en FV en quelques minutes."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE IV : DIAGNOSTIC ET CONDUITE À TENIR PRÉHOSPITALIÈRE ──
    partie_iv = Partie(numero="IV", titre="Diagnostic et conduite à tenir préhospitalière", sous_parties=[
        SousPartie(lettre="A", titre="Diagnostic clinique", rows=[
            FicheRow(concept="◆ Pour les témoins (grand public)", detail_md=(
                "- Patient :\n"
                "  - Inconscient\n"
                "  - Ne bouge plus\n"
                "  - Ne réagit plus\n"
                "  - Ne respire plus OU respire uniquement de manière très anormale (**gasps**)"
            )),
            FicheRow(concept="◆ Pour le public formé / premiers secours", detail_md=(
                "- Il faut également constater :\n"
                "  - **Absence de pouls carotidien**\n"
                "  - OU absence de pouls fémoral"
            )),
            FicheRow(concept="Conduite immédiate", detail_md=(
                "- Dès le diagnostic posé ou suspecté :\n"
                "  - **Appeler le 15**\n"
                "  - **Commencer les manœuvres de réanimation**"
            )),
        ]),
        SousPartie(lettre="B", titre="Mesures de survie ACD avant l'ambulance", rows=[
            FicheRow(concept="◆ Acronyme ACD", detail_md=(
                "- **A : Airway** — maintien des voies aériennes libres\n"
                "- **C : Circulation** — maintien d'une circulation (MCE)\n"
                "- **D : Defibrillation** — si rythme initial = TV ou FV"
            )),
            FicheRow(concept="◆ A : Voies aériennes (Airway)", detail_md=(
                "- Basculer la tête en arrière\n"
                "- Surélever le menton\n"
                "- Vérifier l'absence de corps étranger (retrait éventuel avec doigts en crochet)\n"
                "- Dès l'arrivée des secours ou en milieu médicalisé : mise en place d'une "
                "**canule de Guedel** dans la cavité buccale"
            )),
            FicheRow(concept="◆ C : Circulation (MCE)", detail_md=(
                "- MCE correctement réalisé = **prioritaire** pour limiter le no-flow\n"
                "- Patient en décubitus dorsal\n"
                "- Talon de la main sur le centre du thorax\n"
                "- Compressions de **4 à 5 cm**, fréquence **100/min**\n"
                "- Relais toutes les **2 minutes** entre sauveteurs"
            )),
            FicheRow(concept="◆ D : Défibrillation", detail_md=(
                "- Utiliser le **DSA** si disponible et si le sauveteur sait s'en servir\n"
                "- Avant l'arrivée de l'ambulance médicalisée\n"
                "- Poursuivre la réanimation **2 minutes après le choc** avant de vérifier la reprise "
                "d'une activité circulatoire efficace"
            )),
            FicheRow(concept="◆ Bouche-à-bouche (B : breathing)", detail_md=(
                "- **N'est plus recommandé chez l'adulte**\n"
                "- **Reste recommandé chez l'enfant et le nourrisson** : oxygénation essentielle car "
                "cause souvent hypoxique de l'AC dans cette population\n"
                "- Le MCE reste prioritaire, son interruption doit être la plus limitée possible"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Ne pas connaître les mesures **ACD** est une notion inacceptable au concours.\n"
                "- ⚠ Le bouche-à-bouche **n'est plus recommandé chez l'adulte** mais reste indiqué "
                "chez l'enfant/nourrisson."
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE V : RÉANIMATION MÉDICALISÉE (SMUR) ──
    partie_v = Partie(numero="V", titre="Réanimation médicalisée (Smur)", sous_parties=[
        SousPartie(lettre="A", titre="Arrivée de l'équipe médicalisée", rows=[
            FicheRow(concept="◆ Facteurs pronostiques favorables initiaux", detail_md=(
                "- Présence d'un témoin\n"
                "- Réanimation précoce\n"
                "- Rythme initial : **fibrillation ventriculaire**\n"
                "- Défibrillation rapide\n"
                "- Durée courte de la réanimation"
            )),
            FicheRow(concept="◆ Principes de la réanimation médicalisée", detail_md=(
                "- S'assurer de la très bonne qualité des compressions (se relayer ou utiliser "
                "du matériel de compression)\n"
                "- Minimiser les interruptions entre les compressions (y compris pendant la "
                "ventilation)\n"
                "- Oxygéner dès que possible\n"
                "- Utiliser un **capnographe** (enregistreur de CO2)\n"
                "- Mettre en place des voies d'accès vasculaires (veineuse, cathéter artériel "
                "si possible pour PA invasive)\n"
                "- Administrer des médicaments (adrénaline, etc.)\n"
                "- Préparer le traitement étiologique si pertinent (intoxication, revascularisation)\n"
                "- Discuter la mise en place d'une **assistance circulatoire extracorporelle**"
            )),
            FicheRow(concept="◆ Gestes spécifiques médicalisés", detail_md=(
                "- Défibrillation si appropriée\n"
                "- Oxygénothérapie par ventilation invasive après **intubation endotrachéale**\n"
                "  - **Ne pas interrompre le MCE plus de 30 secondes** pour l'intubation\n"
                "  - En cas de difficulté : ventilation au masque\n"
                "- Pose d'une voie d'abord veineuse pour administration des médicaments"
            )),
        ]),
        SousPartie(lettre="B", titre="Vasoconstricteur : adrénaline", rows=[
            FicheRow(concept="◆ Mécanisme d'action", detail_md=(
                "- Premier médicament historique utilisé dans les AC\n"
                "- Effets bénéfiques principalement liés aux récepteurs **alpha-adrénergiques** :\n"
                "  - Augmentation des débits sanguins myocardique et cérébral\n"
                "- Effets bêta-adrénergiques controversés :\n"
                "  - Augmentation du travail myocardique\n"
                "  - Réduction de la perfusion sous-endocardique"
            )),
            FicheRow(concept="◆ Indication et posologie", detail_md=(
                "- **Traitement incontournable** des AC réfractaires en asystolie\n"
                "- Posologie habituelle : **1 mg toutes les 4 minutes** IV ou endotrachéale\n"
                "- En cas de FV/TV persistante après le 1ᵉʳ CEE : adrénaline également injectée "
                "après 2 min de réanimation, juste avant le 2ᵉ ou le 3ᵉ choc"
            )),
            FicheRow(concept="◆ Limites pronostiques", detail_md=(
                "- Impact sur la survie et les séquelles neurologiques reste limité\n"
                "- Pronostic inversement corrélé à la quantité d'adrénaline utilisée\n"
                "- **Au-delà de 1 à 2 mg** : survie faible et survie sans séquelles neurologiques "
                "lourdes quasi inexistante"
            )),
        ]),
        SousPartie(lettre="C", titre="Antiarythmiques (amiodarone, lidocaïne, magnésium)", rows=[
            FicheRow(concept="◆ Indication générale", detail_md=(
                "- AC réfractaires avec troubles du rythme ventriculaire récidivants après "
                "chocs électriques multiples (2 ou plus)"
            )),
            FicheRow(concept="◆ Amiodarone (1ʳᵉ intention)", detail_md=(
                "- Activité sur canaux sodiques, potassiques, calciques\n"
                "- Propriétés inhibitrices alpha et bêta-adrénergiques\n"
                "- Supérieure à la lidocaïne sur la survie à court terme (études prospectives)\n"
                "- Indication : TV ou FV **réfractaires aux CEE**, juste avant le **3ᵉ choc**\n"
                "- **Posologie initiale** : **300 mg** dilués dans 20 à 30 mL de sérum salé isotonique, "
                "administrés rapidement\n"
                "- **Doses supplémentaires** : **150 mg** renouvelables en cas de TV/FV réfractaires "
                "(persistantes après 3ᵉ CEE) ou récidivantes"
            )),
            FicheRow(concept="◆ Lidocaïne (alternative)", detail_md=(
                "- N'a jamais apporté de bénéfice à court ou long terme\n"
                "- Utilisée uniquement si pas d'amiodarone disponible\n"
                "- **Posologie** : **1,5 mg/kg** en injection IV lente\n"
                "- **Dose totale max** : **3 mg/kg**"
            )),
            FicheRow(concept="◆ Sulfate de magnésium", detail_md=(
                "- **Indications** :\n"
                "  - **Torsades de pointes**\n"
                "  - Suspicion d'hypomagnésémie\n"
                "- **Posologie** : **2 g en IV directe**"
            )),
        ]),
        SousPartie(lettre="D", titre="Bradycardies extrêmes (atropine, isoprénaline)", rows=[
            FicheRow(concept="◆ Atropine", detail_md=(
                "- Indication : bradycardies sinusales extrêmes\n"
                "- **Posologie** : **1 mg** répétée toutes les 3 à 5 minutes\n"
                "- **Dose totale max** : **0,04 mg/kg**"
            )),
            FicheRow(concept="◆ Isoprénaline", detail_md=(
                "- Intérêt dans les bradycardies extrêmes, notamment **BAV du 3ᵉ degré** sans "
                "hémodynamique efficace\n"
                "- **Posologie** : 5 ampoules à **0,2 mg** diluées dans **250 cm³ de glucosé à 5 %**\n"
                "- Débit à adapter à la fréquence : objectif **≥ 50-60 bpm**"
            )),
            FicheRow(concept="◆ Restriction d'usage", detail_md=(
                "- Atropine et isoprénaline réservées aux AC d'étiologie certaine conductive ou "
                "vagale maligne\n"
                "- Bradycardies extrêmes avec conséquences hémodynamiques\n"
                "- AC survenant généralement en milieu intrahospitalier ou médicalisé"
            )),
        ]),
        SousPartie(lettre="E", titre="Agents métaboliques et thrombolyse", rows=[
            FicheRow(concept="◆ Désordres métaboliques de l'AC", detail_md=(
                "- Très rapidement (après 3-4 min d'AC) :\n"
                "  - **Acidose métabolique**\n"
                "  - **Hyperkaliémie**\n"
                "- À corriger lors de la réanimation prolongée"
            )),
            FicheRow(concept="◆ Bicarbonate de sodium 84 ‰ équimolaire", detail_md=(
                "- Utilisation discutée\n"
                "- Vise à corriger l'acidose métabolique (diminution du débit sanguin, hypoxie "
                "tissulaire)\n"
                "- Effet positif théorique sur la perfusion myocardique par rééquilibrage acido-basique\n"
                "- La plupart des études : pas d'amélioration significative sur la survie\n"
                "- **Alcalinisation indiquée dans des situations particulières** :\n"
                "  - Réanimations prolongées\n"
                "  - Hyperkaliémies\n"
                "  - Acidoses préexistantes\n"
                "  - Intoxications aux **stabilisateurs de membrane** : **phénobarbital**, "
                "**antidépresseurs tricycliques**"
            )),
            FicheRow(concept="◆ Thrombolyse préhospitalière", detail_md=(
                "- **Pas recommandée systématiquement**\n"
                "- Réservée au cas par cas :\n"
                "  - **Infarctus du myocarde** avéré ou fortement suspecté\n"
                "  - **Embolie pulmonaire massive** avérée ou fortement suspectée"
            )),
        ]),
    ])

    # ── PARTIE VI : PRONOSTIC PRÉHOSPITALIER ──
    partie_vi = Partie(numero="VI", titre="Pronostic à la phase préhospitalière", sous_parties=[
        SousPartie(lettre="A", titre="Facteurs pronostiques", rows=[
            FicheRow(concept="◆ Pronostic global", detail_md=(
                "- **Pronostic effroyable**\n"
                "- Mort quasi certaine si arrêt en l'absence de témoin\n"
                "- Survie globale des AC : **5-20 %**\n"
                "- Pronostic meilleur pour les AC intrahospitaliers que extrahospitaliers"
            )),
            FicheRow(concept="◆ Survie en milieu extrahospitalier", detail_md=(
                "- Rétablir un rythme stable et efficace est un objectif majeur mais ne garantit "
                "pas la survie prolongée ni le rétablissement ad integrum des fonctions cognitives\n"
                "- Seulement **20 %** des patients arrivés vivants à l'hôpital sortent sans "
                "séquelles neurologiques\n"
                "- **ILCOR** : **2 à 10 %** des patients sortent vivants et peuvent reprendre une vie "
                "normale dans les grandes agglomérations équipées de DSA et avec éducation de la "
                "population (exemple néerlandais)"
            )),
            FicheRow(concept="◆ Facteur clé : prise en charge précoce", detail_md=(
                "- **Facteur essentiel pour la survie**\n"
                "- Cascade de l'anoxie tissulaire → nécrose cardiaque et cérébrale\n"
                "- **Taux de survie décroît de 10 % pour chaque minute** écoulée sans réanimation"
            )),
        ]),
        SousPartie(lettre="B", titre="Rythme initial et survie", rows=[
            FicheRow(concept="◆ Rythmes initiaux selon ILCOR 2015", detail_md=(
                "- **FV** : **70 à 80 %** des cas\n"
                "- **Bradycardie extrême** (BAV haut degré, asystolie) : **15 à 20 %**\n"
                "- AC le plus souvent dû à un trouble du rythme ventriculaire :\n"
                "  - FV d'emblée\n"
                "  - OU TV dégénérant secondairement en FV"
            )),
            FicheRow(concept="◆ Évolution de la FV", detail_md=(
                "- FV à grosses mailles (au départ)\n"
                "- FV à petites mailles\n"
                "- Tracé désorganisé, équivalent d'un tracé plat\n"
                "- **50 % des FV se dégradent en asystolie entre la 4ᵉ et la 8ᵉ minute**\n"
                "- **Asystolie = marqueur de temps écoulé** entre l'AC et le diagnostic"
            )),
            FicheRow(concept="◆ Type de trouble du rythme et pronostic", detail_md=(
                "- Meilleur pronostic en cas de **FV** que d'**asystolie**\n"
                "- Le type de trouble du rythme est directement associé au pronostic"
            )),
            FicheRow(concept="", detail_md=(
                "- **L'asystolie initiale signe presque toujours un arrêt déjà ancien**, soit par "
                "dégradation d'une FV non prise en charge, soit par étiologie extracardiaque (no-flow long)."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE VII : PHASE HOSPITALIÈRE ──
    partie_vii = Partie(numero="VII", titre="Phase hospitalière et préservation cérébrale", sous_parties=[
        SousPartie(lettre="A", titre="Préservation de la fonction cardiaque", rows=[
            FicheRow(concept="◆ Sidération / hibernation myocardique", detail_md=(
                "- La fonction cardiaque peut être transitoirement altérée après l'AC\n"
                "- Facteurs préhospitaliers favorisants :\n"
                "  - Délai long avant la réanimation (no-flow prolongé)\n"
                "  - Délai prolongé de réanimation (low-flow prolongé)\n"
                "  - Doses importantes de vasopresseurs\n"
                "  - Intensité et nombre de chocs électriques"
            )),
            FicheRow(concept="◆ Traitement de l'insuffisance contractile", detail_md=(
                "- **Dobutamine** : inotrope positif, traitement de choix des troubles de la "
                "contractilité\n"
                "- Assistance circulatoire par pompe extracorporelle si insuffisant\n"
                "- Dispositifs de décharge ventriculaire gauche possibles"
            )),
            FicheRow(concept="◆ Monitoring hospitalier", detail_md=(
                "- **Échocardiographie** : monitoring essentiel de la fonction cardiaque\n"
                "- Mesure des pressions invasives : **cathéter de Swan-Ganz**\n"
                "- Angioplastie d'éventuelles lésions coronariennes"
            )),
            FicheRow(concept="◆ Indications de coronarographie post-AC", detail_md=(
                "- À proposer si étiologie coronarienne avérée ou suspectée\n"
                "- Critères en faveur :\n"
                "  - Antécédents cardiovasculaires\n"
                "  - Douleur thoracique précédant l'AC rapportée par le témoin\n"
                "  - ECG post-récupération évocateur de SCA : **susdécalage ST**, **BBG**, etc.\n"
                "- **Coronarographie au moindre doute**"
            )),
            FicheRow(concept="Spécificité du sujet jeune (< 30 ans)", detail_md=(
                "- Maladie coronarienne d'incidence faible\n"
                "- Causes cardiaques principales :\n"
                "  - Troubles du rythme ventriculaire non ischémiques\n"
                "  - Décompensations de cardiopathies congénitales"
            )),
        ]),
        SousPartie(lettre="B", titre="Préservation cérébrale et pronostic neurologique", rows=[
            FicheRow(concept="◆ Mécanisme des lésions cérébrales", detail_md=(
                "- Cerveau très rapidement victime de l'anoxie\n"
                "- Lésions dès les premières minutes\n"
                "- Aggravation possible à la reperfusion : **syndrome inflammatoire systémique** "
                "(lésions d'ischémie-reperfusion)\n"
                "- Neurones très sensibles aux variations de pression intracrânienne\n"
                "- Disparition possible des mécanismes d'autorégulation\n"
                "- **Pression artérielle efficace = pronostic cérébral**"
            )),
            FicheRow(concept="◆ Appréciation du pronostic cérébral", detail_md=(
                "- Évaluations répétées dont spécificité et sensibilité s'affinent entre **J1 et J3** :\n"
                "  - **Score de Glasgow**\n"
                "  - **Électroencéphalogramme (EEG)**\n"
                "  - **Potentiels évoqués sensitifs**"
            )),
            FicheRow(concept="◆ Oxygénation et ventilation", detail_md=(
                "- 1ʳᵉ ligne pour lutter contre l'hypoxie\n"
                "- **Hypoxie et hypercapnie** → **HTIC fatale**"
            )),
            FicheRow(concept="◆ Sédation", detail_md=(
                "- Met le tissu cérébral au repos\n"
                "- Diminue les besoins en oxygène\n"
                "- Permet de lutter contre l'œdème"
            )),
            FicheRow(concept="◆ Glycémie", detail_md=(
                "- Glucose = élément nutritif unique du tissu cérébral\n"
                "- Glycorachie normalement constante dans le LCS (homéostasie)\n"
                "- Homéostasie perturbée lors d'un AC\n"
                "- **Hyperglycémie → œdème cérébral** par phénomènes osmotiques\n"
                "- **Lutte contre l'hyperglycémie = vitale**"
            )),
            FicheRow(concept="◆ Régulation thermique (cooling)", detail_md=(
                "- Système nerveux central très sensible aux variations de température, surtout en "
                "période d'agression\n"
                "- **Hypothermie modérée contrôlée à ~34 °C** : pourrait diminuer les lésions "
                "d'ischémie-reperfusion (place débattue)\n"
                "- **Hyperthermie = aggravation** des lésions d'ischémie-reperfusion → doit être "
                "prévenue (« contrôle thermique »)"
            )),
            FicheRow(concept="◆ Post-resuscitation care", detail_md=(
                "- Phase intrahospitalière succédant à l'AC réanimé avec succès\n"
                "- Constitue le **5ᵉ maillon** de la chaîne de survie\n"
                "- Améliore très significativement le pronostic vital et fonctionnel (notamment cérébral)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Récupérer une activité cardiaque et une hémodynamique correcte **n'est pas "
                "synonyme de survie** : 20 % seulement des patients « arrivés vivants » sortent sans "
                "séquelles neurologiques."
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Aspects éthiques et information de la famille", rows=[
            FicheRow(concept="Séquelles neurologiques", detail_md=(
                "- Pronostic des AC récupérés fréquemment marqué par des séquelles neurologiques :\n"
                "  - État végétatif\n"
                "  - Séquelles motrices\n"
                "  - Séquelles cognitives\n"
                "- Nécessitent une longue rééducation\n"
                "- Peuvent conduire à une perte d'autonomie plus ou moins totale\n"
                "- Conséquences sociales et familiales à évaluer"
            )),
            FicheRow(concept="◆ Information de la famille", detail_md=(
                "- Échanges et information permanents mais contrôlés\n"
                "- Limiter les interlocuteurs côté hospitalier ET familial\n"
                "- Précocité de l'information : éclaire les possibilités évolutives et conséquences\n"
                "- Évite en général les situations conflictuelles\n"
                "- En cas de **mort cérébrale** avérée :\n"
                "  - Possibilités de **prélèvement d'organe** à évoquer\n"
                "  - Information de la famille\n"
                "  - Absence d'inscription au **registre national des refus** à vérifier"
            )),
            FicheRow(concept="◆ Éthique et décision d'arrêt", detail_md=(
                "- AC confronte le médecin aux principes de la déontologie médicale et de l'éthique\n"
                "- Responsabilité à assumer en contexte d'équipe de soins\n"
                "- **Décision d'arrêt de réanimation collégiale**, orientée par un algorithme précis "
                "de neuropronostication"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Survie selon la durée d'arrêt cardiaque", markdown=(
            "| Durée d'arrêt sans réanimation | Survie |\n"
            "|---|---|\n"
            "| **0 à 5 minutes** | Survie acceptable selon prise en charge |\n"
            "| **Au-delà de 5 minutes** | **7 à 8 %** |\n"
            "| **Au-delà de 10 minutes** | **Proche de 0** |\n"
            "| **Au-delà de 30 minutes** | **Nulle** |\n"
            "| Taux de décroissance | **–10 % par minute** sans réanimation |"
        )),
        TableauSynthese(titre="Délai de défibrillation et survie en FV", markdown=(
            "| Délai du 1ᵉʳ CEE | Survie après défibrillation |\n"
            "|---|---|\n"
            "| **1 à 3 minutes** | **40 à 60 %** |\n"
            "| **4 à 6 minutes** | **35 %** |\n"
            "| **7 à 10 minutes** | **25 %** |\n"
            "| **> 10 minutes** | **< 5 %** (survie sans séquelle rare) |"
        )),
        TableauSynthese(titre="Comparaison FV vs asystolie", markdown=(
            "| Caractéristique | FV (initiale) | Asystolie |\n"
            "|---|---|---|\n"
            "| Aspect ECG | Activité électrique chaotique (mailles) | Tracé plat |\n"
            "| Fréquence en début de RCP | **40-70 %** des cas | Plus rare initialement |\n"
            "| Traitement | **CEE** (défibrillation) | **MCE + adrénaline** (pas de CEE) |\n"
            "| Évolution naturelle | Dégrade vers asystolie (4-8ᵉ min : 50 %) | – |\n"
            "| Pronostic | **Meilleur** | **Péjoratif** |\n"
            "| Mécanisme | Trouble du rythme ventriculaire | Étiologie extracardiaque OU no-flow long |"
        )),
        TableauSynthese(titre="Principaux médicaments de la réanimation médicalisée", markdown=(
            "| Médicament | Indication | Posologie |\n"
            "|---|---|---|\n"
            "| **Adrénaline** | AC réfractaire en asystolie ; FV/TV persistante après 1ᵉʳ CEE | **1 mg IV/4 min** |\n"
            "| **Amiodarone** | TV/FV réfractaires aux CEE, juste avant le 3ᵉ choc | **300 mg IV** puis **150 mg** si récidive |\n"
            "| **Lidocaïne** | TV/FV (si pas d'amiodarone) | **1,5 mg/kg IV lente**, max **3 mg/kg** |\n"
            "| **Sulfate de magnésium** | Torsades de pointes ; hypomagnésémie | **2 g IV directe** |\n"
            "| **Atropine** | Bradycardies sinusales extrêmes | **1 mg/3-5 min**, max **0,04 mg/kg** |\n"
            "| **Isoprénaline** | BAV 3ᵉ degré sans hémodynamique | 5 amp. **0,2 mg** dans **250 cm³ G5%**, objectif ≥ 50-60 bpm |\n"
            "| **Bicarbonate 84 ‰** | Réa prolongée, hyperkaliémie, intoxication tricycliques/phénobarbital | – |"
        )),
        TableauSynthese(titre="Étiologies de l'arrêt cardiocirculatoire", markdown=(
            "| Catégorie | Causes principales |\n"
            "|---|---|\n"
            "| **Cardiopathies ischémiques** (1ʳᵉ cause) | **SCA inaugural** (40-77 % des morts subites) |\n"
            "| **Cardiomyopathies** | CMH (formes familiales/obstructives), CMD, DVDA, RAo |\n"
            "| **Troubles du rythme/conduction** | FV idiopathique, **Brugada**, **QT long**, **QT court**, **WPW**, troubles conductifs |\n"
            "| **Inflammatoire** | **Myocardite aiguë** |\n"
            "| **Autres CV** | Cardiopathies congénitales, **tamponnade**, **dissection aortique**, **EP massive**, **rupture d'anévrisme** |\n"
            "| **Non cardiovasculaires** (5-25 %) | **Toxiques**, **traumatiques**, **IRespA**, **noyades** |"
        )),
        TableauSynthese(titre="Acronyme ACD - mesures de survie préhospitalières", markdown=(
            "| Lettre | Mesure | Détails |\n"
            "|---|---|---|\n"
            "| **A : Airway** | Maintien des voies aériennes libres | Bascule de la tête, surélever le menton, retrait corps étranger, canule de Guedel ensuite |\n"
            "| **C : Circulation** | Massage cardiaque externe | Décubitus dorsal, talon de la main, **4-5 cm d'amplitude**, **100/min**, relais toutes les 2 min |\n"
            "| **D : Defibrillation** | Si rythme « chocable » (TV/FV) | DSA dès disponible, RCP 2 min après le choc |\n"
            "| **B : Breathing** | (bouche-à-bouche) | **Plus chez l'adulte** ; reste indiqué chez l'enfant/nourrisson (AC souvent hypoxique) |"
        )),
    ]

    # ── CHIFFRES CLÉS ──
    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|---|---|---|\n"
        "| Décès/an aux États-Unis (AC extrahosp.) | **300 000** | Épidémiologie |\n"
        "| Décès/an en Europe | **500 000** | Épidémiologie |\n"
        "| Décès/an en France | **40 000** | Épidémiologie |\n"
        "| Incidence en France | **0,75 ‰** | Population générale |\n"
        "| Survie au-delà de 5 min d'arrêt | **7 à 8 %** | Sans réanimation |\n"
        "| Survie au-delà de 10 min | **Proche de 0** | – |\n"
        "| Survie nulle | **30 minutes** | Au-delà |\n"
        "| Survie sans séquelles | **2 à 4 %** | Global |\n"
        "| Survie AC intrahospitalier | **40-50 %** | – |\n"
        "| Survie globale AC | **5-20 %** | – |\n"
        "| Sortie hôpital sans séquelles neurologiques | **20 %** des arrivés vivants | – |\n"
        "| ILCOR (sortie + reprise vie normale) | **2-10 %** | Grandes agglomérations équipées |\n"
        "| Taux de décroissance de survie | **–10 %/minute** | Sans réanimation |\n"
        "| No-flow critique | **> 5 minutes** | Mauvais pronostic |\n"
        "| No-flow rédhibitoire | **> 10 minutes** | Survie quasi nulle, question éthique |\n"
        "| AC réfractaire | **> 30 minutes** | Sans circulation spontanée |\n"
        "| FV initiale (début RCP) | **40-70 %** | Variable selon rapidité |\n"
        "| FV (ILCOR 2015) | **70-80 %** | Rythme initial |\n"
        "| Bradycardie extrême (ILCOR 2015) | **15-20 %** | – |\n"
        "| Dégradation FV → asystolie | **50 % entre 4ᵉ et 8ᵉ min** | – |\n"
        "| Lésions coronariennes dans mort subite | **40-77 %** | – |\n"
        "| AC compliquant un IDM | **20-40 %** | – |\n"
        "| AC extrahosp. avec IDM/EP | **~70 %** | – |\n"
        "| Étiologies non CV | **5-25 %** | – |\n"
        "| CEE biphasique | **jusqu'à 200 J** | Plus sûr/efficace |\n"
        "| CEE monophasique | **360 J** | Remplacé |\n"
        "| Survie FV CEE 1-3 min | **40-60 %** | – |\n"
        "| Survie FV CEE 4-6 min | **35 %** | – |\n"
        "| Survie FV CEE 7-10 min | **25 %** | – |\n"
        "| Survie FV CEE > 10 min | **< 5 %** | – |\n"
        "| Idéal 1ᵉʳ CEE | **≤ 3 minutes** | Après l'arrêt |\n"
        "| Compressions MCE | **4-5 cm** | Amplitude |\n"
        "| Fréquence MCE | **100/min** | – |\n"
        "| Relais MCE | **2 minutes** | Entre sauveteurs |\n"
        "| RCP après choc | **2 minutes** | Avant vérification |\n"
        "| Interruption MCE pour intubation | **< 30 secondes** | – |\n"
        "| Adrénaline | **1 mg/4 min** IV ou endotrachéale | Posologie |\n"
        "| Adrénaline limite pronostique | **1-2 mg** | Au-delà : survie sans séquelles quasi nulle |\n"
        "| Amiodarone dose initiale | **300 mg** IV (20-30 mL SSI) | Avant le 3ᵉ CEE |\n"
        "| Amiodarone dose itérative | **150 mg** | Si récidive |\n"
        "| Lidocaïne | **1,5 mg/kg** IV, max **3 mg/kg** | Si pas d'amiodarone |\n"
        "| Sulfate de magnésium | **2 g IV directe** | Torsades, hypoMg |\n"
        "| Atropine | **1 mg/3-5 min**, max **0,04 mg/kg** | Bradycardie sinusale |\n"
        "| Isoprénaline | **5 amp. 0,2 mg** dans **250 cm³ G5%**, objectif ≥ **50-60 bpm** | BAV 3 |\n"
        "| Désordres métaboliques | **3-4 min** après l'AC | Acidose + hyperK |\n"
        "| Formation RCP en France | **10-15 %** | Population |\n"
        "| Hypothermie contrôlée | **~34 °C** | Modérée, place débattue |\n"
        "| Sujet jeune sans coronaropathie | **< 30 ans** | Causes rythmiques ou congénitales |\n"
        "| Mort subite (OMS) délai max | **1 heure** | Symptômes la précédant |\n"
        "| Évaluations cérébrales (Glasgow, EEG, PES) | **J1 à J3** | Affinement |"
    ))

    # ── POINTS CLÉS ──
    points_cles = [
        "**Témoin** clé : appelle le **15** puis débute la RCP pour réduire le **no-flow**",
        "**ACD** : Airway (libérer VAS), Circulation (**MCE 4-5 cm, 100/min**), Defibrillation (TV/FV)",
        "**Survie décroît de 10 %/min** sans RCP ; no-flow > 10 min = survie quasi nulle",
        "**FV 70-80 %** des rythmes initiaux ; dégrade en **asystolie entre 4ᵉ et 8ᵉ min** (50 %)",
        "Défibrillation = seul ttt FV : **CEE biphasique 200 J**, idéal **≤ 3 min**",
        "**Adrénaline 1 mg IV/4 min** (asystolie) ; **amiodarone 300 mg** avant le **3ᵉ CEE**",
        "1ʳᵉ étiologie : **cardiopathies ischémiques** (SCA inaugural, **40-77 %** des morts subites)",
        "**Coronarographie au moindre doute** : ATCD CV, douleur thoracique, ECG évocateur de SCA",
        "Reprise hémodynamique ≠ survie : **20 % seulement** sortent sans séquelles neurologiques",
        "Cérébral : éviter **hypoxie, hypercapnie, hyperglycémie, hyperthermie** (**~34 °C** débattue)",
    ]

    # ── FICHE ÉCLAIR ──
    fiche_eclair_md = (
        "**ACC** : absence pouls + apnée/gasping. AC réfractaire après 30 min RCP. No-flow = sans RCP ; "
        "low-flow = RCP sans hémodynamique.\n\n"
        "**Épidémio** : France 40 000/an. Survie extrahosp. 5-20 %, intrahosp. 40-50 %, sans séquelles 2-4 %. "
        "Décroissance –10 %/min. No-flow > 5 min mauvais ; > 10 min quasi nul (encéphalopathie anoxique).\n\n"
        "**Chaîne de survie (6 maillons)** : témoin (15) → RCP → défibrillation → Smur → réa hospitalière → "
        "rétablissement. 10-15 % formés en France.\n\n"
        "**ACD** : A = airway (bascule tête, menton). C = MCE 4-5 cm, 100/min, relais 2 min, prioritaire. "
        "D = DSA si chocable. Pas de bouche-à-bouche chez l'adulte, maintenu chez l'enfant.\n\n"
        "**Défibrillation** : seul traitement FV. CEE biphasique 200 J. Idéal ≤ 3 min. "
        "Survie 1-3 min 40-60 %, 4-6 min 35 %, 7-10 min 25 %, > 10 min < 5 %.\n\n"
        "**Rythmes** : FV 70-80 % (dégrade en asystolie 4-8 min). Asystolie = MCE + adrénaline PAS de CEE. "
        "Dissociation EM = poursuivre MCE.\n\n"
        "**Étiologies** : 1ʳᵉ cause ischémique (SCA, 40-77 % morts subites). 70 % AC extrahosp. = IDM ou EP. "
        "Autres : CMH, Brugada, QT long, WPW, tamponnade, dissection Ao, EP massive. Non CV 5-25 % (toxiques, noyades).\n\n"
        "**Médicaments** : Adrénaline 1 mg IV/4 min. Amiodarone 300 mg puis 150 mg avant 3ᵉ choc. "
        "Lidocaïne 1,5 mg/kg max 3 mg/kg. Sulfate Mg 2 g (torsades). Atropine 1 mg/3-5 min. "
        "Bicarbonate 84 ‰ : intox tricycliques. Thrombolyse : IDM/EP massive uniquement.\n\n"
        "**Phase hospitalière** (5ᵉ maillon) : dobutamine ± ECMO, coronarographie au moindre doute. "
        "Cérébral = Glasgow/EEG/PES J1-J3, lutter hypoxie/hypercapnie/hyperglycémie/hyperthermie, "
        "hypothermie ~34 °C, sédation. 20 % sortent sans séquelles.\n\n"
        "**Éthique** : information précoce, interlocuteurs limités. Mort cérébrale : don d'organes. "
        "Décision d'arrêt collégiale."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 331 - Arrêt cardiocirculatoire",
        annee="2025-2026",
        item="Item 331",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi, partie_vii],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 331",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-331_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

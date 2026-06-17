"""Génère la fiche de l'Item 342 - Malaises, perte de connaissance, crise comitiale chez l'adulte (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Définitions et sémantique des PDCB", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définitions"),
            PlanSousPartie(lettre="B", titre="Autres états de conscience altérée"),
        ]),
        PlanPartie(numero="II", titre="Physiopathologie des PDCB", sous_parties=[
            PlanSousPartie(lettre="A", titre="Différences syncope, épilepsie, PDCB psychogène"),
            PlanSousPartie(lettre="B", titre="Syncopes"),
            PlanSousPartie(lettre="C", titre="Épilepsie et PDCB psychogènes"),
        ]),
        PlanPartie(numero="III", titre="Étiologies et classification des syncopes", sous_parties=[
            PlanSousPartie(lettre="A", titre="Causes cardiaques par obstacle mécanique"),
            PlanSousPartie(lettre="B", titre="Causes cardiaques rythmiques"),
            PlanSousPartie(lettre="C", titre="Hypotension artérielle orthostatique"),
            PlanSousPartie(lettre="D", titre="Syncopes réflexes"),
        ]),
        PlanPartie(numero="IV", titre="Diagnostic différentiel", sous_parties=[
            PlanSousPartie(lettre="A", titre="Autres états d'altération de conscience"),
            PlanSousPartie(lettre="B", titre="Autres causes de PDCB"),
        ]),
        PlanPartie(numero="V", titre="Prise en charge clinique et paraclinique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Interrogatoire"),
            PlanSousPartie(lettre="B", titre="Examen clinique"),
            PlanSousPartie(lettre="C", titre="Électrocardiogramme"),
            PlanSousPartie(lettre="D", titre="Première synthèse"),
            PlanSousPartie(lettre="E", titre="Examens supplémentaires"),
        ]),
        PlanPartie(numero="VI", titre="Critères de gravité", sous_parties=[
            PlanSousPartie(lettre="A", titre="Critères de surveillance et hospitalisation"),
            PlanSousPartie(lettre="B", titre="Situations à risque faible"),
        ]),
        PlanPartie(numero="VII", titre="Formes cliniques typiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Syncopes réflexes"),
            PlanSousPartie(lettre="B", titre="Hypotension orthostatique"),
            PlanSousPartie(lettre="C", titre="Trouble du rythme/conduction"),
            PlanSousPartie(lettre="D", titre="Notions indispensables et transversalités"),
        ]),
    ]

    # ── PARTIE I : DÉFINITIONS ET SÉMANTIQUE ──
    partie_i = Partie(numero="I", titre="Définitions et sémantique des PDCB", sous_parties=[
        SousPartie(lettre="A", titre="Définitions", rows=[
            FicheRow(concept="◆ Malaise", detail_md=(
                "- Indisposition, gêne, trouble ou \"mal-être\" : sensation pénible vague d'un trouble des fonctions physiologiques\n"
                "- N'est PAS un terme médical mais une plainte ou un motif de recours aux soins\n"
                "- Après le premier contact médical, il faut établir s'il y a eu **perte de connaissance brève (PDCB)**"
            )),
            FicheRow(concept="◆ Perte de connaissance brève (PDCB)", detail_md=(
                "- État réel ou apparent de perte de la conscience avec :\n"
                "  - **Amnésie** de cette période\n"
                "  - Perte du contrôle de la motricité\n"
                "  - Perte de la réactivité\n"
                "  - De courte durée\n"
                "- On oppose d'abord les PDCB traumatiques aux PDCB non traumatiques"
            )),
            FicheRow(concept="◆ Classification des PDCB non traumatiques", detail_md=(
                "- **3 catégories principales** se distinguant par leur physiopathologie "
                "(la présentation sémiologique peut être voisine et trompeuse) :\n"
                "  - **Syncopes** : hypoperfusion cérébrale\n"
                "  - **Crises d'épilepsie** : hyperactivité cérébrale\n"
                "  - **PDCB psychogènes** : phénomène de conversion"
            )),
            FicheRow(concept="★ ◆ Syncope", detail_md=(
                "- PDCB due à une **hypoperfusion cérébrale**\n"
                "- Déclenchement rapide et récupération complète et spontanée\n"
                "- Après l'événement : état neurologique normal (comportement, orientation)\n"
                "- Le patient n'a pas de souvenir enregistré pendant la période de PDCB"
            )),
            FicheRow(concept="Prodromes et lipothymie", detail_md=(
                "- **Prodromes** : signes et symptômes qui précèdent la syncope\n"
                "- **Lipothymie (présyncope)** : la symptomatologie se limite aux prodromes "
                "et la PDCB ne survient pas\n"
                "- Peut se résumer à une sensation imminente de syncope"
            )),
            FicheRow(concept="Syncope « à l'emporte-pièce »", detail_md=(
                "- Syncope sans prodromes\n"
                "- Ancien terme : **syncope de Stokes-Adams** = syncope sans prodrome avec "
                "pâleur, **durée < 30 secondes**, retour abrupt à la conscience\n"
                "- Cause généralement rythmique"
            )),
            FicheRow(concept="", detail_md=(
                "- **3 grandes catégories de PDCB non traumatiques** : syncope (hypoperfusion), "
                "épilepsie (hyperactivité), psychogène (conversion).\n"
                "- Syncope = hypoperfusion cérébrale, début brutal, récupération spontanée complète, "
                "amnésie de l'épisode, état neurologique normal au réveil."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Autres états de conscience altérée", rows=[
            FicheRow(concept="Causes très rares de PDCB", detail_md=(
                "- **AIT vertébrobasilaires** : "
                "perte prolongée, déficit focal (vertiges, ataxie, nystagmus, faiblesse "
                "des membres inférieurs, diplopie, dysarthrie)\n"
                "- **Syndrome de vol sous-clavier** : AIT déclenché par mouvements intenses "
                "et répétés du membre supérieur gauche, différence de PA entre les 2 bras\n"
                "- **HSA** : perte progressive, "
                "céphalées sévères et signes neurologiques\n"
                "- ⚠ **AIT carotidien** : ne donne quasiment jamais de PDCB, déficit focal"
            )),
            FicheRow(concept="Comas", detail_md=(
                "- Perte de connaissance très prolongée\n"
                "- Sortie progressive ou après manœuvres thérapeutiques\n"
                "- Causes toxiques possibles : monoxyde de carbone, médicaments, alcool, etc."
            )),
            FicheRow(concept="Confusion mentale", detail_md=(
                "- **Pas de perte de connaissance**\n"
                "- Déficit d'attention et de concentration\n"
                "- Désorientation, hallucinations, propos incohérents, état d'agitation\n"
                "- Désordre métabolique : hypoglycémie, hypoxie, hypocapnie, etc."
            )),
            FicheRow(concept="Cataplexie", detail_md=(
                "- Perte brusque du tonus musculaire, parfois avec chute\n"
                "- **Sans PDCB**, déclencheur = émotion\n"
                "- Pas d'amnésie\n"
                "- **Narcolepsie** = cataplexie + accès irrépressibles de sommeil pluriquotidiens "
                "+ paralysies de début de sommeil + hypnagogies (états intermédiaires veille/sommeil)"
            )),
            FicheRow(concept="⚠ Drop-attacks", detail_md=(
                "- Terme à éviter qui prête à confusion\n"
                "- Regroupe des formes rares d'épilepsie, la maladie de Ménière et "
                "les chutes inexpliquées\n"
                "- Souvent femmes d'âge mûr rapportant des chutes brèves dont elles se "
                "souviennent parfaitement et se relèvent immédiatement"
            )),
            FicheRow(concept="Arrêt cardiaque", detail_md=(
                "- Le retour à une conscience normale fait suite à une réanimation"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ **Confusion mentale ≠ PDCB** (pas de perte de conscience, déficit attentionnel).\n"
                "- ⚠ **Cataplexie ≠ syncope** (pas de PDCB, pas d'amnésie, déclencheur émotionnel)."
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE II : PHYSIOPATHOLOGIE DES PDCB ──
    partie_ii = Partie(numero="II", titre="Physiopathologie des PDCB", sous_parties=[
        SousPartie(lettre="A", titre="Différences syncope, épilepsie, PDCB psychogène", rows=[
            FicheRow(concept="◆ Mécanismes opposés", detail_md=(
                "- **Syncope** : hypoperfusion cérébrale\n"
                "- **Épilepsie** : hyperactivité cérébrale\n"
                "- **PDCB psychogène** : phénomène de conversion"
            )),
        ]),
        SousPartie(lettre="B", titre="Syncopes", rows=[
            FicheRow(concept="◆ Mécanisme général", detail_md=(
                "- Baisse de la pression artérielle → diminution globale du flux sanguin cérébral\n"
                "- **Arrêt brutal du flux ≥ 6-8 secondes** → syncope\n"
                "- **PAS 50-60 mmHg au cœur** (verticale) → PA cérébrale **30-45 mmHg** → syncope\n"
                "- La substance réticulée activatrice du tronc cérébral provoque la PDCB "
                "quand elle ne reçoit pas ses besoins en oxygène"
            )),
            FicheRow(concept="⚠ Distinction avec AVC", detail_md=(
                "- La baisse globale du flux sanguin cérébral **≠ AVC**\n"
                "- Le mécanisme et la présentation clinique des AVC n'ont rien à voir avec les syncopes"
            )),
            FicheRow(concept="◆ Causes de baisse de PA", detail_md=(
                "- **Baisse du débit cardiaque** :\n"
                "  - Bradycardie\n"
                "  - Tachycardie\n"
                "  - Baisse du retour veineux (déplétion, spoliation veineuse)\n"
                "  - Obstacle à la circulation sanguine\n"
                "- **Baisse des résistances périphériques** (vasodilatation) :\n"
                "  - Réflexe levant le tonus sympathique vasoconstricteur (syncope réflexe)\n"
                "  - Dysautonomie primitive ou secondaire\n"
                "  - Médicaments"
            )),
            FicheRow(concept="⚠ Myoclonies de la syncope", detail_md=(
                "- **NE PAS confondre avec l'épilepsie**\n"
                "- Secousses brèves souvent des épaules\n"
                "- **Durée < 15 secondes**\n"
                "- Débutent **TOUJOURS APRÈS la perte de connaissance** "
                "(le plus souvent après la 30ᵉ seconde)\n"
                "- ⚠ Éviter le terme « syncope convulsivante »"
            )),
            FicheRow(concept="", detail_md=(
                "- Arrêt brutal du flux cérébral pendant **6 à 8 secondes** suffit à provoquer une syncope.\n"
                "- Une **PAS à 50-60 mmHg au cœur** en position verticale → syncope."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Épilepsie et PDCB psychogènes", rows=[
            FicheRow(concept="Crises d'épilepsie causant une PDCB", detail_md=(
                "- Seules les **crises généralisées** (toniques, cloniques, tonicocloniques ou atoniques) "
                "sont des causes de PDCB\n"
                "- En raison de la perte du contrôle de la motricité\n"
                "- Crises partielles en position debout/assise = généralement pas des causes de PDCB"
            )),
            FicheRow(concept="◆ PDCB psychogènes", detail_md=(
                "- **2 formes** :\n"
                "  - L'une imite l'épilepsie\n"
                "  - L'autre imite la syncope\n"
                "- Souvent prolongées\n"
                "- Se répètent plusieurs fois par jour\n"
                "- **Phénomène de conversion**"
            )),
        ]),
    ])

    # ── PARTIE III : ÉTIOLOGIES ET CLASSIFICATION DES SYNCOPES ──
    partie_iii = Partie(numero="III", titre="Étiologies et classification des syncopes", sous_parties=[
        SousPartie(lettre="A", titre="Causes cardiaques par obstacle mécanique", rows=[
            FicheRow(concept="◆ Principe", detail_md=(
                "- Obstacle à la circulation sanguine : soit systémique, soit pulmonaire\n"
                "- Effondrement de la PA par chute du débit cardiaque"
            )),
            FicheRow(concept="◆ Rétrécissement aortique serré", detail_md=(
                "- **Syncope à l'effort** ++"
            )),
            FicheRow(concept="◆ Cardiomyopathies hypertrophiques (CMH) avec obstruction", detail_md=(
                "- Le plus souvent d'origine **génétique**\n"
                "- Mutations des gènes codant pour les **protéines du sarcomère**\n"
                "- Transmission **autosomique dominante**\n"
                "- Hypertrophie du septum interventriculaire → obstacle sur la chambre de chasse du VG "
                "en s'apposant à la grande valvule mitrale\n"
                "- Souffle systolique éjectionnel au bord gauche du sternum\n"
                "- **Syncopes à l'effort** ou juste après l'effort"
            )),
            FicheRow(concept="◆ Embolie pulmonaire", detail_md=(
                "- Thrombus occlusif dans le tronc de l'artère pulmonaire ou la "
                "chambre de chasse du VD\n"
                "- Souvent **EP à haut risque** (avec état de choc)"
            )),
            FicheRow(concept="Tamponnade", detail_md=(
                "- Épanchement péricardique comprimant les cavités cardiaques à basse pression, "
                "dont le ventricule droit"
            )),
            FicheRow(concept="Causes moins fréquentes", detail_md=(
                "- **Thrombose de valve mécanique** (mitrale) — possiblement associée à une "
                "endocardite bactérienne\n"
                "- Tumeurs cardiaques (myxomes)\n"
                "- Dissection aortique\n"
                "- Hypertension pulmonaire sévère"
            )),
            FicheRow(concept="", detail_md=(
                "- L'**insuffisance cardiaque sévère stade IV** ou l'**état de choc** peuvent donner "
                "une confusion mentale ou un trouble de conscience, "
                "mais **ne sont JAMAIS une cause de syncope** en soi."
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Causes cardiaques rythmiques", rows=[
            FicheRow(concept="★ ◆ Troubles conductifs (bradycardie/pause)", detail_md=(
                "- **BAV** :\n"
                "  - **BAV du 3ᵉ degré** surtout infrahissien\n"
                "  - BAV de haut degré\n"
                "  - **BAV du 2ᵉ degré Mobitz 2**\n"
                "  - Plus rarement les autres formes de BAV du 2ᵉ degré\n"
                "- **Dysfonction sinusale** :\n"
                "  - Pauses **> 6 secondes** (parfois moins chez le sujet âgé)\n"
                "  - Possible maladie de l'oreillette / syndrome tachycardie-bradycardie : "
                "FA paroxystique + dysfonction sinusale (pauses de régularisation au retour en rythme sinusal)\n"
                "- **Défaillance de pacemaker** :\n"
                "  - Posé pour BAV ou dysfonction sinusale\n"
                "  - Sonde déplacée ou rompue\n"
                "  - Usure de la batterie"
            )),
            FicheRow(concept="◆ Troubles du rythme (tachycardie)", detail_md=(
                "- **TV** :\n"
                "  - Surtout associées à la maladie coronarienne (SCA avec/sans sus-décalage ST, "
                "phase séquellaire d'IDM parfois des années plus tard)\n"
                "  - Cardiomyopathies dilatées, hypertrophiques ou restrictives "
                "(primitives ou secondaires)\n"
                "  - Cardiomyopathie/dysplasie arythmogène du VD (maladie génétique)\n"
                "- **Torsades de pointes** :\n"
                "  - Surviennent en présence d'un **allongement du QT**\n"
                "  - Si dégénèrent en FV → arrêt cardiaque et non syncope\n"
                "- **TSV** :\n"
                "  - Exceptionnellement responsables de syncopes"
            )),
        ]),
        SousPartie(lettre="C", titre="Hypotension artérielle orthostatique", rows=[
            FicheRow(concept="◆ Définition (1ʳᵉ cause de syncope)", detail_md=(
                "- C'est la **1ʳᵉ cause de syncope**\n"
                "- **Critères** dans les **1 à 3 minutes** suivant le passage à l'orthostatisme :\n"
                "  - **Baisse ≥ 20 mmHg de la PAS**, OU\n"
                "  - **Baisse ≥ 10 mmHg de la PAD**, OU\n"
                "  - **PAS < 90 mmHg**"
            )),
            FicheRow(concept="Facteurs favorisants", detail_md=(
                "- Effort préalable\n"
                "- Période postprandiale\n"
                "- Alitement prolongé"
            )),
            FicheRow(concept="◆ Causes médicamenteuses", detail_md=(
                "- **Vasodilatateurs** : nitrés, inhibiteurs calciques, "
                "inhibiteurs du SRAA (IEC, ARA II)\n"
                "- **Diurétiques**\n"
                "- **Psychotropes**\n"
                "- **Antiparkinsoniens**"
            )),
            FicheRow(concept="Causes hypovolémiques", detail_md=(
                "- Déshydratation\n"
                "- Diarrhée, vomissements\n"
                "- Hémorragie\n"
                "- Insuffisance surrénalienne"
            )),
            FicheRow(concept="Dysautonomie", detail_md=(
                "- **Dysautonomie primaire** :\n"
                "  - Maladie de Parkinson\n"
                "  - Maladie à corps de Lewy\n"
                "- **Dysautonomie secondaire** :\n"
                "  - Diabète\n"
                "  - Amylose\n"
                "  - Neuropathies paranéoplasiques"
            )),
        ]),
        SousPartie(lettre="D", titre="Syncopes réflexes", rows=[
            FicheRow(concept="◆ Syncope vasovagale", detail_md=(
                "- Syncope réflexe s'accompagnant de **bradycardie** ou de **vasodilatation** "
                "ou des deux\n"
                "- Activation du parasympathique → bradycardie\n"
                "- Baisse du tonus sympathique → vasodilatation et hypotension\n"
                "- La composante cardio-inhibitrice peut être spectaculaire avec "
                "**asystolie de plusieurs secondes** ou dizaines de secondes"
            )),
            FicheRow(concept="◆ Syncopes situationnelles", detail_md=(
                "- À la **miction**\n"
                "- Aux **vomissements**\n"
                "- À la **défécation**\n"
                "- À la **toux** (ictus laryngé)\n"
                "- Aux éternuements\n"
                "- Après un effort intense\n"
                "- À la **manœuvre de Valsalva** (trompettistes)"
            )),
            FicheRow(concept="◆ Syndrome du sinus carotidien", detail_md=(
                "- Aussi appelé **hyperréflectivité sinocarotidienne**\n"
                "- Mise en jeu du baroréflexe à la striction cervicale\n"
                "- Compression du glomus carotidien : rasage, cravate, etc."
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Il s'agit du **sinus (glomus) de l'artère carotide**, "
                "**PAS du nœud sinusal** ! Ne pas confondre."
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE IV : DIAGNOSTIC DIFFÉRENTIEL ──
    partie_iv = Partie(numero="IV", titre="Diagnostic différentiel", sous_parties=[
        SousPartie(lettre="A", titre="Autres états d'altération de conscience", rows=[
            FicheRow(concept="Coma et arrêt cardiaque", detail_md=(
                "- États au cours desquels la perte de connaissance n'est ni brève ni "
                "de résolution spontanée"
            )),
            FicheRow(concept="Cataplexie, confusion mentale, drop-attacks", detail_md=(
                "- **Pas de perte de connaissance** dans ces états"
            )),
            FicheRow(concept="Chutes et PDCB traumatiques", detail_md=(
                "- Chutes sans perte de connaissance (notamment personne âgée) OU\n"
                "- PDCB traumatiques\n"
                "- L'interrogatoire et l'examen clinique redressent le diagnostic"
            )),
        ]),
        SousPartie(lettre="B", titre="Autres causes de PDCB", rows=[
            FicheRow(concept="AIT et AVC", detail_md=(
                "- Contexte différent\n"
                "- Ces accidents ne sont que de façon rarissime responsables de PDCB"
            )),
            FicheRow(concept="◆ PDCB psychogènes", detail_md=(
                "- Plus difficiles à écarter\n"
                "- Rythme cardiaque, PA et EEG normaux au moment des faits\n"
                "- **Éléments en faveur** :\n"
                "  - Résistance à l'ouverture des yeux\n"
                "  - **Durée > 15 minutes** de la perte de connaissance\n"
                "  - Répétition fréquente dans la même semaine"
            )),
            FicheRow(concept="◆ Diagnostic différentiel syncope vs crise comitiale", detail_md=(
                "| Élément | Syncope | Crise comitiale |\n"
                "|---------|---------|------------------|\n"
                "| **Mécanisme** | Hypoperfusion cérébrale | Hyperactivité cérébrale |\n"
                "| **Aura** | Non | Possible |\n"
                "| **Survenue pendant le sommeil** | Non | Possible |\n"
                "| **Durée PDCB** | Courte | Plus longue |\n"
                "| **Mouvements tonicocloniques** | Myoclonies < 15 s, après la PDCB | Prolongés, contemporains |\n"
                "| **Automatismes** | Non | Possible |\n"
                "| **Morsure de langue** | Non (sauf accidentelle apicale) | **Bord latéral profond** |\n"
                "| **Cyanose visage** | Pâleur typique | Cyanose possible |\n"
                "| **Phase post-critique** | Récupération rapide | Confusion prolongée, céphalées, courbatures, somnolence |"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La **perte des urines** et la **fatigue avec envie de dormir après la PDCB** "
                "**ne sont PLUS dans le tableau du CEC** car considérées comme **peu discriminantes**."
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE V : PRISE EN CHARGE CLINIQUE ET PARACLINIQUE ──
    partie_v = Partie(numero="V", titre="Prise en charge clinique et paraclinique", sous_parties=[
        SousPartie(lettre="A", titre="Interrogatoire", rows=[
            FicheRow(concept="◆ Objectifs", detail_md=(
                "- Confirmer la PDCB\n"
                "- Écarter si possible épilepsie et PDCB psychogène\n"
                "- Préciser les éléments clés orientant le diagnostic"
            )),
            FicheRow(concept="◆ Éléments clés à préciser", detail_md=(
                "- Âge\n"
                "- **ATCD familiaux de mort subite** → cause génétique\n"
                "- **ATCD personnels de cardiopathie** → cause cardiaque\n"
                "- Prises médicamenteuses (surtout hypotenseurs, modification récente)\n"
                "- Causes de dysautonomie : diabète, maladie de Parkinson, etc."
            )),
            FicheRow(concept="◆ Caractérisation de l'épisode", detail_md=(
                "- **Prodromes** (parfois absents) — distinguer d'une **aura** comitiale\n"
                "- Douleur thoracique ou dyspnée → diagnostics prioritaires\n"
                "- Nausées ou sueurs froides classiques des syncopes vasovagales\n"
                "- Posture au moment de la syncope : debout - assis - couché\n"
                "- Activité : effort ou repos\n"
                "- Facteur déclenchant : douleur, émotion, phobie du sang, prélèvement, "
                "période postprandiale, station debout prolongée, confinement, chaleur"
            )),
            FicheRow(concept="◆ Recueil auprès des témoins", detail_md=(
                "- Mouvements anormaux : crise tonicoclonique ou simples myoclonies\n"
                "- **Contemporains** (crise comitiale) ou **retardés** (myoclonies de la syncope) "
                "par rapport à la perte de connaissance\n"
                "- Durée (attention à l'amnésie passagère)\n"
                "- Mode de réveil : brutal ou progressif, phase post-critique\n"
                "- Nausées, vomissements, sueurs abondantes, sensation de froid\n"
                "- Courbatures au réveil (crise comitiale)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Prendre avec prudence la notion d'**abolition du pouls** rapportée par un témoin : "
                "le pouls radial peut être imperceptible en cas d'hypotension, "
                "surtout en climat de panique."
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Examen clinique", rows=[
            FicheRow(concept="Examen neurologique", detail_md=(
                "- Recherche des signes déficitaires\n"
                "- En cas d'anomalies ou d'altération prolongée de l'état de conscience "
                "(confusion, coma) → on quitte le domaine cardiovasculaire\n"
                "- **Morsure du bord latéral de la langue** → évoque une crise comitiale\n"
                "- Recherche d'insomnie, stimulation lumineuse, sevrage médicamenteux ou éthylique\n"
                "- Mouvements anormaux, déficits transitoires, syndrome confusionnel post-critique"
            )),
            FicheRow(concept="◆ Examen cardiovasculaire", detail_md=(
                "- Permet souvent d'identifier les syncopes mécaniques :\n"
                "  - Souffle systolique de **rétrécissement aortique**\n"
                "  - Signes de cœur pulmonaire aigu\n"
                "  - Assourdissement des bruits d'une prothèse mécanique"
            )),
            FicheRow(concept="◆ Mesure de la PA - recherche de l'HTO", detail_md=(
                "- PA au décours immédiat de la syncope : valeur d'orientation +++\n"
                "- Hypotension prolongée → cause iatrogène ou réflexe\n"
                "- **Recherche d'HTO** :\n"
                "  - PA mesurée allongé\n"
                "  - Puis toutes les minutes pendant **3 minutes** de passage à l'orthostatisme\n"
                "- La survenue de symptômes en cas d'HTO en renforce l'imputabilité"
            )),
        ]),
        SousPartie(lettre="C", titre="Électrocardiogramme", rows=[
            FicheRow(concept="◆ Anomalies permettant de faire le diagnostic", detail_md=(
                "- Dysfonction sinusale avec **bradycardie < 40 bpm** ou **pauses > 3 secondes** "
                "chez un patient éveillé\n"
                "- **TV**\n"
                "- **Torsades de pointes**\n"
                "- **BAV complet** (3ᵉ degré) ou 2ᵉ degré type **Mobitz 2**\n"
                "- **Bloc de branche alternant** (bloc trifasciculaire)\n"
                "- TSV rapide (en pratique **> 150 bpm**)\n"
                "- Défaillance d'un stimulateur ou défibrillateur avec pauses cardiaques"
            )),
            FicheRow(concept="◆ Anomalies qui orientent le diagnostic", detail_md=(
                "- Bradycardie **40-50 bpm** ou pauses **< 3 secondes** → dysfonction sinusale\n"
                "- BAV 2ᵉ degré type Mobitz 1, BBG, bloc bifasciculaire → "
                "**BAV paroxystique**\n"
                "- Syndrome de **Wolff-Parkinson-White** → cause rythmique\n"
                "- ESV nombreuses ou en salves → TV\n"
                "- Allongement du **QT** → torsade de pointes\n"
                "- Syndrome de **Brugada** (sus-décalage convexe ST en V1-V3 sans miroir) → "
                "anomalie génétique (FV → syncope si résolutive, mort subite sinon)\n"
                "- HVG, anomalies de repolarisation, onde Q de nécrose → SCA, séquelle d'IDM, "
                "cardiopathies structurelles → poursuivre vers TV sur séquelle d'IDM"
            )),
            FicheRow(concept="", detail_md=(
                "- **Anomalies ECG diagnostiques** (à mémoriser) :\n"
                "  - **TV**\n"
                "  - **Bradycardie sinusale < 40 bpm**\n"
                "  - **Pauses > 3 secondes**\n"
                "  - **BAV complet ou Mobitz 2**\n"
                "  - **Bloc de branche alternant**\n"
                "  - **TSV rapide > 150 bpm**\n"
                "  - **Torsade de pointes**\n"
                "  - **Défaillance de pacemaker/défibrillateur**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Première synthèse", rows=[
            FicheRow(concept="◆ Bilan à l'issue de la clinique + ECG", detail_md=(
                "- **> 50 % des cas** : la cause est identifiée à ce stade\n"
                "- Possibilités à l'issue de cette synthèse :\n"
                "  - Sortie du cadre des syncopes : douleur thoracique, dyspnée, vertige, etc.\n"
                "  - Altération de conscience non PDCB : coma, confusion mentale\n"
                "  - PDCB mais pas syncope : ex. épilepsie\n"
                "  - Déficit neurologique → **urgence neurovasculaire**\n"
                "- Si diagnostic non établi mais anomalies ECG d'orientation OU cardiopathie sous-jacente :\n"
                "  - Hypothèse dominante = **trouble du rythme ventriculaire** annonciateur de mort subite\n"
                "- Si ECG normal et clinique normale : poursuivre les examens paracliniques\n"
                "- Parfois : SCA ou IDM révélé par la syncope, conditionnant la prise en charge"
            )),
        ]),
        SousPartie(lettre="E", titre="Examens supplémentaires", rows=[
            FicheRow(concept="◆ Échocardiographie", detail_md=(
                "- **Utilisation très large, quasi systématique**\n"
                "- Peut donner le diagnostic : thrombose de valve mécanique, CMH obstructive\n"
                "- Peut confirmer une hypothèse : rétrécissement aortique, embolie pulmonaire\n"
                "- Peut montrer une séquelle d'IDM ou autre cardiopathie\n"
                "- Identifie les situations à risque vital\n"
                "- Si cardiopathie structurelle du VG (CMD, ischémique) avec **altération de la FEVG** : "
                "**défibrillateur implantable** en prévention de la mort subite"
            )),
            FicheRow(concept="Épreuve d'effort", detail_md=(
                "- Syncope pendant ou juste après effort → cause **cardiaque** (ex. BAV à l'effort)\n"
                "- Syncope après l'effort → syncope réflexe"
            )),
            FicheRow(concept="Biomarqueurs", detail_md=(
                "- **BNP / NT-proBNP** et **troponine** : utiles pour identifier une cause cardiaque"
            )),
            FicheRow(concept="◆ Monitorage ECG externe (Holter)", detail_md=(
                "- Obligatoire aux urgences en cas de risque vital avéré ou suspecté "
                "(causes cardiaques)\n"
                "- Méthode Holter en ambulatoire : **24 heures à 3 semaines**\n"
                "- Pour patients non à haut risque vital et syncopes/lipothymies fréquentes\n"
                "- **Sensible** pour : dysfonction sinusale, troubles de conduction AV nodaux\n"
                "- **Normal n'écarte PAS** : trouble du rythme ventriculaire, BAV hissien ou infrahissien paroxystique\n"
                "- Rendement faible mais examen peu onéreux et non invasif"
            )),
            FicheRow(concept="◆ Massage du sinus carotidien", detail_md=(
                "- Réalisé **couché puis debout**\n"
                "- Massage ferme et unilatéral d'une artère carotide puis de l'autre\n"
                "- Au bord antérieur du SCM, au niveau du cartilage cricoïde\n"
                "- Durée : **5 à 10 secondes**\n"
                "- **Positivité** : **pause > 3 s** OU **baisse PAS > 50 mmHg** "
                "reproduisant les symptômes\n"
                "- **Indication** : présomption de syncope réflexe sans cause identifiée\n"
                "- ⚠ **Contre-indications** : AIT, AVC, sténose artérielle carotidienne"
            )),
            FicheRow(concept="◆ Étude électrophysiologique endocavitaire (EEP)", detail_md=(
                "- **Indication** : syncope non élucidée + cardiopathie sous-jacente OU anomalies ECG "
                "(bloc bifasciculaire, BBG) quand l'ECG ne donne pas le diagnostic\n"
                "- **Réalisation** :\n"
                "  - Asepsie, consentement\n"
                "  - Salle de cathétérisme, voie veineuse fémorale\n"
                "  - Anesthésie locale + sédation légère\n"
                "  - 2-3 sondes : recueil du faisceau de His, mesure de l'**intervalle HV** "
                "(conduction infrahissienne)\n"
                "  - Stimulation atriale à fréquence croissante (conduction AV)\n"
                "  - **Stimulation ventriculaire programmée (SVP)** pour déclenchement de TV\n"
                "  - Tests pharmacologiques éventuels\n"
                "  - Surveillance du point de ponction, mobilisation à **4 h**\n"
                "- Non proposée : cœur morphologiquement normal + ECG normal "
                "(sauf si syncope précédée de palpitations)"
            )),
            FicheRow(concept="MAPA", detail_md=(
                "- Monitoring ambulatoire de la PA : peut suggérer une HTO\n"
                "- Fréquente hypertension nocturne paradoxale chez ces patients"
            )),
            FicheRow(concept="◆ Test d'inclinaison (tilt-test)", detail_md=(
                "- Recherche une susceptibilité hypotensive\n"
                "- Reproduit les syncopes vasovagales (debout prolongée)\n"
                "- Utile pour PDCB psychogène avec ECG/PA normaux\n"
                "- **Réalisation** :\n"
                "  - Environnement calme, patient à jeun\n"
                "  - Surveillance continue PA et ECG\n"
                "  - Décubitus initial **≥ 5 min**\n"
                "  - Table basculante : **60° à 70°**, tête en haut\n"
                "  - Inclinaison **20 à 45 min** au plus\n"
                "  - Sensibilisation : **isoprénaline** ou **trinitrine sublinguale**\n"
                "  - Positivité : syncope vasovagale avec hypotension et/ou bradycardie\n"
                "- ⚠ Prudence : peut être positif chez des patients dont la cause de la syncope est cardiaque\n"
                "- Rôle contesté dans les syncopes totalement inexpliquées"
            )),
            FicheRow(concept="◆ Monitorage ECG implantable (MEI)", detail_md=(
                "- Part grandissante dans la prise en charge\n"
                "- **Autonomie > 2 ans**\n"
                "- Permet d'associer les symptômes à une anomalie ECG quand syncopes espacées\n"
                "- **NON indiqué** chez patients à haut risque de mort subite "
                "(relèvent de défibrillateur/pacemaker)\n"
                "- **Indications** :\n"
                "  - EEP négative avec suspicion de faux négatif (BBG, bloc bifasciculaire, séquelle d'IDM)\n"
                "  - Syncopes cliniquement sévères, fréquentes et totalement inexpliquées\n"
                "- Lien transversalité : Items 17/18 (télémédecine, télésanté)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Les **TV sont la 1ʳᵉ cause de mort subite** des patients cardiaques.\n"
                "- ⚠ La syncope peut en être l'élément annonciateur.\n"
                "- ⚠ **Sanction thérapeutique** en cas de déclenchement de TV à l'EEP : "
                "pose d'un **défibrillateur automatique intracorporel (DAI)**."
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE VI : CRITÈRES DE GRAVITÉ ──
    partie_vi = Partie(numero="VI", titre="Critères de gravité", sous_parties=[
        SousPartie(lettre="A", titre="Critères de surveillance et hospitalisation", rows=[
            FicheRow(concept="◆ Critères justifiant le maintien aux urgences / unité syncope / hospitalisation", detail_md=(
                "- **ATCD familiaux de mort subite à un jeune âge**\n"
                "- ATCD personnels : cardiopathie, insuffisance cardiaque, IDM, "
                "**altération connue de la FEVG**\n"
                "- **Caractéristiques de la syncope** :\n"
                "  - À l'effort\n"
                "  - Précédée de palpitations\n"
                "  - En position couchée\n"
                "- **Symptôme grave associé** :\n"
                "  - Douleur thoracique\n"
                "  - Douleur abdominale\n"
                "  - Céphalées\n"
                "  - Dyspnée brutale\n"
                "  - Syncope avec chute responsable d'un traumatisme grave\n"
                "- Souffle systolique éjectionnel\n"
                "- Anomalie ECG diagnostique ou d'orientation"
            )),
        ]),
        SousPartie(lettre="B", titre="Situations à risque faible", rows=[
            FicheRow(concept="◆ Critères autorisant le retour à domicile / consultation ultérieure", detail_md=(
                "- **Diagnostic évident de syncope réflexe** :\n"
                "  - Épisodes répétés identiques depuis plusieurs années\n"
                "  - HTO avec mesures appropriées prises\n"
                "- Examen clinique normal + ECG normal\n"
                "- Absence d'ATCD ou de signe en faveur d'une cardiopathie sous-jacente"
            )),
        ]),
    ])

    # ── PARTIE VII : FORMES CLINIQUES TYPIQUES ──
    partie_vii = Partie(numero="VII", titre="Formes cliniques typiques", sous_parties=[
        SousPartie(lettre="A", titre="Syncopes réflexes", rows=[
            FicheRow(concept="◆ Contextes typiques", detail_md=(
                "- **Syncopes vasovagales** :\n"
                "  - Station debout prolongée, confinement, lieux publics, transports en commun, chaleur\n"
                "  - Douleur, émotion, vue du sang, stimulus olfactif désagréable\n"
                "  - Rarement en position assise\n"
                "- **Syndrome du sinus carotidien** :\n"
                "  - Rasage, mouvements du cou, col trop serré, appui sur le cou\n"
                "- **Syncopes situationnelles** :\n"
                "  - Miction, défécation, après effort intense, toux, stimulation douloureuse pharyngée\n"
                "- Facteurs favorisants communs : nuit, chaleur, période postprandiale"
            )),
            FicheRow(concept="Terrain typique", detail_md=(
                "- **Syncopes vasovagales** : sujet jeune souvent anxieux, émotif ou dépressif, "
                "récidives rapprochées et phases de rémission, passé ancien de syncopes répétées **avant 40 ans**\n"
                "- **Syndrome du sinus carotidien** : homme âgé"
            )),
            FicheRow(concept="◆ Description typique de la syncope vasovagale", detail_md=(
                "- Syncope progressive ou brutale (parfois traumatisante)\n"
                "- **Prodromes** : nausées, vue trouble, faiblesse des jambes, sueurs\n"
                "- Tégument souvent pâle\n"
                "- Myoclonies possibles\n"
                "- Bradycardie parfois sévère avec asystolie\n"
                "- **Conduite** : allonger le patient et surélever ses jambes\n"
                "- Phase de récupération : fatigue et intolérance à la station debout\n"
                "- Les syncopes les plus fréquentes sur cœur sain et ECG normal"
            )),
            FicheRow(concept="◆ Prise en charge (mesures non pharmacologiques)", detail_md=(
                "- Réassurance sur le caractère bénin de l'affection\n"
                "- **Éducation** : éviter les facteurs déclenchants et situations favorisantes\n"
                "- Reconnaissance précoce des prodromes → s'asseoir ou se coucher\n"
                "- Contractions musculaires volontaires isométriques pour limiter la chute de PA\n"
                "- Bonne hydratation et apports sodés suffisants\n"
                "- Arrêt ou diminution des médicaments hypotenseurs\n"
                "- La fréquence des récidives diminue souvent après une première évaluation\n"
                "- Cas rares : **fludrocortisone**, **agonistes alpha**, ou **pacemaker** "
                "si composante bradycardie prédominante et documentée"
            )),
        ]),
        SousPartie(lettre="B", titre="Hypotension orthostatique", rows=[
            FicheRow(concept="◆ Circonstances de survenue", detail_md=(
                "- Facteurs iatrogènes : psychotropes, antiparkinsoniens, antihypertenseurs\n"
                "- Introduction ou changement de dose d'un traitement hypotenseur "
                "(vasodilatateur, diurétique)\n"
                "- Station debout prolongée, notamment en endroit chaud "
                "(syncope au passage du décubitus/assis à debout)\n"
                "- Postprandial\n"
                "- Dysautonomie : diabète, maladie de Parkinson, etc."
            )),
            FicheRow(concept="◆ Prise en charge", detail_md=(
                "- Lutte contre l'hypovolémie : hydratation, apports sodés suffisants\n"
                "- Diminution ou arrêt des médicaments hypotenseurs\n"
                "- **Mesures mécaniques** : croisement des jambes, accroupissement, "
                "bas de contention, lever prudent\n"
                "- **Traitements médicamenteux** :\n"
                "  - Alpha-agonistes : **midodrine**\n"
                "  - **Fludrocortisone** : minéralocorticoïde → rétention hydrosodée"
            )),
        ]),
        SousPartie(lettre="C", titre="Trouble du rythme/conduction", rows=[
            FicheRow(concept="◆ Diagnostic et terrain", detail_md=(
                "- Diagnostic final le plus souvent : **TV** ou **BAV**\n"
                "- Patient avec ATCD (parfois très lointain) d'IDM ou de cardiomyopathie dilatée\n"
                "- Généralement FEVG abaissée\n"
                "- Parfois ATCD familiaux de mort subite (cause génétique)"
            )),
            FicheRow(concept="◆ Éléments d'orientation", detail_md=(
                "- Survenue à l'effort\n"
                "- Position couchée\n"
                "- Palpitations avant la syncope"
            )),
            FicheRow(concept="Diagnostic et thérapeutique", detail_md=(
                "- **ECG** : peut donner le diagnostic ou orienter\n"
                "- Examens supplémentaires : ETT met en évidence la cardiopathie\n"
                "- EEP ou MEI (si EEP négative) → confirme le mécanisme\n"
                "- **Sanction thérapeutique** :\n"
                "  - **DAI** si TV\n"
                "  - **Pacemaker** si atteinte des voies de conduction"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ **Une syncope n'est JAMAIS banale chez un patient porteur d'une cardiopathie.**\n"
                "- ⚠ Le diagnostic de syncope vasovagale chez un cardiaque reste possible "
                "mais doit être un **diagnostic d'élimination** après bilan complet "
                "(EEP et MEI principalement)."
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Notions indispensables et transversalités", rows=[
            FicheRow(concept="◆ Notions indispensables", detail_md=(
                "- Connaître les principaux éléments du diagnostic différentiel des PDCB\n"
                "- Savoir conduire l'interrogatoire pour orienter le diagnostic et les étiologies\n"
                "- Bien connaître les critères cliniques et paracliniques imposant "
                "une surveillance et un bilan en hospitalisation\n"
                "- Syncope chez un cardiaque : jamais banale, bilan complet avant un diagnostic d'élimination"
            )),
            FicheRow(concept="◆ Réflexes transversalités", detail_md=(
                "- **Item 105** : Épilepsie de l'enfant et de l'adulte\n"
                "- **Item 108** : Confusion, démences\n"
                "- **Item 231** : Électrocardiogramme — indications et interprétations\n"
                "- **Item 232** : Fibrillation atriale\n"
                "- **Item 234** : Insuffisance cardiaque de l'adulte\n"
                "- **Item 236** : Troubles de la conduction intracardiaque\n"
                "- **Item 237** : Palpitations\n"
                "- **Item 343** : État confusionnel et trouble de conscience chez l'adulte et l'enfant"
            )),
            FicheRow(concept="", detail_md=(
                "- L'interrogatoire, l'examen clinique et l'ECG résolvent **> 50 % des cas** de syncope/lipothymie.\n"
                "- L'âge oriente mais peut tromper : la syncope vasovagale n'est pas réservée au sujet jeune.\n"
                "- **Objectif principal** : déterminer la cardiopathie sous-jacente et le "
                "risque de mort subite → discussion d'un **défibrillateur implantable**."
            ), kind="a_retenir"),
        ]),
    ])

    tableaux = [
        TableauSynthese(titre="Synthèse — Diagnostic différentiel des PDCB", markdown=(
            "| Entité | Mécanisme | Élément clé |\n"
            "|--------|-----------|-------------|\n"
            "| **Syncope** | Hypoperfusion cérébrale | Récupération complète et spontanée, état neuro normal |\n"
            "| **Crise comitiale** | Hyperactivité cérébrale | Aura, durée longue, morsure latérale langue, confusion post-critique |\n"
            "| **PDCB psychogène** | Conversion | Résistance ouverture yeux, durée > 15 min, répétition |\n"
            "| **Coma** | Causes variées (toxiques, métaboliques) | PDCB **prolongée**, sortie progressive |\n"
            "| **Confusion mentale** | Désordre métabolique | **PAS de PDCB**, désorientation, agitation |\n"
            "| **Cataplexie** | Perte tonus, déclencheur émotion | **PAS de PDCB**, pas d'amnésie |\n"
            "| **AIT vertébrobasilaire** | Ischémie tronc | Déficit focal (vertiges, dysarthrie, diplopie) |\n"
            "| **Arrêt cardiaque** | Asystolie/FV | Retour à conscience après réanimation |"
        )),
        TableauSynthese(titre="Classification étiologique des syncopes", markdown=(
            "| Catégorie | Causes principales | Indices cliniques |\n"
            "|-----------|--------------------|-----------------|\n"
            "| **Obstacle mécanique** | Rétrécissement aortique serré, CMH obstructive, EP, tamponnade, thrombose de valve mécanique, myxome, dissection aortique, HTAP sévère | Syncope **à l'effort**, souffle systolique |\n"
            "| **Rythmiques - conductives** | BAV 3, Mobitz 2, dysfonction sinusale (pauses > 6 s), défaillance pacemaker | Bradycardie sur ECG |\n"
            "| **Rythmiques - tachy** | TV (IDM, CMD, CMH, DAVD), torsades de pointes (QT long) | Palpitations, ATCD cardiopathie |\n"
            "| **HTO** (1ʳᵉ cause) | Médicaments hypotenseurs, hypovolémie, dysautonomie | Test orthostatique positif (PAS ≥ 20, PAD ≥ 10 ou PAS < 90) |\n"
            "| **Réflexes - vasovagale** | Émotion, douleur, station debout, chaleur | Prodromes, sujet jeune |\n"
            "| **Réflexes - situationnelles** | Miction, défécation, toux, Valsalva | Contexte spécifique |\n"
            "| **Réflexes - sinus carotidien** | Rasage, cravate, mouvements du cou | Homme âgé |"
        )),
        TableauSynthese(titre="ECG dans la syncope — anomalies diagnostiques vs d'orientation", markdown=(
            "| Anomalies diagnostiques | Anomalies d'orientation |\n"
            "|------------------------|-------------------------|\n"
            "| **TV** | ESV nombreuses ou en salves → TV |\n"
            "| **Torsades de pointes** | **QT long** → torsade |\n"
            "| **Bradycardie < 40 bpm** | Bradycardie 40-50 bpm → dysfonction sinusale |\n"
            "| **Pauses > 3 s** | Pauses < 3 s → dysfonction sinusale |\n"
            "| **BAV 3 ou Mobitz 2** | Mobitz 1, BBG, bloc bifasciculaire → BAV paroxystique |\n"
            "| **Bloc de branche alternant** | WPW → cause rythmique |\n"
            "| **TSV > 150 bpm** | Brugada → FV (mort subite) |\n"
            "| **Défaillance pacemaker/défibrillateur** | HVG, repolarisation, Q de nécrose → cardiopathie structurelle |"
        )),
        TableauSynthese(titre="Diagnostic différentiel — Syncope vs Crise comitiale", markdown=(
            "| Élément | Syncope | Crise comitiale |\n"
            "|---------|---------|------------------|\n"
            "| **Facteur déclenchant** | Verticalisation, effort | Stimulation lumineuse, privation de sommeil, alcool |\n"
            "| **Prodromes** | Sensation cotonneuse, tête vide, nausées, sueurs, sensation de froid | Aura : déjà-vu, étrangeté, épigastrique, hallucinations |\n"
            "| **Aura** | Non | Possible |\n"
            "| **Sommeil** | Non | Possible |\n"
            "| **Durée de la PDCB** | Brève | Longue |\n"
            "| **Mouvements** | Myoclonies < 15 s **après** la PDCB | Tonicocloniques prolongés, contemporains |\n"
            "| **Automatismes** | Non | Oui |\n"
            "| **Morsure de langue** | Bout de la langue (rare) | **Bord latéral profond** |\n"
            "| **Tégument** | Normal ou pâle | Cyanosé |\n"
            "| **Récupération conscience** | 10 à 30 secondes | Plusieurs minutes |\n"
            "| **État confusionnel** | Très bref (< 10 s) puis vigilance normale | Amnésie fixation, douleurs musculaires, confusion prolongée |"
        )),
        TableauSynthese(titre="Examens paracliniques — indications et apport", markdown=(
            "| Examen | Indication principale | Apport diagnostique |\n"
            "|--------|-----------------------|----------------------|\n"
            "| **ETT** | Quasi systématique | Cardiopathie structurelle, FEVG, RA, CMH, EP, tamponnade |\n"
            "| **Épreuve d'effort** | Syncope d'effort | BAV à l'effort (cause cardiaque) ou syncope réflexe post-effort |\n"
            "| **BNP/NT-proBNP, troponine** | Suspicion cause cardiaque | Marqueurs IC, IDM |\n"
            "| **Holter ECG** | Risque vital, syncopes fréquentes, ambulatoire 24 h-3 sem | Dysfonction sinusale, BAV nodal |\n"
            "| **Massage sinus carotidien** | Suspicion syncope réflexe sans cause | Pause > 3 s OU PAS↓ > 50 mmHg + symptômes (CI : AIT/AVC/sténose carotide) |\n"
            "| **EEP** | Syncope inexpliquée + cardiopathie/anomalies ECG | Intervalle HV, SVP pour TV → DAI |\n"
            "| **MAPA** | Suspicion HTO | HTA nocturne paradoxale |\n"
            "| **Tilt-test** | Suspicion syncope vasovagale ou PDCB psychogène | Reproduction syncope vasovagale (60-70°, isoprénaline/trinitrine) |\n"
            "| **MEI** | Syncopes espacées, EEP négative avec suspicion faux négatif | Corrélation symptômes/ECG sur > 2 ans |"
        )),
        TableauSynthese(titre="Critères de gravité — hospitalisation vs retour à domicile", markdown=(
            "| Hospitalisation / surveillance | Retour à domicile possible |\n"
            "|------------------------------|-----------------------------|\n"
            "| ATCD familial mort subite jeune | Syncope réflexe évidente répétée depuis années |\n"
            "| ATCD cardiopathie, IDM, FEVG ↓ | HTO avec mesures appropriées prises |\n"
            "| Syncope à l'effort | Examen clinique normal |\n"
            "| Syncope précédée de palpitations | ECG normal |\n"
            "| Syncope en position couchée | Absence de cardiopathie sous-jacente |\n"
            "| Symptôme grave associé (douleur thoracique/abdo, céphalées, dyspnée brutale, trauma grave) | |\n"
            "| Souffle systolique éjectionnel | |\n"
            "| Anomalie ECG diagnostique ou d'orientation | |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Arrêt du flux cérébral → syncope | **6 à 8 secondes** | Seuil ischémique |\n"
        "| PAS au cœur déclenchant syncope (debout) | **50 à 60 mmHg** | PA cérébrale 30-45 mmHg |\n"
        "| PA cérébrale à l'origine de la syncope | **30 à 45 mmHg** | En orthostatisme |\n"
        "| Myoclonies de la syncope - durée | **< 15 secondes** | Débutent après PDCB, le plus souvent après 30 s |\n"
        "| Stokes-Adams - durée | **< 30 secondes** | Syncope sans prodrome, cause rythmique |\n"
        "| HTO - chute de PAS | **≥ 20 mmHg** | Critère diagnostique |\n"
        "| HTO - chute de PAD | **≥ 10 mmHg** | Critère diagnostique |\n"
        "| HTO - PAS seuil | **< 90 mmHg** | Critère alternatif |\n"
        "| HTO - délai après orthostatisme | **1 à 3 minutes** | Fenêtre de mesure |\n"
        "| Dysfonction sinusale - pauses (jeune) | **> 6 secondes** | Critère syncope |\n"
        "| Bradycardie diagnostique | **< 40 bpm** | Patient éveillé |\n"
        "| Bradycardie d'orientation | **40 à 50 bpm** | Dysfonction sinusale |\n"
        "| Pause ECG diagnostique | **> 3 secondes** | Patient éveillé |\n"
        "| Pause d'orientation | **< 3 secondes** | Dysfonction sinusale |\n"
        "| TSV rapide diagnostique | **> 150 bpm** | Cause de syncope |\n"
        "| Massage sinus carotidien - durée | **5 à 10 secondes** | Bord antérieur SCM, cartilage cricoïde |\n"
        "| MSC positif - pause | **> 3 secondes** | Reproduction symptômes |\n"
        "| MSC positif - baisse PAS | **> 50 mmHg** | Reproduction symptômes |\n"
        "| Tilt-test - décubitus initial | **≥ 5 minutes** | Avant inclinaison |\n"
        "| Tilt-test - angle | **60° à 70°** | Tête en haut |\n"
        "| Tilt-test - durée inclinaison | **20 à 45 minutes** | Au plus |\n"
        "| EEP - mobilisation post-procédure | **4 heures** | Point de ponction fémoral |\n"
        "| MEI - autonomie | **> 2 ans** | Syncopes espacées |\n"
        "| Holter ECG - durée ambulatoire | **24 h à 3 semaines** | Syncopes fréquentes |\n"
        "| PDCB psychogène - durée évocatrice | **> 15 minutes** | Élément en faveur |\n"
        "| Diagnostic posé clinique + ECG | **> 50 % des cas** | À l'issue du premier bilan |\n"
        "| Syncope vasovagale - début | **avant 40 ans** | Passé ancien typique |"
    ))

    points_cles = [
        "Interrogatoire + examen clinique + **ECG** résolvent **> 50 %** des cas de syncope/lipothymie",
        "**PDCB** = syncope (hypoperfusion), crise comitiale (hyperactivité) ou psychogène (conversion)",
        "**Syncope** : début rapide + récupération complète + état neuro normal ; arrêt flux **6-8 s**",
        "**HTO (1ʳᵉ cause)** : ↓PAS **≥ 20**, ↓PAD **≥ 10** ou PAS **< 90** à 1-3 min orthostatisme",
        "Étiologies : obstacle mécanique, rythme/conduction, **HTO**, réflexes (vasovagale, situationnelle, sinus)",
        "ECG diagnostique : **TV**, brady **< 40**, pauses **> 3 s**, BAV3/Mobitz2, TSV **> 150**, torsades",
        "Myoclonies de syncope : **< 15 s**, **APRÈS** la PDCB ; éviter terme « syncope convulsivante »",
        "Massage sinus carotidien : positif si pause **> 3 s** ou PAS↓ **> 50 mmHg** ; CI : **AIT/AVC/sténose**",
        "Examens : **ETT** + Holter avant **EEP** ; **MEI** si EEP négative et syncopes espacées",
        "⚠ Syncope chez cardiaque **jamais banale** : vasovagale = diagnostic d'élimination après EEP/MEI",
    ]

    fiche_eclair_md = (
        "**PDCB** : amnésie + perte motricité/réactivité + courte durée. 3 catégories : syncope (hypoperfusion), épilepsie (hyperactivité), psychogène (conversion).\n\n"
        "**Syncope** : début rapide, récupération complète, neuro normal au réveil. Arrêt flux 6-8 s → syncope.\n\n"
        "**Myoclonies de syncope** : < 15 s, APRÈS la PDCB. Pas « convulsivante ».\n\n"
        "**Obstacle mécanique** : RA serré (effort), CMH obstructive, EP haut risque, tamponnade, dissection.\n\n"
        "**Rythmiques** : BAV 3 infrahissien, Mobitz 2, dysfonction sinusale (pauses > 6 s), TV, torsades (QT long).\n\n"
        "**HTO (1ʳᵉ cause)** : ↓ PAS ≥ 20 OU ↓ PAD ≥ 10 OU PAS < 90 à 1-3 min. Iatrogène, hypovolémie, dysautonomie.\n\n"
        "**Réflexes** : vasovagale (jeune, prodromes), situationnelles (miction, toux, Valsalva), sinus carotidien (homme âgé).\n\n"
        "**ECG diagnostique** : TV, brady < 40 bpm, pauses > 3 s, BAV 3/Mobitz 2, bloc branche alternant, TSV > 150 bpm, torsades, pacemaker défaillant.\n\n"
        "**Examens** : ETT → Holter → EEP (HV, SVP) → MEI si EEP négative.\n\n"
        "**Massage sinus carotidien** : 5-10 s, couché puis debout. Positif si pause > 3 s ou PAS↓ > 50 mmHg. CI : AIT, AVC, sténose carotide.\n\n"
        "**Tilt-test** : décubitus ≥ 5 min, 60-70°, 20-45 min, isoprénaline/trinitrine.\n\n"
        "**Syncope vs comitiale** : aura, sommeil, tonicocloniques contemporains, morsure latérale langue, confusion post-critique → comitiale.\n\n"
        "**Hospitalisation** : ATCD familial mort subite, cardiopathie/FEVG↓, syncope effort/couché/palpitations, ECG anormal.\n\n"
        "**PEC** : vasovagale = non pharmaco (éducation, sel/hydratation) ; HTO = midodrine + fludrocortisone ; rythme/conduction → DAI si TV, pacemaker si conduction. Syncope chez cardiaque jamais banale."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 342 - Malaises, perte de connaissance, crise comitiale chez l'adulte",
        annee="2025-2026",
        item="Item 342",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi, partie_vii],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 342",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-342_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

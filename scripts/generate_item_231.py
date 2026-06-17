"""Génère la fiche de l'Item 231 - Électrocardiogramme (Cardiologie)."""

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
        PlanPartie(numero="I", titre="ECG normal et bases électrophysiologiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Électrophysiologie cardiaque"),
            PlanSousPartie(lettre="B", titre="Électrogenèse et dérivations"),
            PlanSousPartie(lettre="C", titre="Calcul de l'axe du QRS"),
            PlanSousPartie(lettre="D", titre="Valeurs normales et interprétation systématique"),
        ]),
        PlanPartie(numero="II", titre="Troubles de la conduction", sous_parties=[
            PlanSousPartie(lettre="A", titre="Blocs de branche"),
            PlanSousPartie(lettre="B", titre="Hémiblocs et blocs bifasciculaires"),
            PlanSousPartie(lettre="C", titre="Blocs atrioventriculaires"),
            PlanSousPartie(lettre="D", titre="Dysfonction sinusale"),
        ]),
        PlanPartie(numero="III", titre="Troubles du rythme supraventriculaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Tachycardie sinusale et manoeuvres vagales"),
            PlanSousPartie(lettre="B", titre="Fibrillation atriale"),
            PlanSousPartie(lettre="C", titre="Flutters atriaux"),
            PlanSousPartie(lettre="D", titre="Tachycardies atriales focales et jonctionnelles"),
            PlanSousPartie(lettre="E", titre="Extrasystoles"),
        ]),
        PlanPartie(numero="IV", titre="Troubles du rythme ventriculaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Tachycardies ventriculaires"),
            PlanSousPartie(lettre="B", titre="Fibrillation ventriculaire"),
            PlanSousPartie(lettre="C", titre="Torsades de pointes"),
        ]),
        PlanPartie(numero="V", titre="Hypertrophies et autres pathologies", sous_parties=[
            PlanSousPartie(lettre="A", titre="Hypertrophies atriales et ventriculaires"),
            PlanSousPartie(lettre="B", titre="Dyskaliémies"),
            PlanSousPartie(lettre="C", titre="Péricardites"),
            PlanSousPartie(lettre="D", titre="Préexcitation et Wolff-Parkinson-White"),
            PlanSousPartie(lettre="E", titre="Maladie coronarienne"),
        ]),
        PlanPartie(numero="VI", titre="Stimulateur cardiaque et indications", sous_parties=[
            PlanSousPartie(lettre="A", titre="ECG et pacemaker"),
            PlanSousPartie(lettre="B", titre="Monitorage et ECG conventionnel"),
            PlanSousPartie(lettre="C", titre="Méthode Holter et outils connectés"),
        ]),
    ]

    # ── PARTIE I : ECG NORMAL ET BASES ÉLECTROPHYSIOLOGIQUES ──
    partie_i = Partie(numero="I", titre="ECG normal et bases électrophysiologiques", sous_parties=[
        SousPartie(lettre="A", titre="Électrophysiologie cardiaque", rows=[
            FicheRow(concept="Polarisation et potentiel d'action", detail_md=(
                "- Cellules cardiaques polarisées négativement à l'état de repos (charge négative intracellulaire)\n"
                "- **Dépolarisation** : génère un potentiel d'action transmissible, mécanisme passif (gradients ioniques)\n"
                "- **Repolarisation** : retour au potentiel de repos, mécanisme actif consommant ATP via pompes Na/K-ATPase\n"
                "- Conduction au sein du myocarde = dépolarisation de proche en proche via les jonctions communicantes (gap junctions) situées aux extrémités longitudinales des cellules"
            )),
            FicheRow(concept="Deux types de cellules myocardiques", detail_md=(
                "| Type | Localisation | Conduction | Automatisme |\n"
                "|------|--------------|------------|-------------|\n"
                "| **Contractiles sodiques** | Myocarde atrial et ventriculaire | Lente (proche en proche) | Possible mais faible |\n"
                "| **Nodales calciques** | Noeud sinusal, NAV | Rapide | Forte (intrinsèque) |\n"
                "| **His-Purkinje** | Faisceau de His, branches, Purkinje | Intermédiaire | Intermédiaire |"
            )),
            FicheRow(concept="◆ Hiérarchie des pacemakers", detail_md=(
                "- **Noeud sinusal** : pacemaker physiologique dominant, **60-80 bpm** au repos\n"
                "- En cas de défaillance, prise de relais par les pacemakers de réserve :\n"
                "  - **Jonctionnel** (NAV + His) : **40-60 bpm**\n"
                "  - **Ventriculaire** (branches, Purkinje) : **15-30 bpm**\n"
                "- Quand un pacemaker de réserve prend le relais : échappement jonctionnel ou ventriculaire\n"
                "- Plus le pacemaker est bas, plus la FC d'échappement est basse"
            )),
            FicheRow(concept="Antiarythmiques", detail_md=(
                "- Modulateurs directs des canaux ioniques\n"
                "- Exception : **bêtabloquants** = inhibent le système sympathique (effet indirect)\n"
                "- **Classification de Vaughan-Williams** : décrit l'effet ionique prédominant\n"
                "- La plupart ont en réalité un effet sur plusieurs canaux ioniques"
            )),
            FicheRow(concept="◆ Synchronisation cardiaque", detail_md=(
                "- **NAV** : assure la synchronisation atrioventriculaire\n"
                "- Faisceau de His + branches D/G + Purkinje : synchronisation interventriculaire et intraventriculaire\n"
                "- Le plan fibreux des valves est isolant → seul passage électrique physiologique oreillette-ventricule = **NAV**\n"
                "- Les structures spécialisées ne génèrent pas d'onde propre sur l'ECG (peu de cellules)"
            )),
        ]),
        SousPartie(lettre="B", titre="Électrogenèse et dérivations", rows=[
            FicheRow(concept="Origine du signal ECG", detail_md=(
                "- L'activité enregistrée provient de la somme des potentiels d'action cellulaires suivant la propagation d'un front de dépolarisation\n"
                "- Enregistrement à distance (surface du thorax)\n"
                "- **Onde P** = dépolarisation atriale\n"
                "- **Complexe QRS** = dépolarisation ventriculaire\n"
                "- **Onde T** = repolarisation ventriculaire (repolarisation graduelle des cellules à des instants différents)"
            )),
            FicheRow(concept="◆ Polarité du signal", detail_md=(
                "- Onde de dépolarisation :\n"
                "  - vers l'électrode = positive\n"
                "  - fuit l'électrode = négative\n"
                "- Onde T concordante avec QRS sur ECG normal (T+ si QRS+, T- si QRS-)\n"
                "- Explication : la dépolarisation ventriculaire progresse de l'endocarde vers l'épicarde, alors que la repolarisation s'effectue en sens inverse (épicarde vers endocarde)"
            )),
            FicheRow(concept="Dérivations frontales", detail_md=(
                "- Explorent le plan frontal (vertical)\n"
                "- Bipolaires des membres : D1 (I), D2 (II), D3 (III)\n"
                "- Unipolaires des membres : aVR, aVL, aVF\n"
                "- **Double triaxe de Bailey** : dérivations graduées de 30 en 30° dans le sens horaire à partir de D1 (0°)"
            )),
            FicheRow(concept="Dérivations précordiales", detail_md=(
                "- Explorent le plan horizontal (transversal)\n"
                "- V1 à V9 (numérotation standard)\n"
                "- Complétées parfois par **V3R et V4R** chez l'enfant ou en cas de suspicion de SCA (VD)\n"
                "- Doivent être isodistantes\n"
                "- **Dérivations de Lewis** : électrode rouge à la fourchette sternale, jaune au 5e EIC droit → démasque l'activité atriale en D1"
            )),
            FicheRow(concept="★ ◆ Territoires cardiaques", detail_md=(
                "| Territoire | Dérivations | Paroi explorée |\n"
                "|------------|-------------|----------------|\n"
                "| **Antéroseptal** | V1, V2, V3 | Paroi antérieure VG + septum |\n"
                "| **Apical** | V4 | Apex |\n"
                "| **Latéral haut** | D1, aVL | Paroi latérale haute VG |\n"
                "| **Latéral bas** | V5, V6 | Paroi latérale basse VG |\n"
                "| **Inférieur** | D2, D3, aVF | Face inférieure VG (diaphragmatique) |\n"
                "| **Postérieur** | V7, V8, V9 | Face basale et inférieure VG |\n"
                "| **Ventricule droit** | V1, V2, V3R, V4R | VD |"
            )),
            FicheRow(concept="", detail_md=(
                "- Mauvaise position de V1-V2 (trop hautes, trop écartées, confondues avec les foyers auscultatoires aortique/pulmonaire) → aspect de **pseudonécrose** ou atypie de repolarisation dans le territoire antérieur"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Calcul de l'axe du QRS", rows=[
            FicheRow(concept="◆ Méthode rapide de détermination de l'axe", detail_md=(
                "- Regarder la polarité de D1 et aVF pour déterminer le cadran :\n"
                "  - D1+ et aVF+ → axe 0 à 90° : **normal**\n"
                "  - D1+ et aVF- → axe entre 0 et -90° :\n"
                "    - Si D2+ → axe entre 0 et -30° : normal\n"
                "    - Sinon : **axe hypergauche**\n"
                "  - D1- et aVF+ → axe entre 90 et 180° = **axe hyperdroit**\n"
                "  - D1- et aVF- → axe extrême entre -90 et -180°\n"
                "- **Axe normal : -30° à +90°**"
            )),
            FicheRow(concept="Onde isodiphasique", detail_md=(
                "- Lorsque les composantes successives de l'onde (P, QRS ou T) sont d'égale importance pour le positif et le négatif (aspect de sinusoïde)"
            )),
            FicheRow(concept="Variations physiologiques de l'axe", detail_md=(
                "- Coeur vertical chez le patient filiforme : axe proche de 90°\n"
                "- Coeur horizontal chez le patient obèse ou avec cardiomégalie : axe proche de 0°\n"
                "- Axe également anormal en cas d'anomalie de conduction dans les hémibranches gauches ou d'anomalie morphologique marquée d'un ventricule"
            )),
        ]),
        SousPartie(lettre="D", titre="Valeurs normales et interprétation systématique", rows=[
            FicheRow(concept="◆ Valeurs normales ECG", detail_md=(
                "| Paramètre | Valeur normale |\n"
                "|-----------|----------------|\n"
                "| Vitesse de défilement | **25 mm/s** (40 ms/mm) |\n"
                "| 1 grand carreau (5 mm) | **200 ms** |\n"
                "| Amplitude | **1 mm = 0,1 mV** |\n"
                "| **FC repos adulte** | **60-100 bpm** |\n"
                "| **Onde P** | Axe à **60°**, **< 120 ms** (norme stricte < 110 ms) |\n"
                "| **PR** | **120-200 ms** |\n"
                "| **QRS** | **70-110 ms**, axe **-30 à +90°** |\n"
                "| **QT** | **< 450 ms** (corrigé Bazett) |\n"
                "| Sokolow | **< 35 mm** |"
            )),
            FicheRow(concept="Rythme cardiaque et rythme sinusal", detail_md=(
                "- **Rythme cardiaque** : mécanisme à l'origine des QRS, peut provenir de n'importe quel étage (atrial, jonctionnel, ventriculaire, électroentraîné)\n"
                "- **Rythme sinusal** : naît du noeud sinusal, pacemaker physiologique dominant\n"
                "- Critères ECG du rythme sinusal :\n"
                "  - Onde P positive en D1 et dérivations inférieures (D2, D3, aVF)\n"
                "  - Chaque QRS précédé d'une P et chaque P suivie d'un QRS (conduction AV)"
            )),
            FicheRow(concept="", detail_md=(
                "- Ondes P sinusales régulières sans conduction au ventricule (BAV3) → **ce n'est plus un rythme sinusal**"
            ), kind="piege"),
            FicheRow(concept="◆ Phases du QRS", detail_md=(
                "- 1re phase : dépolarisation septale vers l'avant/droite/haut → onde Q fine et peu profonde en latéral + petite onde positive en V1\n"
                "- 2e phase : vers la jambe gauche et l'avant → grande onde R en V3, V4, D2\n"
                "- 3e phase : vers le haut/arrière → petite onde S dans les dérivations inférieures et latérales\n"
                "- Caractère polyphasique des QRS"
            )),
            FicheRow(concept="Calcul de la FC", detail_md=(
                "- Intervalle RR en secondes, FC = 60/Période\n"
                "- Méthode pratique : **FC = 300 / nombre de grands carreaux séparant 2 QRS**\n"
                "  - RR = 1 grand carreau → FC = 300 bpm\n"
                "  - RR = 2 grands carreaux → FC = 150 bpm\n"
                "- **Bradycardie** : FC < 60 bpm\n"
                "- **Tachycardie** : FC > 100 bpm\n"
                "- Athlètes : bradycardie sinusale physiologique (tonus vagal important)\n"
                "- Sujets jeunes : variation respiratoire physiologique de la FC sinusale"
            )),
            FicheRow(concept="Intervalle PR et QT", detail_md=(
                "- **PR** (début P → début QRS) : **120-200 ms**\n"
                "  - Explore la totalité de la conduction depuis sortie sinusale jusqu'aux extrémités du Purkinje\n"
                "  - Pas seulement la traversée du NAV !\n"
                "- **QT** (début Q → fin T) : explore la durée de la repolarisation\n"
                "  - Mesure dans les dérivations où T est la plus ample/longue (souvent V2-V3)\n"
                "  - Tracer la tangente à l'onde T\n"
                "- **QTc** par formule de **Bazett** : norme pour FC = 60 bpm\n"
                "- Onde U (2e onde de repolarisation) : ne pas inclure dans la mesure du QT"
            )),
            FicheRow(concept="◆ Méthode systématique d'analyse ECG", detail_md=(
                "- **1. Rythme** : sinusal (P+ en D1, D2 ; QRS après chaque P ; P avant chaque QRS) ? Entre 60-100 bpm ?\n"
                "- **2. Conduction** : P < 120 ms, PR 120-200 ms, QRS fins (70-110 ms) avec axe -30 à +90°\n"
                "- **3. Repolarisation** : point J et ST isoélectriques ; T positives sauf en aVR, V1, parfois D3 et aVL ; QT < 450 ms\n"
                "- **4. Morphologique** : amplitude P et QRS normales (**Sokolow < 35 mm**), transition QRS normale en antérieur, absence d'onde Q de nécrose (larges > 40 ms et profondes > 1/3 du QRS)"
            )),
            FicheRow(concept="Repolarisation précoce physiologique", detail_md=(
                "- Chez le jeune homme : sus-décalage du point J de V1 à V4 avec segment ST jonctionnel (pente ascendante entre J et T)\n"
                "- = repolarisation physiologique"
            )),
            FicheRow(concept="Vérification position électrodes", detail_md=(
                "- Regarder la transition de V1 à V6 :\n"
                "  - Onde R qui grandit progressivement\n"
                "  - Onde S qui diminue progressivement"
            )),
        ]),
    ])

    # ── PARTIE II : TROUBLES DE LA CONDUCTION ──
    partie_ii = Partie(numero="II", titre="Troubles de la conduction", sous_parties=[
        SousPartie(lettre="A", titre="Blocs de branche", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Interruption ou ralentissement marqué de la conduction dans l'une ou l'autre des deux branches (D ou G)"
            )),
            FicheRow(concept="", detail_md=(
                "- Avant de décrire un trouble de conduction, toujours commencer par décrire le rythme atrial pour ne pas passer à côté d'une **tachycardie supraventriculaire** (l'association tachycardie SV + bloc de branche n'est pas rare !)"
            ), kind="piege"),
            FicheRow(concept="◆ Bloc complet de branche droite (BBD)", detail_md=(
                "- **QRS > 120 ms**\n"
                "- V1 : QRS globalement positif avec aspect **RsR'**\n"
                "- V6 : aspect qRs avec onde S traînante et le plus souvent arrondie"
            )),
            FicheRow(concept="◆ Bloc complet de branche gauche (BBG)", detail_md=(
                "- **QRS > 120 ms**\n"
                "- V1 : QRS globalement négatif, aspect **rS** ou **QS**\n"
                "- V6, D1, aVL : notch (double pic = activation septale + activation latérale tardive) avec le plus souvent onde R exclusive"
            )),
            FicheRow(concept="Méthode d'interprétation", detail_md=(
                "- 1. Rythme sinusal ?\n"
                "- 2. Durée QRS > 120 ms ?\n"
                "- 3. Aspect en V1 :\n"
                "  - QRS globalement positif → **BBD**\n"
                "  - QRS globalement négatif → **BBG**\n"
                "- 4. Aspect inverse en V6"
            )),
            FicheRow(concept="◆ Discordance appropriée", detail_md=(
                "- En cas de QRS larges → trouble de la dépolarisation induit un trouble de repolarisation\n"
                "- La polarité T et QRS n'est plus concordante = **discordance appropriée**\n"
                "- QRS négatif → T positive avec petit sus-décalage ST\n"
                "- QRS positif → T négative avec petit sous-décalage ST\n"
                "- Risque de faux diagnostic de SCA ST+ surtout en V1-V2"
            )),
            FicheRow(concept="", detail_md=(
                "- **Douleur thoracique persistante + BBG** → évoquer infarctus antérieur : évaluation rapide par cardiologue sans attendre la troponine\n"
                "- Recherche d'arguments cliniques en faveur d'un SCA : sémiologie, effet de la TNT, signes de choc, ETT"
            ), kind="a_retenir"),
            FicheRow(concept="Blocs incomplets et fonctionnels", detail_md=(
                "- **Blocs incomplets** : faible intérêt sémiologique, QRS 110-120 ms avec mêmes anomalies\n"
                "- **Bloc fonctionnel** : existe uniquement à partir d'une FC donnée\n"
                "  - Phase III : apparition lors d'une tachycardie\n"
                "  - Phase IV : apparition lors d'une bradycardie"
            )),
        ]),
        SousPartie(lettre="B", titre="Hémiblocs et blocs bifasciculaires", rows=[
            FicheRow(concept="Caractéristiques générales des hémiblocs", detail_md=(
                "- Élargissement très modéré du QRS (> 110 ms)\n"
                "- Peut dépasser 120 ms si association à un autre bloc ou cardiopathie marquée\n"
                "- Déviation axiale caractéristique"
            )),
            FicheRow(concept="◆ Hémibloc antérieur gauche (HBAG)", detail_md=(
                "- **Déviation axiale gauche au-delà de -30°** (négativité de D2)\n"
                "- Fréquent car la branche est fragile (superficielle et de petite taille)"
            )),
            FicheRow(concept="◆ Hémibloc postérieur gauche (HBPG)", detail_md=(
                "- **Déviation axiale droite > +90°** (négativité de D1, aspect S1Q3)\n"
                "- En l'absence de pathologie du VD, morphologie longiligne ou infarctus latéral\n"
                "- Rare car la branche est profonde"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant D1 négatif : le 1er diagnostic n'est pas un HBPG mais une **inversion de positionnement des électrodes frontales**\n"
                "- Indice : l'onde P est également négative en D1"
            ), kind="piege"),
            FicheRow(concept="◆ Blocs bifasciculaires", detail_md=(
                "- Sémiologie additive : **HBAG + BBD** ou **HBPG + BBD**\n"
                "- QRS > 120 ms\n"
                "- Risque de BAV complet infrahissien si la troisième branche dysfonctionne (syncopes, mort subite)"
            )),
            FicheRow(concept="", detail_md=(
                "- **Syncope + bloc bifasciculaire** = hospitalisation en cardiologie avec télémétrie"
            ), kind="a_retenir"),
            FicheRow(concept="BBG complet et désynchronisation", detail_md=(
                "- Un BBG complet peut contribuer au développement ou à l'aggravation d'une cardiopathie\n"
                "- Par désynchronisation de la contraction des parois ventriculaires (activation tardive latérale)\n"
                "- Correction (resynchronisation) peut améliorer voire guérir la cardiopathie\n"
                "- Indiquée en cas d'apparition de signes d'insuffisance cardiaque"
            )),
            FicheRow(concept="Bloc trifasciculaire", detail_md=(
                "- Terme souvent utilisé par excès devant un bloc bifasciculaire + BAV1\n"
                "- Or le BAV1 peut être :\n"
                "  - Nodal (NAV) = bloc bifasciculaire avec BAV1 nodal\n"
                "  - Infrahissien (3e branche) = **vrai bloc trifasciculaire** = très haut risque de BAV complet\n"
                "- Seul moyen de trancher : exploration électrophysiologique\n"
                "- Bloc trifasciculaire complet = synonyme de **BAV complet infrahissien**\n"
                "- Trifasciculaire infrahissien = indication de pacemaker même sans symptôme"
            )),
            FicheRow(concept="Bloc alternant", detail_md=(
                "- Alternance de BBD et BBG, ou d'HBAG et HBPG sur fond de BBD\n"
                "- Annonce le **BAV complet infrahissien**\n"
                "- Indication de pacemaker même sans symptôme"
            )),
        ]),
        SousPartie(lettre="C", titre="Blocs atrioventriculaires (sémiologie ECG)", rows=[
            FicheRow(concept="◆ BAV1", detail_md=(
                "- **Allongement fixe et constant de PR > 200 ms**\n"
                "- Sans onde P bloquée"
            )),
            FicheRow(concept="◆ BAV2 Mobitz I (Luciani-Wenckebach)", detail_md=(
                "- Allongement progressif du PR jusqu'à blocage d'une onde P\n"
                "- Identifier les ondes P bloquées\n"
                "- ATTENTION : une onde P bloquée plus précoce que les autres correspond à une **extrasystole atriale bloquée** (pas un BAV2)"
            )),
            FicheRow(concept="BAV3 (complet)", detail_md=(
                "- **Dissociation complète** entre activité atriale et ventriculaire\n"
                "- Ondes P dissociées des QRS, bien visibles en V1\n"
                "- Échappement jonctionnel à QRS fins → bloc nodal/suprahissien\n"
                "- Échappement à QRS larges → bloc infrahissien"
            )),
            FicheRow(concept="BAV 2/1", detail_md=(
                "- 1 onde P sur 2 bloquée\n"
                "- Orientation infrahissien si QRS larges\n"
                "- Orientation suprahissien si QRS fins et présence de BAV2 Mobitz 1 à d'autres moments"
            )),
        ]),
        SousPartie(lettre="D", titre="Dysfonction sinusale", rows=[
            FicheRow(concept="Aspects ECG simples", detail_md=(
                "- **Asystole** : tracé plat sans activité cardiaque visible\n"
                "- **Pauses** par manque intermittent d'une onde P = bloc sino-atrial du 2e degré\n"
                "- La pause double l'intervalle PP ou RR normal"
            )),
            FicheRow(concept="Échappement jonctionnel", detail_md=(
                "- En cas de dysfonction sinusale marquée → rythme d'**échappement jonctionnel**\n"
                "- Onde P plus visible devant le QRS mais peut être rétrograde (derrière le QRS dans ST)\n"
                "- Onde P rétrograde négative en D2 (activation atriale de bas en haut)"
            )),
            FicheRow(concept="◆ Bradycardie : deux étiologies seulement", detail_md=(
                "- Seules **2 structures** peuvent entraîner une bradycardie quand elles dysfonctionnent :\n"
                "  - **Noeud sinusal** → dysfonction sinusale\n"
                "  - **NAV** → BAV2 ou BAV3\n"
                "- Algorithme diagnostique systématique devant toute bradycardie"
            )),
        ]),
    ])

    # ── PARTIE III : TROUBLES DU RYTHME SUPRAVENTRICULAIRE ──
    partie_iii = Partie(numero="III", titre="Troubles du rythme supraventriculaire", sous_parties=[
        SousPartie(lettre="A", titre="Tachycardie sinusale et manoeuvres vagales", rows=[
            FicheRow(concept="Trouble du rythme SV", detail_md=(
                "- Activation électrique des oreillettes ou de la jonction AV (NAV ou His) à une fréquence trop élevée\n"
                "- Au-delà de la bifurcation hissienne : troubles du rythme ventriculaire\n"
                "- **QRS fins (< 120 ms)** dans la majorité des cas\n"
                "- Peuvent associer des QRS larges si trouble de conduction intraventriculaire (bloc de branche)\n"
                "- En français : 'trouble du rythme' = tachycardie (les bradycardies = 'troubles de la conduction')"
            )),
            FicheRow(concept="◆ Fonction de filtre du NAV", detail_md=(
                "- **Conduction décrémentielle** du NAV : au-delà d'une certaine fréquence atriale, les ventricules ne suivent plus en 1/1\n"
                "- Fonction vitale : sans ce filtre, chaque FA donnerait une FV et tout flutter à 300 bpm donnerait une tachycardie ventriculaire à 300 bpm\n"
                "- Filtre dépend de : âge, tonus vagal, médicaments ralentisseurs du NAV\n"
                "- Conduction possible : 1/1, 2/1, alternance 1/1-2/1, 2/1-3/1, etc."
            )),
            FicheRow(concept="Tachycardie sinusale (différenciation)", detail_md=(
                "- ECG : ondes P sinusales (positives en D1, D2, D3, aVF)\n"
                "- Variabilité progressive de la FC (vs marches d'escalier des tachycardies SV)\n"
                "- Contexte : fièvre, stress, douleur, effort, etc.\n"
                "- Massage sinocarotidien : ralentissement progressif"
            )),
            FicheRow(concept="◆ Manoeuvres vagales", detail_md=(
                "- But : créer un bloc atrioventriculaire transitoire (intensifier le filtre AV)\n"
                "- **Manoeuvre de Valsalva** : expiration forcée à glotte fermée\n"
                "- **Compression carotidienne unilatérale** (CI : athérome important, souffle carotidien)\n"
                "- Boire un grand verre d'eau froide\n"
                "- NB : la compression oculaire bilatérale n'est plus recommandée (risque de décollement de rétine)"
            )),
            FicheRow(concept="◆ Adénosine IV", detail_md=(
                "- Indiquée si inefficacité des manoeuvres vagales\n"
                "- Mécanisme vagomimétique via les récepteurs purinergiques\n"
                "- Administration en flash IV\n"
                "- Durée d'effet : **~10 secondes**\n"
                "- **CI : asthme** (bronchospasme intense possible), **hypotension artérielle**\n"
                "- Utilisable pour le diagnostic différentiel des tachycardies"
            )),
        ]),
        SousPartie(lettre="B", titre="Fibrillation atriale", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- **Activation atriale anarchique**\n"
                "- Mécanismes électrophysiologiques complexes aboutissant à un état fibrillatoire"
            )),
            FicheRow(concept="◆ Caractéristiques ECG", detail_md=(
                "- Tachycardie **100-200 bpm** à QRS **irrégulièrement irréguliers** (intervalles RR non multiples d'une valeur commune)\n"
                "- QRS fins sauf trouble de conduction associé\n"
                "- Activité sinusale remplacée par :\n"
                "  - Mailles amples OU\n"
                "  - Fine trémulation de la ligne de base\n"
                "- Manoeuvres vagales utiles si activité atriale difficile à analyser"
            )),
            FicheRow(concept="Aspects difficiles", detail_md=(
                "- FA + BAV complet : activité ventriculaire lente et régulière (échappement automatique régulier)\n"
                "- Maladie de l'oreillette / maladie rythmique atriale : alternance bradycardie sinusale et FA (**syndrome tachycardie-bradycardie**)\n"
                "- Pauses de régularisation à l'arrêt de la FA = reprise lente du rythme sinusal\n"
                "- FA + bloc de branche (préexistant ou fonctionnel) : tachycardie irrégulière à QRS larges"
            )),
        ]),
        SousPartie(lettre="C", titre="Flutters atriaux", rows=[
            FicheRow(concept="◆ Mécanisme", detail_md=(
                "- Trouble du rythme par **réentrée** : boucle d'activation atriale se répétant à l'identique\n"
                "- Autour d'un ou plusieurs obstacle(s) anatomique(s) ou fonctionnel(s)\n"
                "- Activation organisée en circuit (vs anarchique dans la FA)\n"
                "- Flutters droits > flutters gauches (oreillette droite avec zones constitutionnelles propices)\n"
                "- Flutters gauches : induits par cardiopathie ou intervention créant des lésions OG\n"
                "- Facteurs prédisposants communs avec la FA"
            )),
            FicheRow(concept="◆ Caractéristiques ECG", detail_md=(
                "- Activité atriale monomorphe rapide (même aspect sur une dérivation donnée)\n"
                "- **300 bpm en moyenne** (entre 240 et 340 bpm)\n"
                "- Sans retour à la ligne isoélectrique dans au moins une dérivation\n"
                "- Aspect sinusoïdal, en toit d'usine ou en **dents de scie**\n"
                "- Ondes atriales = **ondes F**\n"
                "- Parfois démasquées seulement après manoeuvre vagale"
            )),
            FicheRow(concept="◆ Flutter typique antihoraire (commun)", detail_md=(
                "- Le plus fréquent\n"
                "- Boucle atriale droite empruntant l'**isthme cavotricuspide** (entre valve tricuspide et veine cave inférieure)\n"
                "- Fréquence atriale **300 bpm** sur oreillette normale (plus lente si dilatation)\n"
                "- Ondes F : négatives en D2, D3, aVF, positives en V1, négatives en V6\n"
                "- Flutter typique horaire : tourne en sens inverse, toutes les polarités sont inversées"
            )),
            FicheRow(concept="Flutters atypiques", detail_md=(
                "- L'isthme cavotricuspide ne fait pas partie du circuit\n"
                "- Atrial droit, gauche ou biatrial\n"
                "- Fréquence variable 120-320 bpm\n"
                "- Ondes F de morphologies diverses\n"
                "- Diagnostic formel : exploration électrophysiologique"
            )),
            FicheRow(concept="Activité ventriculaire dans le flutter", detail_md=(
                "- Forme usuelle : **cadence ventriculaire 150 bpm** (transmission 2/1)\n"
                "- Plus lente : 100 bpm (3/1), 75 bpm (4/1), etc.\n"
                "- Le plus souvent régulière mais filtre AV variable possible\n"
                "- Flutter à conduction variable : alternance 2/1, 3/1, 4/1\n"
                "- Manoeuvre vagale : démasque l'activité atriale sous-jacente"
            )),
        ]),
        SousPartie(lettre="D", titre="Tachycardies atriales focales et jonctionnelles", rows=[
            FicheRow(concept="◆ Tachycardies atriales focales (TAF)", detail_md=(
                "- Arythmies atriales focales par **hyperautomatisme**\n"
                "- Activité atriale monomorphe\n"
                "- Retour à la ligne de base entre les ondes P dans toutes les dérivations\n"
                "- Ondes P différentes de l'onde P sinusale\n"
                "- Activité régulière\n"
                "- Tachycardie régulière à QRS fins, PR long ou normal\n"
                "- Épisodes paroxystiques, salves d'ESA monomorphes\n"
                "- **Warm-up** (accélération progressive initiale) et **cool-down** (décélération progressive)"
            )),
            FicheRow(concept="Tachycardies jonctionnelles", detail_md=(
                "- = **maladie de Bouveret** en France\n"
                "- Tachycardies très régulières, souvent rapides ~200 bpm (130-260 bpm)\n"
                "- Deux formes principales"
            )),
            FicheRow(concept="◆ Tachycardie par réentrée intranodale", detail_md=(
                "- Mécanisme de réentrée dans le NAV\n"
                "- 20% de la population présente une dualité nodale (voie rapide + voie lente)\n"
                "- Boucle d'activation : descente par une voie, remontée par l'autre\n"
                "- Activité atriale souvent non visible ou devinée dans ST (activation atriale et ventriculaire quasi synchrone)\n"
                "- Tachycardie régulière à QRS fins"
            )),
            FicheRow(concept="◆ Tachycardie par rythme réciproque (voie accessoire)", detail_md=(
                "- Réentrée par une voie accessoire (**faisceau de Kent**)\n"
                "- Voie accessoire = faisceau musculaire entre OG et VG sur le plan de l'anneau\n"
                "- **Tachycardies orthodromiques** (les plus fréquentes) :\n"
                "  - Descente par NAV, remontée par voie accessoire\n"
                "  - QRS fins + activité atriale rétrograde à distance du QRS\n"
                "- **Tachycardies antidromiques** (rares) :\n"
                "  - Descente par voie accessoire, remontée par NAV\n"
                "  - QRS larges"
            )),
            FicheRow(concept="", detail_md=(
                "- Les tachycardies jonctionnelles sont **réduites par les manoeuvres vagales** ou par l'**adénosine IV**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="E", titre="Extrasystoles", rows=[
            FicheRow(concept="Définition générale", detail_md=(
                "- Activation prématurée (trop précoce) par rapport à l'activation attendue d'une cavité cardiaque\n"
                "- Fréquentes, physiologiques sur coeur sain\n"
                "- Charge (nombre/24h) augmente avec l'âge et la cardiopathie\n"
                "- Extrasystoles fréquentes ou polymorphes → rechercher une **cardiopathie**"
            )),
            FicheRow(concept="◆ Types d'extrasystoles selon l'origine", detail_md=(
                "| Type | ECG |\n"
                "|------|-----|\n"
                "| **Atriale (ESA)** | Onde P précoce de morphologie différente de la P sinusale + QRS fin ; P parfois masquée par onde T précédente |\n"
                "| **Jonctionnelle** | QRS fin ± onde P' rétrograde ; rares, traduisent une pathologie de la jonction nodohissienne |\n"
                "| **Ventriculaire (ESV)** | QRS large ± onde P' rétrograde (= trouble du rythme ventriculaire) |"
            )),
            FicheRow(concept="Répartition des extrasystoles", detail_md=(
                "- Répétitives : doublets, triplets, salves\n"
                "- Rythmées :\n"
                "  - 1 battement sur 2 : **bigéminisme**\n"
                "  - 1 battement sur 3 : **trigéminisme**\n"
                "  - etc."
            )),
        ]),
    ])

    # ── PARTIE IV : TROUBLES DU RYTHME VENTRICULAIRE ──
    partie_iv = Partie(numero="IV", titre="Troubles du rythme ventriculaire", sous_parties=[
        SousPartie(lettre="A", titre="Tachycardies ventriculaires", rows=[
            FicheRow(concept="◆ Mécanismes", detail_md=(
                "- Tachycardies naissant en dessous de la bifurcation hissienne\n"
                "- Ne passent pas par les voies de conduction (NAV, His, branches, Purkinje)\n"
                "- Conduction lente de proche en proche → **QRS large**\n"
                "- Deux mécanismes :\n"
                "  - **Réentrée** (le plus fréquent sur cardiopathie) - autour d'une zone de fibrose (infarctus, CMP)\n"
                "  - **Automatisme anormal** (le plus fréquent sur coeur sain)"
            )),
            FicheRow(concept="", detail_md=(
                "- **Toute tachycardie régulière à QRS larges est une TV jusqu'à preuve du contraire**"
            ), kind="a_retenir"),
            FicheRow(concept="", detail_md=(
                "- État électrique instable, **prémonitoire de l'arrêt cardiaque**\n"
                "- Observée dans > 50% des morts subites\n"
                "- Une TV dégénère en FV puis en asystolie (anoxie cellulaire) si non prise en charge\n"
                "- Suspicion de TV → alerte (15), préparation à la réanimation"
            ), kind="piege"),
            FicheRow(concept="◆ Critères diagnostiques simples", detail_md=(
                "- Tachycardie : FC > 100 bpm\n"
                "- **QRS > 120 ms** pour au moins 3 battements consécutifs\n"
                "- **TVNS** : entre 3 battements et 30 secondes\n"
                "- **TV soutenue** : durée > 30 secondes\n"
                "- Caractère monomorphe (QRS identiques) ou polymorphe (conséquences étiologiques et hémodynamiques)"
            )),
            FicheRow(concept="◆ Arguments de certitude de TV", detail_md=(
                "- **Dissociation ventriculoatriale** : ondes P plus lentes et dissociées des QRS (plus de QRS que de P → forcément ventriculaire)\n"
                "- À ne pas confondre avec la dissociation AV du BAV complet (qui a plus de P que de QRS)\n"
                "- **Complexes de capture ou de fusion** :\n"
                "  - Capture : QRS fin précédé d'une onde P (P sinusale traverse les voies de conduction)\n"
                "  - Fusion : QRS intermédiaire entre QRS fin et TV (compétition activation sinusale/TV)\n"
                "  - Ne peuvent être présents qu'en cas de dissociation ventriculoatriale"
            )),
            FicheRow(concept="Arguments en faveur d'une TV (sans certitude)", detail_md=(
                "- Cardiopathie sous-jacente +++\n"
                "- Concordance positive ou négative : QRS entièrement positif (R) ou négatif (QS) de V1 à V6\n"
                "- Déviation axiale extrême : QRS positif en aVR (non visible dans BBD ou BBG)\n"
                "- QRS larges avec aspect différent d'un bloc de branche habituel"
            )),
        ]),
        SousPartie(lettre="B", titre="Fibrillation ventriculaire", rows=[
            FicheRow(concept="◆ Urgence absolue", detail_md=(
                "- **Cardioversion électrique immédiate** avant tout autre geste\n"
                "- Massage cardiaque en attendant le choc électrique\n"
                "- Perte de connaissance après quelques secondes (débit cardiaque nul)\n"
                "- Pouls carotidien aboli = **arrêt cardiaque**"
            )),
            FicheRow(concept="ECG de la FV", detail_md=(
                "- Tachycardie irrégulière à QRS larges polymorphes\n"
                "- Aspect de fuseaux larges ou de fines vagues"
            )),
        ]),
        SousPartie(lettre="C", titre="Torsades de pointes", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- Forme particulière de **tachycardie ventriculaire polymorphe**\n"
                "- Peut s'arrêter spontanément OU dégénérer en FV\n"
                "- Parfois impossible à différencier de la FV sur l'ECG seul\n"
                "- Diagnostic : QT long avant le trouble + contexte clinique\n"
                "- FV : ischémie, cardiopathie évoluée. Torsade : QT long (voir étiologies)"
            )),
            FicheRow(concept="◆ Étiologies (allongement du QT)", detail_md=(
                "- Bradycardie extrême : échappements à QRS larges des BAV bas situés, intoxication aux bradycardisants\n"
                "- **Hypokaliémie**\n"
                "- **Hypocalcémie**\n"
                "- **Hypomagnésémie**\n"
                "- Médicaments allongeant le QT : antiarythmiques, psychotropes, antibiotiques, antiémétiques, antipaludéens (cf. Dictionnaire Vidal)\n"
                "- Syndrome du QT long congénital (maladie génétique)"
            )),
            FicheRow(concept="◆ Prise en charge", detail_md=(
                "- Corriger les troubles ioniques\n"
                "- Accélérer la fréquence cardiaque\n"
                "- Arrêter les médicaments allongeant le QT\n"
                "- Mesure allongée du QT à l'ECG : alerte → vérifier médicaments et ionogramme"
            )),
        ]),
    ])

    # ── PARTIE V : HYPERTROPHIES ET AUTRES PATHOLOGIES ──
    partie_v = Partie(numero="V", titre="Hypertrophies et autres pathologies", sous_parties=[
        SousPartie(lettre="A", titre="Hypertrophies atriales et ventriculaires", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Terme historique signifiant augmentation de la quantité de cellules myocardiques d'une cavité\n"
                "- Conséquence d'une dilatation et/ou d'un épaississement de la paroi\n"
                "- Parfois corrélée au degré de fibrose"
            )),
            FicheRow(concept="◆ Hypertrophie atriale droite (HAD)", detail_md=(
                "- Survient le plus souvent par dilatation\n"
                "- **Onde P > 2,5 mm** (souvent pointue) en **D2**\n"
                "- OU onde P > 2 mm en V1 ou V2"
            )),
            FicheRow(concept="◆ Hypertrophie atriale gauche (HAG)", detail_md=(
                "- **Onde P de durée > 110 ms** (en pratique 120 ms)\n"
                "- Apparition d'une composante négative > 40 ms en V1"
            )),
            FicheRow(concept="◆ Hypertrophie ventriculaire gauche (HVG)", detail_md=(
                "- **Indice de Sokolow** = S(V1 ou V2) + R(V5 ou V6)\n"
                "- **Normal : < 35 mm**\n"
                "- Forme sévère :\n"
                "  - Onde T négative + sous-décalage ST dans les dérivations latérales (D1, aVL, V5, V6)\n"
                "  - Anomalies secondaires de repolarisation\n"
                "  - Disparition de l'onde Q de dépolarisation septale dans les mêmes dérivations\n"
                "- Déviation axiale modeste vers la gauche\n"
                "- QRS un peu élargis mais souvent < 120 ms\n"
                "- Étiologies les plus fréquentes : **HTA**, puis **rétrécissement aortique**\n"
                "- Termes historiques : forme sévère = 'surcharge systolique' ; modérée = 'diastolique'"
            )),
            FicheRow(concept="", detail_md=(
                "- HVG électrique importante : peut donner un aspect QS en V1-V2 **mimant une séquelle d'infarctus** (pseudonécrose)\n"
                "- Peut aussi mimer un sus-décalage ST en V1-V2"
            ), kind="piege"),
            FicheRow(concept="Hypertrophie ventriculaire droite (HVD)", detail_md=(
                "- Intérêt modeste à l'ère de l'échocardiographie\n"
                "- Intérêt clinique chez les patients avec BPCO ou atteinte pulmonaire sévère\n"
                "- Signe le plus précoce : **déviation axiale du QRS > 110°** (en pratique 90°)\n"
                "- V1 : onde R ample > 6 mm\n"
                "- V5, V6 : onde S ample > 7 mm\n"
                "- Souvent associée à : HAD + microvoltage chez les patients BPCO\n"
                "- Onde T négative et asymétrique en V1, parfois V2, V3 dans les formes sévères\n"
                "- Souvent BBD associé"
            )),
            FicheRow(concept="◆ Aspect S1Q3T3 (embolie pulmonaire)", detail_md=(
                "- **Hypertrophie aiguë** du VD\n"
                "- S en D1, Q en D3, T négative en D3\n"
                "- Déviation axiale droite"
            )),
        ]),
        SousPartie(lettre="B", titre="Dyskaliémies", rows=[
            FicheRow(concept="◆ Hypokaliémie", detail_md=(
                "- **Onde T plate ou négative**, diffuse avec ST sous-décalé\n"
                "- QRS normal\n"
                "- Allongement du QT\n"
                "- Apparition d'une **onde U** (onde supplémentaire derrière T, ne pas intégrer dans la mesure du QT)\n"
                "- Troubles du rythme : ESV, TV, **torsade de pointes**, FV"
            )),
            FicheRow(concept="◆ Hyperkaliémie", detail_md=(
                "- **Onde T ample, pointue et symétrique**\n"
                "- Allongement du PR\n"
                "- Élargissement du QRS\n"
                "- Complications : BAV, TV, dysfonction sinusale"
            )),
        ]),
        SousPartie(lettre="C", titre="Péricardites", rows=[
            FicheRow(concept="◆ Phase 1 (brève)", detail_md=(
                "- Microvoltage (d'autant plus important si épanchement liquidien)\n"
                "- **Sus-décalage ST** :\n"
                "  - Concave vers le haut\n"
                "  - Diffus\n"
                "  - Concordant\n"
                "  - **Sans image en miroir**\n"
                "- Sous-décalage de PQ (PR)"
            )),
            FicheRow(concept="Phases 2, 3, 4", detail_md=(
                "- Phase 2 : onde T plate dans toutes les dérivations, ST isoélectrique\n"
                "- Phase 3 : onde T négative persistante\n"
                "- Phase 4 : retour progressif à la normale"
            )),
            FicheRow(concept="", detail_md=(
                "- Ne pas conclure à tort à une péricardite devant un SCA ST+ : l'**image en miroir peut être absente** dans certains SCA"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Préexcitation et Wolff-Parkinson-White", rows=[
            FicheRow(concept="Voie accessoire (faisceau de Kent)", detail_md=(
                "- Fibre musculaire ectopique connectant l'atrium au ventricule\n"
                "- 2 passages possibles oreillette-ventricule : NAV + voie accessoire\n"
                "- Conduction rapide par la voie accessoire → **préexcitation** (excitation du VG avant dépolarisation physiologique par le NAV)\n"
                "- Une voie accessoire typique conduit dans les deux sens"
            )),
            FicheRow(concept="◆ ECG de la préexcitation", detail_md=(
                "- **PR court (< 120 ms)**\n"
                "- Élargissement du QRS par empâtement du pied = **onde δ (delta)**\n"
                "- Anomalies de repolarisation dans le territoire de la voie accessoire"
            )),
            FicheRow(concept="◆ Syndrome de Wolff-Parkinson-White (WPW)", detail_md=(
                "- Préexcitation antérograde + palpitations par mécanisme de **tachycardie jonctionnelle**\n"
                "- **Risque de mort subite** si perméabilité de la voie accessoire bonne (période réfractaire courte)\n"
                "- En cas de FA, la voie accessoire ne filtre pas l'influx (pas de décrément)\n"
                "- → tachycardie irrégulière à QRS larges variables (FA préexcitée), pouvant dégénérer en FV"
            )),
            FicheRow(concept="Manoeuvres et adénosine", detail_md=(
                "- Blocage du NAV (massage, adénosine) force le passage par la voie accessoire\n"
                "- Utile pour démasquer une préexcitation minime\n"
                "- CI : ne pas faire en cas de FA\n"
                "- **Super-Wolff** (FA + voie accessoire perméable, QRS 'en accordéon') : **CI à l'adénosine** (2e CI avec l'asthme)"
            )),
        ]),
        SousPartie(lettre="E", titre="Maladie coronarienne", rows=[
            FicheRow(concept="Analyse de la repolarisation", detail_md=(
                "- Sur ECG normal : T+ partout sauf aVR, parfois V1, aVL, D3\n"
                "- 2 ondes T négatives dans le même territoire = **pathologie** (ex : T- en D2 et D3 = pathologique en inférieur)"
            )),
            FicheRow(concept="★ ◆ Sus-décalage ST significatif", detail_md=(
                "- **>= 2 mm** de V1 à V3\n"
                "- **>= 1 mm** dans les autres dérivations\n"
                "- Sur **>= 2 dérivations adjacentes**\n"
                "- Si le sus-décalage englobe l'onde T : **onde de Pardee**\n"
                "- Traquer d'abord le sus-décalage (territoire de la coronaire occluse), puis chercher le **miroir** (sous-décalage)"
            )),
            FicheRow(concept="", detail_md=(
                "- Sous-décalage en antérieur (V1-V3) = peut être le **miroir d'un sus-décalage en postérieur (V7-V9)**\n"
                "- Toute douleur thoracique → ECG 18 dérivations"
            ), kind="piege"),
            FicheRow(concept="Évolution du sus-décalage", detail_md=(
                "- Régresse rapidement avec la reperfusion\n"
                "- Persiste plusieurs jours en l'absence de reperfusion\n"
                "- Peut persister indéfiniment si évolution anévrismale de la paroi infarcie\n"
                "- Après 48h : évolution normale vers onde T négative ischémique (parfois longtemps)"
            )),
            FicheRow(concept="◆ 5 étiologies de sus-décalage du ST", detail_md=(
                "- **SCA ST+** : sus-décalage type onde de Pardee avec **miroir**\n"
                "- **Anévrisme ventriculaire** : sus-décalage persistant après SCA\n"
                "- **Repolarisation précoce** : sus-décalage dans les dérivations inférolatérales\n"
                "- **Angor de Prinzmetal** : spasme coronarien, semblable au SCA ST+\n"
                "- **Péricardite** : sus-décalage diffus, concave vers le haut, sans miroir"
            )),
            FicheRow(concept="Diagnostics différentiels du sus-décalage", detail_md=(
                "- BBG ou stimulation par pacemaker : ST sus-décalé approprié dans les dérivations à QRS négatif\n"
                "- HVG marquée : sous-décalage en latéral + sus-décalage en V1-V2"
            )),
            FicheRow(concept="◆ Ondes Q de nécrose", detail_md=(
                "- Apparaissent en principe vers la **6e heure**, parfois précoces dans le SCA ST+\n"
                "- Ne contre-indiquent pas la reperfusion (à tort considérée comme tardive)\n"
                "- Critères :\n"
                "  - Largeur **> 30-40 ms**\n"
                "  - Amplitude **> 1/3 (ou 1/4) du QRS**\n"
                "- Peuvent être remplacées par un écrêtement ou rabotage de l'onde R (V2-V3-V4)"
            )),
            FicheRow(concept="SCA sans sus-décalage de ST", detail_md=(
                "- Sous-décalage ST (lésion sous-endocardique)\n"
                "- Inversion des ondes T (ischémie sous-épicardique)\n"
                "- Pseudo-normalisation d'ondes T antérieurement négatives\n"
                "- Aplatissement des ondes T\n"
                "- **ECG normal possible !**\n"
                "- Anomalies parfois masquées par un pacemaker"
            )),
        ]),
    ])

    # ── PARTIE VI : STIMULATEUR CARDIAQUE ET INDICATIONS ──
    partie_vi = Partie(numero="VI", titre="Stimulateur cardiaque et indications", sous_parties=[
        SousPartie(lettre="A", titre="ECG et pacemaker", rows=[
            FicheRow(concept="◆ Indications de pacemaker", detail_md=(
                "- **Bradycardies symptomatiques** :\n"
                "  - Dysfonction sinusale\n"
                "  - BAV2 Mobitz 1\n"
                "  - Bradycardie sinusale\n"
                "- **BAV infrahissien (même asymptomatique)** :\n"
                "  - BAV2 Mobitz 2\n"
                "  - BAV3"
            )),
            FicheRow(concept="◆ Spike de stimulation", detail_md=(
                "- Impulsion de pacemaker : durée **0,4 à 1 ms**\n"
                "- **Pathognomonique** de la présence d'une stimulation cardiaque\n"
                "- Rien de physiologique n'est aussi court sur un ECG\n"
                "- Stimulation unipolaire : entre sonde et boîtier → spike bien visible sur ECG de surface\n"
                "- Stimulation bipolaire : entre bout de sonde et électrode proximale → spike peu visible"
            )),
            FicheRow(concept="Modes de stimulation", detail_md=(
                "- Dysfonction sinusale : pacemaker stimule l'oreillette → onde P après le spike\n"
                "- BAV : pacemaker écoute l'oreillette et stimule le ventricule avec délai AV programmé\n"
                "  - QRS large après le spike avec aspect de **BBG** (stimulation VD transmise lentement de proche en proche)"
            )),
            FicheRow(concept="Types de prothèses", detail_md=(
                "- **Pacemaker** : stimulation\n"
                "- **Défibrillateur** : assure aussi fonction pacemaker (sauf sous-cutané)\n"
                "- **Resynchronisation cardiaque (CRT)** : stimulateur, donc assure aussi fonction pacemaker\n"
                "- Possible d'associer les 3 fonctions : défibrillateur de resynchronisation"
            )),
            FicheRow(concept="Télésuivi des prothèses cardiaques (Item 17)", detail_md=(
                "- Standard progressif\n"
                "- Dispositif à côté du lit, communique avec la prothèse toutes les nuits\n"
                "- Alerte sur plateforme en cas d'anomalie\n"
                "- Améliore le suivi : raccourcit la prise en charge, évite hospitalisations et décès"
            )),
        ]),
        SousPartie(lettre="B", titre="Monitorage et ECG conventionnel", rows=[
            FicheRow(concept="Indications du monitorage ECG", detail_md=(
                "- Toutes situations d'urgence ou de réanimation\n"
                "- Transferts médicalisés\n"
                "- Soins intensifs cardiologiques (SCA, etc.)\n"
                "- Syncope avec cause rythmique suspectée\n"
                "- Peropératoire et salle de réveil postanesthésique\n"
                "- Réadaptation cardiaque (certains exercices)"
            )),
            FicheRow(concept="◆ Indications de l'ECG 12 dérivations", detail_md=(
                "- Bilans de santé dans les centres de santé\n"
                "- Aptitude professionnelle (conducteurs, pilotes) ou sportive (sports à risque, compétition)\n"
                "- Bilan préopératoire **> 65 ans**, patients à risque, interventions à risque\n"
                "- Enquêtes familiales pour certaines cardiopathies héréditaires\n"
                "- Symptômes : palpitations, douleurs thoraciques, dyspnée, malaise, perte de connaissance, syncope\n"
                "- Bilan de l'**HTA** (obligatoire)\n"
                "- Surveillance des cardiopathies et pathologies non cardiaques avec retentissement CV (diabète, AVC, etc.)"
            )),
        ]),
        SousPartie(lettre="C", titre="Méthode Holter et outils connectés", rows=[
            FicheRow(concept="◆ Holter ECG standard", detail_md=(
                "- ECG longue durée, 2 à 12 dérivations simultanées, **24 à 96 heures** maximum\n"
                "- Support numérique, analyse en différé (centre de lecture)\n"
                "- Indications principales :\n"
                "  - Malaises, syncopes, pertes de connaissance, palpitations épisodiques\n"
                "  - Quand l'ECG standard est non contributif et probabilité de récidive pendant l'enregistrement"
            )),
            FicheRow(concept="Méthodes de très longue durée", detail_md=(
                "- ECG ambulatoire **jusqu'à 21 jours**\n"
                "- Enregistreurs d'événements : ECG en cas de symptôme (outils dédiés ou montres connectées ECG)\n"
                "- Holters sous-cutanés (moniteurs implantables) : suivi **jusqu'à 3 ans**\n"
                "  - Indications : syncopes inexpliquées, FA silencieuse"
            )),
            FicheRow(concept="Autres indications du Holter 24h", detail_md=(
                "- Évaluer l'efficacité thérapeutique des médicaments bradycardisants\n"
                "- Surveillance et réglage des pacemakers\n"
                "- Évaluer le risque rythmique (salves de TV asymptomatiques après infarctus, dans les CMP)"
            )),
            FicheRow(concept="Santé numérique (Item 18)", detail_md=(
                "- Outils diagnostiques connectés : montres, smartphones\n"
                "- Recueil de la FC ou tracé ECG sur 1 dérivation (souvent de bonne qualité)\n"
                "- Facilitent le diagnostic des palpitations peu fréquentes, difficiles à documenter par Holter classique"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Valeurs ECG normales", markdown=(
            "| Paramètre | Valeur normale | Pathologique |\n"
            "|-----------|----------------|--------------|\n"
            "| **Vitesse** | 25 mm/s (40 ms/mm) | - |\n"
            "| **1 grand carreau** | 5 mm = 200 ms | - |\n"
            "| **Amplitude** | 1 mm = 0,1 mV | - |\n"
            "| **FC repos** | 60-100 bpm | < 60 (bradycardie) ; > 100 (tachycardie) |\n"
            "| **Onde P** | < 120 ms (norme stricte 110), axe 60° | HAD > 2,5 mm en D2 ; HAG > 110 ms |\n"
            "| **PR** | 120-200 ms | < 120 (préexcitation) ; > 200 (BAV1) |\n"
            "| **QRS** | 70-110 ms, axe -30 à +90° | > 120 ms (bloc, TV) |\n"
            "| **QTc Bazett** | < 450 ms | > 450 ms (risque torsade) |\n"
            "| **Sokolow** | < 35 mm | > 35 mm (HVG) |"
        )),
        TableauSynthese(titre="Classification de Vaughan-Williams des antiarythmiques", markdown=(
            "| Classe | Mécanisme | Effet arythmies atriales | Effet arythmies ventriculaires | Ralentit NAV | DCI principales |\n"
            "|--------|-----------|--------------------------|--------------------------------|--------------|-----------------|\n"
            "| **Classe I** | Canaux sodiques | Oui | Oui | - | Flécaïnide |\n"
            "| **Classe II** | Bêtabloquants | Oui | - | Oui | Bisoprolol |\n"
            "| **Classe III** | Canaux potassiques | Oui | - | - | Amiodarone, sotalol |\n"
            "| **Classe IV** | Canaux calciques | - | - | Oui | Vérapamil |\n"
            "| **Digitaliques** | Inhibent Na/K-ATPase | - | - | Oui | Digoxine |"
        )),
        TableauSynthese(titre="Hiérarchie des pacemakers cardiaques", markdown=(
            "| Pacemaker | Localisation | FC d'échappement |\n"
            "|-----------|--------------|------------------|\n"
            "| **Sinusal** | Noeud sinusal (OD) | 60-80 bpm |\n"
            "| **Jonctionnel** | NAV + His | 40-60 bpm |\n"
            "| **Ventriculaire** | Branches, Purkinje | 15-30 bpm |"
        )),
        TableauSynthese(titre="Diagnostic des blocs de branche et hémiblocs", markdown=(
            "| Bloc | QRS | V1 | Autres critères |\n"
            "|------|-----|----|-----------------| \n"
            "| **BBD complet** | > 120 ms | RsR' positif | V6 : qRs avec S traînante |\n"
            "| **BBG complet** | > 120 ms | rS ou QS négatif | V6, D1, aVL : notch + R exclusive |\n"
            "| **HBAG** | > 110 ms | - | Axe < -30° (D2 négatif) |\n"
            "| **HBPG** | > 110 ms | - | Axe > +90° (D1 négatif, S1Q3) |\n"
            "| **Bloc bifasciculaire** | > 120 ms | Selon | BBG ou BBD + hémibloc |\n"
            "| **Bloc trifasciculaire** | - | - | BAV complet infrahissien |"
        )),
        TableauSynthese(titre="Diagnostic différentiel des tachycardies", markdown=(
            "| Type | Régularité | QRS | Activité atriale |\n"
            "|------|------------|-----|------------------|\n"
            "| **Tachycardie sinusale** | Régulier (variation progressive) | Fins | P sinusales (+D1,D2,D3,aVF) |\n"
            "| **Fibrillation atriale** | Irrégulièrement irrégulier | Fins | Mailles ou trémulation |\n"
            "| **Flutter typique** | Régulier (2/1, 3/1...) | Fins | F négatives D2,D3,aVF ; 300 bpm |\n"
            "| **TAF** | Régulier | Fins, PR long | P monomorphes, retour ligne base |\n"
            "| **Tachycardie jonctionnelle** | Très régulier (~200 bpm) | Fins | Non visible ou rétrograde |\n"
            "| **TV** | Régulier | Larges > 120 ms | Dissociation VA, capture/fusion |\n"
            "| **FV** | Irrégulier | Larges polymorphes | Aucune |\n"
            "| **Torsades de pointes** | Polymorphe | Larges (variation amplitude) | QT long |"
        )),
        TableauSynthese(titre="Sus-décalage ST : 5 étiologies + diagnostics différentiels", markdown=(
            "| Étiologie | Aspect | Miroir |\n"
            "|-----------|--------|--------|\n"
            "| **SCA ST+** | Onde de Pardee | Oui |\n"
            "| **Anévrisme ventriculaire** | Persistance post-SCA | Possible |\n"
            "| **Repolarisation précoce** | Inférolatérales | Non |\n"
            "| **Prinzmetal** | Identique au SCA (spasme) | Oui |\n"
            "| **Péricardite** | Diffus, concave vers haut | Non + sous-décalage PQ |\n"
            "| **DD : BBG/pacemaker** | Sus-décalage approprié si QRS négatif | - |\n"
            "| **DD : HVG marquée** | Sus en V1-V2, sous en latéral | - |"
        )),
        TableauSynthese(titre="Anomalies ECG des dyskaliémies", markdown=(
            "| Anomalie | Hypokaliémie | Hyperkaliémie |\n"
            "|----------|--------------|---------------|\n"
            "| **Onde T** | Plate ou négative, ST sous-décalé | Ample, pointue, symétrique |\n"
            "| **PR** | Normal | Allongé |\n"
            "| **QRS** | Normal | Élargi |\n"
            "| **QT** | Allongé | - |\n"
            "| **Onde U** | Présente | - |\n"
            "| **Arythmies** | ESV, TV, torsade, FV | BAV, TV, dysfonction sinusale |"
        )),
    ]

    # ── CHIFFRES CLÉS ──
    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Vitesse ECG | **25 mm/s** | Calibration standard |\n"
        "| Amplitude | **1 mm = 0,1 mV** | Calibration standard |\n"
        "| Grand carreau | **5 mm = 200 ms** | Vitesse 25 mm/s |\n"
        "| FC pacemaker sinusal | **60-80 bpm** | Au repos |\n"
        "| FC pacemaker jonctionnel | **40-60 bpm** | Échappement |\n"
        "| FC pacemaker ventriculaire | **15-30 bpm** | Échappement |\n"
        "| Bradycardie | **< 60 bpm** | Définition adulte |\n"
        "| Tachycardie | **> 100 bpm** | Définition adulte |\n"
        "| FC normale repos | **60-100 bpm** | Adulte |\n"
        "| Durée onde P | **< 120 ms** | Norme stricte 110 ms |\n"
        "| Intervalle PR | **120-200 ms** | Normal |\n"
        "| Durée QRS normal | **70-110 ms** | - |\n"
        "| Axe QRS normal | **-30° à +90°** | aVL à aVF |\n"
        "| QTc Bazett | **< 450 ms** | Normal |\n"
        "| Indice de Sokolow | **< 35 mm** | HVG si > |\n"
        "| Calcul FC | **300 / nb grands carreaux RR** | Méthode rapide |\n"
        "| FC RR=1 grand carreau | **300 bpm** | - |\n"
        "| FC RR=2 grands carreaux | **150 bpm** | - |\n"
        "| Flutter typique | **300 bpm** atrial, **150 bpm** vent. (2/1) | - |\n"
        "| Flutter atypique | **120-320 bpm** | - |\n"
        "| FA | **100-200 bpm** | Tachycardie irrégulièrement irrégulière |\n"
        "| Tachycardie jonctionnelle | **130-260 bpm** (~200) | - |\n"
        "| TV : durée critère | **QRS > 120 ms** x 3 battements | Tachycardie ventriculaire |\n"
        "| TVNS | **3 batt. - 30 sec** | TV non soutenue |\n"
        "| TV soutenue | **> 30 sec** | - |\n"
        "| Adénosine : durée d'effet | **~10 secondes** | Flash IV |\n"
        "| BBD/BBG complet | **QRS > 120 ms** | - |\n"
        "| BBD/BBG incomplet | **QRS 110-120 ms** | - |\n"
        "| Hémibloc | **QRS > 110 ms** | - |\n"
        "| HBAG | Axe **< -30°** | D2 négatif |\n"
        "| HBPG | Axe **> +90°** | S1Q3, D1 négatif |\n"
        "| BAV1 | **PR > 200 ms** fixe | - |\n"
        "| HAD | **P > 2,5 mm** en D2 | - |\n"
        "| HAD V1/V2 | **P > 2 mm** | - |\n"
        "| HAG | **P > 110 ms** (durée), composante négative > 40 ms en V1 | - |\n"
        "| Préexcitation | **PR < 120 ms**, onde delta | - |\n"
        "| HVD V1 | **R > 6 mm** | - |\n"
        "| HVD V5/V6 | **S > 7 mm** | - |\n"
        "| HVD axe | **> +110°** (90° en pratique) | - |\n"
        "| Sus-décalage ST significatif | **>= 2 mm V1-V3**, **>= 1 mm** ailleurs | Sur >= 2 dérivations adjacentes |\n"
        "| Ondes Q de nécrose | **> 30-40 ms**, **> 1/3 ou 1/4 QRS** | Vers 6e heure |\n"
        "| Holter standard | **24-96 h**, 2-12 dérivations | - |\n"
        "| Holter ambulatoire longue durée | **jusqu'à 21 jours** | - |\n"
        "| Holter sous-cutané | **jusqu'à 3 ans** | Syncopes inexpliquées, FA silencieuse |\n"
        "| Bilan préopératoire systématique | **> 65 ans** | - |\n"
        "| Spike pacemaker | **0,4 à 1 ms** | Pathognomonique |"
    ))

    # ── POINTS CLÉS ──
    points_cles = [
        "Analyse systématique : **rythme**, **conduction** (PR, QRS, QT), **axe**, **repolarisation**, morphologique",
        "Rythme sinusal = **P+ en D1, D2, aVF** + QRS après chaque P + P avant chaque QRS",
        "Bradycardie = **2 mécanismes seuls** : dysfonction sinusale ou BAV (2 ou 3) ; jamais un bloc de branche",
        "Bloc de branche : **QRS > 120 ms** ; V1+ = **BBD**, V1- = **BBG** ; HBAG = axe < -30°, HBPG > +90°",
        "**Toute tachycardie régulière à QRS larges = TV** jusqu'à preuve du contraire (alerte 15, réa)",
        "Manoeuvres vagales et **adénosine IV** : diagnostic et traitement des tachycardies SV (CI : asthme)",
        "**FA** = tachycardie irrégulièrement irrégulière à QRS fins ; **flutter** = activité atriale monomorphe",
        "**Sokolow > 35 mm** = HVG ; peut mimer pseudonécrose en V1-V2 (piège classique)",
        "**SCA ST+** : sus-décalage >= 2 mm V1-V3 ou >= 1 mm ailleurs, sur >= 2 dérivations adjacentes + miroir",
        "**Douleur thoracique + BBG** = SCA antérieur, évaluation cardiologique rapide sans attendre troponine",
    ]

    # ── FICHE ÉCLAIR ──
    fiche_eclair_md = (
        "**Valeurs normales** : FC 60-100 bpm. PR 120-200 ms. QRS 70-110 ms, axe -30 à +90°. QTc < 450 ms. Sokolow < 35 mm. FC = 300/grands carreaux RR.\n\n"
        "**Méthode** : rythme → conduction → axe → repolarisation → morphologique. Sinusal = P+ en D1-D2-aVF + P avant chaque QRS.\n\n"
        "**Pacemakers** : sinusal 60-80 > jonctionnel 40-60 > ventriculaire 15-30 bpm.\n\n"
        "**Blocs branche** : BBD = QRS > 120 ms, V1 RsR'+. BBG = V1 rS/QS-. HBAG = axe < -30°. HBPG = axe > +90°.\n\n"
        "**BAV** : BAV1 = PR > 200 ms. Mobitz 1 = allongement progressif + P bloquée. Mobitz 2 = P bloquée inopinée. BAV3 = dissociation. Bradycardie = dysfonction sinusale ou BAV.\n\n"
        "**FA** : irrégulièrement irrégulière, QRS fins, mailles/trémulation.\n\n"
        "**Flutter typique** : 300 bpm atriaux, F- en D2-D3-aVF, ventricules 150 (2/1).\n\n"
        "**Bouveret** : très régulière ~200 bpm, QRS fins. Réduit par manoeuvres vagales / adénosine.\n\n"
        "**TV** : QRS > 120 ms x 3 batt + dissociation VA + capture/fusion. Toute tachycardie régulière QRS larges = TV jusqu'à preuve du contraire.\n\n"
        "**Torsade** : TV polymorphe sur QT long. HypoK/Ca/Mg, bradycardie, médicaments (psychotropes, ATB).\n\n"
        "**Manoeuvres vagales** : Valsalva, compression carotidienne, eau froide. Adénosine flash IV (CI asthme, super-Wolff).\n\n"
        "**WPW** : PR < 120 ms + onde delta. Mort subite si FA préexcitée. CI adénosine si super-Wolff.\n\n"
        "**HVG** : Sokolow > 35 mm. HTA puis RAo. Pseudonécrose V1-V2.\n\n"
        "**Dyskaliémies** : hypoK = T plate + onde U + QT long. HyperK = T ample symétrique + PR long + QRS large.\n\n"
        "**SCA ST+** : >= 2 mm V1-V3, >= 1 mm ailleurs, >= 2 dérivations adjacentes. Onde de Pardee + miroir. 5 étiologies sus-ST : SCA, anévrisme, repolarisation précoce, Prinzmetal, péricardite (diffus concave sans miroir).\n\n"
        "**Réflexes** : douleur + BBG = SCA antérieur. Syncope + bloc bifasciculaire = télémétrie. Bloc alternant = pacemaker.\n\n"
        "**Indications pacemaker** : bradycardies symptomatiques ; BAV infrahissien (Mobitz 2, BAV3) même asymptomatique.\n"
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 231 - Électrocardiogramme",
        annee="2025-2026",
        item="Item 231",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 231",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-231_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

"""Génère la fiche de l'Item 230 - Douleur thoracique aiguë (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Conduite à tenir devant une douleur thoracique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Première étape : rechercher une détresse vitale"),
            PlanSousPartie(lettre="B", titre="Seconde étape : les quatre urgences cardiovasculaires (PIED)"),
        ]),
        PlanPartie(numero="II", titre="Orientation diagnostique : urgences cardiaques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Syndrome coronarien aigu"),
            PlanSousPartie(lettre="B", titre="Dissection de l'aorte thoracique"),
            PlanSousPartie(lettre="C", titre="Embolie pulmonaire"),
            PlanSousPartie(lettre="D", titre="Péricardite aiguë, tamponnade et myopéricardite"),
        ]),
        PlanPartie(numero="III", titre="Douleurs chroniques de cause cardiaque", sous_parties=[
            PlanSousPartie(lettre="A", titre="Étiologies des douleurs cardiaques chroniques"),
            PlanSousPartie(lettre="B", titre="Démarche diagnostique en cas de SCC"),
        ]),
        PlanPartie(numero="IV", titre="Causes extracardiaques de douleur thoracique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Douleurs d'origine pulmonaire et œsophagienne"),
            PlanSousPartie(lettre="B", titre="Douleurs pariétales, neurologiques, abdominales projetées"),
            PlanSousPartie(lettre="C", titre="Douleurs psychogènes et les 6 urgences non cardiaques"),
        ]),
        PlanPartie(numero="V", titre="Points clés et notions indispensables/inacceptables", sous_parties=[
            PlanSousPartie(lettre="A", titre="Points clés transversaux"),
            PlanSousPartie(lettre="B", titre="Notions indispensables et inacceptables"),
        ]),
    ]

    # ── PARTIE I : CONDUITE À TENIR ──
    partie_i = Partie(numero="I", titre="Conduite à tenir devant une douleur thoracique", sous_parties=[
        SousPartie(lettre="A", titre="Première étape : rechercher une détresse vitale", rows=[
            FicheRow(concept="◆ Détresse respiratoire", detail_md=(
                "- **Polypnée** : FR > 30/min\n"
                "- **Bradypnée** : FR < 10/min ou pauses respiratoires\n"
                "- Tirage par mise en jeu des muscles respiratoires accessoires\n"
                "- Sueurs, cyanose, désaturation (**SpO₂ < 90 %**)\n"
                "- Encéphalopathie respiratoire"
            )),
            FicheRow(concept="◆ Détresse hémodynamique", detail_md=(
                "- **Arrêt circulatoire** : pouls carotidien ou fémoral non perçu + patient inconscient\n"
                "- **État de choc** : collapsus avec hypoperfusion périphérique, hypotension avec pâleur, "
                "marbrures et oligurie\n"
                "- Signes de cœur pulmonaire\n"
                "- **Pouls paradoxal** : dépression du pouls à l'inspiration profonde"
            )),
            FicheRow(concept="Atteinte neurologique", detail_md=(
                "- Troubles de la conscience : confusion, agitation, convulsions, etc.\n"
                "- À rechercher systématiquement car peut témoigner d'une hypoperfusion cérébrale "
                "ou d'une complication neurologique (dissection notamment)"
            )),
            FicheRow(concept="", detail_md=(
                "- La recherche d'une **détresse vitale précède tout** : la signification de la douleur "
                "s'efface devant un collapsus, un état de choc, une détresse respiratoire ou des signes "
                "neurologiques — la prise en charge thérapeutique passe avant le diagnostic étiologique."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Seconde étape : les quatre urgences cardiovasculaires (PIED)", rows=[
            FicheRow(concept="◆ Moyen mnémotechnique « PIED »", detail_md=(
                "- **P** = Péricardite aiguë (le plus souvent bénigne, mais peut se compliquer "
                "d'un épanchement péricardique abondant voire d'une **tamponnade**)\n"
                "- **I** = Infarctus (syndrome coronarien aigu)\n"
                "- **E** = Embolie pulmonaire\n"
                "- **D** = Dissection aortique"
            )),
            FicheRow(concept="◆ Cinquième étiologie à évoquer : rupture de l'œsophage", detail_md=(
                "- Survenue exceptionnelle mais **urgence thérapeutique**\n"
                "- À évoquer devant douleur thoracique associée à :\n"
                "  - une dyspnée\n"
                "  - un emphysème sous-cutané (crépitation neigeuse)\n"
                "  - un pneumomédiastin"
            )),
            FicheRow(concept="◆ Examens complémentaires systématiques", detail_md=(
                "- **ECG 12 dérivations + V3R, V4R, V7, V8, V9** (dérivations postérieures et droites)\n"
                "- Radiographie pulmonaire\n"
                "- **Troponines ultrasensibles** (Tn-us)"
            )),
            FicheRow(concept="◆ Transfert médicalisé via le 15", detail_md=(
                "- Transfert en **Usic** (unité de soins intensifs cardiologiques) ou directement en "
                "salle de coronarographie en cas de SCA ST+\n"
                "- Risque de fibrillation ventriculaire notamment dans les syndromes coronariens aigus\n"
                "- **Appel du 15** systématique : ne pas y recourir est une faute grave "
                "(mortalité préhospitalière élevée)"
            )),
            FicheRow(concept="", detail_md=(
                "- **PIED** : Péricardite — Infarctus — Embolie pulmonaire — Dissection aortique. "
                "Quatre urgences cardiovasculaires à évoquer systématiquement devant toute douleur "
                "thoracique aiguë."
            ), kind="mnemo"),
            FicheRow(concept="", detail_md=(
                "- **Ne jamais doser la troponine avant l'ECG** : c'est l'ECG qui conditionne "
                "la prise en charge initiale. En cas de SCA ST+, la reperfusion ne doit pas attendre "
                "le résultat de la troponine."
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE II : URGENCES CARDIAQUES ──
    partie_ii = Partie(numero="II", titre="Orientation diagnostique : urgences cardiaques", sous_parties=[
        SousPartie(lettre="A", titre="Syndrome coronarien aigu", rows=[
            FicheRow(concept="Terrain", detail_md=(
                "- Présence de facteurs de risque cardiovasculaire\n"
                "- Antécédents coronariens connus"
            )),
            FicheRow(concept="◆ Caractéristiques de la douleur", detail_md=(
                "- Douleur spontanée de repos, **angor de novo** ou **angor crescendo**\n"
                "- Infarctus à évoquer dès que la douleur dépasse **20 minutes**\n"
                "- Dyspnée associée dans 10 % des cas\n"
                "- Douleur coronarienne typique : rétrosternale, constrictive\n"
                "- Formes atypiques fréquentes chez la femme et le sujet âgé : la douleur "
                "peut siéger de la mandibule à l'ombilic, parfois mimer une douleur gastrique "
                "ou biliopancréatique"
            )),
            FicheRow(concept="Examen clinique", detail_md=(
                "- Normal en l'absence de complications\n"
                "- Rechercher une autre localisation de l'athérosclérose : souffle carotidien ou "
                "fémoral, abolition d'un pouls"
            )),
            FicheRow(concept="◆ ECG : à réaliser le plus rapidement possible", detail_md=(
                "- Conditionne la prise en charge ultérieure\n"
                "- Anomalies : sus-décalage ou sous-décalage du segment ST, ondes T négatives, ondes Q\n"
                "- Un ECG percritique normal **n'élimine pas** le diagnostic\n"
                "- Un **bloc de branche gauche** doit être considéré comme un équivalent de **SCA ST+**\n"
                "- Les ischémies du territoire de l'artère circonflexe peuvent être électriquement "
                "muettes → penser à V7, V8, V9 (postérieures)\n"
                "- Un sous-décalage en V2-V4 + douleur prolongée = à prendre en charge **comme un SCA ST+** "
                "(occlusion circonflexe)"
            )),
            FicheRow(concept="Radiographie pulmonaire", detail_md=(
                "- Normale et souvent inutile dans les tableaux typiques\n"
                "- Sauf signes d'insuffisance cardiaque"
            )),
            FicheRow(concept="◆ Troponines ultrasensibles (Tn-us)", detail_md=(
                "- Inutiles dans le **SCA ST+** confirmé par l'ECG : ne doivent pas retarder la "
                "reperfusion (angioplastie ou thrombolyse)\n"
                "- Indispensables dans le **SCA non ST+** : intérêt diagnostique et pronostique\n"
                "- Algorithme à **2 dosages** (H0 et H1 ou H2, selon méthode) :\n"
                "  - Tn-us à H0 très faible/faible + pas d'augmentation significative à H1/H2 "
                "→ évoquer un diagnostic différentiel (ou SCA bas risque), surveillance en Usic\n"
                "  - Tn-us à H0 élevée OU faible avec augmentation significative à H1/H2 "
                "→ **SCA non ST+ à haut risque**"
            )),
            FicheRow(concept="Tableau comparatif SCA ST+ vs non ST+", detail_md=(
                "| Élément | SCA ST+ | SCA non ST+ |\n"
                "|---------|---------|-------------|\n"
                "| ECG | Sus-décalage ST persistant ou BBG | Sous-décalage ST, T négatives, ou normal |\n"
                "| Troponines | Inutiles avant reperfusion | Indispensables (algorithme H0/H1-H2) |\n"
                "| Reperfusion | **Urgente** (angioplastie/thrombolyse) | Selon stratification du risque |\n"
                "| Transfert | Directement coronarographie | Usic |"
            )),
            FicheRow(concept="", detail_md=(
                "- **ECG percritique normal et troponines normales n'éliminent PAS** un SCA, notamment "
                "un angor instable. La clinique reste centrale."
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Dissection de l'aorte thoracique", rows=[
            FicheRow(concept="◆ Facteurs favorisants", detail_md=(
                "- **HTA ancienne**\n"
                "- **Syndrome de Marfan**"
            )),
            FicheRow(concept="◆ Sémiologie typique de la douleur", detail_md=(
                "- Aiguë, prolongée, intense\n"
                "- Type **déchirement**\n"
                "- Irradiation dans le dos, migratrice, descendant vers les lombes\n"
                "- Parfois associée à une syncope"
            )),
            FicheRow(concept="◆ Examen clinique", detail_md=(
                "- **Asymétrie tensionnelle** : différence **> 20 mmHg** entre les deux bras\n"
                "- Abolition d'un pouls\n"
                "- Souffle d'insuffisance aortique (atteinte de la racine aortique)\n"
                "- Déficit neurologique"
            )),
            FicheRow(concept="Tableaux révélateurs (complications)", detail_md=(
                "- Ischémie aiguë de membre\n"
                "- AVC\n"
                "- Infarctus mésentérique avec douleur abdominale trompeuse\n"
                "- Hémopéricarde avec tamponnade\n"
                "- SCA (extension à une artère coronaire)"
            )),
            FicheRow(concept="◆ Score de probabilité clinique", detail_md=(
                "- Score allant de **0 à 3**\n"
                "- Probabilité faible si score = **0 ou 1**\n"
                "- Probabilité forte si score = **2 ou 3**\n"
                "- 3 critères, 1 point chacun :\n"
                "  - Terrain évocateur : Marfan, ATCD familial aortique, anévrisme/valvulopathie connus, ATCD chirurgie aortique\n"
                "  - Douleur évocatrice : thoracique/dorsale/abdominale, début brutal, intense, déchirement\n"
                "  - Signes cliniques : abolition pouls, asymétrie tensionnelle, déficit neurologique focal, IA, hypotension/choc"
            )),
            FicheRow(concept="ECG", detail_md=(
                "- Normal le plus souvent\n"
                "- Peut révéler un SCA si extension à une artère coronaire"
            )),
            FicheRow(concept="◆ Radiographie thoracique", detail_md=(
                "- **Élargissement du médiastin**\n"
                "- Éventuel épanchement pleural\n"
                "- Aspect de double contour aortique"
            )),
            FicheRow(concept="Examens biologiques", detail_md=(
                "- NFS, plaquettes\n"
                "- CRP\n"
                "- **D-dimères** (rare d'avoir une dissection avec D-dimères normaux)\n"
                "- Troponines ultrasensibles (ischémie myocardique)\n"
                "- Créatine-kinase (rhabdomyolyse)\n"
                "- Créatininémie"
            )),
            FicheRow(concept="◆ Imagerie diagnostique", detail_md=(
                "- ETT ou ETO : possible si stabilité hémodynamique (l'ETO nécessite une stabilité)\n"
                "- **Angioscanner thoracique** : souvent nécessaire pour le diagnostic positif et la "
                "planification chirurgicale (porte d'entrée, extension, atteinte des artères carotides, "
                "mésentériques, rénales)\n"
                "- Si stabilité hémodynamique + probabilité faible (score 0-1) : ETT + radiographie "
                "(élargissement médiastinal) + D-dimères (d'emblée très élevés)"
            )),
            FicheRow(concept="◆ Classifications et prise en charge", detail_md=(
                "- **Type A de Stanford** = types I et II de De Bakey : aorte ascendante → "
                "**chirurgie en urgence**\n"
                "- **Type B de Stanford** : aorte descendante → prise en charge médicale "
                "sauf complication périphérique\n"
                "- PA à normaliser : c'est une **urgence hypertensive**"
            )),
            FicheRow(concept="Classification de Stanford/De Bakey", detail_md=(
                "| Stanford | De Bakey | Localisation | Prise en charge |\n"
                "|----------|----------|--------------|------------------|\n"
                "| Type A | Type I (asc + desc) ou II (asc isolée) | Aorte ascendante | Chirurgie urgente |\n"
                "| Type B | Type III | Aorte descendante | Médicale (sauf complication) |"
            )),
            FicheRow(concept="", detail_md=(
                "- Tableaux atypiques possibles : hémopéricarde, IA aiguë, dissection coronarienne avec "
                "SCA, extension digestive (douleur abdominale), ischémie aiguë de membre révélatrice. "
                "Y penser devant des associations cliniques inhabituelles."
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Embolie pulmonaire", rows=[
            FicheRow(concept="◆ Terrain évocateur", detail_md=(
                "- Cancer\n"
                "- Contraception œstroprogestative + tabac\n"
                "- Période postopératoire, post-partum\n"
                "- Alitement\n"
                "- ATCD personnels ou familiaux de maladie thromboembolique"
            )),
            FicheRow(concept="◆ Présentation clinique typique", detail_md=(
                "- Douleur basithoracique associée à une **dyspnée aiguë** avec polypnée\n"
                "- Toux, parfois hémoptysie tardive\n"
                "- Signes de thrombose veineuse (absents dans 1/3 des cas)\n"
                "- Tachycardie\n"
                "- Signes d'insuffisance ventriculaire droite (signe de gravité)"
            )),
            FicheRow(concept="◆ Deux tableaux opposés", detail_md=(
                "- **Infarctus pulmonaire** : douleur basithoracique pariétopleurale fébrile + "
                "hémoptysie noirâtre tardive → bon pronostic\n"
                "- **Cœur pulmonaire aigu** : dyspnée isolée + signes de défaillance VD ou collapsus "
                "(la douleur est au second plan, c'est une urgence vitale)"
            )),
            FicheRow(concept="◆ ECG : signes de cœur pulmonaire aigu", detail_md=(
                "- Tachycardie sinusale\n"
                "- Aspect **S1Q3**\n"
                "- Bloc de branche droit\n"
                "- Ondes T négatives dans les précordiales droites (V1, V3)"
            )),
            FicheRow(concept="Radiographie pulmonaire", detail_md=(
                "- Atélectasies en bandes\n"
                "- Épanchement pleural basal\n"
                "- Coupole surélevée\n"
                "- Hyperclarté\n"
                "- Souvent normale\n"
                "- **Douleur thoracique + dyspnée + radiographie normale** → évoquer obligatoirement "
                "le diagnostic d'EP"
            )),
            FicheRow(concept="◆ Stratification initiale du risque", detail_md=(
                "- **Haut risque** = présence d'une hypotension (**PAS < 90 mmHg** ou baisse PAS "
                "**≥ 40 mmHg** pendant > 15 min, en l'absence de troubles du rythme, hypovolémie ou sepsis) "
                "ou d'un choc"
            )),
            FicheRow(concept="◆ Algorithme diagnostique", detail_md=(
                "- **EP haut risque** : scanner thoracique si disponible immédiatement, sinon "
                "échocardiographie (dilatation du VD)\n"
                "- **EP sans hypotension/choc** : estimer la probabilité clinique par le "
                "**score de Wells modifié** ou le **score de Genève modifié**\n"
                "- Probabilité faible/modérée + D-dimères positifs (**> 500 µg/L** ou "
                "**> 10 × âge** chez les > 50 ans, recommandations ESC 2019) → angioscanner\n"
                "- Probabilité faible/modérée + D-dimères négatifs (méthode Elisa = "
                "*enzyme-linked immunosorbent assay*) → EP éliminée\n"
                "- Probabilité forte : D-dimères inutiles, angioscanner d'emblée\n"
                "- Probabilité intermédiaire ou haute : traitement antithrombotique débuté "
                "avant la confirmation diagnostique"
            )),
            FicheRow(concept="", detail_md=(
                "- **Triade évocatrice d'EP** : douleur + dyspnée + radiographie de thorax normale "
                "dans un contexte d'alitement ou de néoplasie."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Péricardite aiguë, tamponnade et myopéricardite", rows=[
            FicheRow(concept="Péricardite non compliquée : terrain", detail_md=(
                "- Contexte viral\n"
                "- Fièvre\n"
                "- Forme récidivante avec antécédent de péricardite aiguë"
            )),
            FicheRow(concept="◆ Sémiologie de la péricardite aiguë", detail_md=(
                "- Douleur thoracique **augmentée à l'inspiration profonde**\n"
                "- Augmentée en décubitus\n"
                "- **Calmée par l'antéflexion du buste**\n"
                "- Examen : **frottement péricardique** classiquement fugace et inconstant"
            )),
            FicheRow(concept="◆ ECG dans la péricardite", detail_md=(
                "- **Sus-décalage du segment ST** : concave, diffus ou non systématisé\n"
                "- Sans miroir, sans onde Q\n"
                "- **Sous-décalage du PQ**\n"
                "- Microvoltage"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- Radiographie pulmonaire : parfois élargissement de la silhouette cardiaque\n"
                "- **Échocardiographie + dosage des troponines** systématiques\n"
                "- Possible syndrome inflammatoire biologique\n"
                "- ETT : épanchement péricardique ou normale (péricardite sèche, savoir la répéter)\n"
                "- Diagnostic d'élimination : étiologie la plus bénigne parmi PIED"
            )),
            FicheRow(concept="◆ Tamponnade péricardique : urgence vitale", detail_md=(
                "- À la différence de la péricardite non compliquée, c'est une **urgence vitale**\n"
                "- Manifestations :\n"
                "  - Douleur thoracique + dyspnée, polypnée, orthopnée, toux, parfois "
                "dysphagie, nausée, hoquet\n"
                "  - Signes droits : turgescence jugulaire, reflux hépatojugulaire\n"
                "  - Signes de choc : tachycardie, **PAS < 90 mmHg**\n"
                "  - **Pouls paradoxal** : PAS d'inspiration < PAS d'expiration de **10 mmHg**"
            )),
            FicheRow(concept="Mécanisme du pouls paradoxal", detail_md=(
                "- Inspiration → augmentation du retour veineux → dilatation du VD → "
                "compression du VG → baisse de la PAS"
            )),
            FicheRow(concept="◆ Tamponnade : examens", detail_md=(
                "- ECG : microvoltage, parfois alternance électrique\n"
                "- Radiographie de thorax : cardiomégalie, aspect en « carafe » si "
                "épanchement abondant\n"
                "- **Échocardiographie** : collapsus des cavités droites en expiration, "
                "compression du VG par le VD en inspiration, épanchement abondant"
            )),
            FicheRow(concept="Myopéricardite", detail_md=(
                "- Péricardite avec atteinte du myocarde, le plus souvent virale\n"
                "- Douleur péricarditique pouvant mimer un SCA, parfois avec insuffisance cardiaque\n"
                "- **Élévation prolongée des troponines**\n"
                "- ETT : trouble cinétique du VG segmentaire ou diffus + épanchement péricardique éventuel\n"
                "- La myocardite peut être isolée : principal diagnostic différentiel = SCA\n"
                "- Coronarographie normale\n"
                "- **IRM** : œdème et rehaussement tardif sur séquences avec gadolinium, "
                "prédominant en **sous-épicardique**, sans systématisation artérielle"
            )),
            FicheRow(concept="", detail_md=(
                "- **Ne pas méconnaître les signes de tamponnade** : turgescence jugulaire, PAS < 90 mmHg, "
                "pouls paradoxal — c'est une urgence vitale nécessitant un drainage péricardique en urgence."
            ), kind="piege"),
            FicheRow(concept="", detail_md=(
                "- **Élévation prolongée des troponines + douleur péricarditique = myopéricardite**. "
                "L'IRM montre un rehaussement tardif sous-épicardique non systématisé, à différencier "
                "du rehaussement sous-endocardique systématisé du SCA."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE III : DOULEURS CHRONIQUES CARDIAQUES ──
    partie_iii = Partie(numero="III", titre="Douleurs chroniques de cause cardiaque", sous_parties=[
        SousPartie(lettre="A", titre="Étiologies des douleurs cardiaques chroniques", rows=[
            FicheRow(concept="◆ Angor stable", detail_md=(
                "- Douleur atypique dans la localisation ou les irradiations, ou réduite aux irradiations\n"
                "- Caractéristique si **constrictive**, déclenchée par l'effort (ou un repas), "
                "**cédant à l'effort** ou après un spray de **trinitrine en 1 à 3 minutes**"
            )),
            FicheRow(concept="Angor d'effort du rétrécissement aortique serré", detail_md=(
                "- Cause classique d'angor d'effort chez le sujet âgé\n"
                "- À évoquer devant un souffle systolique éjectionnel au foyer aortique"
            )),
            FicheRow(concept="Angor fonctionnel", detail_md=(
                "- Anémie\n"
                "- Tachycardies (fibrillation atriale)\n"
                "- Hyperthyroïdie"
            )),
            FicheRow(concept="Autres causes", detail_md=(
                "- **Cardiomyopathie hypertrophique** : douleur d'effort\n"
                "- **Hypertension artérielle pulmonaire sévère** : douleurs angineuses par "
                "souffrance ischémique du VD lorsque la pression intraventriculaire droite "
                "dépasse la pression de perfusion coronarienne"
            )),
        ]),
        SousPartie(lettre="B", titre="Démarche diagnostique en cas de SCC", rows=[
            FicheRow(concept="◆ Score de probabilité clinique de maladie coronarienne", detail_md=(
                "- Repose sur :\n"
                "  - Âge\n"
                "  - Sexe\n"
                "  - Caractéristiques de la douleur thoracique (0 à 3 points) :\n"
                "    - +1 si typique\n"
                "    - +1 si provoquée par l'effort ou le stress\n"
                "    - +1 si calmée par le repos ou la trinitrine en < 5 min\n"
                "  - +2 si dyspnée est le symptôme prédominant\n"
                "  - Nombre de FDR cardiovasculaire (0 à 5) : ATCD familial, HTA, tabac, "
                "dyslipidémie, diabète"
            )),
            FicheRow(concept="◆ Stratégie selon la probabilité clinique", detail_md=(
                "| Probabilité clinique | Examens recommandés |\n"
                "|----------------------|----------------------|\n"
                "| Très faible (< 5 %) | **Aucun examen complémentaire** |\n"
                "| Faible (5-15 %) | Scanner coronarien d'emblée OU réévaluation avec autres examens |\n"
                "| Modérée (15-50 %) | Scanner coronarien OU imagerie fonctionnelle (scinti, écho stress, IRM) |\n"
                "| Élevée (50-85 %) | Imagerie fonctionnelle |\n"
                "| Très élevée (> 85 %) | **Coronarographie diagnostique** |"
            )),
            FicheRow(concept="Éléments de réévaluation (probabilité faible 5-15 %)", detail_md=(
                "- Onde Q ou sous-décalage du segment ST sur l'ECG de repos\n"
                "- Troubles du rythme ventriculaire\n"
                "- Épreuve d'effort anormale\n"
                "- Altération de la fonction VG à l'échocardiographie\n"
                "- Score calcique élevé au scanner\n"
                "- Atteinte vasculaire périphérique (doppler cou et MI)"
            )),
        ]),
    ])

    # ── PARTIE IV : CAUSES EXTRACARDIAQUES ──
    partie_iv = Partie(numero="IV", titre="Causes extracardiaques de douleur thoracique", sous_parties=[
        SousPartie(lettre="A", titre="Douleurs d'origine pulmonaire et œsophagienne", rows=[
            FicheRow(concept="◆ Pneumothorax", detail_md=(
                "- Douleur de type pleural\n"
                "- Tympanisme, abolition du murmure vésiculaire\n"
                "- Parfois dyspnée\n"
                "- Diagnostic : **radiographie en expiration** pour les pneumothorax partiels"
            )),
            FicheRow(concept="Épanchement pleural", detail_md=(
                "- Douleur de type pleural + matité, parfois dyspnée\n"
                "- Causes chroniques : mésothéliome, pachypleurite\n"
                "- Diagnostic : radiographie avec **ligne de Damoiseau** (parfois clichés en "
                "décubitus latéral)\n"
                "- Ponction pleurale à but diagnostique"
            )),
            FicheRow(concept="◆ Pneumopathies infectieuses", detail_md=(
                "- Douleur intense **en coup de poignard** de type pleural\n"
                "- Fièvre\n"
                "- Syndrome de condensation : souffle tubaire entouré d'une couronne de "
                "râles crépitants\n"
                "- Opacité radiologique systématisée ou non avec bronchogramme aérien\n"
                "- Éventuel épanchement pleural associé"
            )),
            FicheRow(concept="Douleurs œsophagiennes", detail_md=(
                "- Reflux gastro-œsophagien, œsophagite\n"
                "- **Spasme œsophagien** : douleur d'allure angineuse, déclenchée par la déglutition, "
                "piège : peut être **calmée par les dérivés nitrés**\n"
                "- Dysphagie\n"
                "- Rupture de l'œsophage (exceptionnelle)"
            )),
            FicheRow(concept="", detail_md=(
                "- **Le spasme œsophagien peut être calmé par les dérivés nitrés** : la trinitrine "
                "ne fait pas le diagnostic de SCA — son efficacité n'élimine pas une origine "
                "œsophagienne."
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Douleurs pariétales, neurologiques, abdominales projetées", rows=[
            FicheRow(concept="Douleurs pariétales musculosquelettiques", detail_md=(
                "- **Syndrome de Tietze** : inflammation du cartilage à la jonction sterno-costale, "
                "douleur reproduite par la palpation\n"
                "- Lésions sternales, arthralgies chondrocostales\n"
                "- Fractures costales, éventuellement pathologiques (métastases, myélome multiple)\n"
                "- Douleur musculoligamentaire"
            )),
            FicheRow(concept="Douleurs neurologiques", detail_md=(
                "- Zona intercostal\n"
                "- Tassement vertébral"
            )),
            FicheRow(concept="◆ Douleurs abdominales projetées", detail_md=(
                "- Lithiase vésiculaire\n"
                "- Ulcère gastroduodénal\n"
                "- Pancréatite aiguë\n"
                "- Appendicite sous-hépatique\n"
                "- Abcès sous-phrénique"
            )),
            FicheRow(concept="", detail_md=(
                "- **L'infarctus du myocarde inférieur peut mimer une gastroentérite** : attention aux "
                "douleurs épigastriques aiguës chez un patient à risque. À l'inverse, se méfier d'une "
                "ischémie mésentérique compliquant une dissection aortique."
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Douleurs psychogènes et les 6 urgences non cardiaques", rows=[
            FicheRow(concept="Douleurs d'origine psychogène", detail_md=(
                "- Extrêmement fréquentes\n"
                "- Angoisse, névrose\n"
                "- **Diagnostic d'élimination** à évoquer avec la plus grande prudence"
            )),
            FicheRow(concept="◆ 6 urgences non cardiaques à identifier", detail_md=(
                "- Pleurésies et pneumonies\n"
                "- Pneumothorax\n"
                "- Pancréatite aiguë\n"
                "- Ulcère gastrique ou duodénal compliqué\n"
                "- Cholécystite\n"
                "- Douleurs radiculaires"
            )),
            FicheRow(concept="◆ Moyen mnémotechnique « 4 P »", detail_md=(
                "- Parmi les diagnostics thoraciques non cardiovasculaires :\n"
                "  - **P**neumonie\n"
                "  - **P**leurésie\n"
                "  - **P**neumothorax\n"
                "  - **P**ancréatite"
            )),
            FicheRow(concept="Autres étiologies", detail_md=(
                "- Pas d'urgence vitale pour les autres étiologies\n"
                "- Mais urgent de rassurer et soulager le patient"
            )),
            FicheRow(concept="", detail_md=(
                "- **4 P extracardiaques** : Pneumonie, Pleurésie, Pneumothorax, Pancréatite — à rajouter "
                "aux 4 urgences PIED."
            ), kind="mnemo"),
        ]),
    ])

    # ── PARTIE V : POINTS CLÉS ET NOTIONS INDISPENSABLES/INACCEPTABLES ──
    partie_v = Partie(numero="V", titre="Points clés et notions indispensables/inacceptables", sous_parties=[
        SousPartie(lettre="A", titre="Points clés transversaux", rows=[
            FicheRow(concept="Démarche initiale", detail_md=(
                "- Motif très fréquent de recours aux soins\n"
                "- **Priorité absolue** : rechercher les signes de détresse vitale (collapsus, choc, "
                "détresse respiratoire, neurologique)\n"
                "- Transfert médicalisé via le **15** indispensable"
            )),
            FicheRow(concept="◆ Place des examens", detail_md=(
                "- **Interrogatoire + ECG + troponines ultrasensibles** répétées = base de la prise en charge\n"
                "- Échocardiographie et scanner thoracique souvent utiles en 2ᵉ intention\n"
                "- À réaliser en urgence devant suspicion d'EP ou de dissection aortique"
            )),
            FicheRow(concept="SCA ST+", detail_md=(
                "- Suspecté devant toute douleur thoracique **> 20 min**\n"
                "- Patient avec FDR athérome + douleur rétrosternale = tableau évocateur\n"
                "- Attention : ECG normal ou trompeur (pacemaker), troponines initialement normales\n"
                "- **Reperfusion urgente** sans attendre les troponines\n"
                "- Clinique + ECG = diagnostic dans > 90 % des cas\n"
                "- ECG percritique + troponines normaux **n'éliminent PAS** un angor instable"
            )),
            FicheRow(concept="Pièges classiques selon l'étiologie", detail_md=(
                "- **EP** : triade douleur + dyspnée + radiographie normale en contexte d'alitement/néoplasie\n"
                "- **Péricardite** = tableau le moins préoccupant, mais symptômes voisins d'un SCA ; "
                "myopéricardite encore plus trompeuse (troponines élevées)\n"
                "- **Tamponnade** = urgence vitale à ne pas méconnaître\n"
                "- **Dissection** = douleur déchirante à irradiation postérieure sur poussée hypertensive, "
                "mais tableaux très atypiques possibles\n"
                "- **IDM inférieur** peut mimer une gastroentérite"
            )),
        ]),
        SousPartie(lettre="B", titre="Notions indispensables et inacceptables", rows=[
            FicheRow(concept="◆ Notions indispensables", detail_md=(
                "- Devant une douleur thoracique aiguë, toujours **éliminer en premier une détresse vitale**\n"
                "- Puis éliminer les urgences cardiaques = **PIED** (Péricardite, Infarctus, "
                "Embolie pulmonaire, Dissection aortique)"
            )),
            FicheRow(concept="⚠ Notion inacceptable", detail_md=(
                "- **Faire un dosage de la troponine avant de réaliser un ECG**"
            )),
            FicheRow(concept="Réflexes transversalité", detail_md=(
                "- Item 226 : thrombose veineuse profonde et embolie pulmonaire\n"
                "- Item 235 : péricardite aiguë\n"
                "- Item 339 : syndromes coronariens aigus"
            )),
            FicheRow(concept="", detail_md=(
                "- **L'ECG précède TOUJOURS le dosage de la troponine** : c'est la séquence d'urgence "
                "qui conditionne la stratégie diagnostique et thérapeutique."
            ), kind="a_retenir"),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Sémiologie des 4 urgences cardiovasculaires (PIED)", markdown=(
            "| Élément | SCA | Dissection aortique | Embolie pulmonaire | Péricardite |\n"
            "|---------|-----|---------------------|---------------------|--------------|\n"
            "| Terrain | FDRCV, ATCD coronariens | HTA ancienne, Marfan | Cancer, alitement, OP+tabac, post-op | Contexte viral, fièvre |\n"
            "| Douleur | Rétrosternale, constrictive, > 20 min | Aiguë, déchirante, dos, migratrice | Basithoracique + dyspnée + toux | Augmentée à l'inspiration, calmée par antéflexion |\n"
            "| Examen | Normal (sauf complications) | Asymétrie tensionnelle (> 20 mmHg), abolition pouls, souffle IA | Tachycardie, signes IVD, signes TVP (2/3) | Frottement péricardique fugace |\n"
            "| ECG | Sus/sous-décalage ST, T négatives, Q | Normal ou SCA | S1Q3, BBD, T négatives V1-V3 | Sus-décalage ST concave diffus, sous-décalage PQ, microvoltage |\n"
            "| Radio thorax | Normale | Élargissement médiastin, double contour | Normale ou atélectasies en bandes | Élargissement silhouette cardiaque |\n"
            "| Biologie | Troponines | D-dimères élevés | D-dimères (selon proba) | Troponines, syndrome inflammatoire |\n"
            "| Imagerie | Coronarographie | Angioscanner ± ETT/ETO | Angioscanner | ETT (épanchement) |"
        )),
        TableauSynthese(titre="Douleur ischémique versus non ischémique : caractéristiques cliniques", markdown=(
            "| Critère | Douleur ischémique | Douleur non ischémique |\n"
            "|---------|---------------------|--------------------------|\n"
            "| Caractéristiques | Constriction, pesanteur, brûlure | Acérée, en coup de poignard, augmentée par la respiration |\n"
            "| Siège | Rétrosternal, médiothoracique, irradiation cou/épaules/avant-bras/tête, sueurs, nausées | Sous-mammaire gauche, hémithorax gauche, punctiforme (montré du doigt), dorsale (dissection) |\n"
            "| Facteurs déclenchants | Effort, stress, énervement, temps froid | Après l'effort, soulagement par l'effort, provoquée par un mouvement |\n"
            "| Durée | Minutes | Secondes ou heures (en l'absence d'élévation des troponines) |"
        )),
        TableauSynthese(titre="Score clinique d'évocation d'une dissection aortique", markdown=(
            "| Critère (1 point chacun) | Détail |\n"
            "|---------------------------|--------|\n"
            "| Terrain évocateur | Marfan, ATCD familial de maladie aortique, anévrisme/valvulopathie aortique connus, ATCD chirurgie aortique |\n"
            "| Douleur thoracique évocatrice | Thoracique, dorsale ou abdominale, début brutal, intense, type déchirement |\n"
            "| Signes évocateurs à l'examen | Abolition d'un pouls, asymétrie tensionnelle, déficit neurologique focal, IA, hypotension/choc |\n"
            "| Interprétation | Faible : 0-1 / Forte : 2-3 |"
        )),
        TableauSynthese(titre="Algorithme troponines ultrasensibles SCA non ST+", markdown=(
            "| Tn-us H0 | Évolution H1-H2 | Conclusion |\n"
            "|----------|-----------------|-------------|\n"
            "| Très faible/faible | Pas d'augmentation significative | Diagnostic différentiel ou SCA bas risque (surveillance Usic) |\n"
            "| Élevée | — | **SCA non ST+ haut risque** |\n"
            "| Faible | Augmentation significative | **SCA non ST+ haut risque** |"
        )),
        TableauSynthese(titre="Classification de la dissection aortique", markdown=(
            "| Classification | Stanford | De Bakey | Localisation | Prise en charge |\n"
            "|----------------|----------|----------|--------------|------------------|\n"
            "| Type A | A | I (asc + desc) ou II (asc isolée) | Aorte ascendante | **Chirurgie urgente** |\n"
            "| Type B | B | III | Aorte descendante | Médicale (sauf complication périphérique) |"
        )),
        TableauSynthese(titre="Stratégie diagnostique de l'angor stable selon probabilité clinique", markdown=(
            "| Probabilité clinique | Examen recommandé |\n"
            "|----------------------|--------------------|\n"
            "| Très faible (< 5 %) | Aucun examen |\n"
            "| Faible (5-15 %) | Scanner coronarien d'emblée ou réévaluation |\n"
            "| Modérée (15-50 %) | Scanner coronarien ou imagerie fonctionnelle |\n"
            "| Élevée (50-85 %) | Imagerie fonctionnelle |\n"
            "| Très élevée (> 85 %) | Coronarographie |"
        )),
        TableauSynthese(titre="Diagnostics différentiels : urgences cardiaques et 4 P extracardiaques", markdown=(
            "| Catégorie | Étiologies | Mnémotechnique |\n"
            "|-----------|------------|------------------|\n"
            "| Urgences cardiaques | Péricardite, Infarctus, Embolie pulmonaire, Dissection | **PIED** |\n"
            "| Urgences extracardiaques | Pneumonie, Pleurésie, Pneumothorax, Pancréatite | **4 P** |\n"
            "| Autres urgences non cardiaques | Ulcère gastroduodénal compliqué, Cholécystite, Douleurs radiculaires | — |\n"
            "| Causes non urgentes | RGO, spasme œsophagien, Tietze, douleurs psychogènes | — |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Polypnée (détresse respiratoire) | > 30/min | Fréquence respiratoire |\n"
        "| Bradypnée (détresse respiratoire) | < 10/min | Ou pauses respiratoires |\n"
        "| Désaturation | SpO₂ < 90 % | Détresse respiratoire |\n"
        "| ECG : dérivations à enregistrer | 12 dérivations + V3R, V4R, V7, V8, V9 | Postérieures et droites |\n"
        "| SCA : durée seuil d'évocation d'infarctus | > 20 min | Douleur prolongée |\n"
        "| SCA : dyspnée associée | 10 % des cas | Symptôme associé |\n"
        "| Clinique + ECG : diagnostic de SCA | > 90 % des cas | Performance diagnostique |\n"
        "| Dissection : asymétrie tensionnelle | > 20 mmHg | Entre les deux bras |\n"
        "| Dissection : score de probabilité clinique | 0 à 3 | Faible 0-1, forte 2-3 |\n"
        "| EP : hypotension (haut risque) | PAS < 90 mmHg ou ↓ PAS ≥ 40 mmHg | > 15 min, sans rythme/hypovolémie/sepsis |\n"
        "| EP : seuil D-dimères | > 500 µg/L | Ou > 10 × âge si > 50 ans (ESC 2019) |\n"
        "| EP : signes de TVP absents | 1/3 des cas | Examen clinique |\n"
        "| Tamponnade : PAS | < 90 mmHg | Signes de choc |\n"
        "| Tamponnade : pouls paradoxal | PAS inspi < PAS expi de 10 mmHg | Diagnostic |\n"
        "| Angor stable : effet de la trinitrine | 1 à 3 minutes | Cession typique de la douleur |\n"
        "| SCC : très faible probabilité | < 5 % | Pas d'examen |\n"
        "| SCC : probabilité faible | 5-15 % | Scanner coronarien ou réévaluation |\n"
        "| SCC : probabilité modérée | 15-50 % | Scanner ou imagerie fonctionnelle |\n"
        "| SCC : probabilité élevée | 50-85 % | Imagerie fonctionnelle |\n"
        "| SCC : probabilité très élevée | > 85 % | Coronarographie |\n"
        "| Score SCC : points douleur | 0 à 3 | Typique, effort, repos/trinitrine < 5 min |\n"
        "| Score SCC : points dyspnée prédominante | 2 | Si symptôme principal |\n"
        "| Score SCC : nombre FDRCV | 0 à 5 | ATCD familial, HTA, tabac, dyslipidémie, diabète |\n"
        "| Spasme œsophagien : sensibilité aux dérivés nitrés | Calmée | Piège diagnostique |\n"
    ))

    points_cles = [
        "1ʳᵉ étape devant douleur thoracique : **détresse vitale** (choc, respiratoire, neuro) avant étiologie",
        "**PIED** = 4 urgences cardio : **P**éricardite, **I**nfarctus, **E**mbolie pulmonaire, **D**issection aortique",
        "Examens systématiques : **ECG 12D + V3R/V4R/V7-V9**, RP, **troponines ultrasensibles**",
        "Transfert **médicalisé via le 15** obligatoire ; faute grave de ne pas y recourir",
        "**SCA ST+** : douleur > **20 min** ; reperfusion urgente sans attendre Tn ; **BBG = équivalent ST+**",
        "ECG et Tn normaux **n'éliminent PAS** un SCA (angor instable) ; penser V7-V9 (circonflexe)",
        "Tn-us **SCA non ST+** : 2 dosages **H0/H1-H2** ; haut risque si élevée ou hausse significative",
        "**Dissection** : déchirante, asymétrie tensionnelle > **20 mmHg** ; type A = **chirurgie urgente**",
        "**EP** : triade douleur + dyspnée + RP normale ; D-dimères > **500 µg/L** ou **10 × âge** si > 50 ans",
        "**Inacceptable** : doser la troponine **avant l'ECG** — l'ECG conditionne la stratégie",
    ]

    fiche_eclair_md = (
        "**Démarche** : 1) détresse vitale. 2) **PIED**. ECG 12D + V3R/V4R/V7-V9, RP, Tn-us. Transfert via 15.\n\n"
        "**SCA** : rétrosternale constrictive > 20 min. ECG d'abord (BBG = équivalent ST+). Tn-us H0/H1-H2 si non ST+. ST+ : reperfusion sans attendre Tn. ECG + Tn normaux n'éliminent PAS angor instable.\n\n"
        "**Dissection** : HTA, Marfan. Déchirante migratrice dorsale. Asymétrie tensionnelle > 20 mmHg. Score 0-3. Élargissement médiastinal. Angioscanner. Type A = chirurgie urgente, type B = médicale.\n\n"
        "**EP** : cancer, alitement. Triade douleur + dyspnée + RP normale. ECG : S1Q3, BBD. Haut risque = PAS < 90 ou choc. Wells/Genève. D-dimères > 500 µg/L ou 10 × âge.\n\n"
        "**Péricardite** : virale. Douleur ↑ inspi, ↓ antéflexion. Frottement fugace. ECG : ST concave diffus, sous-PQ, microvoltage. ETT + Tn.\n\n"
        "**Tamponnade** : urgence vitale. Signes droits + choc + pouls paradoxal (↓ 10 mmHg inspi). RP « carafe ». ETT collapsus cavités droites.\n\n"
        "**Myopéricardite** : Tn élevées prolongées. IRM : rehaussement tardif sous-épicardique non systématisé.\n\n"
        "**Chroniques** : angor stable (trinitrine 1-3 min), RA serré, fonctionnel (anémie, FA, hyperthyroïdie), CMH, HTAP. SCC : < 5 % rien, > 85 % coro.\n\n"
        "**4 P extracardiaques** : Pneumonie, Pleurésie, Pneumothorax, Pancréatite. Spasme œsophagien calmé par trinitrine = piège.\n\n"
        "**Inacceptable** : doser Tn avant ECG."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 230 - Douleur thoracique aiguë",
        annee="2025-2026",
        item="Item 230",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 230",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-230_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

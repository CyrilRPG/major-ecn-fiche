"""Génère la fiche de l'Item 232 - Fibrillation atriale (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Définition, épidémiologie et physiopathologie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition"),
            PlanSousPartie(lettre="B", titre="Épidémiologie"),
            PlanSousPartie(lettre="C", titre="Physiopathologie et mécanismes"),
        ]),
        PlanPartie(numero="II", titre="Classification et terminologie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Classification en « P »"),
            PlanSousPartie(lettre="B", titre="Formes particulières"),
        ]),
        PlanPartie(numero="III", titre="Diagnostic", sous_parties=[
            PlanSousPartie(lettre="A", titre="Circonstances de découverte et clinique"),
            PlanSousPartie(lettre="B", titre="ECG et examens complémentaires"),
            PlanSousPartie(lettre="C", titre="Diagnostic étiologique"),
        ]),
        PlanPartie(numero="IV", titre="Évaluation et prévention du risque thromboembolique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Autour de la cardioversion"),
            PlanSousPartie(lettre="B", titre="Score CHA₂DS₂-VA et traitement chronique"),
            PlanSousPartie(lettre="C", titre="Fermeture de l'auricule gauche"),
        ]),
        PlanPartie(numero="V", titre="Traitement", sous_parties=[
            PlanSousPartie(lettre="A", titre="Correction des facteurs de risque"),
            PlanSousPartie(lettre="B", titre="Traitement de l'accès de FA"),
            PlanSousPartie(lettre="C", titre="Traitement d'entretien"),
            PlanSousPartie(lettre="D", titre="Éducation du patient"),
        ]),
        PlanPartie(numero="VI", titre="Différents tableaux cliniques", sous_parties=[
            PlanSousPartie(lettre="A", titre="FA avec cœur normal"),
            PlanSousPartie(lettre="B", titre="FA et insuffisance cardiaque"),
            PlanSousPartie(lettre="C", titre="FA valvulaire post-rhumatismale"),
            PlanSousPartie(lettre="D", titre="Embolie révélatrice et maladie de l'oreillette"),
        ]),
        PlanPartie(numero="VII", titre="Dépistage", sous_parties=[
            PlanSousPartie(lettre="A", titre="Indications du dépistage"),
        ]),
    ]

    # ── PARTIE I : DÉFINITION, ÉPIDÉMIOLOGIE ET PHYSIOPATHOLOGIE ──
    partie_i = Partie(numero="I", titre="Définition, épidémiologie et physiopathologie", sous_parties=[
        SousPartie(lettre="A", titre="Définition", rows=[
            FicheRow(concept="◆ Définition de la FA", detail_md=(
                "- **Fibrillation atriale (FA)** = tachycardie irrégulière d'origine supraventriculaire\n"
                "- Due à une activité électrique rapide (**400-600/min**) et anarchique des oreillettes\n"
                "- Conséquence : contractions désynchronisées des 2 massifs atriaux avec "
                "perte de leur efficacité hémodynamique\n"
                "- Anciennement appelée fibrillation « auriculaire »"
            )),
            FicheRow(concept="Réponse ventriculaire", detail_md=(
                "- La réponse ventriculaire est sous la dépendance du **nœud atrioventriculaire (AV)**\n"
                "- Sa capacité de filtration varie selon :\n"
                "  - l'état du système nerveux autonome\n"
                "  - l'imprégnation en médicaments bradycardisants"
            )),
            FicheRow(concept="◆ Diagnostic « clinique » de FA", detail_md=(
                "- Diagnostic retenu devant un ECG (monopiste ou 12 dérivations) présentant :\n"
                "  - activation atriale anarchique **sans onde P individualisable**\n"
                "- Plus de durée minimale de 30 secondes d'enregistrement requise pour diagnostiquer\n"
                "- ⚠ Le diagnostic par **photopléthysmographie** reste non valide"
            )),
            FicheRow(concept="", detail_md=(
                "- La FA = tachycardie irrégulière supraventriculaire sans onde P, par activité atriale "
                "anarchique (400-600/min) filtrée par le nœud AV.\n"
                "- Diagnostic = **ECG documenté** (plus de seuil de 30 s)."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Épidémiologie", rows=[
            FicheRow(concept="◆ Prévalence", detail_md=(
                "- **Trouble du rythme le plus fréquent**\n"
                "- En France : entre **500 000 et 750 000 patients** concernés\n"
                "- Prévalence croît avec l'âge :\n"
                "  - rare avant 50 ans\n"
                "  - **10 % de la population après 80 ans**"
            )),
            FicheRow(concept="◆ Obésité et FA", detail_md=(
                "- Lien fort avec l'obésité :\n"
                "  - **+30 % de fréquence par tranche supplémentaire de 5 kg/m² d'IMC**"
            )),
            FicheRow(concept="◆ FA et AVC", detail_md=(
                "- La FA est responsable de **20-25 % de tous les AVC**, par embolie cérébrale"
            )),
            FicheRow(concept="Associations rythmologiques", detail_md=(
                "- La FA peut faire suite ou s'associer à un flutter atrial typique ou atypique"
            )),
        ]),
        SousPartie(lettre="C", titre="Physiopathologie et mécanismes", rows=[
            FicheRow(concept="Aspects électriques", detail_md=(
                "- Le **nœud AV** filtre l'activité atriale anarchique rapide\n"
                "- → tachycardie irrégulière au repos qui s'accélère à l'effort"
            )),
            FicheRow(concept="◆ Conséquences hémodynamiques", detail_md=(
                "- Perte de la **systole atriale**\n"
                "- Perte de l'adaptation physiologique de la FC à l'effort\n"
                "- Risque d'**insuffisance cardiaque**\n"
                "- **Risque thromboembolique** par stase au niveau de l'auricule gauche "
                "et embolie dans la circulation systémique"
            )),
            FicheRow(concept="◆ Évolution - Cercle vicieux", detail_md=(
                "- Fibrose des oreillettes et, plus tardivement, du tissu de conduction "
                "(nœud sinusal et nœud AV)\n"
                "- **Dilatation atriale** (remodelage atrial) qui pérennise la fibrillation\n"
                "- → cercle vicieux d'autoaggravation"
            )),
            FicheRow(concept="", detail_md=(
                "- Conséquences hémodynamiques = perte systole atriale + perte adaptation FC effort + "
                "**risque IC** + **risque thromboembolique** (stase auricule G).\n"
                "- Évolution = fibrose + remodelage = cercle vicieux d'autoaggravation."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE II : CLASSIFICATION ET TERMINOLOGIE ──
    partie_ii = Partie(numero="II", titre="Classification et terminologie", sous_parties=[
        SousPartie(lettre="A", titre="Classification en « P »", rows=[
            FicheRow(concept="◆ Classification P-P-P-P", detail_md=(
                "- **Paroxystique** : retour spontané ou par cardioversion en rythme sinusal "
                "en moins de **7 jours**\n"
                "- **Persistante** : retour spontané ou par cardioversion au-delà de **7 jours**\n"
                "- **Permanente** : échec de cardioversion et/ou décision d'une stratégie de "
                "contrôle de la fréquence (pas de volonté de restaurer le rythme sinusal)\n"
                "- **Premier épisode** : la FA n'est pas encore classable"
            )),
            FicheRow(concept="Cardioversion - Définition", detail_md=(
                "- **Cardioversion** ou réduction de la FA = actions médicales qui "
                "restaurent le rythme sinusal\n"
                "- Modalités : médicament ou choc électrique"
            )),
            FicheRow(concept="Comparatif des formes de FA", detail_md=(
                "| Forme | Durée | Caractéristique |\n"
                "|-------|-------|----------------|\n"
                "| Paroxystique | < 7 jours | Retour sinusal spontané ou cardioversion |\n"
                "| Persistante | > 7 jours | Retour sinusal spontané ou cardioversion |\n"
                "| Permanente | - | Échec de cardioversion ou pas de volonté de réduire |\n"
                "| Premier épisode | - | Pas encore classable |"
            )),
        ]),
        SousPartie(lettre="B", titre="Formes particulières", rows=[
            FicheRow(concept="◆ Maladie de l'oreillette", detail_md=(
                "- Aussi appelée **syndrome de tachybradycardie**\n"
                "- Correspond à la coexistence de :\n"
                "  - FA paroxystique\n"
                "  - **dysfonction sinusale**"
            )),
            FicheRow(concept="FA récidivantes vs FA de cause aiguë", detail_md=(
                "- Opposition à connaître :\n"
                "  - **FA récidivantes**\n"
                "  - **FA de cause aiguë** : postopératoire, infarctus, infection pulmonaire, péricardite, etc."
            )),
        ]),
    ])

    # ── PARTIE III : DIAGNOSTIC ──
    partie_iii = Partie(numero="III", titre="Diagnostic", sous_parties=[
        SousPartie(lettre="A", titre="Circonstances de découverte et clinique", rows=[
            FicheRow(concept="◆ Circonstances de découverte", detail_md=(
                "- Découverte fortuite lors d'un examen clinique ou ECG chez patient asymptomatique\n"
                "- Bilan de palpitations permanentes ou intermittentes ou d'un essoufflement récent\n"
                "- Révélée par une complication : **AVC**, poussée d'insuffisance cardiaque, etc."
            )),
            FicheRow(concept="◆ Signes fonctionnels", detail_md=(
                "- Signes parfois absents ou intermittents\n"
                "- Mauvaise corrélation entre réalité de la FA et prise du pouls / palpitations\n"
                "- → **Diagnostic ECG indispensable**\n"
                "- Holter ou autres méthodes de monitorage nécessaires si FA paroxystique\n"
                "- Symptômes usuels :\n"
                "  - palpitations\n"
                "  - dyspnée d'effort\n"
                "  - angor fonctionnel\n"
                "  - asthénie inexpliquée"
            )),
            FicheRow(concept="⚠ Symptômes trompeurs", detail_md=(
                "- Lipothymies\n"
                "- **Chutes inexpliquées chez la personne âgée**\n"
                "- Incapacité à faire un effort\n"
                "- Impression que le cœur « bat trop lentement »\n"
                "- Accès de « faiblesse »\n"
                "- Bouffées de chaleur\n"
                "- Œdèmes des membres inférieurs"
            )),
            FicheRow(concept="◆ Examen clinique - Auscultation", detail_md=(
                "- Bruits du cœur **irréguliers** et rythme plus ou moins rapide"
            )),
            FicheRow(concept="◆ Prise en charge initiale", detail_md=(
                "- Apprécier la tolérance : FC, PA, diurèse, FR, état de conscience\n"
                "- Rechercher d'emblée une complication :\n"
                "  - **OAP** ou signes d'insuffisance cardiaque\n"
                "  - **Embolie artérielle systémique** (examen artériel et neurologique)\n"
                "- Rechercher une cardiopathie sous-jacente\n"
                "- Rechercher des facteurs déclenchants (alcool, fièvre, hyperthyroïdie, etc.)"
            )),
        ]),
        SousPartie(lettre="B", titre="ECG et examens complémentaires", rows=[
            FicheRow(concept="◆ ECG - Critères diagnostiques", detail_md=(
                "- Diagnostic confirmé uniquement sur tracé ECG (ECG, holter ou monitoring) :\n"
                "  - **Absence d'onde P visible**\n"
                "  - QRS le plus souvent irréguliers\n"
                "    - Exceptionnellement réguliers en cas de **BAV complet concomitant**\n"
                "- Aspect usuel à petites mailles : trémulations de la ligne de base, QRS fins\n"
                "  - QRS larges possibles si bloc de branche associé"
            )),
            FicheRow(concept="⚠ FA à grosses mailles", detail_md=(
                "- Aspect particulier de FA à grosses mailles\n"
                "- **Ne pas confondre avec le flutter atrial**\n"
                "- C'est un piège classique de l'ECG"
            )),
            FicheRow(concept="Autres aspects ECG", detail_md=(
                "- QRS lents et réguliers = association FA + **bloc AV complet**\n"
                "- Pauses ou dysfonction sinusale de régularisation = **syndrome tachybradycardie**"
            )),
            FicheRow(concept="◆ Bilan biologique", detail_md=(
                "- Ionogramme sanguin\n"
                "- Créatinine\n"
                "- **TSHus** (thyroid-stimulating hormone ultrasensible)\n"
                "- Numération globulaire"
            )),
            FicheRow(concept="◆ Échocardiographie", detail_md=(
                "- Recherche d'une **cardiopathie sous-jacente**\n"
                "- Examen systématique devant la découverte d'une FA"
            )),
            FicheRow(concept="Diagnostic des FA non documentées", detail_md=(
                "- En cas de suspicion de FA non encore documentée (ex : bilan d'AVC) :\n"
                "  - **Holter prolongé (72 heures)**\n"
                "  - Interrogation du pacemaker ou DAI (défibrillateur automatique implantable) "
                "si le patient en est porteur"
            )),
        ]),
        SousPartie(lettre="C", titre="Diagnostic étiologique", rows=[
            FicheRow(concept="◆ Facteurs déclenchants", detail_md=(
                "- Hypokaliémie\n"
                "- Fièvre\n"
                "- Privation de sommeil\n"
                "- Réaction vagale\n"
                "- Alcool, ivresse ou prise de substances illicites\n"
                "- Électrocution"
            )),
            FicheRow(concept="◆ Facteur de prédisposition principal", detail_md=(
                "- **L'âge est le plus puissant facteur de prédisposition**, incontestablement"
            )),
            FicheRow(concept="◆ Facteurs de prédisposition modifiables", detail_md=(
                "- Obésité\n"
                "- Hyperthyroïdie\n"
                "- Diabète\n"
                "- **HTA**\n"
                "- Tabagisme et consommation excessive d'alcool\n"
                "- Sports de grande endurance (marathon)\n"
                "- **SAOS** (syndrome d'apnées obstructives du sommeil)"
            )),
            FicheRow(concept="◆ Causes par ordre de fréquence décroissante", detail_md=(
                "- **HTA** (souvent avec HVG), notamment chez le sujet âgé\n"
                "- **Valvulopathies mitrales**\n"
                "- Autres causes :\n"
                "  - Maladies respiratoires : SAOS, pneumopathies infectieuses, **EP**, "
                "cœur pulmonaire chronique\n"
                "  - Cardiomyopathies (dilatées, hypertrophiques, restrictives)\n"
                "  - SCA et séquelles d'infarctus\n"
                "  - Hyperthyroïdie (cardiothyréose)\n"
                "  - Péricardites\n"
                "  - Chirurgie cardiaque récente\n"
                "  - Cardiopathies congénitales (communication interatriale)\n"
                "  - Phéochromocytome\n"
                "  - Insuffisance rénale sévère"
            )),
            FicheRow(concept="Formes idiopathiques", detail_md=(
                "- Diagnostic d'élimination\n"
                "- Souvent un substratum génétique\n"
                "- Un antécédent de FA chez un apparenté du 1er degré augmente de **40 %** "
                "la probabilité d'atteinte"
            )),
            FicheRow(concept="◆ Bilan étiologique systématique", detail_md=(
                "- Interrogatoire et examen complet\n"
                "- ECG\n"
                "- Radiographie de thorax\n"
                "- **ETT** (échocardiographie transthoracique)\n"
                "- **TSHus**\n"
                "- Ionogramme sanguin\n"
                "- Fonction rénale\n"
                "- Bilan hépatique\n"
                "- Autres examens sur signe d'appel"
            )),
            FicheRow(concept="⚠ HTA et SAOS sous-diagnostiqués", detail_md=(
                "- Diagnostic d'HTA parfois difficile :\n"
                "  - Recourir à l'automesure tensionnelle ou à la **MAPA** (monitoring ambulatoire)\n"
                "- SAOS souvent méconnu :\n"
                "  - Asthénie chronique liée au SAOS souvent imputée à tort à la FA ou aux médicaments\n"
                "  - Recours à la **polygraphie** encouragé, surtout chez le sujet obèse"
            )),
            FicheRow(concept="", detail_md=(
                "- Bilan étio systématique : **interro + examen + ECG + RxT + ETT + TSHus + iono + créat + BH**.\n"
                "- Ne pas oublier l'**HTA** (MAPA si besoin) et le **SAOS** (polygraphie surtout si obèse).\n"
                "- ATCD familial 1er degré → +40 % de risque."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE IV : RISQUE THROMBOEMBOLIQUE ──
    partie_iv = Partie(numero="IV", titre="Évaluation et prévention du risque thromboembolique", sous_parties=[
        SousPartie(lettre="A", titre="Autour de la cardioversion", rows=[
            FicheRow(concept="◆ Risque autour de la cardioversion", detail_md=(
                "- Tout patient est considéré à risque lors de cardioversion (médicamenteuse ou par "
                "choc électrique) pendant les **4 semaines suivantes** au minimum\n"
                "- Risque imposant d'encadrer la cardioversion par une **anticoagulation efficace** "
                "(héparine ou anticoagulant oral)"
            )),
            FicheRow(concept="★ ◆ Schéma classique d'anticoagulation", detail_md=(
                "- Cardioversion précédée d'au moins **3 semaines d'anticoagulation efficace documentée**\n"
                "- Cardioversion suivie de **4 semaines d'anticoagulation efficace**\n"
                "- Ensuite : évaluation du risque chronique pour décider de la poursuite de "
                "l'anticoagulation orale"
            )),
            FicheRow(concept="★ ◆ Exception : éviter les 3 semaines pré-cardioversion", detail_md=(
                "- Anticoagulation pré-cardioversion peut être évitée si :\n"
                "  - **ETO préalable** montre l'absence de thrombus intra-OG\n"
                "  - OU début de la FA parfaitement datable **< 24 heures** (rarement possible)"
            )),
            FicheRow(concept="⚠ Risque très élevé - ETO préalable", detail_md=(
                "- Lorsque le risque est considéré très élevé :\n"
                "  - Valve mécanique mitrale\n"
                "  - **RM** (rétrécissement mitral)\n"
                "- OU si l'anticoagulation pré-cardioversion est incertaine ou mal documentée\n"
                "- → **ETO préalable** pour vérifier l'absence de thrombus atrial gauche "
                "avant la cardioversion"
            )),
            FicheRow(concept="", detail_md=(
                "- **3 semaines AVANT** la cardioversion + **4 semaines APRÈS** la cardioversion "
                "= anticoagulation efficace obligatoire.\n"
                "- Raccourci possible si ETO normale OU FA < 24 h datée."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Score CHA₂DS₂-VA et traitement chronique", rows=[
            FicheRow(concept="⚠ Score CHA₂DS₂-VA NON APPLICABLE", detail_md=(
                "- Le score CHA₂DS₂-VA **ne s'applique pas** dans ces situations à très haut risque :\n"
                "  - FA chez un patient porteur d'un **RM rhumatismal modéré à sévère**\n"
                "  - FA chez un patient porteur d'une **prothèse valvulaire mécanique**\n"
                "- → Dans ces cas : **AVK obligatoire**\n"
                "- Anticoagulation systématique aussi en cas de :\n"
                "  - Cardiomyopathie hypertrophique\n"
                "  - Amylose cardiaque"
            )),
            FicheRow(concept="★ ◆ Score CHA₂DS₂-VA - Composantes", detail_md=(
                "| Lettre | Critère | Points |\n"
                "|--------|---------|--------|\n"
                "| C | Congestion (IC clinique ± FE altérée) | 1 |\n"
                "| H | HTA (traitée ou non, équilibrée ou non) | 1 |\n"
                "| A2 | Âge ≥ 75 ans | 2 |\n"
                "| D | Diabète (traité ou non, équilibré ou non) | 1 |\n"
                "| S2 | Stroke (AVC) ou embolie artérielle | 2 |\n"
                "| V | Atteinte vasculaire (coronarienne, AOMI, athérome troncs cérébraux) | 1 |\n"
                "| A | Âge 65-74 ans | 1 |\n"
                "| **Total** | | **0 à 8** |"
            )),
            FicheRow(concept="◆ Risque thromboembolique annuel", detail_md=(
                "- Le risque annuel thromboembolique varie de façon exponentielle :\n"
                "  - **1 à 18 %** pour les scores de 0 à 8\n"
                "  - Chaque palier augmente globalement le risque annuel de 2 %"
            )),
            FicheRow(concept="Facteurs non pris en compte", detail_md=(
                "- D'autres facteurs non pris en compte dans le score CHA₂DS₂-VA :\n"
                "  - SAOS\n"
                "  - Insuffisance rénale sévère"
            )),
            FicheRow(concept="★ ◆ Indications d'anticoagulation au long cours", detail_md=(
                "| Score CHA₂DS₂-VA | Conduite |\n"
                "|------------------|----------|\n"
                "| Score nul (0) | **Pas d'anticoagulant** |\n"
                "| Score = 1 (risque intermédiaire) | Anticoagulants conseillés, discussion au cas par cas |\n"
                "| Score > 1 | Anticoagulants indiqués de façon indiscutable |"
            )),
            FicheRow(concept="★ ◆ Type d'anticoagulant", detail_md=(
                "- **AOD** (anticoagulants oraux directs) à favoriser par rapport aux AVK\n"
                "- Exception : FA avec prothèse mécanique ou RM modéré à sévère → **AVK obligatoire**"
            )),
            FicheRow(concept="⚠ Type de FA et indication d'anticoagulation", detail_md=(
                "- Le type d'épisode (paroxystique, persistant, permanent) **ne doit pas** "
                "intervenir dans la décision de prise en charge anticoagulante"
            )),
            FicheRow(concept="", detail_md=(
                "- **CHA₂DS₂-VA** = C(1) + H(1) + A2(âge ≥ 75 : 2) + D(1) + S2(AVC : 2) + V(1) + A(65-74 : 1) "
                "= 0 à 8.\n"
                "- Score 0 → pas d'anticoag ; Score = 1 → discussion ; Score > 1 → anticoag indiscutable.\n"
                "- **AOD à privilégier** sauf RM modéré-sévère ou prothèse mécanique → **AVK obligatoire**."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Fermeture de l'auricule gauche", rows=[
            FicheRow(concept="◆ Principe et rationnel", detail_md=(
                "- **Fermeture de l'auricule gauche** par dispositif inséré par voie veineuse percutanée\n"
                "- Par cathétérisme transseptal (à travers la cloison atriale)\n"
                "- Rationnel : les thrombi se forment préférentiellement au niveau de l'auricule"
            )),
            FicheRow(concept="★ ◆ Indications strictes", detail_md=(
                "- Patient avec FA sans prothèse valvulaire mécanique ni RM modéré à sévère\n"
                "- ET haut risque thromboembolique : **CHA₂DS₂-VA ≥ 2**\n"
                "- ET **contre-indication formelle et permanente aux anticoagulants**\n"
                "  - Validée par un comité pluridisciplinaire"
            )),
            FicheRow(concept="Fermeture chirurgicale", detail_md=(
                "- Lors d'une chirurgie cardiaque chez un patient atteint de FA :\n"
                "  - Fermeture chirurgicale de l'auricule désormais indiquée\n"
                "- ⚠ **Ne permet pas de s'affranchir de l'anticoagulation** dans ce cas"
            )),
        ]),
    ])

    # ── PARTIE V : TRAITEMENT ──
    partie_v = Partie(numero="V", titre="Traitement", sous_parties=[
        SousPartie(lettre="A", titre="Correction des facteurs de risque", rows=[
            FicheRow(concept="◆ Prise en charge obligatoire des comorbidités", detail_md=(
                "- Obligatoire et fondamentale chez tous les patients\n"
                "- Corriger l'obésité et le surpoids :\n"
                "  - Encourager une **perte de poids de 10 %**\n"
                "  - Et/ou viser un **IMC < 27 kg/m²** chez le sujet obèse\n"
                "- Programme d'activité physique adaptée\n"
                "- Limiter la consommation d'alcool\n"
                "- Sevrer du tabagisme\n"
                "- Traiter l'HTA : viser une **PAS < 130 mmHg**\n"
                "- Adapter les traitements de l'insuffisance cardiaque\n"
                "- Discuter un traitement du SAOS\n"
                "  - ⚠ Le dépistage par questionnaire n'est plus indiqué"
            )),
        ]),
        SousPartie(lettre="B", titre="Traitement de l'accès de FA", rows=[
            FicheRow(concept="◆ Prévention thromboembolique - Obligatoire", detail_md=(
                "- **Obligatoire** quel que soit le contexte si cardioversion envisagée\n"
                "- Si pas d'anticoagulant oral efficace en cours : AOD d'emblée "
                "en l'absence de contre-indication"
            )),
            FicheRow(concept="⚠ Cardioversion immédiate - Urgence vitale", detail_md=(
                "- **Cardioversion immédiate par choc électrique** en cas d'urgence vitale (état de choc)\n"
                "- Situation très rare : FA très rapide ne répondant pas aux traitements freinateurs"
            )),
            FicheRow(concept="◆ Cardioversion différée (cas habituel)", detail_md=(
                "- Différée après **3 semaines d'anticoagulation orale efficace**\n"
                "- Modalités possibles :\n"
                "  - Choc électrique sous anesthésie générale\n"
                "  - Médicaments antiarythmiques : **amiodarone**, **flécaïnide**\n"
                "  - Ou combinaison des deux\n"
                "- Possibilité d'éviter ce délai de 3 semaines sous réserve de :\n"
                "  - **ETO normale** (pas de thrombus atrial gauche)\n"
                "  - OU FA datée précisément à moins de 24 heures (rare)"
            )),
            FicheRow(concept="◆ Contrôle de la fréquence cardiaque", detail_md=(
                "- En attente de cardioversion ou en cas d'échec :\n"
                "  - Freinateurs nodaux : bêtabloquant, vérapamil ou diltiazem, digoxine\n"
                "- En urgence chez l'insuffisant cardiaque :\n"
                "  - **Digoxine IV** (en cas de kaliémie normale)"
            )),
            FicheRow(concept="◆ Anticoagulation post-cardioversion", detail_md=(
                "- Anticoagulants oraux poursuivis **4 semaines minimum** après cardioversion "
                "(médicamenteuse ou électrique)"
            )),
            FicheRow(concept="⚠ Premier épisode - Pas d'antiarythmique chronique", detail_md=(
                "- S'il s'agit d'un premier épisode :\n"
                "  - **Pas de traitement antiarythmique chronique** pour prévenir une éventuelle récidive"
            )),
        ]),
        SousPartie(lettre="C", titre="Traitement d'entretien", rows=[
            FicheRow(concept="Anticoagulants oraux disponibles", detail_md=(
                "- **AVK** (antivitamines K)\n"
                "- Inhibiteurs de la thrombine : **dabigatran**\n"
                "- Inhibiteurs du facteur X activé : **rivaroxaban**, **apixaban**"
            )),
            FicheRow(concept="◆ Surveillance et antidotes", detail_md=(
                "- **AVK** : efficacité surveillée par l'**INR** ; mode d'action via les "
                "facteurs vitamine K-dépendants (II, VII, IX et X)\n"
                "- **AOD** : efficacité surveillée cliniquement\n"
                "- **Idarucizumab** = antidote spécifique du dabigatran"
            )),
            FicheRow(concept="◆ AVK courants", detail_md=(
                "- Warfarine\n"
                "- Acénocoumarol\n"
                "- **Fluindione** : utilisable uniquement en **2e intention** "
                "(risque d'atteinte rénale immunoallergique)"
            )),
            FicheRow(concept="⚠ FA valvulaire - INR cible", detail_md=(
                "- Si prothèse valvulaire mécanique ou RM modéré à sévère :\n"
                "  - AVK seules recommandées\n"
                "  - **INR cible 2,5 (entre 2 et 3)**\n"
                "- Exception : valve mécanique mitrale ou valve à disque :\n"
                "  - **INR cible 3-4,5**"
            )),
            FicheRow(concept="Autres situations - AOD recommandés", detail_md=(
                "- Dans les autres situations : AOD recommandés en fonction du score CHA₂DS₂-VA\n"
                "- À privilégier par rapport aux AVK"
            )),
            FicheRow(concept="◆ Stratégies de prise en charge - 2 options", detail_md=(
                "- **Contrôle de fréquence** par freinateurs nodaux :\n"
                "  - Bêtabloquants, inhibiteurs calciques bradycardisants, digitaliques\n"
                "  - Objectif : **FC < 110 bpm** pour un effort modeste (marche normale)\n"
                "  - Vérification par holter\n"
                "- **Contrôle du rythme** (prévention des rechutes) par antiarythmique :\n"
                "  - Amiodarone, flécaïnide, propafénone\n"
                "  - ⚠ Chez coronariens et/ou insuffisants cardiaques : "
                "**seule l'amiodarone est utilisable**"
            )),
            FicheRow(concept="⚠ Précautions chez le sujet âgé", detail_md=(
                "- Contraintes du traitement très nombreuses chez les sujets âgés :\n"
                "  - Utilisation difficile des AVK\n"
                "  - Utilisation difficile des freinateurs nodaux\n"
                "  - Utilisation difficile des antiarythmiques\n"
                "- AOD à doses réduites souvent nécessaire **après 80 ans**\n"
                "- À l'inverse : les patients les plus âgés sont aussi les plus exposés "
                "au risque thromboembolique"
            )),
            FicheRow(concept="⚠ Contre-indications chez l'insuffisant cardiaque", detail_md=(
                "- Chez l'insuffisant cardiaque, sont interdits :\n"
                "  - **Inhibiteurs calciques bradycardisants** (vérapamil, diltiazem)\n"
                "  - **Flécaïnide**"
            )),
            FicheRow(concept="◆ Stimulation cardiaque définitive", detail_md=(
                "- Indications dans la maladie de l'oreillette = cliniques :\n"
                "  - Pauses sinusales symptomatiques (en règle **> 3 secondes**)\n"
                "  - OU bradycardie sinusale symptomatique et non iatrogène "
                "(en pratique **< 50 bpm**)"
            )),
            FicheRow(concept="◆ Ablation par cathéter - Isolation des veines pulmonaires", detail_md=(
                "- Pour les patients atteints de FA paroxystique :\n"
                "  - **Ablation par cathéter** par voie percutanée\n"
                "  - = isolation électrique des veines pulmonaires\n"
                "  - **Recommandée en 1re ligne**, équivalent à un traitement par antiarythmique\n"
                "  - Selon évaluation et préférences du patient\n"
                "- Stratégie de contrôle du rythme\n"
                "- Supérieur aux médicaments pour maintenir le rythme sinusal sur le long terme\n"
                "- Aussi recommandée si suspicion de **tachycardiomyopathie** "
                "(altération de la FEVG induite par la FA)\n"
                "- À considérer chez patients sélectionnés avec IC à FE altérée"
            )),
        ]),
        SousPartie(lettre="D", titre="Éducation du patient", rows=[
            FicheRow(concept="◆ Éducation vis-à-vis des anticoagulants oraux", detail_md=(
                "- **AVK** :\n"
                "  - Précautions alimentaires\n"
                "  - Fréquence du suivi de l'INR et valeur des cibles\n"
                "- **AVK et AOD** :\n"
                "  - Interactions médicamenteuses\n"
                "  - Prévention et signes d'alarme des hémorragies\n"
                "  - Carnet\n"
                "  - Contraception en raison des effets tératogènes\n"
                "- **AOD** :\n"
                "  - Suivi de la fonction rénale **au moins 1 fois/an**"
            )),
            FicheRow(concept="Éducation vis-à-vis de la cause", detail_md=(
                "- **HTA** le plus souvent (avec surpoids et/ou syndrome métabolique)"
            )),
            FicheRow(concept="◆ Information sur le pronostic", detail_md=(
                "- **Pas de risque de mort subite** (rassurer)\n"
                "- **Risque cérébral** (embolique) à connaître"
            )),
            FicheRow(concept="⚠ Effets indésirables de l'amiodarone", detail_md=(
                "- Thyroïde (dysthyroïdies)\n"
                "- Photosensibilisation\n"
                "- Dépôts cornéens\n"
                "- Etc."
            )),
        ]),
    ])

    # ── PARTIE VI : TABLEAUX CLINIQUES ──
    partie_vi = Partie(numero="VI", titre="Différents tableaux cliniques", sous_parties=[
        SousPartie(lettre="A", titre="FA avec cœur normal", rows=[
            FicheRow(concept="◆ Présentation typique", detail_md=(
                "- Quinquagénaire se plaignant de palpitations\n"
                "- Peut s'associer à un angor fonctionnel ou une dyspnée d'effort\n"
                "- Documentation parfois difficile malgré le holter\n"
                "- Utilité des enregistrements monopistes par outils connectés "
                "(montre, applications, etc.)"
            )),
            FicheRow(concept="Bilan et traitement", detail_md=(
                "- Échocardiographie normale\n"
                "- Toujours exclure une HTA ou un SAOS\n"
                "- Risque embolique très faible : pas d'anticoagulants au long cours si **CHA₂DS₂-VA nul**\n"
                "- Antiarythmique pour maintenir le rythme sinusal :\n"
                "  - **Flécaïnide en 1re intention**\n"
                "  - Ablation envisageable après information éclairée\n"
                "- Évolution : FA paroxystique → FA persistante en quelques mois ou années"
            )),
        ]),
        SousPartie(lettre="B", titre="FA et insuffisance cardiaque", rows=[
            FicheRow(concept="◆ Terrain", detail_md=(
                "- Patient avec cardiopathie ischémique ou cardiomyopathie dilatée à coronaires saines\n"
                "- Ou cardiopathie hypertensive, hypertrophique, valvulaire\n"
                "- Présentation : **OAP** ou décompensation cardiaque\n"
                "- Difficile d'affirmer si la FA est cause ou conséquence de la décompensation\n"
                "- FA souvent persistante"
            )),
            FicheRow(concept="◆ Prise en charge", detail_md=(
                "- Cardioversion différée le temps de l'anticoagulation efficace\n"
                "- Contrôle de fréquence souvent nécessaire dans l'attente\n"
                "- Maintien du rythme sinusal par **amiodarone**\n"
                "- Ablation envisageable\n"
                "- En cas d'échec : FA respectée avec contrôle de fréquence par bêtabloquants\n"
                "- Risque embolique élevé → anticoagulants oraux avant cardioversion puis "
                "**au long cours dans tous les cas**"
            )),
        ]),
        SousPartie(lettre="C", titre="FA valvulaire post-rhumatismale", rows=[
            FicheRow(concept="◆ Présentation typique", detail_md=(
                "- FA sur **prothèse mécanique valvulaire** (mitrale le plus souvent)\n"
                "- S'assurer de l'absence de thrombose de valve\n"
                "- Stratégie habituelle : contrôle de fréquence\n"
                "  - Maintien du rythme sinusal difficile en raison de la dilatation atriale"
            )),
            FicheRow(concept="⚠ Anticoagulation", detail_md=(
                "- Risque embolique élevé\n"
                "- → **AVK au long cours dans tous les cas** (et obligatoirement)"
            )),
        ]),
        SousPartie(lettre="D", titre="Embolie révélatrice et maladie de l'oreillette", rows=[
            FicheRow(concept="◆ Embolie artérielle systémique révélatrice", detail_md=(
                "- FA méconnue chez une femme âgée\n"
                "- Autres facteurs de risque embolique : HTA mal équilibrée, diabète\n"
                "- Embolie brutale, souvent **sylvienne superficielle gauche**\n"
                "- Infarctus cérébral révélateur de la FA\n"
                "- Imagerie cérébrale obligatoire"
            )),
            FicheRow(concept="⚠ Prise en charge en aigu de l'AVC", detail_md=(
                "- **AVK et héparines non utilisables en aigu** :\n"
                "  - Risque de transformation hémorragique\n"
                "- Anticoagulation au long cours impérative à la sortie de l'hôpital\n"
                "- Prise en charge en **UNV** (unité d'urgence neurovasculaire)\n"
                "- Discussion de thrombolyse ou thromboaspiration"
            )),
            FicheRow(concept="◆ Maladie de l'oreillette", detail_md=(
                "- Association à documenter :\n"
                "  - FA paroxystique rapide alternant avec épisodes de bradycardie sinusale\n"
                "- Symptômes : asymptomatique, lipothymies, syncopes\n"
                "- Terrain : sujet âgé\n"
                "- ⚠ **Emploi périlleux des médicaments bradycardisants** :\n"
                "  - Risque d'aggravation de la dysfonction sinusale\n"
                "- → Recours fréquent à la mise en place d'un **stimulateur cardiaque définitif**\n"
                "- En cas de pause réductionnelle symptomatique : "
                "ablation des veines pulmonaires à considérer"
            )),
            FicheRow(concept="", detail_md=(
                "- **Embolie cérébrale révélant la FA** : femme âgée hypertendue, AVC sylvien G.\n"
                "- En aigu : **pas d'AVK ni héparines** (transformation hémorragique). UNV + thrombolyse.\n"
                "- **Maladie de l'oreillette** = FA paroxystique + dysfonction sinusale → "
                "souvent **pacemaker** indispensable."
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE VII : DÉPISTAGE ──
    partie_vii = Partie(numero="VII", titre="Dépistage", sous_parties=[
        SousPartie(lettre="A", titre="Indications du dépistage", rows=[
            FicheRow(concept="◆ Dépistage routinier", detail_md=(
                "- De manière routinière lors d'un contact médical :\n"
                "  - Patient d'**âge ≥ 65 ans**\n"
                "  - OU patient à risque"
            )),
            FicheRow(concept="◆ Dépistage organisé", detail_md=(
                "- De manière organisée :\n"
                "  - Patient d'**âge ≥ 75 ans**\n"
                "  - OU ≥ 65 ans à risque thromboembolique"
            )),
            FicheRow(concept="◆ Dépistage par monitoring prolongé", detail_md=(
                "- De manière systématique par **monitoring prolongé** :\n"
                "  - Dans le bilan d'**embolie cryptogénique** (notamment AVC sans cause retrouvée)"
            )),
            FicheRow(concept="", detail_md=(
                "- Dépistage routinier ≥ 65 ans ou à risque.\n"
                "- Dépistage organisé ≥ 75 ans ou ≥ 65 ans à risque.\n"
                "- **Monitoring prolongé** systématique si AVC cryptogénique."
            ), kind="mnemo"),
        ]),
    ])

    tableaux = [
        TableauSynthese(titre="Synthèse - Classification P-P-P-P", markdown=(
            "| Forme | Durée | Caractéristique principale | Stratégie usuelle |\n"
            "|-------|-------|---------------------------|-------------------|\n"
            "| Paroxystique | < 7 jours | Retour sinusal spontané ou cardioversion | Contrôle rythme ± fréquence ; ablation possible |\n"
            "| Persistante | > 7 jours | Retour sinusal spontané ou cardioversion | Contrôle rythme : cardioversion électrique/médicamenteuse |\n"
            "| Permanente | - | Échec de cardioversion ou pas de volonté de réduire | Contrôle de fréquence (< 110 bpm marche normale) |\n"
            "| Premier épisode | - | Pas encore classable | Pas d'antiarythmique chronique préventif |"
        )),
        TableauSynthese(titre="Synthèse - Score CHA₂DS₂-VA", markdown=(
            "| Lettre | Critère | Points |\n"
            "|--------|---------|--------|\n"
            "| C | Congestion (insuffisance cardiaque clinique) | 1 |\n"
            "| H | HTA traitée ou non | 1 |\n"
            "| A2 | Âge ≥ 75 ans | 2 |\n"
            "| D | Diabète | 1 |\n"
            "| S2 | Stroke / embolie artérielle | 2 |\n"
            "| V | Maladie vasculaire (coronaire, AOMI, athérome cérébral) | 1 |\n"
            "| A | Âge 65-74 ans | 1 |\n"
            "| **Total max** | | **8** |"
        )),
        TableauSynthese(titre="Synthèse - Indications de l'anticoagulation chronique", markdown=(
            "| Situation | Anticoagulant | Justification |\n"
            "|-----------|--------------|---------------|\n"
            "| Prothèse mécanique ou RM modéré-sévère | **AVK obligatoires** (INR 2-3 ; mitrale/disque 3-4,5) | Score CHA₂DS₂-VA non applicable |\n"
            "| Cardiomyopathie hypertrophique ou amylose | Anticoagulation systématique | Risque élevé constitutif |\n"
            "| Score CHA₂DS₂-VA = 0 | Aucun anticoagulant | Risque faible |\n"
            "| Score = 1 | Conseillé, discussion bénéfice/risque | Risque intermédiaire |\n"
            "| Score > 1 | AOD privilégiés > AVK | Risque significatif |\n"
            "| FA + AVC aigu | Pas d'AVK/héparine en aigu | Risque transformation hémorragique |"
        )),
        TableauSynthese(titre="Synthèse - Stratégies thérapeutiques", markdown=(
            "| Stratégie | Médicaments | Objectif | Population |\n"
            "|-----------|-------------|----------|------------|\n"
            "| Contrôle fréquence | Bêtabloquants, vérapamil, diltiazem, digoxine | FC < 110 bpm marche normale (holter) | FA permanente ou attente cardioversion |\n"
            "| Contrôle rythme - médicament | Amiodarone, flécaïnide, propafénone | Maintien rythme sinusal | FA paroxystique/persistante |\n"
            "| Contrôle rythme - ablation | Isolation veines pulmonaires | Maintien rythme sinusal long terme | FA paroxystique (1re ligne possible), tachycardiomyopathie |\n"
            "| IC ou coronarien | **Amiodarone seule** comme antiarythmique | Contre-indication flécaïnide, vérapamil, diltiazem | IC, coronaropathie |"
        )),
        TableauSynthese(titre="Synthèse - Tableaux cliniques typiques de FA", markdown=(
            "| Tableau | Terrain | Risque embolique | Stratégie |\n"
            "|---------|---------|------------------|-----------|\n"
            "| FA cœur normal | Quinquagénaire palpitations | Très faible (CHA₂DS₂-VA = 0) | Flécaïnide ou ablation |\n"
            "| FA + IC | Cardiopathie sévère, OAP | Élevé | Cardioversion + amiodarone + anticoag long cours |\n"
            "| FA valvulaire | Prothèse mécanique, RM | Très élevé | Contrôle fréquence + AVK long cours |\n"
            "| Embolie révélatrice | Femme âgée HTA mal équilibrée | Très élevé | UNV : pas AVK aigu, anticoag à la sortie |\n"
            "| Maladie de l'oreillette | Sujet âgé, syncopes | Variable | Pacemaker + ablation veines pulmonaires |"
        )),
        TableauSynthese(titre="Synthèse - Pré et post-cardioversion", markdown=(
            "| Phase | Durée | Modalité | Exception |\n"
            "|-------|-------|----------|-----------|\n"
            "| Avant cardioversion | ≥ 3 semaines d'anticoag efficace | Héparine ou AO efficace documentée | ETO normale ou FA < 24 h datée |\n"
            "| Cardioversion | Choc électrique sous AG ou antiarythmique (amiodarone, flécaïnide) | Immédiate si choc/urgence vitale | - |\n"
            "| Après cardioversion | ≥ 4 semaines d'anticoag efficace | AOD ou AVK | Puis poursuite selon CHA₂DS₂-VA |"
        )),
        TableauSynthese(titre="Synthèse - Stratégie thérapeutique selon le type de FA", markdown=(
            "| Objectif | Premier épisode | FA paroxystique | FA persistante | FA permanente |\n"
            "|----------|-----------------|-----------------|----------------|----------------|\n"
            "| Anticoagulation | Initialement, puis selon évolution et terrain | Selon terrain | Avant et après cardioversion, puis selon terrain | Selon terrain |\n"
            "| Cardioversion | Selon évolution | Selon évolution | Oui, si pas de régularisation spontanée | Non, par définition |\n"
            "| Contrôle de la fréquence | Initialement, puis selon évolution | Oui, le plus souvent | En attendant la cardioversion | Oui, le plus souvent |\n"
            "| Contrôle du rythme | Non, le plus souvent | Oui, le plus souvent | Oui, après cardioversion | Non, par définition |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Patients FA en France | 500 000 - 750 000 | Épidémiologie |\n"
        "| Activité atriale en FA | 400-600/min | Définition |\n"
        "| Prévalence après 80 ans | 10 % | Épidémiologie |\n"
        "| Augmentation par tranche IMC | +30 % par +5 kg/m² | Obésité |\n"
        "| Part de FA dans les AVC | 20-25 % | Risque embolique |\n"
        "| FA paroxystique - retour sinusal | < 7 jours | Classification |\n"
        "| FA persistante - retour sinusal | > 7 jours | Classification |\n"
        "| Risque familial 1er degré | +40 % | Génétique |\n"
        "| ATCD familial 1er degré | +40 % de risque | Étiologie |\n"
        "| Anticoag avant cardioversion | ≥ 3 semaines efficace | Cardioversion |\n"
        "| Anticoag après cardioversion | ≥ 4 semaines | Cardioversion |\n"
        "| Risque post-cardioversion | 4 semaines minimum | Surveillance |\n"
        "| FA datable | < 24 heures | Cardioversion sans 3 sem anticoag |\n"
        "| CHA₂DS₂-VA - âge ≥ 75 | 2 points | Score |\n"
        "| CHA₂DS₂-VA - AVC/embolie | 2 points | Score |\n"
        "| CHA₂DS₂-VA - âge 65-74 | 1 point | Score |\n"
        "| CHA₂DS₂-VA - C, H, D, V | 1 point chacun | Score |\n"
        "| Score CHA₂DS₂-VA total | 0 à 8 | Plage |\n"
        "| Risque annuel TE | 1 à 18 % (0 à 8) | Exponentiel, +2 % par palier |\n"
        "| Fermeture auricule - seuil | CHA₂DS₂-VA ≥ 2 | + CI permanente anticoag |\n"
        "| INR cible (FA non valvulaire) | 2,5 (2-3) | AVK |\n"
        "| INR cible (valve mécanique mitrale ou à disque) | 3-4,5 | AVK |\n"
        "| Perte poids cible obèse | 10 % | Hygiène |\n"
        "| IMC cible chez obèse | < 27 kg/m² | Hygiène |\n"
        "| PAS cible HTA | < 130 mmHg | Traitement |\n"
        "| FC cible contrôle fréquence | < 110 bpm | Marche normale, vérifié au holter |\n"
        "| Pauses sinusales pace | > 3 secondes | Symptomatique |\n"
        "| Bradycardie sinusale pace | < 50 bpm | Symptomatique non iatrogène |\n"
        "| Holter prolongé | 72 heures | Diagnostic FA non documentée |\n"
        "| AOD dose réduite | Après 80 ans | Sujet âgé |\n"
        "| INR contrôle minimal | 1 fois/mois | Équilibre atteint |\n"
        "| Fonction rénale AOD | ≥ 1 fois/an | Surveillance |\n"
        "| Dépistage routinier | ≥ 65 ans ou à risque | Dépistage |\n"
        "| Dépistage organisé | ≥ 75 ans ou ≥ 65 à risque TE | Dépistage |"
    ))

    points_cles = [
        "**FA** = tachycardie irrégulière supraventriculaire (400-600/min), **sans onde P** ; diagnostic **ECG obligatoire**",
        "Trouble du rythme le plus fréquent ; **10 %** après 80 ans ; responsable de **20-25 % des AVC**",
        "Classification **P-P-P-P** : paroxystique (< 7 j), persistante (> 7 j), permanente, premier épisode",
        "Bilan étio : interro + examen + ECG + RxT + **ETT + TSHus** + iono + créat + BH ; penser **HTA** (MAPA) et **SAOS**",
        "**CHA₂DS₂-VA** (C-1, H-1, A2-2, D-1, S2-2, V-1, A-1) = 0 à 8 ; non applicable si prothèse mécanique ou RM",
        "Anticoag : score 0 → rien ; score 1 → discuté ; score > 1 → **indiqué**. **AOD** sauf valvulaire → **AVK obligatoire**",
        "Cardioversion : **3 sem AVANT + 4 sem APRÈS** d'anticoag ; exceptions : ETO normale ou FA **< 24 h** datée",
        "2 stratégies : contrôle **fréquence** (FC < 110 bpm) vs contrôle **rythme** ; IC/coronarien → **amiodarone seule**",
        "**Ablation veines pulmonaires** : 1re ligne FA paroxystique, supérieure aux médicaments à long terme",
        "**FA + AVC aigu** : ni AVK ni héparines (transformation hémorragique) → **UNV** ; anticoag à la sortie",
    ]

    fiche_eclair_md = (
        "**FA** : tachycardie irrégulière supraventriculaire, atriale 400-600/min, sans onde P. "
        "Plus fréquent trouble du rythme. 20-25 % des AVC. Diagnostic ECG obligatoire.\n\n"
        "**Classification P-P-P-P** : Paroxystique < 7 j. Persistante > 7 j. Permanente. Premier épisode.\n\n"
        "**Étiologies** : HTA ++, valvulopathies mitrales, SAOS, EP, CMP, SCA, hyperthyroïdie. "
        "Bilan : ECG + RxT + ETT + TSHus + iono + créat + BH. MAPA si HTA, polygraphie si SAOS.\n\n"
        "**CHA₂DS₂-VA** : C-1, H-1, A2(≥75)-2, D-1, S2(AVC)-2, V-1, A(65-74)-1. Score 0 → rien. "
        "Score = 1 → discussion. Score > 1 → anticoag indiscutable. Type FA ne modifie pas l'indication.\n\n"
        "**Exceptions CHA₂DS₂-VA** : prothèse mécanique ou RM modéré-sévère → AVK (INR 2,5 ; "
        "mitrale/disque 3-4,5). CMP hypertrophique, amylose.\n\n"
        "**Anticoag** : AOD à privilégier sauf cas valvulaire. Idarucizumab = antidote dabigatran. "
        "Fluindione en 2e intention.\n\n"
        "**Cardioversion** : 3 sem AVANT + 4 sem APRÈS d'anticoag. Exceptions : ETO normale ou FA < 24 h. "
        "CEE sous AG ou amiodarone/flécaïnide. Urgence vitale → CEE immédiat.\n\n"
        "**Long cours** : contrôle fréquence (BB/inh. calciques/digoxine ; FC < 110 bpm) ou rythme "
        "(amiodarone/flécaïnide/propafénone). IC et coronarien : amiodarone seule. "
        "CI chez IC : vérapamil, diltiazem, flécaïnide.\n\n"
        "**Ablation veines pulmonaires** : 1re ligne FA paroxystique, > médicaments à long terme.\n\n"
        "**Fermeture auricule G** : CHA₂DS₂-VA ≥ 2 + CI permanente anticoag + comité.\n\n"
        "**FdR à corriger** : poids -10 % ou IMC < 27, activité physique, arrêt tabac, PAS < 130 mmHg, SAOS.\n\n"
        "**Tableaux** : cœur normal → flécaïnide ou ablation. IC → amiodarone. Valvulaire → contrôle "
        "fréquence + AVK. Embolie révélatrice → UNV, pas AVK aigu. Maladie oreillette → pacemaker.\n\n"
        "**Dépistage** : routinier ≥ 65 ans ; organisé ≥ 75 ans ; monitoring prolongé si AVC cryptogénique."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 232 - Fibrillation atriale",
        annee="2025-2026",
        item="Item 232",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi, partie_vii],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 232",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-232_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

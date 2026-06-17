"""Génère la fiche de l'Item 235 - Péricardite aiguë (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Généralités et diagnostic positif", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition et critères diagnostiques"),
            PlanSousPartie(lettre="B", titre="Signes cliniques"),
        ]),
        PlanPartie(numero="II", titre="Examens complémentaires", sous_parties=[
            PlanSousPartie(lettre="A", titre="ECG"),
            PlanSousPartie(lettre="B", titre="Bilan biologique"),
            PlanSousPartie(lettre="C", titre="Radiographie thoracique"),
            PlanSousPartie(lettre="D", titre="Échocardiographie"),
            PlanSousPartie(lettre="E", titre="Examens de 2e intention"),
        ]),
        PlanPartie(numero="III", titre="Hospitalisation et orientation", sous_parties=[
            PlanSousPartie(lettre="A", titre="Facteurs de risque majeurs (ESC 2015)"),
            PlanSousPartie(lettre="B", titre="Facteurs de risque mineurs"),
        ]),
        PlanPartie(numero="IV", titre="Étiologies", sous_parties=[
            PlanSousPartie(lettre="A", titre="Péricardite virale et idiopathique"),
            PlanSousPartie(lettre="B", titre="Péricardite purulente"),
            PlanSousPartie(lettre="C", titre="Péricardite tuberculeuse"),
            PlanSousPartie(lettre="D", titre="Péricardite néoplasique"),
            PlanSousPartie(lettre="E", titre="Autres étiologies"),
        ]),
        PlanPartie(numero="V", titre="Complications", sous_parties=[
            PlanSousPartie(lettre="A", titre="Tamponnade"),
            PlanSousPartie(lettre="B", titre="Myocardite associée"),
            PlanSousPartie(lettre="C", titre="Récidive et formes chroniques"),
            PlanSousPartie(lettre="D", titre="Constriction péricardique"),
        ]),
        PlanPartie(numero="VI", titre="Traitement", sous_parties=[
            PlanSousPartie(lettre="A", titre="Péricardite aiguë bénigne"),
            PlanSousPartie(lettre="B", titre="Tamponnade"),
            PlanSousPartie(lettre="C", titre="Suivi et notions inacceptables"),
        ]),
    ]

    # ── PARTIE I : GÉNÉRALITÉS ET DIAGNOSTIC POSITIF ──
    partie_i = Partie(numero="I", titre="Généralités et diagnostic positif", sous_parties=[
        SousPartie(lettre="A", titre="Définition et critères diagnostiques", rows=[
            FicheRow(concept="◆ Contexte diagnostique", detail_md=(
                "- Diagnostic évoqué dans le contexte d'une douleur thoracique aiguë\n"
                "- ⚠ Toujours évoquer les diagnostics différentiels à morbimortalité élevée :\n"
                "  - **Syndrome coronarien aigu (SCA)**\n"
                "  - **Embolie pulmonaire (EP)**\n"
                "  - **Dissection aortique**"
            )),
            FicheRow(concept="◆ Critères diagnostiques de péricardite aiguë", detail_md=(
                "- Le diagnostic repose sur l'association de 4 critères :\n"
                "  - Douleur thoracique évocatrice\n"
                "  - Frottement péricardique (éventuel)\n"
                "  - Modifications ECG typiques\n"
                "  - Épanchement péricardique\n"
                "- ◆ Présence de **2 de ces critères** nécessaire pour confirmer le diagnostic\n"
                "- ECG + échocardiographie : examens systématiques"
            )),
            FicheRow(concept="", detail_md=(
                "- Toute douleur thoracique aiguë impose d'éliminer **SCA, EP et dissection aortique** "
                "avant de retenir une péricardite.\n"
                "- Diagnostic = **2/4 critères** (douleur, frottement, ECG, épanchement) + ECG et "
                "ETT systématiques."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Signes cliniques", rows=[
            FicheRow(concept="◆ Fièvre modérée", detail_md=(
                "- Présente d'emblée, associée à myalgies et asthénie\n"
                "- Souvent précédée d'un épisode grippal\n"
                "- ⚠ Moins fréquente chez le sujet âgé"
            )),
            FicheRow(concept="◆ Douleur thoracique typique", detail_md=(
                "- Rétrosternale ou précordiale gauche, prolongée\n"
                "- **Résistante à la trinitrine**\n"
                "- Majorée par :\n"
                "  - Décubitus\n"
                "  - Inspiration profonde\n"
                "  - Toux\n"
                "- **Calmée par l'antéflexion** (position assise penchée en avant)"
            )),
            FicheRow(concept="Dyspnée", detail_md=(
                "- Parfois associée, également soulagée par l'antéflexion\n"
                "- Possibles : toux sèche, dysphonie, hoquet"
            )),
            FicheRow(concept="◆ Frottement péricardique", detail_md=(
                "- Bruit précoce, **systolodiastolique**, variant dans le temps et les positions\n"
                "- Décrit comme : crissement de cuir neuf, froissement de soie, "
                "bruit de pas dans la neige fraîche\n"
                "- ◆ Quand présent, confirme le diagnostic\n"
                "- ⚠ Mais **inconstant et fugace** : son absence n'élimine pas le diagnostic\n"
                "- Souvent accompagné d'une tachycardie"
            )),
            FicheRow(concept="Épanchement pleural", detail_md=(
                "- Parfois associé"
            )),
            FicheRow(concept="", detail_md=(
                "- Triade caractéristique : douleur **trinitro-résistante calmée par l'antéflexion** "
                "+ fièvre modérée post-grippale + **frottement péricardique** (inconstant).\n"
                "- Absence de frottement = ne pas éliminer le diagnostic."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE II : EXAMENS COMPLÉMENTAIRES ──
    partie_ii = Partie(numero="II", titre="Examens complémentaires", sous_parties=[
        SousPartie(lettre="A", titre="ECG", rows=[
            FicheRow(concept="◆ Principes généraux", detail_md=(
                "- ◆ Examen à répéter car il peut être normal\n"
                "- Anomalies diffuses non systématisées\n"
                "- ⚠ **Sans image en miroir** (≠ SCA)\n"
                "- Évolution en 4 stades"
            )),
            FicheRow(concept="◆ Évolution en 4 stades (Holzmann)", detail_md=(
                "| Stade | Délai | Anomalies ECG |\n"
                "|-------|-------|----------------|\n"
                "| **Stade I** | 1er jour | Sus-décalage ST concave vers le haut + ondes T positives |\n"
                "| **Stade II** | 24e-48e heure | Ondes T plates |\n"
                "| **Stade III** | 1re semaine | Ondes T négatives |\n"
                "| **Stade IV** | 1er mois | Normalisation |"
            )),
            FicheRow(concept="◆ Autres signes ECG", detail_md=(
                "- Sous-décalage de PQ présent à la phase initiale\n"
                "- Troubles du rythme supraventriculaires :\n"
                "  - Tachycardie sinusale\n"
                "  - Extrasystoles atriales\n"
                "  - Fibrillation atriale, flutter atrial\n"
                "- ◆ **Microvoltage** si épanchement abondant :\n"
                "  - Amplitude QRS **< 5 mm** en dérivations périphériques\n"
                "  - Amplitude QRS **< 10 mm** en dérivations précordiales\n"
                "- Alternance électrique (amplitude variable des QRS) : épanchement abondant"
            )),
            FicheRow(concept="", detail_md=(
                "- Comparaison à un SCA : ECG de péricardite = **diffus, sans miroir**, "
                "**sus-ST concave vers le haut**, sous-décalage PQ.\n"
                "- Microvoltage et alternance électrique = signes d'épanchement abondant."
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Bilan biologique", rows=[
            FicheRow(concept="◆ Bilan limité (formes non graves)", detail_md=(
                "- Doit être limité en l'absence d'orientation clinique, de signes de gravité "
                "ou de récidive\n"
                "- Marqueurs inflammatoires : NFS, CRP\n"
                "- Marqueurs de nécrose : **troponines I ou T**, troponines ultrasensibles\n"
                "- Ionogramme sanguin, urée, créatinine\n"
                "- Hémocultures si fièvre\n"
                "- IDR (intradermoréaction) discutée"
            )),
            FicheRow(concept="◆ Élévation des troponines = myocardite associée", detail_md=(
                "- Une augmentation significative des troponines\n"
                "- Coexistant éventuellement avec un trouble de cinétique VG global ou segmentaire\n"
                "- → Oriente vers une **myocardite associée**"
            )),
        ]),
        SousPartie(lettre="C", titre="Radiographie thoracique", rows=[
            FicheRow(concept="Aspect radiologique", detail_md=(
                "- Normale le plus souvent\n"
                "- En cas d'épanchement abondant :\n"
                "  - Rectitude du bord gauche\n"
                "  - **Cardiomégalie en carafe** (cœur triangulaire)\n"
                "- Aide au diagnostic étiologique :\n"
                "  - Pathologie pulmonaire associée\n"
                "  - Épanchement pleural"
            )),
        ]),
        SousPartie(lettre="D", titre="Échocardiographie", rows=[
            FicheRow(concept="◆ Indication systématique", detail_md=(
                "- Examen **systématique**\n"
                "- Parfois normale : on parle de péricardite « sèche »"
            )),
            FicheRow(concept="◆ Épanchement péricardique", detail_md=(
                "- Diagnostic posé devant :\n"
                "  - Simple décollement des deux feuillets péricardiques\n"
                "  - OU espace clair vide d'écho\n"
                "- ◆ Quantification de l'abondance :\n"
                "  - **< 10 mm** : minime\n"
                "  - **10-20 mm** : modéré\n"
                "  - **> 20 mm** : abondant\n"
                "- Évalue aussi la topographie et la tolérance hémodynamique\n"
                "- Confirme le diagnostic de tamponnade"
            )),
            FicheRow(concept="Masse péricardique", detail_md=(
                "- Éventualité rare, habituellement maligne\n"
                "- Visualise : masse localisée, métastases, caillots "
                "(péricardite néoplasique)\n"
                "- Bandes de fibrine + épanchement cloisonné facilement identifiés"
            )),
        ]),
        SousPartie(lettre="E", titre="Examens de 2e intention", rows=[
            FicheRow(concept="Scanner thoracique et IRM cardiaque", detail_md=(
                "- Indications :\n"
                "  - Patient non échogène\n"
                "  - Péricardite néoplasique\n"
                "  - Épanchement péricardique cloisonné\n"
                "- ◆ Avantages de l'**IRM** :\n"
                "  - Visualise la cavité péricardique sans injection ni irradiation\n"
                "  - Met en évidence l'inflammation péricardique (avec ou sans épanchement)\n"
                "  - Détecte une myocardite associée "
                "(séquence de **rehaussement tardif après gadolinium**)"
            )),
            FicheRow(concept="◆ Ponction péricardique - Indications", detail_md=(
                "- À envisager en cas de :\n"
                "  - **Tamponnade**\n"
                "  - Forte suspicion de péricardite néoplasique\n"
                "  - Épanchement abondant symptomatique malgré traitement médical bien conduit "
                "depuis 1 semaine"
            )),
            FicheRow(concept="Analyses du liquide péricardique", detail_md=(
                "- Biochimie : glucose, protides, LDH\n"
                "- Cytologie et analyse microscopique :\n"
                "  - Colorations de **Gram** et de **Ziehl-Nielsen**\n"
                "- Mise en culture bactérienne\n"
                "- PCR : recherche virale et de tuberculose"
            )),
            FicheRow(concept="⚠ Drainage chirurgical", detail_md=(
                "- À privilégier en cas de **suspicion de péricardite purulente**\n"
                "- Liquide péricardique recueilli pour analyse cytologique et microbiologique"
            )),
        ]),
    ])

    # ── PARTIE III : HOSPITALISATION ET ORIENTATION ──
    partie_iii = Partie(numero="III", titre="Hospitalisation et orientation", sous_parties=[
        SousPartie(lettre="A", titre="Facteurs de risque majeurs (ESC 2015)", rows=[
            FicheRow(concept="◆ Indications systématiques d'hospitalisation", detail_md=(
                "- ◆ L'hospitalisation n'est pas systématique une fois le diagnostic posé\n"
                "- Elle est utile en présence d'une complication d'emblée :\n"
                "  - Tamponnade\n"
                "  - Péricardite récidivante\n"
                "  - Constriction péricardique"
            )),
            FicheRow(concept="◆ 4 facteurs prédictifs majeurs (ESC 2015)", detail_md=(
                "- La présence d'un seul des 4 facteurs majeurs conduit à hospitaliser le patient :\n"
                "  - **Fièvre > 38 °C**\n"
                "  - Symptômes depuis plusieurs jours/semaines = début subaigu\n"
                "  - **Épanchement > 20 mm** ou tamponnade\n"
                "  - Résistance au traitement (aspirine/AINS) après **7 jours**\n"
                "- Risque de complication ou d'étiologie inhabituelle (moins de 20 % des cas)"
            )),
            FicheRow(concept="", detail_md=(
                "- **Mnémonique - 4 FdR majeurs ESC 2015** :\n"
                "  - **F**ièvre > 38 °C\n"
                "  - **É**panchement abondant (> 20 mm) ou tamponnade\n"
                "  - **B**ut subaigu (symptômes depuis plusieurs jours/semaines)\n"
                "  - **R**ésistance aux AINS après 7 jours"
            ), kind="mnemo"),
        ]),
        SousPartie(lettre="B", titre="Facteurs de risque mineurs", rows=[
            FicheRow(concept="◆ Autres situations à discuter (ESC 2015)", detail_md=(
                "- Facteurs prédictifs mineurs pouvant conduire à discuter l'hospitalisation :\n"
                "  - Patient immunodéprimé\n"
                "  - Patient traité par anticoagulant\n"
                "  - Suites d'un traumatisme thoracique\n"
                "  - Présence d'une myocardite associée (ou augmentation de la troponine)"
            )),
            FicheRow(concept="", detail_md=(
                "- Hospitalisation : **1 seul** facteur majeur suffit (Fièvre > 38 °C, début subaigu, "
                "épanchement > 20 mm ou tamponnade, résistance AINS 7 j).\n"
                "- Sinon, prise en charge ambulatoire envisageable."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE IV : ÉTIOLOGIES ──
    partie_iv = Partie(numero="IV", titre="Étiologies", sous_parties=[
        SousPartie(lettre="A", titre="Péricardite virale et idiopathique", rows=[
            FicheRow(concept="◆ Épidémiologie", detail_md=(
                "- ◆ Dans **9 cas sur 10**, la cause est virale ou inconnue "
                "(péricardite aiguë idiopathique)\n"
                "- 3 grandes étiologies modifiant la stratégie thérapeutique (pays développés) :\n"
                "  - **Tuberculose**\n"
                "  - **Cancer**\n"
                "  - **Maladies auto-immunes**"
            )),
            FicheRow(concept="◆ Tableau clinique typique - Péricardite virale", detail_md=(
                "- Sujet jeune, syndrome grippal récent, prédominance masculine\n"
                "- Début brutal, fébrile\n"
                "- Douleur thoracique typique augmentant à l'inspiration\n"
                "- Frottement péricardique\n"
                "- Modifications ECG typiques\n"
                "- Échocardiographie normale le plus souvent\n"
                "- Épanchement pleural souvent associé"
            )),
            FicheRow(concept="Virus en cause", detail_md=(
                "- Entérovirus (coxsackie A et B), échovirus, adénovirus\n"
                "- Cytomégalovirus (CMV), parvovirus B19, Epstein-Barr (EBV)\n"
                "- Herpès, VIH, hépatite C, influenza, etc."
            )),
            FicheRow(concept="Diagnostic viral", detail_md=(
                "- Sérologies répétées à **15 jours d'intervalle** : élévation des Ac spécifiques\n"
                "- Seul le diagnostic viral confirme :\n"
                "  - PCR sur épanchement péricardique\n"
                "  - OU biopsie péricardique\n"
                "- ⚠ Sérologies inutiles dans les formes typiques sans gravité"
            )),
            FicheRow(concept="◆ Évolution et complications", detail_md=(
                "- Évolution le plus souvent favorable\n"
                "- ◆ **Récidive 20-30 %** = complication la plus fréquente\n"
                "- Tamponnade et constriction : rares\n"
                "- Formes chroniques récidivantes : traitements spécifiques discutés "
                "(immunoglobulines, interféron α)"
            )),
            FicheRow(concept="Péricardite et VIH", detail_md=(
                "- Survenue fréquente d'une péricardite avec épanchement\n"
                "- Mécanismes multiples :\n"
                "  - Infection virale par le VIH ou autres virus\n"
                "  - Surinfection bactérienne ou fongique chez immunodéprimé\n"
                "  - **Lymphome** ou **sarcome de Kaposi**"
            )),
        ]),
        SousPartie(lettre="B", titre="Péricardite purulente", rows=[
            FicheRow(concept="⚠ Rare mais grave", detail_md=(
                "- Rare mais **grave** ; nette diminution\n"
                "- Touche essentiellement :\n"
                "  - Sujets immunodéprimés\n"
                "  - Porteurs d'infection sévère : septicémie, affection pleuropulmonaire\n"
                "  - Après chirurgie cardiaque ou thoracique"
            )),
            FicheRow(concept="Germes en cause", detail_md=(
                "- **Staphylocoques**, **pneumocoques**, **streptocoques**\n"
                "- Bacilles à Gram négatif, etc."
            )),
            FicheRow(concept="Pronostic et traitement", detail_md=(
                "- Pronostic sévère : survenue fréquente de tamponnade ou de constriction\n"
                "- Traitement :\n"
                "  - **Antibiothérapie adaptée** au germe retrouvé dans le liquide péricardique\n"
                "  - **Drainage chirurgical** souvent nécessaire"
            )),
        ]),
        SousPartie(lettre="C", titre="Péricardite tuberculeuse", rows=[
            FicheRow(concept="◆ Tableau clinique", detail_md=(
                "- Péricardite subaiguë liquidienne\n"
                "- Altération de l'état général et fièvre modérée persistante\n"
                "- Terrains : tuberculeux, âgé, greffé, infecté par le VIH, alcoolique"
            )),
            FicheRow(concept="Éléments d'orientation", detail_md=(
                "- Notion de tuberculose dans l'entourage\n"
                "- Virage récent de l'IDR\n"
                "- ⚠ **IDR faussement négative dans 1/3 des cas**\n"
                "- Anomalies pulmonaires radiologiques fréquentes"
            )),
            FicheRow(concept="◆ Recherche du BK (Mycobacterium tuberculosis)", detail_md=(
                "- Prélèvements : expectoration, tubages gastriques, "
                "liquide pleural et/ou péricardique\n"
                "- Examen direct + cultures sur milieux enrichis\n"
                "- Identification par PCR\n"
                "- ◆ Fortes concentrations d'**adénosine-déaminase** dans le liquide de ponction "
                "= en faveur du diagnostic\n"
                "- Parfois ponction-biopsie du péricarde : granulome inflammatoire"
            )),
            FicheRow(concept="◆ Évolution et traitement", detail_md=(
                "- Évolution fréquente vers tamponnade, récidive ou constriction\n"
                "- Traitement :\n"
                "  - **Antituberculeux**\n"
                "  - ± Corticoïdes (prednisone) pour diminuer le risque de constriction"
            )),
        ]),
        SousPartie(lettre="D", titre="Péricardite néoplasique", rows=[
            FicheRow(concept="Tumeurs primitives", detail_md=(
                "- Mésothéliome péricardique primitif : rare\n"
                "- **40 fois moins fréquentes** que les métastases"
            )),
            FicheRow(concept="◆ Tumeurs secondaires les plus fréquentes", detail_md=(
                "- **Cancer bronchique**\n"
                "- **Cancer du sein**\n"
                "- Mélanomes\n"
                "- Leucémies, lymphomes\n"
                "- Sarcome de Kaposi (sida)"
            )),
            FicheRow(concept="◆ Présentation", detail_md=(
                "- Épanchement péricardique hémorragique fréquent\n"
                "- Tamponnade fréquente\n"
                "- Diagnostic confirmé par échocardiographie\n"
                "- ± Complétée par scanner ou IRM cardiaque\n"
                "- ◆ Analyse du liquide de ponction ou **biopsie péricardique** "
                "essentielles au diagnostic de malignité"
            )),
            FicheRow(concept="⚠ Prise en charge", detail_md=(
                "- Tamponnade = **ponction péricardique en urgence**\n"
                "- Récidive de l'épanchement fréquente\n"
                "- Suivi clinique et échocardiographique indispensable"
            )),
        ]),
        SousPartie(lettre="E", titre="Autres étiologies", rows=[
            FicheRow(concept="Maladies systémiques auto-immunes", detail_md=(
                "- Étiologies les plus fréquentes :\n"
                "  - **Lupus**\n"
                "  - **Polyarthrite rhumatoïde**\n"
                "  - Sclérodermie\n"
                "  - Périartérite noueuse\n"
                "  - Dermatomyosite\n"
                "- Diagnostic d'élimination\n"
                "- Critères diagnostiques : lymphocytes augmentés, "
                "anticorps antisarcolemme dans le liquide péricardique, myocardite associée"
            )),
            FicheRow(concept="◆ Péricardite et infarctus du myocarde", detail_md=(
                "- ◆ **Péricardite précoce (J3-J5)** :\n"
                "  - Au décours d'un infarctus transmural\n"
                "  - Évolution le plus souvent favorable\n"
                "- ◆ **Péricardite tardive 2e-16e semaine = syndrome de Dressler** :\n"
                "  - Fièvre, péricardite, pleurésie, arthralgies, AEG\n"
                "  - Syndrome inflammatoire important\n"
                "  - Allongement du QT à l'ECG\n"
                "  - Devenu rare depuis la reperfusion coronarienne précoce"
            )),
            FicheRow(concept="Péricardite et insuffisance rénale chronique", detail_md=(
                "- Péricardite urémique :\n"
                "  - IR sévère non encore dialysée\n"
                "  - OU premières semaines après instauration de la dialyse\n"
                "- Patient dialysé au long cours :\n"
                "  - Témoigne d'un traitement épurateur inadapté"
            )),
            FicheRow(concept="Syndrome postpéricardotomie", detail_md=(
                "- Origine inflammatoire\n"
                "- Survient dans les jours ou mois suivant une chirurgie cardiaque "
                "ou après transplantation\n"
                "- Tamponnade possible\n"
                "- ⚠ La chirurgie cardiaque est actuellement la **1re cause de constriction**\n"
                "- En postopératoire : possibilité d'hémopéricarde"
            )),
            FicheRow(concept="Autres causes", detail_md=(
                "- Dissection aortique avec tamponnade\n"
                "- Irradiation thoracique (radiothérapie pour lymphome, cancer du sein, etc.), "
                "en général 1 an après\n"
                "- Traumatismes thoraciques/cardiaques : hémopéricarde\n"
                "  - Cathétérismes : surtout après ablation par radiofréquence "
                "ou pose de stimulateur cardiaque\n"
                "  - Postopératoire immédiat\n"
                "- Médicaments : hydralazine, pénicilline\n"
                "- Hypothyroïdie\n"
                "- Rhumatisme articulaire aigu"
            )),
        ]),
    ])

    # ── PARTIE V : COMPLICATIONS ──
    partie_v = Partie(numero="V", titre="Complications", sous_parties=[
        SousPartie(lettre="A", titre="Tamponnade", rows=[
            FicheRow(concept="◆ Définition - URGENCE", detail_md=(
                "- ◆ **Compression des cavités droites** par un épanchement péricardique "
                "abondant et/ou d'installation brutale\n"
                "- ⚠ **URGENCE** : cause d'arrêt cardiocirculatoire par adiastolie "
                "en l'absence de traitement\n"
                "- Confirmation échographique impose le drainage"
            )),
            FicheRow(concept="Contextes étiologiques", detail_md=(
                "- Péricardites néoplasiques\n"
                "- Traumatiques\n"
                "- Tuberculeuses\n"
                "- Hémopéricardes\n"
                "- Exceptionnellement : péricardite aiguë virale"
            )),
            FicheRow(concept="◆ Signes cliniques", detail_md=(
                "- Douleur thoracique avec dyspnée positionnelle, polypnée puis orthopnée, toux\n"
                "- Parfois : dysphagie, nausées, hoquet\n"
                "- ◆ **Signes droits** : turgescence jugulaire, reflux hépatojugulaire\n"
                "- ◆ **Signes de choc** : tachycardie, **PAS < 90 mmHg**\n"
                "- Bruits du cœur assourdis\n"
                "- ◆ **Pouls paradoxal** : PAS inspiration < PAS expiration de **10 mmHg**"
            )),
            FicheRow(concept="◆ Mécanisme du pouls paradoxal", detail_md=(
                "- Inspiration : augmentation du retour veineux\n"
                "- → Dilatation du ventricule droit\n"
                "- → Compression du ventricule gauche\n"
                "- → Baisse de la PAS en inspiration"
            )),
            FicheRow(concept="◆ Examens complémentaires", detail_md=(
                "- ECG : microvoltage, parfois alternance électrique\n"
                "- Radiographie thoracique : cardiomégalie, aspect en « carafe »\n"
                "- ◆ **Échocardiographie** confirme le diagnostic :\n"
                "  - **Collapsus diastolique** des cavités droites en expiration\n"
                "  - Compression du VG par le VD en inspiration\n"
                "  - **« Swinging heart »** : balancement du cœur dans la cavité péricardique\n"
                "  - Septum paradoxal en inspiration\n"
                "  - Épanchement souvent abondant"
            )),
            FicheRow(concept="", detail_md=(
                "- **Tamponnade = urgence vitale** (adiastolie → arrêt cardiocirculatoire).\n"
                "- Triade : **signes droits + signes de choc + pouls paradoxal**.\n"
                "- ETT = swinging heart, collapsus diastolique droit, septum paradoxal.\n"
                "- **Drainage URGENT** (ponction écho-guidée ou chirurgical)."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Myocardite associée", rows=[
            FicheRow(concept="◆ Tableau clinique", detail_md=(
                "- Insuffisance cardiaque fébrile\n"
                "- Parfois état de choc : myocardite fulminante\n"
                "- Souvent cause inconnue ou virale"
            )),
            FicheRow(concept="Diagnostic", detail_md=(
                "- Échocardiographie : trouble de cinétique segmentaire ou global\n"
                "- ◆ **IRM cardiaque** surtout utile"
            )),
        ]),
        SousPartie(lettre="C", titre="Récidive et formes chroniques", rows=[
            FicheRow(concept="◆ Péricardite récidivante", detail_md=(
                "- Survient souvent à la suite d'une durée de traitement insuffisante\n"
                "- ◆ Complication fréquente entre **3 mois et 3 ans** après une péricardite "
                "aiguë d'allure virale\n"
                "- ◆ **La colchicine en prévient la survenue**"
            )),
            FicheRow(concept="Péricardite chronique (> 3 mois)", detail_md=(
                "- Étiologie problématique, surtout en l'absence de contexte évocateur viral\n"
                "- Peut nécessiter une péricardoscopie par fibre optique avec biopsie dirigée\n"
                "- Fait suspecter une péricardite tuberculeuse\n"
                "- ⚠ En pratique, les **causes néoplasiques** sont le plus fréquemment retrouvées"
            )),
        ]),
        SousPartie(lettre="D", titre="Constriction péricardique", rows=[
            FicheRow(concept="◆ Définition et épidémiologie", detail_md=(
                "- Évolution vers une constriction modérée dans **moins de 10 % des cas**\n"
                "- Liée à un épaississement fibreux ou fibrocalcaire du péricarde\n"
                "- Calcifications péricardiques parfois visibles sur radio de thorax, "
                "surtout au scanner"
            )),
            FicheRow(concept="◆ Conséquences hémodynamiques", detail_md=(
                "- **Adiastolie**\n"
                "- Égalisation des pressions télédiastoliques des 4 cavités cardiaques"
            )),
            FicheRow(concept="◆ Tableau clinique", detail_md=(
                "- **Insuffisance cardiaque droite** (souvent prédominante) :\n"
                "  - Turgescence jugulaire\n"
                "  - Ascite\n"
                "- ET gauche"
            )),
            FicheRow(concept="◆ Diagnostic et traitement", detail_md=(
                "- Diagnostic échographique\n"
                "- Parfois confirmé par cathétérisme droit : aspect en **« dip plateau »**\n"
                "- ⚠ Diagnostic différentiel : cardiomyopathies restrictives\n"
                "- Traitement : parfois chirurgical par **péricardectomie**"
            )),
        ]),
    ])

    # ── PARTIE VI : TRAITEMENT ──
    partie_vi = Partie(numero="VI", titre="Traitement", sous_parties=[
        SousPartie(lettre="A", titre="Péricardite aiguë bénigne", rows=[
            FicheRow(concept="★ ◆ Mesures générales", detail_md=(
                "- Hospitalisation si :\n"
                "  - Facteurs de risque majeurs\n"
                "  - Complications\n"
                "  - Étiologie particulière\n"
                "- **Repos** avec arrêt de l'exercice physique :\n"
                "  - Jusqu'à disparition des symptômes\n"
                "  - Et normalisation de la CRP, de l'ECG et de l'échocardiographie\n"
                "  - En général le 1er mois\n"
                "- Traitement de la douleur thoracique\n"
                "- Protecteur gastrique"
            )),
            FicheRow(concept="★ ◆ Bithérapie anti-inflammatoire prolongée", detail_md=(
                "- ◆ **AINS pendant 1 à 2 semaines à pleine dose** :\n"
                "  - **Aspirine 750-1 000 mg/8 h**\n"
                "  - OU **ibuprofène 600 mg/8 h**\n"
                "- Arrêt progressif au bout de **4 à 8 semaines** (recommandations ESC 2015)\n"
                "  - Durée plus courte dans la pratique clinique actuelle\n"
                "- ◆ **+ Colchicine 0,5 mg × 2/j pendant 3 mois** :\n"
                "  - Calme la douleur\n"
                "  - Diminue la durée des symptômes\n"
                "  - ◆ **Réduit le risque de récidives de 50 %**"
            )),
            FicheRow(concept="◆ Tableau - Colchicine : précautions", detail_md=(
                "| Aspect | Détail |\n"
                "|--------|--------|\n"
                "| **Posologie** | 0,5 mg × 2/j pendant 3 mois |\n"
                "| **Effet indésirable principal** | Diarrhée → diminuer les doses |\n"
                "| **Interactions (CYP3A4)** | Macrolides, ciclosporine, vérapamil, statines |\n"
                "| **Surveillance biologique** | Transaminases, créatinine, CPK, NFS, plaquettes |\n"
                "| **Posologie réduite (0,5 mg/j)** | < 70 kg, > 70 ans, IR (DFG < 35 mL/min) |\n"
                "| **Contre-indication** | Insuffisance rénale sévère |\n"
                "| **Arrêt** | Progressif : dernière semaine 0,5 mg/j 1 jour/2 |"
            )),
            FicheRow(concept="⚠ Place des corticoïdes", detail_md=(
                "- ⚠ **Pas indiqués en 1re intention** (risque de récidive accru)\n"
                "- En cas d'échec du traitement AINS + colchicine :\n"
                "  - Corticoïdes utilisés avec la bithérapie\n"
                "  - Dose : **0,25-0,5 mg/kg/j**"
            )),
            FicheRow(concept="◆ Suivi", detail_md=(
                "- À 7 jours : médecin traitant\n"
                "- À 1 mois : cardiologue avec échocardiographie\n"
                "- À 3 et 6 mois : médecin traitant (si besoin cardiologue)\n"
                "- Objectifs : absence de symptômes, CRP normalisée, échocardiographie normalisée\n"
                "- Gestion des modalités d'arrêt des traitements"
            )),
            FicheRow(concept="", detail_md=(
                "- Bithérapie de référence : **AINS 1-2 semaines pleine dose** "
                "(aspirine 750-1000 mg/8 h OU ibuprofène 600 mg/8 h) **+ colchicine 0,5 mg × 2/j × 3 mois**.\n"
                "- **Corticoïdes en 1re intention = notion inacceptable** (risque de récidive)."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Tamponnade", rows=[
            FicheRow(concept="⚠ URGENCE médicochirurgicale", detail_md=(
                "- **Urgence médicochirurgicale** nécessitant une hospitalisation en **USIC** "
                "(soins intensifs de cardiologie)\n"
                "- Risque d'arrêt cardiocirculatoire"
            )),
            FicheRow(concept="◆ Prise en charge initiale", detail_md=(
                "- Remplissage par macromolécules\n"
                "- ⚠ Discuter l'arrêt des anticoagulants ou leur neutralisation"
            )),
            FicheRow(concept="◆ Drainage urgent", detail_md=(
                "- **Ponction péricardique** guidée par échocardiographie\n"
                "- OU drainage péricardique chirurgical"
            )),
        ]),
        SousPartie(lettre="C", titre="Suivi et notions inacceptables", rows=[
            FicheRow(concept="◆ Suivi - Réflexes transversaux", detail_md=(
                "- **Item 230** - Douleur thoracique aiguë\n"
                "- **Item 231** - Électrocardiogramme : indications et interprétation"
            )),
            FicheRow(concept="⚠ Notions inacceptables", detail_md=(
                "- ⚠ Ne pas identifier les situations d'urgence et planifier leur prise en charge "
                "(**tamponnade**)\n"
                "- ⚠ Recourir au traitement corticoïde en 1re intention"
            )),
            FicheRow(concept="", detail_md=(
                "- **Tamponnade** = ponction péricardique écho-guidée OU drainage chirurgical en urgence.\n"
                "- USIC + remplissage + discussion de l'arrêt des anticoagulants.\n"
                "- ⚠ Risque d'arrêt cardiocirculatoire par adiastolie."
            ), kind="a_retenir"),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Synthèse - Critères diagnostiques de péricardite aiguë (2/4)", markdown=(
            "| Critère | Détail | Caractère |\n"
            "|---------|--------|-----------|\n"
            "| **Douleur thoracique** | Rétrosternale, prolongée, trinitro-résistante, majorée à l'inspiration, calmée par antéflexion | Subjectif |\n"
            "| **Frottement péricardique** | Systolodiastolique, variable (cuir neuf, soie, neige fraîche) | Inconstant, fugace |\n"
            "| **Modifications ECG typiques** | Anomalies diffuses sans miroir, 4 stades | À répéter |\n"
            "| **Épanchement péricardique** | À l'échocardiographie | Systématique |"
        )),
        TableauSynthese(titre="Synthèse - ECG : 4 stades de la péricardite", markdown=(
            "| Stade | Délai | Anomalies |\n"
            "|-------|-------|-----------|\n"
            "| **I** | 1er jour | Sus-décalage ST concave vers le haut + onde T positive |\n"
            "| **II** | 24e-48e heure | Ondes T plates |\n"
            "| **III** | 1re semaine | Ondes T négatives |\n"
            "| **IV** | 1er mois | Normalisation |\n"
            "| **Autres** | Initial | Sous-décalage de PQ, tachycardie sinusale, troubles SV |\n"
            "| **Épanchement abondant** | Variable | Microvoltage (QRS < 5 mm périph., < 10 mm précord.), alternance électrique |"
        )),
        TableauSynthese(titre="Synthèse - Quantification de l'épanchement péricardique (ETT)", markdown=(
            "| Abondance | Épaisseur | Conduite |\n"
            "|-----------|-----------|----------|\n"
            "| **Minime** | < 10 mm | Ambulatoire le plus souvent |\n"
            "| **Modéré** | 10-20 mm | Surveillance |\n"
            "| **Abondant** | > 20 mm | **Hospitalisation** (FdR majeur), risque de tamponnade |"
        )),
        TableauSynthese(titre="Synthèse - Facteurs de risque ESC 2015 et indications d'hospitalisation", markdown=(
            "| Type | Facteur | Décision |\n"
            "|------|---------|----------|\n"
            "| **Majeur** (1 seul suffit) | Fièvre > 38 °C | Hospitalisation |\n"
            "| **Majeur** | Début subaigu (jours-semaines) | Hospitalisation |\n"
            "| **Majeur** | Épanchement > 20 mm ou tamponnade | Hospitalisation |\n"
            "| **Majeur** | Résistance aux AINS après 7 jours | Hospitalisation |\n"
            "| **Mineur** | Patient immunodéprimé | À discuter |\n"
            "| **Mineur** | Anticoagulant | À discuter |\n"
            "| **Mineur** | Traumatisme thoracique | À discuter |\n"
            "| **Mineur** | Myocardite associée | À discuter |"
        )),
        TableauSynthese(titre="Synthèse - Principales étiologies", markdown=(
            "| Étiologie | Fréquence | Spécificités | Prise en charge |\n"
            "|-----------|-----------|--------------|-----------------|\n"
            "| **Virale / idiopathique** | 9/10 cas | Sujet jeune, syndrome grippal, masculin | AINS + colchicine |\n"
            "| **Purulente** | Rare mais grave | Immunodéprimé, post-chirurgie | ATB + drainage chirurgical |\n"
            "| **Tuberculeuse** | Subaiguë | AEG, fièvre persistante, IDR (1/3 faux nég.), ADA | Antituberculeux ± corticoïdes |\n"
            "| **Néoplasique** | Métastases > primitives | Bronchique, sein, mélanome, leucémie, lymphome, Kaposi | Ponction + biopsie + chimio |\n"
            "| **Auto-immune** | - | Lupus, PR, sclérodermie, PAN, dermatomyosite | Diagnostic d'élimination |\n"
            "| **Dressler (post-IDM tardive)** | Rare (reperfusion) | 2e-16e semaine, fièvre + pleurésie + arthralgies | AINS + colchicine |\n"
            "| **Précoce post-IDM** | J3-J5, IDM transmural | Évolution favorable | Surveillance |\n"
            "| **Urémique** | IR sévère ou dialyse | - | Optimiser dialyse |\n"
            "| **Postpéricardotomie** | Post-chirurgie | 1re cause de constriction | AINS + colchicine |\n"
            "| **Autres** | - | Dissection, radiothérapie, traumatisme, médicaments, hypothyroïdie, RAA | Étiologique |"
        )),
        TableauSynthese(titre="Synthèse - Tamponnade vs Constriction péricardique", markdown=(
            "| Critère | Tamponnade | Constriction |\n"
            "|---------|------------|--------------|\n"
            "| **Mécanisme** | Compression aiguë des cavités droites par épanchement abondant | Épaississement fibrocalcaire chronique |\n"
            "| **Délai** | Aigu / brutal | Évolution > 3 mois, < 10 % des cas |\n"
            "| **Clinique** | Choc, pouls paradoxal, signes droits | IC droite (turgescence, ascite) + gauche |\n"
            "| **ECG** | Microvoltage, alternance électrique | - |\n"
            "| **ETT** | Swinging heart, collapsus diastolique droit, septum paradoxal | Épaississement péricardique |\n"
            "| **Cathétérisme** | - | Aspect en dip plateau, égalisation pressions 4 cavités |\n"
            "| **DD** | SCA, EP, dissection aortique | Cardiomyopathies restrictives |\n"
            "| **Traitement** | Urgence : ponction écho-guidée ou drainage chirurgical | Péricardectomie chirurgicale |"
        )),
        TableauSynthese(titre="Synthèse - Traitement de la péricardite aiguë bénigne", markdown=(
            "| Médicament | Posologie | Durée | Particularités |\n"
            "|------------|-----------|-------|----------------|\n"
            "| **Aspirine** | 750-1 000 mg/8 h | 1-2 sem pleine dose, arrêt progressif 4-8 sem | À pleine dose |\n"
            "| **Ibuprofène** | 600 mg/8 h | 1-2 sem pleine dose, arrêt progressif 4-8 sem | Alternative |\n"
            "| **Colchicine** | 0,5 mg × 2/j | 3 mois | -50 % récidives ; CI si IR sévère |\n"
            "| **Colchicine - dose réduite** | 0,5 mg/j | 3 mois | < 70 kg, > 70 ans, DFG < 35 mL/min |\n"
            "| **Corticoïdes** | 0,25-0,5 mg/kg/j | À discuter | 2e ligne uniquement (échec AINS+colchicine) |\n"
            "| **Protecteur gastrique** | - | Pendant la bithérapie | Toujours |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Critères diagnostiques nécessaires | 2/4 | Douleur, frottement, ECG, épanchement |\n"
        "| Stade I ECG | 1er jour | Sus-ST concave + T positives |\n"
        "| Stade II ECG | 24e-48e heure | T plates |\n"
        "| Stade III ECG | 1re semaine | T négatives |\n"
        "| Stade IV ECG | 1er mois | Normalisation |\n"
        "| Microvoltage périphérique | QRS < 5 mm | Épanchement abondant |\n"
        "| Microvoltage précordial | QRS < 10 mm | Épanchement abondant |\n"
        "| Épanchement minime | < 10 mm | ETT |\n"
        "| Épanchement modéré | 10-20 mm | ETT |\n"
        "| Épanchement abondant | > 20 mm | ETT, hospitalisation |\n"
        "| Fièvre FdR majeur | > 38 °C | ESC 2015 |\n"
        "| Résistance aux AINS | 7 jours | FdR majeur ESC 2015 |\n"
        "| Cause virale/idiopathique | 9/10 cas | Étiologie |\n"
        "| Récidive après péricardite virale | 20-30 % | Complication la plus fréquente |\n"
        "| Délai récidive | 3 mois à 3 ans | Après péricardite virale |\n"
        "| Évolution vers constriction | < 10 % | Forme modérée |\n"
        "| Tumeurs primitives vs métastases | 1 pour 40 | Tumeurs cardiaques |\n"
        "| IDR faussement négative TB | ~1/3 | Péricardite tuberculeuse |\n"
        "| Péricardite précoce post-IDM | J3-J5 | Post-IDM transmural |\n"
        "| Syndrome de Dressler | 2e-16e semaine | Post-IDM tardive |\n"
        "| Délai irradiation thoracique | ~1 an | Étiologie |\n"
        "| Sérologies virales | À 15 jours d'intervalle | Élévation Ac |\n"
        "| Pouls paradoxal | PAS insp - PAS exp ≥ 10 mmHg | Tamponnade |\n"
        "| PAS dans la tamponnade | < 90 mmHg | Choc |\n"
        "| Aspirine | 750-1 000 mg/8 h | Pleine dose |\n"
        "| Ibuprofène | 600 mg/8 h | Pleine dose |\n"
        "| Durée AINS pleine dose | 1-2 semaines | Puis arrêt progressif 4-8 semaines |\n"
        "| Colchicine - dose standard | 0,5 mg × 2/j | Pendant 3 mois |\n"
        "| Colchicine - dose réduite | 0,5 mg/j | < 70 kg, > 70 ans, DFG < 35 mL/min |\n"
        "| Colchicine - réduction récidive | -50 % | Bénéfice clé |\n"
        "| Colchicine - DFG CI | < 35 mL/min | IR sévère = CI |\n"
        "| Corticoïdes - dose si échec AINS | 0,25-0,5 mg/kg/j | 2e ligne |\n"
        "| Ponction péricardique - échec AINS | > 1 semaine | Épanchement abondant symptomatique |\n"
        "| Suivi à 7 jours | Médecin traitant | - |\n"
        "| Suivi à 1 mois | Cardiologue + ETT | - |\n"
        "| Suivi à 3 et 6 mois | Médecin traitant ± cardiologue | - |"
    ))

    points_cles = [
        "Diagnostic = **2/4 critères** (douleur, frottement, ECG, épanchement) ; ECG + ETT systématiques",
        "Douleur **trinitro-résistante**, majorée inspiration, **calmée par antéflexion** ; éliminer SCA, EP, dissection",
        "ECG : **4 stades Holzmann**, sus-ST concave **diffus sans miroir** + sous-décalage PQ",
        "ETT : épanchement **< 10 mm minime / 10-20 modéré / > 20 mm abondant** ; recherche tamponnade",
        "Hospitalisation si **1 FdR majeur ESC 2015** : fièvre > 38 °C, subaigu, > 20 mm, résistance AINS 7 j",
        "Étiologies : **9/10 virales/idiopathiques** ; 3 clés : tuberculose, cancer, auto-immunes",
        "**Tamponnade = urgence** : signes droits + choc + **pouls paradoxal** ; drainage écho-guidé urgent",
        "Traitement : **AINS 1-2 sem pleine dose + colchicine 0,5 mg × 2/j × 3 mois** (-50 % récidives) + IPP",
        "**Corticoïdes en 1re intention = inacceptable** ; 2e ligne uniquement (0,25-0,5 mg/kg/j)",
        "**Récidive 20-30 %** = complication la + fréquente ; prévenue par colchicine ; constriction < 10 %",
    ]

    fiche_eclair_md = (
        "**Diagnostic** : 2/4 critères (douleur trinitro-résistante calmée par antéflexion + frottement + ECG + épanchement). ECG + ETT systématiques. Éliminer SCA, EP, dissection.\n\n"
        "**ECG** : 4 stades Holzmann — I (J1, sus-ST concave + T+), II (24-48 h, T plates), III (1 sem, T-), IV (1 mois). Diffus sans miroir + sous-PQ. Microvoltage si épanchement abondant.\n\n"
        "**Bilan** : NFS, CRP, troponines (myocardite si ↑), iono/urée/créat, hémocultures si fièvre.\n\n"
        "**ETT** : < 10 mm minime / 10-20 mm modéré / > 20 mm abondant. IRM 2e intention.\n\n"
        "**Hospitalisation ESC 2015** : 1 FdR majeur — fièvre > 38 °C, début subaigu, épanchement > 20 mm, résistance AINS 7 j.\n\n"
        "**Étiologies** : 9/10 virale/idiopathique. 3 à connaître : tuberculose, cancer, auto-immunes. Post-IDM (J3-J5 ; Dressler 2e-16e sem), urémique, postpéricardotomie (1re cause constriction).\n\n"
        "**Tamponnade = urgence** : signes droits + choc + pouls paradoxal (≥ 10 mmHg). ETT : swinging heart, collapsus diastolique droit. Drainage urgent en USIC.\n\n"
        "**Complications** : récidive 20-30 % (la + fréquente), constriction < 10 %, myocardite.\n\n"
        "**Traitement** : repos + AINS 1-2 sem (aspirine 750-1000 mg/8 h OU ibuprofène 600 mg/8 h) + colchicine 0,5 mg × 2/j × 3 mois (-50 % récidives) + IPP.\n\n"
        "**Colchicine** : 0,5 mg/j si < 70 kg, > 70 ans, DFG < 35. CI si IR sévère. Interactions CYP3A4.\n\n"
        "**Inacceptable** : corticoïdes en 1re intention. 2e ligne : 0,25-0,5 mg/kg/j avec bithérapie.\n\n"
        "**Suivi** : J7 (MT), 1 mois (cardio + ETT), 3-6 mois."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 235 - Péricardite aiguë",
        annee="2025-2026",
        item="Item 235",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 235",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-235_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

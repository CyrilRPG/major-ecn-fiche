"""Génère la fiche de l'Item 339 - Syndromes coronariens aigus (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Définitions", sous_parties=[
            PlanSousPartie(lettre="A", titre="Syndromes coronariens aigus (SCA ST+ / SCA ST–)"),
            PlanSousPartie(lettre="B", titre="Infarctus du myocarde et types 1 à 5"),
        ]),
        PlanPartie(numero="II", titre="Épidémiologie & Physiopathologie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Épidémiologie des SCA"),
            PlanSousPartie(lettre="B", titre="Sténose athérothrombotique"),
            PlanSousPartie(lettre="C", titre="Ischémie myocardique aiguë"),
            PlanSousPartie(lettre="D", titre="Patient vulnérable et facteurs déclenchants"),
        ]),
        PlanPartie(numero="III", titre="Diagnostic clinique et différentiel", sous_parties=[
            PlanSousPartie(lettre="A", titre="Présentation clinique et terrain"),
            PlanSousPartie(lettre="B", titre="Examen physique"),
            PlanSousPartie(lettre="C", titre="Diagnostics différentiels"),
        ]),
        PlanPartie(numero="IV", titre="Examens complémentaires", sous_parties=[
            PlanSousPartie(lettre="A", titre="Électrocardiogramme (ECG)"),
            PlanSousPartie(lettre="B", titre="Troponine ultrasensible"),
            PlanSousPartie(lettre="C", titre="Autres biologies et échocardiographie"),
            PlanSousPartie(lettre="D", titre="MINOCA et étiologies particulières"),
        ]),
        PlanPartie(numero="V", titre="Stratégie de prise en charge et Traitement", sous_parties=[
            PlanSousPartie(lettre="A", titre="Stratégie générale et appel du Samu"),
            PlanSousPartie(lettre="B", titre="Traitement antithrombotique"),
            PlanSousPartie(lettre="C", titre="Médicaments symptomatiques et anti-ischémiques"),
            PlanSousPartie(lettre="D", titre="Revascularisation : angioplastie & pontage"),
        ]),
        PlanPartie(numero="VI", titre="Évolution et complications", sous_parties=[
            PlanSousPartie(lettre="A", titre="Unité de soins intensifs coronariens (Usic)"),
            PlanSousPartie(lettre="B", titre="Complications rythmiques et de conduction"),
            PlanSousPartie(lettre="C", titre="Complications hémodynamiques et mécaniques"),
            PlanSousPartie(lettre="D", titre="Complications thrombotiques et tardives"),
        ]),
        PlanPartie(numero="VII", titre="Prise en charge au long cours & Angor stable", sous_parties=[
            PlanSousPartie(lettre="A", titre="Traitement médicamenteux et suivi post-SCA"),
            PlanSousPartie(lettre="B", titre="Angor stable : diagnostic"),
            PlanSousPartie(lettre="C", titre="Angor stable : examens fonctionnels et anatomiques"),
            PlanSousPartie(lettre="D", titre="Angor stable : traitement et revascularisation"),
        ]),
    ]

    # ============================================================
    # PARTIE I — DÉFINITIONS
    # ============================================================
    partie_i = Partie(numero="I", titre="Définitions", sous_parties=[
        SousPartie(lettre="A", titre="Syndromes coronariens aigus (SCA ST+ / SCA ST–)", rows=[
            FicheRow(concept="◆ Définition générale du SCA", detail_md=(
                "- SCA : expression clinique variée d'une **ischémie myocardique aiguë**\n"
                "- À évoquer devant douleur thoracique aiguë (ou équivalent) en contexte prédisposant\n"
                "- **ECG dès le 1er contact** = pierre angulaire : distingue deux entités selon la présence ou non d'un sus-décalage persistant du segment ST\n"
                "  - SCA **ST+** (avec sus-décalage persistant)\n"
                "  - SCA **ST–** (sans sus-décalage persistant)"
            )),
            FicheRow(concept="★ ◆ SCA ST+ (IDM ST+ / STEMI)", detail_md=(
                "- Douleur thoracique persistante **> 30 min**\n"
                "- ECG : sus-décalage persistant du segment ST\n"
                "- Douleur et sus-décalage persistent après **trinitrine (TNT) sublinguale**\n"
                "- Mécanisme : **occlusion coronarienne aiguë** par thrombus fibrinocruorique → ischémie transmurale\n"
                "- Traitement : désobstruction immédiate de l'artère\n"
                "  - Mécanique : angioplastie primaire\n"
                "  - Médicamenteuse : fibrinolytique IV"
            )),
            FicheRow(concept="★ ◆ SCA ST– (IDM NST / NSTEMI ou angor instable)", detail_md=(
                "- Douleur thoracique spontanée ou pour efforts modérés, durée variable, souvent transitoire\n"
                "- ECG possible : sous-décalage transitoire ou persistant, anomalies de l'onde T, ou normal\n"
                "- Sus-décalage per-critique parfois identifié mais **régressif** spontanément ou sous TNT\n"
                "- **Troponine** :\n"
                "  - Élevée → **IDM NST (NSTEMI)**\n"
                "  - Non élevée → **angor instable**"
            )),
            FicheRow(concept="", detail_md=(
                "- **ECG dès le 1er contact** : seul examen permettant de séparer ST+ et ST– et de déclencher la stratégie de reperfusion\n"
                "- La **persistance après TNT** = thrombose occlusive (SCA ST+) ; la **régression** évoque un spasme (SCA ST–)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Infarctus du myocarde et classification en 5 types", rows=[
            FicheRow(concept="◆ Définition de l'IDM", detail_md=(
                "- Élévation de la **troponine ultrasensible** au-dessus du **99ᵉ percentile** de la limite supérieure de référence\n"
                "- + au moins un des éléments suivants :\n"
                "  - symptomatologie clinique d'ischémie myocardique aiguë ;\n"
                "  - anomalies de la repolarisation ou apparition d'une **onde Q** sur l'ECG ;\n"
                "  - perte de myocarde viable (IRM) dans un territoire à contractilité diminuée (échocardiographie) ;\n"
                "  - visualisation d'un **thrombus endoluminal** (coronarographie ou autopsie)."
            )),
            FicheRow(concept="◆ Cinq types d'IDM", detail_md=(
                "| Type | Mécanisme |\n"
                "|------|-----------|\n"
                "| **Type 1** | **Athérothrombotique** : rupture/ulcération/fissuration/érosion d'une plaque + thrombus (occlusif ou réducteur) ; lésion sous-jacente le plus souvent sévère mais **mineure dans 5-10 %** |\n"
                "| **Type 2** | **Hors instabilité athéromateuse** : déséquilibre apport/demande O₂ (HTA/hypoTA, tachy/bradycardie, arythmie, anémie, hypoxémie) ; spasme, dissection coronaire spontanée, embolie coronaire, dysfonction microvasculaire |\n"
                "| **Type 3** | IDM compliqué de **mort subite** lorsque le dosage de troponine n'est pas disponible |\n"
                "| **Type 4** | **Iatrogène** secondaire à une **angioplastie coronaire** |\n"
                "| **Type 5** | **Iatrogène** secondaire à un **pontage aortocoronarien** |"
            )),
            FicheRow(concept="", detail_md=(
                "- L'IDM **n'est PAS** synonyme de SCA ST+ : on peut avoir un IDM ST– (NSTEMI) ou un IDM de type 2 (déséquilibre apport/demande sans rupture de plaque)\n"
                "- Une élévation isolée de troponine **ne suffit pas** à porter le diagnostic d'IDM : un critère associé (clinique, ECG, imagerie, thrombus) est requis"
            ), kind="piege"),
        ]),
    ])

    # ============================================================
    # PARTIE II — ÉPIDÉMIOLOGIE & PHYSIOPATHOLOGIE
    # ============================================================
    partie_ii = Partie(numero="II", titre="Épidémiologie & Physiopathologie", sous_parties=[
        SousPartie(lettre="A", titre="Épidémiologie des SCA", rows=[
            FicheRow(concept="Incidence et fréquence", detail_md=(
                "- Incidence européenne des SCA (ST+ et ST–) : ~ **293 / 100 000 hab** (IC 95 % : 196-530)\n"
                "- IDM ST+ : incidence entre **43 et 144 / 100 000 / an**\n"
                "- France : > **60 000 hospitalisations / an** pour IDM\n"
                "- Tendance : incidence du SCA ST+ en décroissance, celle du SCA ST– en augmentation (en partie grâce à la Tn-us)"
            )),
            FicheRow(concept="Terrain et mortalité", detail_md=(
                "- IDM ST+ : plus fréquent chez les sujets jeunes et chez les hommes\n"
                "- Mortalité hospitalière de l'IDM ST+ : **4-12 % en Europe** ; **~ 10 % à 1 an**\n"
                "- Facteurs de surmortalité : âge avancé, diabète, insuffisance rénale, insuffisance cardiaque, antécédent d'IDM, altération de la FEVG, atteinte coronaire diffuse, prise en charge tardive"
            )),
            FicheRow(concept="Particularités de la femme", detail_md=(
                "- Maladie coronarienne se développe avec **7 à 10 ans de retard** vs homme\n"
                "- Cause fréquente de décès dans cette population\n"
                "- SCA 4 fois plus fréquents chez l'homme avant 60 ans, mais plus fréquents chez la femme après 75 ans\n"
                "- Symptomatologie plus souvent atypique, hospitalisation plus tardive\n"
                "- Prise en charge identique dans les deux sexes (malgré une majoration potentielle des risques iatrogènes chez la femme)"
            )),
        ]),
        SousPartie(lettre="B", titre="Sténose athérothrombotique", rows=[
            FicheRow(concept="Plaque d'athérome vulnérable", detail_md=(
                "- Composition : cœur lipidique nécrotique (avec cellules musculaires lisses migrées de la média + cellules inflammatoires) entouré d'une chape fibreuse de collagène I\n"
                "- **Plaque vulnérable** = cœur lipidique important + chape fibreuse fine\n"
                "- La plaque peut se rompre (rupture) ou se fissurer (érosion) → formation d'un thrombus au contact"
            )),
            FicheRow(concept="Thrombus blanc vs thrombus rouge", detail_md=(
                "| Caractère | Thrombus blanc | Thrombus rouge |\n"
                "|-----------|----------------|----------------|\n"
                "| Composition | Riche en plaquettes | Fibrinocruorique |\n"
                "| Taille | Petit | Volumineux |\n"
                "| Occlusif | Non | Oui |\n"
                "| SCA associé | **SCA ST–** | **SCA ST+** |"
            )),
            FicheRow(concept="Dynamique du thrombus", detail_md=(
                "- Peut régresser sous l'effet d'une fibrinolyse physiologique puis réapparaître\n"
                "- Peut se fragmenter et migrer en aval (embolies dans artérioles et capillaires distaux)\n"
                "- Embolies → nécrose de petits territoires myocardiques → élévation de la troponine"
            )),
        ]),
        SousPartie(lettre="C", titre="Ischémie myocardique aiguë", rows=[
            FicheRow(concept="Déséquilibre apport/demande O₂", detail_md=(
                "- Ischémie aiguë = apports insuffisants face à la demande en oxygène du myocarde\n"
                "- Sténose athérothrombotique = diminution brutale des apports\n"
                "- Sténose dynamique : libération par les plaquettes activées de **sérotonine, thromboxane A2, ADP** → vasoconstriction et majorations paroxystiques\n"
                "- D'où la possibilité d'épisodes ischémiques transitoires"
            )),
            FicheRow(concept="Occlusion aiguë totale", detail_md=(
                "- Occlusion coronarienne totale → ischémie transmurale = sus-décalage de ST à l'ECG\n"
                "- Si vasoconstrictrice (spasme) → régression rapide spontanée ou sous TNT (**angor de Prinzmetal**, SCA ST–)\n"
                "- Si thrombotique occlusive → persistance malgré la TNT = **SCA ST+ (IDM ST+)**"
            )),
        ]),
        SousPartie(lettre="D", titre="Patient vulnérable et facteurs déclenchants", rows=[
            FicheRow(concept="Vulnérabilité artérielle diffuse", detail_md=(
                "- L'instabilité n'est **PAS limitée à la plaque rompue** : elle touche l'ensemble de l'arbre artériel\n"
                "- Justifie un traitement médicamenteux multifocal (ex : **aspirine**)\n"
                "- Facteurs de vulnérabilité majeurs : hypercholestérolémie, tabagisme, hyperfibrinémie"
            )),
            FicheRow(concept="Facteurs déclenchants", detail_md=(
                "- Exercice physique violent\n"
                "- Manque de sommeil\n"
                "- Excès alimentaire\n"
                "- Infection aiguë"
            )),
            FicheRow(concept="", detail_md=(
                "- Athérosclérose : **maladie chronique diffuse** des moyennes (coronaires) et grosses (aorte) artères → l'**aspirine** agit de manière multifocale"
            ), kind="a_retenir"),
        ]),
    ])

    # ============================================================
    # PARTIE III — DIAGNOSTIC CLINIQUE ET DIFFÉRENTIEL
    # ============================================================
    partie_iii = Partie(numero="III", titre="Diagnostic clinique et différentiel", sous_parties=[
        SousPartie(lettre="A", titre="Présentation clinique et terrain", rows=[
            FicheRow(concept="◆ Douleur angineuse typique", detail_md=(
                "- Siège : **rétrosternale en barre**\n"
                "- Caractère : **constrictive**\n"
                "- Irradiations : bras gauche, deux bras ou bras droit, cou, mâchoire\n"
                "- Durée : intermittente brève (quelques minutes), prolongée ou persistante\n"
                "- Signes associés : sudation, nausées, gêne épigastrique, dyspnée, malaise lipothymique, syncope\n"
                "- Régression sous TNT sublinguale = évocatrice (uniquement SCA ST–) mais non spécifique"
            )),
            FicheRow(concept="Présentation atypique", detail_md=(
                "- Siège atypique : épigastrique, simulant une indigestion ; ou absente\n"
                "- Limitée aux irradiations (bras, mâchoire)\n"
                "- Caractère atypique : brûlure thoracique, faible intensité\n"
                "- Forme dyspnée isolée ou asthénie\n"
                "- Plus fréquente chez : patients âgés, femmes, diabétiques, insuffisants rénaux, déments"
            )),
            FicheRow(concept="★ ◆ Critères cliniques évoquant un SCA ST+", detail_md=(
                "- Douleur angineuse **persistante > 30 min**\n"
                "- **Non résolutive après TNT sublinguale**\n"
                "- → Diagnostic immédiatement confirmé par ECG (12 ou 18 dérivations) montrant le sus-décalage de ST"
            )),
            FicheRow(concept="★ ◆ Critères cliniques évoquant un SCA ST–", detail_md=(
                "(en l'absence de sus-décalage persistant)\n"
                "- Douleur thoracique spontanée prolongée **> 20 min**\n"
                "- Angor inaugural récent (< 1 mois) survenant à l'effort pour des efforts modérés (**CCS II ou III**)\n"
                "- Aggravation récente d'un angor d'effort (= **angor crescendo**)\n"
                "- Apparition d'un angor au décours d'un IDM"
            )),
            FicheRow(concept="Facteurs de risque cardiovasculaire", detail_md=(
                "- Âge avancé, sexe masculin\n"
                "- Tabagisme\n"
                "- Hérédité coronarienne\n"
                "- Diabète\n"
                "- Dyslipidémie\n"
                "- HTA\n"
                "- Insuffisance rénale chronique\n"
                "- Antécédents : coronaropathie, AOMI, atteinte des troncs supra-aortiques"
            )),
            FicheRow(concept="Facteurs favorisant la déstabilisation", detail_md=(
                "- Anémie, infection, syndrome inflammatoire\n"
                "- Hyperthermie, poussée hypertensive\n"
                "- Accès de colère, émotion forte, exercice violent\n"
                "- Dérèglement métabolique/endocrine : hyperthyroïdie\n"
                "- Anesthésie générale, chirurgie"
            )),
        ]),
        SousPartie(lettre="B", titre="Examen physique", rows=[
            FicheRow(concept="Examen physique en l'absence de complication", detail_md=(
                "- Habituellement sans particularité\n"
                "- À rechercher :\n"
                "  - signes d'insuffisance cardiaque congestive\n"
                "  - souffle systolique (complication mécanique)\n"
                "- **Mesure de la PA aux deux bras** systématique : asymétrie évoque une **dissection aortique**\n"
                "- Recherche de FRCV (PA, poids) et autres localisations athéromateuses (palpation/auscultation artérielles)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Une **asymétrie tensionnelle** aux deux bras dans un contexte de douleur thoracique aiguë doit faire évoquer une **dissection aortique** en premier lieu (CI absolue à la fibrinolyse)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Diagnostics différentiels", rows=[
            FicheRow(concept="Prévalences dans un SAU (douleur thoracique non sélectionnée)", detail_md=(
                "| Affection | Prévalence |\n"
                "|-----------|------------|\n"
                "| IDM ST+ | **5-10 %** |\n"
                "| IDM ST– | **15-20 %** |\n"
                "| Angor instable | **10 %** |\n"
                "| Autres affections cardiaques | **15 %** |\n"
                "| Affections **non cardiaques** | **50 %** |"
            )),
            FicheRow(concept="Diagnostics différentiels cardiovasculaires", detail_md=(
                "- **Dissection aortique**\n"
                "- **Embolie pulmonaire**\n"
                "- Myocardite / péricardite\n"
                "- Syndrome de **takotsubo** (sus-décalage du segment ST parfois absent)"
            )),
            FicheRow(concept="Diagnostics différentiels extracardiaques", detail_md=(
                "- Pneumothorax, pleurésie\n"
                "- Pneumopathie\n"
                "- Fracture de côte\n"
                "- Douleurs articulaires/musculaires bénignes\n"
                "- Pancréatite, cholécystite\n"
                "- Gastrite, œsophagite, reflux gastro-œsophagien"
            )),
            FicheRow(concept="MINOCA", detail_md=(
                "- **Myocardial Infarction with NonObstructive Coronary Arteries**\n"
                "- = IDM authentique + absence de lésion obstructive > 50 % à la coronarographie/coroscanner\n"
                "- Critères : IDM (troponine + symptômes/ECG) + pas de sténose > 50 % et pas d'autre diagnostic\n"
                "- **~ 6 % des SCA**\n"
                "- Plus fréquente en SCA ST–, patients plus jeunes, ~ 40 % de femmes\n"
                "- **IRM** et **imagerie endocoronarienne** = clés du diagnostic étiologique"
            )),
            FicheRow(concept="Étiologies de MINOCA — causes coronariennes", detail_md=(
                "- Plaque vulnérable rompue/fissurée mineure → identifiée par échographie endocoronarienne (prise en charge = SCA)\n"
                "- **Spasme coronarien** :\n"
                "  - sténose disparaissant après dérivé nitré, ou démasquée par injection de **Méthergin® (méthylergométrine)**\n"
                "  - spasme occlusif → sus-décalage régressif après TNT ; spasme non occlusif → sous-décalage ST ou T négatives\n"
                "  - contexte : migraine, phénomène de Raynaud, épisodes spontanés répétés (angor spastique de Prinzmetal)\n"
                "- **Dissection coronarienne spontanée** : touche plus volontiers les femmes, physiopathologie mal connue\n"
                "- **Embolie coronarienne** : FA (thrombus) ou endocardite infectieuse (végétation)"
            )),
            FicheRow(concept="Étiologies de MINOCA — causes non coronariennes", detail_md=(
                "- Myocardite\n"
                "- Takotsubo\n"
                "- Cardiomyopathies (notamment hypertrophiques)\n"
                "- Traumatisme\n"
                "- Embolie pulmonaire\n"
                "- Causes médicamenteuses"
            )),
        ]),
    ])

    # ============================================================
    # PARTIE IV — EXAMENS COMPLÉMENTAIRES
    # ============================================================
    partie_iv = Partie(numero="IV", titre="Examens complémentaires", sous_parties=[
        SousPartie(lettre="A", titre="Électrocardiogramme (ECG)", rows=[
            FicheRow(concept="◆ Délais de réalisation", detail_md=(
                "- ECG 12 dérivations sans délai dès lors que le diagnostic de SCA est suspecté\n"
                "  - au domicile si appel au **centre 15** ;\n"
                "  - dans les **10 minutes** suivant l'admission au SAU si arrivée spontanée\n"
                "- Intérêt diagnostique + détection d'arythmies ventriculaires (risque de dégradation en TV/FV)"
            )),
            FicheRow(concept="◆ Critères de sus-décalage du segment ST", detail_md=(
                "- Dans **≥ 2 dérivations contiguës**\n"
                "- **Onde de Pardee** : sus-décalage convexe vers le haut\n"
                "- Seuils :\n"
                "  - **≥ 2 mm** en V2-V3 chez l'homme\n"
                "  - **≥ 2,5 mm** en V2-V3 chez l'homme < 40 ans\n"
                "  - **≥ 1,5 mm** en V2-V3 chez la femme\n"
                "  - **≥ 1 mm** dans les autres dérivations\n"
                "- En l'absence de **BBG** ou d'**HVG**\n"
                "- Associé à un **miroir** (sous-décalage dans les dérivations opposées)\n"
                "- Apparition d'une **onde Q de nécrose** classiquement à partir de la **6ᵉ heure**"
            )),
            FicheRow(concept="★ ◆ Localisation de la nécrose selon l'ECG", detail_md=(
                "| Dérivations | Territoire |\n"
                "|-------------|------------|\n"
                "| **D1-aVL** | **Latéral haut** |\n"
                "| **D2-D3-aVF** | **Inférieur** |\n"
                "| **V1-V2-V3** | **Antéroseptal** |\n"
                "| **V4** | **Apical** |\n"
                "| **V5-V6** | **Latéral bas** |\n"
                "| **V1-V6** | **Antérieur étendu** |\n"
                "| **V7-V8-V9** | **Postérieur** |"
            )),
            FicheRow(concept="★ ◆ Extensions à rechercher", detail_md=(
                "- IDM inférieur (D2-D3-aVF) → rechercher **extension au VD** par **V3R-V4R** (dérivations droites)\n"
                "- Sous-décalage en V1-V3 chez patient symptomatique → enregistrer **V7-V8-V9** : un sus-décalage **≥ 0,5 mm** y confirme un **IDM postérieur** (le sous-décalage antérieur étant une image en miroir)"
            )),
            FicheRow(concept="Blocs de branche et stimulation ventriculaire (SCA ST+)", detail_md=(
                "- **BBG** : si suspicion clinique forte (angor persistant) = **équivalent de sus-décalage de ST**, qu'il soit récent ou non\n"
                "  - BBG supposé récent chez patient asymptomatique lors de l'enregistrement = aucune valeur diagnostique\n"
                "- **BBD** : marqueur de mauvais pronostic (souvent lié à atteinte antérieure) = également équivalent de sus-décalage\n"
                "- Stimulation ventriculaire (pacemaker) : ne permet pas d'identifier un sus-décalage de ST"
            )),
            FicheRow(concept="ECG dans le SCA ST–", detail_md=(
                "- ECG post-critique normal chez **> 30 % des SCA ST–** → un ECG normal n'élimine PAS un SCA\n"
                "- Anomalies en faveur :\n"
                "  - sous-décalage du segment ST\n"
                "  - sus-décalage transitoire\n"
                "  - anomalies de l'onde T (T négatives)\n"
                "- Renouveler l'ECG si premier normal (troubles parfois retardés)\n"
                "- Comparaison avec un tracé antérieur = aide précieuse\n"
                "- ECG systématiquement renouvelé **1 à 2 h** plus tard ou en cas de récidive douloureuse"
            )),
            FicheRow(concept="Blocs de branche (SCA ST–)", detail_md=(
                "- BBG asymptomatique = sans valeur diagnostique\n"
                "- BBD chez patient symptomatique : sous-décalage de ST en D1-VL et V5-V6 = en faveur d'un SCA ST–\n"
                "- Près de **50 %** des patients avec bloc de branche hospitalisés pour douleur thoracique suspecte ont en réalité un SCA\n"
                "- Stimulation ventriculaire : ECG non contributif"
            )),
            FicheRow(concept="", detail_md=(
                "- ECG non contributif + clinique fortement évocatrice (angor persistant) = **coronarographie sans délai**, sans attendre la troponine"
            ), kind="a_retenir"),
            FicheRow(concept="", detail_md=(
                "- ⚠ Un **ECG normal n'élimine PAS un SCA ST–** (> 30 % des cas) → renouveler l'ECG et doser la troponine"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Troponine ultrasensible (Tn-us)", rows=[
            FicheRow(concept="★ ◆ Indications et rôle", detail_md=(
                "- **Marqueur essentiel** pour confirmer un IDM et démarche diagnostique du SCA ST–\n"
                "- SCA ST+ : pas de place dans la stratégie initiale → on **n'attend PAS le résultat** pour la prise en charge ; le dosage confirme a posteriori le diagnostic d'IDM\n"
                "- Plus sensible et spécifique que CK, CK-MB ou myoglobine pour une lésion myocytaire\n"
                "- Élévation précoce par rapport au début des symptômes (dans l'heure)"
            )),
            FicheRow(concept="Cinétique de la Tn-us", detail_md=(
                "- Croît rapidement dans l'heure suivant la douleur\n"
                "- Reste élevée plusieurs jours\n"
                "- Sensibilité élevée mais spécificité limitée"
            )),
            FicheRow(concept="Causes d'élévation de troponine hors SCA", detail_md=(
                "- Tachyarythmie\n"
                "- Insuffisance cardiaque\n"
                "- Poussée hypertensive\n"
                "- Urgence vitale\n"
                "- Myocardite\n"
                "- Valvulopathie\n"
                "- Embolie pulmonaire\n"
                "- Dissection aortique\n"
                "- Takotsubo"
            )),
            FicheRow(concept="Facteurs influençant la troponine", detail_md=(
                "- Âge (élévation avec l'âge)\n"
                "- Insuffisance rénale\n"
                "- Délai dosage / début symptômes\n"
                "- Sexe"
            )),
            FicheRow(concept="◆ Algorithme rule-in / rule-out (IDM ST–)", detail_md=(
                "- Repose sur le type de Tn-us (I ou T) et le fabricant, le délai début / dosage et l'évolution à 1-2 h\n"
                "- **Rule-in (SCA très probable)** : valeur initiale très élevée OU augmentation significative au 2ᵉ prélèvement\n"
                "- **Rule-out (SCA très peu probable)** : valeur initiale très basse et pas d'augmentation au 2ᵉ dosage\n"
                "- Zones intermédiaires : investigations complémentaires nécessaires"
            )),
            FicheRow(concept="Autres biomarqueurs (marginaux)", detail_md=(
                "- **Copeptine** : peu spécifique\n"
                "- **CK-MB** : sensibilité insuffisante pour diagnostic précoce ; décroissance plus rapide que la troponine → utile pour suspecter une récidive d'IDM par réascension\n"
                "- **BNP** : marqueur d'IVG → valeur pronostique uniquement"
            )),
        ]),
        SousPartie(lettre="C", titre="Autres biologies et échocardiographie", rows=[
            FicheRow(concept="Bilan biologique de base", detail_md=(
                "- Glycémie\n"
                "- Bilan lipidique\n"
                "- Créatininémie\n"
                "- NFS\n"
                "- → Identifie le terrain à risque et conditionne la prescription d'examens et de traitements"
            )),
            FicheRow(concept="Échocardiographie transthoracique (ETT)", detail_md=(
                "- SCA ST+ : ne doit **PAS retarder** la prise en charge ; indiquée si complication mécanique suspectée\n"
                "- SCA ST– : largement indiquée, participe au diagnostic différentiel\n"
                "- Apporte :\n"
                "  - troubles de la cinétique segmentaire (hypokinésie, akinésie, dyskinésie)\n"
                "  - évaluation de la **FEVG** (paramètre pronostique)"
            )),
        ]),
        SousPartie(lettre="D", titre="MINOCA et étiologies particulières", rows=[
            FicheRow(concept="Définition rappel MINOCA", detail_md=(
                "- IDM (troponine + clinique/ECG) + coronaires non obstructives (< 50 %) + pas d'autre diagnostic différentiel\n"
                "- **~ 6 %** des SCA\n"
                "- Plus fréquent dans le SCA ST–, patients jeunes, ~ 40 % de femmes"
            )),
            FicheRow(concept="Spasme coronarien (angor de Prinzmetal)", detail_md=(
                "- **Spasme occlusif** : sus-décalage régressif avec la douleur après TNT sublinguale\n"
                "- **Spasme non occlusif** : sous-décalage ST ou ondes T négatives modérées\n"
                "- Diagnostic en coronarographie : sténose disparaissant après dérivés nitrés OU démasquée par injection IV/intracoronaire de **Méthergin®**\n"
                "- Mécanismes :\n"
                "  - Hyperactivité plaquettaire secondaire à rupture/fissuration d'une plaque\n"
                "  - Dysfonction endothéliale (angor spastique « pur ») : pas d'élévation de troponine si pas de thrombose associée\n"
                "- Contextes évocateurs : migraine, phénomène de Raynaud, épisodes spontanés répétés"
            )),
            FicheRow(concept="Dissection coronarienne spontanée", detail_md=(
                "- Touche plus volontiers les femmes\n"
                "- Physiopathologie mal connue\n"
                "- Diagnostic évoqué par aspect « inhabituel » de la lésion en coronarographie\n"
                "- Imagerie endocoronarienne peut confirmer"
            )),
            FicheRow(concept="Embolie coronarienne", detail_md=(
                "- Fibrillation atriale (thrombus auriculaire) → embolie\n"
                "- Endocardite infectieuse (végétation) → embolie"
            )),
        ]),
    ])

    # ============================================================
    # PARTIE V — STRATÉGIE DE PRISE EN CHARGE ET TRAITEMENT
    # ============================================================
    partie_v = Partie(numero="V", titre="Stratégie de prise en charge et Traitement", sous_parties=[
        SousPartie(lettre="A", titre="Stratégie générale et appel du Samu", rows=[
            FicheRow(concept="◆ Appel au Samu = règle absolue", detail_md=(
                "- Toute douleur thoracique aiguë → appel **immédiat du 15 (Samu)**\n"
                "- → envoi d'un **Smur** permettant ECG rapide et organisation de la prise en charge\n"
                "- Tout autre intervenant en 1ʳᵉ intention est à proscrire (retard diagnostique et thérapeutique)\n"
                "- Si arrivée spontanée au SAU : ECG **dans les 10 minutes** suivant l'admission"
            )),
            FicheRow(concept="★ ◆ Stratégie de reperfusion du SCA ST+", detail_md=(
                "- **Angioplastie primaire** (intervention coronaire percutanée) privilégiée si possible **dans les 120 min**\n"
                "- Sinon fibrinolyse IV + transfert vers centre de cathétérisme pour angioplastie de sauvetage si la fibrinolyse échoue\n"
                "- Bénéfice = précocité : limitation de la taille de l'IDM et réduction de la mortalité\n"
                "  - Au-delà de la **12ᵉ heure** : bénéfice faible\n"
                "  - Au-delà de la **24ᵉ heure** : bénéfice **nul**"
            )),
            FicheRow(concept="◆ Contre-indications absolues à la fibrinolyse", detail_md=(
                "- Antécédent d'**AVC hémorragique**\n"
                "- Antécédent d'**AVC < 6 mois**\n"
                "- Malformation artério-veineuse ou tumeur cérébrale\n"
                "- Traumatisme cérébral **< 1 mois**\n"
                "- Hémorragie digestive récente (**< 1 mois**)\n"
                "- **Dissection aortique**\n"
                "- Ponction/biopsie hépatique ou rénale, ponction lombaire récente (< 24 h)\n"
                "- Anomalies connues de l'hémostase prédisposant aux saignements"
            )),
            FicheRow(concept="★ ◆ Stratégie du SCA ST–", detail_md=(
                "- Stratégie invasive recommandée, délai de coronarographie selon gravité\n"
                "- **Facteurs de très haut risque (coronarographie < 2 h)** :\n"
                "  - instabilité hémodynamique, hypoTA, tachycardie, **choc cardiogénique**\n"
                "  - douleur persistante ou récurrente sous traitement\n"
                "  - insuffisance cardiaque\n"
                "  - TV/FV ou arrêt cardiaque\n"
                "  - complication mécanique\n"
                "  - variation dynamique de l'ECG\n"
                "- **Facteurs de haut risque (coronarographie < 24 h)** :\n"
                "  - IDM ST– confirmé par ECG ou troponine\n"
                "  - **Score GRACE > 140** (peu utilisé en France)\n"
                "  - Sus-décalage de ST transitoire\n"
                "  - Sous-décalage dynamique ou négativation des ondes T\n"
                "- Autres cas : choix entre stratégie invasive et tests non invasifs selon les habitudes locales"
            )),
        ]),
        SousPartie(lettre="B", titre="Traitement antithrombotique", rows=[
            FicheRow(concept="◆ Trithérapie de référence", detail_md=(
                "- Association **aspirine + inhibiteur P2Y12 + anticoagulant** en l'absence de CI hémorragique\n"
                "- Modalités diffèrent selon SCA ST+ vs ST– et risques hémorragique / ischémique"
            )),
            FicheRow(concept="Facteurs de risque hémorragique", detail_md=(
                "- Âge **> 75 ans**\n"
                "- Sexe féminin\n"
                "- Insuffisance rénale\n"
                "- Diathèse hémorragique\n"
                "- AVC ancien\n"
                "- Poids **< 65 kg**\n"
                "- Chirurgie/traumatisme sévère récent\n"
                "- Pas de score validé → évaluation empirique"
            )),
            FicheRow(concept="◆ Aspirine (inhibiteur du thromboxane A2)", detail_md=(
                "- Dose de charge : **250 mg IVD**\n"
                "- Entretien : **75-100 mg/j** per os\n"
                "- Associée à un inhibiteur de la pompe à protons (oméprazole)"
            )),
            FicheRow(concept="★ ◆ Inhibiteurs des récepteurs P2Y12", detail_md=(
                "| Molécule | Charge | Entretien | Commentaire |\n"
                "|----------|--------|-----------|-------------|\n"
                "| **Clopidogrel (Plavix®)** | **600 mg po** | **75 mg/j** | Si prasugrel/ticagrélor CI ; **moins efficace**, délai d'action **plus long** |\n"
                "| **Prasugrel (Efient®)** | **60 mg po** | **10 mg/j** | **CI si ATCD d'AVC** ; non recommandé si > 75 ans et/ou < 60 kg |\n"
                "| **Ticagrélor (Brilique®)** | **180 mg po** | **90 mg ×2/j** | Peut induire **bradycardie** et **dyspnée** réversibles |"
            )),
            FicheRow(concept="Stratégie antiplaquettaire dans le SCA ST+", detail_md=(
                "- Angioplastie primaire : aspirine + **prasugrel** OU **ticagrélor** en 1ʳᵉ intention\n"
                "- Si CI au prasugrel/ticagrélor ou patient à risque hémorragique : **clopidogrel**\n"
                "- Fibrinolyse : aspirine d'emblée ; **clopidogrel = seul** P2Y12 autorisé en association\n"
                "  - Charge **300 mg** uniquement chez patients < 75 ans"
            )),
            FicheRow(concept="Stratégie antiplaquettaire dans le SCA ST–", detail_md=(
                "- **PLUS de bithérapie dès l'admission** en Usic tant que la coronarographie n'est pas faite (risque hémorragique majoré)\n"
                "- Bithérapie indiquée secondairement après angioplastie selon les mêmes modalités que le ST+\n"
                "- Bithérapie pré-coronarographie possible si délai > 24 h avant la coronarographie"
            )),
            FicheRow(concept="★ ◆ Anticoagulants", detail_md=(
                "- Angioplastie immédiate (SCA ST+ ou ST– à très haut risque) :\n"
                "  - **HNF 70-100 UI/kg IVD**\n"
                "  - OU **énoxaparine 0,5 mg/kg IVD**\n"
                "  - Arrêt après revascularisation\n"
                "- SCA ST– à haut risque :\n"
                "  - **Énoxaparine (Lovenox®) 1 mg/kg SC x2/j**\n"
                "  - OU **fondaparinux (Arixtra®) 2,5 mg/j SC** + bolus d'HNF lors de la coronarographie\n"
                "  - HNF IVSE (400-600 UI/kg/24 h) rarement : si CI aux HBPM/fondaparinux (IRC sévère)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ En SCA ST– : **ne PAS prescrire** de bithérapie antiplaquettaire dès l'admission si la coronarographie est prévue rapidement (risque hémorragique accru démontré)"
            ), kind="piege"),
            FicheRow(concept="", detail_md=(
                "- **Prasugrel** : CI absolue si ATCD d'AVC ; **ticagrélor** : penser à la bradycardie/dyspnée réversibles ; **clopidogrel** : seul autorisé avec la **fibrinolyse**"
            ), kind="mnemo"),
        ]),
        SousPartie(lettre="C", titre="Médicaments symptomatiques et anti-ischémiques", rows=[
            FicheRow(concept="Antalgiques et anxiolytiques", detail_md=(
                "- Antalgique : **chlorhydrate de morphine** si douleur invalidante persistante\n"
                "- Anxiolytique : **benzodiazépine** à doses adaptées"
            )),
            FicheRow(concept="◆ Oxygénothérapie", detail_md=(
                "- Réservée aux hypoxémiques : **SaO₂ < 90 %** ou **PaO₂ < 60 mmHg**\n"
                "- L'**hyperoxie peut être délétère**"
            )),
            FicheRow(concept="Dérivés nitrés", detail_md=(
                "- IV (**dinitrate d'isosorbide 2 mg/h**) :\n"
                "  - antalgique dans le SCA ST–\n"
                "  - antihypertenseur\n"
                "  - traitement d'une IVG congestive\n"
                "- Dose adaptée à la PA"
            )),
            FicheRow(concept="Bêtabloquants", detail_md=(
                "- Diminuent la consommation O₂ : bradycardisants, hypotenseurs, inotropes négatifs\n"
                "- Largement prescrits à la phase aiguë\n"
                "- Poursuite systématique remise en cause chez patient asymptomatique avec FEVG préservée\n"
                "- Indications fermes au long cours : angor résiduel et/ou **FEVG abaissée**"
            )),
            FicheRow(concept="", detail_md=(
                "- L'**hyperoxie** chez un patient non hypoxémique est délétère : l'oxygène n'est pas systématique dans le SCA"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Revascularisation : angioplastie & pontage", rows=[
            FicheRow(concept="◆ Coronarographie et angioplastie coronarienne", detail_md=(
                "- Cathéter introduit par voie radiale (préférée) ou fémorale jusqu'à l'ostium coronaire\n"
                "- Injection de produit de contraste iodé\n"
                "- Angioplastie : franchissement de la lésion par un guide, ballonnet ± **stent**\n"
                "- HNF/HBPM durant la procédure pour prévenir la thrombose du cathéter\n"
                "- **Voie radiale préférée** : risque hémorragique nettement plus faible"
            )),
            FicheRow(concept="Durée de la bithérapie antiagrégante post-angioplastie", detail_md=(
                "- SCA + angioplastie : **12 mois** (réductible/augmentable selon risques ischémique/hémorragique)\n"
                "- Angor stable + stent : habituellement **6 mois**"
            )),
            FicheRow(concept="Revascularisation chirurgicale : pontage coronarien", detail_md=(
                "- Sternotomie sous anesthésie générale\n"
                "- Cœur arrêté, circulation extracorporelle habituelle\n"
                "- Greffon **artériel préférentiel** : artères mammaires (subclavières)\n"
                "- Greffon veineux possible : veine saphène (mollet)\n"
                "- Greffon suturé en aval de la lésion + sur aorte ascendante si veineux\n"
                "- Lésions coronariennes non abordées : le pontage contourne la sténose"
            )),
            FicheRow(concept="◆ Choix de la stratégie de revascularisation", detail_md=(
                "- **SCA ST+** : angioplastie à la phase aiguë de la lésion coupable, puis revascularisation systématique des autres lésions significatives pluritronculaires (recommandation actuelle)\n"
                "- **SCA ST–** : angioplastie OU pontage selon siège, étendue, âge, comorbidités, risque opératoire\n"
                "- **Pontage privilégié** :\n"
                "  - lésions du tronc coronaire gauche\n"
                "  - tritronculaires complexes\n"
                "  - notamment diabétique (si terrain le permet)"
            )),
            FicheRow(concept="", detail_md=(
                "- **Angioplastie primaire dans les 120 min** est supérieure à la fibrinolyse (SCA ST+) ; si délai > 120 min impossible → **fibrinolyse** puis transfert + angioplastie de sauvetage si échec"
            ), kind="a_retenir"),
        ]),
    ])

    # ============================================================
    # PARTIE VI — ÉVOLUTION ET COMPLICATIONS
    # ============================================================
    partie_vi = Partie(numero="VI", titre="Évolution et complications", sous_parties=[
        SousPartie(lettre="A", titre="Unité de soins intensifs coronariens (Usic)", rows=[
            FicheRow(concept="Organisation et surveillance", detail_md=(
                "- **Monitorage ECG continu**\n"
                "- Surveillance :\n"
                "  - clinique : PA et auscultation cardiopulmonaire biquotidienne\n"
                "  - ECG 12 dérivations biquotidien et à chaque récidive douloureuse\n"
                "  - biologique : troponine, glycémie, créatininémie, NFS quotidiennes\n"
                "  - échocardiographique : ETT le jour de l'admission puis selon évolution"
            )),
            FicheRow(concept="Critères d'admission", detail_md=(
                "- SCA ST+ : admission après revascularisation, depuis la salle de coronarographie où ils sont dirigés directement par le Smur\n"
                "- SCA ST– : habituellement admis en USI ; unité « douleur thoracique » (UDT) pour les SCA ST– non compliqués / à bas risque\n"
                "- Complication → transfert en Usic"
            )),
            FicheRow(concept="Durée d'hospitalisation", detail_md=(
                "- SCA ST– : retour à domicile/chambre conventionnelle dès le lendemain de la coronarographie, **sortie 24-48 h** après revascularisation (si pas de complication)\n"
                "- SCA ST+ : sortie entre le **3ᵉ et le 5ᵉ jour** selon évolution ; transfert possible en centre de réadaptation cardiovasculaire"
            )),
        ]),
        SousPartie(lettre="B", titre="Complications rythmiques et de conduction", rows=[
            FicheRow(concept="◆ Troubles du rythme ventriculaire", detail_md=(
                "- Très fréquents, indépendants de l'étendue de la nécrose\n"
                "- Par gravité croissante : ESV → TV non soutenue → TV soutenue → **FV**\n"
                "- **FV** : responsable de la plupart des morts subites\n"
                "  - peut survenir d'emblée (mort subite préhospitalière)\n"
                "  - **JAMAIS réversible spontanément** → **choc électrique externe immédiat**"
            )),
            FicheRow(concept="Troubles du rythme supraventriculaire", detail_md=(
                "- Plus rares\n"
                "- **FA** : peut induire une décompensation hémodynamique (→ cardioversion électrique) ou des accidents thromboemboliques (AVC ischémique au 1er plan) → **anticoagulation**"
            )),
            FicheRow(concept="◆ Troubles de la conduction", detail_md=(
                "| Type | Topographie typique | Réponse à l'atropine | Conduite |\n"
                "|------|--------------------|----------------------|----------|\n"
                "| **BAV nodal** | SCA ST+ inférieur | Oui | Habituellement transitoire |\n"
                "| **BAV infranodal (hissien)** | SCA ST+ antérieur (nécrose étendue) | Non | Sonde d'entraînement / pacemaker ; souvent définitif → **pacemaker permanent** |\n"
                "| **Hypertonie vagale** | SCA ST+ inférieur | Oui + remplissage | Bradycardie/hypoTA |"
            )),
        ]),
        SousPartie(lettre="C", titre="Complications hémodynamiques et mécaniques", rows=[
            FicheRow(concept="◆ Insuffisance ventriculaire gauche (IVG)", detail_md=(
                "- Conséquence de l'étendue de la nécrose, favorisée par une arythmie OU traduit une complication mécanique (à rechercher systématiquement par échographie)\n"
                "- Traitement : **diurétiques + IEC + inhibiteurs des récepteurs aux minéralocorticoïdes**\n"
                "- Sévérité = **classification de Killip** (tableau 5.1)"
            )),
            FicheRow(concept="◆ Classification de Killip", detail_md=(
                "| Stade | Description |\n"
                "|-------|-------------|\n"
                "| **1** | Absence de râles crépitants |\n"
                "| **2** | Râles crépitants aux bases (≤ moitié des champs pulmonaires) |\n"
                "| **3** | Râles dépassant la moitié (OAP), **galop** |\n"
                "| **4** | **Choc cardiogénique** |"
            )),
            FicheRow(concept="◆ Choc cardiogénique", detail_md=(
                "- Habituellement associé à une nécrose étendue (antérieure ou récidive)\n"
                "- Coronarographie : occlusion proximale de l'**IVA** et/ou lésions pluritronculaires ± tronc commun\n"
                "- Peut être inaugural ou progressif (24-48 h), précédé d'un préchoc : **PAS < 90 mmHg** mal tolérée, ne répondant pas au remplissage\n"
                "- Stade constitué : signes d'hypoperfusion (extrémités froides, oligurie, confusion)\n"
                "- Traitement : **inotropes positifs (dobutamine)** + envisager une assistance circulatoire\n"
                "- Pronostic sombre : **mortalité > 70 %**"
            )),
            FicheRow(concept="◆ Infarctus du ventricule droit (VD)", detail_md=(
                "- Complique classiquement les **IDM inférieurs**\n"
                "- Peut prendre le masque d'un choc cardiogénique mais traitement différent\n"
                "- Triade classique : **hypoTA + champs pulmonaires clairs + turgescence jugulaire**\n"
                "- ECG : sus-décalage **V3R-V4R** (à enregistrer dans ce contexte)\n"
                "- ETT : dilatation et hypokinésie VD, dilatation OD, IT par dilatation de l'anneau\n"
                "- Complication fréquente : FA → à réduire rapidement (compromet l'hémodynamique)\n"
                "- **CI absolue** à l'administration de **vasodilatateurs**"
            )),
            FicheRow(concept="★ ◆ Rupture de la paroi libre du VG", detail_md=(
                "- Aiguë : **collapsus + dissociation électromécanique** → rapidement fatale\n"
                "- Subaiguë : pronostic très sombre\n"
                "- Signes : recrudescence de la douleur, réélévation de ST en cours de normalisation, hypoTA brutale et prolongée\n"
                "- ETT immédiate ± scanner cardiaque\n"
                "- **Hémopéricarde** → **chirurgie immédiate**"
            )),
            FicheRow(concept="★ Rupture septale (CIV post-IDM)", detail_md=(
                "- Survient typiquement dans les **24-48 h**\n"
                "- Plus fréquente si pas de revascularisation précoce et chez les sujets âgés\n"
                "- **Souffle systolique précordial « en rayon de roue »**\n"
                "- Confirmation par ETT\n"
                "- Pronostic mauvais\n"
                "- Traitement : chirurgical OU fermeture percutanée ; meilleurs résultats si différé de quelques jours"
            )),
            FicheRow(concept="★ ◆ Rupture de pilier mitral", detail_md=(
                "- **Pilier postéromédian** atteint le plus souvent (vascularisation unique par la coronaire droite)\n"
                "- Nécrose du pilier / d'un chef de pilier → **insuffisance mitrale massive** → IVG brutale\n"
                "- Souffle systolique souvent peu intense\n"
                "- Rupture totale = choc cardiogénique rapide\n"
                "- À évoquer si **IDM inférieur + OAP** (le plus souvent rupture partielle)\n"
                "- Diagnostic : ETT\n"
                "- Traitement chirurgical urgent (suture / remplacement valvulaire) ; **MitraClip®** dans certains cas"
            )),
            FicheRow(concept="", detail_md=(
                "- Toute IVG brutale ou souffle systolique nouveau post-IDM → **ETT immédiate** à la recherche d'une complication mécanique (CIV, rupture de pilier, rupture pariétale)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Complications thrombotiques et tardives", rows=[
            FicheRow(concept="Thrombose veineuse / embolie pulmonaire", detail_md=(
                "- Rare car anticoagulation et mobilisation précoce\n"
                "- Anticoagulation préventive si alitement prolongé"
            )),
            FicheRow(concept="Thrombus intra-VG et embolies systémiques", detail_md=(
                "- Associé à une nécrose étendue : surtout SCA ST+ antérieur\n"
                "- Dépistage : ETT dans les **48 h** suivant l'admission en Usic\n"
                "- IRM plus sensible que l'ETT\n"
                "- Présence d'un thrombus → **anticoagulation curative**"
            )),
            FicheRow(concept="Péricardite précoce", detail_md=(
                "- Inflammatoire, associée à un IDM étendu\n"
                "- Douleur thoracique de caractéristiques différentes de la douleur angineuse"
            )),
            FicheRow(concept="Récidive ischémique", detail_md=(
                "- Réocclusion de l'artère désobstruée (SCA ST+) OU\n"
                "- Ischémie controlatérale chez patients pluritronculaires (SCA ST+ et SCA ST–)"
            )),
            FicheRow(concept="◆ Syndrome de Dressler (péricardite tardive)", detail_md=(
                "- **3ᵉ semaine** suivant un IDM étendu\n"
                "- Épanchement péricardique ± épanchement pleural + arthralgies + hyperthermie\n"
                "- Syndrome inflammatoire important\n"
                "- Évolution favorable sous anti-inflammatoires"
            )),
            FicheRow(concept="IVG tardive (remodelage / anévrisme)", detail_md=(
                "- Complique l'IDM étendu ou non revascularisé / revascularisé tardivement\n"
                "- Remodelage progressif du VG (dilatation) ou anévrisme du VG (déformation diastolique)\n"
                "- Traitement = celui de l'insuffisance cardiaque"
            )),
            FicheRow(concept="◆ Troubles du rythme ventriculaire tardifs et DAI", detail_md=(
                "- Fréquence augmente avec l'altération de la FEVG\n"
                "- **Défibrillateur automatique implantable (DAI)** : si **FEVG < 35 %** à distance (≥ **6 semaines** post-IDM), après optimisation du traitement médical\n"
                "- **Lifevest** : si FEVG < 35 % en phase précoce, en attendant l'amélioration potentielle (sidération) après revascularisation et traitement médical"
            )),
        ]),
    ])

    # ============================================================
    # PARTIE VII — PRISE EN CHARGE AU LONG COURS & ANGOR STABLE
    # ============================================================
    partie_vii = Partie(numero="VII", titre="Prise en charge au long cours & Angor stable", sous_parties=[
        SousPartie(lettre="A", titre="Traitement médicamenteux et suivi post-SCA", rows=[
            FicheRow(concept="★ ◆ Antithrombotiques au long cours", detail_md=(
                "- **Aspirine** au long cours\n"
                "- **Inhibiteur P2Y12** associé pendant **12 mois**\n"
                "- Anticoagulant oral justifié (FA, thrombus VG) → pleine dose\n"
                "  - Privilégier par défaut une bithérapie (P2Y12 = clopidogrel + anticoagulant pleine dose) pendant **12 mois**\n"
                "  - Au-delà : anticoagulation seule\n"
                "  - Trithérapie transitoire (~ 1 mois) possible si faible risque hémorragique et haut risque ischémique"
            )),
            FicheRow(concept="Inhibiteurs de la pompe à protons (IPP)", detail_md=(
                "- Prescrits si risque hémorragique digestif élevé :\n"
                "  - âge **≥ 65 ans**\n"
                "  - antécédent d'ulcère\n"
                "  - corticothérapie au long cours\n"
                "- Association aspirine ± autre antiplaquettaire ± anticoagulant\n"
                "- Largement prescrits en pratique"
            )),
            FicheRow(concept="★ ◆ Hypolipémiants — statines", detail_md=(
                "- **Statines à forte dose** en 1ʳᵉ intention\n"
                "  - **Atorvastatine 80 mg** OU **rosuvastatine 20 mg**\n"
                "- Objectif LDL-C : baisse **≥ 50 %** ET **LDL-C < 0,55 g/L**\n"
                "- Si objectif non atteint à 4 semaines à dose maximale tolérée → ajout d'**ézétimibe 10 mg**\n"
                "- Si toujours non atteint → **inhibiteur PCSK9** (remboursé si LDL-C > 0,7 g/L)"
            )),
            FicheRow(concept="IEC / ARA-2", detail_md=(
                "- Prescription non systématique\n"
                "- Indiqués si :\n"
                "  - **FEVG ≤ 40 %**\n"
                "  - Diabète\n"
                "  - Insuffisance rénale chronique"
            )),
            FicheRow(concept="Bêtabloquants au long cours", detail_md=(
                "- Non systématiques mais largement prescrits, surtout après SCA ST+\n"
                "- Indication formelle : **FEVG ≤ 40 %**"
            )),
            FicheRow(concept="Inhibiteurs des récepteurs minéralocorticoïdes (IMR)", detail_md=(
                "- Si **FEVG ≤ 40 %** + manifestations d'IC congestive OU diabète\n"
                "- Après BB + IEC\n"
                "- CI :\n"
                "  - insuffisance rénale (**créatininémie > 221 µmol/L**)\n"
                "  - hyperkaliémie"
            )),
            FicheRow(concept="★ Réadaptation cardiovasculaire", detail_md=(
                "- Recommandée chez **tous** les patients post-SCA\n"
                "- Modalités : hospitalisation conventionnelle OU ambulatoire\n"
                "- Buts :\n"
                "  - vérification de l'évolution\n"
                "  - éducation thérapeutique (signes d'alerte, traitements, mode de vie)\n"
                "  - reprise d'activité physique\n"
                "- Prise en charge pluridisciplinaire : médecins, infirmiers, diététiciens, éducateurs sportifs, psychologues"
            )),
            FicheRow(concept="Suivi médical post-SCA", detail_md=(
                "- Suivi conjoint médecin référent + cardiologue\n"
                "- Objectifs :\n"
                "  - contrôle des FRCV : **sevrage tabagique**, activité physique, régime méditerranéen, LDL-C dans la cible (sans toxicité hépatique/musculaire), contrôle glycémique du diabétique, contrôle PA de l'hypertendu\n"
                "  - dépistage des autres localisations athéromateuses : échodoppler des TSA, échographie de l'aorte abdominale, échodoppler des membres inférieurs\n"
                "  - observance et tolérance du traitement\n"
                "  - dépistage des complications tardives : récidive ischémique (interrogatoire, tests fonctionnels), dégradation de la FEVG"
            )),
        ]),
        SousPartie(lettre="B", titre="Angor stable : généralités, physiopathologie, clinique", rows=[
            FicheRow(concept="Définition de l'angor stable", detail_md=(
                "- = **Syndrome coronarien chronique**\n"
                "- Signe d'ischémie myocardique : besoins en O₂ > apports\n"
                "- Mécanismes : obstruction (athérosclérose le plus souvent) ou spasme\n"
                "- Survient le plus fréquemment à l'effort, **toujours pour le même type d'effort**\n"
                "- Peut être déclenché par : stress émotionnel, repas copieux, froid\n"
                "- Peut être 1ʳᵉ manifestation ou survenir au décours d'un SCA"
            )),
            FicheRow(concept="Physiopathologie de l'ischémie", detail_md=(
                "- **Cascade ischémique** :\n"
                "  - augmentation H⁺ et K⁺ dans le sang veineux drainant\n"
                "  - anomalie de la cinétique segmentaire (diastole puis systole)\n"
                "  - modifications ECG (ST et T)\n"
                "  - douleur (libération de métabolites stimulant les terminaisons nerveuses)\n"
                "- Augmentation de la consommation O₂ : tachycardie, inotropisme, PA (effort)"
            )),
            FicheRow(concept="Facteurs aggravants surajoutés", detail_md=(
                "- Augmentation des besoins en O₂ : hyperthermie, tachycardie, tachyarythmie, hyperthyroïdie, hyperadrénergie, augmentation post-charge VG (poussée HTA, **sténose aortique**)\n"
                "- Diminution des apports : anémie, hypoxémie, méthémoglobinémie (ex : **poppers**)"
            )),
            FicheRow(concept="◆ Seuil de sténose induisant une ischémie d'effort", detail_md=(
                "- Sténose induit classiquement une ischémie d'effort si réduit **≥ 70 % du calibre coronaire**\n"
                "- Notion remise en cause : ischémie pas toujours proportionnelle à la sévérité angiographique\n"
                "- À l'effort : vasodilatation distale retarde l'apparition de l'ischémie"
            )),
            FicheRow(concept="◆ Angor typique", detail_md=(
                "- Rétrosternal en barre, d'un pectoral à l'autre (signe « main à plat »)\n"
                "- Irradiations : épaules, avant-bras, poignets, mâchoires, parfois dos\n"
                "- Constrictif (« poitrine serrée dans un étau »), angoissant\n"
                "- Intensité variable (gêne ↔ douleur syncopale)\n"
                "- Provoqué par l'effort, cède à l'arrêt ou après TNT sublinguale\n"
                "- **Angor stable** = douleur exclusivement à l'effort et toujours pour le même type d'effort\n"
                "- ⚠ Un **angor de novo** doit être considéré comme un **SCA** jusqu'à preuve du contraire"
            )),
            FicheRow(concept="◆ Classification CCS de la sévérité de l'angor", detail_md=(
                "| Classe | Description |\n"
                "|--------|-------------|\n"
                "| **1** | Activités quotidiennes non limitées. Angor pour efforts **soutenus, abrupts ou prolongés** |\n"
                "| **2** | Limitation discrète. Angor à la **marche rapide ou en côte** (escaliers rapides, montagne, après repas, froid, émotions, réveil) |\n"
                "| **3** | Limitation importante. Angor au **moindre effort** (marche à plat **100-200 m**, ascension lente de quelques escaliers) |\n"
                "| **4** | Impossibilité de mener la moindre activité physique sans douleur |"
            )),
            FicheRow(concept="Autres présentations cliniques de l'angor", detail_md=(
                "- Atypie : siège épigastrique, irradiations isolées\n"
                "- Blocpnée d'effort (impossibilité de vider l'air à l'expiration), proche de la dyspnée\n"
                "- Palpitations d'effort : trouble du rythme ischémique\n"
                "- IVG d'effort : ischémie étendue\n"
                "- Ischémie silencieuse : détectée lors d'un test fonctionnel de dépistage\n"
                "- Valeur diagnostique majeure : survenue à l'effort + disparition à l'arrêt"
            )),
            FicheRow(concept="Examen clinique", detail_md=(
                "- Habituellement normal\n"
                "- À rechercher : FRCV (PA, poids), autres localisations athéromateuses, **souffle de rétrécissement aortique**"
            )),
        ]),
        SousPartie(lettre="C", titre="Angor stable : examens fonctionnels et anatomiques", rows=[
            FicheRow(concept="Examens fonctionnels — principes", detail_md=(
                "- Démarche diagnostique si angor stable suspecté\n"
                "- **CI** en cas de SCA récent\n"
                "- Principe : effort ou stress pharmacologique révèle le déséquilibre apport/demande\n"
                "- Probabilité forte : homme > 40 ans, angor d'effort typique\n"
                "- Probabilité faible : femme < 50 ans, précordialgies atypiques"
            )),
            FicheRow(concept="◆ ECG d'effort", detail_md=(
                "- Effort progressif sur bicyclette ou tapis roulant (**protocole de Bruce**)\n"
                "- Surveillance clinique, tensionnelle, ECG (12 dérivations)\n"
                "- Critères d'arrêt :\n"
                "  - mauvaise tolérance (dyspnée, angor typique, hypoTA)\n"
                "  - **PAS > 210 mmHg**\n"
                "  - trouble du rythme ventriculaire répétitif\n"
                "  - FMT atteinte = **220 – âge**\n"
                "  - résultat positif\n"
                "- **Positivité** : sous-décalage ST **> 1 mm**, horizontal ou descendant ± douleur thoracique"
            )),
            FicheRow(concept="ECG d'effort — limites et CI", detail_md=(
                "- Limites :\n"
                "  - Ininterprétable si ECG de repos anormal (BBG, pacemaker)\n"
                "  - Sensibilité et spécificité inférieures aux autres tests fonctionnels (scinti, écho, IRM de stress)\n"
                "- **Contre-indications absolues** :\n"
                "  - IDM récent **< 48 h** ou SCA non stabilisé\n"
                "  - Sténose connue du tronc commun gauche\n"
                "  - Rétrécissement aortique serré symptomatique\n"
                "  - TV/troubles de conduction non contrôlés\n"
                "  - Insuffisance cardiaque non contrôlée\n"
                "  - Embolie pulmonaire récente\n"
                "  - Myocardite aiguë\n"
                "- Avantage : peu coûteux"
            )),
            FicheRow(concept="◆ Scintigraphie myocardique de perfusion", detail_md=(
                "- Traceur isotopique (**thallium 201**) injecté à l'effort maximal et au repos\n"
                "- VG divisé en **17 segments**\n"
                "- Effort ou **dipyridamole (Persantine®)** (vasodilatateur)\n"
                "- Interprétation :\n"
                "  - **Ischémie** : hypofixation à l'effort, normalisation au repos\n"
                "  - **Nécrose** : hypofixation à l'effort ET au repos\n"
                "- Limites : BBG (interprétation aléatoire), obésité (artefacts), irradiant, coûteux\n"
                "- **CI au dipyridamole** : **asthme**\n"
                "- Avantages : meilleure sensibilité/spécificité que l'ECG d'effort ; localise et évalue l'étendue de l'ischémie"
            )),
            FicheRow(concept="◆ Échocardiographie d'effort ou de stress", detail_md=(
                "- Étude cinétique/épaississement pariétal sur **17 segments**\n"
                "- Stress = effort OU **dobutamine** (inotrope positif, alternative si AOMI, troubles locomoteurs)\n"
                "- Diminution (hypokinésie, akinésie) à l'effort vs repos = ischémie\n"
                "- Limites : opérateur-dépendant\n"
                "- Avantages : sensibilité/spécificité voisines de la scintigraphie, pas d'irradiation, moins coûteux"
            )),
            FicheRow(concept="◆ IRM de stress", detail_md=(
                "- Étude des troubles de cinétique segmentaire OU anomalie de perfusion sous stress\n"
                "- Effort impossible sur IRM → **dobutamine** (cinétique) ou **adénosine** (perfusion)\n"
                "- Limites : disponibilité limitée, CI de l'IRM, CI à l'adénosine (**asthme**)\n"
                "- Avantages : alternative à l'écho (patient anéchogène) et à la scintigraphie (effort impossible) ; pas de marqueur radioactif"
            )),
            FicheRow(concept="◆ Coronarographie", detail_md=(
                "- Identifie directement une sténose coronarienne par luminographie (injection de produit de contraste iodé)\n"
                "- **Voie radiale préférée** (moins de complications)\n"
                "- Complications :\n"
                "  - rénales (IRC, diabète) et anaphylactiques liées au contraste iodé\n"
                "  - infectieuses locales\n"
                "  - vasculaires (hématome, dissection, ischémie périphérique)\n"
                "  - emboliques (cérébrale, périphérique)\n"
                "  - rythmiques (cardioversion immédiate parfois nécessaire)\n"
                "- Prévention IRC : hyperhydratation préalable + réduction du volume de produit de contraste"
            )),
            FicheRow(concept="FFR (Fractional Flow Reserve)", detail_md=(
                "- Évaluation fonctionnelle invasive d'une sténose incertaine\n"
                "- Guide avec capteur de pression au-delà de la sténose\n"
                "- Injection de dérivés nitrés + adénosine (vasodilatation)\n"
                "- FFR = pression distale / pression proximale\n"
                "- **FFR ≤ 0,8** = sténose critique induisant une ischémie à l'effort"
            )),
            FicheRow(concept="Coroscanner", detail_md=(
                "- Angioscanner couplé à un ECG (après ralentissement par bêtabloquant si besoin)\n"
                "- Identifie sténose et plaque athéromateuse (pariétographie)\n"
                "- Limites : FC élevée/irrégulière (FA), calcifications, petits calibres, irradiation (risque mammaire chez la femme), évaluation difficile dans un stent\n"
                "- Très performant pour la perméabilité d'un pontage\n"
                "- **Excellente valeur prédictive négative**"
            )),
        ]),
        SousPartie(lettre="D", titre="Angor stable : traitement et revascularisation", rows=[
            FicheRow(concept="◆ Stratification du risque", detail_md=(
                "- Évaluation du risque annuel de décès :\n"
                "  - Bas risque : **< 1 %**\n"
                "  - Risque intermédiaire : **≥ 1 % et ≤ 3 %**\n"
                "  - Haut risque : **> 3 %**\n"
                "- Critères de haut risque :\n"
                "  - angor **CCS 3-4**\n"
                "  - FEVG diminuée\n"
                "  - épreuve d'effort précocement positive (**≤ 6 min**)\n"
                "  - ischémie d'effort **> 10 % du VG**\n"
                "- Situations à haut risque : sténose du tronc commun, IVA proximale, tritronculaire proximal → revascularisation complémentaire"
            )),
            FicheRow(concept="Correction des FRCV", detail_md=(
                "- **Arrêt définitif** du tabac\n"
                "- Activité physique régulière + perte d'excès pondéral\n"
                "- HTA (**> 135/85 mmHg** en automesure) : **IEC, ARA-2 ou BB** en 1ʳᵉ intention\n"
                "- Diabète : régime + traitement\n"
                "- Dyslipidémie : statine ± ézétimibe ; objectif **LDL-C < 0,55 g/L** en prévention secondaire"
            )),
            FicheRow(concept="Traitement de la crise angineuse", detail_md=(
                "- **Trinitrine sublinguale en spray**\n"
                "- Effet vasodilatateur artériel efficace en quelques secondes\n"
                "- Effets indésirables : céphalées, chute tensionnelle\n"
                "- Conseil : s'asseoir/s'allonger lors de la prise"
            )),
            FicheRow(concept="◆ Anti-ischémiques au long cours — Bêtabloquants", detail_md=(
                "- Diminuent FC, inotropisme, PA\n"
                "- **Contre-indications** :\n"
                "  - Asthme\n"
                "  - BPCO sévère (bronchoconstricteurs)\n"
                "  - Phénomène de Raynaud (vasoconstricteurs)\n"
                "  - Bradycardie sévère (**< 50/min**)\n"
                "  - BAV 2 ou 3"
            )),
            FicheRow(concept="Inhibiteurs calciques", detail_md=(
                "- Réduisent inotropisme et PA ± FC\n"
                "- Effet indésirable principal : **œdèmes des membres inférieurs** (surtout dihydropyridines)\n"
                "- Bradycardisants (diltiazem, vérapamil) : si CI ou intolérance aux BB ; **PAS d'association** aux BB (trouble de conduction)\n"
                "- Non bradycardisants (dihydropyridines) : 1ʳᵉ intention si CI aux BB OU FC basse (< 60/min) ; 2ᵉ intention en association aux BB si angor résiduel"
            )),
            FicheRow(concept="Dérivés nitrés à libération prolongée", detail_md=(
                "- Favorisent la sécrétion de NO (vasodilatateur coronaire et veineux)\n"
                "- Per os ou timbre transdermique 18 h/j\n"
                "- **CI** : association aux **inhibiteurs de PDE5** (sildénafil…)\n"
                "- Effets indésirables : céphalées, échappement thérapeutique\n"
                "- 3ᵉ intention chez les patients symptomatiques sous BB et/ou ICa\n"
                "- Molsidomine : mécanisme et profil identiques"
            )),
            FicheRow(concept="Nicorandil", detail_md=(
                "- Activateur des canaux potassiques ATP-dépendants, vasodilatateur + effet protecteur (préconditionnement)\n"
                "- Effet indésirable : **ulcérations péribuccales, intestinales, périanales**\n"
                "- Prescrit habituellement en 3ᵉ intention"
            )),
            FicheRow(concept="Ivabradine", detail_md=(
                "- Indiquée si rythme sinusal + FC **≥ 70/min**\n"
                "- Pratiquement plus utilisée\n"
                "- Inhibiteur du canal **If** du nœud sinusal\n"
                "- Effet indésirable principal : **phosphènes** (visuels, transitoires)\n"
                "- Inefficace en FA"
            )),
            FicheRow(concept="Antiagrégants plaquettaires dans l'angor stable", detail_md=(
                "- **Aspirine** : inhibition irréversible de la Cox-1 plaquettaire\n"
                "  - Effets digestifs proportionnels à la dose mais pas l'effet antiplaquettaire\n"
                "  - Indication systématique chez tout coronarien à **75-100 mg/j**\n"
                "- **Clopidogrel** :\n"
                "  - si CI à l'aspirine\n"
                "  - OU en association à l'aspirine pendant **6 mois** après stent actif\n"
                "  - parfois préféré chez les patients polyartériels (AOMI)\n"
                "- Nouveaux P2Y12 : non indiqués en angor stable"
            )),
            FicheRow(concept="◆ Revascularisation dans l'angor stable", detail_md=(
                "- Indications :\n"
                "  - fonctionnelle : symptômes persistants malgré traitement médical optimal\n"
                "  - pronostique : patients à haut risque (sténose tronc commun, IVA proximale, tritronculaire proximal)\n"
                "- Pas de supériorité de la revascularisation systématique vs traitement médical optimal dans l'angor stable\n"
                "- Choix angioplastie vs pontage : siège, diffusion, comorbidités, **EuroSCORE / STS score**\n"
                "- **Pontage privilégié** :\n"
                "  - lésions diffuses\n"
                "  - diabétique\n"
                "  - tronc coronaire gauche\n"
                "  - IVA proximale\n"
                "  - sous réserve d'un lit d'aval accessible"
            )),
            FicheRow(concept="Angioplastie en angor stable", detail_md=(
                "- Précédée d'une coronarographie\n"
                "- Ballonnet + **stent** (actif = enduit antimitotique → réduction de la resténose)\n"
                "- Bithérapie aspirine + clopidogrel habituellement **6 mois** après stent"
            )),
            FicheRow(concept="Pontages coronariens", detail_md=(
                "- Sous CEC habituelle (rarement à cœur battant)\n"
                "- Greffon **artériel préférentiel** : artères mammaires internes (subclavières)\n"
                "- Pontages aortocoronariens : veine saphène (mollet) ou artère radiale"
            )),
            FicheRow(concept="", detail_md=(
                "- **Angor de novo** = à traiter comme un **SCA** jusqu'à preuve du contraire ; objectif **LDL-C < 0,55 g/L** en prévention secondaire ; **arrêt tabac** non négociable"
            ), kind="a_retenir"),
        ]),
    ])

    # ============================================================
    # TABLEAUX DE SYNTHÈSE
    # ============================================================
    tableaux = [
        TableauSynthese(titre="SCA ST+ vs SCA ST– : synthèse comparative", markdown=(
            "| Critère | SCA ST+ (STEMI) | SCA ST– (NSTEMI / angor instable) |\n"
            "|---------|-----------------|-----------------------------------|\n"
            "| **Douleur** | Persistante > 30 min, **non régressive sous TNT** | Spontanée ou efforts modérés, variable, souvent transitoire ; régressive sous TNT |\n"
            "| **ECG** | **Sus-décalage ST persistant** + miroir | Sous-décalage, T négatives, sus-décalage transitoire OU normal |\n"
            "| **Mécanisme** | **Occlusion coronarienne totale** (thrombus rouge) | Thrombus blanc non occlusif ; spasme ; emboles |\n"
            "| **Troponine** | Confirme a posteriori | **Clé du diagnostic** (algorithme rule-in/rule-out) |\n"
            "| **Reperfusion** | **Angioplastie primaire < 120 min** OU fibrinolyse | Coronarographie : **< 2 h** très haut risque, **< 24 h** haut risque |\n"
            "| **Antithrombotique initial** | Aspirine + **prasugrel/ticagrélor** ± clopidogrel | Aspirine d'emblée, **P2Y12 après coronarographie** |\n"
            "| **Anticoagulant** | HNF 70-100 UI/kg IVD (ou énoxaparine 0,5 mg/kg IVD) | Énoxaparine 1 mg/kg SC ×2 OU fondaparinux 2,5 mg/j SC |\n"
            "| **Hospitalisation Usic** | 3-5 jours | 24-48 h post-revascularisation |"
        )),
        TableauSynthese(titre="Les 5 types d'infarctus du myocarde", markdown=(
            "| Type | Définition | Mécanisme principal |\n"
            "|------|-----------|---------------------|\n"
            "| **1** | Athérothrombotique | Rupture/fissuration/érosion de plaque + thrombus |\n"
            "| **2** | Déséquilibre apport/demande | Tachy/bradycardie, anémie, hypoxémie, spasme, dissection spontanée, embolie, dysfonction microvasculaire |\n"
            "| **3** | Mort subite | Décès avant dosage de troponine |\n"
            "| **4** | Iatrogène | **Angioplastie** coronaire |\n"
            "| **5** | Iatrogène | **Pontage** aortocoronarien |"
        )),
        TableauSynthese(titre="Localisation de l'IDM ST+ à l'ECG", markdown=(
            "| Dérivations | Territoire | Artère habituelle |\n"
            "|-------------|------------|-------------------|\n"
            "| **D2-D3-aVF** | Inférieur | **CD** (extension VD possible : V3R-V4R) |\n"
            "| **V1-V2-V3** | Antéroseptal | IVA |\n"
            "| **V4** | Apical | IVA |\n"
            "| **V5-V6** | Latéral bas | Circonflexe / IVA distale |\n"
            "| **D1-aVL** | Latéral haut | Circonflexe (marginale) |\n"
            "| **V1-V6** | Antérieur étendu | **IVA proximale** |\n"
            "| **V7-V8-V9** | Postérieur | Circonflexe (image miroir V1-V3) |"
        )),
        TableauSynthese(titre="Classification de Killip de l'IVG dans l'IDM", markdown=(
            "| Stade | Description |\n"
            "|-------|-------------|\n"
            "| **1** | Pas de râles crépitants |\n"
            "| **2** | Râles crépitants aux bases (≤ moitié des champs pulmonaires) |\n"
            "| **3** | Râles > moitié (OAP), galop |\n"
            "| **4** | **Choc cardiogénique** |"
        )),
        TableauSynthese(titre="Classification CCS de l'angor stable", markdown=(
            "| Classe | Description |\n"
            "|--------|-------------|\n"
            "| **1** | Activités quotidiennes non limitées. Angor pour efforts soutenus, abrupts ou prolongés |\n"
            "| **2** | Limitation discrète. Angor à la marche rapide ou en côte |\n"
            "| **3** | Limitation importante. Angor au moindre effort (marche 100-200 m) |\n"
            "| **4** | Impossibilité de toute activité physique sans douleur |"
        )),
        TableauSynthese(titre="Antithrombotiques au cours du SCA — récapitulatif", markdown=(
            "| Classe | Molécule | Posologie | Particularités |\n"
            "|--------|----------|-----------|----------------|\n"
            "| **Aspirine** | acide acétylsalicylique | **250 mg IVD** puis **75-100 mg/j po** | + IPP |\n"
            "| **P2Y12** | **clopidogrel** | charge **600 mg** (300 si fibrinolyse), **75 mg/j** | Moins efficace ; seul autorisé avec fibrinolyse |\n"
            "| **P2Y12** | **prasugrel** | charge **60 mg**, **10 mg/j** | **CI si ATCD AVC**, > 75 ans, < 60 kg |\n"
            "| **P2Y12** | **ticagrélor** | charge **180 mg**, **90 mg ×2/j** | Bradycardie, dyspnée réversibles |\n"
            "| **Anticoagulant (angioplastie)** | HNF / énoxaparine IVD | 70-100 UI/kg IVD ; 0,5 mg/kg IVD | Arrêt post-procédure |\n"
            "| **Anticoagulant (SCA ST– HR)** | énoxaparine / fondaparinux | 1 mg/kg SC ×2/j ; 2,5 mg/j SC | Fondaparinux + bolus HNF en coronarographie |"
        )),
        TableauSynthese(titre="Comparaison des tests fonctionnels d'ischémie", markdown=(
            "| Test | Principe | Avantages | Limites |\n"
            "|------|----------|-----------|---------|\n"
            "| **ECG d'effort** | Sous-décalage > 1 mm horizontal/descendant | Peu coûteux | Sensibilité faible ; CI : BBG, pacemaker, IDM < 48 h, RAO serré sympt., TV/IC non contrôlées, EP récente, myocardite |\n"
            "| **Scintigraphie** | Thallium 201 ± dipyridamole | Sensibilité ↑, localisation et étendue | Irradiation, coût, CI dipyridamole = **asthme**, artefacts (BBG, obésité) |\n"
            "| **Échocardio de stress** | Cinétique sous effort/dobutamine | Pas d'irradiation, peu coûteuse | Opérateur-dépendant |\n"
            "| **IRM de stress** | Cinétique (dobutamine) ou perfusion (adénosine) | Alternative si écho non réalisable, pas de marqueur radioactif | Disponibilité ↓, CI IRM, CI adénosine = **asthme** |\n"
            "| **Coroscanner** | Anatomique (pariétographie) | Excellente **VPN** | FC élevée/irrégulière, calcifications, stents, irradiation |\n"
            "| **Coronarographie ± FFR** | Anatomique de référence ± fonctionnelle invasive | Référence, complétée par geste interventionnel | Invasive, complications iodées et vasculaires |"
        )),
    ]

    # ============================================================
    # CHIFFRES-CLÉS
    # ============================================================
    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Durée minimale de la douleur du SCA ST+ | **> 30 min** | Persistante, non régressive sous TNT |\n"
        "| Durée de la douleur SCA ST– (forme prolongée) | **> 20 min** | Spontanée |\n"
        "| Délai ECG au SAU | **< 10 min** | Après l'admission |\n"
        "| Délai max angioplastie primaire (vs fibrinolyse) | **120 min** | Détermine la stratégie de reperfusion |\n"
        "| Coronarographie SCA ST– très haut risque | **< 2 h** | Comme SCA ST+ |\n"
        "| Coronarographie SCA ST– haut risque | **< 24 h** | Stratégie invasive |\n"
        "| Bénéfice de la reperfusion : seuil de chute | **12 h** | Faible au-delà |\n"
        "| Bénéfice de la reperfusion : nul au-delà | **24 h** | |\n"
        "| Seuil de sus-décalage ST en V2-V3 (homme) | **≥ 2 mm** | |\n"
        "| Seuil sus-décalage V2-V3 homme < 40 ans | **≥ 2,5 mm** | |\n"
        "| Seuil sus-décalage V2-V3 femme | **≥ 1,5 mm** | |\n"
        "| Seuil sus-décalage autres dérivations | **≥ 1 mm** | |\n"
        "| Seuil sus-décalage en V7-V9 (postérieur) | **≥ 0,5 mm** | |\n"
        "| Délai d'apparition de l'onde Q | **6 h** | À partir du début des symptômes |\n"
        "| ECG normal en SCA ST– | **> 30 %** | N'élimine PAS le SCA |\n"
        "| Prévalence IDM ST+ aux urgences | **5-10 %** | Douleur thoracique non sélectionnée |\n"
        "| Prévalence IDM ST– aux urgences | **15-20 %** | |\n"
        "| Prévalence angor instable aux urgences | **10 %** | |\n"
        "| Prévalence MINOCA parmi les SCA | **~ 6 %** | |\n"
        "| Femmes parmi les MINOCA | **~ 40 %** | |\n"
        "| Incidence européenne SCA | **293/100 000 hab** | IC 95 % : 196-530 |\n"
        "| Incidence IDM ST+ | **43-144/100 000/an** | |\n"
        "| Hospitalisations IDM/an en France | **> 60 000** | |\n"
        "| Mortalité hospitalière IDM ST+ Europe | **4-12 %** | |\n"
        "| Mortalité IDM ST+ à 1 an | **~ 10 %** | |\n"
        "| Mortalité du choc cardiogénique | **> 70 %** | Pronostic très sombre |\n"
        "| PAS définissant le « préchoc » | **< 90 mmHg** | Mal tolérée, non corrigée par remplissage |\n"
        "| Décalage des âges H/F dans la maladie coronaire | **7-10 ans** | F après H |\n"
        "| Aspirine charge IVD | **250 mg** | Puis 75-100 mg/j po |\n"
        "| Aspirine entretien po | **75-100 mg/j** | + IPP |\n"
        "| Clopidogrel charge / entretien | **600 / 75 mg/j** | 300 mg si fibrinolyse < 75 ans |\n"
        "| Prasugrel charge / entretien | **60 / 10 mg/j** | CI ATCD AVC, > 75 ans, < 60 kg |\n"
        "| Ticagrélor charge / entretien | **180 / 90 mg ×2/j** | Bradycardie, dyspnée |\n"
        "| HNF (angioplastie) | **70-100 UI/kg IVD** | |\n"
        "| Énoxaparine IVD (angioplastie) | **0,5 mg/kg IVD** | |\n"
        "| Énoxaparine SCA ST– HR | **1 mg/kg SC ×2/j** | |\n"
        "| Fondaparinux SCA ST– HR | **2,5 mg/j SC** | + bolus HNF en coronarographie |\n"
        "| Dinitrate d'isosorbide IV | **2 mg/h** | Antalgique, antihypertenseur, IVG |\n"
        "| Atorvastatine forte dose | **80 mg** | Post-SCA |\n"
        "| Rosuvastatine forte dose | **20 mg** | Post-SCA |\n"
        "| Objectif LDL-C en prévention secondaire | **< 0,55 g/L** | + réduction ≥ 50 % |\n"
        "| Seuil LDL-C pour PCSK9 (remboursement) | **> 0,7 g/L** | Si objectif non atteint |\n"
        "| Ézétimibe | **10 mg** | Si objectif non atteint à 4 sem |\n"
        "| Seuil FEVG → IEC/ARA-2/BB/IMR | **≤ 40 %** | Post-SCA |\n"
        "| Seuil FEVG → DAI à distance | **< 35 %** | À ≥ 6 semaines post-IDM |\n"
        "| Seuil FEVG → Lifevest en phase précoce | **< 35 %** | |\n"
        "| Délai minimal post-IDM pour DAI | **6 semaines** | |\n"
        "| Seuil créatininémie CI IMR | **> 221 µmol/L** | |\n"
        "| SaO₂ déclenchant O₂ | **< 90 %** | Sinon hyperoxie délétère |\n"
        "| PaO₂ déclenchant O₂ | **< 60 mmHg** | |\n"
        "| Seuil sténose induisant ischémie d'effort | **≥ 70 %** | Notion remise en cause |\n"
        "| FFR seuil de sténose critique | **≤ 0,8** | |\n"
        "| FMT (épreuve d'effort) | **220 – âge** | Critère d'arrêt |\n"
        "| PAS critère d'arrêt EE | **> 210 mmHg** | |\n"
        "| ECG d'effort : seuil de positivité | **> 1 mm** | Sous-décalage horizontal/descendant |\n"
        "| Épreuve d'effort précocement positive | **≤ 6 min** | Critère de haut risque |\n"
        "| Ischémie étendue à l'imagerie | **> 10 % du VG** | Critère de haut risque |\n"
        "| Risque annuel de décès bas / intermédiaire / haut | **< 1 % / 1-3 % / > 3 %** | Angor stable |\n"
        "| HTA en automesure : seuil de traitement | **> 135/85 mmHg** | |\n"
        "| Bradycardie sévère CI aux BB | **< 50/min** | |\n"
        "| FC ivabradine | **≥ 70/min** | En rythme sinusal |\n"
        "| Score GRACE seuil de haut risque (SCA ST–) | **> 140** | Peu utilisé en France |\n"
        "| Segments d'analyse du VG | **17** | Échocardio/scinti/IRM |\n"
        "| Délai d'apparition du syndrome de Dressler | **3ᵉ semaine** | Post-IDM étendu |\n"
        "| Délai d'apparition de la rupture septale | **24-48 h** | |\n"
        "| Dépistage thrombus VG par ETT | **48 h** | Suivant l'admission en Usic |\n"
        "| Durée de la bithérapie post-stent SCA | **12 mois** | Adaptable au risque |\n"
        "| Durée de la bithérapie post-stent angor stable | **6 mois** | |\n"
        "| Âge seuil IPP systématique | **≥ 65 ans** | + autres FR digestifs |\n"
        "| Âge à risque hémorragique (saignement) | **> 75 ans** | |\n"
        "| Poids à risque hémorragique | **< 65 kg** | |"
    ))

    # ============================================================
    # POINTS-CLÉS
    # ============================================================
    points_cles = [
        "SCA = ischémie myocardique aiguë ; **ECG initial** sépare **ST+** (sus-décalage persistant) et **ST–**",
        "SCA ST+ : **angioplastie primaire < 120 min** > fibrinolyse ; bénéfice **nul au-delà de 24 h**",
        "SCA ST– : **troponine us** = clé (rule-in/rule-out) ; coro **< 2 h** (très haut risque) ou **< 24 h** (haut risque)",
        "IDM = **Tn-us > 99ᵉ percentile** + 1 critère (clinique, ECG, imagerie ou thrombus endoluminal)",
        "**5 types d'IDM** : 1 athérothrombotique, 2 apport/demande, 3 mort subite, 4 angioplastie, 5 pontage",
        "**ECG normal n'élimine PAS un SCA ST–** (> 30 %) ; **BBG/BBD** symptomatique = équivalent de sus-décalage",
        "Trithérapie = **aspirine + P2Y12 + anticoagulant** ; en ST– la bithérapie est **différée** post-coronarographie",
        "**CI fibrinolyse** : AVC hémorragique, AVC < 6 mois, dissection aortique, hémorragie digestive récente",
        "Complications mécaniques (**CIV, pilier mitral, rupture pariétale**) : **ETT immédiate** si souffle ou IVG brutale",
        "Post-SCA : aspirine + P2Y12 **12 mois** + **statine forte dose** (**LDL-C < 0,55 g/L**) + réadaptation",
    ]

    # ============================================================
    # FICHE ÉCLAIR
    # ============================================================
    fiche_eclair_md = (
        "**SCA ST+** : douleur > 30 min non régressive TNT, sus-décalage persistant. Angioplastie < 120 min > fibrinolyse. Bénéfice nul à 24 h.\n\n"
        "**SCA ST–** : douleur > 20 min, angor récent ou crescendo. Troponine = clé. Coro < 2 h très haut risque, < 24 h haut risque.\n\n"
        "**IDM** : Tn > 99ᵉ p + critère associé. 5 types (athéro, apport/demande, mort subite, angioplastie, pontage).\n\n"
        "**ECG ST+** : Pardee ≥ 2 mm V2-V3 (1,5 F), ≥ 1 mm autres. D2D3aVF inférieur, V1-V3 antéroseptal, V5-V6 latéral bas, V7-V9 postérieur, V3R-V4R VD. Normal en ST– > 30 %.\n\n"
        "**CI fibrinolyse** : AVC hémorragique ou < 6 mois, tumeur/MAV cérébrale, TC < 1 mois, hémorragie digestive < 1 mois, dissection aortique.\n\n"
        "**Trithérapie** : aspirine 250 IVD puis 75-100/j + IPP. P2Y12 prasugrel (CI AVC, > 75 ans, < 60 kg)/ticagrélor/clopidogrel (seul avec fibrinolyse). HNF 70-100 UI/kg ou énoxaparine 0,5 mg/kg IVD ; énoxaparine 1 mg/kg ×2 ou fondaparinux 2,5/j (ST– HR).\n\n"
        "**Killip** : 1 normal / 2 crépitants / 3 OAP / 4 choc (mortalité > 70 %). **O₂** si SaO₂ < 90 %.\n\n"
        "**Complications** : FV → CEE. BAV inférieur → atropine ; hissien antérieur → pacemaker. IDM du VD : hypoTA + champs clairs + TJ ; CI vasodilatateurs. Mécaniques (CIV en rayon de roue, pilier mitral) → ETT immédiate. Dressler 3ᵉ sem. DAI si FEVG < 35 % à ≥ 6 sem.\n\n"
        "**Post-SCA** : aspirine + P2Y12 12 mois + statine forte dose, LDL-C < 0,55 g/L. IEC/BB/IMR si FEVG ≤ 40 %. Réadaptation pour tous. Sevrage tabac.\n\n"
        "**Angor stable** : effort, même type. CCS 1-4. Sténose ≥ 70 %. Tests : ECG d'effort > 1 mm, scinti, écho/IRM stress, coroscanner, coro ± FFR ≤ 0,8.\n\n"
        "**Anti-ischémiques** : BB (CI asthme, Raynaud, FC < 50, BAV 2-3), ICa, nitrés LP, nicorandil, ivabradine. Pontage si tronc commun, IVA proximale, tritronculaire, diabétique.\n"
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 339 - Syndromes coronariens aigus",
        annee="2025-2026",
        item="Item 339",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi, partie_vii],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 339",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-339_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

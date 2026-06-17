"""Génère la fiche exhaustive d'Hépato-gastro-entérologie."""

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
        PlanPartie(numero="I", titre="Anomalies du bilan hépatique et ictère", sous_parties=[
            PlanSousPartie(lettre="A", titre="Cytolyse hépatique"),
            PlanSousPartie(lettre="B", titre="Cholestase et augmentation isolée des GGT"),
            PlanSousPartie(lettre="C", titre="Ictère à bilirubine non conjuguée et conjuguée"),
        ]),
        PlanPartie(numero="II", titre="Cirrhose", sous_parties=[
            PlanSousPartie(lettre="A", titre="Cirrhose non compliquée : diagnostic et étiologies"),
            PlanSousPartie(lettre="B", titre="Score de Child-Pugh et prise en charge"),
            PlanSousPartie(lettre="C", titre="Hémorragie digestive sur HTP"),
            PlanSousPartie(lettre="D", titre="Encéphalopathie hépatique et syndrome hépato-rénal"),
            PlanSousPartie(lettre="E", titre="Ascite et infection du liquide d'ascite"),
        ]),
        PlanPartie(numero="III", titre="Hépatites virales", sous_parties=[
            PlanSousPartie(lettre="A", titre="Hépatites aiguës virales et hépatite fulminante"),
            PlanSousPartie(lettre="B", titre="Hépatite B : aiguë et chronique"),
            PlanSousPartie(lettre="C", titre="Hépatite C : aiguë et chronique"),
            PlanSousPartie(lettre="D", titre="Hépatites A, D et E"),
        ]),
        PlanPartie(numero="IV", titre="Pathologie gastro-duodénale et RGO", sous_parties=[
            PlanSousPartie(lettre="A", titre="Ulcère gastro-duodénal"),
            PlanSousPartie(lettre="B", titre="Gastrites et gastropathies"),
            PlanSousPartie(lettre="C", titre="Reflux gastro-oesophagien"),
        ]),
        PlanPartie(numero="V", titre="Pathologie biliaire et pancréatique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Lithiase biliaire : colique hépatique et cholécystite"),
            PlanSousPartie(lettre="B", titre="Lithiase de la VBP et angiocholite"),
            PlanSousPartie(lettre="C", titre="Pancréatite aiguë"),
            PlanSousPartie(lettre="D", titre="Pancréatite chronique"),
        ]),
        PlanPartie(numero="VI", titre="Urgences et pathologies fonctionnelles digestives", sous_parties=[
            PlanSousPartie(lettre="A", titre="Hémorragies digestives"),
            PlanSousPartie(lettre="B", titre="Péritonite aiguë"),
            PlanSousPartie(lettre="C", titre="Syndrome occlusif"),
            PlanSousPartie(lettre="D", titre="Diarrhées aiguës infectieuses"),
            PlanSousPartie(lettre="E", titre="Diverticulose colique et diverticulite"),
            PlanSousPartie(lettre="F", titre="Colopathie fonctionnelle"),
        ]),
    ]

    # ── PARTIE I : ANOMALIES DU BILAN HÉPATIQUE ET ICTÈRE ──
    partie_i = Partie(numero="I", titre="Anomalies du bilan hépatique et ictère", sous_parties=[
        SousPartie(lettre="A", titre="Cytolyse hépatique", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Cytolyse** : augmentation des transaminases liée à la destruction des hépatocytes\n"
                "- **ALAT** (11-40 UI/L) : surtout présente dans le **foie** (plus spécifique)\n"
                "- **ASAT** (10-30 UI/L) : surtout présente dans le **myocarde** et le muscle squelettique"
            )),
            FicheRow(concept="Cytolyse chronique < 10N", detail_md=(
                "- **Causes hépatiques** :\n"
                "  - Hépatite chronique B et C\n"
                "  - Hémochromatose\n"
                "  - **Alcool** : rapport ASAT/ALAT > 1 + augmentation GGT\n"
                "  - Stéato-hépatite non alcoolique (NASH)\n"
                "  - Médicamenteuse\n"
                "  - Rares : hépatite auto-immune, maladie de Wilson, déficit en alpha-1 antitrypsine\n"
                "- **Causes extra-hépatiques** :\n"
                "  - **Maladie coeliaque** +++\n"
                "  - Dysthyroïdie\n"
                "  - Myopathie, exercice physique intense\n"
                "  - Insuffisance surrénalienne (rare)"
            )),
            FicheRow(concept="◆ Bilan de 1re intention", detail_md=(
                "- Échographie abdominale et voies biliaires\n"
                "- Sérologies hépatite B et C\n"
                "- Bilan métabolique : glycémie à jeun, EAL\n"
                "- Bilan martial : ferritinémie, **CST**\n"
                "- Électrophorèse des protides plasmatiques (EPP)\n"
                "- TSH\n"
                "- CPK"
            )),
            FicheRow(concept="", detail_md=(
                "- Rapport **ASAT/ALAT** :\n"
                "  - < 1 : cytolyse d'origine hépatique habituelle\n"
                "  - **> 1** : cytolyse musculaire, IDM, **cirrhose évoluée**, hépatopathie OH, ischémie hépatique"
            ), kind="a_retenir"),
            FicheRow(concept="★ Cytolyse aiguë > 10N", detail_md=(
                "- **Hépatite virale aiguë** : VHA, VHB, VHC, VHD, VHE, CMV, EBV, HSV, VZV\n"
                "- **Hépatite médicamenteuse** :\n"
                "  - Immuno-allergique : non dose-dépendante (anti-épileptiques, AINS, ATB, antituberculeux)\n"
                "  - Toxique : **dose-dépendante**, paracétamol ++\n"
                "- Hépatite toxique : amanite phalloïde, solvants\n"
                "- Hépatite auto-immune\n"
                "- **Migration lithiasique** : cytolyse rapidement régressive\n"
                "- Ischémie hépatique : foie de choc\n"
                "- Rares : maladie de Wilson, syndrome de Budd-Chiari aigu"
            )),
        ]),
        SousPartie(lettre="B", titre="Cholestase et augmentation isolée des GGT", rows=[
            FicheRow(concept="Cholestase", detail_md=(
                "- **Définition** : augmentation GGT, PAL +/- bilirubine conjuguée si prolongée\n"
                "- Normes :\n"
                "  - GGT : < 30 UI/L\n"
                "  - PAL : 32-104 UI/L (augmentation physiologique pendant grossesse et croissance ; "
                "augmentation en cas de métastases osseuses)"
            )),
            FicheRow(concept="Augmentation isolée des GGT", detail_md=(
                "- **Alcool** +++\n"
                "- Syndrome métabolique\n"
                "- Médicaments inducteurs enzymatiques : anti-épileptiques, rifampicine, contraceptifs oraux, "
                "corticoïdes, griséofulvine\n"
                "- Rares : lésion intra-hépatique, cholestase débutante, diabète, pathologie thyroïdienne\n"
                "- Bilan de 1re intention : échographie abdominale + bilan métabolique"
            )),
        ]),
        SousPartie(lettre="C", titre="Ictère à bilirubine non conjuguée et conjuguée", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- **Ictère** : coloration jaune des tissus par dépôt de bilirubine\n"
                "- Bilirubine totale : 5-17 µmol/L\n"
                "  - Bilirubine non conjuguée : < 15 µmol/L\n"
                "  - Bilirubine conjuguée : < 5 µmol/L\n"
                "- Sub-ictère : bilirubine > **30** µmol/L (conjonctives jaunes)\n"
                "- Ictère franc : bilirubine > **50** µmol/L"
            )),
            FicheRow(concept="Ictère à bilirubine non conjuguée", detail_md=(
                "- Urines claires, selles normales\n"
                "- **Hémolyse** et dysérythropoïèse\n"
                "- Diminution activité bilirubine glucuronide transférase : **syndrome de Gilbert** "
                "(ce n'est pas une maladie !)"
            )),
            FicheRow(concept="Ictère à bilirubine conjuguée", detail_md=(
                "- Urines foncées, selles décolorées\n"
                "- Orientation clinique :\n"
                "  - Ictère « nu » (pas de fièvre ni douleur) : évocateur de cause **tumorale**\n"
                "  - Fluctuant avec douleur biliaire/fièvre : évocateur de cause **lithiasique**\n"
                "  - Précédé d'un syndrome grippal : évocateur d'**hépatite virale** aiguë"
            )),
            FicheRow(concept="◆ Examens complémentaires", detail_md=(
                "- Biologie : NFS, hémostase (TP, TCA, facteur V, facteurs vitamino-K dépendants), "
                "BHC complet, ionogramme\n"
                "- **Échographie abdominale** en 1re intention :\n"
                "  - Cholestase extra-hépatique : **dilatation VBP > 6 mm**\n"
                "  - Cholestase intra-hépatique : absence de dilatation\n"
                "- 2e intention : bili-IRM, écho-endoscopie, TDM"
            )),
            FicheRow(concept="Cholestase extra-hépatique", detail_md=(
                "- Cancer tête du pancréas / cholangiocarcinome\n"
                "- **Lithiase VBP**\n"
                "- Pancréatite chronique\n"
                "- Compression VBP par ADP tumorales\n"
                "- Ampullome vatérien\n"
                "- Cholangite sclérosante primitive"
            )),
            FicheRow(concept="Cholestase intra-hépatique", detail_md=(
                "- Dysfonction hépatocytes : hépatites (virales, médicamenteuses, AI, OH), cirrhose, "
                "hémochromatose, Wilson, foie cardiaque, stéatose hépatique aiguë gravidique\n"
                "- Cholangite biliaire primitive\n"
                "- Compression canaux biliaires intra-hépatiques"
            )),
            FicheRow(concept="", detail_md=(
                "- **Urgences** associées à l'ictère : encéphalopathie bilirubinémique du nouveau-né, "
                "angiocholite, insuffisance hépatique (cirrhose, cancer foie, IH aiguë)"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE II : CIRRHOSE ──
    partie_ii = Partie(numero="II", titre="Cirrhose", sous_parties=[
        SousPartie(lettre="A", titre="Cirrhose non compliquée : diagnostic et étiologies", rows=[
            FicheRow(concept="Signes d'HTP", detail_md=(
                "- **HTP** : gradient de pression veine porte - veine cave > **4 mmHg**\n"
                "- Ascite\n"
                "- Splénomégalie\n"
                "- OMI\n"
                "- Circulation veineuse collatérale :\n"
                "  - Épigastrique\n"
                "  - Péri-ombilicale : syndrome de **Cruveilhier-Baumgarten**"
            )),
            FicheRow(concept="Signes d'IHC", detail_md=(
                "- > 5 **angiomes stellaires** prédominant partie supérieure du thorax\n"
                "- Ictère\n"
                "- Érythrose palmaire et plantaire\n"
                "- Troubles de conscience débutant par inversion du rythme nycthéméral et **astérixis**\n"
                "- Ongles blancs, foetor hépatique, hippocratisme digital\n"
                "- Hypogonadisme : aménorrhée (femme), gynécomastie et dépilation (homme)"
            )),
            FicheRow(concept="◆ Biologie", detail_md=(
                "- Hypersplénisme : **thrombopénie**, leuco-neutropénie +/- anémie\n"
                "- IHC : diminution TP et facteur V, augmentation INR, **hypoalbuminémie**, "
                "hypocholestérolémie, hyperbilirubinémie conjuguée\n"
                "- Augmentation enzymes hépatiques\n"
                "- Hyperferritinémie avec CST normale\n"
                "- **Hypergammaglobulinémie polyclonale**"
            )),
            FicheRow(concept="Écho-doppler hépatique", detail_md=(
                "- Foie : contours irréguliers, bosselés, nodulaires ; dysmorphie (hypertrophie foie gauche, "
                "atrophie foie droit) ; échostructure granité et hétérogène\n"
                "- HTP : diamètre veine porte > **12 mm**, voies de dérivation, flux **hépatofuge**, "
                "reperméabilisation veine ombilicale, splénomégalie\n"
                "- Complications : nodules suspects de CHC, thrombose porte"
            )),
            FicheRow(concept="FOGD", detail_md=(
                "- Varices oesophagiennes : cordons bleutés dans la paroi oesophagienne\n"
                "- Varices gastriques : cardio-tubérositaires/sous-cardiales\n"
                "- Gastropathie d'HTP : aspect en mosaïque"
            )),
            FicheRow(concept="PBH", detail_md=(
                "- **Pas toujours nécessaire** +++ : méthodes non invasives (Fibroscan, Fibrotest)\n"
                "- Indications : doute diagnostique, bilan étiologique négatif\n"
                "- Définition histologique : **fibrose annulaire** délimitant des **nodules de régénération**\n"
                "- Biopsie percutanée si : TP > 50%, plaquettes > 50 G/L, pas d'ascite volumineuse ; "
                "sinon voie transjugulaire"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "| Étiologie | Arguments diagnostiques |\n"
                "|-----------|------------------------|\n"
                "| **Alcool** (1re cause) | OH > 40 g/j (F), > 60 g/j (H) ; VGM augmenté ; ASAT/ALAT > 2 ; "
                "augmentation IgA, bloc béta-gamma EPP |\n"
                "| **VHB** | Ag HBs +, Ac anti-HBc +, Ac anti-HBs - |\n"
                "| **VHC** | Sérologie VHC + et PCR ARN VHC + |\n"
                "| **NASH** | Syndrome métabolique, pas d'OH, surpoids, diabète, hyperTG |\n"
                "| Hémochromatose | CST > 45%, hyperferritinémie, mutation C282Y gène HFE |\n"
                "| Hépatite AI | Femme, autres MAI, hypergammaglobulinémie IgG, Ac anti-noyaux/anti-actine (type I) "
                "ou anti-LKM1 (type II) |\n"
                "| CBP | Femme 50 ans, PAL augmentées, IgM augmentées, Ac anti-mitochondrie M2 |\n"
                "| CSP | Homme 40 ans, association MICI (RCH), pANCA, sténoses étagées voies biliaires en "
                "bili-IRM |\n"
            )),
        ]),
        SousPartie(lettre="B", titre="Score de Child-Pugh et prise en charge", rows=[
            FicheRow(concept="★ Score de Child-Pugh", detail_md=(
                "| Paramètre | 1 point | 2 points | 3 points |\n"
                "|-----------|---------|----------|----------|\n"
                "| Bilirubine (µmol/L) | < 35 | 35-50 | > 50 |\n"
                "| Albumine (g/L) | > 35 | 28-35 | < 28 |\n"
                "| TP (%) | > 50 | 40-50 | < 40 |\n"
                "| Ascite | Absente | Minime | Abondante |\n"
                "| Encéphalopathie | Absente | Grades I-II | Grades III-IV |\n\n"
                "- **Child A** : 5-6 points ; **Child B** : 7-9 ; **Child C** : 10-15"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- Traitement étiologique et prise en charge facteurs aggravants :\n"
                "  - **Sevrage OH complet** quelle que soit l'étiologie\n"
                "  - Contrôle surcharge pondérale, diabète, dyslipidémie\n"
                "- Prévention complications :\n"
                "  - VO stade 2-3 : **BB- non cardiosélectifs** / ligature si CI\n"
                "  - Vaccinations : VHA, VHB, grippe, pneumocoque, COVID\n"
                "  - Adapter posologies médicaments à métabolisme hépatique"
            )),
            FicheRow(concept="Transplantation hépatique", detail_md=(
                "- Indications : IHC sévère (TP < 50%, INR > 1,7), ascite réfractaire, +/- CHC petite taille\n"
                "- Si cirrhose OH : après **6 mois d'arrêt** complet d'OH\n"
                "- Si cirrhose virale B avec réplication : traitement antiviral préalable indispensable\n"
                "- CI : âge > 65-70 ans, affection extra-hépatique grave, ATCD récent cancer non hépatique, "
                "troubles psychiatriques compromettant le suivi"
            )),
        ]),
        SousPartie(lettre="C", titre="Hémorragie digestive sur HTP", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- **Mortalité > 30%**\n"
                "- Étiologies :\n"
                "  - HTP : **VO 60%** (FDR : taille VO, signes rouges, sévérité IHC), "
                "varices cardio-tubérositaires, gastropathie d'HTP\n"
                "  - UGD 15%\n"
                "  - Oesophagite, syndrome de Mallory-Weiss, tumeurs"
            )),
            FicheRow(concept="PEC initiale", detail_md=(
                "- **Réanimation** (proche plateau endoscopie)\n"
                "- O2 SpO2 > 92%, à jeun, scope, VVP, remplissage si hypotension\n"
                "- Transfusion si Hb < 7 g/dL ou mauvaise tolérance\n"
                "- Prévention : pneumopathie d'inhalation (position assise), **ATB prophylaxie** "
                "(norfloxacine 400 mg x 2/j ou C3G pendant 7 jours), prévention sevrage OH\n"
                "- **Drogues vasoactives IVSE** : octréotide ou terlipressine "
                "(CI si coronaropathie/AOMI), poursuivre 2-5 jours puis relais BB-"
            )),
            FicheRow(concept="FOGD en urgence", detail_md=(
                "- Dans les **12 heures** (patient hémodynamiquement stable)\n"
                "- **Érythromycine IV** 30-60 min avant pour vidange gastrique\n"
                "- Geste d'hémostase :\n"
                "  - VO : **ligature élastique**\n"
                "  - Varices gastriques : obturation à la **glue**\n"
                "- Récidive : nouvelle FOGD ; échec : **TIPS** (Child-Pugh < 12)\n"
                "- Hémorragie massive : **sonde de Blackmore** en attente TIPS"
            )),
            FicheRow(concept="", detail_md=(
                "- **Prévention primaire** : VO grade 2-3 → BB- non cardiosélectifs / ligature si CI\n"
                "- **Prévention secondaire** : séances de ligature jusqu'à éradication + BB- au long cours\n"
                "- Classification VO : grade 1 (s'efface à l'insufflation), grade 2 (ne s'efface pas, non confluentes), "
                "grade 3 (ne s'efface pas, confluentes)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Encéphalopathie hépatique et syndrome hépato-rénal", rows=[
            FicheRow(concept="Encéphalopathie hépatique", detail_md=(
                "- Encéphalopathie métabolique **sans lésion cérébrale organique**\n"
                "- Deux types :\n"
                "  - Primitive : liée IHC grave / shunts porto-caves\n"
                "  - Secondaire : médicaments (BZP ++, neuroleptiques, barbituriques)\n"
                "- Facteurs déclenchants : médicaments sédatifs, hémorragie digestive, "
                "infection, insuffisance rénale, hyponatrémie, **constipation**"
            )),
            FicheRow(concept="Stades de gravité", detail_md=(
                "| Stade | Clinique |\n"
                "|-------|----------|\n"
                "| I | Insomnie, confusion |\n"
                "| II | Abattement, comportement anormal |\n"
                "| III | Somnolence, désorientation |\n"
                "| IV | Coma |\n\n"
                "- Signes clés : **astérixis** (flapping tremor), **foetor hepaticus**, "
                "inversion rythme nycthéméral, syndrome confusionnel"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Toujours rechercher un **facteur déclenchant** : TR systématique "
                "(hémorragie digestive), bilan infectieux, dosage BZP\n"
                "- ⚠ Médicaments CI chez le cirrhotique : BZP, neuroleptiques, barbituriques"
            ), kind="piege"),
            FicheRow(concept="Syndrome hépato-rénal", detail_md=(
                "- **Complication la plus grave** de la cirrhose\n"
                "- IRA fonctionnelle sur cirrhose avec ascite réfractaire et IHC sévère (TP < 50%)\n"
                "- SHR type I : rapidement évolutif (< 15 jours) ; type II : peu évolutif\n"
                "- FDR : ponctions d'ascite > 3L non compensées, infection (ISLA), "
                "hépatite alcoolique aiguë, **AINS** ++++"
            )),
            FicheRow(concept="Diagnostic SHR", detail_md=(
                "- 4 critères majeurs **tous présents** :\n"
                "  - Créatinine > **133** µmol/L (SHR I) ; doublement en < 2 semaines pour atteindre "
                "**221** µmol/L (SHR II)\n"
                "  - Absence d'état de choc\n"
                "  - Absence d'amélioration après arrêt diurétiques et expansion volémique par albumine IV\n"
                "  - Pas d'atteinte rénale organique (protéinurie < 0,5 g/24h, écho rénale normale)\n"
                "- **Traitement** : remplissage IV albumine + vasoconstricteur (terlipressine/noradrénaline) ; "
                "transplantation hépatique en urgence"
            )),
        ]),
        SousPartie(lettre="E", titre="Ascite et infection du liquide d'ascite", rows=[
            FicheRow(concept="Diagnostic clinique", detail_md=(
                "- Épanchement libre dans la cavité péritonéale (hémopéritoine exclu)\n"
                "- Ascite < 2L : prise de poids récente, matité mobile et déclive\n"
                "- Ascite > 2L : abdomen distendu, diastasis grands droits, "
                "déplissement ombilic, signe du flot\n"
                "- Diagnostic étiologique : signes IHC/HTP (cirrhose), ICD, OMI, aires ganglionnaires"
            )),
            FicheRow(concept="Ponction d'ascite exploratrice", detail_md=(
                "- **Systématique** (échoguidée si doute)\n"
                "- Ponction en pleine matité : 1/3 externe ligne EIAS-ombilic\n"
                "- Examens : biochimie (**protides**, albumine, lipase, TG), "
                "bactériologie (tube standard + hémocultures), cytologie"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "| | Transsudat (protides < 25 g/L) | Exsudat (protides > 25 g/L) |\n"
                "|--|-------------------------------|-----------------------------|\n"
                "| Causes | **Cirrhose** +++, SN, anasarques | **Carcinose péritonéale**, tuberculose péritonéale |\n"
                "| Autres | Entéropathie exsudative, dénutrition | ICD, Budd-Chiari, ascite pancréatique, thrombose porte |\n\n"
                "- **Gradient albumine sérum-ascite > 11 g/L** : ascite liée à une **HTP**"
            )),
            FicheRow(concept="◆ PEC de l'ascite", detail_md=(
                "- Hospitalisation, rechercher et traiter facteur déclenchant\n"
                "- Arrêt médicaments hépatotoxiques\n"
                "- **Régime hyposodé** < 5 g/jour\n"
                "- **Spironolactone** en 1re intention +/- furosémide\n"
                "- Ponction évacuatrice si ascite tendue : **albumine 20 g / 3L** évacués à partir du 3e litre\n"
                "- Objectif : perte de poids 500 g - 1 kg/jour\n"
                "- Pas de restriction hydrique"
            )),
            FicheRow(concept="Infection spontanée du liquide d'ascite (ISLA)", detail_md=(
                "- Germes : **entérobactéries** le plus souvent\n"
                "- FDR : hémorragie digestive, hépatite alcoolique aiguë, **Child C**, protides ascite < 15 g/L\n"
                "- Clinique : fièvre/hypothermie, douleurs abdominales, diarrhées, +/- asymptomatique\n"
                "- Diagnostic positif : **PNN > 250/mm³** (culture négative dans 50%)"
            )),
            FicheRow(concept="", detail_md=(
                "- La ponction d'ascite exploratrice est une **urgence** devant toute décompensation de cirrhose\n"
                "- **PNN > 250/mm³** = ISLA jusqu'à preuve du contraire, traiter en urgence\n"
                "- Prévention primaire : **ciprofloxacine 500 mg/j** si Child C + protides ascite < 15 g/L"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Traitement ISLA", detail_md=(
                "- ATB 5-7 jours : **céfotaxime** 1g x 4/j IV, OU Augmentin 1g x 3/j IV, "
                "OU ofloxacine 200 mg x 2/j\n"
                "- **Albumine IV** : 1,5 g/kg à J1 et 1 g/kg à J3 (prévention SHR)\n"
                "- Prophylaxie secondaire : ciprofloxacine 500 mg/j au long cours\n"
                "- Contrôle : ponction d'ascite à 48h → diminution > 25% PNN"
            )),
        ]),
    ])

    # ── PARTIE III : HÉPATITES VIRALES ──
    partie_iii = Partie(numero="III", titre="Hépatites virales", sous_parties=[
        SousPartie(lettre="A", titre="Hépatites aiguës virales et hépatite fulminante", rows=[
            FicheRow(concept="Tableau clinique", detail_md=(
                "- **Asymptomatique** dans 80%\n"
                "- Forme classique :\n"
                "  - Phase pré-ictérique (5-15 j) : AEG, fièvre, syndrome grippal, douleurs HCD, "
                "arthralgies, urticaire\n"
                "  - Phase ictérique (4-8 j à 2-6 semaines) : ictère cutanéo-muqueux, "
                "urines foncées, selles décolorées, prurit\n"
                "- Biologie : cytolyse > **10N** prédominant sur ALAT, cholestase, "
                "augmentation bilirubine conjuguée\n"
                "- Surveillance **TP et facteur V** ++"
            )),
            FicheRow(concept="Sérologies virales", detail_md=(
                "| Virus | Marqueur diagnostique |\n"
                "|-------|----------------------|\n"
                "| VHA | **IgM anti-VHA** |\n"
                "| VHB | **IgM anti-HBc** +/- Ag HBs |\n"
                "| VHD | Ac anti-delta (si VHB connu) |\n"
                "| VHE | IgM anti-VHE / ARN VHE par PCR |\n"
                "| VHC | IgM anti-VHC +/- PCR ARN |\n"
            )),
            FicheRow(concept="★ Hépatite fulminante", detail_md=(
                "- Encéphalopathie hépatique dans les **2 semaines** après apparition de l'ictère, "
                "souvent TP < 50%\n"
                "- Concerne 1% hépatites B, 0,1% hépatite A, femmes enceintes pour VHE, "
                "**jamais** pour VHC\n"
                "- FDR : sujet âgé, OH, médicaments hépatotoxiques (paracétamol, AINS), "
                "co-infection B+D, immunodépression\n"
                "- **Transplantation hépatique en urgence** (USI à proximité centre de transplantation si TP < 50%)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Hépatite aiguë : **CI paracétamol** et tout médicament hépatotoxique/neurosédatif\n"
                "- Sub-fulminante si délai > 2 semaines ; hépatite aiguë sévère si baisse TP sans encéphalopathie"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Hépatite B : aiguë et chronique", rows=[
            FicheRow(concept="Généralités VHB", detail_md=(
                "- Incubation : 60-110 jours\n"
                "- Transmission : **sexuelle**, parentérale (sang), verticale (mère-enfant), "
                "contact familial (objets de toilette)\n"
                "- VHB responsable **75% des CHC**\n"
                "- Passage à la chronicité : adultes < 5%, enfants 25%, **NN > 90%**"
            )),
            FicheRow(concept="Profils sérologiques VHB", detail_md=(
                "| Situation | Ag HBs | Ac anti-HBs | Ac anti-HBc | ADN VHB |\n"
                "|-----------|--------|-------------|-------------|----------|\n"
                "| Hépatite aiguë | + | - | IgM + | + |\n"
                "| Guérison | - | **+** | IgG + | - |\n"
                "| Vaccination | - | **+** | **-** | - |\n"
                "| Porteur inactif | + | - | IgG + | < 2000 UI/mL |\n"
                "| Hépatite chronique | + | - | IgG + | > 2000 UI/mL |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- **Vaccination** = Ac anti-HBs + isolé (Ac anti-HBc **négatif**)\n"
                "- **Guérison** = Ac anti-HBs + ET Ac anti-HBc + (IgG)\n"
                "- Ag HBs **persistant > 6 mois** = infection chronique"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Indications de traitement VHB chronique", detail_md=(
                "- **Cirrhose** (quelque soit charge virale et bilan hépatique)\n"
                "- Hépatite B chronique avec fibrose modérée\n"
                "- Charge virale > 20 000 UI/mL + cytolyse > 2N\n"
                "- Traitement : **analogues nucléos(t)idiques** (ténofovir/entécavir) au long cours "
                "OU interféron pégylé durée limitée"
            )),
        ]),
        SousPartie(lettre="C", titre="Hépatite C : aiguë et chronique", rows=[
            FicheRow(concept="Généralités VHC", detail_md=(
                "- 6 génotypes (les plus fréquents en France : 1, 2, 3, 4)\n"
                "- Incubation : 7-8 semaines\n"
                "- Transmission : **parentérale** ++, verticale, sexuelle rare\n"
                "- Population à risque : toxicomanes IV, détenus, VIH+\n"
                "- Évolution : guérison 20-30%, **hépatite C chronique 70-80%**"
            )),
            FicheRow(concept="Score METAVIR", detail_md=(
                "| Activité | Fibrose |\n"
                "|----------|---------|\n"
                "| A0 : pas d'activité | F0 : pas de fibrose |\n"
                "| A1 : minime | F1 : fibrose portale sans septa |\n"
                "| A2 : modérée | F2 : fibrose portale + quelques septa |\n"
                "| A3 : sévère | F3 : fibrose septale sans cirrhose |\n"
                "| | **F4 : cirrhose** |\n"
            )),
            FicheRow(concept="Traitement VHC chronique", detail_md=(
                "- Indication : **tous les patients** avec infection chronique VHC\n"
                "- Parcours simplifié si : pas de co-infection VHB/VIH, pas d'IR sévère, "
                "pas de maladie hépatique sévère, Fibroscan < 10 kPa\n"
                "- **Epclusa** (velpatasvir + sofosbuvir) 1 cp/j x 12 semaines OU "
                "**Maviret** (glécaprévir + pibrentasvir) 3 cp/j x 8 semaines\n"
                "- Vérifier absence d'**interaction médicamenteuse** +++\n"
                "- Contrôle : charge virale à 12 semaines post-traitement → "
                "ARN indétectable = guérison définitive"
            )),
            FicheRow(concept="◆ Dépistage VHC", detail_md=(
                "- Personnes transfusées avant 1992\n"
                "- Usagers de drogues\n"
                "- ATCD hospitalisation pour soins majeurs (dialyse, transplantation)\n"
                "- ATCD tatouage/acupuncture\n"
                "- Proche porteur VHC"
            )),
        ]),
        SousPartie(lettre="D", titre="Hépatites A, D et E", rows=[
            FicheRow(concept="Hépatite A", detail_md=(
                "- Transmission **oro-fécale**, incubation 2-4 semaines\n"
                "- Asymptomatique 80%, **pas de passage à la chronicité**\n"
                "- Diagnostic : **IgM anti-VHA** ; guérison : IgG anti-VHA\n"
                "- **Déclaration obligatoire**\n"
                "- Prévention : hygiène + vaccination avant voyage en zone d'endémie"
            )),
            FicheRow(concept="Hépatite D", detail_md=(
                "- Virus ARN **défectif** nécessitant le VHB pour se multiplier\n"
                "- Co-infection VHB+VHD : risque hépatite fulminante 5%\n"
                "- Surinfection : évolution chronique dans **90%**, risque accru cirrhose et CHC\n"
                "- Diagnostic : Ac anti-delta + ARN delta par PCR"
            )),
            FicheRow(concept="Hépatite E", detail_md=(
                "- Contamination oro-fécale, réservoir humain/animal/environnemental\n"
                "- De plus en plus fréquent en France\n"
                "- Rares passages à la chronicité\n"
                "- Diagnostic : Ac anti-VHE, ARN VHE par RT-PCR (référence)\n"
                "- Pas de vaccin disponible"
            )),
        ]),
    ])

    # ── PARTIE IV : PATHOLOGIE GASTRO-DUODÉNALE ET RGO ──
    partie_iv = Partie(numero="IV", titre="Pathologie gastro-duodénale et RGO", sous_parties=[
        SousPartie(lettre="A", titre="Ulcère gastro-duodénal", rows=[
            FicheRow(concept="Épidémiologie", detail_md=(
                "- 90 000 nouveaux cas/an en France, incidence en diminution\n"
                "- Mortalité complications ulcéreuses : 2-10%\n"
                "- UD plus fréquent que UG avant 55 ans, sex ratio 2H/1F\n"
                "- Étiologies : **H. pylori** (Gram -, oro-orale/féco-orale), **AINS/aspirine**, "
                "syndrome de Zollinger-Ellison (rare), tabac, Crohn"
            )),
            FicheRow(concept="★ Douleur ulcéreuse typique", detail_md=(
                "- Siège **épigastrique**, type crampe/« faim douloureuse »\n"
                "- **Post-prandial tardif** (1-3h après repas), nocturne\n"
                "- Soulagée par alimentation, antiacides, lait\n"
                "- **Périodicité** : 2-4 semaines de douleur puis rémission semaines/mois\n"
                "- Douleurs atypiques fréquentes, asymptomatique possible"
            )),
            FicheRow(concept="FOGD : diagnostic positif", detail_md=(
                "- Visualisation tractus digestif jusqu'à D2\n"
                "- Siège : duodénale (bulbe ++) ou gastrique (antre, petite courbure)\n"
                "- **Biopsies** +++ :\n"
                "  - Antrales et fundiques systématiques → recherche **H. pylori** (anatomopathologie, "
                "culture, PCR)\n"
                "  - **Berges si UG** car risque de cancer"
            )),
            FicheRow(concept="Traitement UGD", detail_md=(
                "| Situation | Traitement |\n"
                "|-----------|------------|\n"
                "| UGD à H. pylori + | Éradication HP (quadrithérapie bismuthée ou traitement concomitant ou orienté par ATBG) "
                "+ contrôle éradication à 4 sem post-ATB |\n"
                "| UD HP+ compliqué | Éradication + IPP pleine dose 6 sem |\n"
                "| UG HP+ | Éradication + IPP pleine dose 6 sem + **FOGD contrôle à 6-8 sem** avec biopsies |\n"
                "| UGD HP- | IPP simple dose 4 sem (UD) / 8 sem (UG) |\n"
                "| Poursuite AINS/aspirine | IPP demi-dose au long cours |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Contrôle éradication H. pylori **systématique** (30% échec) : 4 semaines après fin ATB "
                "et 2 semaines après fin IPP → **test respiratoire à l'urée marquée** ou biopsies\n"
                "- IPP préventif si AINS + : âge > 65 ans, ATCD UGD, AAP/anticoagulant/corticoïdes associés"
            ), kind="a_retenir"),
            FicheRow(concept="Complications", detail_md=(
                "- **Hémorragie** (10% mortalité) : classification de **Forrest** (Ia-Ib hémorragie active ; "
                "IIa-IIb risque récidive ; IIc-III faible risque) → IPP IVSE 72h + hémostase endoscopique\n"
                "- **Perforation** : douleur épigastrique en « coup de poignard », pneumopéritoine, "
                "**CI absolue à la FOGD**, urgence chirurgicale\n"
                "- Sténose pyloro-duodénale : vomissements alimentaires tardifs, clapotage à jeun\n"
                "- Cancérisation : uniquement UG (2%)"
            )),
        ]),
        SousPartie(lettre="B", titre="Gastrites et gastropathies", rows=[
            FicheRow(concept="Gastrite à H. pylori", detail_md=(
                "- Gastrite chronique atrophiante → peut évoluer vers **lymphome gastrique du MALT**\n"
                "- Diagnostic histologique par biopsies + recherche HP\n"
                "- Traitement : éradication H. pylori"
            )),
            FicheRow(concept="Maladie de Biermer", detail_md=(
                "- Gastrite chronique auto-immune avec **atrophie fundique**\n"
                "- Ac anti-cellules pariétales et **anti-facteur intrinsèque**\n"
                "- Femme > 50 ans, contexte auto-immunité (diabète type 1, thyroïdite, vitiligo)\n"
                "- Stade atrophie sévère : **carence B12** → anémie macrocytaire "
                "(B12 IM à vie), carence martiale (achlorhydrie)\n"
                "- Risques : ADK gastrique, tumeurs endocrines du corps gastrique (ECL-omes)\n"
                "- Surveillance : FOGD tous les **3 ans** si < 70 ans et bon état général"
            )),
            FicheRow(concept="Gastropathies", detail_md=(
                "- **Absence d'infiltrat inflammatoire** (contrairement aux gastrites)\n"
                "- Gastropathie aux AINS : lésions multiples (pétéchies, érosions, ulcères)\n"
                "- Gastropathie chimique : alcool, reflux biliaire\n"
                "- Gastropathie d'HTP : ectasies vasculaires antrales\n"
                "- Syndrome de Zollinger-Ellison : hyperplasie glandes fundiques sous action gastrine"
            )),
        ]),
        SousPartie(lettre="C", titre="Reflux gastro-oesophagien", rows=[
            FicheRow(concept="Diagnostic clinique", detail_md=(
                "- Concerne 20-40% population adulte\n"
                "- Symptômes typiques (diagnostic positif clinique) :\n"
                "  - **Pyrosis** : brûlure rétrosternale ascendante à point de départ épigastrique\n"
                "  - **Régurgitations acides** : remontée liquide gastrique sans effort de vomissement\n"
                "- Majorés par antéflexion/décubitus, post-prandiaux\n"
                "- Survenue nocturne : marqueur de **sévérité**"
            )),
            FicheRow(concept="Signes atypiques", detail_md=(
                "- Toux, dyspnée asthmatiforme, enrouement\n"
                "- Gingivites, caries à répétition\n"
                "- Laryngite postérieure\n"
                "- Douleurs précordiales\n"
                "- **Signes d'alarme** : dysphagie, AEG, hémorragie digestive, anémie"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- **FOGD** : indiquée si âge > 50 ans, signes d'alarme, résistance au traitement, "
                "symptômes atypiques isolés\n"
                "  - Diagnostic d'oesophagite peptique ; normale dans 30-50% des RGO\n"
                "- **pH-métrie 24h** sans IPP : 2e intention après FOGD normale si symptômes atypiques, "
                "résistants, ou bilan pré-opératoire\n"
                "- pH-impédancemétrie : reflux peu/non acide sous IPP\n"
                "- Manométrie oesophagienne : bilan pré-opératoire, suspicion troubles moteurs"
            )),
            FicheRow(concept="Stratégie thérapeutique", detail_md=(
                "| Situation | Traitement |\n"
                "|-----------|-----------|\n"
                "| Symptômes typiques espacés (< 1/sem) | Antiacides/alginates à la demande |\n"
                "| Symptômes typiques rapprochés (> 1/sem) | **IPP demi-dose** 4 semaines |\n"
                "| Échec IPP demi-dose | FOGD + IPP **pleine dose** 8 semaines |\n"
                "| Oesophagite sévère (Los Angeles C/D) | IPP dose 8 sem + IPP dose minimale au long cours + FOGD contrôle |\n"
                "| RGO résistant aux IPP | FOGD + vérifier observance + pH-impédancemétrie |\n"
            )),
            FicheRow(concept="Traitement chirurgical", detail_md=(
                "- Indications : récidive à l'arrêt du traitement médical, symptômes persistants malgré "
                "traitement bien conduit, volumineuse hernie hiatale\n"
                "- **Fundoplicature de Nissen** (complète) ou Toupet (hémifundoplicature)\n"
                "- CI : troubles moteurs oesophagiens (achalasie, sclérodermie)"
            )),
            FicheRow(concept="Complications", detail_md=(
                "- **Oesophagite peptique** : classification de **Los Angeles** "
                "(A/B = non sévère ; C/D = sévère)\n"
                "- **Sténose peptique** : dysphagie, IPP pleine dose +/- dilatation endoscopique\n"
                "- **Endobrachyoesophage (Barrett)** : métaplasie glandulaire intestinale = "
                "**état pré-cancéreux** (risque ADK oesophagien) → IPP à vie si symptomatique + "
                "surveillance FOGD avec biopsies étagées"
            )),
        ]),
    ])

    # ── PARTIE V : PATHOLOGIE BILIAIRE ET PANCRÉATIQUE ──
    partie_v = Partie(numero="V", titre="Pathologie biliaire et pancréatique", sous_parties=[
        SousPartie(lettre="A", titre="Lithiase biliaire : colique hépatique et cholécystite", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Prévalence 20%, 2F/1H, pic 60 ans\n"
                "- Types : cholestéroliques (80%) et pigmentaires (20%)\n"
                "- FDR lithiase cholestérolique : âge > 60 ans, sexe féminin, obésité, "
                "hyperTG, jeûne prolongé, grossesse, fibrates, contraception orale\n"
                "- FDR lithiase pigmentaire : hémolyse chronique (drépanocytose, thalassémie), cirrhose"
            )),
            FicheRow(concept="Colique hépatique", detail_md=(
                "- Douleur **épigastrique/HCD**, début brutal, intense, continue, < 6h\n"
                "- Irradiation omoplate/épaule droite, inhibe inspiration forcée\n"
                "- **Signe de Murphy** : douleur avec blocage inspiratoire à la palpation HCD\n"
                "- Pas de défense, pas d'ictère, pas de fièvre\n"
                "- Biologie normale, échographie abdominale (référence) : "
                "calcul hyperéchogène avec cône d'ombre postérieur\n"
                "- Traitement : antispasmodiques, antalgiques puis **cholécystectomie sous coelioscopie** à 1 mois"
            )),
            FicheRow(concept="Cholécystite aiguë", detail_md=(
                "- Douleur identique colique hépatique mais **> 6 heures**\n"
                "- **Fièvre 38,5°C**, signe de Murphy, défense HCD, **pas d'ictère**\n"
                "- Biologie : hyperleucocytose à PNN, CRP augmentée, BHC et lipase normales\n"
                "- Échographie en urgence : parois vésiculaires épaissies > **4 mm**, "
                "vésicule augmentée de volume, Murphy échographique\n"
                "- **Urgence médico-chirurgicale** :\n"
                "  - ATB IV : Augmentin +/- aminosides\n"
                "  - Grade I/II : cholécystectomie sous coelioscopie dans les **24 heures**\n"
                "  - Grade III : drainage transcutané puis cholécystectomie à distance"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Cholécystite = fièvre + douleur > 6h ; colique hépatique = pas de fièvre + douleur < 6h\n"
                "- ⚠ Cholécystite : BHC et lipase **normales** (sinon évoquer migration lithiasique)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Lithiase de la VBP et angiocholite", rows=[
            FicheRow(concept="Lithiase VBP", detail_md=(
                "- 90% : calculs vésiculaires ayant migré dans la VBP\n"
                "- Asymptomatique 30%, sinon douleur type colique hépatique et/ou ictère\n"
                "- Échographie : **dilatation VBP > 8 mm**\n"
                "- Bilan complémentaire : **bili-IRM** (non invasif, visualise calculs > 3 mm) "
                "ou écho-endoscopie sous AG\n"
                "- Traitement : **CPRE** avec sphinctérotomie + extraction du calcul"
            )),
            FicheRow(concept="Angiocholite", detail_md=(
                "- **Triade de Charcot** (dans l'ordre) :\n"
                "  - 1. Douleur de colique hépatique\n"
                "  - 2. **Fièvre**\n"
                "  - 3. **Ictère cholestatique** fluctuant\n"
                "- Hémocultures positives dans **70%**\n"
                "- Échographie : dilatation voies biliaires intra et extra-hépatiques"
            )),
            FicheRow(concept="◆ PEC angiocholite", detail_md=(
                "- Hospitalisation en urgence, à jeun, antalgiques\n"
                "- ATB IV : Augmentin + aminosides OU C3G + Flagyl + aminosides (10-14 j)\n"
                "- **CPRE** selon gravité :\n"
                "  - Grade III (sévère) : < 12-24h\n"
                "  - Grade II (modérée) : 24-72h\n"
                "  - Grade I (légère) : délai rapide\n"
                "- Cholécystectomie dans un 2e temps"
            )),
        ]),
        SousPartie(lettre="C", titre="Pancréatite aiguë", rows=[
            FicheRow(concept="Étiologies", detail_md=(
                "- **Alcool** (40%) et **biliaire** (40%) = principales causes\n"
                "- Métabolique : hypercalcémie > 3 mmol/L, hypertriglycéridémie > 10 mmol/L\n"
                "- Médicamenteuse, toxique (cannabis), tumorale (TIPMP)\n"
                "- Post-CPRE, pancréatite auto-immune, génétique (SPINK1, PRSS1, CFTR)\n"
                "- Idiopathique si aucune cause retrouvée"
            )),
            FicheRow(concept="★ Tableau clinique", detail_md=(
                "- Douleur pancréatique typique : **épigastrique**, intense, en **barre**, **transfixiante**, "
                "irradiant dans le dos, position antalgique en **chien de fusil**\n"
                "- NV, iléus réflexe, météorisme, défense épigastrique\n"
                "- Signes de gravité : signe de **Cullen** (ecchymoses péri-ombilicales), "
                "signe de **Grey Turner** (ecchymoses des flancs)"
            )),
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- **2 des 3 critères** suivants :\n"
                "  - Douleur de pancréatite aiguë\n"
                "  - **Lipase > 3N**\n"
                "  - Pancréatite aiguë au scanner\n"
                "- La clinique et la biologie suffisent ; scanner non utile au diagnostic sauf si lipase < 3N "
                "ou douleur atypique"
            )),
            FicheRow(concept="◆ Évaluation de la gravité", detail_md=(
                "- **SRIS** initial ou persistant à 48h : T < 36 ou > 38°C, FC > 90, FR > 20, "
                "leucocytes > 12 000 ou < 4 000\n"
                "- CRP > **150 mg/L** au 2e jour\n"
                "- Scanner pancréatique entre **72e et 96e heure** (score CTSI > 4)\n"
                "- Les scores de Ranson et Imrie ne sont **plus utilisés**"
            )),
            FicheRow(concept="PEC", detail_md=(
                "- Hospitalisation (médecine si bénigne, réanimation si sévère)\n"
                "- Antalgiques, antiémétiques, HBPM prophylactique +++\n"
                "- Jeûne strict puis reprise alimentaire sans graisse dès diminution des douleurs\n"
                "- PA sévère : nutrition entérale par sonde naso-gastrique/jéjunale\n"
                "- **PAS d'ATB prophylactique**"
            )),
            FicheRow(concept="", detail_md=(
                "- Origine **biliaire** bénigne : cholécystectomie avec cholangiographie per-opératoire "
                "au cours de la même hospitalisation\n"
                "- Biliaire + angiocholite/ictère obstructif : ATB + **CPRE en urgence** + "
                "cholécystectomie à distance\n"
                "- Biliaire grave : CPRE + sphinctérotomie dans les **72h**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Pancréatite chronique", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Fibrose progressive du parenchyme pancréatique : exocrine puis endocrine\n"
                "- Prédominance masculine (SR = 8), âge moyen 40 ans\n"
                "- Étiologie principale : **alcool** (80-90%), consommation > 10 ans\n"
                "- FDR indépendant : **tabagisme**\n"
                "- Autres : obstructives (TIPMP), auto-immune (IgG4), génétique (mucoviscidose), "
                "idiopathique (10%)"
            )),
            FicheRow(concept="Histoire naturelle", detail_md=(
                "- Phase 1 (0-5 ans) : douleurs chroniques et **poussées de PA**, complications aiguës\n"
                "- Phase 2 (5-10 ans) : diminution douleurs, disparition poussées de PA\n"
                "- Phase 3 (> 10 ans) : plus de douleur, **insuffisance pancréatique exocrine et endocrine**"
            )),
            FicheRow(concept="◆ Diagnostic", detail_md=(
                "- **TDM abdominale** en 1re intention : calcifications pancréatiques "
                "(pathognomoniques), dilatation Wirsung, atrophie/augmentation volume pancréas\n"
                "- Biologie : glycémie à jeun + HbA1c, BHC, lipasémie si douleur, "
                "**élastase fécale** effondrée si insuffisance exocrine\n"
                "- 2e intention : wirsungo-IRM, écho-endoscopie bilio-pancréatique"
            )),
            FicheRow(concept="Complications", detail_md=(
                "- **Pseudo-kystes** : abstention ++ ; si > 6 cm ou complications → drainage "
                "par prothèse kysto-gastrique (écho-endoscopie)\n"
                "- **Insuffisance pancréatique exocrine** (> 10 ans) : malabsorption, stéatorrhée, "
                "carences vitamines liposolubles (A, D, K) et B12 → extraits pancréatiques gastroprotégés\n"
                "- **Diabète** (> 10 ans) : souvent insulino-requérant, hypoglycémies fréquentes\n"
                "- Dénutrition, ostéoporose\n"
                "- ADK pancréatique : évoquer si réapparition douleur à phase tardive/AEG\n"
                "- Complications du terrain **éthylo-tabagique** ++++ (ORL, pulmonaire, CV, hépatique)"
            )),
        ]),
    ])

    # ── PARTIE VI : URGENCES ET PATHOLOGIES FONCTIONNELLES DIGESTIVES ──
    partie_vi = Partie(numero="VI", titre="Urgences et pathologies fonctionnelles digestives", sous_parties=[
        SousPartie(lettre="A", titre="Hémorragies digestives", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Plus fréquent chez l'homme, âge médian 70 ans\n"
                "- Mortalité : HD hautes 3-10%, HD basses 2-8%\n"
                "- HD hautes (80%) > HD basses (20%)\n"
                "- Diagnostic positif :\n"
                "  - **Hématémèse** : hémorragie digestive haute\n"
                "  - **Méléna** : sang digéré noir et fétide (en amont angle colique droit)\n"
                "  - **Rectorragies** : sang rouge vif (HD basse ++ mais aussi haute)"
            )),
            FicheRow(concept="HD haute : étiologies et PEC", detail_md=(
                "- **UGD** (30-60%) : aspirine/AINS/anticoagulants dans 50%\n"
                "- **HTP / VO** (20%)\n"
                "- Érosions gastriques/duodénales (20%)\n"
                "- Oesophagite, syndrome de **Mallory-Weiss** (10%) : déchirure jonction oeso-gastrique "
                "post-vomissements\n"
                "- Angiodysplasies (5%), cancer (5%)\n"
                "- PEC : FOGD en urgence < **12-24h** après érythromycine IV ; "
                "hémostase endoscopique (clips, coagulation, sérum adrénaliné)"
            )),
            FicheRow(concept="Classification de Forrest", detail_md=(
                "| Stade | Description | Risque récidive |\n"
                "|-------|-------------|----------------|\n"
                "| Ia | Hémorragie en jet | Élevé |\n"
                "| Ib | Suintement diffus | Élevé |\n"
                "| IIa | Vaisseau visible non hémorragique | Moyen |\n"
                "| IIb | Caillot adhérent | Moyen |\n"
                "| IIc | Taches pigmentées | Faible |\n"
                "| III | Cratère à fond propre | Faible |\n"
            )),
            FicheRow(concept="HD basse : étiologies", detail_md=(
                "- **Hémorragie diverticulaire** (30-40%) : rectorragies indolores, arrêt spontané 80%\n"
                "- Colites inflammatoire/ischémique/infectieuse (30%)\n"
                "- Angiodysplasies coliques (5%) : sujet âgé, colon droit/caecum\n"
                "- Cancer colo-rectal (5%)\n"
                "- Causes grêliques (5-10%) : angiodysplasies, diverticule de Meckel, tumeurs GIST\n"
                "- Causes proctologiques (5-10%) : hémorroïdes internes, fissure"
            )),
        ]),
        SousPartie(lettre="B", titre="Péritonite aiguë", rows=[
            FicheRow(concept="Classification de Hambourg", detail_md=(
                "- **Primaire** : infection spontanée mono-bactérienne (ascite cirrhotique, dialyse péritonéale) "
                "→ traitement médical\n"
                "- **Secondaire** (90%) : perforation viscère/infection intra-abdominale "
                "(appendicite, diverticulite, perforation UGD, cholécystite) → poly-microbienne → chirurgie\n"
                "- **Tertiaire** : infection abdominale persistante malgré traitement bien conduit"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Douleur abdominale intense, généralisée ou localisée, début brutal/progressif\n"
                "- Signes péritonéaux : **contracture abdominale** +++, douleur cul-de-sac de Douglas au TR\n"
                "- Fièvre/hypothermie, troubles du transit (NV, arrêt matières et gaz)\n"
                "- Recherche tympanisme pré-hépatique (pneumopéritoine)\n"
                "- Signes de gravité : sepsis sévère, choc septique, défaillance multi-viscérale"
            )),
            FicheRow(concept="◆ Orientation étiologique", detail_md=(
                "| | Appendiculaire | Perforation UGD | Diverticulite |\n"
                "|--|---------------|-----------------|---------------|\n"
                "| Début | Progressif | **Brutal** | Progressif |\n"
                "| Maximum | FID | Épigastre | FIG |\n"
                "| Fièvre | Oui | Non au début | Oui |\n"
                "| Pneumopéritoine | Non | Oui | Oui |\n"
            )),
            FicheRow(concept="PEC", detail_md=(
                "- Hospitalisation en urgence (chirurgie/réanimation)\n"
                "- À jeun, antalgiques, IPP IV\n"
                "- **ATB** dès indication opératoire : Augmentin + aminosides OU C3G + Flagyl + aminosides "
                "(5-10 jours)\n"
                "- **Chirurgie en urgence** : laparotomie/coelioscopie, prélèvements bactériologiques, "
                "traitement du facteur causal, lavage abondant au sérum physiologique\n"
                "- NB : péritonites primaire et tertiaire souvent traitement médical seul"
            )),
        ]),
        SousPartie(lettre="C", titre="Syndrome occlusif", rows=[
            FicheRow(concept="Diagnostic clinique", detail_md=(
                "- Triade : **arrêt matières et gaz** (signe le plus spécifique), douleurs abdominales, "
                "NV (soulagent les douleurs)\n"
                "- Météorisme abdominal (75%), tympanisme, BHA diminués/absents\n"
                "- Retentissement : DEC/DIC, tachycardie, fièvre"
            )),
            FicheRow(concept="Strangulation vs obstruction", detail_md=(
                "| | Strangulation | Obstruction | Fonctionnelle |\n"
                "|--|--------------|-------------|---------------|\n"
                "| Douleur | Aiguë, brutale, constante | Progressive, spasmes | Progressive |\n"
                "| Arrêt transit | Rapide | Progressif | Rapide |\n"
                "| Vomissements | Précoces, clairs | Tardifs, fécaloïdes | Inconstants |\n"
                "| Météorisme | Variable | Important si colon | Variable |\n"
            )),
            FicheRow(concept="◆ Examens complémentaires", detail_md=(
                "- Biologie : NFS, CRP, ionogramme, créatinine, **lactates**, bilan pré-opératoire\n"
                "- **Scanner abdomino-pelvien** sans et avec injection : confirmation occlusion, "
                "localisation (jonction plat/dilaté), étiologie, signes de gravité\n"
                "- Signes de gravité scanner : diamètre caecum > **12 cm**, absence de rehaussement paroi "
                "(ischémie), pneumatose pariétale, aéroportie, pneumopéritoine\n"
                "- **AUCUNE indication de l'ASP**"
            )),
            FicheRow(concept="PEC", detail_md=(
                "- Hospitalisation, à jeun, VVP, correction hydro-électrolytique\n"
                "- **SNG en aspiration** systématique\n"
                "- Antalgiques, antispasmodiques IV (éviter morphiniques), IPP IV\n"
                "- Chirurgie si : complication, mauvaise tolérance, absence d'amélioration, "
                "signes de gravité, hernie étranglée\n"
                "- **Occlusion sur brides** : cause la plus fréquente (ATCD chirurgie abdominale) → "
                "traitement médical 6-12h si pas de gravité, sinon chirurgie"
            )),
        ]),
        SousPartie(lettre="D", titre="Diarrhées aiguës infectieuses", rows=[
            FicheRow(concept="Profils syndromiques", detail_md=(
                "| Syndrome | Caractéristiques | Étiologies |\n"
                "|----------|-----------------|------------|\n"
                "| **Gastro-entéritique** | Peu sévère, pas de glaire/sang, évolution 1-3 j | "
                "Calicivirus (adulte), Rotavirus (enfant) |\n"
                "| **Cholériforme** | Diarrhée profuse afécale « eau de riz », risque déshydratation | "
                "TIAC (S. aureus, C. perfringens), choléra, tourista (E. coli) |\n"
                "| **Dysentérique** | Glaire, sang, pus, syndrome rectal, fièvre | "
                "Campylobacter, Shigella, Salmonella, E. coli invasif |\n"
            )),
            FicheRow(concept="Colite à C. difficile", detail_md=(
                "- Diarrhée fébrile sous ATB / persistante 48h après arrêt / jusqu'à 2 mois après\n"
                "- Diagnostic : recherche **toxine A/B** dans selles ; "
                "recto-sigmoïdoscopie : **fausses membranes** (pathognomonique)\n"
                "- Traitement : arrêt ATB responsable, **vancomycine PO** 125 mg x 4/j pendant 10 jours ; "
                "fidaxomicine si risque de récidive\n"
                "- Récidive 15-30%, risque de colectasie"
            )),
            FicheRow(concept="", detail_md=(
                "- **Aucun examen complémentaire** dans la majorité des cas\n"
                "- Examens seulement si : syndrome dysentérique, diarrhée > 3 j, déshydratation sévère, "
                "sepsis grave, immunodéprimé, TIAC\n"
                "- **Loperamide** : uniquement après avoir éliminé une infection bactérienne invasive"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="E", titre="Diverticulose colique et diverticulite", rows=[
            FicheRow(concept="Définitions", detail_md=(
                "- **Diverticule** : hernie muqueuse/sous-muqueuse à travers paroi musculaire du côlon\n"
                "- **Diverticulose** : présence de diverticules non inflammatoires (asymptomatique, aucun traitement)\n"
                "- **Diverticulite** : inflammation/infection d'un diverticule +/- complications\n"
                "- FDR : âge > 50 ans (60-70 ans ++), AINS ; protecteurs : fibres alimentaires, activité physique"
            )),
            FicheRow(concept="Diverticulite aiguë", detail_md=(
                "- Fièvre 38-39°C, douleur **FIG** +++ (mais FID possible si boucle sigmoïdienne)\n"
                "- Défense FIG, douleur à la décompression (irritation péritonéale)\n"
                "- **Scanner abdomino-pelvien** en urgence (max 72h) : diverticules, épaississement paroi > 4 mm, "
                "infiltration graisse péri-colique\n"
                "- Signes de gravité scanner : bulles d'air extra-digestives, abcès, pneumopéritoine"
            )),
            FicheRow(concept="PEC diverticulite non compliquée", detail_md=(
                "- **Ambulatoire** le plus souvent +++\n"
                "- Repos digestif limité puis régime sans résidu\n"
                "- Antalgiques, antispasmodiques ; **AINS CI** !!!\n"
                "- **ATB pas systématique** : pas d'ATB si absence de signes de gravité, "
                "pas d'immunodépression, ASA < 3, pas de grossesse\n"
                "- Si échec symptomatique : Augmentin 7 jours (ou FQ + métronidazole si allergie)\n"
                "- Coloscopie à distance si forme compliquée"
            )),
            FicheRow(concept="Complications", detail_md=(
                "- **Abcès sigmoïdien** (1/3) : drainage radiologique/chirurgical si > 3 cm\n"
                "- **Péritonite** : urgence chirurgicale (résection sigmoïdienne + Hartmann/stomie)\n"
                "- **Fistules** (10%) : colo-vésicales (> 50%) → pneumaturie, fécalurie, "
                "infections urinaires récidivantes\n"
                "- Hémorragie diverticulaire : indépendante des poussées de diverticulite"
            )),
        ]),
        SousPartie(lettre="F", titre="Colopathie fonctionnelle", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Syndrome de l'intestin irritable (SII) : douleurs abdominales associées à des "
                "troubles du transit **sans maladie organique digestive**\n"
                "- 4 sous-types : SII-D (diarrhée), SII-C (constipation), SII-A (alternance), SII-I (indéterminé)\n"
                "- Terrain : femme d'âge jeune/moyen, troubles anxio-dépressifs"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- **Absence d'AEG**\n"
                "- Douleurs abdominales chroniques > 6 mois : spasmes, FIG ++, "
                "intermittentes, matinales/post-prandiales, absentes la nuit, "
                "soulagées par émission selles/gaz\n"
                "- Ballonnements abdominaux post-prandiaux\n"
                "- Troubles du transit : constipation/diarrhée/alternance\n"
                "- **Signes d'alarme** : âge > 50 ans, amaigrissement, symptômes nocturnes, "
                "rectorragies, anémie, ATCD familiaux CCR"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- **Aucun** +++\n"
                "- Coloscopie si signes d'alarme\n"
                "- Si diarrhée : EPS, TSH, recherche maladie coeliaque (IgA anti-transglutaminases + "
                "dosage pondéral IgA)"
            )),
            FicheRow(concept="PEC", detail_md=(
                "- Relation médecin-malade de qualité : écouter, expliquer, rassurer\n"
                "- **Antispasmodiques** : alvérine + siméthicone, trimébutine, phloroglucinol\n"
                "- Traitement troubles du transit (si alternance → traiter comme constipation)\n"
                "- Ballonnements : éviter boissons gazeuses, aliments fermentescibles\n"
                "- Psychothérapie de soutien +/- antidépresseurs (amitriptyline)"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Étiologies de la cirrhose", markdown=(
            "| Étiologie | Fréquence | Argument clé |\n"
            "|-----------|-----------|-------------|\n"
            "| Alcool | 1re cause | ASAT/ALAT > 2, VGM augmenté, bloc béta-gamma |\n"
            "| Hépatite C | 2e cause | Sérologie VHC + et PCR + |\n"
            "| NASH | En augmentation | Syndrome métabolique, pas d'OH |\n"
            "| Hépatite B | 3e cause | Ag HBs +, Ac anti-HBc + |\n"
            "| Hémochromatose | | CST > 45%, mutation C282Y |\n"
            "| Hépatite auto-immune | | Femme, IgG élevées, auto-Ac |\n"
            "| CBP | | Femme 50 ans, Ac anti-mitochondrie M2 |\n"
        )),
        TableauSynthese(titre="Complications de la cirrhose et PEC", markdown=(
            "| Complication | Mortalité | Traitement clé |\n"
            "|-------------|-----------|---------------|\n"
            "| Hémorragie VO | > 30% | FOGD + ligature + octréotide + ATB prophylaxie |\n"
            "| ISLA | Élevée | Céfotaxime + albumine IV |\n"
            "| Encéphalopathie | Variable | Traiter facteur déclenchant + laxatifs osmotiques |\n"
            "| SHR | Très élevée | Albumine + terlipressine + transplantation |\n"
            "| Ascite réfractaire | | Ponctions itératives + TIPS + transplantation |\n"
        )),
        TableauSynthese(titre="Comparaison hépatites virales", markdown=(
            "| | VHA | VHB | VHC | VHD | VHE |\n"
            "|--|-----|-----|-----|-----|-----|\n"
            "| Transmission | Oro-fécale | Sexuelle, parentérale, verticale | Parentérale ++ | Sexuelle, parentérale | Oro-fécale |\n"
            "| Chronicité | Jamais | < 5% adulte, > 90% NN | 70-80% | 90% (surinfection) | Rare |\n"
            "| Fulminante | 0,1% | 1% | Jamais | 5% (co-infection) | Femme enceinte |\n"
            "| Vaccin | Oui | Oui | Non | Via VHB | Non |\n"
            "| DO | Oui | Non | Non | Non | Non |\n"
        )),
        TableauSynthese(titre="Lithiase biliaire : colique hépatique vs cholécystite vs angiocholite", markdown=(
            "| | Colique hépatique | Cholécystite | Angiocholite |\n"
            "|--|-------------------|-------------|-------------|\n"
            "| Douleur | HCD < 6h | HCD > 6h | HCD (colique hépatique) |\n"
            "| Fièvre | Non | Oui (38,5°C) | Oui |\n"
            "| Ictère | Non | Non | Oui |\n"
            "| BHC | Normal | Normal | Cholestase |\n"
            "| Urgence | Ambulatoire | Cholécystectomie 24h | CPRE + ATB |\n"
        )),
        TableauSynthese(titre="Pancréatite aiguë : gravité et PEC selon étiologie", markdown=(
            "| Situation | PEC spécifique |\n"
            "|-----------|---------------|\n"
            "| PA bénigne biliaire | Cholécystectomie même hospitalisation |\n"
            "| PA + angiocholite | ATB + CPRE en urgence + cholécystectomie à distance |\n"
            "| PA grave biliaire | CPRE + sphinctérotomie dans 72h |\n"
            "| PA alcoolique | Prévention sevrage + sevrage à distance |\n"
            "| Nécrose infectée | Réanimation + ATB large spectre + drainage |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Bilirubine sub-ictère | > **30** µmol/L | Conjonctives jaunes |\n"
        "| Bilirubine ictère franc | > **50** µmol/L | Ictère cutanéo-muqueux |\n"
        "| Gradient albumine sérum-ascite | > **11 g/L** | Ascite liée à HTP |\n"
        "| ISLA : seuil PNN | > **250/mm³** | Diagnostic positif |\n"
        "| Albumine post-ponction | **20 g / 3L** | À partir du 3e litre |\n"
        "| Prévention ISLA | Cipro **500 mg/j** | Child C + protides < 15 g/L |\n"
        "| Veine porte dilatée | > **12 mm** | Signe d'HTP |\n"
        "| Dilatation VBP | > **8 mm** | Lithiase VBP |\n"
        "| Lipase diagnostic PA | > **3N** | Critère biologique |\n"
        "| CRP gravité PA | > **150 mg/L** | Au 2e jour |\n"
        "| Scanner PA | **72-96h** | Délai optimal |\n"
        "| Créatinine SHR I | > **133** µmol/L | Critère diagnostique |\n"
        "| Caecum danger | > **12 cm** | Risque perforation (occlusion) |\n"
        "| Épaisseur paroi vésicule | > **4 mm** | Cholécystite aiguë |\n"
        "| UGD : incidence France | **90 000**/an | En diminution |\n"
        "| Mortalité hémorragie VO | > **30%** | Cirrhose compliquée |\n"
    ))

    points_cles = [
        "Les deux causes les plus fréquentes d'ascite en France sont la **cirrhose** et la **carcinose péritonéale**",
        "La ponction d'ascite exploratrice est **systématique** devant toute décompensation de cirrhose ; "
        "PNN > **250/mm³** = ISLA",
        "La **transplantation hépatique** est le seul traitement curatif de la cirrhose sévère ; "
        "si cirrhose OH : 6 mois de sevrage préalable",
        "Le diagnostic d'UGD repose sur la **FOGD avec biopsies** ; le contrôle d'éradication de H. pylori "
        "est **systématique** (30% d'échec)",
        "Le RGO typique (pyrosis + régurgitations) est un diagnostic **clinique** ; la FOGD est indiquée si "
        "> 50 ans, signes d'alarme ou résistance au traitement",
        "La pancréatite aiguë se diagnostique sur 2/3 critères : douleur typique, **lipase > 3N**, "
        "scanner ; le scanner se fait entre **72 et 96h**",
        "L'angiocholite se manifeste par la **triade de Charcot** (douleur, fièvre, ictère) ; "
        "traitement = ATB + CPRE",
        "La diverticulite non compliquée se traite en **ambulatoire** ; l'**ATB n'est pas systématique** ; "
        "les **AINS sont CI**",
    ]

    fiche_eclair_md = (
        "**Cirrhose** : IHC (angiomes stellaires, ictère, hypoalbuminémie) + HTP "
        "(ascite, VO, splénomégalie). Score de Child-Pugh. Complications : hémorragie VO "
        "(FOGD + ligature), ISLA (PNN > 250), encéphalopathie (astérixis), SHR.\n\n"
        "**Hépatites virales** : VHB (Ag HBs, sexuelle/parentérale, NN > 90% chronicité) ; "
        "VHC (parentérale, 70-80% chronicité, traitement par AAD pour tous). "
        "Fulminante : VHB 1%, jamais VHC.\n\n"
        "**UGD** : FOGD + biopsies. H. pylori = éradication + contrôle. "
        "Complications : hémorragie (Forrest), perforation (CI FOGD), sténose, cancer (UG).\n\n"
        "**RGO** : pyrosis + régurgitations = diagnostic clinique. IPP si symptômes fréquents. "
        "Barrett = état pré-cancéreux.\n\n"
        "**Lithiase biliaire** : colique hépatique (< 6h, pas fièvre) vs cholécystite (> 6h, fièvre) "
        "vs angiocholite (triade de Charcot). Cholécystectomie pour tous.\n\n"
        "**PA** : lipase > 3N, scanner à 72-96h, CTSI. Alcool/biliaire = 80%. "
        "Pas d'ATB prophylactique.\n\n"
        "**Péritonite** : contracture abdominale, scanner, ATB + chirurgie en urgence.\n\n"
        "**Occlusion** : arrêt matières et gaz, scanner (pas d'ASP), SNG systématique. "
        "Brides = 1re cause."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Hépato-gastro-entérologie",
        annee="2025-2026",
        item="Items 163, 276, 279, 280, 163, 274, 275, 300, 349, 351, 354, 283, 284, 285, 286, 287, 288, 290, 353, 355",
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
    captions_file = PROJECT_ROOT / "output" / ".work" / "hepato-gastro-enterologie" / "image_captions.json"
    if captions_file.exists():
        # image loading code placeholder
        pass

    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    docx_path = output_dir / "Medecine_generale_hepato-gastro-enterologie_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Medecine_generale_hepato-gastro-enterologie_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path}")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

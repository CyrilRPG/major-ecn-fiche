"""Génère la fiche Endocrinologie."""
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
        PlanPartie(numero="I", titre="Hyperthyroïdie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Syndrome de thyrotoxicose"),
            PlanSousPartie(lettre="B", titre="Examens complémentaires"),
            PlanSousPartie(lettre="C", titre="Étiologies"),
            PlanSousPartie(lettre="D", titre="Prise en charge"),
            PlanSousPartie(lettre="E", titre="Complications"),
        ]),
        PlanPartie(numero="II", titre="Hypothyroïdie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Tableau clinique"),
            PlanSousPartie(lettre="B", titre="Examens complémentaires et étiologies"),
            PlanSousPartie(lettre="C", titre="Prise en charge et complications"),
        ]),
        PlanPartie(numero="III", titre="Goitre et nodules thyroïdiens", sous_parties=[
            PlanSousPartie(lettre="A", titre="Goitre"),
            PlanSousPartie(lettre="B", titre="Nodules thyroïdiens et cancers"),
        ]),
        PlanPartie(numero="IV", titre="Diabète de type 1", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et diagnostic"),
            PlanSousPartie(lettre="B", titre="Acidocétose diabétique"),
            PlanSousPartie(lettre="C", titre="Prise en charge au long cours"),
        ]),
        PlanPartie(numero="V", titre="Diabète de type 2 et complications", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités, diagnostic et dépistage"),
            PlanSousPartie(lettre="B", titre="Prise en charge thérapeutique"),
            PlanSousPartie(lettre="C", titre="Complications métaboliques aiguës"),
            PlanSousPartie(lettre="D", titre="Complications dégénératives"),
        ]),
        PlanPartie(numero="VI", titre="Syndrome de Cushing et insuffisance surrénale", sous_parties=[
            PlanSousPartie(lettre="A", titre="Hypercorticisme : syndrome de Cushing"),
            PlanSousPartie(lettre="B", titre="Insuffisance surrénale chronique"),
            PlanSousPartie(lettre="C", titre="Insuffisance surrénale aiguë"),
        ]),
        PlanPartie(numero="VII", titre="HTA secondaire endocrine et hypoglycémie", sous_parties=[
            PlanSousPartie(lettre="A", titre="HTA secondaire d'origine endocrine"),
            PlanSousPartie(lettre="B", titre="Hypoglycémie"),
        ]),
    ]

    # ── PARTIE I : HYPERTHYROÏDIE ──
    partie_i = Partie(numero="I", titre="Hyperthyroïdie", sous_parties=[
        SousPartie(lettre="A", titre="Syndrome de thyrotoxicose", rows=[
            FicheRow(concept="Signes cardiovasculaires", detail_md=(
                "- **Tachycardie** régulière, sinusale, exagérée lors des efforts et émotions, "
                "persistant au repos +/- palpitations et dyspnée d'effort\n"
                "- Pouls vibrant, élévation de la **PAS**"
            )),
            FicheRow(concept="Signes neuropsychiques", detail_md=(
                "- Nervosité excessive, agitation psychomotrice\n"
                "- Troubles de l'humeur : labilité, irritabilité, syndrome maniaque/dépressif\n"
                "- **Tremblement** fin et régulier des extrémités\n"
                "- Asthénie, insomnie"
            )),
            FicheRow(concept="Signes généraux", detail_md=(
                "- **Thermophobie** avec hypersudation, mains chaudes et moites\n"
                "- **Amaigrissement** rapide, souvent important, à appétit conservé/augmenté (polyphagie)\n"
                "- Polydipsie\n"
                "- Faiblesse musculaire : **signe du tabouret**, amyotrophie\n"
                "- Augmentation fréquence des selles (accélération du transit)\n"
                "- Gynécomastie/impuissance (homme), troubles des règles (femme)"
            )),
            FicheRow(concept="", detail_md=(
                "- La prise de poids est possible si la polyphagie dépasse l'hypercatabolisme\n"
                "- La fertilité est le plus souvent conservée"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Examens complémentaires", rows=[
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- Dosage **TSH** en première intention :\n"
                "  - **Effondrée** : dosage **T4L** pour confirmer et préciser l'intensité\n"
                "  - Normale : diagnostic éliminé (sauf rare adénome thyréotrope)\n"
                "  - Élevée : diagnostic éliminé sauf conviction clinique très forte"
            )),
            FicheRow(concept="", detail_md=(
                "- TSH effondrée = hyperthyroïdie jusqu'à preuve du contraire\n"
                "- Une TSH normale élimine pratiquement toujours le diagnostic"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Retentissement", detail_md=(
                "- NFS : leuconeutropénie avec lymphocytose relative\n"
                "- BHC : cytolyse et cholestase anictérique\n"
                "- EAL : diminution CT-T et TG\n"
                "- Bilan phosphocalcique : **hypercalcémie** avec hypercalciurie\n"
                "- Glycémie : intolérance au glucose / aggravation diabète"
            )),
            FicheRow(concept="Bilan étiologique", detail_md=(
                "- Systématiques : dosage **TRAK** + **échographie thyroïdienne**\n"
                "- Si et seulement si TRAK négatifs : **scintigraphie iode 123**\n"
                "- ECG systématique +/- ETT\n"
                "- Examen ophtalmologique complet\n"
                "- HCG, recherche MAI associée si Basedow"
            )),
        ]),
        SousPartie(lettre="C", titre="Étiologies", rows=[
            FicheRow(concept="Maladie de Basedow", detail_md=(
                "- **Cause la plus fréquente** en Europe (prévalence 1% femmes, 0,4% hommes)\n"
                "- Maladie **auto-immune** : anticorps stimulant le récepteur TSH (**TRAK**)\n"
                "- Terrain : femme **20-40 ans**, ATCD MAI, tabagisme\n"
                "- Goitre basedowien : diffus, homogène, indolore, élastique, **souffle** à l'auscultation\n"
                "- **Orbitopathie dysthyroïdienne** (50%) : exophtalmie bilatérale souvent asymétrique, "
                "oedème des paupières, inflammation conjonctive\n"
                "- TRAK positifs, échographie hypoéchogène et très vascularisée\n"
                "- Scintigraphie : hyperfixation homogène et diffuse (non indispensable si forme typique)"
            )),
            FicheRow(concept="◆ GMHNT et adénome toxique", detail_md=(
                "| Critère | GMHNT | Adénome toxique |\n"
                "|---------|-------|-----------------|\n"
                "| Fréquence | 2e cause en Europe | 3e cause en Europe |\n"
                "| Terrain | H/F > 40 ans, goitre ancien | Femme 40-60 ans |\n"
                "| Clinique | Goitre multi-nodulaire +/- compressif | Nodule palpable |\n"
                "| Dosages immuno | Négatifs | Négatifs |\n"
                "| Scintigraphie | Aspect **en damier** | **Nodule chaud**, parenchyme éteint |\n"
            )),
            FicheRow(concept="★ Surcharge iodée", detail_md=(
                "- Origine : **amiodarone**, PDC iodés, interféron\n"
                "- Dissociation T3/T4 (T4L augmentée, T3L normale)\n"
                "- Scintigraphie **blanche**"
            )),
            FicheRow(concept="Thyroïdite de De Quervain", detail_md=(
                "- Affection d'**origine virale** avec lyse des cellules thyroïdiennes\n"
                "- Syndrome pseudo-grippal fébrile + goitre **ferme et douloureux**\n"
                "- Douleurs cervicales antérieures intenses avec irradiation ascendante\n"
                "- Syndrome inflammatoire très important, thyroglobuline augmentée\n"
                "- Scintigraphie **blanche**\n"
                "- Évolution : thyrotoxicose initiale +/- hypothyroïdie puis récupération en 2-3 mois"
            )),
            FicheRow(concept="Thyrotoxicose factice", detail_md=(
                "- Prise cachée d'hormones thyroïdiennes\n"
                "- Échographie normale, scintigraphie blanche\n"
                "- **Thyroglobuline effondrée** (quasi-pathognomonique)"
            )),
        ]),
        SousPartie(lettre="D", titre="Prise en charge", rows=[
            FicheRow(concept="Traitements non spécifiques", detail_md=(
                "- Repos, sédatifs (benzodiazépines)\n"
                "- **Bêta-bloquants** : propranolol 60-160 mg/24h (non cardio-sélectif)\n"
                "- **Contraception** efficace chez la femme jeune"
            )),
            FicheRow(concept="ATS (antithyroïdiens de synthèse)", detail_md=(
                "- **Carbimazole**, PTU (à privilégier si grossesse), BTU\n"
                "- Effet purement **suspensif**, efficacité en 10-15 jours\n"
                "- Effets secondaires : allergies cutanées, élévation enzymes hépatiques, "
                "neutropénie, **agranulocytose** immunoallergique (0,1%)\n"
                "- Surveillance : T4L à S4, puis TSH + T4L tous les 3-4 mois\n"
                "- NFS tous les 10 jours pendant 2 mois, BHC avant mise en place"
            )),
            FicheRow(concept="", detail_md=(
                "- Si fièvre sous ATS : **arrêt ATS** systématique et NFS en urgence\n"
                "- Si agranulocytose : arrêt **définitif** ATS et déclaration pharmacovigilance"
            ), kind="piege"),
            FicheRow(concept="Stratégie selon étiologie", detail_md=(
                "| Étiologie | Stratégie |\n"
                "|-----------|----------|\n"
                "| **Basedow** | ATS 1-2 ans, si rechute (40-60%) : chirurgie ou radio-iode |\n"
                "| **Adénome toxique / GMHNT** | Chirurgie ou iode 131 |\n"
                "| **Surcharge iodée** | Arrêt produit + ATS ou corticoïdes |\n"
            )),
            FicheRow(concept="Chirurgie et radio-iode", detail_md=(
                "- Chirurgie : **après obtention euthyroïdie**, thyroïdectomie totale (Basedow) "
                "ou lobectomie (adénome toxique)\n"
                "- Radio-iode (I131) : destruction thyroïde par irradiation interne, "
                "délai 1-2 mois, **CI grossesse**, contraception 6 mois"
            )),
        ]),
        SousPartie(lettre="E", titre="Complications", rows=[
            FicheRow(concept="Cardiothyréose", detail_md=(
                "- FDR : sujets âgés, cardiopathie préexistante\n"
                "- Troubles du rythme supra-ventriculaires : **FA**, flutter atrial\n"
                "- IC à débit élevé\n"
                "- Insuffisance coronaire"
            )),
            FicheRow(concept="Crise aiguë thyrotoxique", detail_md=(
                "- Facteur déclenchant : patient opéré en situation d'hyperthyroïdie\n"
                "- Syndrome de thyrotoxicose majeur + troubles CV + troubles "
                "neuropsychiatriques (délire, agitation, coma)"
            )),
            FicheRow(concept="◆ Hyperthyroïdie et grossesse", detail_md=(
                "- **Thyrotoxicose gestationnelle transitoire** : repos +/- BB- en attendant régression\n"
                "- **Basedow** : formes mineures = repos sous surveillance ; "
                "formes plus importantes = ATS faible dose (**PTU** préféré), propranolol possible\n"
                "- Formes graves : thyroïdectomie possible à partir du T2"
            )),
            FicheRow(concept="Ostéoporose", detail_md=(
                "- Complication de l'hyperthyroïdie prolongée\n"
                "- Le plus souvent asymptomatique, à rechercher"
            )),
        ]),
    ])

    # ── PARTIE II : HYPOTHYROÏDIE ──
    partie_ii = Partie(numero="II", titre="Hypothyroïdie", sous_parties=[
        SousPartie(lettre="A", titre="Tableau clinique", rows=[
            FicheRow(concept="Myxoedème cutanéo-muqueux", detail_md=(
                "- Visage pâle, rond, bouffi (faciès lunaire)\n"
                "- Infiltration face dorsale mains et pieds : doigts **boudinés**\n"
                "- Infiltration laryngée : dysarthrie, **voix rauque**\n"
                "- Macroglossie, ronflements voire SAOS\n"
                "- **Syndrome du canal carpien**"
            )),
            FicheRow(concept="Signes d'hypométabolisme", detail_md=(
                "- Asthénie physique et psycho-intellectuelle (possible syndrome dépressif/confusionnel/démentiel)\n"
                "- Somnolence, prise de poids modeste contrastant avec perte d'appétit\n"
                "- **Hypothermie** avec frilosité\n"
                "- **Constipation** acquise\n"
                "- **Bradycardie** avec assourdissement des BDC, hypotension"
            )),
            FicheRow(concept="Autres signes", detail_md=(
                "- Atteinte neuromusculaire : syndrome myogène, myalgies, crampes\n"
                "- Peau pâle/jaunâtre, sèche et squameuse, alopécie diffuse\n"
                "- Troubles des règles divers, troubles de la libido\n"
                "- Rares galactorrhées (hypothyroïdie primaire profonde uniquement)"
            )),
        ]),
        SousPartie(lettre="B", titre="Examens complémentaires et étiologies", rows=[
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- **TSH** en première intention :\n"
                "  - Augmentée : origine **périphérique**\n"
                "  - Diminuée : origine **centrale**\n"
                "- **T4L** en deuxième intention : détermine la profondeur de l'hypothyroïdie\n"
                "- Ac anti-TPO (1re intention), anti-TG si TPO négatifs\n"
                "- Échographie thyroïdienne si goitre associé"
            )),
            FicheRow(concept="◆ Retentissement", detail_md=(
                "- NFS : anémies de tout type, souvent **macrocytaire**\n"
                "- Ionogramme : **hyponatrémie** à secteur extra-cellulaire normal\n"
                "- CPK augmentées, EAL : dyslipidémie (++ à LDL)"
            )),
            FicheRow(concept="Thyroïdite d'Hashimoto", detail_md=(
                "- **Étiologie la plus fréquente** en France\n"
                "- Terrain : femme 40-60 ans, ATCD MAI\n"
                "- Goitre irrégulier, ligneux, hétérogène\n"
                "- Ac anti-TPO positifs à taux très élevés\n"
                "- Échographie : goitre hypoéchogène avec zones hyperplasiques pseudo-nodulaires"
            )),
            FicheRow(concept="Thyroïdite atrophique", detail_md=(
                "- Femme 40-60 ans, ménopausée, ATCD MAI\n"
                "- Absence de goitre, thyroïde impalpable\n"
                "- Ac anti-TPO positifs à taux faibles / TRAB positifs"
            )),
            FicheRow(concept="Autres étiologies", detail_md=(
                "- **Thyroïdite du post-partum** (5% des grossesses) : hypothyroïdie vers 3-6e mois PP\n"
                "- Thyroïdite de De Quervain (après phase d'hyperthyroïdie)\n"
                "- **Carence iodée** sévère : zones d'endémie goitreuse\n"
                "- Causes iatrogènes : **amiodarone**, I131, radiothérapie cervicale, "
                "thyroïdectomie, lithium, immunothérapies\n"
                "- Insuffisance thyréotrope (origine centrale) : IRM hypophysaire"
            )),
            FicheRow(concept="", detail_md=(
                "- Rechercher systématiquement une **insuffisance surrénale** associée "
                "(syndrome de Schmidt) avant de traiter\n"
                "- Rechercher : Biermer, DT1, myasthénie"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Prise en charge et complications", rows=[
            FicheRow(concept="Traitement substitutif", detail_md=(
                "- **Lévothyroxine** PO : dose cible 1-1,5 ug/kg/j\n"
                "- Augmentation progressive par paliers\n"
                "- Prise à heures fixes, matin à jeun 30 min avant petit-déjeuner\n"
                "- **Traitement à vie**\n"
                "- Majoration posologie pendant **grossesse** (+30-50% au T1)\n"
                "- Interactions : IPP, fer, inducteurs enzymatiques, oestrogènes"
            )),
            FicheRow(concept="◆ Surveillance", detail_md=(
                "- Objectif TSH : **0,5-2,5 mUI/L** (situation standard)\n"
                "- Coronarien/personne très âgée : TSH < 10 mUI/L\n"
                "- Contrôle TSH 4-8 semaines après modification de dose\n"
                "- Puis TSH 1/6 mois puis 1/an"
            )),
            FicheRow(concept="◆ Hypothyroïdie frustre", detail_md=(
                "| Risque | Critères | CAT |\n"
                "|--------|----------|-----|\n"
                "| **Élevé** | TSH > 10 mUI/L et/ou Ac anti-TPO | Traitement recommandé |\n"
                "| Intermédiaire | TSH < 10 + anti-TPO ou signes cliniques | Traitement à discuter |\n"
                "| Faible | TSH < 10, pas d'anti-TPO | Surveillance TSH 1/6 mois puis 1/an |\n"
            )),
            FicheRow(concept="Coma myxoedémateux", detail_md=(
                "- Terrain : hypothyroïdie primaire profonde (TSH > 50), femme âgée\n"
                "- Facteurs déclenchants : froid, infection, sédatifs\n"
                "- Coma calme, bradycardie, hypotension/choc, bradypnée, **hypothermie** sévère\n"
                "- **Hyponatrémie** sévère, hypoventilation alvéolaire\n"
                "- Si hyperkaliémie + hypoglycémie : penser au **syndrome de Schmidt**"
            )),
            FicheRow(concept="", detail_md=(
                "- Les dosages ne doivent **jamais retarder** le traitement du coma myxoedémateux\n"
                "- Risque de démasquer une insuffisance coronaire à l'instauration du traitement"
            ), kind="piege"),
            FicheRow(concept="◆ Hypothyroïdie et grossesse", detail_md=(
                "- Risques maternels : fausse couche, HTA gravidique, pré-éclampsie, MAP\n"
                "- Risques foetaux : RCIU, prématurité, mort foetale in utero\n"
                "- Risque enfant : **retard mental**, goitre néonatal"
            )),
        ]),
    ])

    # ── PARTIE III : GOITRE ET NODULES THYROÏDIENS ──
    partie_iii = Partie(numero="III", titre="Goitre et nodules thyroïdiens", sous_parties=[
        SousPartie(lettre="A", titre="Goitre", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Goitre = augmentation du volume de la glande thyroïde\n"
                "- Volume échographique > **18 mL** (femme) / **20 mL** (homme)\n"
                "- Fréquent : 5-10% de la population en France"
            )),
            FicheRow(concept="Examen clinique", detail_md=(
                "- Inspection : thyroïde bien visible\n"
                "- Tuméfaction cervicale antérieure remontant à la déglutition\n"
                "- Déterminer : limites, taille, consistance, homogénéité, sensibilité, souffle\n"
                "- Recherche : nodules, ADP cervicales, signes de compression\n"
                "- Signes de compression : **3 D** = Dysphonie, Dysphagie, Dyspnée"
            )),
            FicheRow(concept="", detail_md=(
                "- **3 D** de la compression : Dysphonie (nerf récurrent), "
                "Dysphagie (oesophage), Dyspnée inspiratoire (trachée)"
            ), kind="mnemo"),
            FicheRow(concept="◆ Goitre simple : évolution", detail_md=(
                "- Stade 1 : goitre diffus, homogène (adolescent/adulte jeune) : peut régresser\n"
                "- Stade 2 : goitre pauci/multi-nodulaire (20-40 ans) : lésions irréversibles\n"
                "- Stade 3 : goitre multi-nodulaire **toxique** (40-60 ans)\n"
                "- Stade 4 : goitre multiloculaire **compressif**"
            )),
            FicheRow(concept="Complications", detail_md=(
                "- Hyperthyroïdie, inflammation (strumite), hématocèle\n"
                "- Compression (++ goitre plongeant) : dyspnée, dysphonie, dysphagie, "
                "syndrome cave supérieur\n"
                "- Manoeuvre de **Pemberton** : aspect cramoisi lorsque bras levés "
                "(gêne au retour veineux)"
            )),
        ]),
        SousPartie(lettre="B", titre="Nodules thyroïdiens et cancers", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Affection fréquente : 4-7% population (nodules palpables)\n"
                "- FDR : sexe féminin (SR 2-3/1), âge, grossesse, carence en iode, "
                "irradiation cervicale"
            )),
            FicheRow(concept="★ Bilan d'un nodule", detail_md=(
                "- **TSH** : si abaissée, faire scintigraphie\n"
                "- **Échographie** : score **EU-TIRADS**\n"
                "- **Cytoponction** à l'aiguille fine : selon taille et EU-TIRADS, "
                "ou si nodule froid à la scintigraphie\n"
                "- Résultats classés selon **classification de Bethesda**"
            )),
            FicheRow(concept="Orientations cliniques", detail_md=(
                "- Nodule douloureux + fièvre : thyroïdite de De Quervain\n"
                "- Nodule compressif + ADP : évoquer **cancer**\n"
                "- Nodule + hyperthyroïdie : nodule toxique"
            )),
            FicheRow(concept="Cancers thyroïdiens", detail_md=(
                "- Rares mais en augmentation : 1,5% des cancers, 4e cancer chez la femme\n"
                "- 75% chez la femme, survie à 10 ans > 90%\n"
                "- **Carcinomes épithéliaux** (90%) : papillaires ou vésiculaires\n"
                "  - Calcitonine normale\n"
                "  - Thyroïdectomie totale + curage + IRA thérapie\n"
                "- **Carcinome médullaire** : calcitonine **augmentée**, chirurgie + hormonothérapie"
            )),
        ]),
    ])

    # ── PARTIE IV : DIABÈTE DE TYPE 1 ──
    partie_iv = Partie(numero="IV", titre="Diabète de type 1", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et diagnostic", rows=[
            FicheRow(concept="Définition et mécanisme", detail_md=(
                "- Carence en insuline par destruction **auto-immune** des cellules B des îlots de Langerhans\n"
                "- Facteurs génétiques : HLA **DR3, DR4, DQB1**\n"
                "- Auto-anticorps : anti-îlots, anti-insuline, anti-**GAD**, anti-**IA2**, anti-ZnT8\n"
                "- 10% des diabètes mais 90% des diabètes de l'enfant"
            )),
            FicheRow(concept="◆ Histoire naturelle", detail_md=(
                "- Prédisposition génétique + facteur environnemental : apparition auto-Ac\n"
                "- Insulite infra-clinique\n"
                "- Insulinopénie modérée quand **90%** des cellules B détruites (~5 ans)\n"
                "- Insulinopénie absolue +/- précédée d'une **lune de miel**"
            )),
            FicheRow(concept="Circonstances de découverte", detail_md=(
                "- **Syndrome cardinal** (50%) : polyuro-polydipsie, asthénie, "
                "amaigrissement, polyphagie\n"
                "- **Acidocétose** diabétique (50%)\n"
                "- Découverte fortuite (rare)"
            )),
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- Glycémie > **2 g/L** avec manifestations cliniques\n"
                "- Glycémie > **1,26 g/L** à jeun (8h), vérifiée à 2 reprises\n"
                "- Glycémie > 2 g/L après HGPO\n"
                "- BU : glycosurie + cétonurie 3-4 croix"
            )),
            FicheRow(concept="", detail_md=(
                "- En pratique : **hyperglycémie + maigreur/cétose/âge < 35 ans = DT1**\n"
                "- Affirmer la nature auto-immune : dosage auto-Ac (GAD, IA2, insuline, ZnT8)"
            ), kind="a_retenir"),
            FicheRow(concept="Bilan initial", detail_md=(
                "- HbA1c (équilibre des 3 derniers mois)\n"
                "- Dosage Ac du diabète\n"
                "- Recherche MAI associée : thyroïdite (TSH, anti-TPO), maladie coeliaque (IgA anti-TG)\n"
                "- FDR CV, dépistage complications après **5 ans** d'évolution"
            )),
        ]),
        SousPartie(lettre="B", titre="Acidocétose diabétique", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Cause de **mortalité la plus fréquente** chez le DT1\n"
                "- Liée à une carence profonde en insuline + élévation hormones de contre-régulation"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Syndrome cardinal + déshydratation (DEC + DIC)\n"
                "- Signes digestifs : douleurs abdominales, nausées/vomissements\n"
                "- Signes respiratoires : dyspnée de **Kussmaul**, odeur **acétonique** de l'haleine\n"
                "- Signes neurologiques : obnubilation, somnolence, coma"
            )),
            FicheRow(concept="Confirmation biologique", detail_md=(
                "- Glycémie veineuse > **2,50 g/L**\n"
                "- GDS veineux : pH < **7,30** ou HCO3- < 15 mM (sévère si pH < 7,1)\n"
                "- Corps cétoniques : cétonurie capillaire > **3 mM**\n"
                "- Natrémie corrigée : Nac = Na + 2 x ((glycémie - 5,6) / 5,6)\n"
                "- Kaliémie habituellement normale mais stock potassique très abaissé\n"
                "- ECG : recherche signes de dyskaliémie"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- **Hospitalisation en urgence**, monitoring, 2 VVP, mise à jeun\n"
                "- Réhydratation : NaCl 0,9% + **KCl** systématique (si pas d'anurie ni hyperkaliémie ECG)\n"
                "- Insulinothérapie : insuline rapide **IV** 0,05-0,1 UI/kg/h\n"
                "- Objectifs : disparition cétonurie H12-H24, glycémie ~10 mM entre H12-H24\n"
                "- Relai insuline SC vers H24 quand état clinique (digestif) le permet"
            )),
            FicheRow(concept="", detail_md=(
                "- Ne **JAMAIS** arrêter l'insuline IV dans les 24 premières heures\n"
                "- En cas d'hypoglycémie : rajouter du soluté glucosé (ne pas arrêter l'insuline)"
            ), kind="piege"),
            FicheRow(concept="Complications acidocétose", detail_md=(
                "- **Oedème cérébral** : céphalées, altération brutale de conscience, convulsions "
                "=> mannitol IV, diminution débits, transfert réanimation\n"
                "- Hypokaliémie, inhalation, hypoglycémie, hypophosphorémie"
            )),
        ]),
        SousPartie(lettre="C", titre="Prise en charge au long cours", rows=[
            FicheRow(concept="Insulinothérapie", detail_md=(
                "- Traitement **à vie**, débuté en hospitalisation avec ETP\n"
                "- Capteur de glycémie interstitielle à privilégier (FSL, DEXCOM)\n"
                "- **Schéma basal-bolus** : insuline lente 1/j + rapide avant repas\n"
                "- **Pompe à insuline** : débit de base + bolus avant repas\n"
                "- Système **boucle fermée** : algorithme CGM + pompe pour atteindre glycémie cible\n"
                "- **Insulinothérapie fonctionnelle** à privilégier : calcul des glucides"
            )),
            FicheRow(concept="◆ Objectifs et RHD", detail_md=(
                "- Objectif HbA1c < **7%**\n"
                "- Alimentation équilibrée, pas d'interdits alimentaires (IF)\n"
                "- Activité physique encouragée sauf parachutisme, plongée sous-marine\n"
                "- Prise en charge FDRCV"
            )),
            FicheRow(concept="Mesures sociales", detail_md=(
                "- ALD 100%, PAI à l'école\n"
                "- Association AJD (Aide au Jeunes Diabétiques)\n"
                "- Soutien psychologique (++ adolescence)"
            )),
            FicheRow(concept="◆ Suivi", detail_md=(
                "- Consultations spécialisées tous les **2-3 mois**\n"
                "- HbA1c **4 fois/an**\n"
                "- Recherche MAI associées 1/an\n"
                "- Dépistage complications après **5 ans** : rénales (microalbuminurie, créatinine), "
                "ophtalmologiques (rétinographie/FO), neurologiques\n"
                "- Bilan lipidique annuel"
            )),
        ]),
    ])

    # ── PARTIE V : DIABÈTE DE TYPE 2 ET COMPLICATIONS ──
    partie_v = Partie(numero="V", titre="Diabète de type 2 et complications", sous_parties=[
        SousPartie(lettre="A", titre="Généralités, diagnostic et dépistage", rows=[
            FicheRow(concept="Épidémiologie et FDR", detail_md=(
                "- 80-90% des diabètes, prévalence **4%** population générale (> 2M en France)\n"
                "- FDR : âge > 45 ans, sédentarité, IMC > 28, obésité androïde\n"
                "- ATCD familiaux DT2, ATCD diabète gestationnel/enfant macrosome\n"
                "- Marqueurs de risque : HTA, hypo-HDL-C, hyper-TG, tabagisme, SOPK"
            )),
            FicheRow(concept="Diagnostic", detail_md=(
                "- **Asymptomatique** dans la majorité des cas\n"
                "- Glycémie > **1,26 g/L** à jeun (8h) vérifiée à 2 reprises\n"
                "- Ou symptômes + glycémie > **2 g/L**\n"
                "- Ou glycémie > 2 g/L après HGPO\n"
                "- Pré-diabète : glycémie entre 1,10 et 1,26 g/L à jeun"
            )),
            FicheRow(concept="◆ Confirmer le DT2", detail_md=(
                "- Âge > 40 ans, ATCD familial DT2, FDRCV associés\n"
                "- IMC > 25, syndrome métabolique, obésité androïde\n"
                "- Cétonurie absente, Ac anti-GAD et IA2 négatifs"
            )),
            FicheRow(concept="Dépistage", detail_md=(
                "- Patients > 40 ans avec au moins 1 FDR :\n"
                "  - IMC > 25 / obésité abdominale (> 80 cm F, > 94 cm H)\n"
                "  - HTA > 140/90, hyper-TG > 2 g/L et/ou HDLc < 0,35 g/L\n"
                "  - ATCD diabète gestationnel / familial 1er degré\n"
                "- Modalité : glycémie veineuse après 8h de jeûne\n"
                "- Renouvellement : tous les 1-3 ans ou 1/an si pré-diabète"
            )),
        ]),
        SousPartie(lettre="B", titre="Prise en charge thérapeutique", rows=[
            FicheRow(concept="RHD", detail_md=(
                "- Perte de poids 5-10% si excès pondéral\n"
                "- Alimentation : privilégier oméga-3, index glycémique faible, "
                "sel < 6 g/j si HTA\n"
                "- Activité physique : au moins **30 min/j** + 2-3 séances/semaine de renforcement\n"
                "- Sevrage tabagique"
            )),
            FicheRow(concept="Stratégie médicamenteuse", detail_md=(
                "- RHD seule pendant **3-6 mois** en première intention\n"
                "- Monothérapie par **metformine** en 1re ligne\n"
                "- Si glycémie > 3 g/L ou HbA1c > 10% : d'emblée bithérapie ou insuline\n"
                "- Escalade thérapeutique selon HbA1c"
            )),
            FicheRow(concept="◆ Insulinothérapie dans le DT2", detail_md=(
                "- Indications : signes d'insulino-requérance (amaigrissement, asthénie, amyotrophie) "
                "ou échec traitement oral\n"
                "- **Insulinothérapie combinée** : insuline lente 1/j + ADO (débuter 0,2 UI/kg/j)\n"
                "- Schéma basal-bolus si nécessaire\n"
                "- Objectifs glycémiques : avant repas 0,7-1,2 g/L, post-prandial < 1,80 g/L"
            )),
            FicheRow(concept="", detail_md=(
                "- Évaluation cardiologique **obligatoire** avant reprise d'activité physique\n"
                "- CI activité si insuffisance coronarienne non stabilisée"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Complications métaboliques aiguës", rows=[
            FicheRow(concept="Coma hyperosmolaire", detail_md=(
                "- Décompensation classique du sujet âgé DT2, **20-40% mortalité**\n"
                "- FDR : âge > 80 ans, déshydratation, corticothérapie, infection aiguë\n"
                "- Clinique : syndrome cardinal + déshydratation intense + troubles de la vigilance, "
                "**absence** de signes d'acidose\n"
                "- BU : glycosurie 3-4+, cétonurie 0-1+, glycémie > **6 g/L**\n"
                "- Osmolalité > **320 mOsm/kg**, hypernatrémie, IRA fonctionnelle"
            )),
            FicheRow(concept="PEC coma hyperosmolaire", detail_md=(
                "- **Réanimation**, réhydratation prudente et lente : 6-10 L NaCl 0,9% en 24h\n"
                "- Insulinothérapie IVSE en maintenant glycémie > **2,5 g/L**\n"
                "- Supplémentation sodée et potassique, héparinothérapie préventive"
            )),
            FicheRow(concept="◆ Acidose lactique", detail_md=(
                "- Complication iatrogène des **biguanides** (metformine)\n"
                "- FDR : insuffisance rénale, hépatique, anesthésie, PDC iodé\n"
                "- Syndrome d'acidose métabolique + douleurs diffuses + collapsus\n"
                "- BU : glycosurie +++ mais cétonurie -, lactatémie élevée\n"
                "- PEC : réanimation, **dialyse** en urgence, alcalinisation"
            )),
            FicheRow(concept="", detail_md=(
                "- Arrêt **metformine** 48h après injection de PDC iodé\n"
                "- Arrêt metformine avant toute chirurgie/anesthésie\n"
                "- Respect des CI : insuffisance rénale, hépatique, cardiaque, respiratoire aiguë"
            ), kind="a_retenir"),
            FicheRow(concept="★ Hypoglycémies iatrogènes", detail_md=(
                "- Dues à l'insuline ou aux **sulfamides hypoglycémiants** (SH)\n"
                "- Sous insuline : erreur de maniement, lipodystrophie, OH\n"
                "- Sous SH : potentialisation (AINS, diurétiques, AVK, miconazole), "
                "insuffisance rénale, surdosage\n"
                "- Chez patient sous SH : **glucagon inefficace**"
            )),
        ]),
        SousPartie(lettre="D", titre="Complications dégénératives", rows=[
            FicheRow(concept="Neuropathie diabétique", detail_md=(
                "- 50% des diabétiques après 20 ans d'évolution\n"
                "- **Polynévrite sensitive distale symétrique** (la plus fréquente, 40%) :\n"
                "  - Topographie **en chaussettes et en gants**\n"
                "  - Paresthésies, hypoesthésie, douleurs neuropathiques\n"
                "  - Réflexes achilléens et rotuliens abolis\n"
                "  - Évolution chronique, régression rare"
            )),
            FicheRow(concept="◆ Neuropathie autonome", detail_md=(
                "- **CV** : tachycardie sinusale ~110 bpm, allongement QT, "
                "ischémie **silencieuse**\n"
                "- **Vasomotrice** : hypotension orthostatique sans accélération du pouls\n"
                "- **Digestive** : gastroparésie, diarrhée motrice\n"
                "- **Vésicale** : défaut de perception, incontinence, RAU"
            )),
            FicheRow(concept="Macroangiopathie", detail_md=(
                "- Risque coronarien x 2-4, AVC x 1,5-2, AOMI x 5-10\n"
                "- Ischémie myocardique **silencieuse** fréquente\n"
                "- PEC : équilibre glycémique, activité physique, contrôle LDLc (SCORE 2-Diabète), "
                "contrôle PA, sevrage tabagique"
            )),
            FicheRow(concept="Pied diabétique", detail_md=(
                "- 1/10 diabétiques subiront au moins 1 amputation (50% évitables)\n"
                "- **Mal perforant plantaire** : neuropathie => hypoesthésie + déformations "
                "=> points d'appui anormaux => durillons => abcès => ostéite\n"
                "- Ischémie/nécrose noire : oblitération artérielle\n"
                "- Gangrène/cellulite extensive : urgence vitale, amputation + ATB IV"
            )),
            FicheRow(concept="PEC pied diabétique", detail_md=(
                "- Examen clinique : artériopathie/neuropathie, localisation plaie, signes diffusion\n"
                "- **Mise en décharge** systématique du pied\n"
                "- Parage lésion, prélèvement en profondeur, recherche contact osseux\n"
                "- ATB non systématique : seulement si infection clinique, durée 15 jours\n"
                "- Score SINBAD\n"
                "- Éducation : inspection quotidienne des pieds, chaussures adaptées, "
                "soins pédicurie réguliers"
            )),
            FicheRow(concept="", detail_md=(
                "- Le test au **monofilament** dépiste la neuropathie sensitive du pied\n"
                "- Rechercher systématiquement **contact osseux** au stylet (ostéite)"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE VI : CUSHING ET INSUFFISANCE SURRÉNALE ──
    partie_vi = Partie(numero="VI", titre="Syndrome de Cushing et insuffisance surrénale", sous_parties=[
        SousPartie(lettre="A", titre="Hypercorticisme : syndrome de Cushing", rows=[
            FicheRow(concept="Signes d'hypercatabolisme protidique", detail_md=(
                "- **Atrophie musculaire** prédominant aux ceintures : fatigabilité, signe du tabouret\n"
                "- **Atrophie cutanée** : peau mince et fragile, lenteur cicatrisation\n"
                "- **Vergetures pourpres** larges > 1 cm\n"
                "- Fragilité capillaire : ecchymoses au moindre choc\n"
                "- Visage érythrosique, congestif, télangiectasies"
            )),
            FicheRow(concept="Anomalies morphologiques", detail_md=(
                "- Prise pondérale modérée (~10 kg) avec topographie **facio-tronculaire**\n"
                "- Obésité androïde (augmentation rapport taille/hanche)\n"
                "- Visage rond (**faciès lunaire**), bouffi\n"
                "- Cou avec **bosse de bison**\n"
                "- Hyperandrogénie : hirsutisme modéré, séborrhée, acné"
            )),
            FicheRow(concept="Autres signes", detail_md=(
                "- HTA, ostéoporose (souvent asymptomatique)\n"
                "- Troubles gonadiques : aménorrhée (femme), impuissance (homme)\n"
                "- Troubles psychiatriques : irritabilité, anxiété nocturne, dépression\n"
                "- Hypersensibilité aux infections, thrombophlébite\n"
                "- **Mélanodermie** uniquement si ACTH-dépendant"
            )),
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- **Cortisol libre urinaire** (CLU) sur 3 jours (rapporté à créatininurie)\n"
                "- Cortisol à minuit : < 1,8 ug/dL élimine, > 7,2 ug/dL affirme\n"
                "- **Test de freinage minute** (le plus simple, ambulatoire) : "
                "cortisolémie matin après 1 mg DXM la veille, positif si cortisol > 5 ug/L\n"
                "- Test de freinage faible (standard) : CLU < 10 ug/j le dernier jour élimine le diagnostic"
            )),
            FicheRow(concept="Diagnostic étiologique", detail_md=(
                "- Dosage **ACTH** sanguin :\n"
                "  - Cortisol augmenté + ACTH effondré = **ACTH-indépendant** (surrénalien)\n"
                "  - Cortisol augmenté + ACTH normal/augmenté = **ACTH-dépendant**"
            )),
            FicheRow(concept="◆ Étiologies", detail_md=(
                "| Étiologie | Fréquence | Explorations | Caractéristiques |\n"
                "|-----------|-----------|--------------|------------------|\n"
                "| **Maladie de Cushing** | 70% | IRM hypophyse, freinage fort + | Micro-adénome (90%) |\n"
                "| Adénome surrénalien | 10% | TDM : nodule < 3-4 cm, < 10 UH | Surrénale controlatérale atrophiée |\n"
                "| Corticosurrénalome malin | 10% | TDM : tumeur > 4-5 cm, > 10 UH | Mauvais pronostic |\n"
                "| Sécrétion paranéoplasique | 10% | Pas de freinage fort | Cancer bronchique, carcinoïde |\n"
            )),
        ]),
        SousPartie(lettre="B", titre="Insuffisance surrénale chronique", rows=[
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Asthénie physique et psychique augmentant au cours de la journée\n"
                "- Amaigrissement, anorexie mais **conservation appétence pour le sel**\n"
                "- **Hypotension** artérielle majorée à l'orthostatisme\n"
                "- Troubles digestifs : nausées, douleurs abdominales\n"
                "- **Mélanodermie** (uniquement si cause périphérique) : zones exposées, "
                "plis palmaires, ongles, taches ardoisées buccales"
            )),
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- Ionogramme : **hyponatrémie + hyperkaliémie**\n"
                "- Cortisolémie 8-9h :\n"
                "  - < 30 ng/mL (83 nmol/L) : diagnostic certain\n"
                "  - > 200 ng/mL (550 nmol/L) : diagnostic éliminé\n"
                "  - Entre les deux : tests dynamiques\n"
                "- **ACTH à 8h** : élevée (> 100 pg/mL) = IS primaire ; "
                "normale/basse = IS corticotrope\n"
                "- **Test au Synacthène** : cortisolémie à 1h > 210 ng/mL = réponse normale "
                "(élimine IS primaire mais 10% FN pour IS corticotrope)"
            )),
            FicheRow(concept="Étiologies IS primaire", detail_md=(
                "- **Rétraction corticale auto-immune** (80%) : femme, ATCD MAI, "
                "Ac anti-21-hydroxylase, surrénales atrophiques\n"
                "- **Tuberculose** bilatérale (20%) : atrophie + calcifications surrénaliennes\n"
                "- VIH, maladies génétiques (adrénoleucodystrophie), "
                "maladies infiltratives, métastases bilatérales"
            )),
            FicheRow(concept="IS corticotrope", detail_md=(
                "- Cause la plus fréquente : **arrêt brutal d'une corticothérapie** prolongée "
                "(> 7 mg prednisone pendant > 4 semaines)\n"
                "- Autres : adénome hypophysaire, lésions hypophysaires"
            )),
            FicheRow(concept="Traitement substitutif", detail_md=(
                "- **Hydrocortisone** 20-30 mg/j (2/3 matin, 1/3 midi)\n"
                "- **Fludrocortisone** 50-150 mg/j (minéralocorticoïdes)\n"
                "- Si IS corticotrope : **hydrocortisone seule** suffit\n"
                "- Traitement **à vie**, régime normosodé\n"
                "- Éducation : doubler dose si fièvre, avoir ampoules hydrocortisone 100 mg IM/IV, "
                "porter carte de traitement"
            )),
            FicheRow(concept="", detail_md=(
                "- Pas d'automédication (++ laxatifs, diurétiques)\n"
                "- Augmenter doses si grossesse\n"
                "- Prévenir tout nouveau médecin de la pathologie surrénalienne"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Insuffisance surrénale aiguë", rows=[
            FicheRow(concept="Tableau clinique", detail_md=(
                "- D'emblée très aigu, +/- signes ISC préexistante\n"
                "- **Déshydratation** extracellulaire sévère, hypotension/**collapsus**\n"
                "- Confusion, convulsions, coma\n"
                "- Troubles digestifs : anorexie, NV, douleurs abdominales, diarrhée\n"
                "- Douleurs diffuses (musculaires), céphalées, hyperthermie"
            )),
            FicheRow(concept="Biologie", detail_md=(
                "- **Hyponatrémie**, **hyperkaliémie** => ECG en urgence\n"
                "- Natriurèse inadaptée (normale/augmentée)\n"
                "- IRA fonctionnelle, **hypoglycémie**\n"
                "- Cortisolémie effondrée, ACTH augmentée si IS primitive"
            )),
            FicheRow(concept="PEC : urgence extrême", detail_md=(
                "- Débuter traitement dès que diagnostic évoqué (prélèvement cortisol si possible)\n"
                "- Au domicile : **hydrocortisone 100 mg IM/IV**\n"
                "- Transport médicalisé, hospitalisation\n"
                "- Rééquilibration hydro-électrolytique + correction hypoglycémie\n"
                "- Hydrocortisone IV : 100-200 mg puis 50-100 mg/6-8h ou 200 mg IVSE/24h\n"
                "- Décroissance 50%/j pour arriver à 20 mg PO en 4-5 jours\n"
                "- Minéralocorticoïdes non nécessaires en phase aiguë"
            )),
            FicheRow(concept="", detail_md=(
                "- L'ISA est une **urgence vitale** : traiter sans attendre les résultats biologiques\n"
                "- Étiologie la plus fréquente : ISC décompensée"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE VII : HTA SECONDAIRE ET HYPOGLYCÉMIE ──
    partie_vii = Partie(numero="VII", titre="HTA secondaire endocrine et hypoglycémie", sous_parties=[
        SousPartie(lettre="A", titre="HTA secondaire d'origine endocrine", rows=[
            FicheRow(concept="Quand dépister", detail_md=(
                "- Signes orientant vers une endocrinopathie, néphropathie, sténose artères rénales\n"
                "- Hypokaliémie, anomalies BU ou insuffisance rénale\n"
                "- Devant toute **HTA résistante** au traitement : toujours rechercher cause secondaire"
            )),
            FicheRow(concept="Hyperaldostéronisme primaire", detail_md=(
                "- Terrain : sujet jeune < 30 ans, HTA résistante (10% des HTA)\n"
                "- Biologie : **hypokaliémie**, augmentation kaliurèse\n"
                "- Exploration rénine-aldostérone : aldostérone élevée + rénine basse\n"
                "- Conditions : arrêt IEC/ARA2/BB-/anti-aldostérones/thiazidiques 15 j-6 sem avant, "
                "remplacer par IC ou anti-HTA centraux, régime normosodé + 6 g/j sel"
            )),
            FicheRow(concept="◆ Adénome de Conn vs hyperplasie", detail_md=(
                "| Critère | Adénome de Conn | Hyperplasie bilatérale |\n"
                "|---------|----------------|------------------------|\n"
                "| Scanner | Nodule unilatéral 6 mm-2 cm, hypodense | Surrénales épaissies, irrégulières |\n"
                "| Traitement | Surrénalectomie unilatérale (coelioscopie) | Aldactone à vie |\n"
                "| Résultat | HTA pas toujours guérie, hypokaliémie corrigée | Association anti-HTA |\n"
                "| Surveillance | TA + kaliémie à vie | TA + kaliémie à vie |\n"
            )),
            FicheRow(concept="Phéochromocytome", detail_md=(
                "- Tumeur sécrétant des **catécholamines**, rare (1/1 000 HTA)\n"
                "- 30% familial : NF1, **NEM 2** (mutation RET), Von Hippel-Lindau => "
                "**bilan génétique indispensable**\n"
                "- Épisodes paroxystiques : HTA + **triade de Ménard** (céphalées, sueurs, palpitations) "
                "= très spécifique\n"
                "- Hypotension orthostatique, signes d'hypermétabolisme\n"
                "- 10% de formes malignes (métastases foie, poumons)"
            )),
            FicheRow(concept="Diagnostic et PEC phéochromocytome", detail_md=(
                "- Dosage **dérivés méthoxylés** plasmatiques : positif si > **4N**\n"
                "- Scanner/IRM surrénales + imagerie fonctionnelle (TEP FDG, MIBG)\n"
                "- Traitement **chirurgical**\n"
                "- Surveillance annuelle à vie : PA, glycémie, métanéphrines"
            )),
        ]),
        SousPartie(lettre="B", titre="Hypoglycémie", rows=[
            FicheRow(concept="Tableau clinique", detail_md=(
                "- **Syndrome neurovégétatif** : pâleur, anxiété, tremblements, "
                "palpitations, faim douloureuse, sueurs\n"
                "- **Syndrome neuroglucopénique** : asthénie, signes moteurs "
                "(ophtalmoplégie, hémiplégie transitoire), paresthésies, "
                "confusion, convulsions\n"
                "- Coma hypoglycémique : sueurs profuses, Babinski bilatéral, "
                "coma agité, pas de signe de localisation"
            )),
            FicheRow(concept="", detail_md=(
                "- Signes neurovégétatifs absents si : prise de BB-, "
                "hypoglycémies à répétition, neuropathie végétative diabétique"
            ), kind="piege"),
            FicheRow(concept="Triade de Whipple", detail_md=(
                "- Signes neuroglucopéniques\n"
                "- Glycémie < **0,50 g/L** (< 0,60 g/L chez diabétique)\n"
                "- Correction des symptômes après normalisation glycémie"
            )),
            FicheRow(concept="◆ Fonctionnelle vs organique", detail_md=(
                "| Critère | Hypoglycémie fonctionnelle | Hypoglycémie organique |\n"
                "|---------|---------------------------|------------------------|\n"
                "| Terrain | Sujet anxieux, neurotonique | Prise de poids récente |\n"
                "| Horaire | Post-prandial (2-5h) | À jeun, après effort |\n"
                "| Tableau | Syndrome adrénergique seul | Neuroglucopénie/coma d'emblée |\n"
                "| Glycémie à jeun | Normale | Basse à plusieurs reprises |\n"
            )),
            FicheRow(concept="Épreuve de jeûne", detail_md=(
                "- Hospitalisation, surveillance constante, 72h de jeûne\n"
                "- Bilan initial et répété : glycémie veineuse, **insulinémie**, **peptide C**\n"
                "- Fonctionnelle : épreuve bien supportée, insulinémie et peptide C diminués\n"
                "- Organique : épreuve mal supportée, bilan insulinique perturbé"
            )),
            FicheRow(concept="PEC symptomatique", detail_md=(
                "| Situation | Traitement |\n"
                "|-----------|------------|\n"
                "| Patient conscient calme | Glucose PO 10-20 g + glucide IG bas |\n"
                "| Patient confus/agité | Glucagon 1-2 mg IM/SC (CI si SH ou OH) + glucose PO/IV + G10 IVSE |\n"
                "| Patient inconscient | Hospitalisation + G30% 10-30 mL IV + glucagon 1-2 mg |\n"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Étiologies des hyperthyroïdies — Comparaison", markdown=(
            "| Étiologie | Terrain | TRAK | Scintigraphie | Spécificité |\n"
            "|-----------|---------|------|---------------|-------------|\n"
            "| Basedow | F 20-40 ans, MAI | + | Hyperfixation diffuse | Orbitopathie 50% |\n"
            "| GMHNT | H/F > 40 ans | - | Aspect en damier | Goitre ancien |\n"
            "| Adénome toxique | F 40-60 ans | - | Nodule chaud | Parenchyme éteint |\n"
            "| Surcharge iodée | Amiodarone, PDC | - | Blanche | Dissociation T3/T4 |\n"
            "| De Quervain | Post-viral | - | Blanche | Douleur + CRP |\n"
            "| Thyrotoxicose factice | Prise cachée | - | Blanche | Thyroglobuline effondrée |\n"
        )),
        TableauSynthese(titre="Hypothyroïdie vs Hyperthyroïdie — Signes cliniques", markdown=(
            "| Signe | Hypothyroïdie | Hyperthyroïdie |\n"
            "|-------|--------------|----------------|\n"
            "| Poids | Prise modeste | Amaigrissement |\n"
            "| Température | Frilosité | Thermophobie |\n"
            "| FC | Bradycardie | Tachycardie |\n"
            "| Transit | Constipation | Accélération |\n"
            "| Humeur | Dépression, somnolence | Nervosité, insomnie |\n"
            "| Peau | Sèche, infiltrée | Chaude, moite |\n"
            "| TSH (cause périph.) | Élevée | Effondrée |\n"
        )),
        TableauSynthese(titre="Complications aiguës du diabète — Comparaison", markdown=(
            "| Critère | Acidocétose | Coma hyperosmolaire | Acidose lactique |\n"
            "|---------|------------|---------------------|------------------|\n"
            "| Type diabète | DT1 (++ ) | DT2 sujet âgé | DT2 sous biguanides |\n"
            "| Glycémie | > 2,5 g/L | > 6 g/L | Variable |\n"
            "| Cétonurie | +++ | 0-1+ | - |\n"
            "| pH | < 7,30 | Normal | Diminué |\n"
            "| Osmolalité | Variable | > 320 mOsm/kg | Variable |\n"
            "| Spécificité | Kussmaul, odeur acétone | Troubles vigilance | Collapsus, lactatémie |\n"
        )),
        TableauSynthese(titre="IS primaire vs IS corticotrope", markdown=(
            "| Critère | IS primaire (Addison) | IS corticotrope |\n"
            "|---------|---------------------|------------------|\n"
            "| ACTH | Élevée (> 100 pg/mL) | Normale/basse |\n"
            "| Mélanodermie | Oui | Non |\n"
            "| Aldostérone | Basse, rénine élevée | Normale |\n"
            "| Hyperkaliémie | Oui | Non (pas de déficit minéralocorticoïde) |\n"
            "| Cause fréquente | Auto-immune (80%), BK (20%) | Arrêt brutal corticothérapie |\n"
            "| Traitement | Hydrocortisone + fludrocortisone | Hydrocortisone seule |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Diabète (glycémie à jeun) | > **1,26 g/L** x2 | Seuil diagnostique |\n"
        "| DT1 acidocétose (glycémie) | > **2,50 g/L** | Confirmation biologique |\n"
        "| Acidocétose sévère | pH < **7,1** | Gravité |\n"
        "| Coma hyperosmolaire | Glycémie > **6 g/L** | DT2 sujet âgé |\n"
        "| Coma hyperosmolaire (osmolalité) | > **320 mOsm/kg** | Confirmation |\n"
        "| HbA1c cible DT1 | < **7%** | Équilibre glycémique |\n"
        "| Hypoglycémie | < **0,50 g/L** | < 0,60 si diabétique |\n"
        "| TSH hypothyroïdie (cible) | **0,5-2,5 mUI/L** | Sous lévothyroxine |\n"
        "| Coma myxoedémateux (TSH) | > **50 mUI/L** | Hypothyroïdie profonde |\n"
        "| Cushing freinage minute | Cortisol > **5 ug/L** | Test positif |\n"
        "| IS primaire (ACTH) | > **100 pg/mL** | Maladie d'Addison |\n"
        "| Synacthène (réponse N) | Cortisol 1h > **210 ng/mL** | Élimine IS primaire |\n"
        "| Phéochromocytome (méthoxylés) | > **4N** | Diagnostic positif |\n"
        "| HTA résistante | **10%** des HTA | Hyperaldostéronisme primaire |\n"
        "| Nodule thyroïdien | **4-7%** population | Nodules palpables |\n"
    ))

    points_cles = [
        "L'hyperthyroïdie se dépiste par la **TSH** en 1re intention ; si effondrée, doser la T4L",
        "La maladie de Basedow est la cause la plus fréquente d'hyperthyroïdie : TRAK positifs, orbitopathie",
        "L'hypothyroïdie d'Hashimoto est la cause la plus fréquente en France : Ac anti-TPO élevés",
        "Le DT1 se présente par un syndrome cardinal ou une acidocétose ; ne jamais arrêter l'insuline IV dans les 24 premières heures",
        "Le DT2 est asymptomatique ; débuter par RHD 3-6 mois puis metformine en 1re ligne",
        "Le coma hyperosmolaire du sujet âgé a une mortalité de 20-40% : réhydratation prudente et lente",
        "Le syndrome de Cushing : freinage minute à la DXM en 1re intention, ACTH pour orienter l'étiologie",
        "L'insuffisance surrénale aiguë est une **urgence vitale** : hydrocortisone 100 mg IV sans attendre les résultats",
    ]

    fiche_eclair_md = (
        "**Hyperthyroïdie** : TSH effondrée + T4L augmentée. Basedow (TRAK+, orbitopathie), "
        "GMHNT (damier), adénome toxique (nodule chaud), surcharge iodée (scinti blanche). "
        "ATS 1-2 ans pour Basedow, BB- en attendant. Agranulocytose sous ATS = arrêt définitif.\n\n"
        "**Hypothyroïdie** : TSH augmentée (périphérique) ou basse (centrale). "
        "Hashimoto (anti-TPO), atrophique, post-partum, iatrogène. "
        "Lévothyroxine à vie, TSH cible 0,5-2,5. Coma myxoedémateux = urgence.\n\n"
        "**DT1** : destruction auto-immune cellules B. Syndrome cardinal ou acidocétose. "
        "Insuline à vie, schéma basal-bolus, HbA1c < 7%. "
        "Acidocétose : insuline IV + NaCl + KCl, ne jamais arrêter insuline IV.\n\n"
        "**DT2** : asymptomatique, glycémie > 1,26 g/L x2. RHD puis metformine. "
        "Complications : coma hyperosmolaire (glycémie > 6 g/L), acidose lactique (biguanides), "
        "neuropathie en chaussettes, pied diabétique, macroangiopathie.\n\n"
        "**Cushing** : hypercatabolisme protidique + obésité facio-tronculaire. "
        "CLU, freinage minute DXM, ACTH pour étiologie. "
        "Maladie de Cushing (70%), adénome surrénalien (10%), paranéoplasique (10%).\n\n"
        "**IS** : asthénie + hypotension + mélanodermie (si primaire). "
        "Hyponatrémie + hyperkaliémie. ACTH élevée = primaire, basse = corticotrope. "
        "Hydrocortisone + fludrocortisone à vie. ISA = urgence vitale.\n\n"
        "**HTA endocrine** : hyperaldo (hypokaliémie + rénine basse), "
        "phéochromocytome (triade de Ménard, méthoxylés > 4N).\n\n"
        "**Hypoglycémie** : triade de Whipple (neuroglucopénie + glycémie < 0,5 g/L + correction). "
        "Fonctionnelle (post-prandiale) vs organique (à jeun). Épreuve de jeûne 72h."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Endocrinologie",
        annee="2025-2026",
        item="Items 238, 240, 241, 245, 247, 248, 249, 251",
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
    captions_file = PROJECT_ROOT / "output" / ".work" / "endocrinologie" / "image_captions.json"
    if captions_file.exists():
        # ... (image loading code)
        pass

    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Medecine_generale_endocrinologie_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out} ({pdf_out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()

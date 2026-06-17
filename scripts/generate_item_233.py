"""Génère la fiche de l'Item 233 - Valvulopathies (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Rétrécissement aortique — Généralités et physiopathologie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition et anatomie"),
            PlanSousPartie(lettre="B", titre="Physiopathologie et conséquences hémodynamiques"),
            PlanSousPartie(lettre="C", titre="Étiologies"),
        ]),
        PlanPartie(numero="II", titre="Rétrécissement aortique — Diagnostic et traitement", sous_parties=[
            PlanSousPartie(lettre="A", titre="Clinique et auscultation"),
            PlanSousPartie(lettre="B", titre="Examens complémentaires"),
            PlanSousPartie(lettre="C", titre="Évolution et complications"),
            PlanSousPartie(lettre="D", titre="Traitement et indications"),
        ]),
        PlanPartie(numero="III", titre="Insuffisance mitrale — Mécanismes et étiologies", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition et classification de Carpentier"),
            PlanSousPartie(lettre="B", titre="Physiopathologie"),
            PlanSousPartie(lettre="C", titre="Étiologies"),
            PlanSousPartie(lettre="D", titre="Causes d'IM aiguës"),
        ]),
        PlanPartie(numero="IV", titre="Insuffisance mitrale — Diagnostic et prise en charge", sous_parties=[
            PlanSousPartie(lettre="A", titre="Clinique et auscultation"),
            PlanSousPartie(lettre="B", titre="Examens complémentaires"),
            PlanSousPartie(lettre="C", titre="Évolution et complications"),
            PlanSousPartie(lettre="D", titre="Traitement et indications"),
        ]),
        PlanPartie(numero="V", titre="Insuffisance aortique — Mécanismes et étiologies", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définition et anatomie"),
            PlanSousPartie(lettre="B", titre="Physiopathologie (chronique et aiguë)"),
            PlanSousPartie(lettre="C", titre="Étiologies"),
        ]),
        PlanPartie(numero="VI", titre="Insuffisance aortique — Diagnostic et prise en charge", sous_parties=[
            PlanSousPartie(lettre="A", titre="Clinique et auscultation"),
            PlanSousPartie(lettre="B", titre="Examens complémentaires"),
            PlanSousPartie(lettre="C", titre="Évolution, complications et surveillance"),
            PlanSousPartie(lettre="D", titre="Traitement et indications chirurgicales"),
        ]),
    ]

    # ==========================================================================
    # PARTIE I : Rétrécissement aortique — Généralités et physiopathologie
    # ==========================================================================
    partie_i = Partie(numero="I", titre="Rétrécissement aortique — Généralités et physiopathologie", sous_parties=[
        SousPartie(lettre="A", titre="Définition et anatomie", rows=[
            FicheRow(concept="◆ Définition du RA", detail_md=(
                "- **Rétrécissement aortique (RA)** = obstacle à l'éjection du ventricule gauche localisé "
                "le plus souvent au niveau de la valve aortique\n"
                "- Valvulopathie la plus fréquente\n"
                "- Étiologie principale : **RA dégénératif > 65 ans**"
            )),
            FicheRow(concept="Autres obstacles à l'éjection VG (non abordés ici)", detail_md=(
                "- Rétrécissement supra-aortique\n"
                "- Rétrécissement sous-aortique (diaphragme)\n"
                "- Obstruction dynamique des cardiomyopathies obstructives"
            )),
            FicheRow(concept="Anatomie de la valve aortique", detail_md=(
                "- Normalement **tricuspide** = 3 feuillets (cusps ou sigmoïdes) :\n"
                "  - Cusp antérodroite (en regard sinus de Valsalva antérodroit)\n"
                "  - Cusp antérogauche\n"
                "  - Cusp non coronaire\n"
                "- Ouverture passive vers l'aorte pendant l'éjection ventriculaire\n"
                "- Avec le vieillissement : épaississement, rigidité, calcification → restriction de mobilité"
            )),
            FicheRow(concept="◆ Bicuspidie aortique", detail_md=(
                "- Présente chez **1-2 % de la population**\n"
                "- Anomalie congénitale : fusion ou défaut de séparation embryologique\n"
                "- Favorise la survenue d'un RA"
            )),
        ]),
        SousPartie(lettre="B", titre="Physiopathologie et conséquences hémodynamiques", rows=[
            FicheRow(concept="Principe général", detail_md=(
                "- Diminution de la surface orificielle aortique = résistance à l'éjection ventriculaire\n"
                "- Trois conséquences principales :\n"
                "  - Gradient de pression ventriculoaortique\n"
                "  - Hypertrophie pariétale\n"
                "  - Dysfonction diastolique"
            )),
            FicheRow(concept="Gradient de pression VG-aorte", detail_md=(
                "- En l'absence de RA : gradient très faible 2-5 mmHg (courbes PVG/PAo superposables)\n"
                "- En présence d'un RA : hyperpression intraventriculaire gauche avec gradient PVG > PAo\n"
                "- **Gradient moyen ≥ 40 mmHg** → RA considéré comme **serré**"
            )),
            FicheRow(concept="Hypertrophie pariétale (loi de Laplace)", detail_md=(
                "- ↑ pression intraVG → ↑ contraintes pariétales (postcharge)\n"
                "- Adaptation par **hypertrophie concentrique** : ↑ taille cardiomyocytes, fibrose, "
                "modifications matrice extracellulaire\n"
                "- L'hypertrophie compense l'élévation de pression et normalise les contraintes pariétales\n"
                "- Performance systolique longtemps préservée\n"
                "- Si hypertrophie insuffisante : ↓ FEVG + signes d'insuffisance cardiaque\n"
                "- Possible fibrose intramyocardique (zone de forte contrainte) → récupération "
                "post-opératoire parfois incomplète\n"
                "- Ischémie myocardique par inadéquation apports/besoins"
            )),
            FicheRow(concept="Dysfonction diastolique", detail_md=(
                "- L'hypertrophie pariétale altère la compliance ventriculaire et ralentit la relaxation\n"
                "- ↑ pressions VG en phase de remplissage → transmission rétrograde veines/capillaires "
                "pulmonaires → congestion pulmonaire\n"
                "- La systole atriale prend un rôle majeur dans le remplissage VG\n"
                "- La **fibrillation atriale est mal tolérée** chez un patient atteint de RA"
            )),
            FicheRow(concept="", detail_md=(
                "- RA serré = gradient moyen ≥ 40 mmHg, Vmax > 4 m/s, surface < 1 cm² ou < 0,6 cm²/m²\n"
                "- Performance systolique longtemps préservée par hypertrophie concentrique compensatrice\n"
                "- La FA est mal tolérée car la systole atriale joue un rôle clé"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Étiologies", rows=[
            FicheRow(concept="★ ◆ RA dégénératif (maladie de Mönckeberg)", detail_md=(
                "- Étiologie la plus fréquente chez le sujet **> 65-70 ans**\n"
                "- Prévalence augmente avec l'âge\n"
                "- Dépôt de calcifications à la base des valvules qui deviennent rigides\n"
                "- Valve d'autant plus calcifiée que la sténose est sévère\n"
                "- Physiopathologie proche de l'athérosclérose"
            )),
            FicheRow(concept="★ ◆ Bicuspidie aortique", detail_md=(
                "- Étiologie la plus fréquente **entre 30 et 65 ans**\n"
                "- Bien tolérée pendant l'enfance/adolescence\n"
                "- Malformation évolutive entraînant un RA à l'âge adulte\n"
                "- **Association à anévrisme de l'aorte ascendante** (à rechercher) ± coarctation (rare)\n"
                "- Dépistage familial (apparentés du 1ᵉʳ degré) - transmission autosomique dominante "
                "à pénétrance variable\n"
                "- Forme type I avec raphé (la plus fréquente) : fusion des sigmoïdes antérogauche et "
                "antérodroite"
            )),
            FicheRow(concept="Post-rhumatismal (RAA)", detail_md=(
                "- Devenu rare, observé chez les migrants\n"
                "- En général associé à une insuffisance aortique (IA) et à une atteinte mitrale (RM + IM)"
            )),
            FicheRow(concept="Synthèse étiologique", detail_md=(
                "| Âge | Étiologie principale |\n"
                "|-----|----------------------|\n"
                "| < 65-70 ans | **Bicuspidie** |\n"
                "| > 65-70 ans | **RA dégénératif** |\n"
                "| Migrants, toute âge | **Post-rhumatismal (RAA)** |"
            )),
            FicheRow(concept="", detail_md=(
                "- Toujours rechercher un **anévrisme de l'aorte ascendante** en cas de bicuspidie\n"
                "- Dépister la bicuspidie chez les apparentés du 1ᵉʳ degré"
            ), kind="a_retenir"),
        ]),
    ])

    # ==========================================================================
    # PARTIE II : Rétrécissement aortique — Diagnostic et traitement
    # ==========================================================================
    partie_ii = Partie(numero="II", titre="Rétrécissement aortique — Diagnostic et traitement", sous_parties=[
        SousPartie(lettre="A", titre="Clinique et auscultation", rows=[
            FicheRow(concept="Circonstances de découverte", detail_md=(
                "- Souffle entendu lors d'une consultation\n"
                "- Apparition de symptômes d'effort\n"
                "- Complication : insuffisance cardiaque\n"
                "- Échocardiographie réalisée pour une autre cause"
            )),
            FicheRow(concept="★ ◆ Triade symptomatique du RA serré", detail_md=(
                "- **Dyspnée d'effort**\n"
                "- **Angor d'effort**\n"
                "- **Syncope d'effort**\n"
                "- Précédés d'une longue période asymptomatique (plusieurs années)\n"
                "- Mauvais pronostic en l'absence de traitement"
            )),
            FicheRow(concept="Interrogatoire — point clé", detail_md=(
                "- Le patient peut limiter ses efforts pour ne plus avoir de symptômes\n"
                "- Rechercher une diminution progressive des activités par rapport aux mois/années précédents\n"
                "- Préciser les efforts au cours desquels il est anormalement limité"
            )),
            FicheRow(concept="Palpation", detail_md=(
                "- Frémissement palpatoire au foyer aortique (patient penché en avant, fin d'expiration) :\n"
                "  - Traduit un RA hémodynamiquement significatif\n"
                "  - Souffle d'intensité 4/6\n"
                "- Dans les cas évolués : élargissement et déviation en bas et à gauche du choc de pointe "
                "(dilatation VG)"
            )),
            FicheRow(concept="◆ Auscultation typique", detail_md=(
                "- **Souffle mésosystolique éjectionnel**, intense, rude, râpeux\n"
                "- Maximum au **2ᵉ espace intercostal droit** (foyer aortique)\n"
                "- **Irradiation aux carotides**\n"
                "- Souffle losangique, renforcé après une diastole longue\n"
                "- **Abolition de B2** dans les RA serrés calcifiés\n"
                "- Tonalité parfois musicale au foyer pulmonaire ou à la pointe\n"
                "- Possible souffle d'IA associé = « maladie aortique »"
            )),
            FicheRow(concept="", detail_md=(
                "- Dans le RA évolué avec bas débit, le souffle peut devenir moins intense, "
                "voire quasiment inaudible"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Examens complémentaires", rows=[
            FicheRow(concept="Radiographie thoracique", detail_md=(
                "- Peut être strictement normale\n"
                "- Si RA évolué :\n"
                "  - Cardiomégalie par dilatation VG\n"
                "  - Surcharge pulmonaire si insuffisance cardiaque gauche"
            )),
            FicheRow(concept="Électrocardiogramme", detail_md=(
                "- Peut être normal si RA peu évolué\n"
                "- En cas de RA serré :\n"
                "  - **HVG de surcharge systolique** (T négatives asymétriques en précordiales gauches)\n"
                "  - Hypertrophie atriale gauche\n"
                "  - Troubles de conduction : BBG, BAV 1ᵉʳ degré\n"
                "  - FA (moins fréquente que dans les valvulopathies mitrales)\n"
                "- L'absence d'HVG électrique n'exclut PAS un RA serré"
            )),
            FicheRow(concept="◆ ETT — examen clé", detail_md=(
                "- Permet de :\n"
                "  - Confirmer le diagnostic de RA\n"
                "  - Quantifier la sévérité\n"
                "  - Apprécier le retentissement ventriculaire et hémodynamique\n"
                "  - Éliminer une autre atteinte valvulaire (mitrale notamment)"
            )),
            FicheRow(concept="★ ◆ Critères de RA serré (ETT)", detail_md=(
                "| Paramètre | Valeur seuil RA serré |\n"
                "|-----------|----------------------|\n"
                "| **Vmax** (doppler continu) | **> 4 m/s** (normal ~1 m/s) |\n"
                "| **Gradient moyen** VG-aorte | **> 40 mmHg** |\n"
                "| **Surface aortique** | **< 1 cm² ou < 0,6 cm²/m²** |\n"
                "| **Surface critique** | **≤ 0,75 cm² ou ≤ 0,4 cm²/m²** |\n"
                "- Surface normale : 2 à 3,5 cm²"
            )),
            FicheRow(concept="★ ⚠ RA serré à bas gradient", detail_md=(
                "- Un RA serré peut avoir un gradient moyen < 40 mmHg en cas de **bas débit**\n"
                "- Volume d'éjection systolique **≤ 35 mL/m²** que la FEVG soit préservée ou altérée\n"
                "- **Écho sous dobutamine** à faible dose pour confirmer le caractère serré :\n"
                "  - Si surface dépasse 1 cm² sous dobutamine → **pseudosténose** "
                "(surveiller, traiter comme insuffisance cardiaque)"
            )),
            FicheRow(concept="Retentissement ETT", detail_md=(
                "- Sur le VG : degré d'hypertrophie, dilatation, FEVG\n"
                "- Sur le débit cardiaque : longtemps conservé, baisse dans les RA évolués\n"
                "- PAP : reste longtemps normale, s'élève si dysfonction VG\n"
                "- Strain et IRM (recherche de fibrose) peuvent compléter si doute"
            )),
            FicheRow(concept="Coronarographie préopératoire", detail_md=(
                "- Indications :\n"
                "  - Âge **> 40 ans** chez l'homme et chez la femme ménopausée sans FdR\n"
                "  - Facteurs de risque coronarien (personnels ou familiaux) quel que soit l'âge\n"
                "  - Angor d'effort ou signes d'insuffisance cardiaque\n"
                "- Justifiée car angor possible dans le RA sans coronaropathie (impossible à distinguer "
                "cliniquement)"
            )),
            FicheRow(concept="Coroscanner et scanner cardiaque", detail_md=(
                "- Coroscanner : place controversée chez sujets âgés (calcifications coronariennes gênant "
                "l'interprétation)\n"
                "- **Scanner cardiaque obligatoire avant TAVI** :\n"
                "  - Mesure anneau aortique, culot aortique, distance des ostia coronaires\n"
                "  - Évaluation des axes vasculaires (voie d'abord percutanée)\n"
                "- Score calcique valvulaire (RA dégénératif) :\n"
                "  - **> 2 000 unités Agatston** chez l'homme\n"
                "  - **> 1 200 unités Agatston** chez la femme\n"
                "  - → en faveur d'un RA serré"
            )),
            FicheRow(concept="★ ⚠ Épreuve d'effort", detail_md=(
                "- Indication : RA serré asymptomatique (vérification objective du caractère asymptomatique)\n"
                "- Évalue niveau d'effort + adaptation de la PA (chute ou non-augmentation)\n"
                "- **CONTRE-INDIQUÉE dans le RA symptomatique**"
            )),
            FicheRow(concept="Cathétérisme", detail_md=(
                "- Habituellement non réalisé (mêmes paramètres obtenus en échodoppler)\n"
                "- Indications restantes : rares cas de discordance clinique/échographie "
                "(patients peu échogènes)"
            )),
        ]),
        SousPartie(lettre="C", titre="Évolution et complications", rows=[
            FicheRow(concept="Évolution naturelle", detail_md=(
                "- RA peut rester longtemps asymptomatique\n"
                "- **Apparition des symptômes = mauvais pronostic** en l'absence de traitement\n"
                "- Doit faire poser l'indication thérapeutique"
            )),
            FicheRow(concept="◆ Complications du RA", detail_md=(
                "- Insuffisance cardiaque\n"
                "- Fibrillation atriale (mal tolérée car perte de la systole atriale)\n"
                "- Troubles de conduction\n"
                "- **Mort subite +++** (surtout RA serré symptomatique)\n"
                "- Endocardite (rare)\n"
                "- Hyperexcitabilité ventriculaire (rare)\n"
                "- Embolies calcaires systémiques (rares) : artères cérébrales, rénales, coronaires, "
                "artère centrale de la rétine (pertes transitoires de vision)\n"
                "- Anémie ferriprive par hémorragie digestive : angiodysplasies intestinales + "
                "anomalie acquise du facteur Von Willebrand = **syndrome de Heyde**"
            )),
        ]),
        SousPartie(lettre="D", titre="Traitement et indications", rows=[
            FicheRow(concept="Prothèses valvulaires — comparaison", detail_md=(
                "| Type | Anticoagulation | Durabilité | Indication |\n"
                "|------|----------------|------------|------------|\n"
                "| **Mécanique** | **AVK à vie** | Longue | Sujet **jeune** |\n"
                "| **Biologique** | Non requise | Risque de dégénérescence à **10-15 ans** | Patient **> 65 ans** |"
            )),
            FicheRow(concept="★ ◆ TAVI (implantation percutanée d'une prothèse aortique)", detail_md=(
                "- Voie d'abord : fémorale ou apicale\n"
                "- Prothèse biologique\n"
                "- Indication validée en **Heart Team** (équipe médico-chirurgicale ESC)\n"
                "- Décision selon : âge, fragilité, comorbidités, souhaits du patient\n"
                "- A dépassé en nombre les remplacements valvulaires chirurgicaux en France\n"
                "- Recommandé :\n"
                "  - Patients inopérables ou à risque opératoire quel que soit l'âge\n"
                "  - **1ʳᵉ intention chez les patients > 75 ans** quel que soit le risque chirurgical "
                "(si voie fémorale possible)"
            )),
            FicheRow(concept="Valvuloplastie percutanée", detail_md=(
                "- Dilatation simple du RA par ballon, sans prothèse\n"
                "- Quasi abandonnée (taux élevé de resténose précoce)\n"
                "- Reste indiquée en cas de chirurgie urgente non cardiaque à risque chez patients "
                "avec RA serré symptomatique"
            )),
            FicheRow(concept="◆ Indications RA serré symptomatique", detail_md=(
                "- Tout RA serré symptomatique doit être pris en charge (**RVA ou TAVI**)\n"
                "- Pratiquement sans limite d'âge (sous réserve d'état général conservé et "
                "d'absence d'autre pathologie pronostique court terme)\n"
                "- Risque vital justifie l'intervention"
            )),
            FicheRow(concept="◆ Indications RA serré asymptomatique", detail_md=(
                "- Surveillance préférée si FEVG normale, sauf :\n"
                "  - Épreuve d'effort anormale\n"
                "  - RA très serré : **Vmax > 5 m/s**\n"
                "  - Aggravation rapide de la sténose lors du suivi\n"
                "  - **FEVG < 55 %**"
            )),
            FicheRow(concept="RA avec dysfonction VG (FE < 35 %)", detail_md=(
                "- Risque opératoire plus élevé, pronostic plus mauvais à long terme\n"
                "- Pronostic le pire chez les patients non opérés\n"
                "- Échocardiographie de stress sous dobutamine : évalue la réserve de contractilité, "
                "exclut une pseudosténose"
            )),
            FicheRow(concept="Bilan préopératoire", detail_md=(
                "- Imagerie des coronaires (coronarographie ou coroscanner)\n"
                "- Scanner ou IRM de l'aorte si dilatation aortique (bicuspidie) + score calcique valvulaire\n"
                "- Échodoppler des troncs supra-aortiques\n"
                "- Recherche de foyers infectieux ORL/stomatologique (radio des sinus, panoramique dentaire)\n"
                "- Recherche de comorbidités (fonction rénale, pathologie pulmonaire)\n"
                "- Avis gériatrique chez le sujet très âgé"
            )),
            FicheRow(concept="", detail_md=(
                "- Toujours penser à l'**éducation thérapeutique** : prévention de l'EI + consultation "
                "urgente si symptômes d'effort\n"
                "- Penser à une **EI en cas de fièvre** chez un patient porteur de sténose aortique"
            ), kind="a_retenir"),
            FicheRow(concept="", detail_md=(
                "- Ne PAS faire d'épreuve d'effort dans un RA symptomatique\n"
                "- Ne PAS oublier la coronarographie préopératoire selon âge et FdR\n"
                "- Adresser systématiquement au spécialiste : RA symptomatique, souffle modifié, "
                "nouveaux symptômes, suivi annuel"
            ), kind="piege"),
        ]),
    ])

    # ==========================================================================
    # PARTIE III : Insuffisance mitrale — Mécanismes et étiologies
    # ==========================================================================
    partie_iii = Partie(numero="III", titre="Insuffisance mitrale — Mécanismes et étiologies", sous_parties=[
        SousPartie(lettre="A", titre="Définition et classification de Carpentier", rows=[
            FicheRow(concept="◆ Définition de l'IM", detail_md=(
                "- **Défaut d'étanchéité de la valve mitrale** entraînant un reflux de sang du VG vers "
                "l'AG au cours de la systole"
            )),
            FicheRow(concept="Rappel anatomique mitral", detail_md=(
                "- 2 feuillets : antérieur (grande valve) et postérieur (petite valve)\n"
                "- Insertion sur un anneau fibreux\n"
                "- 2 commissures : antéroexterne et postéro-interne\n"
                "- Rattachée au VG par des cordages insérés sur 2 piliers musculaires\n"
                "- En systole : affrontement des deux feuillets dans le plan de l'anneau → étanchéité"
            )),
            FicheRow(concept="◆ Classification de Carpentier", detail_md=(
                "| Type | Mouvement valvulaire | Mécanismes typiques |\n"
                "|------|---------------------|----------------------|\n"
                "| **Type I** | **Normal** (dans le plan de l'anneau) | Perforation, fente, dilatation de "
                "l'anneau (IM atriale) |\n"
                "| **Type II** | **Exagéré** (dépasse le plan, vers AG) | Prolapsus (IM dystrophique) |\n"
                "| **Type IIIa** | **Restrictif systolo-diastolique** | RAA, radiothérapie, IM médicamenteuses |\n"
                "| **Type IIIb** | **Restrictif systolique seulement** | IM secondaire (cardiopathies "
                "dilatées/ischémiques) |"
            )),
            FicheRow(concept="Composants de l'appareil valvulaire mitral", detail_md=(
                "- Anneau\n"
                "- Feuillets\n"
                "- Cordages\n"
                "- Piliers (+ leur déplacement si ventricule sphérique/dilaté)\n"
                "- L'IM peut résulter d'une ou plusieurs anomalies isolées ou conjointes"
            )),
        ]),
        SousPartie(lettre="B", titre="Physiopathologie", rows=[
            FicheRow(concept="Facteurs influençant le volume régurgité", detail_md=(
                "- Taille de l'orifice régurgitant\n"
                "- Gradient de pression VG-AG\n"
                "- Durée de la systole"
            )),
            FicheRow(concept="Conséquences en aval (VG)", detail_md=(
                "- Surcharge volumique du VG → dilatation ventriculaire\n"
                "- **Hypertrophie excentrique** des parois (lutte contre stress pariétal)\n"
                "- À terme : dysfonction ventriculaire + fibrose myocardique (potentiel de récupération "
                "réduit)\n"
                "- ⚠ La FEVG est surestimée dans l'IM car le VG est déchargé (éjecte moins de sang dans "
                "l'aorte qu'il ne le devrait)\n"
                "- On parle de **dysfonction à FE < 60 %**"
            )),
            FicheRow(concept="Conséquences en amont (AG, circulation pulmonaire)", detail_md=(
                "- Dilatation de l'AG → risque de **FA**\n"
                "- HTP post-capillaire par élévation pression AG\n"
                "  - Cathétérisme : **PAPO > 15 mmHg** + onde V de reflux\n"
                "- L'HTP dépend du volume régurgité, de la compliance de l'AG et des veines pulmonaires\n"
                "- Dans l'IM chronique : dilatation AG maintient une pression intra-atriale subnormale "
                "(PAP peu élevée pendant longtemps)\n"
                "- En cas d'IM aiguë : AG non dilatée → HTP immédiate"
            )),
            FicheRow(concept="", detail_md=(
                "- **Correction recommandée chez patient asymptomatique** si :\n"
                "  - **Diamètre télésystolique du VG ≥ 40 mm** et/ou\n"
                "  - **FEVG ≤ 60 %**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Étiologies", rows=[
            FicheRow(concept="◆ Classification physiopathologique", detail_md=(
                "- **IM primaires (organiques)** : anomalie initiale au niveau des feuillets ou cordages\n"
                "- **IM secondaires (fonctionnelles)** : feuillets normaux, anomalie au niveau du ventricule "
                "(origine ventriculaire) ou de l'anneau dilaté à la suite d'une dilatation de l'AG "
                "(origine atriale)"
            )),
            FicheRow(concept="◆ IM dystrophique = type II de Carpentier (la + fréquente)", detail_md=(
                "- Étiologie la plus fréquente des fuites mitrales sévères = IM primaire\n"
                "- Élongations ou ruptures de cordages, ± excès de tissu valvulaire avec ballonnisation\n"
                "- Ballonnisation : bombement du feuillet en systole dans l'AG, bord libre reste dans le plan\n"
                "- **Prolapsus** : extrémité du feuillet passe en arrière du plan de l'anneau\n"
                "- Peut prédominer sur valve postérieure (petite), antérieure (grande) ou les deux"
            )),
            FicheRow(concept="Sous-types d'IM dystrophiques", detail_md=(
                "| Sous-type | Caractéristiques | Mécanisme |\n"
                "|-----------|------------------|-----------|\n"
                "| **Dégénérescence myxoïde (maladie de Barlow)** | **Excès de tissu**, valves redondantes, "
                "épaissies | Excès de mobilité, ruptures de cordages |\n"
                "| **Dégénérescence fibroélastique** (+ fréquente) | Sujets **âgés**, ♂, surtout valve "
                "**postérieure**, pas d'excès de tissu | **Rupture de cordages** |\n"
                "- Possibles dans la **maladie de Marfan** ou d'**Ehlers-Danlos**"
            )),
            FicheRow(concept="IM secondaire = type IIIb de Carpentier", detail_md=(
                "- IM d'origine ischémique : classiquement après **infarctus inférieur** "
                "(trouble séquellaire de cinétique pariétale)\n"
                "- IM par dilatation et dysfonction du VG (toutes causes)"
            )),
            FicheRow(concept="IM rhumatismale et apparentées = type IIIa de Carpentier", detail_md=(
                "- IM restrictive (systolo-diastolique)\n"
                "- Devenue rare dans les pays développés, endémique dans pays en développement\n"
                "- Souvent associée à un rétrécissement mitral + atteinte valve aortique\n"
                "- Valves épaissies, rétractées, appareil sous-valvulaire remanié, cordages raccourcis, "
                "ruptures possibles\n"
                "- Association sténose + IM = « maladie mitrale »\n"
                "- IM apparentées : médicamenteuses (ergot de seigle, fenfluramine, benfluorex), "
                "post-radiothérapiques"
            )),
            FicheRow(concept="IM atriale (type I de Carpentier)", detail_md=(
                "- IM secondaire par dilatation de l'anneau sans atteinte des feuillets\n"
                "- Sur atriums très dilatés (souvent FA permanente)\n"
                "- Plus rare"
            )),
            FicheRow(concept="IM sur endocardite", detail_md=(
                "- Survient sur lésion préexistante dans plus de la moitié des cas\n"
                "- Lésions végétantes + mutilantes (destruction du feuillet)\n"
                "- Mécanisme : ruptures de cordages (type II) ou perforations/déchirures valvulaires "
                "(type I), surtout valve antérieure"
            )),
            FicheRow(concept="Autres causes d'IM", detail_md=(
                "- **IM ischémique aiguë** par rupture de pilier mitral → choc, urgence chirurgicale\n"
                "- CMH obstructive : SAM (mouvement systolique antérieur), fuite par défaut de coaptation\n"
                "- Congénitale (fente de la valve antérieure, canal atrioventriculaire)\n"
                "- Traumatique (rare)\n"
                "- Dystrophies conjonctivoélastiques (Marfan, Ehlers-Danlos, pseudoxanthome élastique)\n"
                "- Maladies auto-immunes : lupus + SAPL\n"
                "- Calcifications de l'anneau (origine dégénérative)"
            )),
        ]),
        SousPartie(lettre="D", titre="Causes d'IM aiguës", rows=[
            FicheRow(concept="◆ Causes d'IM aiguës", detail_md=(
                "- Rupture de cordages :\n"
                "  - Dégénérescence myxoïde ou fibroélastique\n"
                "  - **Endocardite**\n"
                "  - Traumatisme thoracique\n"
                "- Rupture de pilier, restriction aiguë sur akinésie, dysfonction ischémique de pilier "
                "(contexte d'IDM)\n"
                "- Traumatisme thoracique\n"
                "- Perforation par endocardite"
            )),
            FicheRow(concept="", detail_md=(
                "- L'IM aiguë est le plus souvent responsable d'un tableau hémodynamique grave "
                "(urgence vitale)\n"
                "- Particularité : **OAP unilatéral** possible avec régurgitation « directionnelle » "
                "vers les veines pulmonaires d'un seul poumon"
            ), kind="a_retenir"),
        ]),
    ])

    # ==========================================================================
    # PARTIE IV : Insuffisance mitrale — Diagnostic et prise en charge
    # ==========================================================================
    partie_iv = Partie(numero="IV", titre="Insuffisance mitrale — Diagnostic et prise en charge", sous_parties=[
        SousPartie(lettre="A", titre="Clinique et auscultation", rows=[
            FicheRow(concept="Circonstances de découverte", detail_md=(
                "- Découverte d'un souffle lors d'une visite systématique\n"
                "- Signes fonctionnels : palpitations, dyspnée d'effort, asthénie d'effort\n"
                "- Complication : OAP, FA\n"
                "- Fièvre prolongée (endocardite)"
            )),
            FicheRow(concept="Signes fonctionnels", detail_md=(
                "- Absents dans l'IM modérée\n"
                "- IM sévère possiblement asymptomatique\n"
                "- IM chronique : dyspnée d'effort progressive + asthénie\n"
                "- Tardivement : dyspnée de repos, palpitations, orthopnée, dyspnée paroxystique nocturne\n"
                "- **OAP** : signe tardif et de gravité"
            )),
            FicheRow(concept="Palpation", detail_md=(
                "- Frémissement systolique à l'apex\n"
                "- Déviation et abaissement du choc de pointe si dilatation VG"
            )),
            FicheRow(concept="◆ Auscultation typique de l'IM", detail_md=(
                "- **Souffle holosystolique de régurgitation** débutant dès B1 et se poursuivant jusqu'à "
                "B2 (peut le dépasser)\n"
                "- Maximum à la pointe, siège **apexoaxillaire** (foyer mitral)\n"
                "- Timbre « en jet de vapeur », doux, parfois rude\n"
                "- Intensité variable (souvent proportionnelle à la sévérité, mais pas toujours)\n"
                "- Irradiation vers l'**aisselle**\n"
                "- Souffle ne se renforce PAS après une diastole longue (≠ RA)"
            )),
            FicheRow(concept="⚠ Cas particulier : prolapsus", detail_md=(
                "- Souffle débute parfois après B1 par un **clic mésosystolique** (mise en tension des "
                "cordages)\n"
                "- Souffle mésotélésystolique ou télésystolique\n"
                "- Dans le prolapsus du feuillet postérieur : irradiation vers la base du cœur "
                "(foyer aortique) car jet orienté vers le septum interauriculaire et la partie postérieure "
                "de l'aorte"
            )),
            FicheRow(concept="Autres signes si IM importante", detail_md=(
                "- B3 (galop protodiastolique)\n"
                "- Roulement mésodiastolique (hyperdébit, mime un RM)\n"
                "- Éclat de B2 au foyer pulmonaire si HTP\n"
                "- Souffle d'IT fonctionnelle si HTP et retentissement droit\n"
                "- Râles crépitants d'insuffisance cardiaque gauche"
            )),
            FicheRow(concept="", detail_md=(
                "- Le souffle des IM secondaires est souvent **très discret, voire inaudible**, "
                "mal corrélé à la sévérité"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Examens complémentaires", rows=[
            FicheRow(concept="ECG", detail_md=(
                "- Reste longtemps normal\n"
                "- Peut objectiver :\n"
                "  - Hypertrophie atriale gauche\n"
                "  - HVG\n"
                "  - FA\n"
                "  - Hypertrophie ventriculaire droite (IM évoluée avec HTP sévère)"
            )),
            FicheRow(concept="Radiographie thoracique", detail_md=(
                "- Normale dans les IM minimes/modérées\n"
                "- Cardiomégalie par dilatation VG\n"
                "- Dilatation AG : arc moyen gauche convexe, débord arc inférieur droit\n"
                "- Signes d'HTP et d'IC si IM chronique évoluée ou aiguë :\n"
                "  - Dilatation des artères pulmonaires\n"
                "  - Redistribution vasculaire vers les sommets\n"
                "  - **Lignes de Kerley**\n"
                "  - Œdème alvéolaire"
            )),
            FicheRow(concept="◆ ETT — examen clé", detail_md=(
                "- Diagnostic positif : signal doppler holosystolique en arrière du plancher mitral\n"
                "- Diagnostic étiologique : précise le mécanisme selon classification de Carpentier\n"
                "- Diagnostic de sévérité : quantification de la fuite et retentissement"
            )),
            FicheRow(concept="◆ Quantification - grades de l'IM primaire", detail_md=(
                "| Grade | SOR (mm²) | Volume régurgité (mL) |\n"
                "|-------|-----------|----------------------|\n"
                "| **I** (minime) | **< 20** | **< 30** |\n"
                "| **II** (modérée) | **20-29** | **30-44** |\n"
                "| **III** (moyenne) | **30-39** | **45-59** |\n"
                "| **IV** (importante) | **≥ 40** | **≥ 60** |\n"
                "- **IM significative** = grade III ou IV\n"
                "- **IM secondaire** : seuil de sévérité **SOR ≥ 30 mm²**"
            )),
            FicheRow(concept="Méthode PISA", detail_md=(
                "- Proximal isovelocity surface area\n"
                "- Calcul de la surface de l'orifice régurgitant (**SOR**)"
            )),
            FicheRow(concept="Retentissement ETT", detail_md=(
                "- Dilatation VG : **diamètre télésystolique ≥ 40 mm**\n"
                "- Fonction VG : **FE ≤ 60 %**\n"
                "- Volume AG : **≥ 60 mL/m²**\n"
                "- Pressions droites : **PAP systolique ≥ 50 mmHg**"
            )),
            FicheRow(concept="⚠ IM secondaire — particularités d'évaluation", detail_md=(
                "- Fuite mitrale secondaire dépendante de la volémie = « accordéon »\n"
                "- Évaluation à répéter, après optimisation du traitement médical de l'insuffisance "
                "cardiaque"
            )),
            FicheRow(concept="Autres valves", detail_md=(
                "- Vérifier surtout la valve tricuspide :\n"
                "  - Recherche de prolapsus, dilatation d'anneau, fuite\n"
                "  - **Annuloplastie tricuspide** si fuite + anneau > 40 mm (apicale 4 cavités) "
                "lors du geste mitral"
            )),
            FicheRow(concept="ETO", detail_md=(
                "- Complète l'étude des mécanismes et étiologies\n"
                "- Aide à planifier une plastie mitrale\n"
                "- Examen fondamental et obligatoire pour le diagnostic des **IM sur endocardite** "
                "(visualisation des végétations parfois très fines)\n"
                "- Précise les ruptures partielles de cordages et les segments atteints en cas de prolapsus"
            )),
            FicheRow(concept="Bilan préopératoire coronarien", detail_md=(
                "- Coroscanner si faible probabilité prétest de coronaropathie\n"
                "- Coronarographie si :\n"
                "  - Suspicion d'ischémie myocardique\n"
                "  - Altération de la fonction systolique (baisse FEVG)\n"
                "  - Homme > 40 ans ou femme ménopausée\n"
                "  - Facteurs de risque cardiovasculaire\n"
                "- Cathétérisme droit : mesure du débit (thermodilution), des pressions droites"
            )),
            FicheRow(concept="Épreuve d'effort et écho d'effort", detail_md=(
                "- Démasquage de symptômes chez patient se disant asymptomatique\n"
                "- VO₂ : capacité à l'effort\n"
                "- Échographie d'effort : appréciation de la fuite à l'effort + retentissement sur les "
                "pressions pulmonaires"
            )),
        ]),
        SousPartie(lettre="C", titre="Évolution et complications", rows=[
            FicheRow(concept="Évolution naturelle", detail_md=(
                "- Dépend de la sévérité, étiologie, rapidité de constitution, fonction VG, lésions "
                "associées (coronaropathie)\n"
                "- IM constituées progressivement : bien tolérées longtemps, signes d'IC tardifs\n"
                "- Suivi régulier avec ETT annuelle\n"
                "- IM aiguës (rupture de cordages, endocardite, IDM) : mal tolérées, OAP rapide"
            )),
            FicheRow(concept="Complications", detail_md=(
                "- Rupture de cordage : IM dystrophique par prolapsus, parfois RAA ou CMH\n"
                "- Endocardite infectieuse : aggravation de la fuite\n"
                "- Troubles du rythme :\n"
                "  - **FA / flutter** : favorisés par la dilatation AG, justifient une chirurgie précoce "
                "même chez l'asymptomatique\n"
                "  - Troubles du rythme ventriculaire : plus rares, signent une détérioration de la "
                "fonction VG\n"
                "  - Cas du prolapsus mitral avec **disjonction annulaire** : femme jeune avec ESV + "
                "ondes T négatives en précordium, risque exceptionnel de mort subite\n"
                "- Insuffisance cardiaque : tardive si IM chronique, rapide si IM aiguë"
            )),
        ]),
        SousPartie(lettre="D", titre="Traitement et indications", rows=[
            FicheRow(concept="Surveillance (IM minime ou modérée, grade I-II)", detail_md=(
                "- Réévaluation clinique et échocardiographique régulière\n"
                "- Prévention oslérienne de l'EI : hygiène cutanée + soins dentaires\n"
                "- Pas d'antibioprophylaxie systématique recommandée"
            )),
            FicheRow(concept="Traitement médical", detail_md=(
                "- Si IM importante et symptomatique → penser à la chirurgie\n"
                "- IM secondaire : traitement de l'insuffisance cardiaque (médicaments, "
                "resynchronisation si QRS larges) - intervention discutée si échec\n"
                "- IM primaire : pas de traitement médical spécifique :\n"
                "  - Poussée d'IC : diurétiques + vasodilatateurs\n"
                "  - IM aiguë : traiter OAP/choc + chirurgie en urgence\n"
                "  - FA → anticoagulation orale\n"
                "  - Maladie de Marfan : **bêtabloquants** (réduction risque dissection aortique)"
            )),
            FicheRow(concept="◆ Plastie mitrale (réparation) — traitement de référence", detail_md=(
                "- Respecte l'appareil sous-valvulaire → moins de dysfonctions VG post-opératoires\n"
                "- Moindre morbi-mortalité à long terme que le RVM\n"
                "- Moindre risque d'endocardite\n"
                "- Pas d'anticoagulants au long cours\n"
                "- **Indiquée dans les prolapsus** ± rupture de cordages\n"
                "- Bons résultats à long terme (léger risque de récidive)\n"
                "- Possible dans certaines IM post-rhumatismales ou ischémiques (risque de récidive)\n"
                "- Nécessite expérience importante du chirurgien"
            )),
            FicheRow(concept="Remplacement valvulaire mitral", detail_md=(
                "- Si plastie impossible (valve trop remaniée)\n"
                "- **Prothèse mécanique** : AVK à vie, durabilité longue, sujet jeune ou FA associée\n"
                "- **Prothèse biologique** : pas d'AVK, risque de dégénérescence, patient âgé ou "
                "contre-indication aux anticoagulants ou désir de grossesse\n"
                "- Choix selon âge, rythme (FA), préférence, risque AVK :\n"
                "  - **> 70 ans → bioprothèse**\n"
                "  - **< 65 ans → prothèse mécanique**"
            )),
            FicheRow(concept="Traitement percutané (clip)", detail_md=(
                "- Réparation bord à bord percutanée (rapprochement feuillets antérieur/postérieur)\n"
                "- ESC 2021 : uniquement en cas de haut risque ou contre-indication chirurgicale\n"
                "- Critères échocardiographiques précis d'éligibilité"
            )),
            FicheRow(concept="« Clinique des valves » et Heart Team", detail_md=(
                "- Discussion collégiale pluridisciplinaire : clinique, imagerie, chirurgie, anesthésie, "
                "cathétérisme interventionnel\n"
                "- Niveau 1 des recommandations ESC 2021"
            )),
            FicheRow(concept="◆ Indications thérapeutiques — IM aiguë", detail_md=(
                "- **IM aiguë mal tolérée → chirurgie urgente**"
            )),
            FicheRow(concept="◆ Indications — IM chronique primaire significative symptomatique", detail_md=(
                "- Chirurgie : **plastie reconstructrice +++**\n"
                "- Si plastie impossible :\n"
                "  - RVM si FE > 30 %\n"
                "  - **FE < 30 % → RVM contre-indiqué** (baisse FE moyenne 10-15 % en post-op) : "
                "traitement médical ou transplantation cardiaque si patient relativement jeune\n"
                "- Clip percutané : IM dystrophique symptomatique chez patient inopérable ou haut "
                "risque chirurgical"
            )),
            FicheRow(concept="◆ Indications — IM chronique primaire importante asymptomatique", detail_md=(
                "- Chirurgie (plastie privilégiée) si l'IM retentit sur le VG (au moins un critère) :\n"
                "  - **DTS du VG ≥ 40 mm** et rupture de cordage\n"
                "  - **FEVG ≤ 60 %**\n"
                "  - **PAP systolique ≥ 50 mmHg** au repos\n"
                "  - FA associée (même paroxystique) ou dilatation AG > 60 mL/m² en rythme sinusal\n"
                "- Sinon surveillance ETT tous les 6 mois + chirurgie si apparition de :\n"
                "  - Retentissement (FE ≤ 60 %, DTS ≥ 40 mm, vol AG indexé ≥ 60 mL/m²) entre 2 examens\n"
                "  - Symptômes (dyspnée d'effort)\n"
                "  - Trouble du rythme supraventriculaire (FA)"
            )),
            FicheRow(concept="Synthèse stratégique", detail_md=(
                "| Situation | Conduite |\n"
                "|-----------|----------|\n"
                "| IM grade I-II isolée | **Pas d'intervention** |\n"
                "| Autres IM | **Surveillance ETT tous les 6 mois** |\n"
                "| IM primaire grade III-IV **symptomatique** | **Chirurgie** (plastie +++) |\n"
                "| IM primaire asympt. + dilatation VG, FE≤60 %, PAP≥50, FA | **Chirurgie** |\n"
                "| IM secondaire | **Traiter l'IC d'abord** ; chirurgie/clip si échec |"
            )),
            FicheRow(concept="Bilan préopératoire", detail_md=(
                "- Imagerie des coronaires (coronarographie ou coroscanner)\n"
                "- Échodoppler des troncs supra-aortiques\n"
                "- Recherche de foyers infectieux ORL/stomatologique (radio sinus + panoramique dentaire)\n"
                "- Recherche de comorbidités\n"
                "- Avis gériatrique chez le sujet très âgé"
            )),
            FicheRow(concept="", detail_md=(
                "- L'éducation thérapeutique de l'IM est INDISPENSABLE : prévention de l'EI, "
                "consultation rapide en cas de fièvre ou symptômes nouveaux\n"
                "- TOUJOURS adresser au spécialiste : IM symptomatique, IM avec souffle modifié, "
                "nouveaux symptômes, suivi annuel"
            ), kind="a_retenir"),
        ]),
    ])

    # ==========================================================================
    # PARTIE V : Insuffisance aortique — Mécanismes et étiologies
    # ==========================================================================
    partie_v = Partie(numero="V", titre="Insuffisance aortique — Mécanismes et étiologies", sous_parties=[
        SousPartie(lettre="A", titre="Définition et anatomie", rows=[
            FicheRow(concept="◆ Définition de l'IA", detail_md=(
                "- **Reflux de sang de l'aorte vers le VG** en diastole\n"
                "- Également appelée régurgitation valvulaire aortique ou fuite aortique\n"
                "- Valvulopathie peu fréquente, dont la prévalence augmente avec l'âge"
            )),
            FicheRow(concept="Anatomie de la racine aortique", detail_md=(
                "- Anneau aortique (insertion des cusps)\n"
                "- Sinus aortiques (de Valsalva) : zone d'insertion des commissures\n"
                "- Jonction sinotubulaire\n"
                "- Aorte initiale\n"
                "- Valve aortique normale : tricuspide (3 cusps : antérodroite, antérogauche, non "
                "coronaire), forme en « nid d'hirondelle »\n"
                "- **Bicuspidie** : 1-2 % de la population (cause d'IA et de RA)"
            )),
        ]),
        SousPartie(lettre="B", titre="Physiopathologie (chronique et aiguë)", rows=[
            FicheRow(concept="Facteurs du volume de la fuite", detail_md=(
                "- Taille de l'orifice régurgitant\n"
                "- Durée de la diastole\n"
                "- Gradient de pression de part et d'autre de l'orifice aortique en diastole"
            )),
            FicheRow(concept="◆ Surcharge mécanique mixte du VG (IA chronique)", detail_md=(
                "- **Surcharge volumétrique** : volume sanguin régurgité en diastole → ↑ volume "
                "télédiastolique et précharge\n"
                "- **Surcharge barométrique** : ↑ volume d'éjection systolique → ↑ PAS aortique "
                "(augmentation de la postcharge)"
            )),
            FicheRow(concept="Remodelage VG en cas d'IA chronique", detail_md=(
                "- ↑ précharge et postcharge → remodelage VG visant à normaliser la contrainte pariétale\n"
                "- **Hypertrophie excentrique** (plus marquée que dans l'IM)\n"
                "- Remodelage maladaptatif à terme : destruction cardiomyocytaire + fibrose interstitielle\n"
                "- Hypertrophie myocardique compensatrice initialement → FE normale\n"
                "- Compliance VG grande → fonctionnement avec pressions normales malgré dilatation pendant "
                "des années\n"
                "- Progressivement : altération contractilité + compliance → IC d'effort puis de repos\n"
                "- VG très dilaté ou FE abaissée → remodelage potentiellement irréversible après chirurgie"
            )),
            FicheRow(concept="Conséquences aortiques", detail_md=(
                "- ↑ pression systolique (volume d'éjection + compliance aortique)\n"
                "- ↓ pression diastolique (régurgitation)\n"
                "- → ↑ pression artérielle différentielle (pression pulsée) → **hyperpulsatilité artérielle**"
            )),
            FicheRow(concept="Conséquences coronariennes", detail_md=(
                "- ↓ pression diastolique aortique → ↓ perfusion coronarienne (perfusion en diastole)\n"
                "- IA sévère : possible « vol » coronarien (aspiration du sang coronarien en diastole "
                "par la fuite)\n"
                "- Hypoperfusion → angor (de repos ou d'effort) + ischémie + fibrose myocardique"
            )),
            FicheRow(concept="◆ IA aiguë — physiopathologie particulière", detail_md=(
                "- Étiologie principale : **endocardite infectieuse**\n"
                "- IA volumineuse sur cavité VG de taille normale, peu dilatée, à compliance normale\n"
                "- Élévation brutale des pressions de remplissage VG → ↑ pressions AG et circulation "
                "pulmonaire → **œdème pulmonaire**\n"
                "- Auscultation parfois peu audible dans l'IA aiguë\n"
                "- Circulation coronarienne particulièrement pénalisée"
            )),
        ]),
        SousPartie(lettre="C", titre="Étiologies", rows=[
            FicheRow(concept="◆ Classification mécanique (3 types)", detail_md=(
                "| Type | Mouvement des cusps | Mécanisme |\n"
                "|------|---------------------|-----------|\n"
                "| **Type 1** | **Normal** (quasi normal) | Dilatation racine aortique, perforation |\n"
                "| **Type 2** | **Excessif** en diastole (prolapsus) | Prolapsus de cusp |\n"
                "| **Type 3** | **Restreint** | RAA, lésions médicamenteuses |"
            )),
            FicheRow(concept="◆ IA type 1 — mouvement normal", detail_md=(
                "- Dilatation de l'anneau aortique (rarement isolée)\n"
                "- Dilatation de la racine aortique :\n"
                "  - **Maladie annuloectasiante** (dilatation anneau + sinus)\n"
                "  - Maladies génétiques : **Marfan**, Loeys-Dietz, Ehlers-Danlos\n"
                "  - Idiopathique\n"
                "  - Bicuspidie aortique\n"
                "  - Aortites : Takayasu, Horton, Behçet, spondylarthrite ankylosante, syphilis\n"
                "- Perforation/destruction partielle de cusp :\n"
                "  - **Endocardite infectieuse** (cause essentielle)\n"
                "  - Lésion traumatique\n"
                "  - Fenestration (congénitale ou dégénérative)"
            )),
            FicheRow(concept="◆ IA type 2 — prolapsus valvulaire", detail_md=(
                "- Prolapsus valvulaire aortique isolé (valve tricuspide dystrophique ou dysplasique) :\n"
                "  - Fuite excentrée depuis la cusp qui prolabe\n"
                "- Prolapsus dans le cadre d'une bicuspidie : cusp la plus grande (issue de la fusion)\n"
                "- Plus rare : déchirure traumatique, infection, CIV sous-aortique infundibulaire = "
                "**syndrome de Laubry-Pezzi**"
            )),
            FicheRow(concept="◆ IA type 3 — restriction", detail_md=(
                "- **RAA** (principale cause d'IA restrictive) :\n"
                "  - Rare dans pays occidentaux, populations migrantes (Maghreb, Asie, Afrique)\n"
                "  - Épaississement et rétraction des bords libres → orifice central\n"
                "  - Peut être associée à une sténose = « maladie aortique »\n"
                "- Lésions médicamenteuses :\n"
                "  - Dérivés de l'ergot de seigle (antimigraineux)\n"
                "  - Anorexigènes (fenfluramine, dexfenfluramine, benfluorex/Médiator)\n"
                "  - Amphétaminiques (MDMA)\n"
                "  - Action via dérivés de sérotonine\n"
                "- Autres : tumeur carcinoïde (rare car filtre pulmonaire), radiothérapie médiastinale "
                "(lymphome, cancer du sein)"
            )),
            FicheRow(concept="◆ IA aiguë — étiologies", detail_md=(
                "- **Endocardite infectieuse** en phase aiguë : IA souvent massive par destruction/"
                "perforation valvulaire et/ou abcès de l'anneau\n"
                "- **Dissection aortique aiguë** atteignant l'anneau\n"
                "- Traumatisme avec lésion valvulaire (fermé du thorax, décélération, cathétérisme)"
            )),
            FicheRow(concept="IA sur prothèse valvulaire", detail_md=(
                "- IA paraprothétique :\n"
                "  - Désinsertion partielle septique (EI précoce/tardive) ou aseptique (anneau "
                "fragilisé, calcifications)\n"
                "  - Précocement après RVA ou TAVI : généralement minime, à signaler et surveiller\n"
                "- IA intraprothétique :\n"
                "  - Thrombus bloquant l'ailette\n"
                "  - Endocardite\n"
                "  - Dégénérescence de bioprothèse\n"
                "  - IA minime physiologique sur prothèse mécanique ou biologique"
            )),
            FicheRow(concept="", detail_md=(
                "- La maladie annuloectasiante et la dilatation de l'aorte ascendante exposent au "
                "**risque de rupture ou de dissection aortique** → indication chirurgicale possible "
                "sur le diamètre aortique"
            ), kind="a_retenir"),
        ]),
    ])

    # ==========================================================================
    # PARTIE VI : Insuffisance aortique — Diagnostic et prise en charge
    # ==========================================================================
    partie_vi = Partie(numero="VI", titre="Insuffisance aortique — Diagnostic et prise en charge", sous_parties=[
        SousPartie(lettre="A", titre="Clinique et auscultation", rows=[
            FicheRow(concept="Circonstances de découverte", detail_md=(
                "- Le plus souvent fortuite : souffle entendu lors d'une consultation pour autre cause\n"
                "- Bilan d'une pathologie causale\n"
                "- Découverte tardive au stade d'insuffisance cardiaque : devenue rare"
            )),
            FicheRow(concept="Signes fonctionnels", detail_md=(
                "- IA souvent asymptomatique\n"
                "- **Dyspnée d'effort** (NYHA)\n"
                "- Plus rarement angor d'effort ou parfois de repos (fonctionnel, IA massive)\n"
                "- Asthénie anormale (peut signer l'IC sur IA)\n"
                "- Signes au repos : rares, tardifs, mauvais pronostic"
            )),
            FicheRow(concept="◆ Auscultation typique", detail_md=(
                "- **Souffle diastolique +++** :\n"
                "  - Durée variable dans la diastole\n"
                "  - Foyer aortique, irradie le long du bord gauche du sternum\n"
                "  - Mieux perçu **patient penché en avant**, assis/debout, **expiration bloquée**\n"
                "  - Holodiastolique si IA importante\n"
                "  - Protomésodiastolique si IA moindre\n"
                "- Souffle systolique éjectionnel d'accompagnement au foyer aortique (modéré, par "
                "hyperdébit antérograde)\n"
                "- Parfois **roulement de Flint** apexien (sténose mitrale fonctionnelle si IA gêne "
                "l'ouverture mitrale) ou bruit de galop = IA sévère"
            )),
            FicheRow(concept="Palpation", detail_md=(
                "- Choc de pointe étalé, dévié en bas et à gauche si dilatation VG\n"
                "- Choc « en dôme »"
            )),
            FicheRow(concept="◆ Signes périphériques d'hyperpulsatilité", detail_md=(
                "- **Hyperpulsatilité des pouls artériels périphériques ++**\n"
                "- Battements artériels parfois apparents au cou\n"
                "- Oscillation de la tête, pulsatilité sous-unguéale, pulsatilité cutanée\n"
                "- Élargissement de la pression artérielle différentielle avec **abaissement de la PAd** "
                "= IA sévère"
            )),
        ]),
        SousPartie(lettre="B", titre="Examens complémentaires", rows=[
            FicheRow(concept="ECG", detail_md=(
                "- Peut être normal\n"
                "- Rythme généralement sinusal\n"
                "- FA ou ESV = mauvais pronostic\n"
                "- HVG diastolique : onde R ample en précordiales gauches + ondes T positives\n"
                "- Parfois HVG systolique (sous-décalage ST, T négatives en précordiales gauches)"
            )),
            FicheRow(concept="Radiographie thoracique", detail_md=(
                "- Normale dans les IA de petit volume\n"
                "- IA volumineuses chroniques : ↑ index cardiothoracique\n"
                "- Débord aortique au niveau de l'arc moyen droit (aorte déroulée)"
            )),
            FicheRow(concept="◆ ETT — examen clé", detail_md=(
                "- Confirmation diagnostique (DC : insuffisance pulmonaire +++)\n"
                "- Quantification de la fuite\n"
                "- Évaluation étiologique et du retentissement"
            )),
            FicheRow(concept="◆ Grades de l'IA (4 grades)", detail_md=(
                "| Grade | Description |\n"
                "|-------|-------------|\n"
                "| **1** | Minime |\n"
                "| **2** | Minime à modérée |\n"
                "| **3** | Modérée à moyenne |\n"
                "| **4** | Sévère |\n"
                "- Seules les fuites de **grades 3 et 4** entraînent une surcharge volumétrique "
                "significative\n"
                "- Certaines recommandations (US) ne distinguent que 3 grades"
            )),
            FicheRow(concept="Critères indirects de quantification ETT", detail_md=(
                "- Hyperdébit dans la chambre de chasse VG : > 4 L/min/m² (IA grade 3-4)\n"
                "- Dilatation du VG en diastole : signe une surcharge volumétrique ≥ grade 3\n"
                "- Flux télédiastolique isthmique : vitesse rétrograde **≥ 20 cm/s** chez l'adulte → "
                "IA sévère"
            )),
            FicheRow(concept="★ Critères directs de quantification ETT", detail_md=(
                "- **Vena contracta** : diamètre du jet régurgitant à son origine en doppler couleur\n"
                "- **Méthode PISA** (zone de convergence) :\n"
                "  - Surface de l'orifice régurgitant (SOR)\n"
                "  - Volume régurgité par battement"
            )),
            FicheRow(concept="Évaluation du retentissement ETT", detail_md=(
                "- Mesures VG : DTD, DTS (à indexer à la surface corporelle), volumes\n"
                "- Aspect d'hypertrophie excentrique\n"
                "- FEVG (Simpson biplan) : > 50 % dans les IA compensées\n"
                "- Estimation des pressions de remplissage VG\n"
                "- Mesure de la PAP"
            )),
            FicheRow(concept="Évaluation étiologique ETT", detail_md=(
                "- Mobilité des cusps : normale / augmentée / restreinte\n"
                "- Aspect des valves : fines/épaissies, calcifiées, tricuspide/bicuspide\n"
                "- Recherche de végétations ou d'abcès (EI)\n"
                "- Diamètres : anneau aortique, sinus de Valsalva, aorte ascendante\n"
                "- Maladie annuloectasiante : aspect « piriforme » ou « en bulbe d'oignon »\n"
                "- Bicuspidie : dilatation associée de l'aorte ascendante dans ~50 % des cas\n"
                "- Flap en cas de dissection aortique\n"
                "- Atteinte valvulaire associée (mitrale, tricuspide)"
            )),
            FicheRow(concept="ETO — indications", detail_md=(
                "- Échogénicité insuffisante en transthoracique\n"
                "- Examen de l'aorte thoracique\n"
                "- Suspicion d'EI ou de dissection aortique"
            )),
            FicheRow(concept="Test d'effort", detail_md=(
                "- Non systématique, aide à la décision thérapeutique\n"
                "- Apprécie la tolérance fonctionnelle\n"
                "- Trois types : standard, VO₂, échographie d'effort\n"
                "- Critères de mauvaise tolérance :\n"
                "  - Arrêt principalement pour dyspnée ++ (et non épuisement musculaire)\n"
                "  - Capacité d'effort < 80-85 % de la théorique\n"
                "  - Plafonnement du pouls d'O₂\n"
                "  - Défaut de réserve contractile VG en échographie d'effort\n"
                "  - Survenue de troubles du rythme ventriculaire"
            )),
            FicheRow(concept="Imagerie en coupes (scanner, IRM)", detail_md=(
                "- Scanner : disponible mais irradiant (à peser si répétition)\n"
                "- IRM : moins disponible, non irradiante, gadolinium contre-indiqué si IR sévère\n"
                "- Surveillance des dimensions de l'aorte ascendante\n"
                "- IRM permet aussi : volumes VG, FEVG (si mauvaise échogénicité), volume de régurgitation\n"
                "- Coroscanner de plus en plus utilisé en remplacement de la coronarographie préopératoire"
            )),
            FicheRow(concept="Cathétérisme et coronarographie", detail_md=(
                "- Coronarographie préopératoire :\n"
                "  - Hommes > 40 ans, femmes > 50 ans\n"
                "  - Facteurs de risque cardiovasculaire\n"
                "  - Coroscanner avec sténose significative ou inconclusif\n"
                "- Angiographie sus-sigmoïdienne : exceptionnellement réalisée\n"
                "- Cathétérisme droit : si nécessaire (débit + pressions droites)"
            )),
            FicheRow(concept="Diagnostic différentiel", detail_md=(
                "- Insuffisance pulmonaire (contexte différent, cardiopathie congénitale connue)\n"
                "- Double souffle (rupture d'un sinus aortique)\n"
                "- Souffle continu (canal artériel persistant, fistule coronarienne)\n"
                "- Frottement péricardique\n"
                "- L'échographie permet généralement de trancher"
            )),
        ]),
        SousPartie(lettre="C", titre="Évolution, complications et surveillance", rows=[
            FicheRow(concept="IA chronique — évolution", detail_md=(
                "- Faible surrisque d'EI\n"
                "- IA significative (grades 3-4) :\n"
                "  - Longtemps bien tolérée, asymptomatique\n"
                "  - **Apparition de symptômes = tournant pronostique**\n"
                "  - Lésions myocardiques possiblement irréversibles → indication opératoire posée chez "
                "des patients asymptomatiques (dilatation VG, FE)\n"
                "  - Surveillance étroite des IA grade 3-4\n"
                "- Risque de rupture ou dissection aortique sur dilatation aortique → surveillance "
                "annuelle du diamètre par écho ± IRM/scanner\n"
                "- Bicuspidie : risque de dissection légèrement augmenté (mais bien < Marfan)\n"
                "- **Marfan** : dépistage familial obligatoire (apparentés 1ᵉʳ degré)\n"
                "- Bicuspidie : dépistage possible (10 % de récurrence)"
            )),
            FicheRow(concept="IA aiguë — évolution", detail_md=(
                "- Évolution rapide, souvent mal tolérée si sévère\n"
                "- Risque d'**OAP**, voire de mort subite\n"
                "- Chirurgie précoce habituellement nécessaire"
            )),
            FicheRow(concept="Complications de l'IA", detail_md=(
                "- Endocardite infectieuse :\n"
                "  - Prophylaxie (hygiène buccodentaire) toujours recommandée\n"
                "  - Antibioprophylaxie NON systématique sauf si antécédent d'EI, prothèse valvulaire, "
                "cardiopathie cyanogène\n"
                "- Insuffisance cardiaque gauche ou globale (tardive)\n"
                "- Dissection / rupture aortique\n"
                "- Mort subite (rare) : trouble du rythme dans les formes évoluées, rupture aortique"
            )),
            FicheRow(concept="Surveillance IA chronique", detail_md=(
                "- Estimer le volume de la régurgitation\n"
                "- Surveiller progression de la dilatation VG et FEVG\n"
                "- Surveiller dilatation aortique\n"
                "- Prévention EI\n"
                "- Rythme :\n"
                "  - 1 à 2 fois/an si fuite sévère\n"
                "  - Tous les 2 à 3 ans si fuite modérée à moyenne\n"
                "- Comporte : examen clinique, ECG, ETT, test d'effort (≤ 1×/an si IA sévère, "
                "idéalement avec VO₂), IRM/scanner si dilatation aortique, **surveillance dentaire 2×/an**"
            )),
        ]),
        SousPartie(lettre="D", titre="Traitement et indications chirurgicales", rows=[
            FicheRow(concept="Traitement médical", detail_md=(
                "- Aucun traitement médicamenteux spécifique validé dans l'IA\n"
                "- IEC NON recommandés pour prévenir le remodelage ou l'IC\n"
                "- IA sévère + IC congestive : diurétiques ± IEC/vasodilatateurs en attente de chirurgie\n"
                "- **Bêtabloquants classiquement CONTRE-INDIQUÉS** car allongent la diastole et aggravent "
                "la fuite\n"
                "- **Marfan + dilatation aortique** : bêtabloquants = traitement validé (protection aorte)\n"
                "- ARA2 : alternative si intolérance aux bêtabloquants\n"
                "- Sport de compétition CI si IA sévère\n"
                "- Sport de loisir d'endurance encouragé à niveau modéré"
            )),
            FicheRow(concept="Prophylaxie de l'EI", detail_md=(
                "- Gestes à risque (dentaires) :\n"
                "  - Pas d'antibioprophylaxie systématique dans l'IA sur valves natives\n"
                "  - Antibioprophylaxie si : antécédent d'EI, prothèse valvulaire, cardiopathie cyanogène\n"
                "- Hygiène dentaire + examen tous les 6 mois recommandés"
            )),
            FicheRow(concept="Traitement chirurgical — modalités", detail_md=(
                "- IA isolée → **RVA simple** (prothèse mécanique ou biologique)\n"
                "  - Choix discuté entre patient et chirurgien (choix final patient)\n"
                "  - Bioprothèse : après 60-65 ans, ou femme désirant grossesse\n"
                "  - Patient prévenu de réopération vers 10 ans (dégénérescence bioprothèse)\n"
                "- IA + dilatation aortique → RVA + remplacement de l'aorte ascendante :\n"
                "  - **Bentall** : tube prothétique avec réimplantation des coronaires\n"
                "  - Ou tube sus-coronaire (sans réimplantation)\n"
                "- Plastie conservatrice (chirurgiens entraînés) : feuillets normaux ou bicuspidie "
                "peu altérée si IA sur dilatation aortique (Tyron-David, Yacoub)\n"
                "- Autres : intervention de Ross (RVA par valve pulmonaire native), intervention "
                "d'Osaki (autogreffe péricardique)"
            )),
            FicheRow(concept="◆ Indications chirurgicales — IA chronique sévère symptomatique", detail_md=(
                "- **Chirurgie indiquée** (dyspnée, insuffisance cardiaque congestive)"
            )),
            FicheRow(concept="★ ◆ Indications — IA chronique sévère asymptomatique", detail_md=(
                "- Chirurgie si :\n"
                "  - **DTS > 50 mm** ou **> 25 mm/m²** en échographie\n"
                "  - Ou **FEVG ≤ 50 %**\n"
                "- Si chirurgie à bas risque :\n"
                "  - DTS > 20 mm/m²\n"
                "  - Ou FEVG ≤ 55 %\n"
                "- Si chirurgie cardiaque envisagée par ailleurs (pontages, dilatation aortique, autre "
                "valvulopathie)"
            )),
            FicheRow(concept="◆ Indications — sur diamètre aortique", detail_md=(
                "- Tout grade d'IA, dilatation de l'aorte ascendante :\n"
                "  - **Racine aortique ≥ 55 mm** (toute zone de mesure)\n"
                "  - **≥ 50 mm dans le Marfan**\n"
                "  - Marfan + facteurs de risque (ATCD familial/perso de dissection, IA/IM sévère, "
                "désir de grossesse, HTA non contrôlée, progression > 3 mm/an) : **45 mm**\n"
                "  - Bicuspidie + facteurs de risque : **50 mm**"
            )),
            FicheRow(concept="◆ Indications — IA aiguë sévère", detail_md=(
                "- Indication opératoire formelle et urgente en cas de signe d'insuffisance cardiaque\n"
                "- EI : indication chirurgicale non systématique (à discuter si sepsis non maîtrisé, "
                "insuffisance cardiaque, volumineuses végétations à risque embolique)"
            )),
            FicheRow(concept="Bilan préopératoire", detail_md=(
                "- Bilan biologique\n"
                "- Imagerie des coronaires (coroscanner ou coronarographie)\n"
                "- Angioscanner ou ARM aortique si dilatation aortique\n"
                "- Échodoppler des troncs supra-aortiques\n"
                "- Spirométrie si suspicion pathologie respiratoire\n"
                "- Recherche et traitement de foyers infectieux dentaires (panoramique, cone beam) ± ORL "
                "(sinusite)\n"
                "- Recherche d'autres comorbidités\n"
                "- Avis gériatrique > 75 ans"
            )),
            FicheRow(concept="Résultats chirurgicaux", detail_md=(
                "- Résultats excellents (patients opérés plus précocement)\n"
                "- Mortalité périopératoire :\n"
                "  - **1-3 %** : RVA isolé chez patient asymptomatique\n"
                "  - **3-10 %** : patients symptomatiques, ou chirurgie de l'aorte ascendante/pontages associés"
            )),
            FicheRow(concept="TAVI dans l'IA", detail_md=(
                "- Parfois proposé chez patients à très haut risque chirurgical ou inopérables, en "
                "l'absence d'EI\n"
                "- Prothèses non conçues pour cette pathologie (s'accrochent sur calcifications)\n"
                "- Risque de migration après implantation\n"
                "- Reste très marginal actuellement"
            )),
            FicheRow(concept="", detail_md=(
                "- Dépistage familial **formel dans le syndrome de Marfan**, **proposé en cas de bicuspidie**\n"
                "- Penser à la **dissection aortique** devant une IA aiguë sans fièvre avec douleur "
                "thoracique ou AVC\n"
                "- Penser à l'**EI** devant une IA aiguë fébrile"
            ), kind="a_retenir"),
            FicheRow(concept="", detail_md=(
                "- Ne PAS prescrire systématiquement des antibiotiques avant un soin dentaire chez un "
                "patient porteur d'IA sur valve native\n"
                "- Ne PAS traiter une IA symptomatique uniquement par médicaments de l'IC\n"
                "- Ne PAS oublier d'évoquer le Marfan devant une IA avec maladie annuloectasiante"
            ), kind="piege"),
        ]),
    ])

    # ==========================================================================
    # TABLEAUX DE SYNTHÈSE
    # ==========================================================================
    tableaux = [
        TableauSynthese(titre="Critères de sévérité du RA serré (ETT)", markdown=(
            "| Paramètre | Valeur seuil |\n"
            "|-----------|-------------|\n"
            "| Vmax (doppler continu) | **> 4 m/s** |\n"
            "| Gradient moyen VG-aorte | **> 40 mmHg** |\n"
            "| Surface aortique | **< 1 cm² ou < 0,6 cm²/m²** |\n"
            "| Surface critique | **≤ 0,75 cm² ou ≤ 0,4 cm²/m²** |\n"
            "| Surface normale (référence) | 2 à 3,5 cm² |\n"
            "| Vmax normale (référence) | ~1 m/s |\n"
            "| Volume d'éjection (bas débit) | ≤ 35 mL/m² |\n"
            "| Score Agatston (RA serré ♂) | > 2 000 |\n"
            "| Score Agatston (RA serré ♀) | > 1 200 |"
        )),
        TableauSynthese(titre="Classification de Carpentier des IM", markdown=(
            "| Type | Mouvement valvulaire | Étiologies/Mécanismes |\n"
            "|------|---------------------|------------------------|\n"
            "| **I** | Normal (plan de l'anneau) | Perforation, fente, **IM atriale** (dilatation anneau) |\n"
            "| **II** | Exagéré (vers AG, prolapsus) | **IM dystrophique** : Barlow, fibroélastique |\n"
            "| **IIIa** | Restrictif systolo-diastolique | RAA, radiothérapie, médicamenteuses |\n"
            "| **IIIb** | Restrictif systolique seulement | IM secondaire (cardiopathies dilatées/ischémiques) |"
        )),
        TableauSynthese(titre="Grades de sévérité de l'IM primaire", markdown=(
            "| Grade | SOR (mm²) | Volume régurgité (mL) |\n"
            "|-------|-----------|----------------------|\n"
            "| **I** — minime | **< 20** | < 30 |\n"
            "| **II** — modérée | 20-29 | 30-44 |\n"
            "| **III** — moyenne | 30-39 | 45-59 |\n"
            "| **IV** — importante | **≥ 40** | ≥ 60 |\n"
            "- IM **significative** = grade III ou IV\n"
            "- IM **secondaire** : seuil SOR ≥ 30 mm²"
        )),
        TableauSynthese(titre="IA : types mécaniques et étiologies", markdown=(
            "| Type | Mouvement | Étiologies clés |\n"
            "|------|-----------|-----------------|\n"
            "| **Type 1** | Quasi normal | Dilatation racine/anneau (Marfan, Loeys-Dietz, Ehlers-Danlos, idiopathique, aortites, bicuspidie, dissection), perforation (EI, traumatisme, fenestration) |\n"
            "| **Type 2** | Excessif (prolapsus) | Dystrophie/dysplasie valvulaire, bicuspidie, syndrome de Laubry-Pezzi |\n"
            "| **Type 3** | Restreint | RAA, médicamenteuses (ergot, anorexigènes, MDMA), carcinoïde, radiothérapie |"
        )),
        TableauSynthese(titre="Comparaison prothèse mécanique / bioprothèse", markdown=(
            "| Critère | Mécanique | Biologique |\n"
            "|---------|-----------|------------|\n"
            "| Anticoagulation | **AVK à vie** | Non requise |\n"
            "| Durabilité | Très longue | **Dégénérescence 10-15 ans** |\n"
            "| Indication d'âge | **< 65 ans** | **> 65-70 ans** |\n"
            "| Désir de grossesse | Contre-indication relative | Favorisée |\n"
            "| FA associée | Favorise le choix | Bioprothèse possible si AVK indiquée |"
        )),
        TableauSynthese(titre="Comparaison auscultatoire des 3 valvulopathies", markdown=(
            "| Caractère | RA | IM | IA |\n"
            "|-----------|----|----|----|\n"
            "| Type | **Systolique éjectionnel, mésosystolique** | **Holosystolique de régurgitation** | **Diastolique** |\n"
            "| Timbre | Rude, râpeux | « Jet de vapeur » | Doux, humé |\n"
            "| Foyer max | 2ᵉ EICD (aortique) | Pointe (foyer mitral) | Foyer aortique + bord gauche du sternum |\n"
            "| Irradiation | **Carotides** | **Aisselle** (postérieur → base/aortique) | Le long du sternum |\n"
            "| Renforcement après diastole longue | **OUI** | NON | — |\n"
            "| Position | — | — | **Penché en avant, expiration bloquée** |\n"
            "| Autres signes | B2 aboli si serré | Clic dans prolapsus, B3 | Hyperpulsatilité, PA différentielle élargie |"
        )),
        TableauSynthese(titre="Indications opératoires synthétisées", markdown=(
            "| Pathologie | Indications principales |\n"
            "|------------|------------------------|\n"
            "| **RA serré symptomatique** | RVA ou TAVI (quasi sans limite d'âge) |\n"
            "| **RA serré asymptomatique** | Si épreuve d'effort anormale, Vmax > 5 m/s, aggravation rapide, FEVG < 55 % |\n"
            "| **IM primaire grade III-IV symptomatique** | Chirurgie (plastie +++); RVM si FE > 30 % |\n"
            "| **IM primaire grade III-IV asympt.** | Chirurgie si DTS ≥ 40 mm + rupture cordage, FEVG ≤ 60 %, PAP ≥ 50, FA, AG > 60 mL/m² |\n"
            "| **IA chronique sévère sympt.** | Chirurgie |\n"
            "| **IA chronique sévère asympt.** | DTS > 50 mm (ou 25 mm/m²) ; FEVG ≤ 50 % |\n"
            "| **IA + dilat. aortique** | Aorte ≥ 55 mm (≥ 50 si Marfan, ≥ 45 si Marfan + FdR, ≥ 50 si bicuspidie + FdR) |\n"
            "| **IA aiguë sévère** | Chirurgie urgente si IC |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Prévalence bicuspidie | **1-2 %** | Population générale |\n"
        "| Gradient PVG-PAo normal | 2-5 mmHg | Sans RA |\n"
        "| **Vmax RA serré** | **> 4 m/s** | (normal ~1 m/s) |\n"
        "| **Gradient moyen RA serré** | **≥ 40 mmHg** | ETT |\n"
        "| **Surface RA serré** | **< 1 cm² ou < 0,6 cm²/m²** | ETT |\n"
        "| **Surface RA critique** | **≤ 0,75 cm² ou ≤ 0,4 cm²/m²** | ETT |\n"
        "| Volume éjection (bas débit) | ≤ 35 mL/m² | RA serré à bas gradient |\n"
        "| Vmax RA très serré (asympt.) | **> 5 m/s** | Indication chirurgicale |\n"
        "| FEVG RA asympt. (chirurgie) | **< 55 %** | Indication |\n"
        "| Score Agatston RA serré ♂ | > 2 000 unités | Scanner |\n"
        "| Score Agatston RA serré ♀ | > 1 200 unités | Scanner |\n"
        "| Âge TAVI 1ʳᵉ intention | **> 75 ans** | Voie fémorale possible |\n"
        "| Âge coronarographie préop RA | > 40 ans (♂ + ♀ ménopausée) | Bilan |\n"
        "| Choix bioprothèse RA | > 65 ans | Indication |\n"
        "| Choix prothèse mécanique RA | sujet jeune | Indication |\n"
        "| Durée vie bioprothèse | 10-15 ans | Dégénérescence |\n"
        "| **IM SOR grade IV** | **≥ 40 mm²** | Importante |\n"
        "| IM volume régurgité grade IV | **≥ 60 mL** | Importante |\n"
        "| IM SOR seuil sévérité (secondaire) | ≥ 30 mm² | Sévère |\n"
        "| **IM — DTS VG indication chirurgicale** | **≥ 40 mm** | Asymptomatique |\n"
        "| **IM — FEVG indication chirurgicale** | **≤ 60 %** | Asymptomatique |\n"
        "| **IM — Volume AG indexé** | **≥ 60 mL/m²** | Indication |\n"
        "| **IM — PAP systolique** | **≥ 50 mmHg** | Indication |\n"
        "| FE seuil RVM impossible | **< 30 %** | Traitement médical/greffe |\n"
        "| Cathétérisme : PAPO IM | > 15 mmHg | Post-capillaire |\n"
        "| Annuloplastie tricuspide | Anneau > 40 mm | Apicale 4 cavités |\n"
        "| Choix bioprothèse IM/RVM | > 70 ans | |\n"
        "| Choix prothèse mécanique IM/RVM | < 65 ans | |\n"
        "| Surveillance IM asympt. | 6 mois | ETT |\n"
        "| Bicuspidie + dilatation aortique | ~50 % | Association |\n"
        "| **IA flux télédiastolique isthmique** | **≥ 20 cm/s** | Sévère |\n"
        "| **IA hyperdébit chambre de chasse** | > 4 L/min/m² | Grades 3-4 |\n"
        "| **IA — DTS chirurgicale** | **> 50 mm ou > 25 mm/m²** | Asympt. |\n"
        "| IA — DTS bas risque | > 20 mm/m² | Asympt. |\n"
        "| **IA — FEVG chirurgicale** | **≤ 50 %** | Asympt. |\n"
        "| IA — FEVG (chir. bas risque) | ≤ 55 % | Asympt. |\n"
        "| **IA — Aorte ascendante chirurgie** | **≥ 55 mm** | Toute IA |\n"
        "| IA — Aorte Marfan | ≥ 50 mm | Indication |\n"
        "| IA — Aorte Marfan + FdR | ≥ 45 mm | Indication |\n"
        "| IA — Aorte bicuspidie + FdR | ≥ 50 mm | Indication |\n"
        "| Progression aorte (FdR) | > 3 mm/an | Indication |\n"
        "| Mortalité RVA asympt. | **1-3 %** | Périopératoire |\n"
        "| Mortalité RVA sympt./complexe | **3-10 %** | Périopératoire |\n"
        "| Surveillance IA sévère | 1-2 ×/an | Suivi |\n"
        "| Surveillance IA modérée | 2-3 ans | Suivi |\n"
        "| Récurrence bicuspidie familiale | ~10 % | Dépistage |\n"
        "| Capacité d'effort (critère mauvais) | < 80-85 % théorique | IA |"
    ))

    points_cles = [
        "**RA** : valvulopathie la + fréquente ; **dégénératif > 65 ans**, **bicuspidie 30-65 ans**, RAA migrants",
        "Triade du RA serré : **dyspnée + angor + syncope d'effort** ; apparition = tournant pronostique",
        "RA serré ETT : **Vmax > 4 m/s**, gradient ≥ **40 mmHg**, surface < **1 cm²** ; épreuve d'effort **CI si symptomatique**",
        "**TAVI** : inopérables/haut risque, **1ʳᵉ intention > 75 ans** (voie fémorale possible)",
        "Carpentier IM : **I normal**, **II prolapsus**, **IIIa restrictif** (RAA), **IIIb secondaire**",
        "IM dystrophique (type II) = cause la + fréquente d'IM sévère ; **plastie reconstructrice** = traitement de référence",
        "Chirurgie IM asympt : **DTS ≥ 40 mm**, **FEVG ≤ 60 %**, **PAP ≥ 50 mmHg**, **FA**, AG > 60 mL/m²",
        "IA types : **1** dilatation racine, **2** prolapsus, **3** restrictif (RAA/médicaments)",
        "IA chronique longtemps silencieuse ; chirurgie si **DTS > 50 mm**, **FEVG ≤ 50 %** ou dilatation aortique ≥ 55 mm",
        "**Fièvre + valvulopathie → EI** ; IA aiguë + douleur thoracique sans fièvre → **dissection**",
    ]

    fiche_eclair_md = (
        "**RA** : valvulopathie la + fréquente. Dégénératif > 65 ans, bicuspidie 30-65 ans, RAA. "
        "Triade : dyspnée + angor + syncope d'effort. Souffle mésosystolique 2ᵉ EICD aux carotides.\n\n"
        "**RA serré ETT** : Vmax > 4 m/s, gradient ≥ 40 mmHg, surface < 1 cm². Épreuve d'effort CI "
        "si symptomatique.\n\n"
        "**Traitement RA** : RVA ou TAVI (1ʳᵉ intention > 75 ans). Asympt : Vmax > 5 m/s, FEVG < 55 %. "
        "Mécanique < 65 ans, bio > 65 ans.\n\n"
        "**IM Carpentier** : I normal, II prolapsus (dystrophique = + fréquente), IIIa restrictif (RAA), "
        "IIIb (secondaire).\n\n"
        "**Souffle IM** : holosystolique apexoaxillaire « jet de vapeur ». Prolapsus : clic + télésystolique. "
        "Sévérité : SOR ≥ 40 mm² + volume ≥ 60 mL.\n\n"
        "**Traitement IM** : plastie +++. RVM si plastie impossible et FE > 30 %. Asympt : DTS ≥ 40 mm, "
        "FEVG ≤ 60 %, PAP ≥ 50, FA, AG > 60 mL/m².\n\n"
        "**IA types** : 1 (dilatation racine : Marfan, bicuspidie, EI), 2 (prolapsus), 3 (RAA, "
        "anorexigènes). Aiguë : EI, dissection.\n\n"
        "**Souffle IA** : diastolique foyer aortique, penché en avant expiration bloquée. "
        "Hyperpulsatilité + PA différentielle élargie = IA sévère.\n\n"
        "**Traitement IA** : RVA (Bentall si dilatation). Bêtabloquants CI sauf Marfan. Asympt : "
        "DTS > 50 mm, FEVG ≤ 50 %. Aorte ≥ 55 mm (50 Marfan).\n\n"
        "**3 valvulopathies** : prévention EI, dentaire 2×/an, Heart Team. Antibioprophylaxie seulement "
        "si ATCD EI / prothèse / cyanogène."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 233 - Valvulopathies",
        annee="2025-2026",
        item="Item 233",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 233",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-233_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

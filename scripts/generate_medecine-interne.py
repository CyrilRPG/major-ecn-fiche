"""Génère la fiche Médecine interne."""
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
        PlanPartie(numero="I", titre="Maladies auto-immunes : généralités", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définitions et épidémiologie"),
            PlanSousPartie(lettre="B", titre="Anticorps anti-nucléaires et bilan immunologique"),
            PlanSousPartie(lettre="C", titre="Classification des pathologies auto-immunes"),
        ]),
        PlanPartie(numero="II", titre="Vascularites systémiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et classification de Chapel Hill"),
            PlanSousPartie(lettre="B", titre="Vascularites des gros vaisseaux"),
            PlanSousPartie(lettre="C", titre="Vascularites des vaisseaux de moyen calibre"),
            PlanSousPartie(lettre="D", titre="Vascularites des vaisseaux de petit calibre"),
            PlanSousPartie(lettre="E", titre="Diagnostics différentiels des vascularites"),
        ]),
        PlanPartie(numero="III", titre="Purpura vasculaire", sous_parties=[
            PlanSousPartie(lettre="A", titre="Orientation diagnostique devant un purpura"),
            PlanSousPartie(lettre="B", titre="Bilan de première intention"),
            PlanSousPartie(lettre="C", titre="Vascularite à IgA"),
        ]),
        PlanPartie(numero="IV", titre="Anémie et carence martiale", sous_parties=[
            PlanSousPartie(lettre="A", titre="Classification des anémies"),
            PlanSousPartie(lettre="B", titre="Carence martiale"),
            PlanSousPartie(lettre="C", titre="Maladie coeliaque"),
        ]),
        PlanPartie(numero="V", titre="Thrombopénie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Orientation diagnostique"),
            PlanSousPartie(lettre="B", titre="Thrombopénie immunologique (PTI)"),
        ]),
        PlanPartie(numero="VI", titre="Artérite à cellules géantes et PPR", sous_parties=[
            PlanSousPartie(lettre="A", titre="Phénomène de Raynaud"),
            PlanSousPartie(lettre="B", titre="Pseudo-polyarthrite rhizomélique"),
            PlanSousPartie(lettre="C", titre="Artérite à cellules géantes (Horton)"),
            PlanSousPartie(lettre="D", titre="Corticothérapie au long cours"),
        ]),
        PlanPartie(numero="VII", titre="Sarcoïdose et SAPL", sous_parties=[
            PlanSousPartie(lettre="A", titre="Sarcoïdose"),
            PlanSousPartie(lettre="B", titre="Syndrome des anti-phospholipides"),
        ]),
    ]

    # ── PARTIE I : MALADIES AUTO-IMMUNES : GENERALITES ──
    partie_i = Partie(numero="I", titre="Maladies auto-immunes : généralités", sous_parties=[
        SousPartie(lettre="A", titre="Définitions et épidémiologie", rows=[
            FicheRow(concept="Définitions", detail_md=(
                "- **Auto-immunité** : phénomène physiologique (tolérance du soi)\n"
                "- **Maladie auto-immune (MAI)** : rupture de la tolérance immunitaire\n"
                "- **Prévalence** : 6-7% de la population\n"
                "- 3e comorbidité en fréquence\n"
                "- Associations possibles entre MAI (ex : syndrome de Reynolds, PEAI 1, PEAI 2)"
            )),
            FicheRow(concept="Facteurs favorisants", detail_md=(
                "- **Facteurs génétiques** ++ : association HLA\n"
                "- **Facteurs environnementaux** : virus, médicaments, toxiques\n"
                "- **Facteurs hormonaux** : prédominance féminine pour les connectivites"
            )),
            FicheRow(concept="Évolution", detail_md=(
                "- Évolution par **poussées** entrecoupées de **rémissions**\n"
                "- Diagnostic repose sur une association de critères clinico-biologiques"
            )),
        ]),
        SousPartie(lettre="B", titre="Anticorps anti-nucléaires et bilan immunologique", rows=[
            FicheRow(concept="ANA — Dépistage", detail_md=(
                "- **Technique de référence** : immunofluorescence indirecte (IFI) sur cellules **HEP-2**\n"
                "- Résultat : aspect de fluorescence + titre (dilution)\n"
                "- **Sensible mais non spécifique**\n"
                "- Étape 1 : dépistage par IFI\n"
                "- Étape 2 : détermination de la cible = **ENA** (antigènes nucléaires solubles)\n"
                "- Étape 3 : quantification par **ELISA** (ex : anti-Sm, anti-SSa)"
            )),
            FicheRow(concept="Aspect de fluorescence et spécificités", detail_md=(
                "| Fluorescence | Spécificité anticorps | MAI associée |\n"
                "|-------------|----------------------|-------------|\n"
                "| **Homogène** | Anti-ADNdb, anti-histone | LES |\n"
                "| Homogène renforcement périph. | Anti-ADNdb | LES |\n"
                "| **Moucheté** | Anti-Sm, anti-SSA/SSB, anti-RNP | LES, Gougerot-Sjögren, Sharp |\n"
                "| **Nucléolaire** | Anti-Scl70 | Sclérodermie systémique |\n"
                "| **Centromérique** | Anti-centromère | Sclérodermie cutanée limitée |"
            )),
            FicheRow(concept="Anti-ADN natifs", detail_md=(
                "- Si ANA positifs : quantification des anti-ADNdb\n"
                "- Techniques : test de **Farr**, **Crithidia luciliae**, ELISA\n"
                "- Intérêt dans le suivi thérapeutique du LES"
            )),
            FicheRow(concept="", detail_md=(
                "- Les ANA sont un **test de dépistage** (sensible, peu spécifique)\n"
                "- Un titre positif impose la recherche de la **cible antigénique** (ENA)\n"
                "- Une fluorescence homogène est compatible avec la présence d'anti-ADN natifs"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Classification des pathologies auto-immunes", rows=[
            FicheRow(concept="Connectivites", detail_md=(
                "- **Lupus érythémateux systémique** (LES)\n"
                "- **Syndrome de Gougerot-Sjögren**\n"
                "- **Sclérodermie systémique**\n"
                "- **Connectivite mixte** (syndrome de Sharp)\n"
                "- Syndrome des anti-phospholipides (SAPL)"
            )),
            FicheRow(concept="Vascularites", detail_md=(
                "| Calibre | Pathologies |\n"
                "|---------|------------|\n"
                "| **Gros** | Artérite à cellules géantes (Horton), Maladie de Takayasu |\n"
                "| **Moyen** | Périartérite noueuse (PAN), Maladie de Kawasaki |\n"
                "| **Petit** — pauci-immune (ANCA) | GPA, GEPA, MPA |\n"
                "| **Petit** — complexes immuns | Vascularite à IgA, Cryoglobulinémie |"
            )),
            FicheRow(concept="◆ Autres auto-anticorps", detail_md=(
                "| Anticorps | Technique | Pathologie |\n"
                "|-----------|-----------|------------|\n"
                "| Anti-phospholipides (ACL, ACC, anti-B2GP1) | ELISA, coagulation | SAPL |\n"
                "| Facteur rhumatoïde | Test LATEX | PR (30-80%), GS (30-80%), peu spécifique |\n"
                "| Anti-CCP | ELISA | PR (spécifique) |\n"
                "| Anti-M2 | IFI | Cirrhose biliaire primitive |\n"
                "| Anti-muscle lisse | IFI | Hépatite auto-immune type 1 |\n"
                "| Anti-LKM1 | IFI | Hépatite auto-immune type 2 |"
            )),
        ]),
    ])

    # ── PARTIE II : VASCULARITES SYSTEMIQUES ──
    partie_ii = Partie(numero="II", titre="Vascularites systémiques", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et classification de Chapel Hill", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Vascularite** : atteinte inflammatoire des vaisseaux sanguins "
                "(artériels, capillaires ou veineux) responsable d'une modification pariétale\n"
                "- Classification selon le **calibre des vaisseaux** atteints (Chapel Hill)"
            )),
            FicheRow(concept="Manifestations aspécifiques", detail_md=(
                "- **AEG** : anorexie, amaigrissement, asthénie\n"
                "- Fièvre / hyperthermie\n"
                "- Arthromyalgies\n"
                "- Syndrome inflammatoire biologique"
            )),
            FicheRow(concept="Manifestations spécifiques (petit calibre)", detail_md=(
                "- **Purpura vasculaire** +/- PAN\n"
                "- **Néphropathie** (glomérulaire/vasculaire)\n"
                "- **Neuropathie périphérique** (mononévrite multiple +++)\n"
                "- **Hémorragie intra-alvéolaire**\n"
                "- Ischémie digestive"
            )),
            FicheRow(concept="", detail_md=(
                "- Le purpura vasculaire est **infiltré, déclive, polymorphe**, épargne les muqueuses\n"
                "- La mononévrite multiple est le signe neurologique le plus fréquent des vascularites de petit calibre"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Vascularites des gros vaisseaux", rows=[
            FicheRow(concept="Artérite à cellules géantes (Horton)", detail_md=(
                "- **Terrain** : femme, > 50 ans\n"
                "- **Tropisme** : ophtalmologique et vertébro-basilaire\n"
                "- Clinique :\n"
                "  - Fièvre, AEG, arthromyalgies (PPR associée)\n"
                "  - **Céphalées temporales pulsatiles**\n"
                "  - **Claudication de la mâchoire**\n"
                "  - Hyperesthésie cuir chevelu (signe du peigne, oreiller, chapeau)\n"
                "  - **BAV dans 30%** : NOIAA / OACR / NOIP\n"
                "  - Toux quinteuse, claudication des membres supérieurs\n"
                "  - Absence de pouls temporal, anisotension, souffle vasculaire\n"
                "  - AVC, douleur thoracique inflammatoire"
            )),
            FicheRow(concept="Paraclinique ACG", detail_md=(
                "- **Biologie** : syndrome inflammatoire (pas de marqueur spécifique), "
                "cholestase fréquente, anémie et thrombocytose inflammatoire\n"
                "- **Imagerie** : angioscanner TAP injecté, TEP-scanner, EDTSA\n"
                "- **Histologie** : biopsie d'artère temporale (examen de référence)"
            )),
            FicheRow(concept="Traitement ACG", detail_md=(
                "- **Corticothérapie d'attaque** pendant 4 semaines : **0,5-0,7 mg/kg/j**\n"
                "- Si atteinte ophtalmologique : **bolus IV** puis relais **1 mg/kg/j**\n"
                "- Décroissance progressive sur **18 mois**\n"
                "- **50% de rechute** : discuter épargne cortisonique par MTX ou tocilizumab (TCZ)\n"
                "- Anti-agrégant plaquettaire à discuter\n"
                "- Pronostic : équivalent à population générale, risque principal = **visuel**"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant toute **BAV brutale indolore** avec syndrome inflammatoire chez sujet > 50 ans, "
                "évoquer systématiquement l'artérite à cellules géantes\n"
                "- La corticothérapie doit être débutée **avant** la biopsie d'artère temporale"
            ), kind="piege"),
            FicheRow(concept="Maladie de Takayasu", detail_md=(
                "- **Terrain** : femme +++ < 40 ans\n"
                "- **Tropisme** : arc aortique, artères des membres, atteinte pulmonaire ++++\n"
                "- Clinique : début insidieux, claudications et souffles vasculaires au 1er plan, "
                "absence de pouls périphériques, anisotension, HTA réno-vasculaire, AVC\n"
                "- Paraclinique : sténose/anévrysme au TAP injecté, TEP avec hypermétabolisme\n"
                "- Syndrome inflammatoire souvent absent ou discret"
            )),
        ]),
        SousPartie(lettre="C", titre="Vascularites des vaisseaux de moyen calibre", rows=[
            FicheRow(concept="Périartérite noueuse (PAN)", detail_md=(
                "- **Terrain** : H > F, 30-50 ans\n"
                "- **Tropisme** : artère rénale ++, **jamais les artères pulmonaires**\n"
                "- Clinique :\n"
                "  - Fièvre > 5 jours, AEG, arthromyalgies\n"
                "  - **HTA réno-vasculaire**\n"
                "  - Purpura vasculaire (25%), polyneuropathie/mononévrite (30%)\n"
                "  - **Orchite**\n"
                "  - Infarctus rénaux, ischémie mésentérique\n"
                "- Biologie : syndrome inflammatoire, éosinophilie possible, "
                "**négativité des marqueurs d'auto-immunité**\n"
                "- Association fréquente : **VHB**"
            )),
            FicheRow(concept="Maladie de Kawasaki", detail_md=(
                "- **Terrain** : enfant < 5 ans\n"
                "- **Tropisme** : **coronaire**\n"
                "- Critères diagnostiques : fièvre > 5 jours + **5 critères** :\n"
                "  - Chéilite\n"
                "  - Conjonctivite\n"
                "  - Érythro-oedème des mains\n"
                "  - Éruption cutanée diffuse (rash scarlatiniforme)\n"
                "  - Adénopathie de taille significative\n"
                "- Autres : cholestase, épaississement vésicule biliaire, "
                "réactivation cicatrice BCG\n"
                "- Complication : **anévrysme coronaire**"
            )),
            FicheRow(concept="◆ Traitement Kawasaki", detail_md=(
                "- **IgIV** + **aspirine** à dose anti-inflammatoire\n"
                "- Surveillance des coronaires par ETT à **J2, S2, M2**"
            )),
            FicheRow(concept="", detail_md=(
                "- La PAN n'atteint **jamais** les artères pulmonaires\n"
                "- Toujours rechercher une **sérologie VHB** devant une PAN\n"
                "- Dans le Kawasaki, le risque principal est l'**anévrysme coronaire**"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Vascularites des vaisseaux de petit calibre", rows=[
            FicheRow(concept="Vascularites à ANCA", detail_md=(
                "- Vascularites **nécrosantes** sur les analyses histologiques\n"
                "- Clinique commune :\n"
                "  - AEG, fièvre, arthromyalgies\n"
                "  - Purpura vasculaire, ulcères, nécroses cutanées\n"
                "  - **Mononévrite multiple** +++\n"
                "  - Néphropathie glomérulaire (GNRP)\n"
                "  - Hémorragie intra-alvéolaire"
            )),
            FicheRow(concept="GPA, GEPA, MPA — Comparaison", detail_md=(
                "| | GPA | GEPA | MPA |\n"
                "|--|-----|------|-----|\n"
                "| ORL | **Sinusite crouteuse nécrosante** | Polypose nasale | 0 |\n"
                "| Poumon | **Nodules excavés** | Infiltrat éosinophilique, asthme tardif | Hémorragie IA |\n"
                "| Coeur | - | Fibrose endomyocardique | - |\n"
                "| Rein | GNRP | GNRP | **GNRP** |\n"
                "| ANCA | **C-ANCA** (anti-PR3) | P-ANCA +/- (anti-MPO) | **P-ANCA** (anti-MPO) |\n"
                "| Spécificité | Rhinite crouteuse + nodules excavés | Asthme + éosinophilie | IRRA + P-ANCA |"
            )),
            FicheRow(concept="", detail_md=(
                "- GPA = atteinte **ORL** (rhinite crouteuse nécrosante) + **nodules pulmonaires excavés** + C-ANCA anti-PR3\n"
                "- GEPA = **asthme tardif** + éosinophilie + P-ANCA anti-MPO\n"
                "- MPA = GNRP + hémorragie IA + P-ANCA anti-MPO"
            ), kind="a_retenir"),
            FicheRow(concept="Vascularites à dépôts de complexes immuns", detail_md=(
                "- **Vascularite à IgA** : purpura, atteinte digestive, orchite, "
                "néphropathie à IgA, CRP pas forcément élevée\n"
                "- **Cryoglobulinémie** : purpura ++++, Raynaud +++, ulcères, "
                "complément consommé (types 1/2/3)\n"
                "- **Vascularite urticarienne** : urticaire fixé peu prurigineux, "
                "douleurs abdominales, hypocomplémentémie"
            )),
        ]),
        SousPartie(lettre="E", titre="Diagnostics différentiels des vascularites", rows=[
            FicheRow(concept="◆ Vascularites secondaires", detail_md=(
                "- **MAI** : polyarthrite rhumatoïde, lupus érythémateux systémique\n"
                "- **Infections** :\n"
                "  - VHC : cryoglobulinémie\n"
                "  - VHB : périartérite noueuse\n"
                "  - Endocardite infectieuse : vascularite petit calibre\n"
                "  - Syphilis, tuberculose : vascularite gros calibre\n"
                "  - VIH : vascularite de tous les calibres\n"
                "- **Autres** : maladie des embols de cristaux de cholestérol"
            )),
            FicheRow(concept="Bilan étiologique", detail_md=(
                "- Sérologies VIH, VHB, VHC\n"
                "- Imagerie orientée selon le calibre\n"
                "- Preuve histologique à tenter +++ (biopsie cutanée, PBR, biopsie ORL, "
                "biopsie digestive, biopsie neuromusculaire)"
            )),
            FicheRow(concept="◆ Traitement des vascularites", detail_md=(
                "- **Corticothérapie**\n"
                "- **Immunosuppresseurs** (cyclophosphamide, azathioprine)\n"
                "- **Biothérapie** (rituximab, tocilizumab)\n"
                "- IgIV (Kawasaki)\n"
                "- Revascularisation si nécessaire"
            )),
            FicheRow(concept="Facteurs de mauvais pronostic", detail_md=(
                "- Atteinte **cardiaque**\n"
                "- Atteinte **rénale**\n"
                "- Atteinte **digestive**\n"
                "- Atteinte **neurologique centrale**"
            )),
        ]),
    ])

    # ── PARTIE III : PURPURA VASCULAIRE ──
    partie_iii = Partie(numero="III", titre="Purpura vasculaire", sous_parties=[
        SousPartie(lettre="A", titre="Orientation diagnostique devant un purpura", rows=[
            FicheRow(concept="Urgences à éliminer", detail_md=(
                "| Urgence | Caractéristiques |\n"
                "|---------|------------------|\n"
                "| **Purpura fulminans** | Instabilité hémodynamique, extension rapide, nécrose, tableau méningé |\n"
                "| **Purpura hémorragique thrombopénique** | Étendu, cutanéo-muqueux, pétéchies/ecchymoses, plaquettes < 30 000/mm3 |"
            )),
            FicheRow(concept="Purpura vasculaire vs thrombopénique", detail_md=(
                "| Critère | Vasculaire | Thrombopénique |\n"
                "|---------|-----------|----------------|\n"
                "| Relief | **Infiltré** | Écchymotique et pétéchial |\n"
                "| Localisation | **Déclive** | Diffus |\n"
                "| Aspect | **Polymorphe** | Pétéchial et écchymotique |\n"
                "| Muqueuses | **Épargnées** | Atteintes |"
            )),
        ]),
        SousPartie(lettre="B", titre="Bilan de première intention", rows=[
            FicheRow(concept="Recherche de retentissement", detail_md=(
                "- **Atteinte rénale** : créatinine, urée, ionogramme sanguin, "
                "protéinurie, créatininurie, BU\n"
                "- **Atteinte pulmonaire** (hémorragie IA) : hémogramme, hémostase\n"
                "- **Atteinte cutanée** : biopsie cutanée\n"
                "- Recherche d'atteinte nerveuse et digestive"
            )),
            FicheRow(concept="Bilan étiologique spécifique", detail_md=(
                "| Étiologie recherchée | Examen |\n"
                "|---------------------|--------|\n"
                "| Vascularite à ANCA | **ANCA** |\n"
                "| Vascularite rhumatoïde | FR, anti-CCP |\n"
                "| Cryoglobulinémie | C3, C4, **CH50**, cryoglobulinémie |\n"
                "| Lupus | **ANA** |\n"
                "| Vascularite à IgA | Dosage pondéral des Ig, EPS |\n"
                "| Endocardite infectieuse | **Hémocultures**, FR, complément |\n"
                "| Hémostase | TP, TCA, fibrinogène, schizocytes |"
            )),
        ]),
        SousPartie(lettre="C", titre="Vascularite à IgA (purpura rhumatoïde)", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Terrain : **enfant** (plus rare chez l'adulte)\n"
                "- Souvent après épisode infectieux\n"
                "- Synonymes : purpura rhumatoïde, purpura d'Henoch-Schönlein"
            )),
            FicheRow(concept="Triade clinique", detail_md=(
                "- **Purpura vasculaire**\n"
                "- **Polyarthrite ou polyarthralgies**\n"
                "- **Douleurs abdominales**"
            )),
            FicheRow(concept="Diagnostic", detail_md=(
                "- Triade clinique\n"
                "- **Dépôts d'IgA** en immunohistochimie (biopsie cutanée)\n"
                "- Élévation des taux d'IgA (inconstant, 50% des cas)\n"
                "- CRP pas forcément élevée"
            )),
            FicheRow(concept="Éléments de gravité", detail_md=(
                "- **Néphropathie** (mésangiale ou proliférative) à dépôts d'IgA\n"
                "- **Atteinte digestive**"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Repos** +++ et **colchicine**\n"
                "- Bandes de contention + surélévation des membres\n"
                "- Surveillance biologique mensuelle\n"
                "- Formes graves : corticothérapie, cyclophosphamide\n"
                "- Évolution par poussées successives (adulte)"
            )),
        ]),
    ])

    # ── PARTIE IV : ANEMIE ET CARENCE MARTIALE ──
    partie_iv = Partie(numero="IV", titre="Anémie et carence martiale", sous_parties=[
        SousPartie(lettre="A", titre="Classification des anémies", rows=[
            FicheRow(concept="Anémie microcytaire", detail_md=(
                "- **Définition** : Hb < 12 g/dL (femme) ou < 13 g/dL (homme), VGM < 80 fL\n"
                "- 2 étiologies principales :\n"
                "  - **Carence martiale** (ferritine basse)\n"
                "  - **Syndrome inflammatoire prolongé** (ferritine normale/haute, CRP élevée)\n"
                "- Bilan de 1re intention : **ferritine** + **CRP**\n"
                "- Autres causes : carence en B6, hémoglobinopathie, ARSI"
            )),
            FicheRow(concept="Anémie normo-macrocytaire arégénérative", detail_md=(
                "- Insuffisance rénale chronique\n"
                "- Insuffisance hépatocellulaire\n"
                "- Carence vitaminique B9/B12\n"
                "- Toxicité médullaire (médicaments, alcool)\n"
                "- Dysfonction médullaire : myélome, leucémie, syndrome myélodysplasique"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant une anémie microcytaire, les 2 diagnostics principaux sont la **carence martiale** "
                "et le **syndrome inflammatoire** : le bilan minimal comporte **ferritine** + **CRP**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Carence martiale", rows=[
            FicheRow(concept="Syndrome anémique", detail_md=(
                "- Pâleur cutanéo-muqueuse généralisée\n"
                "- Asthénie généralisée, céphalées\n"
                "- Dyspnée d'effort puis de repos\n"
                "- Angor d'effort puis de repos\n"
                "- Symptômes neurologiques aspécifiques\n"
                "- Souffle systolique aspécifique"
            )),
            FicheRow(concept="◆ Syndrome carentiel", detail_md=(
                "- **Perlèches**, glossite\n"
                "- **Koilonychies** (ongles concaves)\n"
                "- Alopécie, dysgueusie\n"
                "- Dysphagie : syndrome de **Plummer-Vinson** (ou Kelly-Patterson)"
            )),
            FicheRow(concept="Étiologies de la carence martiale", detail_md=(
                "| Mécanisme | Causes |\n"
                "|-----------|--------|\n"
                "| **Carence d'apport** | Régime végétarien, restrictif, psychiatrique |\n"
                "| **Défaut d'absorption** | MICI (Crohn, RCH), **maladie coeliaque** |\n"
                "| **Augmentation des besoins** | Grossesse, adolescence |\n"
                "| **Augmentation des pertes** | Pertes digestives, pertes gynécologiques |"
            )),
        ]),
        SousPartie(lettre="C", titre="Maladie coeliaque", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Maladie inflammatoire intestinale caractérisée par une réaction "
                "immunomédiée contre des composants du **gluten** (blé, seigle, orge)\n"
                "- Anticorps : **anti-transglutaminase**, **anti-endomysium**"
            )),
            FicheRow(concept="Terrain et clinique", detail_md=(
                "- Terrain : femme, jeune\n"
                "- Clinique : AEG, diarrhée chronique, ballonnements\n"
                "- Biologie : carence en **fer**, carence en **vitamine D**, carence en **B9**, "
                "**hypocalcémie**\n"
                "- Syndrome de malabsorption malgré un régime varié"
            )),
            FicheRow(concept="", detail_md=(
                "- Évoquer la maladie coeliaque devant une carence martiale par malabsorption "
                "chez un sujet jeune avec diarrhée chronique et carences multiples (fer, B9, vitamine D, calcium)"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE V : THROMBOPENIE ──
    partie_v = Partie(numero="V", titre="Thrombopénie", sous_parties=[
        SousPartie(lettre="A", titre="Orientation diagnostique", rows=[
            FicheRow(concept="Clinique", detail_md=(
                "- Syndrome hémorragique cutanéo-muqueux :\n"
                "  - Ecchymoses, macules purpuriques\n"
                "  - **Bulles hémorragiques endobuccales**\n"
                "  - Saignements de nez (épistaxis)\n"
                "- 1er diagnostic à évoquer devant syndrome hémorragique isolé : **leucémie aiguë**"
            )),
            FicheRow(concept="Bilan de 1re intention", detail_md=(
                "- **NFS, frottis sanguin**\n"
                "- Hémostase : TP, TCA, fibrinogène\n"
                "- Fonction rénale : créatinine, urée, ionogramme\n"
                "- Fonction hépatique"
            )),
            FicheRow(concept="Mécanismes de thrombopénie isolée", detail_md=(
                "| Mécanisme | Étiologies |\n"
                "|-----------|------------|\n"
                "| **Central** | Syndrome myélodysplasique |\n"
                "| **Périphérique — destruction** | PTI, infection virale |\n"
                "| **Périphérique — consommation** | CIVD, microangiopathie thrombotique |\n"
                "| **Séquestration** | Hypersplénisme |"
            )),
        ]),
        SousPartie(lettre="B", titre="Thrombopénie immunologique (PTI)", rows=[
            FicheRow(concept="Bilan diagnostique du PTI", detail_md=(
                "- NFS\n"
                "- Hémostase (éliminer une CIVD)\n"
                "- **ANA** : éliminer un lupus sous-jacent\n"
                "- **Bilan thyroïdien** : dysthyroïdie spécifiquement associée au PTI\n"
                "- **EPS** (électrophorèse des protéines sériques) : éliminer un DICV associé"
            )),
            FicheRow(concept="Indications du myélogramme", detail_md=(
                "- Âge **< 18 ans** ou **> 65 ans**\n"
                "- Autre cytopénie associée\n"
                "- Syndrome tumoral clinique\n"
                "- Résistance au traitement de 1re intention"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Corticothérapie en cures courtes** en 1re intention\n"
                "- Formes sévères : IgIV\n"
                "- Formes réfractaires : splénectomie, agonistes TPO, rituximab"
            )),
            FicheRow(concept="", detail_md=(
                "- Le myélogramme est **obligatoire** si âge > 65 ans, autre cytopénie, "
                "syndrome tumoral ou résistance au traitement\n"
                "- Ne pas oublier de rechercher un **lupus** (ANA) et une **dysthyroïdie** devant un PTI"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE VI : ACG, PPR, RAYNAUD, CORTICOTHERAPIE ──
    partie_vi = Partie(numero="VI", titre="Artérite à cellules géantes et PPR", sous_parties=[
        SousPartie(lettre="A", titre="Phénomène de Raynaud", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Acrosyndrome paroxystique** le plus fréquent en population générale (10%)\n"
                "- Trois phases successives :\n"
                "  - **Phase syncopale** (pathognomonique) : doigts exsangues, froids, "
                "anesthésiés, aspect de doigts morts, durée ~20 min\n"
                "  - **Phase cyanique** : doigts bleutés, cyanosés, stase veineuse\n"
                "  - **Phase érythémateuse** : érythème, douleur"
            )),
            FicheRow(concept="Signes d'atypie (Raynaud secondaire)", detail_md=(
                "- Âge tardif (> 35-40 ans)\n"
                "- Asymétrie, atteinte des pouces\n"
                "- Persistance, complications trophiques\n"
                "- Sexe masculin\n"
                "- Absence d'antécédents familiaux"
            )),
            FicheRow(concept="◆ Examens complémentaires", detail_md=(
                "- Indiqués si atypie clinique ou âge > 35-40 ans\n"
                "- **ANA** et **capillaroscopie** en 1re intention\n"
                "- EDAMS si atteinte asymétrique ou FDR cardiovasculaire majeur"
            )),
            FicheRow(concept="Diagnostics différentiels", detail_md=(
                "- **Acrorhigose** : doigts suintants\n"
                "- **Acrocyanose** : persistance\n"
                "- **Érythermalgie** : opposé (chaleur, rougeur)"
            )),
            FicheRow(concept="", detail_md=(
                "- Les **bêta-bloquants** et les **triptans** sont des facteurs déclenchants classiques du Raynaud\n"
                "- L'atteinte du pouce est un signe d'alarme vers un Raynaud secondaire"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Pseudo-polyarthrite rhizomélique (PPR)", rows=[
            FicheRow(concept="Clinique", detail_md=(
                "- Rhumatisme inflammatoire des **ceintures** (épaules +++, hanches)\n"
                "- Terrain : > 50 ans\n"
                "- AEG + arthromyalgies des ceintures avec raideur matinale invalidante\n"
                "- Syndrome inflammatoire biologique (VS/CRP élevées)\n"
                "- CPK normales (pas de myolyse)\n"
                "- Échographie : **bursite sous-acromio-deltoïdienne bilatérale**"
            )),
            FicheRow(concept="Biologie", detail_md=(
                "- Anémie microcytaire inflammatoire\n"
                "- Thrombocytose inflammatoire\n"
                "- VS élevée, CRP élevée\n"
                "- **CPK normales** (diagnostic différentiel avec myosite)"
            )),
            FicheRow(concept="◆ Diagnostic différentiel", detail_md=(
                "- **Polyarthrite rhumatoïde** : diagnostic différentiel principal\n"
                "- Arguments en faveur de PPR : âge, atteinte rhizomélique, AEG associée, "
                "syndrome inflammatoire biologique\n"
                "- Association fréquente PPR et ACG"
            )),
            FicheRow(concept="Traitement PPR", detail_md=(
                "- **Corticothérapie** : 0,2-0,35 mg/kg/j (très corticosensible)\n"
                "- Traitement quotidien au long terme\n"
                "- Décroissance progressive"
            )),
            FicheRow(concept="", detail_md=(
                "- Évoquer une **PPR** devant des douleurs inflammatoires bilatérales des ceintures "
                "chez un sujet > 50 ans avec syndrome inflammatoire et CPK normales\n"
                "- Toujours rechercher une **ACG associée** (céphalées, BAV, claudication mâchoire)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Artérite à cellules géantes — Complications ophtalmologiques", rows=[
            FicheRow(concept="NOIAA", detail_md=(
                "- **Neuropathie optique ischémique antérieure aiguë**\n"
                "- BAV brutale, oeil blanc et indolore\n"
                "- Principale complication ophtalmologique de l'ACG\n"
                "- Rechercher systématiquement un syndrome inflammatoire biologique"
            )),
            FicheRow(concept="OACR", detail_md=(
                "- **Occlusion de l'artère centrale de la rétine**\n"
                "- Oeil blanc et indolore, amaurose transitoire, cécité brutale\n"
                "- Réflexe photomoteur aboli\n"
                "- FO : oedème rétinien, artères grêles, **cerise maculaire**, rétine pâle\n"
                "- Étiologies : embolie (athérome, cardiopathie), ACG, Takayasu, SAPL, vascularite à ANCA"
            )),
            FicheRow(concept="◆ PEC OACR", detail_md=(
                "- Bilan : ETT + ETO + EDTSA +/- angioscanner\n"
                "- Traitement : hypotonisant (acétazolamide), vasodilatation, fibrinolyse si très précoce\n"
                "- Par ailleurs : AAP + statines (prise en charge AVC-like)\n"
                "- Pronostic défavorable, régression oedème rétinien en 1 mois"
            )),
            FicheRow(concept="BAV — Orientation diagnostique", detail_md=(
                "| Oeil | Douleur | Pathologies |\n"
                "|------|---------|------------|\n"
                "| **Blanc** | **Indolore** | NOIAA, OVCR, OACR/OBACR, NOIP/NORB |\n"
                "| **Rouge** | **Douloureux** | GAFA, kératite, uvéite antérieure |\n"
                "| **Rouge** | **Indolore** | Hémorragie intravitréenne |"
            )),
        ]),
        SousPartie(lettre="D", titre="Corticothérapie au long cours", rows=[
            FicheRow(concept="Mesures associées", detail_md=(
                "- Prise quotidienne, au long terme\n"
                "- Conseils hygiéno-diététiques :\n"
                "  - Apports caloriques : 35-40 kcal/kg/j\n"
                "  - Apports protidiques : 1-1,5 g/kg/j\n"
                "  - Limiter sucres rapides, graisses saturées, **sel < 6 g/j**\n"
                "  - Activité physique à poursuivre"
            )),
            FicheRow(concept="Prévention ostéoporose cortisonique", detail_md=(
                "- Indications systématiques : **âge > 50 ans** ou ménopause, "
                "> 7,5 mg/j d'équivalent prednisone pendant > 3 mois\n"
                "- Mesures :\n"
                "  - Activité physique régulière\n"
                "  - Supplémentation vitaminocalcique si apports insuffisants\n"
                "  - **Bisphosphonates** (anti-résorptif)"
            )),
            FicheRow(concept="Complications du sevrage", detail_md=(
                "- Rechute de la maladie de fond\n"
                "- Infection intercurrente sous corticoïdes\n"
                "- **Insuffisance surrénalienne aiguë** si arrêt brutal : douleurs abdominales, "
                "nausées, vomissements, hypotension, tachycardie, hyponatrémie, hyperkaliémie"
            )),
            FicheRow(concept="", detail_md=(
                "- L'arrêt brutal d'une corticothérapie prolongée peut provoquer une **insuffisance "
                "surrénalienne aiguë** : urgence vitale\n"
                "- L'hyponatrémie + l'hyperkaliémie sont les anomalies ioniques caractéristiques"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE VII : SARCOIDOSE ET SAPL ──
    partie_vii = Partie(numero="VII", titre="Sarcoïdose et SAPL", sous_parties=[
        SousPartie(lettre="A", titre="Sarcoïdose", rows=[
            FicheRow(concept="Syndrome de Löfgren", detail_md=(
                "- **Érythème noueux** + arthralgies des chevilles + "
                "**adénomégalies bilatérales et péri-hilaires** à la radiographie\n"
                "- Forme aiguë de sarcoïdose de bon pronostic"
            )),
            FicheRow(concept="Biologie compatible", detail_md=(
                "- **Anergie tuberculinique** (IDR négative)\n"
                "- **Hypergammaglobulinémie polyclonale**\n"
                "- **Hypercalcémie**\n"
                "- Élévation de l'**ECA** (enzyme de conversion de l'angiotensine)\n"
                "- Lymphopénie possible"
            )),
            FicheRow(concept="Preuve histologique", detail_md=(
                "- **Granulome épithélioïde et gigantocellulaire** sans nécrose caséeuse\n"
                "- Sites de biopsie : biopsie cutanée, biopsie de glandes salivaires accessoires, "
                "**biopsie transbronchique**"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- Syndrome de Löfgren : surveillance (évolution souvent favorable)\n"
                "- Formes évolutives : **corticothérapie** (0,5 mg/kg)\n"
                "- Mesures associées : mise à jour calendrier vaccinal, régime adapté (pauvre en sel et sucres rapides)"
            )),
            FicheRow(concept="", detail_md=(
                "- Le syndrome de Löfgren (érythème noueux + arthralgies chevilles + ADP hilaires bilatérales) "
                "est **quasi pathognomonique** de la sarcoïdose\n"
                "- Ne pas confondre l'anergie tuberculinique de la sarcoïdose avec une tuberculose"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Syndrome des anti-phospholipides (SAPL)", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Prédominance féminine (4/1), associé à 20% des LES\n"
                "- Association de :\n"
                "  - Manifestations **thrombo-emboliques** artérielles ou veineuses\n"
                "  - Et/ou manifestations **gynéco-obstétricales**\n"
                "  - Avec **anticorps anti-phospholipides** positifs à 2 reprises à 12 semaines d'intervalle"
            )),
            FicheRow(concept="Critères obstétricaux", detail_md=(
                "- 3 fausses couches spontanées précoces (FCSP) consécutives et inexpliquées < 10 SA\n"
                "- 1 naissance prématurée (foetus normal) ou pré-éclampsie/éclampsie "
                "ou insuffisance placentaire\n"
                "- 1 mort foetale inexpliquée > 10 SA à foetus normal"
            )),
            FicheRow(concept="Manifestations cliniques", detail_md=(
                "- AVC, thrombophlébite cérébrale, myélopathie vasculaire\n"
                "- Endocardite de Libman-Sacks\n"
                "- OVCR, OACR, OBACR, NOIAA\n"
                "- IDM, ischémie aiguë de membre, ischémie mésentérique\n"
                "- Budd-Chiari, thrombose portale, EP, TVP\n"
                "- Insuffisance rénale, MAT\n"
                "- Livedo, ulcères cutanés, hémorragies sous-unguéales"
            )),
            FicheRow(concept="Anticorps anti-phospholipides", detail_md=(
                "- **Anti-B2GP1**\n"
                "- **Anticardiolipine** (ACL)\n"
                "- **Anticoagulant circulant lupique** (ACC/APT)\n"
                "- Positifs à **2 reprises** à 12 semaines d'intervalle"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Anticoagulation curative** au long terme par **AVK** (INR 2-3)\n"
                "- Formes obstétricales : **aspirine** en prévention"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHESE ──
    tableaux = [
        TableauSynthese(titre="Classification de Chapel Hill — Vascularites", markdown=(
            "| Calibre | Pathologie | Terrain | Tropisme | ANCA |\n"
            "|---------|-----------|---------|----------|------|\n"
            "| Gros | ACG (Horton) | F > 50 ans | Ophtalmo, vertébro-basilaire | - |\n"
            "| Gros | Takayasu | F < 40 ans | Arc aortique, membres, poumon | - |\n"
            "| Moyen | PAN | H, 30-50 ans | Rein (jamais poumon) | - |\n"
            "| Moyen | Kawasaki | Enfant < 5 ans | Coronaire | - |\n"
            "| Petit (ANCA) | GPA | H = F | ORL, poumon (nodules), rein | C-ANCA anti-PR3 |\n"
            "| Petit (ANCA) | GEPA | H = F | Asthme, poumon, coeur | P-ANCA anti-MPO |\n"
            "| Petit (ANCA) | MPA | H = F | Rein, poumon | P-ANCA anti-MPO |\n"
            "| Petit (CI) | Vasc. IgA | Enfant | Peau, digestif, rein | - |\n"
            "| Petit (CI) | Cryoglobulinémie | VHC | Peau, Raynaud, rein | - |"
        )),
        TableauSynthese(titre="ANA — Fluorescence et orientations diagnostiques", markdown=(
            "| Fluorescence | Anticorps | Pathologie |\n"
            "|-------------|-----------|------------|\n"
            "| Homogène | Anti-ADNdb, anti-histone | LES |\n"
            "| Moucheté | Anti-Sm, anti-SSA/SSB, anti-RNP | LES, Gougerot-Sjögren, Sharp |\n"
            "| Nucléolaire | Anti-Scl70 | Sclérodermie systémique |\n"
            "| Centromérique | Anti-centromère | Sclérodermie cutanée limitée |"
        )),
        TableauSynthese(titre="Vascularites à ANCA — Comparaison GPA/GEPA/MPA", markdown=(
            "| Critère | GPA | GEPA | MPA |\n"
            "|---------|-----|------|-----|\n"
            "| Atteinte ORL | Sinusite crouteuse nécrosante | Polypose nasale | Non |\n"
            "| Poumon | Nodules excavés | Infiltrat éosinophilique, asthme | Hémorragie IA |\n"
            "| Spécificité | C-ANCA anti-PR3 | P-ANCA anti-MPO | P-ANCA anti-MPO |\n"
            "| Éosinophilie | Non | Oui +++ | Non |\n"
            "| Rein | GNRP | GNRP | GNRP |"
        )),
        TableauSynthese(titre="Purpura — Vasculaire vs Thrombopénique", markdown=(
            "| Critère | Vasculaire | Thrombopénique |\n"
            "|---------|-----------|----------------|\n"
            "| Relief | Infiltré | Plat |\n"
            "| Localisation | Déclive | Diffus |\n"
            "| Polymorphisme | Oui | Non |\n"
            "| Muqueuses | Épargnées | Atteintes |\n"
            "| Thrombopénie | Non | Oui |"
        )),
        TableauSynthese(titre="Étiologies de la carence martiale", markdown=(
            "| Mécanisme | Étiologies |\n"
            "|-----------|------------|\n"
            "| Carence d'apport | Régime végétarien, restrictif, psychiatrique |\n"
            "| Défaut d'absorption | Maladie coeliaque, MICI |\n"
            "| Augmentation des besoins | Grossesse, adolescence |\n"
            "| Augmentation des pertes | Pertes digestives, gynécologiques |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| MAI | **6-7%** de la population | 3e comorbidité |\n"
        "| ACG — corticothérapie | **0,5-0,7 mg/kg/j** | Attaque 4 semaines |\n"
        "| ACG — bolus ophtalmo | **1 mg/kg/j** | Si atteinte visuelle |\n"
        "| ACG — sevrage CTC | **18 mois** | Décroissance progressive |\n"
        "| ACG — rechute | **50%** | MTX ou TCZ en épargne |\n"
        "| PPR — corticothérapie | **0,2-0,35 mg/kg/j** | Très corticosensible |\n"
        "| Kawasaki — fièvre | > **5 jours** | Critère diagnostique |\n"
        "| Kawasaki — surveillance | **J2, S2, M2** | ETT coronaire |\n"
        "| PTI — myélogramme | Âge **< 18** ou **> 65** ans | Indication formelle |\n"
        "| Thrombopénie hémorragique | < **30 000/mm3** | Seuil plaquettaire |\n"
        "| BAV — ACG | **30%** des ACG | NOIAA, OACR, NOIP |\n"
        "| SAPL — contrôle APL | **12 semaines** | 2 prélèvements positifs |\n"
        "| Ostéoporose cortisonique | > **7,5 mg/j** pendant > 3 mois | Seuil prévention |\n"
        "| Sel sous CTC | < **6 g/j** | Régime hyposodé |"
    ))

    points_cles = [
        "Les ANA se dépistent par **IFI sur cellules HEP-2** (sensible, non spécifique) ; la cible est déterminée par ENA puis ELISA",
        "Les vascularites se classent par **calibre des vaisseaux** atteints (Chapel Hill) : gros, moyen, petit",
        "GPA = sinusite crouteuse nécrosante + nodules pulmonaires excavés + **C-ANCA anti-PR3**",
        "GEPA = asthme tardif + éosinophilie + **P-ANCA anti-MPO**",
        "La PAN n'atteint **jamais** les artères pulmonaires ; toujours rechercher le **VHB**",
        "Le purpura vasculaire est **infiltré, déclive, polymorphe** et épargne les muqueuses",
        "L'artérite à cellules géantes : corticothérapie **0,5-0,7 mg/kg/j**, BAV dans **30%**, bolus si atteinte visuelle",
        "Devant un PTI, rechercher systématiquement un **lupus** (ANA) et une **dysthyroïdie**",
        "L'arrêt brutal d'une corticothérapie prolongée peut provoquer une **insuffisance surrénalienne aiguë**",
        "Le SAPL associe thromboses + manifestations obstétricales + **APL positifs à 2 reprises** (12 semaines) ; traitement par **AVK**",
    ]

    fiche_eclair_md = (
        "**MAI** : 6-7% population, rupture tolérance, FDR génétiques (HLA) + "
        "environnementaux + hormonaux. ANA par IFI HEP-2 puis ENA puis ELISA.\n\n"
        "**Vascularites** : Chapel Hill selon calibre. Gros (ACG, Takayasu), "
        "Moyen (PAN, Kawasaki), Petit ANCA (GPA/GEPA/MPA), Petit CI (IgA, cryo). "
        "Manifestations communes : AEG + purpura + mononévrite + GNRP + hémorragie IA.\n\n"
        "**ACG (Horton)** : F > 50 ans, céphalées temporales, claudication mâchoire, "
        "BAV 30%. CTC 0,5-0,7 mg/kg, bolus si ophtalmo, sevrage 18 mois, 50% rechute.\n\n"
        "**PPR** : ceintures inflammatoires > 50 ans, CPK normales, très corticosensible 0,2-0,35 mg/kg.\n\n"
        "**Purpura vasculaire** : infiltré, déclive, polymorphe, muqueuses épargnées. "
        "Bilan : ANCA, ANA, cryo, FR, hémocultures, biopsie cutanée.\n\n"
        "**Anémie microcytaire** : carence martiale vs inflammation. Bilan = ferritine + CRP.\n\n"
        "**PTI** : thrombopénie isolée, myélogramme si > 65 ans. Rechercher lupus + dysthyroïdie.\n\n"
        "**SAPL** : thromboses + obstetrical + APL x2 (12 sem). AVK au long cours.\n\n"
        "**Sarcoïdose** : Löfgren = érythème noueux + arthralgies chevilles + ADP hilaires."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Médecine interne",
        annee="2025-2026",
        item="Items 189, 190, 191, 193, 194, 197, 207, 209, 211, 213",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi, partie_vii],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()

    # Images : charger depuis image_captions.json si disponible
    captions_file = PROJECT_ROOT / "output" / ".work" / "medecine-interne" / "image_captions.json"
    if captions_file.exists():
        # image loading code
        pass

    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Medecine_generale_medecine-interne_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out} ({pdf_out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()

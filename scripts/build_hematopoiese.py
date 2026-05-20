#!/usr/bin/env python3
"""Génère la fiche Major ECN « Hématopoïèse ».

Construite à partir du contenu fusionné des 3 PDF sources (chapitre
« Hématopoïèse », Hématologie, Elsevier Masson), en une fiche unique.
Sortie : examples/Hematologie_Hematopoiese_2025-2026.{pdf,docx}
"""

from __future__ import annotations

import glob
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from major_ecn.config import LOGO_PATH  # noqa: E402
from major_ecn.content_builder import output_basename  # noqa: E402
from major_ecn.docx_generator import render_docx  # noqa: E402
from major_ecn.models import (  # noqa: E402
    Algorithme,
    AnalyzedImage,
    ExtractedImage,
    FicheData,
    FicheRow,
    Partie,
    PlanPartie,
    PlanSousPartie,
    SousPartie,
    TableauSynthese,
)
from major_ecn.pdf_generator import render_pdf  # noqa: E402

FIG_DIR = PROJECT_ROOT / "examples" / "sample_figures"


def _row(concept: str, detail: str) -> FicheRow:
    return FicheRow(concept=concept, detail_md=detail)


def _reflexe(kind: str, detail: str) -> FicheRow:
    return FicheRow(concept="", detail_md=detail, kind=kind)


def _prepare_figures() -> None:
    """Recrée les schémas en découpant les pages des PDF sources.

    Les fichiers sources (« 1 - Hématopoïèse - Partie {1,2,3}.pdf ») sont des
    pages scannées : chaque figure est obtenue par recadrage d'une page.
    """
    import fitz
    from PIL import Image

    FIG_DIR.mkdir(parents=True, exist_ok=True)
    sources = sorted(glob.glob(str(PROJECT_ROOT / "examples" / "*Partie*.pdf")))
    if len(sources) < 3:
        print("Sources PDF introuvables — figures non régénérées.")
        return
    part1, part2, part3 = sources[0], sources[1], sources[2]

    # (source, index de page, y0, y1, x0, x1, nom de sortie) — fractions de page.
    crops = [
        (part1, 2, 0.500, 0.875, 0.036, 0.976, "hemato_cascade.png"),
        (part1, 6, 0.325, 0.712, 0.028, 0.976, "hemato_erythropoiese.png"),
        (part2, 5, 0.138, 0.435, 0.028, 0.976, "hemato_granulopoiese.png"),
        (part3, 4, 0.085, 0.800, 0.028, 0.976, "hemato_hemopathies.png"),
    ]
    for src, page_idx, y0, y1, x0, x1, name in crops:
        doc = fitz.open(src)
        pix = doc[page_idx].get_pixmap(dpi=220)
        doc.close()
        image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        width, height = image.size
        box = (int(x0 * width), int(y0 * height),
               int(x1 * width), int(y1 * height))
        image.crop(box).save(FIG_DIR / name)


def _figure(name: str, description: str, number: int) -> AnalyzedImage:
    path = FIG_DIR / name
    source = ExtractedImage(data=b"", ext="png", page=1, index=number,
                            width=2200, height=1200, sha=f"hemato-{number}")
    return AnalyzedImage(source=source, description=description,
                         concept_lie=description, pertinence=9, type="schema",
                         section_suggeree=description, saved_path=path,
                         figure_number=number)


def _plan() -> list[PlanPartie]:
    return [
        PlanPartie("I", "Organisation du tissu hématopoïétique",
                   "Sites de l'hématopoïèse, moelle osseuse et organes lymphoïdes.",
                   [PlanSousPartie("A", "Moelle osseuse hématopoïétique",
                                   "Localisation et microenvironnement."),
                    PlanSousPartie("B", "Organes lymphoïdes",
                                   "Organes centraux et périphériques.")]),
        PlanPartie("II", "Cellules souches et cascade hématopoïétique",
                   "Cellules souches et compartiments de différenciation.",
                   [PlanSousPartie("A", "Cellules souches hématopoïétiques",
                                   "Définition, propriétés, marqueurs."),
                    PlanSousPartie("B", "Les trois compartiments de la cascade",
                                   "Progéniteurs, précurseurs, cellules matures.")]),
        PlanPartie("III", "Régulation de l'hématopoïèse",
                   "Facteurs de croissance et microenvironnement.",
                   [PlanSousPartie("A", "Facteurs de croissance hématopoïétiques",
                                   "Facteurs de différenciation et facteurs amont."),
                    PlanSousPartie("B", "Microenvironnement et régulation cellulaire",
                                   "Hypoxie et îlot érythroblastique.")]),
        PlanPartie("IV", "Lignée érythrocytaire et hémoglobine",
                   "Érythropoïèse, structure de l'hématie et hémolyse.",
                   [PlanSousPartie("A", "Érythropoïèse", "Cascade et réticulocyte."),
                    PlanSousPartie("B", "Structure de l'hématie et hémoglobine",
                                   "Membrane, cytosquelette, hémoglobine."),
                    PlanSousPartie("C", "Métabolisme et hémolyse de l'hématie",
                                   "Glycolyse, durée de vie, hémolyse.")]),
        PlanPartie("V", "Facteurs nutritionnels de l'érythropoïèse",
                   "Métabolisme du fer, des folates et de la vitamine B12.",
                   [PlanSousPartie("A", "Métabolisme du fer",
                                   "Répartition, absorption, transport."),
                    PlanSousPartie("B", "Folates (B9) et vitamine B12",
                                   "Apports, absorption, rôle.")]),
        PlanPartie("VI", "Leucocytes et plaquettes",
                   "Granulopoïèse, monocytes, lymphocytes et plaquettes.",
                   [PlanSousPartie("A", "Polynucléaires (granulocytes)",
                                   "Neutrophiles, éosinophiles, basophiles."),
                    PlanSousPartie("B", "Monocytes et lymphocytes",
                                   "Lymphopoïèse B et T, cellules NK."),
                    PlanSousPartie("C", "Plaquettes sanguines",
                                   "Origine mégacaryocytaire.")]),
        PlanPartie("VII", "Exploration hématologique et principales hémopathies",
                   "Examens d'exploration et grandes hémopathies.",
                   [PlanSousPartie("A", "Exploration du sang et de la moelle",
                                   "NFS, myélogramme, BOM, immunophénotypage."),
                    PlanSousPartie("B", "Principales hémopathies",
                                   "Hémopathies malignes et insuffisance médullaire.")]),
    ]


def _parties() -> list[Partie]:
    p1 = Partie("I", "Organisation du tissu hématopoïétique", [
        SousPartie("A", "Moelle osseuse hématopoïétique", [
            _row("★ Sites de l'hématopoïèse",
                 "- Apparition du sang dès le **21ᵉ jour** de l'embryogenèse "
                 "(mésoderme du **sac vitellin**)\n"
                 "- Entre le **2ᵉ et le 7ᵉ mois** : relais par le **foie** et la "
                 "**rate**\n"
                 "- **2 derniers mois** de vie intra-utérine : la **moelle "
                 "osseuse** devient prédominante\n"
                 "- Après la naissance : la moelle est le site **exclusif** de "
                 "production sanguine"),
            _row("◆ Topographie chez l'adulte",
                 "- Au cours de l'enfance, le tissu hématopoïétique des **os "
                 "longs** est remplacé par du **tissu adipeux**\n"
                 "- Chez l'adulte : **3/4** de la moelle hématopoïétique dans "
                 "les **os plats** (bassin, sternum) et les **vertèbres**"),
            _row("Microenvironnement médullaire",
                 "- Espace **contraint** (cadre osseux non extensible), très "
                 "richement **vascularisé** (sinus)\n"
                 "- **Matrice extracellulaire** : fibronectine, laminine, "
                 "collagènes\n"
                 "- **Cellules stromales** : interactions via des **molécules "
                 "d'adhésion**\n"
                 "- **Niches hématopoïétiques** : les cellules immatures y sont "
                 "fixées ; leur maturation modifie les facteurs d'ancrage et "
                 "favorise la libération des cellules différenciées dans le sang"),
            _reflexe("a_retenir",
                     "Chez l'adulte, la moelle osseuse est le site **exclusif** "
                     "de l'hématopoïèse, localisée pour les **3/4** dans les os "
                     "plats et les vertèbres."),
        ]),
        SousPartie("B", "Organes lymphoïdes", [
            _row("Organes lymphoïdes centraux",
                 "- **Moelle osseuse** : tissu lymphoïde diffus, non folliculaire\n"
                 "- **Thymus** : structure non folliculaire, lobules avec une "
                 "zone **corticale** (thymocytes immatures CD3+ CD4+ CD8+) et "
                 "une zone **médullaire** (lymphocytes T matures)\n"
                 "  - apparaît à la **6ᵉ semaine**, **involue à partir de la "
                 "puberté**, persiste à l'état de traces jusqu'à ~60 ans"),
            _row("Organes lymphoïdes périphériques",
                 "- **Ganglions lymphatiques**, **rate**, amygdales, tissu "
                 "lymphoïde des muqueuses (MALT), système lymphoïde cutané\n"
                 "- Des lymphocytes sont présents dans presque tous les organes "
                 "(sauf le **système nerveux central**)"),
            _row("★ Structure du ganglion lymphatique",
                 "- **Zone corticale externe** : follicules lymphoïdes "
                 "(**lymphocytes B**)\n"
                 "- **Zone paracorticale** : **lymphocytes T** + cellules "
                 "dendritiques\n"
                 "- **Zone médullaire** : pauvre en cellules\n"
                 "- Follicule **secondaire** (après stimulation antigénique) : "
                 "manteau, **centre germinatif** avec zone sombre "
                 "centroblastique (prolifération, **commutation isotypique**) et "
                 "zone claire centrocytique (sélection par l'antigène)"),
            _row("Rate",
                 "- **Pulpe rouge** : sinus veineux + cordons de Billroth\n"
                 "- **Pulpe blanche** périartériolaire : manchons lymphoïdes "
                 "(LT) + follicules lymphoïdes (LB) en périphérie\n"
                 "- Organe hématopoïétique jusqu'au **9ᵉ mois** de vie "
                 "intra-utérine"),
            _reflexe("piege",
                     "Le thymus **involue à partir de la puberté** : ce n'est "
                     "pas un organe lymphoïde fonctionnellement actif chez "
                     "l'adulte."),
        ]),
    ])

    p2 = Partie("II", "Cellules souches et cascade hématopoïétique", [
        SousPartie("A", "Cellules souches hématopoïétiques (CSH)", [
            _row("◆ Définition et fonctions",
                 "- Sous-population **très minoritaire** de progéniteurs "
                 "immatures **multipotents**\n"
                 "- Deux fonctions : l'**auto-renouvellement** et la **production "
                 "de cellules différenciées**\n"
                 "- Capables de **reconstituer à long terme** une hématopoïèse "
                 "complète (lymphoïde **et** myéloïde) après myéloablation"),
            _row("Modes d'auto-renouvellement",
                 "- **Embryogenèse** : auto-renouvellement d'**expansion** — "
                 "division **symétrique** (1 CSH → 2 CSH), amplification du pool\n"
                 "- **Après la naissance** : auto-renouvellement **de maintien** "
                 "— division **asymétrique** (1 CSH + 1 progéniteur engagé dans "
                 "la différenciation)"),
            _row("◆ Quiescence",
                 "- Au sein des niches, les CSH font **très peu de mitoses** et "
                 "sont majoritairement **quiescentes**\n"
                 "- Cette quiescence les **protège des chimiothérapies** "
                 "(antimitotiques) à doses conventionnelles"),
            _row("★ Marqueur CD34",
                 "- Les progéniteurs expriment la sialomucine **CD34**\n"
                 "- Les cellules **CD34+** représentent environ **1 %** des "
                 "cellules mononucléées médullaires\n"
                 "- Les progéniteurs les plus immatures sont **CD34+ CD38−**"),
            _row("Propriétés (thérapie cellulaire)",
                 "- **Résistent à la congélation** à −196 °C (azote liquide)\n"
                 "- Capables de **migrer dans le sang** → collecte par "
                 "**cytaphérèse** (cellules souches périphériques)"),
            _row("Cellules souches mésenchymateuses",
                 "- Présentes aussi dans la moelle\n"
                 "- À l'origine du **stroma médullaire**, des **ostéoblastes**, "
                 "des adipocytes et des cellules musculaires lisses"),
        ]),
        SousPartie("B", "Les trois compartiments de la cascade", [
            _row("Progéniteurs",
                 "- **Non identifiables** morphologiquement ; quantification par "
                 "**culture cellulaire**\n"
                 "- Progéniteurs **clonogéniques** : **CFU** (colony-forming "
                 "unit) — CFU-GEMM, CFU-GM, CFU-G, CFU-M, BFU-E, CFU-E…\n"
                 "- La capacité d'auto-renouvellement **diminue** avec la "
                 "maturation"),
            _row("Précurseurs",
                 "- **Identifiables morphologiquement** (myélogramme, frottis)\n"
                 "- Nom terminé par le suffixe **« …blaste »** (ex : "
                 "érythroblaste) témoignant du caractère jeune/immature"),
            _row("Cellules matures",
                 "- Cellules spécialisées qui **quittent la moelle** pour "
                 "rejoindre la circulation sanguine"),
            _reflexe("piege",
                     "Le terme **« blastes »** employé seul désigne a priori "
                     "des **cellules malignes** — à distinguer des précurseurs "
                     "normaux en « …blaste »."),
            _reflexe("a_retenir",
                     "Cascade hématopoïétique = **3 compartiments** : "
                     "progéniteurs → précurseurs → cellules matures. **CD34** "
                     "est le marqueur des progéniteurs."),
        ], images=[_figure("hemato_cascade.png",
                           "Cascade hématopoïétique : de la cellule souche aux "
                           "cellules matures du sang.", 1)]),
    ])

    p3 = Partie("III", "Régulation de l'hématopoïèse", [
        SousPartie("A", "Facteurs de croissance hématopoïétiques", [
            _row("◆ Production médullaire quotidienne",
                 "- **200 × 10⁹ érythrocytes**\n"
                 "- **100 × 10⁹ plaquettes**\n"
                 "- **50 × 10⁹ polynucléaires neutrophiles**\n"
                 "- Régulation très fine, adaptée aux besoins de chaque lignée"),
            _row("★ Facteurs de différenciation terminale",
                 "| Facteur | Lignée |\n"
                 "|---------|--------|\n"
                 "| **EPO** (érythropoïétine) | Érythroïde |\n"
                 "| **TPO** (thrombopoïétine) | Mégacaryocytaire |\n"
                 "| **GM-CSF** | Granuleuse + monocytaire |\n"
                 "| **G-CSF** | Granuleuse |\n"
                 "| **M-CSF** | Monocytaire |\n"
                 "| **IL-5** | Éosinophile |\n"
                 "| **SCF / kit ligand** | Basophile |"),
            _row("Facteurs actifs en amont (CSH)",
                 "- **SCF**, **TPO**, **GM-CSF**, interleukines **IL-3** et "
                 "**IL-6** : actifs sur le cycle cellulaire des CSH\n"
                 "- **SDF-1 (CXCL-12)** : chimiokine fortement concentrée dans "
                 "les niches, attire les CSH exprimant le récepteur **CXCR4**"),
            _row("Récepteurs et signalisation",
                 "- Récepteurs membranaires spécifiques : **c-Kit** (SCF), "
                 "**MPL** (TPO), récepteur de l'**EPO**\n"
                 "- Signalisation du récepteur de l'EPO : voie **JAK/STAT** "
                 "(JAK2, STAT5) → activation du facteur de transcription "
                 "**GATA1**"),
            _reflexe("a_retenir",
                     "L'**EPO** est synthétisée essentiellement par le **rein**, "
                     "la **TPO** par le **foie** : ce sont des régulations de "
                     "type **hormonal**."),
        ]),
        SousPartie("B", "Microenvironnement et régulation cellulaire", [
            _row("Gradient d'oxygène",
                 "- Gradient entre le vaisseau (**pO₂ ≈ 4 %**) et le fond des "
                 "niches (**pO₂ < 1 %**)\n"
                 "- Les CSH fonctionnent de façon optimale en **hypoxie "
                 "chronique**"),
            _row("◆ Îlot érythroblastique",
                 "- Érythroblastes étroitement au contact, autour d'un "
                 "**macrophage pourvoyeur de fer**\n"
                 "- Régulation par le système **Fas / Fas-L** : les "
                 "érythroblastes matures présentent Fas-L aux proérythroblastes "
                 "voisins → **apoptose** → **frein de l'érythropoïèse**"),
        ]),
    ])

    p4 = Partie("IV", "Lignée érythrocytaire et hémoglobine", [
        SousPartie("A", "Érythropoïèse", [
            _row("◆ Cascade érythroïde",
                 "- Progéniteurs : CFU-GEMM → **BFU-E** → **CFU-E**\n"
                 "- Précurseurs : **proérythroblaste** → érythroblastes "
                 "basophiles I et II → polychromatophile → **acidophile**\n"
                 "- Après **énucléation** : **réticulocyte** → **hématie**\n"
                 "- 1 proérythroblaste donne **16 réticulocytes**"),
            _row("Maturation érythroblastique",
                 "- Chaque division : **↓ taille**, **↓ rapport "
                 "nucléocytoplasmique**, condensation de la chromatine\n"
                 "- Cytoplasme **acidophile** (orangé au MGG) = traduit la "
                 "fabrication d'**hémoglobine**"),
            _row("★ Réticulocyte",
                 "- Hématie **jeune**, anucléée, riche en **ARN**\n"
                 "- Séjour : **1-3 j** dans la moelle, **1-2 j** dans le sang\n"
                 "- Valeur normale : **20-100 G/L**\n"
                 "- Reflète la **production médullaire** → caractère "
                 "**régénératif ou non** d'une anémie"),
            _row("Durée et délais",
                 "- Érythropoïèse normale = **7 jours** (raccourcie si besoins "
                 "augmentés)\n"
                 "- Après une hémorragie : délai minimal de **3 jours** avant "
                 "délivrance de nouvelles hématies"),
            _reflexe("piege",
                     "La présence de **corps de Howell-Jolly** (reliquat "
                     "nucléaire) sur le frottis est constante après "
                     "**splénectomie** ou fait suspecter une **asplénie**."),
        ], images=[_figure("hemato_erythropoiese.png",
                           "Érythropoïèse : de la BFU-E à l'hématie mature.", 2)]),
        SousPartie("B", "Structure de l'hématie et hémoglobine", [
            _row("Hématie mature",
                 "- Disque **biconcave**, **anucléé**, diamètre **7,8 µm**, "
                 "épaisseur 1,7 µm\n"
                 "- Grande capacité de **déformation** (capillaires de 5 µm)\n"
                 "- 20 × 10¹² hématies ; durée de vie **120 jours**"),
            _row("Membrane et cytosquelette",
                 "- **Bicouche lipidique** de phospholipides stabilisée par du "
                 "**cholestérol**\n"
                 "- Cytosquelette : **spectrine** (tétramères), **actine**, "
                 "protéine **bande 4.1**, **ankyrine** (relie la spectrine à la "
                 "**bande 3** transmembranaire)\n"
                 "- Anomalies → ↓ déformabilité → hémolyse "
                 "(**sphérocytose héréditaire / maladie de "
                 "Minkowski-Chauffard**)"),
            _row("◆ Hémoglobine",
                 "- 4 chaînes de **globine** identiques 2 à 2 + 4 molécules "
                 "d'**hème**\n"
                 "- **Hème** = porphyrine + atome de **fer** central (fixe l'O₂)\n"
                 "- Le **2,3-DPG** se fixe à l'état désoxygéné et régule "
                 "l'affinité de l'Hb pour l'O₂"),
            _row("★ Types d'hémoglobine",
                 "| Hémoglobine | Composition | Proportion (adulte) |\n"
                 "|-------------|-------------|---------------------|\n"
                 "| **HbA** | α2β2 | 97-99 % |\n"
                 "| **HbA2** | α2δ2 | 1-3,5 % |\n"
                 "| **HbF** (fœtale) | α2γ2 | traces (prédominante chez le fœtus) |\n"
                 "\n- **HbA1c** = HbA glycosylée, **augmentée dans le diabète**"),
            _row("Courbe de dissociation de l'O₂",
                 "- **↑ affinité** pour l'O₂ → décalage vers la **gauche**\n"
                 "- **↓ affinité** → décalage vers la **droite**"),
        ]),
        SousPartie("C", "Métabolisme et hémolyse de l'hématie", [
            _row("Métabolisme énergétique",
                 "- Énergie fournie **exclusivement** par la **glycolyse "
                 "intra-érythrocytaire**\n"
                 "- Voie principale anaérobie (90 %) d'**Embden-Meyerhof** : "
                 "**pyruvate kinase (PK)** → ATP\n"
                 "- Voie accessoire (10 %), **shunt des pentoses** : **G6PD** → "
                 "NADPH (lutte contre l'oxydation)"),
            _row("⚠ Déficits enzymatiques",
                 "- Tout déficit de la glycolyse, en particulier en **G6PD** ou "
                 "en **PK**, peut être à l'origine d'une **hémolyse**"),
            _row("Hémolyse physiologique",
                 "- Durée de vie **120 j** ; hématies vieillies phagocytées par "
                 "les **macrophages** (foie, moelle)\n"
                 "- Globine → acides aminés ; **fer recyclé** vers les "
                 "érythroblastes\n"
                 "- Hème → biliverdine → **bilirubine libre** (non conjuguée, "
                 "liée à l'albumine) → **glycuroconjugaison hépatique** → bile"),
            _row("★ Hémolyse intravasculaire",
                 "- L'hémoglobine libérée dans le plasma est captée par "
                 "l'**haptoglobine**\n"
                 "- L'**effondrement de l'haptoglobine** sérique est un "
                 "marqueur d'**hyperhémolyse**"),
            _reflexe("a_retenir",
                     "Bilirubine libre normale **< 17 µmol/L** ; liposoluble, "
                     "elle traverse la barrière hémato-encéphalique en cas de "
                     "dépassement de l'albumine → **ictère nucléaire** du "
                     "nouveau-né."),
        ]),
    ])

    p5 = Partie("V", "Facteurs nutritionnels de l'érythropoïèse", [
        SousPartie("A", "Métabolisme du fer", [
            _row("◆ Répartition du fer",
                 "- Organisme : **4 à 5 g** de fer\n"
                 "- **80 %** sous forme **héminique** : hémoglobine, "
                 "myoglobine, cytochromes\n"
                 "- **20 %** sous forme **non héminique** : ferritine, "
                 "transferrine, hémosidérine"),
            _row("Besoins et pertes",
                 "- Pertes physiologiques ≈ **1 mg/j** (urines, fèces, "
                 "desquamation)\n"
                 "- Majorées par les **menstruations** (2-3 mg/j) et la "
                 "**grossesse** (8-10 mg/j)\n"
                 "- Apports alimentaires 10-25 mg/j dont **10-20 % absorbés**, "
                 "essentiellement au niveau du **duodénum**"),
            _row("★ Absorption et régulation",
                 "- Fer ferreux capté au pôle apical de l'entérocyte par "
                 "**DMT1**\n"
                 "- Relargué dans la circulation au pôle basolatéral par la "
                 "**ferroportine**\n"
                 "- L'**hepcidine** (synthétisée par le **foie**) est l'hormone "
                 "de régulation : elle **inhibe la ferroportine** → ↓ "
                 "absorption et ↑ rétention macrophagique du fer"),
            _row("Transport et réserves",
                 "- Transport plasmatique par la **transferrine** "
                 "(sidérophiline) — le fer n'est **jamais libre** dans le "
                 "plasma\n"
                 "- Réserves : **ferritine** (rapidement disponible) et "
                 "**hémosidérine** (lentement disponible)\n"
                 "- Exploration : **ferritine**, fer sérique, coefficient de "
                 "saturation de la transferrine"),
            _reflexe("piege",
                     "Carence **martiale** → anémie **microcytaire** sans autre "
                     "cytopénie. Carence en **B9/B12** → anémie "
                     "**macrocytaire**, parfois avec thrombopénie/leucopénie "
                     "(pancytopénie)."),
        ]),
        SousPartie("B", "Folates (B9) et vitamine B12", [
            _row("Acide folique (vitamine B9)",
                 "- Vitamine **hydrosoluble**, **thermolabile** ; légumes "
                 "verts, céréales, foie\n"
                 "- Besoins adulte **400 µg/j** (600 grossesse, 500 "
                 "allaitement)\n"
                 "- Absorption dans le **jéjunum** ; **réserves faibles** "
                 "(foie), épuisables en **2 à 4 mois**"),
            _row("Vitamine B12 (cobalamines)",
                 "- **Absente du règne végétal** : foie, viandes, laitages, "
                 "œufs, poissons\n"
                 "- Besoins **3 µg/j** ; **réserves hépatiques importantes** "
                 "(suffisantes ~4 ans)"),
            _row("★ Absorption de la vitamine B12",
                 "- Liée au **facteur intrinsèque (FI)** — glycoprotéine "
                 "sécrétée par les **cellules pariétales fundiques**\n"
                 "- Absorption au niveau de l'**iléon terminal** (récepteur "
                 "**cubuline**)\n"
                 "- Transport plasmatique par les **transcobalamines** "
                 "(**TCII** = la plus importante physiologiquement)"),
            _row("Rôle métabolique",
                 "- **B9 et B12** sont indispensables à la **synthèse de "
                 "l'ADN** (donc à toutes les lignées hématopoïétiques)\n"
                 "- La **B12** intervient dans la conversion de "
                 "l'homocystéine en méthionine et le catabolisme du "
                 "méthylmalonyl-CoA (sa carence → **complications "
                 "neurologiques**)"),
            _reflexe("mnemo",
                     "Médicaments inhibant le cycle des folates : le "
                     "**méthotrexate** (dihydrofolate réductase) et le "
                     "**5-fluoro-uracile** (thymidylate synthase)."),
        ]),
    ])

    p6 = Partie("VI", "Leucocytes et plaquettes", [
        SousPartie("A", "Polynucléaires (granulocytes)", [
            _row("◆ Granulopoïèse neutrophile",
                 "- Progéniteurs : CFU-GEMM → **CFU-GM** → **CFU-G**\n"
                 "- Durée **10 jours**, deux secteurs :\n"
                 "  - **multiplication/différenciation** : myéloblaste, "
                 "promyélocyte, myélocyte\n"
                 "  - **maturation/stockage** : métamyélocyte, polynucléaire "
                 "neutrophile\n"
                 "- Compartiment de **réserve médullaire** considérable "
                 "(**8 ×** le compartiment sanguin), mobilisable en cas de "
                 "besoin aigu"),
            _row("★ Polynucléaires neutrophiles (PNN)",
                 "- Noyau **polylobé** (2 à 5 lobes) ; granulations primaires "
                 "azurophiles (myéloperoxydase) et secondaires neutrophiles\n"
                 "- Durée de vie sanguine **24 h** ; fonction = **défense "
                 "antibactérienne** par phagocytose\n"
                 "- Répartition : **pool circulant** + **pool marginé** (la NFS "
                 "ne reflète que le pool circulant)\n"
                 "- Étapes : chimiotactisme → **diapédèse** → phagocytose → "
                 "bactéricidie (dérivés oxygénés, H₂O₂)"),
            _row("Polynucléaires éosinophiles",
                 "- Cytokines clés : **IL-5** (la plus importante), IL-3, "
                 "GM-CSF\n"
                 "- Fonctions : phagocytose des **helminthes**, neutralisation "
                 "de l'**hypersensibilité immédiate**\n"
                 "- Éosinophilopoïèse **inhibée par les corticoïdes**"),
            _row("Polynucléaires basophiles",
                 "- Les **moins nombreux** des leucocytes ; granulations riches "
                 "en **histamine**\n"
                 "- Contrôle par IL-3, GM-CSF, **SCF** ; équivalents tissulaires "
                 "= **mastocytes**\n"
                 "- Récepteurs pour les **IgE** → **hypersensibilité "
                 "immédiate** (dégranulation)"),
        ], images=[_figure("hemato_granulopoiese.png",
                           "Granulopoïèse neutrophile : du myéloblaste au "
                           "polynucléaire.", 3)]),
        SousPartie("B", "Monocytes et lymphocytes", [
            _row("Monocytes",
                 "- Progéniteurs : **CFU-GM → CFU-M** ; monocytopoïèse rapide "
                 "(~**48 h**) ; **M-CSF** spécifique de la lignée\n"
                 "- Séjour sanguin 2-3 j puis passage tissulaire :\n"
                 "  - **macrophages** : phagocytose, survivent après la "
                 "phagocytose\n"
                 "  - **cellules dendritiques** : présentation de l'antigène "
                 "aux lymphocytes T"),
            _row("★ Lymphopoïèse B",
                 "- Survient dans la **moelle osseuse**\n"
                 "- Stades : **pro-B** (CD34+ CD19+ CD10+) → **pré-B** (chaîne µ "
                 "intracytoplasmique) → **B immature** (IgM de surface) → "
                 "**B mature** (IgM + IgD)\n"
                 "- ~**10 %** des lymphocytes circulants"),
            _row("★ Lymphopoïèse T",
                 "- Survient dans le **thymus**\n"
                 "- Stades : **prothymocyte** (CD2+ CD7+) → **thymocyte "
                 "cortical** (CD4+ CD8+) → **thymocyte médullaire** CD3+ "
                 "(CD4 **ou** CD8)\n"
                 "- Récepteur T : **TCR αβ** (majoritaire) ou γδ ; ~**70-80 %** "
                 "des lymphocytes circulants"),
            _row("Lymphocytes NK",
                 "- ~**10 %** des lymphocytes circulants ; phénotype **CD3− "
                 "CD16+ CD56+**\n"
                 "- Cytotoxicité **indépendante de l'antigène**, **sans "
                 "activation préalable**"),
        ]),
        SousPartie("C", "Plaquettes sanguines", [
            _row("Origine des plaquettes",
                 "- Issues de la **fragmentation du cytoplasme** des "
                 "**mégacaryocytes** (grandes cellules hyperploïdes de la "
                 "moelle)\n"
                 "- Facteur de croissance = **thrombopoïétine (TPO)**"),
        ]),
    ])

    p7 = Partie("VII", "Exploration hématologique et principales hémopathies", [
        SousPartie("A", "Exploration du sang et de la moelle", [
            _row("★ Hémogramme (NFS)",
                 "- Prélèvement de sang veineux sur **EDTA** (chélateur du "
                 "calcium)\n"
                 "- Paramètres : Hb, GR, leucocytes, plaquettes, **VGM**, "
                 "**CCMH**\n"
                 "- **Formule leucocytaire** : frottis coloré au **May-Grünwald-"
                 "Giemsa (MGG)**, décompte de 100 leucocytes en 5 catégories"),
            _row("◆ Myélogramme",
                 "- **Ponction** de moelle (sternum ou épine iliaque), "
                 "étalement + coloration **MGG**\n"
                 "- Analyse **cytologique** et **qualitative** : richesse, "
                 "pourcentages des lignées, anomalies morphologiques\n"
                 "- Ne fournit **pas** de numération par unité de volume ; "
                 "résultat obtenu **dans la journée**"),
            _row("◆ Biopsie ostéomédullaire (BOM)",
                 "- Prélèvement d'un cylindre d'os spongieux (**épine "
                 "iliaque**), examen **histologique**\n"
                 "- Réalisée **après vérification de l'absence de thrombopénie "
                 "sévère** et de trouble de la coagulation\n"
                 "- Seul examen appréciant l'**architecture médullaire** "
                 "(myélofibrose, envahissement nodulaire)"),
            _row("Immunophénotypage (cytométrie en flux)",
                 "- Analyse rapide par anticorps fluorescents ; positivité si "
                 "**> 20 %** de cellules positives\n"
                 "| Lignée | Marqueur (CD) |\n"
                 "|--------|---------------|\n"
                 "| Progéniteurs | **CD34** |\n"
                 "| Lymphoïde B | CD19, CD20 |\n"
                 "| Lymphoïde T | CD3 |\n"
                 "| Érythroïde | CD235a (glycophorine A) |\n"
                 "| Plaquettaire | CD41a, CD61 |\n"
                 "| Monocytaire | CD14 |"),
            _row("★ Cytogénétique et biologie moléculaire",
                 "- **Caryotype** et **FISH** : translocations et délétions "
                 "(ex : **t(9;22)** = chromosome **Philadelphie**)\n"
                 "- Biologie moléculaire : mutations (**JAK2 V617F**) et "
                 "transcrits de fusion (**BCR::ABL1**)"),
            _reflexe("piege",
                     "Myélogramme = examen **cytologique et qualitatif** ; "
                     "BOM = examen **histologique et quantitatif**. Seule la "
                     "BOM met en évidence l'architecture médullaire."),
        ]),
        SousPartie("B", "Principales hémopathies", [
            _row("Mécanisme général",
                 "- Anomalies génomiques **acquises** (mutations, "
                 "translocations) dans un progéniteur/précurseur → **clone** "
                 "cellulaire\n"
                 "- Le clone envahit moelle, sang, ganglions, rate et inhibe "
                 "les fonctions normales\n"
                 "- ⚠ Pas de métastases au sens strict → la classification "
                 "**TNM n'est pas utilisée** en hématologie"),
            _row("★ Hémopathies malignes aiguës",
                 "- **Perte de la capacité de différenciation** → accumulation "
                 "de **blastes** dans la moelle\n"
                 "- **Leucémie aiguë myéloïde (LAM)** ou **lymphoïde (LAL)** ; "
                 "début souvent **brutal**"),
            _row("◆ Syndromes myéloprolifératifs",
                 "- Capacité de différenciation **conservée** → production "
                 "dérégulée de cellules matures\n"
                 "- **Polyglobulie primitive** (maladie de Vaquez)\n"
                 "- **Leucémie myéloïde chronique** (chromosome **Philadelphie**, "
                 "t(9;22), BCR::ABL1)\n"
                 "- **Thrombocytémie essentielle**\n"
                 "- **Splénomégalie myéloïde** (myélofibrose primitive)"),
            _row("Syndromes lymphoprolifératifs",
                 "- **Leucémie lymphoïde chronique** : hyperlymphocytose B "
                 "monoclonale\n"
                 "- **Lymphomes** (B ou T) : prolifération préférentiellement "
                 "ganglionnaire\n"
                 "- **Myélome** : prolifération de **plasmocytes** tumoraux "
                 "(ostéolyse, immunoglobuline monoclonale)"),
            _row("◆ Déficit de production intramédullaire",
                 "- **4 conditions** indispensables : présence de CSH, absence "
                 "de dysfonctionnement des CSH, apports en fer/folates/B12, "
                 "espace médullaire suffisant\n"
                 "- Défaillances : **aplasie médullaire** (absence de CSH), "
                 "**syndromes myélodysplasiques** (dysfonctionnement), "
                 "**carences**, **envahissement / myélofibrose** (manque "
                 "d'espace)"),
        ], images=[_figure("hemato_hemopathies.png",
                           "Schéma de l'hématopoïèse normale et localisation "
                           "des principales hémopathies myéloïdes et "
                           "lymphoïdes.", 4)]),
    ])

    return [p1, p2, p3, p4, p5, p6, p7]


def _algorithmes() -> list[Algorithme]:
    return [
        Algorithme(
            titre="Orientation devant une hémopathie maligne",
            arbre_md=(
                "- Anomalie génomique acquise dans un progéniteur/précurseur\n"
                "  - Capacité de différenciation **perdue** → accumulation de "
                "blastes → **leucémie aiguë** (LAM ou LAL)\n"
                "  - Capacité de différenciation **conservée**\n"
                "    - Lignée **myéloïde** → **syndrome myéloprolifératif** "
                "(Vaquez, LMC, thrombocytémie essentielle, myélofibrose)\n"
                "    - Lignée **lymphoïde** → **syndrome lymphoprolifératif** "
                "(LLC, lymphome, myélome)"
            ),
        ),
        Algorithme(
            titre="Déficit de production intramédullaire : les 4 conditions",
            arbre_md=(
                "- Hématopoïèse normale = 4 conditions réunies\n"
                "  - Absence de **CSH** → **aplasie médullaire**\n"
                "  - **Dysfonctionnement** des CSH → **syndrome "
                "myélodysplasique**\n"
                "  - Apports insuffisants → **carence** en fer, folates ou B12\n"
                "  - Manque d'**espace** → **envahissement** ou **myélofibrose**"
            ),
        ),
    ]


def _tableaux() -> list[TableauSynthese]:
    return [
        TableauSynthese(
            "Les trois compartiments de l'hématopoïèse",
            "| Compartiment | Identification | Exemples |\n"
            "|--------------|----------------|----------|\n"
            "| **Progéniteurs** | Non identifiables (culture) | CSH, CFU-GEMM, "
            "BFU-E, CFU-GM |\n"
            "| **Précurseurs** | Morphologie (myélogramme) | Proérythroblaste, "
            "myéloblaste |\n"
            "| **Cellules matures** | Frottis sanguin | Hématie, PNN, "
            "plaquette |",
        ),
        TableauSynthese(
            "Facteurs de croissance hématopoïétiques",
            "| Facteur | Lignée stimulée | Source principale |\n"
            "|---------|-----------------|-------------------|\n"
            "| **EPO** | Érythroïde | Rein |\n"
            "| **TPO** | Mégacaryocytaire | Foie |\n"
            "| **G-CSF** | Granuleuse | Cellules stromales |\n"
            "| **GM-CSF** | Granuleuse + monocytaire | Cellules stromales |\n"
            "| **M-CSF** | Monocytaire | Cellules stromales |\n"
            "| **IL-5** | Éosinophile | Lymphocytes T |",
        ),
        TableauSynthese(
            "Myélogramme normal de l'adulte",
            "| Lignée | Pourcentage |\n"
            "|--------|-------------|\n"
            "| Cellules indifférenciées (hémoblastes) | 1-2 % |\n"
            "| Lignée granuleuse neutrophile (totale) | ≈ 50-60 % |\n"
            "| Lignée éosinophile | 1-4 % |\n"
            "| Lignée basophile | 0,5-1 % |\n"
            "| Lignée érythroblastique (totale) | ≈ 15-30 % |\n"
            "| Lymphocytes | 5-15 % |\n"
            "| Plasmocytes | 1-3 % |\n"
            "\n*Rapport érythroblastes / granuleux normal : 1/3 à 1/4.*",
        ),
        TableauSynthese(
            "Carences et anémies",
            "| Carence | Type d'anémie | Particularités |\n"
            "|---------|---------------|----------------|\n"
            "| **Fer** | Microcytaire | Sans autre cytopénie |\n"
            "| **Folates (B9)** | Macrocytaire | ± thrombopénie / leucopénie |\n"
            "| **Vitamine B12** | Macrocytaire | + signes neurologiques |",
        ),
        TableauSynthese(
            "Myélogramme vs biopsie ostéomédullaire",
            "| Critère | Myélogramme | Biopsie ostéomédullaire |\n"
            "|---------|-------------|--------------------------|\n"
            "| Nature | Cytologique | Histologique |\n"
            "| Apport | Qualitatif (morphologie) | Quantitatif (richesse, "
            "architecture) |\n"
            "| Architecture médullaire | Non | **Oui** (myélofibrose…) |\n"
            "| Délai | Dans la journée | 2-3 jours |",
        ),
    ]


def _chiffres() -> TableauSynthese:
    return TableauSynthese(
        "Chiffres-clés",
        "| Paramètre | Valeur |\n"
        "|-----------|--------|\n"
        "| Production quotidienne d'érythrocytes | **200 × 10⁹** |\n"
        "| Production quotidienne de plaquettes | **100 × 10⁹** |\n"
        "| Production quotidienne de PNN | **50 × 10⁹** |\n"
        "| Durée de vie de l'hématie | **120 jours** |\n"
        "| Durée de vie sanguine du PNN | **24 heures** |\n"
        "| Durée de l'érythropoïèse / granulopoïèse | **7 j / 10 j** |\n"
        "| Réticulocytes (valeur normale) | **20-100 G/L** |\n"
        "| Cellules CD34+ dans la moelle | **≈ 1 %** |\n"
        "| Fer total de l'organisme | **4-5 g** |\n"
        "| Bilirubine libre (normale) | **< 17 µmol/L** |\n"
        "| HbA / HbA2 chez l'adulte | **97-99 % / 1-3,5 %** |\n"
        "| Besoins en folates / vitamine B12 | **400 µg/j / 3 µg/j** |",
    )


def _points_cles() -> list[str]:
    return [
        "Chez l'adulte, la **moelle osseuse** (os plats, vertèbres) est le site "
        "**exclusif** de l'hématopoïèse.",
        "Les **cellules souches hématopoïétiques** assurent l'**auto-"
        "renouvellement** et la production de cellules différenciées ; elles "
        "sont **quiescentes** et expriment le **CD34**.",
        "La cascade comprend **3 compartiments** : progéniteurs → précurseurs "
        "(« …blaste ») → cellules matures.",
        "L'**EPO** (rein) régule l'érythropoïèse, la **TPO** (foie) la lignée "
        "plaquettaire : régulations hormonales.",
        "L'**érythropoïèse** dure 7 jours ; le **réticulocyte** reflète la "
        "production médullaire et le caractère régénératif d'une anémie.",
        "La **vitamine B12** est absorbée dans l'**iléon** grâce au **facteur "
        "intrinsèque** ; B9 et B12 sont indispensables à la synthèse de l'ADN.",
        "Le **fer** est régulé par l'**hepcidine** (foie) ; carence martiale → "
        "anémie **microcytaire**, carence B9/B12 → anémie **macrocytaire**.",
        "Les hémopathies malignes naissent d'un **clone** : différenciation "
        "perdue → **leucémie aiguë**, conservée → **syndrome myélo- ou "
        "lymphoprolifératif**.",
    ]


def _fiche_eclair() -> str:
    return (
        "**Sites** : embryon (sac vitellin) → foie/rate → moelle osseuse, "
        "site exclusif après la naissance (os plats + vertèbres).\n\n"
        "**Cellules souches** : auto-renouvellement + différenciation ; "
        "quiescentes ; marqueur **CD34** ; cascade en 3 compartiments "
        "(progéniteurs → précurseurs → cellules matures).\n\n"
        "**Régulation** : facteurs de croissance — **EPO** (rein, érythroïde), "
        "**TPO** (foie, plaquettes), G/GM/M-CSF, IL-5 ; microenvironnement "
        "(niches, hypoxie, îlot érythroblastique).\n\n"
        "**Lignée rouge** : érythropoïèse 7 j (BFU-E → … → réticulocyte → "
        "hématie 120 j) ; hémoglobine = globine + hème + fer ; hémolyse → "
        "bilirubine libre, haptoglobine.\n\n"
        "**Facteurs nutritionnels** : fer (hepcidine, transferrine, ferritine), "
        "folates et B12 (facteur intrinsèque, iléon) — synthèse de l'ADN.\n\n"
        "**Autres lignées** : granulopoïèse 10 j (PNN), monocytes/macrophages, "
        "lymphopoïèse B (moelle) et T (thymus), plaquettes (mégacaryocytes).\n\n"
        "**Exploration** : NFS, myélogramme (cytologie), BOM (histologie), "
        "immunophénotypage (CD), cytogénétique.\n\n"
        "**Hémopathies** : leucémies aiguës (blastes), syndromes myélo- et "
        "lymphoprolifératifs ; déficit médullaire (aplasie, SMD, carences, "
        "envahissement)."
    )


def build() -> FicheData:
    return FicheData(
        matiere="Hématologie",
        nom_cours="Hématopoïèse",
        annee="2025-2026",
        item="",
        plan=_plan(),
        parties=_parties(),
        algorithmes=_algorithmes(),
        tableaux=_tableaux(),
        chiffres_cles=_chiffres(),
        points_cles=_points_cles(),
        fiche_eclair_md=_fiche_eclair(),
        images=[],
        fiche_numero="Hématologie",
    )


def main() -> None:
    _prepare_figures()
    fiche = build()
    output_dir = PROJECT_ROOT / "examples"
    basename = output_basename(fiche.matiere, fiche.nom_cours, fiche.annee)
    logo = LOGO_PATH if LOGO_PATH.exists() else None

    pdf_path = render_pdf(fiche, output_dir / f"{basename}.pdf")
    print(f"PDF généré  : {pdf_path}")
    docx_path = render_docx(fiche, output_dir / f"{basename}.docx", logo)
    print(f"DOCX généré : {docx_path}")


if __name__ == "__main__":
    main()

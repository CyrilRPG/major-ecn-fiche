"""Fiche de revision BPCO (Medecine Generale, 10 pages max)."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from major_ecn.models import (
    AnalyzedImage,
    ExtractedImage,
    FicheData,
    FicheRow,
    Partie,
    PlanPartie,
    PlanSousPartie,
    SousPartie,
    TableauSynthese,
    UsageStats,
)
from major_ecn.config import LOGO_PATH
from major_ecn.pdf_generator import render_pdf


_SOURCE_IMAGES = [
    {
        "file": "source_07_p7.png",
        "partie": 0,  # I. Généralités
        "sp": 0,
        "desc": "Schema emphyseme centrolobulaire vs panlobulaire",
        "concept": "Types d'emphyseme",
        "type": "schema",
    },
    {
        "file": "source_11_p7.png",
        "partie": 0,
        "sp": 0,
        "desc": "Histologie emphyseme et obstruction bronchique",
        "concept": "Physiopathologie BPCO",
        "type": "schema",
    },
    {
        "file": "source_08_p7.png",
        "partie": 1,  # II. Tableau clinique
        "sp": 0,
        "desc": "Thorax en tonneau : signes cliniques et radiographique",
        "concept": "Distension thoracique BPCO",
        "type": "photo_clinique",
    },
    {
        "file": "source_12_p8.png",
        "partie": 2,  # III. Diagnostic / EFR (mais aussi évaluation GOLD = partie III si je veux)
        "sp": 1,
        "desc": "Classification GOLD et evaluation ABCD",
        "concept": "Stades GOLD BPCO",
        "type": "classification",
    },
    {
        "file": "source_16_p10.png",
        "partie": 3,  # IV. Prise en charge
        "sp": 1,      # B. Traitement et réhabilitation
        "desc": "Algorithme de traitement pharmacologique de la BPCO",
        "concept": "Traitement BPCO",
        "type": "algorithme",
    },
    {
        "file": "source_17_p11.png",
        "partie": 4,  # V. Exacerbations
        "sp": 1,
        "desc": "Tableau de l'antibiotherapie des exacerbations de BPCO",
        "concept": "ATB exacerbation BPCO",
        "type": "tableau",
    },
]


def build_fiche() -> FicheData:
    plan = [
        PlanPartie(
            numero="I",
            titre="Generalites et facteurs de risque",
            sous_parties=[
                PlanSousPartie(lettre="A", titre="Definition et entites cliniques"),
                PlanSousPartie(lettre="B", titre="Facteurs de risque"),
            ],
        ),
        PlanPartie(
            numero="II",
            titre="Tableau clinique",
            sous_parties=[
                PlanSousPartie(lettre="A", titre="Signes fonctionnels et physiques"),
                PlanSousPartie(lettre="B", titre="Phenotypes cliniques"),
            ],
        ),
        PlanPartie(
            numero="III",
            titre="Diagnostic positif : EFR",
            sous_parties=[
                PlanSousPartie(lettre="A", titre="Spirometrie"),
                PlanSousPartie(lettre="B", titre="Severite et explorations complementaires"),
            ],
        ),
        PlanPartie(
            numero="IV",
            titre="Evaluation et prise en charge au long cours",
            sous_parties=[
                PlanSousPartie(lettre="A", titre="Bilan, mesures generales et vaccinations"),
                PlanSousPartie(lettre="B", titre="Traitement pharmacologique et rehabilitation"),
            ],
        ),
        PlanPartie(
            numero="V",
            titre="Exacerbations de BPCO",
            sous_parties=[
                PlanSousPartie(lettre="A", titre="Definition et etiologies"),
                PlanSousPartie(lettre="B", titre="Prise en charge"),
            ],
        ),
    ]

    # ── PARTIE I : GÉNÉRALITÉS ──
    partie_i = Partie(
        numero="I",
        titre="Généralités et facteurs de risque",
        sous_parties=[
            SousPartie(lettre="A", titre="Définition et entités cliniques", rows=[
                FicheRow(concept="★ Définition", detail_md=(
                    "- **BPCO** : maladie respiratoire chronique définie par une obstruction "
                    "**permanente** et **progressive** des voies aériennes\n"
                    "- **Prévalence** : ~7,5 % de la population > 40 ans\n"
                    "- Incidence se stabilise chez l'homme, augmente chez la femme"
                )),
                FicheRow(concept="★ Entités cliniques", detail_md=(
                    "- **Bronchite chronique** (définition clinique) : toux productive quotidienne :\n"
                    "  - > **3 mois/an** pendant > **2 années consécutives**\n"
                    "  - 50 % des fumeurs\n"
                    "  - Peut être simple (sans TVO) ou obstructive (avec TVO = BPCO)\n"
                    "- **Emphysème** : élargissement permanent des espaces aériens distaux avec "
                    "destruction des parois alvéolaires, sans fibrose :\n"
                    "  - Centro-lobulaire ou pan-lobulaire\n"
                    "  - Radio : zones d'hypodensité (raréfaction parenchyme)"
                )),
                FicheRow(concept="", detail_md=(
                    "- **BPCO** = TVO non complètement réversible avec **réversibilité possible**\n"
                    "- La bronchite chronique simple sans TVO **n'est pas une BPCO**"
                ), kind="a_retenir"),
            ]),
            SousPartie(lettre="B", titre="Facteurs de risque", rows=[
                FicheRow(concept="★ Tabac", detail_md=(
                    "- **Tabac +++** : principal facteur de risque\n"
                    "  - > **15 PA** chez la femme, > **20 PA** chez l'homme\n"
                    "- Cannabis"
                )),
                FicheRow(concept="Autres", detail_md=(
                    "- Exposition aux aérocontaminants professionnels\n"
                    "- Pollution atmosphérique"
                )),
            ]),
        ],
    )

    # ── PARTIE II : TABLEAU CLINIQUE ──
    partie_ii = Partie(
        numero="II",
        titre="Tableau clinique",
        sous_parties=[
            SousPartie(lettre="A", titre="Signes fonctionnels et physiques", rows=[
                FicheRow(concept="Signes fonctionnels", detail_md=(
                    "- **Dyspnée** : initialement à l'effort, évaluée par échelle **mMRC**\n"
                    "- Toux et expectoration chroniques"
                )),
                FicheRow(concept="★ Signes physiques", detail_md=(
                    "- Stades croissants à l'auscultation :\n"
                    "  - Ronchi\n"
                    "  - Allongement du temps expiratoire\n"
                    "  - Diminution du murmure vésiculaire\n"
                    "  - Distension thoracique (**thorax en tonneau**)\n"
                    "- ⚠ **Signe de Hoover** : diminution paradoxale du diamètre transversal "
                    "thoracique inférieur à l'inspiration (distension sévère)\n"
                    "- Posture du **tripode** : assis, penché en avant, appui des mains sur cuisses\n"
                    "- Exacerbations : muscles respiratoires accessoires (SCM++), expiration "
                    "abdominale active"
                )),
            ]),
            SousPartie(lettre="B", titre="Phénotypes cliniques", rows=[
                FicheRow(concept="◆ Blue bloater vs Pink puffer", detail_md=(
                    "| Caractéristique | Blue bloater | Pink puffer |\n"
                    "|-----------------|--------------|-------------|\n"
                    "| Prédominance | Voies aériennes | Emphysème |\n"
                    "| Morphotype | Corpulent | Maigre, distendu |\n"
                    "| Hypoxémie | Franche, cyanose | Modérée |\n"
                    "| ICD | Fréquente | Absente |"
                )),
                FicheRow(concept="", detail_md=(
                    "- Description ancienne mais utile pour la pédagogie\n"
                    "- La plupart des patients ont un phénotype mixte"
                ), kind="a_retenir"),
            ]),
        ],
    )

    # ── PARTIE III : DIAGNOSTIC POSITIF (EFR) ──
    partie_iii = Partie(
        numero="III",
        titre="Diagnostic positif : EFR",
        sous_parties=[
            SousPartie(lettre="A", titre="Spirométrie", rows=[
                FicheRow(concept="★ TVO persistant", detail_md=(
                    "- **VEMS/CVF < 0,7** après bronchodilatateur\n"
                    "- Réversibilité significative possible (mais non complète)"
                )),
                FicheRow(concept="", detail_md=(
                    "- ⚠ **Réversibilité complète** (VEMS/CVF > 0,7 + normalisation VEMS) "
                    "**exclut la BPCO** → orienter vers asthme"
                ), kind="piege"),
            ]),
            SousPartie(lettre="B", titre="Sévérité et explorations complémentaires", rows=[
                FicheRow(concept="◆ Sévérité GOLD", detail_md=(
                    "| Stade | VEMS post-BD |\n"
                    "|-------|--------------|\n"
                    "| GOLD 1 (léger) | ≥ 80 % |\n"
                    "| GOLD 2 (modéré) | 50-79 % |\n"
                    "| GOLD 3 (sévère) | 30-49 % |\n"
                    "| GOLD 4 (très sévère) | < 30 % |"
                )),
                FicheRow(concept="Pléthysmographie", detail_md=(
                    "- Mesure des volumes statiques : **VR**, CRF, CPT\n"
                    "- Distension pulmonaire : augmentation VR avec VR/CPT élevé"
                )),
                FicheRow(concept="Transfert du CO", detail_md=(
                    "- Reflète la surface d'échanges gazeux disponible\n"
                    "- Pathologique : **DLCO < 70 %** de la valeur prédite\n"
                    "- Évalue la destruction alvéolaire (emphysème)"
                )),
            ]),
        ],
    )

    # ── PARTIE IV : ÉVALUATION ET PRISE EN CHARGE ──
    partie_iv = Partie(
        numero="IV",
        titre="Évaluation et prise en charge au long cours",
        sous_parties=[
            SousPartie(lettre="A", titre="Bilan, mesures générales et vaccinations", rows=[
                FicheRow(concept="Bilan initial", detail_md=(
                    "- EFR + score **GOLD**\n"
                    "- NFS (polyglobulie → IRC), iono, créatinine\n"
                    "- Bilan nutritionnel (dénutrition = mauvais pronostic)\n"
                    "- **GDS** : recherche d'IRC\n"
                    "- RXT (recherche cancer/anomalies), TDM non systématique\n"
                    "- ECG + ETT si signes cardiaques (cœur pulmonaire chronique)"
                )),
                FicheRow(concept="★ Mesures générales", detail_md=(
                    "- **Sevrage tabagique +++** : seule mesure interrompant la progression\n"
                    "- ALD si : PaO2 < 60 mmHg, PaCO2 > 50 mmHg ou VEMS < 50 %\n"
                    "- Activité physique régulière, alimentation équilibrée"
                )),
                FicheRow(concept="★ Vaccinations", detail_md=(
                    "- **Anti-grippale** : tous les ans\n"
                    "- **Anti-pneumococcique** : tous les 5 ans"
                )),
            ]),
            SousPartie(lettre="B", titre="Traitement pharmacologique et réhabilitation", rows=[
                FicheRow(concept="◆ BDLA inhalés", detail_md=(
                    "- **B2-mimétiques LDA** et/ou **anticholinergiques LDA** :\n"
                    "  - Anticholinergiques LDA plus efficaces pour réduire les exacerbations\n"
                    "- **CDA** « à la demande » si dyspnée\n"
                    "- **CSI en association** avec BDLA si VEMS < 70 % + exacerbations > 2/an\n"
                    "- Ne pas prescrire d'antitussifs"
                )),
                FicheRow(concept="", detail_md=(
                    "- ⚠ **CSI seuls** : **NON indiqués** dans la BPCO (≠ asthme)\n"
                    "- ⚠ **Corticothérapie orale au long cours** : **NON indiquée**"
                ), kind="piege"),
                FicheRow(concept="◆ Réhabilitation respiratoire", detail_md=(
                    "- Dès le **stade II** si dyspnée / diminution tolérance à l'exercice\n"
                    "- Multidisciplinaire :\n"
                    "  - Optimisation thérapeutique + éducation\n"
                    "  - Kinésithérapie (drainage, renforcement, endurance)\n"
                    "  - Prise en charge psychosociale et nutritionnelle"
                )),
                FicheRow(concept="★ Stade IV", detail_md=(
                    "- **OLD** si IRC documentée\n"
                    "- **VNI nocturne** si SAS associé ou IRC hypercapnique grave\n"
                    "- < 65 ans : **transplantation pulmonaire**"
                )),
            ]),
        ],
    )

    # ── PARTIE V : EXACERBATIONS ──
    partie_v = Partie(
        numero="V",
        titre="Exacerbations de BPCO",
        sous_parties=[
            SousPartie(lettre="A", titre="Définition et étiologies", rows=[
                FicheRow(concept="★ Définition", detail_md=(
                    "- Événement aigu : aggravation > **24 h** des symptômes respiratoires "
                    "→ modification thérapeutique\n"
                    "- **Critères d'Anthonisen** :\n"
                    "  - Augmentation du volume des expectorations\n"
                    "  - Augmentation de la purulence des expectorations\n"
                    "  - Augmentation de la dyspnée"
                )),
                FicheRow(concept="★ Étiologies", detail_md=(
                    "- **Infectieuse** le plus souvent :\n"
                    "  - Haemophilus influenzae\n"
                    "  - Streptococcus pneumoniae\n"
                    "  - Moraxella catarrhalis\n"
                    "  - Pseudomonas aeruginosa si VEMS < 50 % ou séjour hospitalier\n"
                    "- Cause environnementale (pollution)\n"
                    "- Non identifiée fréquemment"
                )),
            ]),
            SousPartie(lettre="B", titre="Prise en charge", rows=[
                FicheRow(concept="★ ◆ Traitement", detail_md=(
                    "- **Bronchodilatateurs** CDA inhalés (B2-mimétiques +/- anticholinergiques)\n"
                    "- **O2** : objectif SpO2 **88-92 %** (⚠ différent de l'asthme !)\n"
                    "- **ATB** si :\n"
                    "  - Expectoration purulente\n"
                    "  - BPCO très sévère (VEMS < 30 %)\n"
                    "  - Signes de gravité\n"
                    "- **Corticothérapie systémique** :\n"
                    "  - Domicile : 2e intention si pas d'amélioration après 48 h\n"
                    "  - Hôpital : < 40 mg/j pendant max 5 jours\n"
                    "- Kinésithérapie si encombrement, prophylaxie thrombose\n"
                    "- **VNI** en 1re intention si acidose respiratoire ; intubation si troubles "
                    "de conscience"
                )),
                FicheRow(concept="", detail_md=(
                    "- ⚠ Objectif SpO2 dans la BPCO : **88-92 %** (et non 93-95 % comme dans l'asthme)\n"
                    "- Risque d'aggraver une hypercapnie si O2 trop généreux"
                ), kind="piege"),
            ]),
        ],
    )

    # ── SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Comparaison Asthme vs BPCO", markdown=(
            "| Critère | Asthme | BPCO |\n"
            "|---------|--------|------|\n"
            "| Début | Jeune | > 40 ans |\n"
            "| Tabac | Variable | Constant |\n"
            "| Réversibilité TVO | **Complète** | **Incomplète** |\n"
            "| Cible SpO2 urgence | 93-95 % | **88-92 %** |\n"
            "| CSI seul | Indication 1re intention | **Contre-indiqué** |\n"
            "| CTC PO longue durée | Non | **Non** |"
        )),
        TableauSynthese(titre="Stades GOLD et conduite", markdown=(
            "| Stade | VEMS post-BD | Conduite |\n"
            "|-------|-------------|----------|\n"
            "| GOLD 1 (léger) | ≥ 80 % | Sevrage tabagique, BDCA si besoin |\n"
            "| GOLD 2 (modéré) | 50-79 % | BDLA + réhabilitation |\n"
            "| GOLD 3 (sévère) | 30-49 % | BDLA + CSI si exacerbations |\n"
            "| GOLD 4 (très sévère) | < 30 % | OLD, VNI, transplantation < 65 ans |"
        )),
        TableauSynthese(titre="Antibiothérapie des exacerbations", markdown=(
            "| Situation | Antibiotique | Durée |\n"
            "|-----------|--------------|-------|\n"
            "| Non sévère | Amoxicilline ± ac. clavulanique | 5-7 j |\n"
            "| Allergie | Pristinamycine | 5-7 j |\n"
            "| VEMS < 30 % ou comorbidité | Amox-clav ou C3G | 7 j |\n"
            "| Suspicion Pseudomonas | Couverture anti-Pseudomonas (avis spé.) | 7-14 j |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Prévalence | ~7,5 % | > 40 ans |\n"
        "| Bronchite chronique | > 3 mois/an × > 2 ans | Définition clinique |\n"
        "| Tabac (femme / homme) | > 15 PA / > 20 PA | Seuil de risque |\n"
        "| TVO BPCO | VEMS/CVF < 0,7 post-BD | Diagnostic |\n"
        "| GOLD 1 / 2 / 3 / 4 | ≥80 / 50-79 / 30-49 / <30 % | VEMS post-BD |\n"
        "| DLCO pathologique | < 70 % prédit | Atteinte emphysème |\n"
        "| Cible SpO2 exacerbation | **88-92 %** | Risque hypercapnie |\n"
        "| ALD critère gaz du sang | PaO2 < 60 et/ou PaCO2 > 50 | + VEMS < 50 % |\n"
        "| Corticothérapie hôpital | < 40 mg/j × max 5 j | Exacerbation |\n"
        "| Anthonisen | Volume + purulence + dyspnée | Critères exacerbation |"
    ))

    points_cles = [
        "BPCO = TVO **non complètement réversible** (VEMS/CVF < 0,7 post-BD)",
        "Tabac > 15 PA femme / 20 PA homme = FDR principal ; sevrage = seule mesure ralentissant l'évolution",
        "Réversibilité complète exclut la BPCO et oriente vers l'asthme",
        "Cible SpO2 en exacerbation : **88-92 %** (≠ 93-95 % asthme)",
        "**CSI seuls et corticothérapie orale au long cours : NON indiqués** dans la BPCO",
        "Vaccinations recommandées : antigrippale annuelle + antipneumococcique tous les 5 ans",
        "Anthonisen : volume + purulence + dyspnée = critères d'exacerbation",
        "Réhabilitation respiratoire dès le stade II avec dyspnée d'effort",
        "Stade IV : OLD, VNI, transplantation pulmonaire (< 65 ans)",
    ]

    fiche_eclair_md = (
        "**Définition** : TVO non complètement réversible (VEMS/CVF < 0,7 post-BD). "
        "Tabac principal FDR.\n\n"
        "**Entités** : bronchite chronique (toux > 3 mois/an × 2 ans, 50 % fumeurs) ; "
        "emphysème (destruction parois alvéolaires, sans fibrose).\n\n"
        "**Clinique** : dyspnée d'effort (mMRC), toux, expectoration. "
        "Distension : thorax en tonneau, signe de Hoover, tripode.\n\n"
        "**Diagnostic** : EFR — TVO post-BD, réversibilité incomplète. "
        "Stades GOLD selon VEMS post-BD (≥ 80 / 50-79 / 30-49 / < 30 %).\n\n"
        "**EFR complémentaire** : pléthysmographie (VR ↑, distension) ; "
        "DLCO < 70 % = emphysème.\n\n"
        "**PEC long cours** : sevrage tabagique (seule mesure efficace) ; "
        "BDLA (anticholinergiques > B2-mimétiques) ; vaccins (grippe/an + pneumo/5 ans).\n\n"
        "**CSI** : association BDLA seulement si VEMS < 70 % + exacerbations > 2/an. "
        "**CSI seul = NON. Corticothérapie orale long cours = NON.**\n\n"
        "**Réhabilitation** : dès stade II + dyspnée d'effort.\n\n"
        "**Stade IV** : OLD si PaO2 < 60 ; VNI nocturne ; transplantation si < 65 ans.\n\n"
        "**Exacerbation** : aggravation > 24 h. Anthonisen (volume + purulence + dyspnée). "
        "Germes : H. influenzae, S. pneumoniae, Moraxella ; Pseudomonas si VEMS < 50 %.\n\n"
        "**Traitement exacerbation** : BDCA, O2 **88-92 %**, ATB si expectoration purulente / "
        "VEMS < 30 % / gravité ; CTC < 40 mg × max 5 j ; VNI si acidose respiratoire."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="BPCO",
        annee="2025-2026",
        item="BPCO",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="BPCO",
        usage=UsageStats(),
    )


def _make_analyzed_image(path: Path, desc: str, concept: str, section: str,
                         fig_num: int, img_type: str = "schema") -> AnalyzedImage:
    """Crée une AnalyzedImage à partir d'un chemin d'image."""
    from PIL import Image
    try:
        with Image.open(str(path)) as img:
            width, height = img.size
    except Exception:
        width, height = 1200, 900

    return AnalyzedImage(
        source=ExtractedImage(
            data=b"", ext="png", page=fig_num, index=fig_num,
            width=width, height=height, sha=path.stem,
        ),
        description=desc, concept_lie=concept, pertinence=9,
        type=img_type, section_suggeree=section, saved_path=path,
        figure_number=fig_num,
    )


def _place_source_images(fiche: FicheData, figures_dir: Path) -> None:
    all_images = []
    for i, entry in enumerate(_SOURCE_IMAGES):
        path = figures_dir / entry["file"]
        if not path.exists():
            print(f"  [SKIP] {entry['file']} not found")
            continue
        img = _make_analyzed_image(
            path, entry["desc"], entry["concept"], entry["desc"],
            fig_num=i + 1, img_type=entry.get("type", "schema"),
        )
        all_images.append(img)
        pi, si = entry["partie"], entry["sp"]
        if pi < len(fiche.parties) and si < len(fiche.parties[pi].sous_parties):
            fiche.parties[pi].sous_parties[si].images.append(img)
    fiche.images = all_images


def main() -> None:
    fiche = build_fiche()

    figures_dir = PROJECT_ROOT / "output" / "figures"
    if figures_dir.exists():
        _place_source_images(fiche, figures_dir)
        print(f"Placed {len(fiche.images)} source images")

    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Medecine_generale_BPCO_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out} ({pdf_out.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()

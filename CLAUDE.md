# Major ECN — Spécification de génération de fiches

Ce document définit les règles absolues pour la génération de fiches de révision Major ECN.
Toute future génération DOIT respecter ces exigences sans exception.

---

## 1. Architecture du projet

```
inputs/                         # PDFs sources des cours (1 par spécialité)
Annales/                        # Annales EVC par code spécialité (.DOC Word 97)
assets/                         # Logo, fonts, templates HTML/CSS
src/major_ecn/                  # Pipeline (models, renderers, config)
scripts/generate_<slug>.py      # Un script par spécialité → FicheData → PDF
scripts/add_images_all.py       # Ajoute les images source et régénère les PDFs
scripts/validate_fiche.py       # Validation automatique avant rendu
output/fiches/                  # PDFs finaux
output/.work/<slug>/            # Fichiers intermédiaires (images, captions)
output/.extracted/<Spécialité>.txt  # Texte extrait des PDFs sources
output/.annales_txt/            # Texte extrait des annales + notions_mg.json
```

---

## 2. Format de sortie : le script Python structuré

Chaque fiche est un script `scripts/generate_<slug>.py` qui construit un objet `FicheData`
directement en Python. **Ne pas utiliser de markdown intermédiaire** — le passage
markdown → parser introduit des bugs de parsing et de structure.

### Structure obligatoire du script

```python
"""Génère la fiche exhaustive de <Spécialité>."""
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
        PlanPartie(numero="I", titre="...", sous_parties=[
            PlanSousPartie(lettre="A", titre="..."),
            PlanSousPartie(lettre="B", titre="..."),
        ]),
        # ... 4 à 7 PlanPartie max
    ]

    partie_i = Partie(numero="I", titre="...", sous_parties=[
        SousPartie(lettre="A", titre="...", rows=[
            FicheRow(concept="Nom du concept", detail_md=(
                "- **Mot-clé** : explication\n"
                "  - Sous-point\n"
                "    - Sous-sous-point"
            )),
            FicheRow(concept="", detail_md=(
                "- Notion essentielle à retenir"
            ), kind="a_retenir"),
        ]),
    ])

    # ... autres parties ...

    tableaux = [TableauSynthese(titre="...", markdown="| Col1 | Col2 |\n|---|---|\n| ... | ... |")]
    chiffres = TableauSynthese(titre="Chiffres-clés", markdown="...")
    points_cles = ["Point 1", "Point 2"]
    fiche_eclair_md = "- Notion 1\n- Notion 2"

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="<Spécialité>",
        annee="2025-2026",
        item="Items ECN identifiés",
        plan=plan,
        parties=[partie_i, ...],
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
    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Medecine_generale_<Slug>_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()
```

---

## 3. Structure d'une fiche

### Page de garde
- **Matière** : toujours `"Médecine Générale"` (avec accents)
- **Nom du cours** : nom de la spécialité (ex: `"Cardiologie"`, `"Psychiatrie"`)
- **Plan** : 4 à 7 grandes parties en chiffres romains (I à VII)
- **Légende** : ★ Déjà tombé aux EVC / ◆ Haut rendement / ⚠ Piège classique

### Corps (Parties et sous-parties)
- **4-7 grandes parties** (chiffres romains I-VII)
- **2-5 sous-parties** par partie (lettres A-E)
- **3-6 FicheRow** par sous-partie
- **Cible : ~30 pages** par fiche PDF

### Éléments d'un FicheRow

| Type | Code | Rendu |
|------|------|-------|
| Ligne standard | `FicheRow(concept="Nom", detail_md="...")` | Concept à gauche (gras), détail à droite |
| Encadré à retenir | `FicheRow(concept="", detail_md="...", kind="a_retenir")` | Pleine largeur, fond gris, accent navy |
| Encadré piège | `FicheRow(concept="", detail_md="...", kind="piege")` | Pleine largeur, fond rose pâle, accent bordeaux |
| Encadré mnémo | `FicheRow(concept="", detail_md="...", kind="mnemo")` | Pleine largeur, fond crème, accent or |

### detail_md — Syntaxe Markdown

```python
FicheRow(concept="★ Paliers thérapeutiques", detail_md=(
    "- **Mot-clé** : explication courte et claire\n"
    "  - Sous-point avec détail\n"
    "    - Sous-sous-point si nécessaire\n"
    "- Deuxième point\n"
    "| Palier | Traitement |\n"           # Tableau comparatif intégré
    "|--------|------------|\n"
    "| 1 | BDCA à la demande |\n"
    "| 2 | **CSI faible dose** |"
))
```

Règles du detail_md :
- Sauts de ligne avec `\n` (dans des strings entre guillemets, PAS des f-strings)
- `**gras**` → rendu en gras bordeaux (mots-clés médicaux importants)
- Puces avec `- `, sous-puces avec `  - ` (2 espaces par niveau)
- Tableaux Markdown `| col1 | col2 |` pour les comparaisons et classifications
- Concaténation multi-lignes avec `("ligne1\n" "ligne2\n")`

### Synthèse (fin de fiche)
- **3-5 TableauSynthese** : tableaux comparatifs Markdown
- **1 tableau Chiffres-clés** : `| Paramètre | Valeur | Contexte |`
- **6-8 points à retenir** : les notions les plus importantes
- **Fiche éclair** : synthèse ultra-condensée en puces (1 page)

---

## 4. Marqueurs ★ ◆ ⚠ — Règles strictes

### ★ Déjà tombé aux EVC de médecine générale

**RÈGLE ABSOLUE : les ★ ne se placent que sur des notions vérifiées dans les annales EVC
de MÉDECINE GÉNÉRALE (code 71).** Jamais sur la base des annales de la spécialité elle-même.

#### Procédure de placement des ★

1. **Supprimer toutes les ★** des scripts existants
2. **Lire les annales** : `output/.annales_txt/medecine_generale_combined.txt`
   (texte combiné des 12 fichiers EVCF/EVCP code 71, 2009-2019)
3. **Pour chaque annale** (dossier clinique ou QCM) :
   a. Identifier la pathologie principale et les notions spécifiques testées
   b. Identifier la spécialité correspondante
   c. Ouvrir le script `generate_<specialite>.py`
   d. Chercher le FicheRow dont le concept correspond EXACTEMENT
   e. Ajouter `★ ` au début du concept
4. **Passer à l'annale suivante** et répéter
5. **Ne JAMAIS placer de ★** sur la base de mots génériques (« traitement », « urgence »,
   « hospitalisation ») — la correspondance doit être SPÉCIFIQUE à une pathologie

#### Fichier de référence : `output/.annales_txt/notions_mg.json`

Ce fichier structure les notions extraites des annales :
```json
[
  {
    "annale": "EVCF 2015 - Sujet 7",
    "pathologie": "SAOS",
    "notions": ["polysomnographie", "PPC", "benzodiazépines aggravent SAOS"],
    "specialite": "cardiologie",
    "contexte": "Patient obèse ronfleur somnolent"
  }
]
```

#### Spécialités sans ★ (jamais abordées en annales MG)

Ces spécialités n'apparaissent dans aucune annale de médecine générale code 71 :
- Gynécologie
- Ophtalmologie
- ORL
- Pédiatrie
- Pharmacologie (notions douleur/paliers traitées dans Rhumatologie)
- Médecine interne

**Ces fiches ont 0 ★. C'est normal et honnête.**

### ◆ Notion à haut rendement

Placer avec discernement (5-10 par fiche max). Réservé aux notions que tout étudiant
DOIT connaître pour l'examen, même si elles ne sont pas tombées aux EVC MG.

### ⚠ Piège classique

Placer dans le concept OU dans un FicheRow `kind="piege"`. Signale une erreur fréquente
ou une confusion classique.

---

## 5. Contenu — Règles de rédaction

### Fidélité à la source

- **UNIQUEMENT** les informations présentes dans le PDF source (`inputs/<Spécialité>.pdf`)
- **AUCUNE** information inventée, extrapolée ou ajoutée de mémoire
- Si le cours source est bref sur un sujet, la fiche l'est aussi

### Lisibilité

- La fiche doit être compréhensible en **première lecture** comme un cours
- Pas de résumé cryptique ni de mots-clés isolés incompréhensibles
- Phrases courtes mais claires avec le contexte nécessaire

### Longueur

- **Cible : ~30 pages** PDF par fiche
- 4-7 parties, 2-5 sous-parties, 3-6 lignes par sous-partie
- Ni trop long (pas de remplissage) ni trop court (pas de résumé)

### Encodage

- **UTF-8** obligatoire partout
- Accents français corrects : Épidémiologie, Étiologies, Généralités, Sévérité,
  Thérapeutique, Évaluation, Épanchement, Épilepsie (PAS Epidemiologie, Etiologie, etc.)
- `matiere="Médecine Générale"` (avec É et é)
- **Jamais** de caractères répétés (éééé, ààà) — bug d'encodage à corriger immédiatement
- **Jamais** de mojibake (Ã©, Ã¨)

---

## 6. Images

### Extraction

Les images sont extraites du PDF source par `add_images_all.py` :
- Taille minimale : 200×200 px
- Ratio max : 5:1 (filtre les bandeaux et lignes)
- Déduplication par SHA-1
- Maximum 25 images par fiche

### Analyse de pertinence

Le fichier `output/.work/<slug>/image_captions.json` classe chaque image :

```json
[
  {"page": 5, "relevant": true, "description": "Classification de Carpentier de l'IM",
   "concept": "IM classification", "section": "Valvulopathies", "type": "schema"},
  {"page": 8, "relevant": false}
]
```

**Pertinent** : schémas anatomiques, algorithmes, arbres décisionnels, ECG, imagerie
médicale (radio, scanner, IRM), classifications, scores, photos cliniques.

**Non pertinent** : logos, texte formaté, bandeaux, icônes, en-têtes de page.

### Placement

Les images sont placées dans la sous-partie correspondant à leur `section_suggeree`
(par similarité de titre). Fallback : placement proportionnel par numéro de page.

### Légendes

Description médicale en français (max 15 mots), PAS "Figure X — page Y".
Exemples :
- "Algorithme diagnostique de l'embolie pulmonaire"
- "Classification de Carpentier des insuffisances mitrales"
- "IRM cérébrale : séquences diffusion et FLAIR dans l'AVC ischémique"

---

## 7. Validation obligatoire

Avant chaque rendu PDF, exécuter :

```bash
python scripts/validate_fiche.py --fix scripts/generate_<slug>.py
```

Le validateur vérifie :
- Syntaxe Python valide
- Pas de caractères accentués répétés (éééé)
- Pas de mojibake
- Accents corrects sur les mots courants
- `matiere="Médecine Générale"` avec accents
- ★ <= 25 par fiche (alerte si dépassement)
- Structure FicheData complète (plan, parties, synthèse, éclair)

Pour valider toutes les fiches d'un coup :
```bash
python scripts/validate_fiche.py --all
```

---

## 8. Workflow de génération d'une nouvelle fiche

### Étape 1 — Extraction du texte source
```bash
# Extraire le texte du PDF dans output/.extracted/
python -c "
import fitz
doc = fitz.open('inputs/<Spécialité>.pdf')
text = '\n\n'.join(page.get_text() for page in doc)[:140000]
open('output/.extracted/<Spécialité>.txt', 'w', encoding='utf-8').write(text)
"
```

### Étape 2 — Rédaction du script Python
Créer `scripts/generate_<slug>.py` en lisant le texte source et en suivant
le format exact décrit en section 2. Le script de référence est
`scripts/generate_cardiologie.py`.

### Étape 3 — Validation
```bash
python scripts/validate_fiche.py --fix scripts/generate_<slug>.py
```

### Étape 4 — Placement des ★
Lire `output/.annales_txt/notions_mg.json` et placer les ★ uniquement sur
les concepts correspondant à des notions retrouvées dans les annales MG code 71.

### Étape 5 — Génération du PDF sans images
```bash
python scripts/generate_<slug>.py
```

### Étape 6 — Analyse des images et rendu final
```bash
python scripts/add_images_all.py
```

### Étape 7 — Vérification visuelle
Ouvrir le PDF et vérifier :
- Page de garde : plan I-VII, légende visible, accents corrects
- Tableaux : concept|détail bien structurés, gras bordeaux
- Images : pertinentes, bien placées, bien légendées
- ★ : uniquement sur les notions des annales MG
- Encodage : pas de caractères cassés

---

## 9. Commandes utiles

```bash
# Régénérer UNE fiche (sans images)
python scripts/generate_cardiologie.py

# Régénérer TOUTES les fiches avec images
python scripts/add_images_all.py

# Valider toutes les fiches
python scripts/validate_fiche.py --all

# Valider + corriger automatiquement
python scripts/validate_fiche.py --fix --all

# Extraire le texte d'un nouveau PDF source
python -c "import fitz; ..." (voir étape 1)

# Vérifier le comptage des ★
python -c "
from pathlib import Path
for s in sorted(Path('scripts').glob('generate_*.py')):
    text = s.read_text(encoding='utf-8')
    print(f'{s.stem}: {text.count(chr(9733))} étoiles')
"
```

---

## 10. Erreurs à ne JAMAIS commettre

| Erreur | Conséquence | Prévention |
|--------|-------------|------------|
| Placer des ★ sans vérifier les annales MG | Fausses ★, perte de confiance | Suivre la procédure section 4 |
| Utiliser du markdown intermédiaire au lieu de FicheData Python | Parsing cassé, structure dégradée | Toujours écrire du Python structuré |
| Oublier les accents français | « Epidemiologie » au lieu de « Épidémiologie » | validate_fiche.py --fix |
| Ajouter du contenu absent du PDF source | Hallucinations médicales dangereuses | Relire le source, comparer |
| Mettre les sous-parties (A, B, C) dans le plan de la page de garde | Plan trop long, légende masquée | Plan = chiffres romains uniquement |
| Images de logos/déco dans la fiche | Pollution visuelle | Filtrage image_captions.json |
| Plus de 30 ★ par fiche | ★ sans valeur si trop nombreuses | validate_fiche.py alerte si > 25 |
| Caractères répétés (éééé) | Texte illisible | validate_fiche.py détecte |

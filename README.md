# Major ECN Generator

> Transforme un dossier de **PDF de cours de médecine** en **fiches de révision
> « Major ECN »** haut de gamme, exportées simultanément en **PDF** et **Word (.docx)**.

`major-ecn-generator` est un logiciel en ligne de commande (CLI) pour macOS qui
lit un dossier de PDF de cours, les retravaille avec l'IA Claude (Anthropic) en
trois étapes (plan → rédaction exhaustive → tableaux de synthèse), analyse les
schémas par vision, puis produit des fiches élégantes selon une charte
« luxe médical ».

```
major-ecn /chemin/vers/Cardiologie
# → crée /chemin/vers/Fiches_Major_ECN/ avec un .pdf et un .docx par cours
```

---

## ✨ Fonctionnalités

- **Pipeline IA en 3 étapes** : plan détaillé, rédaction exhaustive partie par
  partie, tableaux de synthèse — avec partage de contexte et *prompt caching*.
- **Analyse d'images par vision** : chaque schéma du PDF est noté ; seuls les
  plus pertinents (≥ 6/10) sont conservés et replacés dans la bonne section.
- **Double export** : PDF (WeasyPrint) et Word (python-docx), mise en page
  équivalente.
- **Traitement par lot parallélisé** : 4 à 8 PDF simultanés, barre de
  progression avec ETA et coût API en temps réel.
- **Robustesse** : un PDF en échec n'interrompt pas le lot ; retry automatique
  sur erreurs API transitoires ; repli OCR pour les PDF scannés.
- **Charte « luxe médical »** : rouge signature `#E11D48`, or, crème, polices
  Playfair Display / Cormorant Garamond / Inter.

---

## 📦 Installation (macOS)

### Installation en une commande

```bash
git clone <repo> major-ecn-generator
cd major-ecn-generator
./install.sh
```

Le script `install.sh` installe Homebrew (si absent), les bibliothèques système
nécessaires, `uv`, l'environnement virtuel Python et le paquet.

### Installation manuelle

1. **Bibliothèques système** (WeasyPrint + OCR) :

   ```bash
   brew install pango cairo gdk-pixbuf libffi tesseract tesseract-lang poppler
   ```

2. **Environnement Python 3.11+** :

   ```bash
   uv venv --python 3.11 .venv
   uv pip install --python .venv/bin/python -e ".[dev]"
   # ou, sans uv :
   python3.11 -m venv .venv && source .venv/bin/activate && pip install -e ".[dev]"
   ```

3. **Configuration** :

   ```bash
   cp .env.example .env
   # puis éditez .env pour renseigner ANTHROPIC_API_KEY
   ```

---

## ⚙️ Configuration

La configuration se fait via le fichier `.env` (voir `.env.example`) :

| Variable                   | Rôle                                            | Défaut             |
|----------------------------|-------------------------------------------------|--------------------|
| `ANTHROPIC_API_KEY`        | Clé API Anthropic (**obligatoire**)             | —                  |
| `MAJOR_ECN_WRITER_MODEL`   | Modèle de rédaction                             | `claude-opus-4-5`  |
| `MAJOR_ECN_VISION_MODEL`   | Modèle d'analyse d'images                       | `claude-sonnet-4-5`|
| `MAJOR_ECN_YEAR`           | Année universitaire affichée                    | `2025-2026`        |
| `MAJOR_ECN_CONCURRENCY`    | PDF traités en parallèle (1-8)                  | `4`                |
| `MAJOR_ECN_MAX_INPUT_CHARS`| Caractères de cours max envoyés à l'IA          | `140000`           |
| `MAJOR_ECN_MAX_IMAGES`     | Images analysées max par cours                  | `40`               |

### Logo & polices

- **Logo** : placez votre logo dans `assets/logo_major_ecn.png`. Un placeholder
  est généré automatiquement par `install.sh` (ou via
  `python scripts/generate_placeholder_logo.py`).
- **Polices** : déposez les fichiers `.ttf` dans `assets/fonts/`
  (voir `assets/fonts/README.md`). En leur absence, des polices de repli sont
  utilisées.

---

## 🚀 Utilisation

```bash
# Le nom du dossier = la matière
major-ecn /chemin/vers/Cardiologie
```

### Options

| Option                  | Description                                              |
|-------------------------|----------------------------------------------------------|
| `-r`, `--recursive`     | Parcourt aussi les sous-dossiers                          |
| `--year ANNÉE`          | Année universitaire affichée                              |
| `-o`, `--output DIR`    | Dossier de sortie (défaut : `../Fiches_Major_ECN`)        |
| `-c`, `--concurrency N` | Nombre de PDF traités en parallèle (1-8)                  |
| `-l`, `--limit N`       | Ne traite que les N premiers PDF                          |
| `--no-pdf`              | N'exporte pas le PDF                                      |
| `--no-docx`             | N'exporte pas le DOCX                                     |
| `-v`, `--verbose`       | Logs détaillés                                            |

### Exemples

```bash
major-ecn ~/Cours/Pneumologie --year 2025-2026
major-ecn ~/Cours/Cardiologie --recursive --concurrency 6
major-ecn ~/Cours/Cardiologie --limit 5 --verbose
```

### Sorties

Pour chaque PDF, deux fichiers sont créés dans `Fiches_Major_ECN/` :

```
Cardiologie_Hypertension-Arterielle_2025-2026.pdf
Cardiologie_Hypertension-Arterielle_2025-2026.docx
```

Un journal détaillé est écrit dans `logs/run_<timestamp>.log`.

---

## 🧱 Architecture

```
src/major_ecn/
├── cli.py             # Point d'entrée Typer
├── config.py          # Charte, modèles, paramètres
├── models.py          # Modèles de données (FicheData…)
├── prompts.py         # Prompts des 3 étapes + vision
├── pdf_extractor.py   # Extraction texte + images (PyMuPDF, OCR)
├── ai_processor.py    # Pipeline IA en 3 étapes (chaining + caching)
├── image_analyzer.py  # Scoring des images par Claude Vision
├── content_builder.py # Assemblage + parsing en FicheData
├── html_renderer.py   # Markdown → HTML (Jinja2)
├── pdf_generator.py   # HTML → PDF (WeasyPrint)
├── docx_generator.py  # FicheData → DOCX (python-docx)
├── batch_runner.py    # Orchestration parallèle (asyncio)
└── utils/             # logger, slugify, retry
```

### Pipeline (par PDF)

1. Extraction du texte et des images (repli OCR si PDF scanné).
2. Étape 1 IA — plan détaillé + nom du cours.
3. Analyse vision des images (en parallèle des étapes suivantes).
4. Étape 2 IA — rédaction exhaustive partie par partie.
5. Étape 3 IA — tableaux de synthèse + points à retenir.
6. Placement des images pertinentes dans les sections.
7. Rendu HTML, puis export PDF et DOCX.

---

## 🎨 Aperçu

Pour générer une fiche d'exemple (données fictives, sans appel API) :

```bash
python scripts/generate_example.py
# → examples/Cardiologie_Hypertension-Arterielle_2025-2026.pdf + .docx
```

---

## 🧪 Tests

```bash
.venv/bin/pytest        # ou : pytest
```

Les tests couvrent l'extraction PDF, le parsing du contenu IA et les
utilitaires. Ils ne nécessitent pas de clé API.

---

## 🔧 Dépannage

| Problème                                        | Solution                                                                 |
|-------------------------------------------------|--------------------------------------------------------------------------|
| `WeasyPrint indisponible — bibliothèques…`      | `brew install pango cairo gdk-pixbuf libffi`                              |
| `clé API Anthropic manquante`                   | Renseignez `ANTHROPIC_API_KEY` dans `.env`                                |
| PDF scanné non lu                               | Installez l'OCR : `brew install tesseract tesseract-lang poppler`         |
| Rendu de police incorrect                       | Déposez les `.ttf` dans `assets/fonts/` (voir le README du dossier)       |
| Erreurs `429` répétées                          | Réduisez `--concurrency` ou `MAJOR_ECN_CONCURRENCY`                       |
| Coût API trop élevé                             | Réduisez `MAJOR_ECN_MAX_INPUT_CHARS` et `MAJOR_ECN_MAX_IMAGES`            |

---

## 📄 Licence

MIT.

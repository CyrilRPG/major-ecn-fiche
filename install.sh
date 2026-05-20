#!/usr/bin/env bash
# ──────────────────────────────────────────────────────────────────────────────
#  Major ECN Generator — Installation macOS (one-shot)
#  Usage :  ./install.sh
# ──────────────────────────────────────────────────────────────────────────────
set -euo pipefail

BOLD="\033[1m"; RED="\033[0;31m"; GREEN="\033[0;32m"; YELLOW="\033[0;33m"; NC="\033[0m"
info()  { echo -e "${BOLD}▸${NC} $1"; }
ok()    { echo -e "${GREEN}✓${NC} $1"; }
warn()  { echo -e "${YELLOW}!${NC} $1"; }
fail()  { echo -e "${RED}✗${NC} $1"; exit 1; }

echo -e "${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BOLD}  Major ECN Generator — Installation${NC}"
echo -e "${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# ── 1. Homebrew ───────────────────────────────────────────────────────────────
if ! command -v brew >/dev/null 2>&1; then
  warn "Homebrew introuvable — installation…"
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi
ok "Homebrew présent"

# ── 2. Dépendances système (WeasyPrint + OCR) ─────────────────────────────────
info "Installation des bibliothèques système (Pango / Cairo / Tesseract / Poppler)…"
brew install pango cairo gdk-pixbuf libffi tesseract tesseract-lang poppler >/dev/null 2>&1 || \
  warn "Certaines formules étaient déjà installées."
ok "Dépendances système prêtes"

# ── 3. Gestionnaire de paquets Python (uv de préférence) ──────────────────────
if ! command -v uv >/dev/null 2>&1; then
  warn "uv introuvable — installation…"
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi
ok "uv présent"

# ── 4. Environnement virtuel + dépendances Python ─────────────────────────────
info "Création de l'environnement virtuel et installation du paquet…"
uv venv --python 3.11 .venv
uv pip install --python .venv/bin/python -e ".[dev]"
ok "Paquet 'major-ecn-generator' installé en mode editable"

# ── 5. Fichier de configuration ───────────────────────────────────────────────
if [ ! -f .env ]; then
  cp .env.example .env
  warn "Fichier .env créé — éditez-le pour renseigner ANTHROPIC_API_KEY."
else
  ok "Fichier .env déjà présent"
fi

# ── 6. Logo placeholder ───────────────────────────────────────────────────────
if [ ! -f assets/logo_major_ecn.png ]; then
  info "Génération du logo placeholder…"
  .venv/bin/python scripts/generate_placeholder_logo.py || warn "Placeholder non généré."
fi

echo
echo -e "${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
ok "Installation terminée."
echo
echo -e "  Activez l'environnement :  ${BOLD}source .venv/bin/activate${NC}"
echo -e "  Renseignez la clé API   :  ${BOLD}\$EDITOR .env${NC}"
echo -e "  Lancez une génération   :  ${BOLD}major-ecn /chemin/vers/Cardiologie${NC}"
echo -e "${BOLD}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

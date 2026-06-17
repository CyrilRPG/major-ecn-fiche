"""Validation automatique d'un script generate_*.py avant rendu PDF.

Vérifie :
  1. Syntaxe Python valide
  2. Pas de bugs d'encodage (caractères répétés, mojibake)
  3. Accents français corrects sur les mots courants
  4. matiere = "Médecine Générale" avec accents
  5. ★ non abusives (max 25 par fiche, alerte si > 25)
  6. Pas de ★ sans vérification annales (alerte informative)
  7. Structure FicheData complète (plan, parties, synthèse, éclair)

Usage :
    python scripts/validate_fiche.py scripts/generate_cardiologie.py
    python scripts/validate_fiche.py --all          # valide tous les scripts
    python scripts/validate_fiche.py --fix <script>  # corrige automatiquement
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Mots courants qui doivent avoir des accents
ACCENT_FIXES = {
    "Epidemiologie": "Épidémiologie",
    "Etiologie": "Étiologie",
    "Etiologies": "Étiologies",
    "Generalites": "Généralités",
    "Severite": "Sévérité",
    "Therapeutique": "Thérapeutique",
    "Therapeutiques": "Thérapeutiques",
    "Evaluation": "Évaluation",
    "Epanchement": "Épanchement",
    "Epilepsie": "Épilepsie",
    "Etiopathogenie": "Étiopathogénie",
    "Echographie": "Échographie",
    "Electrocardiogramme": "Électrocardiogramme",
}

MAX_STARS = 25  # Alerte si plus de 25 ★ par fiche


class ValidationResult:
    def __init__(self, script_path: Path):
        self.path = script_path
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.fixes_applied: list[str] = []

    @property
    def ok(self) -> bool:
        return len(self.errors) == 0

    def report(self) -> str:
        name = self.path.stem.replace("generate_", "")
        lines = [f"{'✅' if self.ok else '❌'} {name}"]
        for e in self.errors:
            lines.append(f"  ERREUR: {e}")
        for w in self.warnings:
            lines.append(f"  ALERTE: {w}")
        for f in self.fixes_applied:
            lines.append(f"  CORRIGÉ: {f}")
        return "\n".join(lines)


def validate(script_path: Path, fix: bool = False) -> ValidationResult:
    """Valide un script generate_*.py et optionnellement corrige les problèmes."""
    result = ValidationResult(script_path)

    if not script_path.exists():
        result.errors.append(f"Fichier introuvable : {script_path}")
        return result

    text = script_path.read_text(encoding="utf-8")
    new_text = text

    # 1. Syntaxe Python
    try:
        ast.parse(text)
    except SyntaxError as e:
        result.errors.append(f"Erreur de syntaxe ligne {e.lineno}: {e.msg}")

    # 2. Caractères répétés (éééé, ààà, etc.)
    repeated = re.findall(r"([éèêëàâùûîïôç])\1{2,}", text)
    if repeated:
        result.errors.append(
            f"{len(repeated)} caractères accentués répétés (ex: éééé)"
        )
        if fix:
            new_text = re.sub(
                r"([éèêëàâùûîïôç])\1{2,}",
                lambda m: m.group(1).upper(),
                new_text,
            )
            result.fixes_applied.append("Caractères répétés corrigés")

    # 3. Mojibake (UTF-8 mal décodé)
    mojibake = re.findall(r"Ã[©¨\x20®´¹]|Ã¢|Ã§|Ã‰|Ã¼", text)
    if mojibake:
        result.errors.append(f"{len(mojibake)} séquences mojibake détectées")

    # 4. Accents manquants dans les titres
    for wrong, correct in ACCENT_FIXES.items():
        # Cherche le mot sans accent dans un contexte de titre (entre guillemets)
        if re.search(rf'"{wrong}"', text) or re.search(rf"'{wrong}'", text):
            result.warnings.append(f'Accent manquant : "{wrong}" → "{correct}"')
            if fix:
                new_text = new_text.replace(f'"{wrong}"', f'"{correct}"')
                new_text = new_text.replace(f"'{wrong}'", f"'{correct}'")
                result.fixes_applied.append(f"{wrong} → {correct}")

    # 5. matiere sans accents
    if "Medecine Generale" in text and "Médecine Générale" not in text:
        result.errors.append('matiere="Medecine Generale" sans accents')
        if fix:
            new_text = new_text.replace(
                '"Medecine Generale"', '"Médecine Générale"'
            )
            result.fixes_applied.append("Accents ajoutés sur matiere")

    # 6. Comptage ★
    star_count = text.count("★")
    if star_count > MAX_STARS:
        result.warnings.append(
            f"{star_count} ★ détectées (max recommandé : {MAX_STARS}). "
            "Vérifier avec les annales MG code 71."
        )
    elif star_count == 0:
        result.warnings.append(
            "Aucune ★ détectée. Vérifier si des notions tombées aux EVC MG "
            "code 71 sont présentes."
        )

    # 7. Structure minimale
    for required in ["FicheData", "PlanPartie", "Partie", "SousPartie", "FicheRow"]:
        if required not in text:
            result.errors.append(f"Import/utilisation de {required} manquant")
    if "tableaux" not in text.lower() and "TableauSynthese" not in text:
        result.warnings.append("Pas de tableaux de synthèse détectés")
    if "fiche_eclair" not in text and "eclair" not in text.lower():
        result.warnings.append("Pas de fiche éclair détectée")

    # Appliquer les corrections
    if fix and new_text != text:
        script_path.write_text(new_text, encoding="utf-8")

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python scripts/validate_fiche.py scripts/generate_<slug>.py")
        print("  python scripts/validate_fiche.py --all")
        print("  python scripts/validate_fiche.py --fix scripts/generate_<slug>.py")
        print("  python scripts/validate_fiche.py --fix --all")
        sys.exit(1)

    fix_mode = "--fix" in sys.argv
    all_mode = "--all" in sys.argv

    if all_mode:
        scripts = sorted(
            (PROJECT_ROOT / "scripts").glob("generate_*.py")
        )
        scripts = [
            s for s in scripts
            if s.name not in ("generate_all.py", "generate_pneumologie.py")
        ]
    else:
        scripts = [
            Path(a) for a in sys.argv[1:]
            if not a.startswith("--") and a.endswith(".py")
        ]

    if not scripts:
        print("Aucun script à valider.")
        sys.exit(1)

    errors_total = 0
    for script in scripts:
        result = validate(script, fix=fix_mode)
        print(result.report())
        errors_total += len(result.errors)

    print(f"\n{'═' * 50}")
    print(f"{len(scripts)} scripts validés, {errors_total} erreur(s)")
    if fix_mode:
        print("Mode --fix : corrections appliquées automatiquement")

    sys.exit(1 if errors_total > 0 else 0)


if __name__ == "__main__":
    main()

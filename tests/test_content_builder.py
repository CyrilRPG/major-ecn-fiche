"""Tests du parsing et de l'assemblage du contenu IA."""

from __future__ import annotations

from major_ecn.content_builder import (
    _normalize_indentation,
    output_basename,
    parse_plan,
    parse_section,
    parse_synthesis,
)

PLAN_MD = """\
I. **Définition et épidémiologie** : Cadre général de la maladie.
   A. **Définitions** : Seuils et critères.
   B. **Épidémiologie** : Prévalence et facteurs de risque.

II. **Diagnostic** : Démarche diagnostique.
   A. **Examen clinique** : Signes et symptômes.
"""

SECTION_MD = """\
I. **Définition et épidémiologie**
   A. **Définitions**
      - **HTA** : pression artérielle élevée
        - seuil de 140/90 mmHg
      - **Confirmation** : mesures répétées
   B. **Épidémiologie**
      - **Prévalence** : environ 30 %
"""

SYNTHESIS_MD = """\
### Grades de sévérité
| Grade | PAS | PAD |
|-------|-----|-----|
| 1 | 140-159 | 90-99 |
| 2 | 160-179 | 100-109 |

### POINTS À RETENIR ABSOLUMENT
- L'HTA se définit par une PA ≥ 140/90.
- La MAPA confirme le diagnostic.
- Le traitement combine mesures et médicaments.
"""


def test_parse_plan_structure() -> None:
    parties = parse_plan(PLAN_MD)
    assert len(parties) == 2
    assert parties[0].numero == "I"
    assert parties[0].titre == "Définition et épidémiologie"
    assert parties[0].resume.startswith("Cadre général")
    assert len(parties[0].sous_parties) == 2
    assert parties[0].sous_parties[1].titre == "Épidémiologie"
    assert parties[1].numero == "II"


def test_parse_section_structure() -> None:
    partie = parse_section(SECTION_MD, "I", "Repli")
    assert partie.titre == "Définition et épidémiologie"
    assert len(partie.sous_parties) == 2
    assert partie.sous_parties[0].lettre == "A"
    assert partie.sous_parties[0].titre == "Définitions"
    assert "HTA" in partie.sous_parties[0].corps_md
    assert partie.sous_parties[1].titre == "Épidémiologie"


def test_parse_section_fallback_without_subparts() -> None:
    partie = parse_section("- contenu brut sans sous-partie", "III", "Titre de repli")
    assert partie.titre == "Titre de repli"
    assert len(partie.sous_parties) == 1


def test_parse_synthesis() -> None:
    tableaux, points = parse_synthesis(SYNTHESIS_MD)
    assert len(tableaux) == 1
    assert tableaux[0].titre == "Grades de sévérité"
    assert "|" in tableaux[0].markdown
    assert len(points) == 3
    assert points[0].startswith("L'HTA")


def test_normalize_indentation_levels() -> None:
    raw = "- niveau 1\n      - niveau 2\n            - niveau 3"
    normalized = _normalize_indentation(raw)
    lines = normalized.split("\n")
    assert lines[0] == "- niveau 1"
    assert lines[1] == "    - niveau 2"
    assert lines[2] == "        - niveau 3"


def test_output_basename() -> None:
    name = output_basename("Cardiologie", "Hypertension Artérielle", "2025-2026")
    assert name == "Cardiologie_Hypertension-Arterielle_2025-2026"

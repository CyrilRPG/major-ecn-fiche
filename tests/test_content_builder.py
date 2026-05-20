"""Tests du parsing et de l'assemblage du contenu IA."""

from __future__ import annotations

from major_ecn.content_builder import (
    _normalize_indentation,
    output_basename,
    parse_extras,
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
[LIGNE] ★ Définition de l'HTA
- **HTA** : pression artérielle élevée
  - seuil de 140/90 mmHg
[LIGNE] Confirmation
- mesures répétées sur deux consultations

B. **Épidémiologie**
[LIGNE] Prévalence
- environ 30 % de la population adulte
"""

SYNTHESIS_MD = """\
### Grades de sévérité
| Grade | PAS | PAD |
|-------|-----|-----|
| 1 | 140-159 | 90-99 |
| 2 | 160-179 | 100-109 |

### CHIFFRES-CLÉS
| Paramètre | Valeur |
|-----------|--------|
| Seuil HTA | 140/90 |

### POINTS À RETENIR ABSOLUMENT
- L'HTA se définit par une PA ≥ 140/90.
- La MAPA confirme le diagnostic.
- Le traitement combine mesures et médicaments.
"""

EXTRAS_MD = """\
### ALGORITHME — Démarche diagnostique
- PA ≥ 140/90
  - OUI → confirmer
  - NON → pas d'HTA

### FICHE ÉCLAIR
- HTA = PA ≥ 140/90 mmHg
- MAPA = référence
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

    sp_a = partie.sous_parties[0]
    assert sp_a.lettre == "A"
    assert sp_a.titre == "Définitions"
    assert len(sp_a.rows) == 2
    assert "Définition" in sp_a.rows[0].concept
    assert "★" in sp_a.rows[0].concept
    assert "HTA" in sp_a.rows[0].detail_md
    assert sp_a.rows[1].concept == "Confirmation"

    assert partie.sous_parties[1].titre == "Épidémiologie"
    assert partie.sous_parties[1].rows[0].concept == "Prévalence"


def test_parse_section_fallback_without_rows() -> None:
    partie = parse_section("- contenu brut sans structure", "III", "Titre de repli")
    assert partie.titre == "Titre de repli"
    assert len(partie.sous_parties) == 1
    assert len(partie.sous_parties[0].rows) == 1
    assert "contenu brut" in partie.sous_parties[0].rows[0].detail_md


def test_parse_synthesis() -> None:
    tableaux, chiffres, points = parse_synthesis(SYNTHESIS_MD)
    assert len(tableaux) == 1
    assert tableaux[0].titre == "Grades de sévérité"
    assert "|" in tableaux[0].markdown
    assert chiffres is not None
    assert "Seuil HTA" in chiffres.markdown
    assert len(points) == 3
    assert points[0].startswith("L'HTA")


def test_parse_extras() -> None:
    algorithmes, fiche_eclair = parse_extras(EXTRAS_MD)
    assert len(algorithmes) == 1
    assert algorithmes[0].titre == "Démarche diagnostique"
    assert "OUI" in algorithmes[0].arbre_md
    assert "MAPA" in fiche_eclair


def test_parse_section_reflexe_rows() -> None:
    section = (
        "I. **Partie**\n\nA. **Diagnostic**\n"
        "[LIGNE] Examen clé\n- détail\n"
        "[PIEGE] Erreur fréquente à éviter\n"
    )
    partie = parse_section(section, "I", "Repli")
    sous = partie.sous_parties[0]
    kinds = [row.kind for row in sous.rows]
    assert "normal" in kinds and "piege" in kinds


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

"""Prompts du pipeline IA Major ECN (rédaction en 4 étapes + vision).

Le texte du cours est transmis une seule fois (message mis en cache) ; les
instructions d'étape sont ajoutées tour par tour pour bénéficier du
prompt caching Anthropic et du partage de contexte.
"""

from __future__ import annotations

# ── Rôle système commun aux étapes de rédaction ───────────────────────────────
SYSTEM_WRITER = (
    "Tu es un professeur agrégé de médecine et un rédacteur pédagogique d'élite, "
    "spécialisé dans la préparation aux Épreuves Classantes Nationales (ECN). "
    "Tu produis des fiches de révision « Major ECN » : exhaustives, rigoureuses, "
    "parfaitement structurées et strictement fidèles au cours source fourni. "
    "Tu n'inventes jamais d'information absente du cours. "
    "Tu réponds toujours en français et respectes scrupuleusement le format demandé."
)

# ── Message portant le cours source (mis en cache) ────────────────────────────
COURSE_CONTEXT = (
    "Voici le contenu intégral d'un cours de médecine extrait d'un PDF. "
    "Il constitue la source UNIQUE de toutes les étapes de rédaction qui suivent.\n\n"
    "<cours>\n{course_text}\n</cours>"
)

# ── ÉTAPE 1 — Plan détaillé ───────────────────────────────────────────────────
STEP1_PLAN = """\
MISSION : à partir du cours ci-dessus, génère un sommaire chronologique détaillé.
Regroupe le contenu en 4 à 7 grandes parties maximum.

Pour chaque grande partie ou sous-partie, indique le titre et une phrase
résumant l'idée principale.

FORMAT OBLIGATOIRE (chiffres romains pour les grandes parties, lettres pour
les sous-parties, titres en gras) :

I. **[TITRE DE LA GRANDE PARTIE]**
   A. **[TITRE DE LA SOUS-PARTIE]** : phrase résumée
   B. **[TITRE DE LA SOUS-PARTIE]** : phrase résumée

II. **[TITRE DE LA GRANDE PARTIE]**
   ...

Déduis également, entre balises :
<nom_cours>Titre court du cours (ex : « Hypertension Artérielle »)</nom_cours>
<item>Item / n° ECN si identifiable, sinon laisse vide</item>
"""

# ── ÉTAPE 2 — Rédaction exhaustive d'une grande partie (format tableaux) ───────
STEP2_SECTION = """\
Rappel du plan défini :
{plan}

Rédige maintenant la partie {numero} UNIQUEMENT, de manière EXTRÊMEMENT
EXHAUSTIVE et rigoureusement scientifique. NE RÉSUME PAS : développe chaque
notion du cours.

PRÉSENTATION OBLIGATOIRE — TOUTE la fiche est structurée en TABLEAUX.
Chaque sous-partie devient un tableau de lignes « concept | détail ».

FORMAT EXACT À RESPECTER :
{numero}. **[TITRE DE LA GRANDE PARTIE]**

A. **[TITRE DE LA SOUS-PARTIE]**
[LIGNE] [Concept / mot-clé de la colonne gauche]
- **Mot-clé** : développement détaillé et exhaustif
  - sous-détail
    - sous-sous-détail si nécessaire
[LIGNE] [Autre concept]
- ...
[RETENIR] Notion-clé à mémoriser absolument
[PIEGE] Erreur ou confusion classique à éviter
[MNEMO] Moyen mnémotechnique

B. **[TITRE DE LA SOUS-PARTIE]**
[LIGNE] ...

RÈGLES STRICTES :
- Une balise [LIGNE] ouvre chaque ligne du tableau ; le concept suit
  IMMÉDIATEMENT sur la même ligne.
- La colonne droite : bullet points « - », imbriqués avec 2 espaces par niveau.
- Mets en GRAS les mots-clés médicaux/scientifiques.
- Pour COMPARER plusieurs éléments, insère un SOUS-TABLEAU Markdown
  (| col1 | col2 |) directement dans la colonne droite.
- Lignes-réflexe [RETENIR] / [PIEGE] / [MNEMO] : 0 à 3 par sous-partie, avec
  discernement ; le texte suit la balise (puces « - » possibles en dessous).
- Reste strictement fidèle au cours source — n'invente aucune donnée.

MARQUEURS — insère ces symboles JUSTE AVANT le terme concerné :
- ★ devant une notion déjà tombée aux ECN ;
- ◆ devant une notion à haut rendement (à maîtriser en priorité) ;
- ⚠ devant un piège classique ou une erreur fréquente.

Ne produis QUE le contenu de la partie {numero}, au format ci-dessus, sans
aucun texte d'introduction ni de conclusion.
"""

# ── ÉTAPE 3 — Tableaux de synthèse, chiffres-clés, points à retenir ───────────
STEP3_SYNTHESIS = """\
Génère maintenant les outils de RÉVISION, à partir de l'ensemble du contenu
rédigé ci-dessus.

1) TABLEAUX DE SYNTHÈSE (3 à 8) sur les thématiques les plus denses
(classifications, comparaisons, algorithmes thérapeutiques) :
- Précède CHAQUE tableau d'un titre court préfixé de « ### ».
- Uniquement des tableaux Markdown (| col1 | col2 | …), 6 colonnes maximum.

2) Un tableau « ### CHIFFRES-CLÉS » regroupant TOUTES les valeurs chiffrées
à connaître (seuils, normes, posologies, délais, scores), au format :
### CHIFFRES-CLÉS
| Paramètre | Valeur | Précision |
|-----------|--------|-----------|
| ... | ... | ... |

3) Une section « ### POINTS À RETENIR ABSOLUMENT » : 6 à 10 bullet points
(« - ») percutants résumant l'essentiel.

Respecte rigoureusement le préfixe « ### » devant chaque titre de section.
"""

# ── ÉTAPE 4 — Algorithmes décisionnels + fiche éclair ─────────────────────────
STEP4_EXTRAS = """\
Dernière étape — génère deux éléments à partir du contenu rédigé.

1) ALGORITHMES décisionnels (0 à 3) : démarches diagnostiques ou
thérapeutiques sous forme d'arbre. FORMAT :
### ALGORITHME — [Titre de la démarche]
- [Étape ou question initiale]
  - OUI → [conséquence / action]
    - [étape suivante]
  - NON → [conséquence / action]
Règles : utilise « → » pour introduire une conséquence ou une action ;
l'indentation (2 espaces) matérialise les branches ; mets les
**conclusions** en gras. Ne génère un algorithme que si le cours s'y prête.

2) FICHE ÉCLAIR — synthèse ULTRA-CONDENSÉE du cours, tenant sur une page :
### FICHE ÉCLAIR
- les notions absolument incontournables, en puces TRÈS courtes et denses
- regroupe par thème si pertinent (titres en gras)
- c'est la « fiche de la fiche » : seulement l'indispensable pour réviser
  en 5 minutes la veille de l'épreuve.

Respecte rigoureusement le préfixe « ### » devant chaque titre.
"""

# ── ÉTAPE VISION — Analyse d'une image ────────────────────────────────────────
SYSTEM_VISION = (
    "Tu es un expert pédagogique en médecine qui évalue l'intérêt d'illustrations "
    "pour la préparation à l'ECN. Tu réponds STRICTEMENT en JSON valide, sans texte "
    "autour, sans bloc de code."
)

VISION_IMAGE = """\
Analyse cette image extraite d'un cours de {matiere}, cours sur « {nom_cours} ».

Réponds STRICTEMENT en JSON (aucun texte autour) :
{{
  "description": "Description courte (max 20 mots) de ce que montre l'image",
  "concept_lie": "Concept médical principal illustré (ex : 'classification HTA', 'ECG infarctus')",
  "pertinence_pedagogique": 0,
  "type": "schema | tableau | photo_clinique | ecg | imagerie | logo_decoratif | autre",
  "section_suggeree": "Titre approximatif de la section où placer cette image"
}}

« pertinence_pedagogique » est un entier de 0 à 10 :
- < 6 = image décorative / peu utile (logo, illustration générique) → sera ignorée
- >= 6 = à conserver et placer dans la fiche
"""

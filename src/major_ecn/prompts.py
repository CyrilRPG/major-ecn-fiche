"""Prompts du pipeline IA Major ECN (rédaction en 3 étapes + vision).

Le texte du cours est transmis une seule fois (message mis en cache) ; les
instructions d'étape sont ajoutées tour par tour pour bénéficier du
prompt caching Anthropic et du partage de contexte.
"""

from __future__ import annotations

# ── Rôle système commun aux 3 étapes de rédaction ─────────────────────────────
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

Pour chaque grande partie ou changement de thème, indique :
- Le titre de la section
- Une phrase résumant l'idée principale

Ne rentre pas dans les détails, donne-moi la structure squelette.
Regroupe les infos pour obtenir entre 4 et 7 grandes parties maximum.

FORMAT OBLIGATOIRE (titres et sous-titres en gras, chiffres romains pour les
grandes parties, lettres majuscules pour les sous-parties) :

I. **[TITRE DE LA GRANDE PARTIE]**
   A. **[TITRE DE LA SOUS-PARTIE]** : Phrase résumée
   B. **[TITRE DE LA SOUS-PARTIE]** : Phrase résumée

II. **[TITRE DE LA GRANDE PARTIE]**
   ...

Déduis également :
- Le NOM DU COURS (titre principal court, ex : « Hypertension Artérielle ») \
→ renvoie-le entre balises <nom_cours></nom_cours>
- Le NIVEAU/ITEM ECN si identifiable → renvoie-le entre balises <item></item>
"""

# ── ÉTAPE 2 — Rédaction exhaustive d'une grande partie (format tableaux) ───────
STEP2_SECTION = """\
Rappel du plan défini :
{plan}

Rédige maintenant la partie {numero} UNIQUEMENT, de manière EXTRÊMEMENT
EXHAUSTIVE et rigoureusement scientifique. NE RÉSUME PAS : développe chaque
notion du cours.

PRÉSENTATION OBLIGATOIRE — TOUTE la fiche est structurée en TABLEAUX.
Chaque sous-partie devient un tableau. Chaque ligne de tableau a :
- une COLONNE GAUCHE : un concept / mot-clé / thème court (1 à 5 mots) ;
- une COLONNE DROITE : le développement exhaustif en bullet points imbriqués.

FORMAT EXACT À RESPECTER :
{numero}. **[TITRE DE LA GRANDE PARTIE]**

A. **[TITRE DE LA SOUS-PARTIE]**
[LIGNE] [Concept de la colonne gauche]
- **Mot-clé** : développement détaillé et exhaustif
  - sous-détail
    - sous-sous-détail si nécessaire
[LIGNE] [Autre concept]
- ...

B. **[TITRE DE LA SOUS-PARTIE]**
[LIGNE] ...

RÈGLES STRICTES :
- Une balise [LIGNE] ouvre chaque ligne du tableau ; le concept de la colonne
  gauche suit IMMÉDIATEMENT sur la même ligne que [LIGNE].
- La colonne droite : bullet points « - », imbriqués avec 2 espaces par niveau.
- Mets en GRAS les mots-clés médicaux/scientifiques (structures, mécanismes,
  pathologies, valeurs chiffrées, classifications).
- Pour COMPARER plusieurs éléments, insère un SOUS-TABLEAU Markdown
  (| col1 | col2 |) directement dans la colonne droite.
- Reste strictement fidèle au cours source — n'invente aucune donnée.

MARQUEURS — insère ces symboles JUSTE AVANT le terme concerné :
- ★ devant une notion déjà tombée aux ECN ;
- ◆ devant une notion à haut rendement (à maîtriser en priorité) ;
- ⚠ devant un piège classique ou une erreur fréquente.
Utilise ces marqueurs avec discernement, uniquement là où c'est justifié.

Ne produis QUE le contenu de la partie {numero}, au format ci-dessus, sans
aucun texte d'introduction ni de conclusion.
"""

# ── ÉTAPE 3 — Tableaux de synthèse + points à retenir ─────────────────────────
STEP3_SYNTHESIS = """\
Nous arrivons à la phase finale. Génère des TABLEAUX DE SYNTHÈSE pour faciliter
la révision, à partir de l'ensemble du contenu rédigé ci-dessus.

Identifie les thématiques les plus complexes ou denses :
- Classifications
- Comparaisons (pathologies, traitements, mécanismes)
- Valeurs chiffrées clés
- Pathologies et traitements
- Algorithmes décisionnels

RÈGLES :
- Uniquement des tableaux Markdown (| col1 | col2 | col3 |)
- En-têtes de colonnes explicites et concis
- Maximum 6 colonnes par tableau
- Contenu rigoureux et fidèle au cours
- Précède CHAQUE tableau d'un titre court sur sa propre ligne, préfixé de « ### »
- Génère 3 à 8 tableaux maximum, sur les sujets les plus importants pour l'ECN

À LA FIN, ajoute une section « ### POINTS À RETENIR ABSOLUMENT » suivie de 5 à 10
bullet points (« - ») percutants résumant l'essentiel du cours.
"""

# ── ÉTAPE 4 — Analyse vision d'une image ──────────────────────────────────────
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

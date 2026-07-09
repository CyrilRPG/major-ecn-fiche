#!/usr/bin/env python3
"""Flashcards UE5 – Cours n°4 : Rôle du rein dans le bilan de l'eau.

Source : cours du 9 mars 2026, UE5 Voies Urinaires et Appareil Génital Masculin.
Contenu : FLASHCARDS EXHAUSTIVES uniquement (pas de fiche de cours, pas de QCM).
Sortie : output/Physiologie_Bilan_Eau_UE5C4_2025-2026.{pdf,docx}
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from major_ecn.models import (  # noqa: E402
    FicheData,
    FicheRow,
    Partie,
    PlanPartie,
    PlanSousPartie,
    SousPartie,
    TableauSynthese,
)


def _fc(concept: str, detail: str) -> FicheRow:
    """Flashcard normale : concept → détail."""
    return FicheRow(concept=concept, detail_md=detail)


def _key(detail: str) -> FicheRow:
    """Bannière À RETENIR."""
    return FicheRow(concept="", detail_md=detail, kind="a_retenir")


def _trap(detail: str) -> FicheRow:
    """Bannière PIÈGE."""
    return FicheRow(concept="", detail_md=detail, kind="piege")


def _mnemo(detail: str) -> FicheRow:
    """Bannière MNÉMOTECHNIQUE."""
    return FicheRow(concept="", detail_md=detail, kind="mnemo")


# ---------------------------------------------------------------------------
# Plan du cours
# ---------------------------------------------------------------------------
plan = [
    PlanPartie(
        "I", "Généralités – Règles de raisonnement",
        "Compartiments hydriques, osmolalité, règles fondamentales.",
        [
            PlanSousPartie("A", "Compartiments de l'eau", "Répartition 60 % / 1/3 EC / 2/3 IC."),
            PlanSousPartie("B", "Eau et osmolalité", "Définition, formules, natrémie."),
        ],
    ),
    PlanPartie(
        "II", "Bilan de l'eau : entrées et sorties",
        "Sources et élimination de l'eau ; rôle du rein.",
        [
            PlanSousPartie("A", "Entrées d'eau", "Eau endogène et exogène."),
            PlanSousPartie("B", "Sorties d'eau", "Extra-rénales et rénales."),
            PlanSousPartie("C", "Rein et excrétion d'eau", "Dissociation débit/osmoles."),
            PlanSousPartie("D", "Perméabilité à l'eau des segments du néphron", "AQP par segment."),
        ],
    ),
    PlanPartie(
        "III", "Concentration / Dilution de l'urine",
        "Gradient CP, ADH, multiplicateur à contre-courant.",
        [
            PlanSousPartie("A", "Gradient osmotique cortico-papillaire", "Création et maintien."),
            PlanSousPartie("B", "Hormone antidiurétique (ADH)", "Synthèse, action, diabète insipide."),
        ],
    ),
    PlanPartie(
        "IV", "Régulation du bilan de l'eau",
        "Stimuli de l'ADH et mise en jeu de la soif.",
        [
            PlanSousPartie("A", "Stimuli de la sécrétion d'ADH", "Osmolalité et volémie."),
            PlanSousPartie("B", "Mise en jeu de la soif", "Osmorécepteurs et angiotensine II."),
        ],
    ),
    PlanPartie(
        "V", "Modifications de la diurèse",
        "Situations physiologiques et pathologiques ; diurétiques.",
        [
            PlanSousPartie("A", "Modifications physiologiques", "Diurèse normale et antidiurèse."),
            PlanSousPartie("B", "Modifications pathologiques", "Diabète insipide, diurèse osmotique."),
            PlanSousPartie("C", "Diurétiques", "Mécanismes d'action."),
        ],
    ),
]

# ---------------------------------------------------------------------------
# Parties avec flashcards
# ---------------------------------------------------------------------------
parties = [

    # ════════════════════════════════════════════════════════════════════════
    Partie("I", "Généralités – Règles de raisonnement", [

        SousPartie("A", "Compartiments de l'eau et règles de base", [

            _fc("★ Eau corporelle totale",
                "- Représente **60 %** du poids corporel\n"
                "- Répartition :\n"
                "  - **1/3 extracellulaire (EC)** : liquide interstitiel (~15 %) + plasma (**3 L**)\n"
                "  - **2/3 intracellulaire (IC)** : compartiment le plus volumineux\n"
                "- Le plasma = reflet du milieu EC (ionogramme sanguin)"),

            _fc("◆ Échanges entre compartiments",
                "- EC ↔ IC : passifs via **aquaporines** (présentes dans toutes les cellules)\n"
                "- Sens du mouvement d'eau : toujours de l'osmolalité **la plus faible** vers la **plus élevée**\n"
                "- Équilibre très rapide par transfert d'eau"),

            _key("L'eau s'échange **passivement** entre les compartiments selon le gradient d'osmolalité. "
                 "La réabsorption d'eau dans le néphron est **TOUJOURS passive**."),

            _fc("★ Règle du compartiment IC",
                "- Dans le secteur IC : **nombre d'osmoles = constant** dans le temps\n"
                "- Conséquence : si l'osmolalité IC varie → c'est le **volume d'eau** qui a varié\n"
                "  (pas le nombre d'osmoles)\n"
                "- Cette règle **ne s'applique pas** au compartiment EC (osmoles ET volume peuvent varier)"),

            _trap("Ne pas confondre :\n"
                  "- **EC** : osmoles ET volume imprévisibles (toutes les perturbations arrivent par ce secteur)\n"
                  "- **IC** : seul le **volume d'eau** varie (osmoles fixes)\n"
                  "⇒ Si osmolalité IC varie → c'est le volume qui a changé"),

            _fc("★ Osmolalité extracellulaire = reflet de l'hydratation IC",
                "- Ce qu'on mesure / calcule → **osmolalité extracellulaire**\n"
                "- L'équilibre EC↔IC est atteint très rapidement\n"
                "- Donc : osmolalité EC = osmolalité IC (à l'équilibre)\n"
                "- Et comme les osmoles IC sont fixes : osmolalité EC reflète le **volume d'eau IC**"),
        ]),

        SousPartie("B", "Eau et osmolalité – formules clés", [

            _fc("★ Définition de l'osmolalité",
                "- **Osmolalité** = nombre d'osmoles / volume de solvant (eau)\n"
                "- L'organisme ne peut pas mesurer directement le contenu en eau\n"
                "- Ce qui est régulé : **l'osmolalité** (via osmorécepteurs)\n"
                "- Variable régulée = **homeostasie** : s'écarte très peu de sa valeur consigne"),

            _fc("★ Osmolalité plasmatique normale",
                "- Mesurée à l'osmomètre : **295 ± 5 mosm/kg H₂O** (≈ 300 par simplification)\n"
                "- Calculée à partir d'une prise de sang :\n"
                "  **2 × [Na⁺] + [glucose] + [urée]** ≈ **285–290 mosm/kg H₂O**\n"
                "  (glucose et urée ≈ 5 mmol/L chacun chez le sujet normal)\n"
                "- À l'état stable, toutes les osmolalités (EC et IC) sont égales ≈ 300 mosm/kg H₂O"),

            _fc("◆ Osmolalité efficace (tonicité)",
                "- = **2 × [Na⁺]** ≈ **280 mosm/kg H₂O** (2 × 140)\n"
                "- On exclut glucose et urée qui traversent librement les membranes biologiques\n"
                "  (sauf en pathologie : diabète → glucose ne traverse pas bien)\n"
                "- C'est la tonicité qui détermine vraiment les transferts d'eau entre compartiments"),

            _fc("★ La natrémie : ce qu'elle reflète",
                "- Natrémie = concentration plasmatique du sodium\n"
                "- Reflète le **volume intracellulaire** (via l'osmolalité EC)\n"
                "- **Ne reflète PAS le volume extracellulaire** (point MAJEUR)\n"
                "- Exemples :\n"
                "  - Natrémie 160 mmol/L → hyperosm plasmatique → **déshydratation IC**\n"
                "  - Natrémie 120 mmol/L → hypoosm plasmatique → **hyperhydratation IC**"),

            _key("**Natrémie = reflet de l'état d'hydratation intracellulaire** +++\n"
                 "Elle ne renseigne **jamais** sur le volume extracellulaire."),

            _fc("◆ Osmolalité et volume IC : exemple chiffré",
                "- Formule : Osmolalité = N osmoles (fixe IC) / Volume d'eau\n"
                "- Si osm = 280 au lieu de 300 → volume IC **augmenté** (eau IC en excès)\n"
                "- Si osm = 320 au lieu de 300 → volume IC **diminué** (eau IC insuffisante)\n"
                "→ Osmolalité IC varie = volume a varié (numérateur fixe)"),
        ]),
    ]),

    # ════════════════════════════════════════════════════════════════════════
    Partie("II", "Bilan de l'eau : entrées et sorties", [

        SousPartie("A", "Entrées d'eau", [

            _fc("◆ Eau endogène",
                "- Due au **métabolisme** : eau d'oxydation issue du catabolisme des protides, glucides, lipides\n"
                "- Quantité : environ **500 mL/j** → production **stable** et fixe"),

            _fc("◆ Eau exogène",
                "- Boissons + eau contenue dans l'alimentation\n"
                "- Variable : **1 à 3 L** par individu et par jour\n"
                "- Dépend des habitus et de l'**accès à l'eau**"),

            _fc("★ Populations vulnérables au défaut d'apport hydrique",
                "- **Nouveau-nés** : ne peuvent pas exprimer la soif\n"
                "- **Personnes âgées** : sensation de soif altérée → ne se rendent pas compte de la déshydratation\n"
                "⚠ Risque de déshydratation +++ dans ces deux populations\n"
                "→ Surveillance et apport hydrique régulier indispensables"),

            _fc("◆ Régulation des entrées",
                "- Par la **sensation de soif** (voir partie IV B)"),
        ]),

        SousPartie("B", "Sorties d'eau", [

            _fc("◆ Sorties extra-rénales (non régulées)",
                "- Cutanées (sueur), respiratoires, fèces (++ si diarrhée)\n"
                "- **Non contrôlées** : environ **500–800 mL/j**\n"
                "- Augmentent considérablement en cas de diarrhée ou de fièvre"),

            _fc("★ Sorties rénales (régulées)",
                "- Filtration glomérulaire : environ **180 L d'eau/j**\n"
                "- Volume uriné : environ **1,8 L/j** (100× moins = ~1 % du filtrat)\n"
                "- **Hautement régulées** par le rein qui adapte le volume d'eau excrété"),

            _key("Le rein est le seul organe capable de **réguler** la sortie d'eau. "
                 "Les pertes extra-rénales sont non contrôlées."),
        ]),

        SousPartie("C", "Rein et excrétion d'eau", [

            _fc("★ Principe fondamental : dissociation débit/osmoles",
                "- Le rein adapte le **volume d'urine** aux entrées d'eau\n"
                "- Objectif : maintenir l'osmolalité plasmatique constante\n"
                "- Le rein peut excréter le **même nombre d'osmoles** dans un volume très variable\n"
                "- Plage d'osmolalité urinaire : **60 → 1200 mosm/kg H₂O** (limites fixes chez l'homme)\n"
                "- Débit urinaire minimum : **0,5 L/j**"),

            _fc("◆ Charge osmolaire quotidienne",
                "- Excrétion quotidienne obligatoire : **~600 mosm/j** (urée, sulfates, phosphates)\n"
                "- Cette charge est excrétée même à jeun\n"
                "- Le débit urinaire est **dissocié** de la sortie des osmoles"),

            _mnemo("Pour retenir les limites rénales :\n"
                   "**60 à 1200** mosm/kg H₂O = ni plus, ni moins chez l'humain sain\n"
                   "↑ apports hydriques → ↑ débit urinaire, **osmoles stables**"),
        ]),

        SousPartie("D", "Perméabilité à l'eau des segments du néphron", [

            _fc("★ Tube contourné proximal (TCP)",
                "- **Extrêmement perméable** à l'eau : voie paracellulaire (PC) + **AQP1** en grande quantité\n"
                "- L'eau passe librement → grosse réabsorption d'eau\n"
                "- Réabsorption iso-osmotique (eau suit le Na⁺, osmolalité reste à 300)"),

            _fc("★ Branche descendante de l'anse de Henlé",
                "- **Perméable à l'eau** : présence d'**AQP1** → réabsorption d'eau possible\n"
                "- **Imperméable aux solutés** : pas de réabsorption de Cl⁻, Na⁺, etc."),

            _fc("★ Branche ascendante large de l'anse de Henlé",
                "- **IMPERMÉABLE à l'eau en toute circonstance** :\n"
                "  - Absence totale d'aquaporines\n"
                "  - Jonctions intercellulaires très serrées\n"
                "- **Perméable aux solutés** : réabsorption massive de **NaCl** via Na⁺/K⁺/2Cl⁻\n"
                "→ C'est ici que se crée l'effet élémentaire du gradient CP"),

            _fc("★ Tube contourné distal (TCD)",
                "- **Imperméable à l'eau** en toutes circonstances\n"
                "- Reste **perméable aux solutés** (réabsorption de Na⁺)"),

            _fc("★ Canal collecteur",
                "- Perméabilité variable, **dépendante de l'ADH** :\n"
                "  - **Sans ADH** → imperméable à l'eau (surface apicale lisse)\n"
                "  - **Avec ADH** → perméable à l'eau (insertion AQP2 en face apicale)\n"
                "- Face **basolatérale** : **AQP3 et AQP4** (constitutives, non dépendantes de l'ADH)\n"
                "- Face **apicale** : **AQP2** seulement si ADH présente"),

            _key("Seul le **canal collecteur** modifie sa perméabilité à l'eau selon l'ADH. "
                 "La branche ascendante large est **imperméable à l'eau en toute circonstance**."),

            _fc("◆ Quantités d'eau réabsorbées par segment",
                "- Filtration glomérulaire : **180 L/j**\n"
                "- TCP : **60–70 %** réabsorbés (iso-osmotique, osmolalité reste à 300 mosm)\n"
                "- Branche descendante anse de Henlé : **15–20 %** d'eau réabsorbée (pas de soluté)\n"
                "- Branche ascendante : **0 %** d'eau, réabsorption NaCl → osmolalité tubulaire ↓\n"
                "- TCD : osmolalité ≈ **150 mosm/kg H₂O**\n"
                "- Entrée collecteur : osmolalité ≈ **100 mosm/kg H₂O**\n"
                "- Canal collecteur : **12–20 %** (dépendant ADH)\n"
                "- **Urines finales : 1 % du filtrat**"),

            _fc("◆ Évolution de l'osmolalité tubulaire",
                "- TCP : reste à **300** (réabsorption iso-osmotique eau + osmoles)\n"
                "- Fond de l'anse (branche descendante) : monte jusqu'à **1200 mOsm/kg** (eau sort, osmoles restent)\n"
                "- Branche ascendante : descend fortement (osmoles réabsorbées, pas d'eau)\n"
                "- TCD : ≈ **150 mosm/kg H₂O**\n"
                "- Entrée collecteur : ≈ **100 mosm/kg H₂O**\n"
                "- Fin collecteur : **60–1200 mosm/kg H₂O** selon ADH"),
        ]),
    ]),

    # ════════════════════════════════════════════════════════════════════════
    Partie("III", "Concentration / Dilution de l'urine", [

        SousPartie("A", "Gradient osmotique cortico-papillaire (GCP)", [

            _fc("★ Principe du gradient cortico-papillaire",
                "- Gradient croissant de l'osmolalité dans l'**interstitium rénal**\n"
                "- Cortex : **300 mosm/kg H₂O**\n"
                "- Papille (maximum) : **1200 mOsm/kg H₂O**\n"
                "- Plus on plonge dans la médullaire → plus l'osmolalité interstitielle augmente"),

            _fc("★ Deux conditions nécessaires à la réabsorption d'eau dans le collecteur",
                "1. **Présence d'un gradient osmotique CP** : pour attirer l'eau vers l'interstitium\n"
                "2. **Perméabilité du collecteur à l'eau** : dépend de l'ADH\n"
                "→ Les deux sont indispensables"),

            _key("Pour concentrer les urines, il faut **LE gradient CP ET L'ADH**. "
                 "Un des deux manquant → impossibilité de concentrer."),

            _fc("◆ Effet élémentaire : cotransporteur Na⁺/K⁺/2Cl⁻",
                "- Situé dans la **branche ascendante large de l'anse de Henlé**\n"
                "- Réabsorbe NaCl dans l'interstitium sans eau → crée un gradient local de **200 mOsm/kg H₂O**\n"
                "- **Inhibé par le Furosémide** +++\n"
                "- Associé à la différence de perméabilité entre branches :\n"
                "  - Descendante : perméable à l'eau, imperméable aux solutés\n"
                "  - Ascendante : imperméable à l'eau, perméable aux solutés"),

            _fc("◆ Multiplicateur à contre-courant",
                "- Branches descendante et ascendante **parallèles**, fluide en **sens inverse**\n"
                "- Amplification progressive du gradient jusqu'à **1200 mOsm/kg H₂O** au fond de l'anse\n"
                "- Mécanisme : chaque cycle = l'effet élémentaire (200 mOsm) se multiplie\n"
                "- Plus l'anse est longue → plus l'osmolalité maximale atteinte est élevée"),

            _fc("◆ Le cycle de l'urée",
                "- L'urée : petite molécule librement filtrée qui descend dans l'anse puis remonte\n"
                "- Segments imperméables à l'urée → concentration élevée dans le fluide tubulaire\n"
                "- Fin du collecteur : **perméable à l'urée** → l'urée diffuse dans l'interstitium\n"
                "  puis rejoint le fluide tubulaire de la branche ascendante\n"
                "- L'urée s'accumule autour de la papille\n"
                "- Contribution de l'urée à l'hyperosm médullaire interne : **moitié** (l'autre moitié = NaCl)\n"
                "- L'ADH augmente la perméabilité à l'urée du canal collecteur terminal"),

            _fc("★ Vasa recta : rôle et fonctionnement",
                "- Capillaires droits longeant les **anses de Henlé des néphrons profonds**\n"
                "- Les néphrons superficiels **n'ont pas de vasa recta** → ne participent pas à la concentration\n"
                "- Débit sanguin médullaire : seulement **10 %** du DSR (90 % pour la corticale)\n"
                "- **Système d'échange à contre-courant** :\n"
                "  - Descente : sortie d'eau + entrée d'osmoles dans le capillaire (sang se concentre)\n"
                "  - Remontée : entrée d'eau + sortie d'osmoles (sang récupère son eau)\n"
                "→ Le gradient interstitiel est **préservé**"),

            _fc("◆ Importance du faible débit sanguin médullaire",
                "- **Faible débit = essentiel** :\n"
                "  - Évite le **lavage** du gradient osmotique médullaire\n"
                "  - Permet le maintien du gradient CP (coûteux à produire)\n"
                "- Si débit sanguin médullaire ↑ → gradient perdu → rein **perd la capacité** de concentrer les urines"),

            _fc("★ Inhibiteurs / altérateurs du gradient CP", []),

            _fc("◆ Furosémide (inhibiteur du GCP)",
                "- Inhibe le cotransporteur **Na⁺/K⁺/2Cl⁻** de la branche ascendante\n"
                "- À forte dose : **supprime totalement le gradient CP**\n"
                "- Conséquence : en présence de Furosémide, le rein **ne peut plus concentrer les urines**\n"
                "- Mécanisme du diurétique puissant"),

            _fc("◆ Régimes sans protéines (inhibition par défaut d'urée)",
                "- L'urée = produit du catabolisme des protides\n"
                "- Sans protéines (régime végétarien strict) → moins d'urée\n"
                "- Or l'urée contribue à **moitié** aux osmoles médullaires\n"
                "- Conséquence : ↓ gradient osmotique CP → capacité de concentration réduite"),

            _fc("◆ Diurèse osmotique (altération du GCP)",
                "- Augmente le débit dans les vasa recta\n"
                "- Conséquence : ↓ voire abolition du gradient osmotique CP\n"
                "- Rein incapable de concentrer les urines\n"
                "→ Polyurie (voir partie V B)"),
        ]),

        SousPartie("B", "Hormone antidiurétique (ADH) – AVP", [

            _fc("★ Nature et synthèse de l'ADH",
                "- Petit **peptide** (arginine vasopressine = AVP)\n"
                "- Produit par des **neurones hypothalamiques**\n"
                "- Circuit :\n"
                "  1. Synthèse dans les neurones hypothalamiques\n"
                "  2. Transport le long des **axones**\n"
                "  3. Stockage dans la **post-hypophyse**\n"
                "- Post-hypophyse très vascularisée → libère l'ADH dans le sang par **exocytose** selon les besoins"),

            _fc("★ Organe cible de l'ADH",
                "- **Canal collecteur** (tube collecteur)"),

            _fc("★ Mode d'action de l'ADH sur le canal collecteur",
                "- **Sans ADH** :\n"
                "  - Face basolatérale : AQP3 et AQP4 (constitutives)\n"
                "  - Face apicale : **aucune aquaporine** → eau ne peut pas entrer\n"
                "  - Surface apicale **lisse** au MEB\n\n"
                "- **Avec ADH** :\n"
                "  1. ADH se fixe sur récepteur membranaire **V2**\n"
                "  2. Active l'**adénylate cyclase**\n"
                "  3. Augmente l'**AMPc**\n"
                "  4. Active la **PKA**\n"
                "  5. PKA phosphoryle une protéine\n"
                "  6. En présence de **Ca²⁺** → insertion des **AQP2** (stockées en IC) dans la membrane apicale\n"
                "  → L'eau peut rentrer par osmose\n"
                "  - Surface apicale **granuleuse** au MEB (aquaporines visibles)"),

            _key("Cascade ADH → récepteur V2 → AC → AMPc → PKA → phosphorylation → **insertion AQP2 en apical** +++"),

            _fc("◆ Relation ADH / osmolalité urinaire",
                "- Osmolalité urinaire ↑ **linéairement** avec la concentration plasmatique d'ADH\n"
                "- Plateau à **1200 mOsm/kg H₂O** (maximum physiologique)\n"
                "- Sans ADH : osmolalité urinaire ≈ **60 mosm/L** (urines très diluées)\n"
                "- Avec ADH max : osmolalité urinaire ≈ **1200 mosm/L** (urines très concentrées)"),

            _fc("★ Diabète insipide : deux types",
                "- **Neurogénique** (central) : l'hypothalamus ne produit plus suffisamment d'ADH\n"
                "  (assez rare)\n"
                "- **Néphrogénique** : ADH présente mais les cellules cibles ne répondent pas\n"
                "  (problème de récepteur V2 ou autre)\n"
                "- Dans les **deux cas** : **polyurie importante** (urines très diluées)"),

            _trap("Diabète insipide ≠ diabète sucré :\n"
                  "- Insipide : urines **sans saveur** (sans glucose)\n"
                  "- Sucré : urines **sucrées** (glycosurie car transport max du glucose dépassé)\n"
                  "Historiquement : distinction faite en... goûtant les urines (XVIIIe siècle) !"),

            _fc("◆ Diabète insipide : conséquences chiffrées",
                "- Sans ADH, pour excréter **900 mosm/j** à une osmolalité de **60 mosm/L** :\n"
                "  → Débit urinaire = 900 / 60 = **15 L/j** !!!"),
        ]),
    ]),

    # ════════════════════════════════════════════════════════════════════════
    Partie("IV", "Régulation du bilan de l'eau", [

        SousPartie("A", "Stimuli à l'origine de la sécrétion d'ADH", [

            _fc("★ Les deux systèmes d'alarme de la régulation hydrique",
                "1. **Osmolalité plasmatique** → reflète l'hydratation IC → toujours mis en jeu\n"
                "2. **Volémie** → reflète le secteur EC → mis en jeu si situation d'urgence/danger vital\n\n"
                "Deux systèmes de régulation :\n"
                "- **Soif** : régule les entrées\n"
                "- **Rein + ADH** : régule les sorties"),

            _fc("★ Stimulus principal : osmolalité plasmatique",
                "- Perçue par les **osmorécepteurs hypothalamiques**\n"
                "- Libération d'ADH ↑ **linéairement** avec l'osmolalité plasmatique\n"
                "- **Seuil d'apparition** de l'ADH dans le plasma : **280 mosm/L** (en situation normale)\n"
                "- En dessous de 280 : ADH **non synthétisée**"),

            _fc("◆ Stimulus volumique (urgence)",
                "- Mis en jeu si volémie diminue de **> 7 %**\n"
                "- Perçu par les **volorécepteurs** de l'oreillette droite (OD)\n"
                "- Conséquences :\n"
                "  - Seuil d'apparition de l'ADH **abaissé** (ADH apparaît même si hypo-osmolaire)\n"
                "  - Production d'ADH **augmentée**\n"
                "- Si PA perturbée : **barorécepteurs** aortiques et carotidiens → sécrétion d'ADH"),

            _key("En situation courante : c'est **l'osmolalité plasmatique** qui régule l'ADH, **NON la volémie**.\n"
                 "Le stimulus volumique est un **mécanisme d'urgence** (priorité : maintenir la pression artérielle)."),

            _trap("En cas d'hémorragie brutale :\n"
                  "L'organisme privilégie le **maintien de la PA et de la volémie** sur l'osmolalité.\n"
                  "→ L'ADH est sécrétée même si le sujet est déjà hypo-osmolaire."),
        ]),

        SousPartie("B", "Mise en jeu de la soif", [

            _fc("★ Centres de la soif et seuil d'apparition",
                "- Centres de la soif proches des **osmorécepteurs hypothalamiques**\n"
                "- Seuil d'apparition de la soif : osmolalité plasmatique > **290 mosm/kg H₂O**\n"
                "- (Seuil ADH = 280, seuil soif = **290** → ADH est activée avant la soif)"),

            _fc("◆ Régulation de la soif et rôle du tractus digestif",
                "- Osmorécepteurs dans le **tractus digestif supérieur** :\n"
                "  - Dès qu'on boit → inhibent les osmorécepteurs hypothalamiques\n"
                "  - **Évite la sur-correction** de l'osmolalité (on ne boit pas au-delà du besoin)"),

            _fc("◆ Soif déclenchée par la volémie",
                "- Baisse de volémie > **13 %** → risque vital\n"
                "- Barorécepteurs **intra-rénaux** → système sympathique → **rénine** par l'appareil juxtaglomérulaire\n"
                "- Rénine → production d'**angiotensine II** (molécule **dipsogène** = donne soif)\n"
                "→ Voie d'urgence pour compenser la déshydratation sévère"),

            _trap("**Personnes âgées** : sensation de soif **altérée**\n"
                  "→ Ne se rendent pas compte de la déshydratation\n"
                  "→ Risque de déshydratation grave +++\n"
                  "→ Donner des verres d'eau régulièrement (ne pas attendre la soif)"),

            _mnemo("Seuils à retenir :\n"
                   "- **280** mosm/L = seuil de sécrétion ADH\n"
                   "- **290** mosm/kg H₂O = seuil de la soif\n"
                   "- **-7 %** volémie = stimulus volumique ADH\n"
                   "- **-13 %** volémie = risque vital, angiotensine II et soif"),
        ]),
    ]),

    # ════════════════════════════════════════════════════════════════════════
    Partie("V", "Modifications de la diurèse", [

        SousPartie("A", "Modifications physiologiques", [

            _fc("★ Diurèse normale",
                "- Condition : pas de déshydratation → ADH suffisante (ni nulle, ni maximum)\n"
                "- Au niveau du TCD / entrée collecteur : 15 L/j restant à réabsorber, osmolalité 100 mosm/L\n"
                "- Réabsorption partielle d'eau dans le collecteur\n"
                "- Résultat : **débit urinaire = 1,5 L/j**, osmolalité urinaire = **600 mosm/L**\n"
                "- Excrétion quotidienne : **900 mosm/j** (600 × 1,5)"),

            _fc("★ Antidiurèse (déshydratation / privation d'eau)",
                "- Condition : ADH **au maximum** (déshydratation, privation d'eau)\n"
                "- Objectif : économiser l'eau\n"
                "- Réabsorption maximale d'eau dans le collecteur\n"
                "- Résultat : **débit urinaire = 750 mL/j**, osmolalité urinaire = **1200 mosm/L**\n"
                "- Excrétion : toujours **900 mosm/j** (1200 × 0,75)"),

            _key("Quelle que soit la situation (normale ou antidiurèse), "
                 "le rein doit toujours excréter **~900 mosm/j**. "
                 "Seul le volume d'urine (et donc la concentration) varie."),
        ]),

        SousPartie("B", "Modifications pathologiques", [

            _fc("★ Diurèse aqueuse / Diabète insipide",
                "- Cause : **absence d'ADH** (neurogénique) ou **résistance à l'ADH** (néphrogénique)\n"
                "- Sans ADH → collecteur imperméable à l'eau\n"
                "- Débit : **15 L/j** à osmolalité = **60 mosm/L** pour excréter 900 mosm/j\n"
                "- Risque : déshydratation (situation pas fréquente mais grave)"),

            _fc("★ Diurèse osmotique",
                "- Définition : polyurie due à une **substance osmotiquement active** filtrée mais **peu réabsorbée**\n"
                "- Mécanisme : ↑ charge osmolaire tubulaire → ↑ débit vasa recta → **abolition du gradient CP**\n"
                "- Interstitium reste à ~300 mosm/L cortex → papille (gradient effacé)\n"
                "- Urines : **polyurie iso-osmotique** (osmolalité urinaire ≤ 300 mosm/L)"),

            _fc("◆ Substances responsables de la diurèse osmotique", []),

            _fc("→ Substances exogènes",
                "- **Mannitol** : sucre utilisé en thérapeutique (ex : œdèmes cérébraux)\n"
                "- **Produits de contraste** radiologiques"),

            _fc("→ Substances endogènes en excès",
                "- **Glucose** (diabète déséquilibré : glycémie > 2 g/L ou > 10 mmol/L)\n"
                "- **Urée** (levée d'obstacle urologique)"),

            _fc("★ Diurèse osmotique au glucose (diabète déséquilibré)",
                "1. Transport max du glucose atteint dans le proximal → **glycosurie** (glucose dans les urines)\n"
                "2. Glucose dans le tube = osmotiquement actif → perturbe réabsorption eau et Na⁺ dans le **proximal**\n"
                "   (là où 2/3 de l'eau et du Na⁺ sont normalement réabsorbés → très grave)\n"
                "3. Débit tubulaire proximal très élevé → ↑↑ débit dans les vasa recta\n"
                "4. **Abolition du gradient CP** → interstitium reste à 300 mosm/L\n"
                "5. Malgré ADH : urines ne peuvent être concentrées à > **300 mOsm/L**\n"
                "6. **Polyurie iso-osmotique** → polydipsie compensatrice\n"
                "⚠ Risque déshydratation surtout chez les personnes âgées"),

            _trap("Dans la diurèse osmotique au glucose :\n"
                  "L'ADH **fonctionne** mais est **inefficace** car il n'y a plus de gradient CP.\n"
                  "Le collecteur est perméable à l'eau mais il n'y a rien pour l'attirer !"),
        ]),

        SousPartie("C", "Diurétiques – mécanismes d'action", [

            _fc("★ Furosémide (diurétique de l'anse)",
                "- Site d'action : **branche ascendante large** de l'anse de Henlé\n"
                "- Mécanisme : **inhibe le cotransporteur Na⁺/K⁺/2Cl⁻**\n"
                "- Conséquence : suppression du gradient osmotique CP\n"
                "- En présence de Furosémide : le rein **ne peut pas** concentrer les urines\n"
                "  → Diurétique de **l'anse** = diurétique **puissant**"),

            _fc("◆ Inhibiteurs de l'anhydrase carbonique",
                "- Site d'action : **tube contourné proximal**\n"
                "- Mécanisme : bloquent l'anhydrase carbonique → bloquent réabsorption de **HCO₃⁻** et Na⁺\n"
                "- Peu utilisés en pratique"),

            _mnemo("Sites des diurétiques sur le néphron :\n"
                   "- Inhibiteurs anhydrase carbonique → **PROXIMAL**\n"
                   "- Furosémide → **ANSE** (branche ascendante large)\n"
                   "- (Thiazides → TCD – non vu dans ce cours)\n"
                   "- (Spironolactone → collecteur – non vu dans ce cours)"),
        ]),
    ]),
]

# ---------------------------------------------------------------------------
# Tableaux de synthèse
# ---------------------------------------------------------------------------
tableaux = [
    TableauSynthese(
        "Perméabilité des segments du néphron",
        "| Segment | Eau | Solutés (NaCl) | Aquaporines |\n"
        "|---|---|---|---|\n"
        "| TCP | **Oui** (massive) | Oui | **AQP1** |\n"
        "| Branche descendante anse Henlé | **Oui** | **Non** | **AQP1** |\n"
        "| Branche ascendante large anse Henlé | **NON (jamais)** | **Oui (Na/K/2Cl)** | **Aucune** |\n"
        "| TCD | **Non** | Oui | — |\n"
        "| Canal collecteur sans ADH | **Non** | Oui | AQP3/4 (baso) |\n"
        "| Canal collecteur avec ADH | **Oui** | Oui | **AQP2 (apical)** + AQP3/4 |",
    ),
    TableauSynthese(
        "Situations de diurèse : comparatif chiffré",
        "| Situation | ADH | Osmolalité urinaire | Débit urinaire | Osmoles excrétées |\n"
        "|---|---|---|---|---|\n"
        "| Diurèse normale | Partielle | **600 mosm/L** | **1,5 L/j** | 900 mosm/j |\n"
        "| Antidiurèse (déshydratation) | **Maximum** | **1200 mosm/L** | **750 mL/j** | 900 mosm/j |\n"
        "| Diabète insipide (sans ADH) | **Absente** | **60 mosm/L** | **15 L/j** | 900 mosm/j |\n"
        "| Diurèse osmotique | Présente | ≤ **300 mosm/L** | **Polyurie** | ↑↑ osmoles |\n"
        "| Diurèse aqueuse sous Furosémide | Présente | **60 mosm/L** | Polyurie | 900 mosm/j |",
    ),
    TableauSynthese(
        "Inhibiteurs du gradient cortico-papillaire",
        "| Inhibiteur | Mécanisme | Conséquence |\n"
        "|---|---|---|\n"
        "| **Furosémide** | Inhibe Na/K/2Cl dans branche ascendante | Suppression totale du gradient CP |\n"
        "| **Régime sans protéines** | ↓ urée → ↓ osmoles médullaires | Réduction du gradient CP |\n"
        "| **Diurèse osmotique** | ↑ débit vasa recta → lavage du gradient | Abolition du gradient CP |",
    ),
]

# ---------------------------------------------------------------------------
# Chiffres clés
# ---------------------------------------------------------------------------
chiffres_cles = TableauSynthese(
    "Chiffres clés à retenir",
    "| Paramètre | Valeur | Précision |\n"
    "|---|---|---|\n"
    "| Eau corporelle totale | **60 %** du poids | 1/3 EC, 2/3 IC |\n"
    "| Volume plasmatique | **3 L** | Reflet du milieu EC |\n"
    "| Osmolalité plasmatique normale | **295 ± 5** mosm/kg H₂O | ≈ 300 par simplification |\n"
    "| Tonicité (osmolalité efficace) | **2 × [Na⁺] ≈ 280** mosm/kg H₂O | 2 × 140 |\n"
    "| Eau endogène | **500 mL/j** | Fixe |\n"
    "| Sorties extra-rénales | **500–800 mL/j** | Non régulées |\n"
    "| Filtration glomérulaire | **180 L/j** | |\n"
    "| Débit urinaire normal | **1,5–1,8 L/j** | 1 % du filtrat |\n"
    "| Débit urinaire minimum | **0,5 L/j** | |\n"
    "| Charge osmolaire quotidienne | **600–900 mosm/j** | Urée, sulfates, phosphates |\n"
    "| Osmolalité urinaire (plage) | **60–1200** mosm/kg H₂O | |\n"
    "| Osmolalité cortex interstitium | **300** mosm/kg H₂O | |\n"
    "| Osmolalité papille interstitium (max) | **1200** mOsm/kg H₂O | |\n"
    "| Gradient élémentaire Na/K/2Cl | **200** mOsm/kg H₂O | Entre lumière et interstitium |\n"
    "| Contribution urée au gradient médullaire | **50 %** | L'autre moitié = NaCl |\n"
    "| DSR médullaire | **10 %** du DSR total | 90 % pour la corticale |\n"
    "| Seuil sécrétion ADH | **280** mosm/L | |\n"
    "| Seuil soif | **290** mosm/kg H₂O | Après le seuil ADH |\n"
    "| Stimulus volumique ADH | **-7 %** volémie | Urgence |\n"
    "| Risque vital (volémie) | **-13 %** | Angiotensine II dipsogène |\n"
    "| Osmolalité urinaire antidiurèse max | **1200 mosm/L** → débit **750 mL/j** | |\n"
    "| Osmolalité urinaire diabète insipide | **60 mosm/L** → débit **15 L/j** | |",
)

# ---------------------------------------------------------------------------
# Points clés résumés
# ---------------------------------------------------------------------------
points_cles = [
    "La **natrémie** reflète l'état d'hydratation **intracellulaire**, jamais le volume extracellulaire.",
    "La branche ascendante large de l'anse de Henlé est **imperméable à l'eau en toute circonstance** (pas d'AQP, jonctions serrées).",
    "Pour concentrer les urines : il faut **LE gradient CP ET L'ADH** (les deux sont indispensables).",
    "L'ADH agit sur le canal collecteur via V2 → AMPc → PKA → **insertion d'AQP2 en face apicale**.",
    "Le **Furosémide** inhibe Na/K/2Cl → supprime le gradient CP → diurétique puissant.",
    "L'urée contribue à **50 %** à l'hyperosmolalité médullaire (l'autre moitié = NaCl).",
    "Les **vasa recta** maintiennent le gradient CP par échange à contre-courant ; leur faible débit est essentiel.",
    "Régulation ADH : osmolalité (principale) → seuil 280 mosm/L ; volémie (urgence) si −7 % ; barorécepteurs si PA atteinte.",
    "Soif : seuil > **290 mosm/kg H₂O** ; osmorécepteurs digestifs inhibent la soif dès qu'on boit (évite la sur-correction).",
    "Diabète insipide (neurogénique ou néphrogénique) → **15 L/j** d'urines à 60 mosm/L. Diurèse osmotique → polyurie iso-osmotique (≤ 300 mosm/L).",
]

# ---------------------------------------------------------------------------
# Fiche éclair
# ---------------------------------------------------------------------------
fiche_eclair_md = """\
## UE5 C4 – Bilan de l'eau : flash

**Compartiments** : 60 % PC → 1/3 EC (plasma 3 L + interstitiel) / 2/3 IC. Eau échangée passivement via AQP.
**Osmolalité** : 295 ± 5 mosm/kg H₂O. Formule : 2×[Na⁺] + glu + urée. Tonicité = 2×[Na⁺] ≈ 280.
**Natrémie** = reflet du volume IC (pas EC !).

**Segments néphron** :
- TCP : perméable eau + solutés (AQP1), réabsorption iso-osmotique (60–70 %)
- Branche ↓ anse : eau oui, solutés non
- Branche ↑ large : **eau JAMAIS** (pas d'AQP), NaCl via Na/K/2Cl → ↓ osm tubulaire
- TCD : eau non, solutés oui
- Canal collecteur : eau si **ADH** (AQP2 apical)

**Gradient CP** : 300 (cortex) → 1200 mosm/kg H₂O (papille). Créé par Na/K/2Cl (↑ branche ↑ large).
Amplifié par **contre-courant**. Urée = 50 % des osmoles médullaires. Maintenu par **vasa recta** (10 % DSR).
**Furosémide** → inhibe Na/K/2Cl → supprime gradient → diurétique puissant.

**ADH** : synthèse hypothalamus → stockage post-hypophyse → V2 → AMPc → PKA → **AQP2 apical**.
- Sans ADH : 60 mosm/L, 15 L/j
- ADH max : 1200 mosm/L, 750 mL/j

**Régulation** : osmolalité (principal, seuil 280) + volémie (urgence, −7 %) + PA (barorécepteurs).
Soif : seuil 290 mosm/kg H₂O. AngII dipsogène (volémie −13 %).

**Patho** : DI neurogénique (pas d'ADH) / néphrogénique (résistance) → 15 L/j.
Diurèse osmotique (glucose diabète, mannitol) → gradient CP aboli → polyurie iso-osmotique ≤ 300 mosm/L.
"""

# ---------------------------------------------------------------------------
# FicheData assemblée
# ---------------------------------------------------------------------------
fiche = FicheData(
    matiere="Physiologie",
    nom_cours="Rôle du rein dans le bilan de l'eau",
    annee="2025-2026",
    item="UE5 – C4 (9 mars 2026)",
    plan=plan,
    parties=parties,
    tableaux=tableaux,
    chiffres_cles=chiffres_cles,
    points_cles=points_cles,
    fiche_eclair_md=fiche_eclair_md,
    images=[],
)


# ---------------------------------------------------------------------------
# Génération des sorties
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from major_ecn.content_builder import output_basename
    from major_ecn.docx_generator import render_docx
    from major_ecn.pdf_generator import render_pdf

    OUT_DIR = PROJECT_ROOT / "output"
    OUT_DIR.mkdir(exist_ok=True)

    basename = output_basename(fiche)
    pdf_path = OUT_DIR / f"{basename}.pdf"
    docx_path = OUT_DIR / f"{basename}.docx"

    print(f"Génération PDF  → {pdf_path}")
    render_pdf(fiche, pdf_path)

    print(f"Génération DOCX → {docx_path}")
    render_docx(fiche, docx_path)

    print("✓ Flashcards UE5 C4 générées avec succès.")

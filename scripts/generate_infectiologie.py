"""Génère la fiche exhaustive d'Infectiologie à partir du texte source extrait."""

from __future__ import annotations

import json
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
        PlanPartie(numero="I", titre="Antibiotiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Bêta-lactamines"),
            PlanSousPartie(lettre="B", titre="Aminosides, glycopeptides et autres anti-Gram+"),
            PlanSousPartie(lettre="C", titre="Macrolides, cyclines et fluoroquinolones"),
            PlanSousPartie(lettre="D", titre="Autres antibiotiques et principes d'antibiothérapie"),
        ]),
        PlanPartie(numero="II", titre="Fièvre", sous_parties=[
            PlanSousPartie(lettre="A", titre="Fièvre aiguë de l'adulte"),
            PlanSousPartie(lettre="B", titre="Fièvre prolongée"),
            PlanSousPartie(lettre="C", titre="Fièvre de l'immunodéprimé et neutropénie fébrile"),
        ]),
        PlanPartie(numero="III", titre="Méningites et méningo-encéphalites", sous_parties=[
            PlanSousPartie(lettre="A", titre="Syndrome méningé et méningo-encéphalite herpétique"),
            PlanSousPartie(lettre="B", titre="Méningites à liquide clair : Listeria et tuberculose"),
            PlanSousPartie(lettre="C", titre="Méningites purulentes"),
        ]),
        PlanPartie(numero="IV", titre="Paludisme", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et diagnostic"),
            PlanSousPartie(lettre="B", titre="Prise en charge et prophylaxie"),
        ]),
        PlanPartie(numero="V", titre="Vaccinations", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et vaccins obligatoires du nourrisson"),
            PlanSousPartie(lettre="B", titre="Vaccins recommandés et populations ciblées"),
        ]),
        PlanPartie(numero="VI", titre="Infections spécifiques", sous_parties=[
            PlanSousPartie(lettre="A", titre="Grippe"),
            PlanSousPartie(lettre="B", titre="Infection VIH"),
            PlanSousPartie(lettre="C", titre="Syphilis"),
            PlanSousPartie(lettre="D", titre="Zoonoses et voyage en pays tropical"),
        ]),
    ]

    # ── PARTIE I : ANTIBIOTIQUES ──
    partie_i = Partie(numero="I", titre="Antibiotiques", sous_parties=[
        SousPartie(lettre="A", titre="Bêta-lactamines", rows=[
            FicheRow(concept="Mode d'action commun", detail_md=(
                "- Inhibition de la **synthèse de la paroi bactérienne** (liaison aux PLP)\n"
                "- **Bactéricides**, temps-dépendants\n"
                "- Élimination principalement **urinaire** (sauf ceftriaxone : biliaire)\n"
                "- Mauvaise diffusion dans : oeil, os, SNC, prostate"
            )),
            FicheRow(concept="Pénicillines", detail_md=(
                "| Sous-classe | Exemples | Spectre principal | Particularités |\n"
                "|-------------|----------|-------------------|----------------|\n"
                "| Péni G et V | Péni G, Péni V, Benzathine-Péni | Streptocoques, Listeria, Treponema | Absorption digestive médiocre, mauvaise diffusion LCR |\n"
                "| Péni A | **Amoxicilline**, Ampicilline | Streptocoques, Entérocoques, Listeria, Méningocoque | Biodispo orale 80% (amox), bonne diffusion LCR à forte dose |\n"
                "| Péni M | **Oxacilline**, Cloxacilline | SAMS, S. pyogenes | Diffusion très faible oeil/LCR/prostate |\n"
                "| Uréidopéni | Pipéracilline | CGP, BGP, BGN aérobies | Bonne diffusion méningée et biliaire |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- **Amoxicilline** : ATB de 1re intention dans angine, otite, sinusite, pneumopathie communautaire\n"
                "- Jamais d'amoxicilline seule sur S. aureus (pénicillinase dans 95% des cas)"
            ), kind="a_retenir"),
            FicheRow(concept="Céphalosporines", detail_md=(
                "| Génération | Exemples | Spectre | Particularités |\n"
                "|------------|----------|--------|----------------|\n"
                "| C1G | Céfalexine, **Céfazoline** | CGP, quelques BGN | Diffusion LCR insuffisante |\n"
                "| C2G | Céfuroxime, Céfoxitine | CGP, entérobactéries sans BLSE | Diffusion LCR insuffisante |\n"
                "| **C3G** | **Céfotaxime**, **Ceftriaxone**, Ceftazidime | **BGN**, streptocoques, pneumocoque | Bonne diffusion LCR, allergie croisée péni 10% |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ C3G : résistance naturelle de **Listeria**, Légionella, entérocoques, SARM, intracellulaires\n"
                "- Ceftriaxone : élimination **biliaire**, risque de pseudo-lithiase vésiculaire"
            ), kind="piege"),
            FicheRow(concept="◆ Carbapénèmes", detail_md=(
                "- **Imipénem**, Méropénem, Ertapénem\n"
                "- Spectre le plus large des bêta-lactamines\n"
                "- Voie **IV uniquement** (absorption intestinale nulle)\n"
                "- Résistance : P. aeruginosa résistant uniquement à l'ertapénem\n"
                "- EI : convulsions (imipénem), colite à Clostridium"
            )),
            FicheRow(concept="Inhibiteurs de bêta-lactamases", detail_md=(
                "- **Augmentin** (amox + ac. clavulanique), Tazocilline (pipéra + tazobactam)\n"
                "- Élargissent le spectre aux bactéries productrices de pénicillinases et aux **anaérobies**\n"
                "- EI : troubles digestifs, surinfection à Candida, colite à Clostridium"
            )),
        ]),
        SousPartie(lettre="B", titre="Aminosides, glycopeptides et autres anti-Gram+", rows=[
            FicheRow(concept="Aminosides", detail_md=(
                "- **Gentamicine**, Tobramycine, **Amikacine**\n"
                "- Mode d'action : inhibition synthèse protéique, **bactéricide concentration-dépendante**\n"
                "- Voie **IV uniquement** (aucune absorption digestive)\n"
                "- Surveillance : pic (30 min post-perfusion) et **résiduelle (H24)**\n"
                "- EI majeurs : **néphrotoxicité**, **ototoxicité cochléo-vestibulaire** (irréversible si > 7j)\n"
                "- CI : myasthénie, grossesse (ototoxicité foetale)"
            )),
            FicheRow(concept="Glycopeptides", detail_md=(
                "- **Vancomycine**, Teicoplanine\n"
                "- Spectre : uniquement **Gram+** (streptocoques, entérocoques, SAMS et SARM)\n"
                "- Voie IV (pas d'absorption orale)\n"
                "- EI : **néphrotoxicité**, Red man syndrome, veinite\n"
                "- Dosage régulier des concentrations résiduelles\n"
                "- Résistance acquise : ERV (entérocoques résistants vancomycine), VISA/GISA, VRSA"
            )),
            FicheRow(concept="Linézolide", detail_md=(
                "- Oxazolidinone, **bactériostatique**\n"
                "- Biodisponibilité **100%** (prise orale possible)\n"
                "- Spectre : Gram+ dont SARM, pneumocoques péni-R, ERV\n"
                "- Effet **anti-toxinique** (Panton-Valentine)\n"
                "- EI : **myélotoxicité** (thrombopénie, anémie) si traitement > 28j\n"
                "- Surveillance NFS nécessaire"
            )),
            FicheRow(concept="Daptomycine", detail_md=(
                "- Lipopeptide, inhibition synthèse membrane cytoplasmique\n"
                "- Spectre : Gram+ dont SAMS, SARM, entérocoques\n"
                "- IV uniquement, faible diffusion tissulaire\n"
                "- EI : **rhabdomyolyse** (doser CPK avant et pendant traitement)"
            )),
        ]),
        SousPartie(lettre="C", titre="Macrolides, cyclines et fluoroquinolones", rows=[
            FicheRow(concept="Macrolides", detail_md=(
                "- **Azithromycine**, Clarithromycine, Spiramycine\n"
                "- Mode d'action : inhibition synthèse protéique, **bactériostatiques**\n"
                "- Spectre : streptocoques, SAMS, **intracellulaires** (sauf Coxiella burnetii)\n"
                "- Bonne diffusion tissulaire sauf LCR, élimination biliaire\n"
                "- EI : troubles digestifs, **allongement QT**, hépatite immunoallergique\n"
                "- **Interactions** ++++ : ergotamine, AVK, ciclosporine"
            )),
            FicheRow(concept="Cyclines", detail_md=(
                "- **Doxycycline**, Minocycline, Tigécycline\n"
                "- Bactériostatiques, bonne absorption intestinale (sauf tigécycline IV)\n"
                "- Spectre : bactéries atypiques (Mycoplasma), **intracellulaires**, Borrelia\n"
                "- EI : **phototoxicité**, anomalies osseuses/dentaires enfant, ulcérations oesophagiennes\n"
                "- CI : femme enceinte/allaitante, enfant < **8 ans**, association rétinoïdes\n"
                "- ⚠ Interaction avec AVK"
            )),
            FicheRow(concept="Fluoroquinolones", detail_md=(
                "- **Ciprofloxacine**, **Lévofloxacine**, Ofloxacine\n"
                "- Inhibition synthèse ADN, **bactéricides concentration-dépendants**\n"
                "- Excellente biodisponibilité orale et diffusion tissulaire\n"
                "- Spectre : entérobactéries, intracellulaires, SAMS ; FQ anti-pneumococciques : pneumocoque\n"
                "- EI : **tendinopathies**, allongement QTc, convulsions, phototoxicité\n"
                "- CI : grossesse, enfant en croissance, déficit en G6PD"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Ne jamais utiliser les FQ en **monothérapie** (sélection de mutants résistants)\n"
                "- Si acide nalidixique R sur antibiogramme, ne pas utiliser de FQ"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Autres antibiotiques et principes d'antibiothérapie", rows=[
            FicheRow(concept="Rifampicine", detail_md=(
                "- Inhibition synthèse ARN bactérien, **bactéricide**\n"
                "- Bonne diffusion tissulaire (os, LCR, poumon)\n"
                "- **Ne jamais utiliser en monothérapie**\n"
                "- EI : coloration orange des sécrétions, hépatotoxicité\n"
                "- Interactions ++++ : AVK, oestroprogestatifs, antiépileptiques\n"
                "- CI : porphyrie"
            )),
            FicheRow(concept="Cotrimoxazole (Bactrim)", detail_md=(
                "- Sulfaméthoxazole + triméthoprime\n"
                "- Inhibition synthèse acide folique, bactériostatique\n"
                "- Spectre : pneumocoques, E. coli, **SARM** (95%), **Pneumocystis**\n"
                "- Excellente biodisponibilité, bonne diffusion tissulaire\n"
                "- EI : toxidermies graves (SJS, Lyell), anémie hémolytique si déficit G6PD\n"
                "- CI : grossesse T1, allergie sulfamides"
            )),
            FicheRow(concept="Métronidazole (Flagyl)", detail_md=(
                "- Imidazolé, **bactéricide** sur anaérobies\n"
                "- Spectre : **tous anaérobies** (sauf P. acnes, Actinomyces), Clostridium, protozoaires (amibes, Giardia)\n"
                "- Bonne diffusion tissulaire dont LCR\n"
                "- EI : effet **antabuse**, neuropathie sensitive si traitement prolongé\n"
                "- CI : grossesse T1 et allaitement"
            )),
            FicheRow(concept="Principes d'antibiothérapie", detail_md=(
                "- La majorité des ATB ont des durées < **14 jours** (exceptions : endocardite, os, abcès)\n"
                "- Bithérapie utile pour : éviter résistances, synergie rapide (sepsis), élargir spectre\n"
                "- **ATB probabiliste** selon site : urinaire (C3G), cutanée (oxacilline), digestive (C3G + métronidazole), pulmonaire (C3G + macrolide/FQ)\n"
                "- **ATB documentée** : un site, un germe, un patient"
            )),
            FicheRow(concept="", detail_md=(
                "- Les **entérocoques** ont une résistance naturelle aux céphalosporines\n"
                "- Ne jamais donner d'amoxicilline seule sur un S. aureus (pénicillinase 95%)"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE II : FIÈVRE ──
    partie_ii = Partie(numero="II", titre="Fièvre", sous_parties=[
        SousPartie(lettre="A", titre="Fièvre aiguë de l'adulte", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Fièvre : T°C centrale > **38°C** le matin et **38,3°C** le soir\n"
                "- Fébricule : T°C entre 37,5 et 38°C\n"
                "- Fièvre aiguë : < **5 jours**, étiologies souvent infectieuses\n"
                "- Conditions de mesure : à distance repas, après 20 min de repos\n"
                "- Voie axillaire/buccale : majorer de **0,5°C** pour T°C centrale"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **Infectieuses** +++ (cause la plus fréquente)\n"
                "- Syndromes d'hyperthermie (non infectieux) :\n"
                "  - Coup de chaleur, canicule chez sujet âgé\n"
                "  - Causes médicamenteuses : syndrome malin des neuroleptiques, ISRS\n"
                "  - Thyrotoxicose\n"
                "- Contexte lésionnel : chirurgie, polytraumatisme, hématome, EP, hémorragie méningée\n"
                "- Contexte inflammatoire : lupus, SAPL, maladie de Still, DRESS"
            )),
            FicheRow(concept="◆ Bilan devant fièvre > 72h", detail_md=(
                "- NFS-plaquettes, ionogramme, urée, créatinine\n"
                "- BHC, BU, **hémocultures** (avant ATB)\n"
                "- RXT face\n"
                "- +/- CRP et **PCT**\n"
                "- Si signes de gravité : GDS, lactatémie, TP\n"
                "- Si sepsis grave : scanner TAP en urgence après stabilisation"
            )),
            FicheRow(concept="Indications d'hospitalisation", detail_md=(
                "- Sepsis grave, choc septique\n"
                "- Terrain à risque : femme enceinte, immunodépression\n"
                "- Difficultés prise orale ATB\n"
                "- Absence d'amélioration à 48-72h"
            )),
            FicheRow(concept="Traitement symptomatique", detail_md=(
                "- **Hydratation** +++ : boissons abondantes, sucrées et salées\n"
                "- Antipyrétiques si fièvre mal tolérée : **paracétamol** 1g x 4/j\n"
                "- ⚠ Aspirine et AINS **non recommandés** (syndrome de Reye chez enfant, risque complication bactérienne)"
            )),
        ]),
        SousPartie(lettre="B", titre="Fièvre prolongée", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Fièvre prolongée : évolution > **20 jours**\n"
                "- Fièvres récurrentes : épisodes fébriles espacés d'intervalles libres"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **Infections (40%)** :\n"
                "  - **Endocardite** +++, **tuberculose** +++\n"
                "  - Foyers suppurés : dentaires, sinusiens, urinaires, digestifs, prothèse articulaire\n"
                "  - Bactéries intracellulaires : fièvre Q, brucellose, Whipple, syphilis\n"
                "  - Virales : VIH, EBV, CMV ; Fongiques : candidose systémique, cryptococcose\n"
                "- **Affections malignes (20-30%)** : cancers solides (rein, ovaire, foie), lymphomes, leucémies\n"
                "- **Maladies inflammatoires (10%)** : Horton (> 60 ans +++), auto-immunes, MICI\n"
                "- Causes médicamenteuses : 7-28j après introduction, hyperéosinophilie dans 20%\n"
                "- Fièvres factices : thermopathomimie, syndrome de Münchausen"
            )),
            FicheRow(concept="", detail_md=(
                "- La **maladie de Horton** est la cause de fièvre inflammatoire la plus fréquente après **60 ans**\n"
                "- Toujours rechercher une **endocardite** devant une fièvre prolongée"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Bilan de 1re intention", detail_md=(
                "- NFS, CRP, ionogramme, créatinine, calcémie, BHC, BU, EPP, TSH, CPK, LDH\n"
                "- **Hémocultures** répétées (préciser recherche endocardite)\n"
                "- Sérologies : VIH, EBV, CMV, toxoplasmose\n"
                "- Imagerie : RXT, panoramique dentaire, échographie abdominale"
            )),
            FicheRow(concept="Bilan de 2e intention", detail_md=(
                "- Ac antinucléaires, ANCA\n"
                "- Crachats/tubages gastriques (BAAR)\n"
                "- Sérologies : Legionella, Coxiella, Bartonella\n"
                "- ETT, écho-doppler veineux MI\n"
                "- Scanner TAP +/- TEP-scan\n"
                "- BOM avec myéloculture\n"
                "- **BAT** si > 60 ans"
            )),
        ]),
        SousPartie(lettre="C", titre="Fièvre de l'immunodéprimé et neutropénie fébrile", rows=[
            FicheRow(concept="Types d'immunodépression", detail_md=(
                "| Type | Étiologies | Pathogènes principaux |\n"
                "|------|-----------|----------------------|\n"
                "| Neutropénie | Leucémies, CT/RT, aplasie | Précoces : BGN (E. coli, P. aeruginosa), CGP. Tardifs : Candida, Aspergillus |\n"
                "| Déficit immunité cellulaire | VIH (CD4 < 200), corticothérapie, IS | Listeria, Mycobactéries, Pneumocystis, Toxoplasma, CMV |\n"
                "| Hypogammaglobulinémie | Myélome, LLC, SN | **Pneumocoque**, H. influenzae, Méningocoque |\n"
                "| Asplénie | Post-chirurgicale, drépanocytose | Pneumocoque, Méningocoque |\n"
            )),
            FicheRow(concept="Neutropénie fébrile", detail_md=(
                "- Neutropénie : PNN < **500/mm3** (agranulocytose)\n"
                "- Fièvre : 1 mesure > **38,3°C** ou 2 mesures > 38°C à 1h d'intervalle\n"
                "- Gravité majorée si PNN < 100/mm3, neutropénie > 7j, mucite sévère\n"
                "- Portes d'entrée fréquentes : tube digestif (translocation), peau/cathéters, poumons\n"
                "- Agents : 2/3 CGP (SCN ++, S. aureus), 1/3 BGN (E. coli, Klebsiella, P. aeruginosa)"
            )),
            FicheRow(concept="PEC neutropénie fébrile", detail_md=(
                "- ATB **urgente**, bactéricide, large spectre, après prélèvements\n"
                "- **Bêta-lactamine antipyocyanique** forte dose en 1re intention\n"
                "- + **Aminosides** si sepsis sévère ou suspicion BGN multi-R\n"
                "- + **Glycopeptides** si choc septique, mucite sévère, suspicion infection cathéter\n"
                "- Réévaluation à **48-72h**\n"
                "- Si fièvre persistante sous ATB : TDM thorax + sinus, Ag aspergillaire, ajout anti-fongique"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Le pus est absent chez le neutropénique : pas de suppuration visible\n"
                "- 70% des fièvres aiguës neutropéniques n'ont pas de documentation microbiologique"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE III : MÉNINGITES ET MÉNINGO-ENCÉPHALITES ──
    partie_iii = Partie(numero="III", titre="Méningites et méningo-encéphalites", sous_parties=[
        SousPartie(lettre="A", titre="Syndrome méningé et méningo-encéphalite herpétique", rows=[
            FicheRow(concept="Syndrome méningé aigu", detail_md=(
                "- **Céphalées** intenses, continues, non calmées par antalgiques, avec rachialgies\n"
                "- Phonophotophobie\n"
                "- Vomissements en jets, précoces, sans rapport avec les repas\n"
                "- **Raideur de nuque** douloureuse et permanente (attitude en chien de fusil)\n"
                "- Signes de Kernig et Brudzinski"
            )),
            FicheRow(concept="Syndrome encéphalitique", detail_md=(
                "- Troubles de la conscience\n"
                "- Crises convulsives focales/généralisées\n"
                "- Signes de focalisation neurologique\n"
                "- Troubles du comportement\n"
                "- Troubles neurovégétatifs (irrégularité FC, PA, T°C)"
            )),
            FicheRow(concept="Signes de gravité", detail_md=(
                "- Encéphalite au cours d'une méningite\n"
                "- **Purpura extensif**\n"
                "- Troubles respiratoires (Cheyne-Stokes, pauses)\n"
                "- Troubles végétatifs (bradycardie, HTA, hypothermie)\n"
                "- **HTIC**, choc septique"
            )),
            FicheRow(concept="Méningo-encéphalite herpétique", detail_md=(
                "- HSV-1 (95% adulte), polioencéphalite nécrosante et hémorragique des **lobes temporaux**\n"
                "- Début brutal, syndrome infectieux constant\n"
                "- Troubles vigilance, convulsions (partielles ++), hallucinations olfactives/gustatives\n"
                "- Modifications comportement, troubles mnésiques antérogrades\n"
                "- LCS : lymphocytaire < 500, protéinorachie modérée < 1g/L, **glycorachie normale**\n"
                "- **PCR HSV** sur LCS (si négative, refaire à 72h)"
            )),
            FicheRow(concept="", detail_md=(
                "- Toute **confusion fébrile** est une méningo-encéphalite herpétique jusqu'à preuve du contraire\n"
                "- Traitement par **aciclovir** IV 10 mg/kg/8h pendant **15-21 jours**, sans attendre les résultats"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Imagerie", detail_md=(
                "- **Scanner** : souvent normal initialement, puis hypodensité temporale\n"
                "- **IRM** (T2) : hypersignal temporal antérieur, bilatéral et **asymétrique**\n"
                "- Mortalité 15% avec traitement / 80% sans traitement\n"
                "- Séquelles : syndrome de Korsakoff, aphasie, syndrome de Klüver-Bucy, épilepsie"
            )),
        ]),
        SousPartie(lettre="B", titre="Méningites à liquide clair : Listeria et tuberculose", rows=[
            FicheRow(concept="Listériose neuroméningée", detail_md=(
                "- Listeria monocytogenes : **bacille Gram+** intracellulaire\n"
                "- Contamination : voie digestive (produits laitiers, charcuterie)\n"
                "- Terrain : sujet âgé, grossesse, OH chronique, diabète, immunodépression\n"
                "- Phase prodromique : asthénie, douleurs abdominales, céphalées\n"
                "- **Rhombencéphalite** (50%) : atteinte paires crâniennes, syndrome cérébelleux"
            )),
            FicheRow(concept="LCS Listeria", detail_md=(
                "- Clair (parfois puriforme), hypertendu\n"
                "- Pléiocytose franche (200-300 éléments), **lymphocytaire ou panachée**\n"
                "- Hyperprotéinorachie modérée, **hypoglycorachie** ou normoglycorachie\n"
                "- Examen direct : bacille Gram+ (inconstant), HC souvent contributives"
            )),
            FicheRow(concept="Traitement Listeria", detail_md=(
                "- **Amoxicilline + aminosides** IV pendant 3-4 semaines\n"
                "- Si allergie : cotrimoxazole\n"
                "- Mortalité **30%**, séquelles neurologiques fréquentes\n"
                "- **Déclaration obligatoire** à l'ARS"
            )),
            FicheRow(concept="Méningite tuberculeuse", detail_md=(
                "- Terrain : immigrés, ID, VIH, diabète, OH, sujet âgé\n"
                "- Installation **subaiguë/chronique** : AEG, sueurs nocturnes, fébricule\n"
                "- Atteinte **basilaire** : paralysie oculomotrice (III, VI), PF\n"
                "- LCS : clair, lymphocytaire, protéinorachie > 1g/L, **hypoglycorachie constante**, hypochlorurachie\n"
                "- Coloration de Ziehl-Nielsen, culture Lowenstein (3 semaines), PCR BK\n"
                "- IRM : prise de contraste méningée basale, tuberculomes"
            )),
            FicheRow(concept="Traitement TB méningée", detail_md=(
                "- **Quadrithérapie** 2 mois puis **bithérapie** 10 mois\n"
                "- Corticothérapie **systématique**\n"
                "- Mortalité **25%**, séquelles chez 15% des survivants\n"
                "- Déclaration obligatoire à l'ARS"
            )),
            FicheRow(concept="◆ Méningites virales bénignes", detail_md=(
                "- Première cause de méningites aiguës, adulte jeune/enfant\n"
                "- Virus : **entérovirus** ++ (Coxsackie, echovirus), virus ourlien, rougeole\n"
                "- LCS : clair, lymphocytaire, protéinorachie < 1g/L, **glycorachie normale**\n"
                "- Aucun signe de localisation ni de gravité\n"
                "- Évolution favorable en quelques jours, traitement symptomatique"
            )),
        ]),
        SousPartie(lettre="C", titre="Méningites purulentes", rows=[
            FicheRow(concept="Germes selon terrain", detail_md=(
                "| Terrain | Germes principaux |\n"
                "|---------|------------------|\n"
                "| NN < 2 mois | Streptocoque B, E. coli, Listeria |\n"
                "| Enfant 2 mois-6 ans | H. influenzae, **Méningocoque**, Pneumocoque |\n"
                "| Enfant > 6 ans et adulte jeune | **Méningocoque**, Pneumocoque |\n"
                "| Sujet > 50 ans | **Pneumocoque**, Méningocoque, Listeria, BGN |\n"
                "| Immunodéprimé | Germes habituels + BK, Cryptocoque, Nocardia |\n"
                "| Post-neurochirurgie | Staphylocoque |\n"
                "| Brèche ostéo-méningée | **Pneumocoque** |\n"
            )),
            FicheRow(concept="LCS purulent", detail_md=(
                "- Aspect trouble, « eau de riz », purulent\n"
                "- Hypercytose > **500 éléments**, PNN altérés prédominants\n"
                "- Hyperprotéinorachie > **1 g/L**\n"
                "- **Hypoglycorachie** < 0,4 fois glycémie capillaire\n"
                "- Élévation acide lactique"
            )),
            FicheRow(concept="PEC initiale", detail_md=(
                "- **ATB IV** dans l'heure, bactéricide, forte dose\n"
                "- Commencer **avant PL** si : purpura fulminans, PEC hospitalière > 90 min, CI PL\n"
                "- Probabiliste : enfant > 3 mois : **C3G** ; adulte : + amoxicilline si argument pour Listeria\n"
                "- **Corticothérapie** : DXM IV 10 mg/6h, débutée 10-20 min avant 1re injection ATB, 4 jours\n"
                "- Arrêter DXM si méningocoque chez enfant"
            )),
            FicheRow(concept="◆ Méningite à méningocoque", detail_md=(
                "- Cause la plus fréquente en France (1 000/an), sérotypes **B** (60%), C (30%)\n"
                "- Terrain : enfant, adulte jeune, notion de contage\n"
                "- Arguments : herpès naso-labial, arthralgies fugaces, **purpura**\n"
                "- Diplocoque **Gram-** encapsulé\n"
                "- Traitement : amoxicilline 200 mg/kg/j IV, **4-7 jours**\n"
                "- Prophylaxie contacts : **rifampicine 2 jours** + vaccination si sérotype A/C"
            )),
            FicheRow(concept="★ ◆ Méningite à pneumocoque", detail_md=(
                "- 2e cause, **la plus grave** en morbi-mortalité\n"
                "- Terrain : sujet âgé, diabète, OH, splénectomie, brèche ostéo-méningée\n"
                "- Diplocoque **Gram+** encapsulé\n"
                "- Traitement : **céfotaxime** 200-300 mg/kg/j, 10-14 jours\n"
                "- + Vancomycine si gravité ou suspicion pneumocoque résistant"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Indications au scanner **avant** PL : signes focaux, Glasgow < 11, crises épileptiques, signes d'engagement\n"
                "- ⚠ Ne jamais retarder l'ATB : commencer avant la PL si celle-ci est retardée"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE IV : PALUDISME ──
    partie_iv = Partie(numero="IV", titre="Paludisme", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et diagnostic", rows=[
            FicheRow(concept="Épidémiologie", detail_md=(
                "- **4 000 cas/an** en France (paludisme d'importation)\n"
                "- Agent : protozoaires du genre **Plasmodium**\n"
                "- 5 espèces : **P. falciparum** (le plus grave, incubation 7j-3 mois), P. vivax, P. ovale, P. malariae, P. knowlesi\n"
                "- Réservoir strictement **humain**\n"
                "- Transmission : piqûre de moustique **anophèle**\n"
                "- Zones : Afrique centrale/sud, Asie du Sud, Amérique centrale et du Sud"
            )),
            FicheRow(concept="Clinique", detail_md=(
                "- **Fièvre** par accès avec frissons, sueurs, sensation de froid\n"
                "  - Fièvre **tierce** (P. falciparum, vivax, ovale) ou **quarte** (P. malariae)\n"
                "- Ictère, splénomégalie (évolution prolongée)\n"
                "- Céphalées, myalgies\n"
                "- **Troubles digestifs** : NV, diarrhées +++"
            )),
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- Signes d'orientation : **thrombopénie** constante, +/- leucopénie, CRP > 100, anémie hémolytique\n"
                "- Pas d'hyperéosinophilie\n"
                "- Confirmation : **frottis sanguin + goutte épaisse** (examen de référence, en urgence)\n"
                "  - Diagnostic positif + espèce + **parasitémie**\n"
                "- Tests de diagnostic rapide (bandelettes) : sensibilité 98%, reste positif 2-3 semaines"
            )),
            FicheRow(concept="", detail_md=(
                "- Toute **fièvre au retour de zone d'endémie** est un paludisme jusqu'à preuve du contraire\n"
                "- Le frottis/goutte épaisse doit être fait en **urgence**, sans attendre le pic fébrile"
            ), kind="a_retenir"),
            FicheRow(concept="Critères de gravité (P. falciparum)", detail_md=(
                "- Terrain à risque : enfant, femme enceinte, sujet âgé, splénectomisé, ID\n"
                "- Critères d'hospitalisation : tout signe de gravité, plaquettes < 50 000, Hb < 10 g/dL, créatinine > 150, **parasitémie > 2%**"
            )),
        ]),
        SousPartie(lettre="B", titre="Prise en charge et prophylaxie", rows=[
            FicheRow(concept="Traitement paludisme non grave", detail_md=(
                "| Ligne | Médicaments | Voie |\n"
                "|-------|------------|------|\n"
                "| 1re intention | **Atovaquone-proguanil** (Malarone) OU **Artéméther-luméfantrine** (Riamet) OU Dihydroartémisine-pipéraquine | PO |\n"
                "| 2e intention | Méfloquine PO OU Quinine PO | PO |\n"
                "| Vomissements | Quinine IVL dans sérum glucosé, relais PO dès possible | IV |\n"
            )),
            FicheRow(concept="Traitement paludisme grave", detail_md=(
                "- **Artésunate IV** en 1re intention : H0, H12, H24 puis 1x/24h, max 7 jours\n"
                "- Relais PO dès que possible avec bithérapie\n"
                "- Alternative : quinine IV (dose de charge), surveillance hypoglycémie et ECG"
            )),
            FicheRow(concept="Suivi", detail_md=(
                "- Frottis goutte épaisse à **J3, J7 et J28**\n"
                "- Surveillance hématologique 1 mois si artésunate IV (hémolyse retardée)\n"
                "- DO si paludisme autochtone en métropole"
            )),
            FicheRow(concept="Prophylaxie", detail_md=(
                "- **Protection anti-vectorielle** : vêtements couvrants dès la tombée du jour, moustiquaires imprégnées, répulsifs\n"
                "- **Chimioprophylaxie** selon zone : Atovaquone-proguanil, Doxycycline ou Méfloquine\n"
                "- Choix selon : zones visitées, durée séjour, ATCD personnels, grossesse, interactions\n"
                "- Séjours > 3 mois : chimioprophylaxie les 6 premiers mois"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Doxycycline CI chez l'enfant < 8 ans et la femme enceinte\n"
                "- ⚠ Méfloquine CI si troubles psychiatriques, ATCD convulsions"
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE V : VACCINATIONS ──
    partie_v = Partie(numero="V", titre="Vaccinations", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et vaccins obligatoires du nourrisson", rows=[
            FicheRow(concept="Types de vaccins", detail_md=(
                "| Type | Principe | Exemples | CI majeure |\n"
                "|------|---------|----------|------------|\n"
                "| Vivants atténués | Agents à virulence réduite | BCG, **ROR**, Varicelle, Fièvre jaune | **Immunodépression** |\n"
                "| Inactivés | Agents inaptes à multiplication | Poliomyélite, Hépatite A, Grippe | Allergie dose précédente |\n"
                "| Sous-unités | Ag purifiés +/- adjuvant | DTP, Coqueluche, Hépatite B, Pneumocoque | Allergie dose précédente |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Les vaccins vivants sont **contre-indiqués** chez les immunodéprimés (risque de déclencher la maladie)\n"
                "- CI générale : réaction allergique lors d'une administration antérieure"
            ), kind="a_retenir"),
            FicheRow(concept="Vaccins obligatoires du nourrisson", detail_md=(
                "- **DTP** (Diphtérie-Tétanos-Polio) : 2 mois, 4 mois, rappel 11 mois\n"
                "- **Coqueluche** : intégré au DTP (vaccin acellulaire), stratégie du **cocooning**\n"
                "- **Haemophilus influenzae b** : 2 mois, 4 mois, rappel 11 mois\n"
                "- **Hépatite B** : intégré à l'hexavalent, obligatoire nourrissons et professionnels de santé\n"
                "- **Pneumocoque** : obligatoire < 2 ans (conjugué 13-valent)\n"
                "- **ROR** : obligatoire, 2 doses (12 mois et 16-18 mois)\n"
                "- **Méningocoque C** : obligatoire à 12 mois, rattrapage jusqu'à 24 ans"
            )),
            FicheRow(concept="◆ Rappels DTP adulte", detail_md=(
                "- **25 ans** : dTcaPolio\n"
                "- Puis tous les **20 ans** jusqu'à 65 ans (45 et 65 ans)\n"
                "- Puis tous les **10 ans** à partir de 65 ans"
            )),
        ]),
        SousPartie(lettre="B", titre="Vaccins recommandés et populations ciblées", rows=[
            FicheRow(concept="Grippe", detail_md=(
                "- Vaccin inactivé, adapté chaque année, CI : allergie à l'oeuf\n"
                "- Recommandé : > 65 ans, femmes enceintes, patients > 6 mois avec comorbidités\n"
                "- IMC > 40, entourage nourrissons < 6 mois à risque, personnel soignant"
            )),
            FicheRow(concept="Pneumocoque > 2 ans", detail_md=(
                "- Recommandé si : asplénisme, déficits immunitaires, VIH, chimiothérapie\n"
                "- IRC, BPCO, asthme sévère, diabète non équilibré, cardiopathies\n"
                "- Schéma : vaccin conjugué **13-valent** puis polyosidique **23-valent** tous les 5 ans"
            )),
            FicheRow(concept="Varicelle", detail_md=(
                "- Vaccin vivant atténué, CI : immunodépression\n"
                "- Recommandé : adolescents 12-18 ans sans ATCD varicelle, femmes en âge de procréer\n"
                "- Test de grossesse obligatoire, contraception 3 mois après injection"
            )),
            FicheRow(concept="Papillomavirus (HPV)", detail_md=(
                "- Vaccins inactivés, recommandés filles et garçons **11-14 ans**\n"
                "- Rattrapage 15-19 ans (3 doses)\n"
                "- Recommandé jusqu'à 26 ans chez les HSH"
            )),
            FicheRow(concept="Autres vaccins", detail_md=(
                "- **Hépatite A** : homosexuels masculins, enfants de familles originaires zones d'endémie, mucoviscidose\n"
                "- **BCG** : recommandé (non obligatoire) chez enfants à risque (Ile-de-France, Guyane, Mayotte)\n"
                "- **Zona** : vaccin vivant, recommandé 65-74 ans (CI si ID)\n"
                "- **Fièvre jaune** : obligatoire Guyane, vaccin vivant, protection à vie"
            )),
        ]),
    ])

    # ── PARTIE VI : INFECTIONS SPÉCIFIQUES ──
    partie_vi = Partie(numero="VI", titre="Infections spécifiques", sous_parties=[
        SousPartie(lettre="A", titre="Grippe", rows=[
            FicheRow(concept="Virologie et épidémiologie", detail_md=(
                "- Myxovirus influenzae (Orthomyxoviridae), 3 types : **A** (réservoir oiseaux), B, C\n"
                "- Glycoprotéines : **Hémagglutinine** (HA) et **Neuraminidase** (NA)\n"
                "- Transmission inter-humaine : gouttelettes (directe) et manuportage (indirect)\n"
                "- Saison en France : **novembre à février**"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Incubation : **1-3 jours**, contagiosité 1j avant et 6j après symptômes\n"
                "- Invasion brutale : malaise général fébrile, frissons, myalgies, céphalées\n"
                "- État : fièvre **39-40°C**, congestion nasale, toux sèche, arthralgies\n"
                "- Guérison : asthénie et toux résiduelles de plusieurs semaines"
            )),
            FicheRow(concept="", detail_md=(
                "- Apparition brutale de **toux fébrile de novembre à février** = grippe jusqu'à preuve du contraire"
            ), kind="a_retenir"),
            FicheRow(concept="Complications", detail_md=(
                "- **Respiratoires** : OMA, sinusite, pneumonie bactérienne secondaire (S. aureus, S. pneumoniae, J5-7)\n"
                "- Grippe maligne primaire : SDRA d'un seul tenant\n"
                "- **Extra-respiratoires** : myocardite, encéphalite, rhabdomyolyse\n"
                "- Syndrome de **Reye** (enfant + aspirine + grippe B) : encéphalite + hépatite fulminante, mortalité 50%"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- Symptomatique : paracétamol, repos, hydratation\n"
                "- Si surinfection bactérienne : **amoxicilline-ac. clavulanique** 7 jours\n"
                "- Inhibiteurs de la neuraminidase : **oseltamivir** PO ou zanamivir inhalé\n"
                "  - Dans les **48 premières heures** ; curatif 5 jours, prophylaxie 10 jours\n"
                "- Vaccination annuelle essentielle ++"
            )),
        ]),
        SousPartie(lettre="B", titre="Infection VIH", rows=[
            FicheRow(concept="Épidémiologie", detail_md=(
                "- France : **150 000** personnes infectées dont 30 000 l'ignorent, 6 500 nouvelles contaminations/an\n"
                "- Transmission : sexuelle ++, sanguine (AES, partage matériel injection), mère-enfant\n"
                "- Risque majoré si : rapport anal, lésion génitale, charge virale élevée, co-existence IST"
            )),
            FicheRow(concept="Primo-infection", detail_md=(
                "- 10-15 jours après contamination, guérison spontanée en 1-3 semaines\n"
                "- Syndrome rétro-viral aigu (90%) : fièvre, sueurs, myalgies, céphalées, pharyngodynie\n"
                "- **Exanthème** (60-70%) : maculopapuleux morbilliforme, tronc et racine des membres\n"
                "- PolyADP ferme et indolore (75%)\n"
                "- Signes neurologiques (20%) : syndrome méningé, PFP, polyradiculonévrite\n"
                "- Biologie : leucopénie, **thrombopénie** (75%), cytolyse hépatique"
            )),
            FicheRow(concept="Diagnostic", detail_md=(
                "- Sérologie VIH : test **ELISA** combiné (Ac + Ag p24)\n"
                "  - Si positif : confirmation par **Western Blot** + 2e sérologie sur 2e prélèvement\n"
                "  - Si négatif : éliminer fenêtre sérologique (15 jours)\n"
                "- Primo-infection : si ELISA négatif/douteux → recherche **ARN VIH plasmatique** (CV)\n"
                "- Bilan initial : CD4 + charge virale + test génotypique de résistance + HLA-B*5701"
            )),
            FicheRow(concept="◆ Infections opportunistes", detail_md=(
                "- **Pneumocystose** (CD4 < 200) : toux sèche, dyspnée progressive, PID bilatérale, verre dépoli au TDM\n"
                "  - Traitement : **Bactrim forte dose** 21j + corticothérapie si PaO2 < 70 mmHg\n"
                "- **Tuberculose** : quel que soit le taux de CD4, atteinte extra-pulmonaire dans 75%\n"
                "- Prophylaxie primaire Pneumocystis : **Bactrim** si CD4 < 200"
            )),
            FicheRow(concept="Traitement antirétroviral", detail_md=(
                "- Indication : **tous** les patients infectés VIH quel que soit le taux de CD4\n"
                "- Objectif : CV **indétectable** (< 50 copies/mL) et CD4 > 500/mm3\n"
                "- 1re intention : **trithérapie** en 1 prise/jour (2 INTI + 1 INNTI ou IP ou INI)\n"
                "- Prescription initiale **hospitalière**, traitement **à vie**\n"
                "- Suivi : CV + CD4 à 2-4 semaines puis tous les 3-6 mois"
            )),
            FicheRow(concept="Prévention", detail_md=(
                "- **TPE** (traitement post-exposition) : dans les heures suivant un risque significatif\n"
                "- **PrEP** (prophylaxie pré-exposition) : ténofovir + emtricitabine, surtout HSH\n"
                "- Prévention mère-enfant : traitement ARV maternel + prophylaxie néonatale 2 semaines\n"
                "- DO anonyme, ALD, éducation thérapeutique"
            )),
        ]),
        SousPartie(lettre="C", titre="Syphilis", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- IST à **Treponema pallidum**, non immunisante, très contagieuse\n"
                "- Transmission : sexuelle +++, materno-foetale (2e moitié grossesse)\n"
                "- Population à risque : HSH, co-infection VIH"
            )),
            FicheRow(concept="Syphilis primaire", detail_md=(
                "- Incubation 10-90 jours (moyenne 3 semaines)\n"
                "- **Chancre** : exulcération **indurée, indolore**, unique, au point d'inoculation\n"
                "  - Homme : sillon balano-préputial ; Femme : vulve\n"
                "  - Très contagieux, régression spontanée sans séquelles en quelques semaines\n"
                "- ADP satellite non inflammatoire, unilatérale"
            )),
            FicheRow(concept="Syphilis secondaire", detail_md=(
                "- Diffusion systémique, durée < 1 an\n"
                "- **Roséole** : macules rose pâle disséminées sur tronc, disparition en 7-10 jours\n"
                "- **Syphilides papuleuses** : papules cuivrées avec collerette de **Biett**\n"
                "  - Syphilides **palmo-plantaires** (30%) : très évocatrices\n"
                "  - Syphilides génitales/périnéales : très contagieuses\n"
                "- Alopécie en fourrure mitée, dépapillation linguale"
            )),
            FicheRow(concept="Diagnostic sérologique", detail_md=(
                "- Association : **TPHA** (spécifique tréponématose) + **VDRL** (non spécifique)\n"
                "- Se positivent à J8-10 du chancre\n"
                "- TPHA+/VDRL+ : tréponématose vénérienne ou non\n"
                "- Examen ophtalmo systématique si syphilis secondaire\n"
                "- PL si suspicion neurosyphilis : VDRL positif dans LCS"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- Syphilis précoce : **benzathine pénicilline G** IM injection unique\n"
                "- Syphilis tardive : benzathine péni G IM x 3 injections (J0, J7, J15)\n"
                "- Neurosyphilis : **pénicilline G IV** 16 MUI/j pendant 15 jours\n"
                "- Allergie péni : doxycycline (ou désensibilisation si grossesse/VIH)\n"
                "- Réaction de **Herxheimer** : fièvre, céphalées, myalgies après injection (lyse tréponèmes)"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Suivi VDRL quantitatif : doit être divisé par **4** à 6 mois\n"
                "- Rechercher systématiquement les **autres IST** : VIH, VHB, VHC, gonocoque, Chlamydia"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Zoonoses et voyage en pays tropical", rows=[
            FicheRow(concept="Maladie de Lyme", detail_md=(
                "- Borrelia burgdorferi, transmission par **tiques Ixodes**\n"
                "- Phase primaire : **érythème migrant** (pathognomonique) centrifuge, 10-30 cm\n"
                "- Phase secondaire : arthrite genou, méningoradiculite, **PF**, myocardite, lymphocytome\n"
                "- Phase tertiaire : **acrodermatite chronique atrophiante**, atteinte neurologique chronique\n"
                "- Traitement : phase I amoxicilline/doxycycline 14-21j ; phases II-III ceftriaxone 21-28j"
            )),
            FicheRow(concept="Pasteurellose et griffes du chat", detail_md=(
                "- **Pasteurellose** : Pasteurella multocida, morsure/griffure chat/chien\n"
                "  - Incubation rapide (3-6h), inflammation autour plaie\n"
                "  - Traitement : amoxicilline 10-14 jours\n"
                "- **Maladie des griffes du chat** : Bartonella henselae, enfant 80%\n"
                "  - ADP satellite 2-4 semaines après griffure, +/- fièvre\n"
                "  - Évolution spontanément favorable en 2-3 mois, si traitement : azithromycine 5j"
            )),
            FicheRow(concept="★ TIAC", detail_md=(
                "- Au moins **2 cas groupés** d'origine alimentaire commune, **DO** obligatoire\n"
                "- Syndrome dysentérique (entéro-invasif) : Salmonella, Campylobacter, incubation longue\n"
                "- Syndrome cholériforme (entéro-toxinogène) : S. aureus (2-4h), C. perfringens (9-15h)\n"
                "- **Botulisme** : conserves artisanales, syndrome parasympatholytique\n"
                "- CAT : conserver aliments 3 derniers jours, coproculture, déclaration ARS"
            )),
            FicheRow(concept="◆ Fièvre au retour de zone tropicale", detail_md=(
                "- **Paludisme** toujours en premier\n"
                "- < 7j : diarrhées infectieuses, dengue\n"
                "- 7-14j : paludisme, fièvre typhoïde, rickettsioses\n"
                "- > 14j : paludisme, primo-infection VIH, hépatites virales\n"
                "- Avec signes hémorragiques : penser fièvres hémorragiques virales (isolement strict)"
            )),
            FicheRow(concept="◆ Fièvre typhoïde", detail_md=(
                "- Salmonella Typhi, incubation 7-14 jours\n"
                "- Céphalées intenses, insomnie, pouls dissocié, splénomégalie\n"
                "- Fièvre en plateau à 40°C en 3e semaine\n"
                "- Confirmation : hémocultures + coproculture"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Antibiotiques — Principales classes et caractéristiques", markdown=(
            "| Classe | Mode d'action | Type | Particularités clés |\n"
            "|--------|--------------|------|--------------------|\n"
            "| Bêta-lactamines | Inhibition paroi (PLP) | Bactéricide, temps-dépendant | Allergie croisée, mauvaise diffusion SNC |\n"
            "| Aminosides | Inhibition synthèse protéique | Bactéricide, concentration-dépendant | Néphro/ototoxicité, voie IV |\n"
            "| Macrolides | Inhibition synthèse protéique | Bactériostatique | Allongement QT, interactions |\n"
            "| Fluoroquinolones | Inhibition synthèse ADN | Bactéricide | Tendinopathies, excellente biodispo orale |\n"
            "| Glycopeptides | Inhibition paroi | Bactéricide | Anti-Gram+ seul, néphrotoxicité |\n"
            "| Cyclines | Inhibition synthèse protéique | Bactériostatique | Phototoxicité, CI enfant < 8 ans |\n"
            "| Rifampicine | Inhibition synthèse ARN | Bactéricide | Jamais en monothérapie, interactions |\n"
        )),
        TableauSynthese(titre="LCS — Orientation étiologique", markdown=(
            "| Caractéristique | Méningite purulente | Listeria/BK | Virale | Herpétique |\n"
            "|----------------|--------------------|-----------:|-------:|-----------:|\n"
            "| Aspect | Trouble/purulent | Clair | Clair | Clair |\n"
            "| Cytologie | > 500 PNN | 200-300 Lympho/panachée | Lymphocytaire | Lymphocytaire < 500 |\n"
            "| Protéinorachie | > 1 g/L | Modérée (BK > 1g/L) | < 1 g/L | < 1 g/L |\n"
            "| Glycorachie | Basse (< 0,4x gly) | Basse | Normale | Normale |\n"
            "| Germe | Gram+/Gram- | BG+ / BAAR | Négatif | PCR HSV+ |\n"
        )),
        TableauSynthese(titre="Méningites purulentes — Germes selon terrain", markdown=(
            "| Terrain | 1er germe | 2e germe | Autres |\n"
            "|---------|----------|---------|--------|\n"
            "| NN < 2 mois | Streptocoque B | E. coli | Listeria |\n"
            "| Enfant 2 mois-6 ans | Méningocoque | Pneumocoque | H. influenzae |\n"
            "| Adulte jeune | Méningocoque | Pneumocoque | |\n"
            "| Sujet > 50 ans | Pneumocoque | Méningocoque | Listeria, BGN |\n"
            "| Brèche ostéo-méningée | Pneumocoque | | |\n"
        )),
        TableauSynthese(titre="Vaccins obligatoires du nourrisson", markdown=(
            "| Vaccin | Âge primo-vaccination | Rappel | Type |\n"
            "|--------|----------------------|--------|------|\n"
            "| DTP | 2 mois, 4 mois | 11 mois | Inactivé |\n"
            "| Coqueluche | 2 mois, 4 mois | 11 mois | Sous-unité |\n"
            "| H. influenzae b | 2 mois, 4 mois | 11 mois | Conjugué |\n"
            "| Hépatite B | 2 mois, 4 mois | 11 mois | Recombinant |\n"
            "| Pneumocoque | 2 mois, 4 mois | 11 mois | Conjugué 13-valent |\n"
            "| ROR | 12 mois | 16-18 mois | Vivant atténué |\n"
            "| Méningocoque C | 12 mois | | Conjugué |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Fièvre aiguë | T°C > **38°C** matin / **38,3°C** soir | Définition |\n"
        "| Fièvre prolongée | > **20 jours** | Définition |\n"
        "| Neutropénie fébrile | PNN < **500/mm3** + T > 38,3°C | Définition |\n"
        "| Paludisme France | **4 000** cas/an | Importation |\n"
        "| Parasitémie grave | > **2%** | Critère hospitalisation |\n"
        "| VIH France | **150 000** infectés, 30 000 l'ignorent | Épidémiologie |\n"
        "| CV cible VIH | < **50** copies/mL | Objectif traitement |\n"
        "| CD4 cible VIH | > **500/mm3** | Objectif traitement |\n"
        "| Prophylaxie Pneumocystis | CD4 < **200/mm3** | Bactrim |\n"
        "| Mortalité méningite Listeria | **30%** | Malgré traitement |\n"
        "| Mortalité méningite BK | **25%** | Malgré traitement |\n"
        "| Méningocoque : sérotype B | **60%** en France | Épidémiologie |\n"
        "| Méningo-encéphalite HSV mortalité | **15%** traité / **80%** non traité | Pronostic |\n"
        "| Aciclovir posologie | **10 mg/kg/8h** IV pendant 15-21j | Herpès neuroméningé |\n"
        "| DTP rappel adulte | Tous les **20 ans** puis **10 ans** après 65 ans | Calendrier vaccinal |\n"
    ))

    points_cles = [
        "Toute fièvre au retour de zone d'endémie est un **paludisme** jusqu'à preuve du contraire (frottis/GE en urgence)",
        "Toute confusion fébrile est une **méningo-encéphalite herpétique** JPDC : aciclovir IV sans attendre",
        "Les vaccins **vivants** sont contre-indiqués chez l'immunodéprimé",
        "La **neutropénie fébrile** impose une ATB urgente bactéricide à large spectre après prélèvements",
        "L'endocardite et la tuberculose sont les 2 premières causes infectieuses de **fièvre prolongée**",
        "Le traitement ARV du VIH est indiqué chez **tous** les patients, quel que soit le taux de CD4",
        "La syphilis primaire se traite par **benzathine pénicilline G** IM en injection unique",
        "Les C3G ont une résistance naturelle de la **Listeria** : toujours ajouter amoxicilline si suspicion",
    ]

    fiche_eclair_md = (
        "**Antibiotiques** : Bêta-lactamines (inhibition paroi, bactéricides). C3G = référence BGN "
        "mais résistance naturelle Listeria/entérocoques. Aminosides = concentration-dépendants, "
        "néphro/ototoxicité. FQ = excellente biodispo orale mais tendinopathies, jamais en monothérapie.\n\n"
        "**Fièvre** : Aiguë < 5j (infectieuse ++), prolongée > 20j (endocardite, BK, cancer, Horton). "
        "Neutropénie fébrile (PNN < 500 + T > 38,3°C) = ATB urgente bétalactamine antipyocyanique.\n\n"
        "**Méningites** : Purulente = C3G IV + DXM dans l'heure. Méningocoque (Gram-, B 60%) vs "
        "Pneumocoque (Gram+, le plus grave). Listeria = amoxicilline + aminosides. BK = quadrithérapie. "
        "Herpès = aciclovir 10 mg/kg/8h 21j dès suspicion.\n\n"
        "**Paludisme** : P. falciparum le plus grave. Frottis/GE en urgence. Non grave = Malarone/Riamet PO. "
        "Grave = artésunate IV. Prophylaxie = protection vectorielle + chimioprophylaxie.\n\n"
        "**VIH** : Trithérapie pour tous, CV < 50 copies/mL. Pneumocystose si CD4 < 200 = Bactrim. "
        "Primo-infection = syndrome pseudo-grippal + exanthème + thrombopénie.\n\n"
        "**Vaccinations** : 11 vaccins obligatoires nourrisson. Vivants CI si ID. DTP rappel 20 ans puis 10 ans.\n\n"
        "**Syphilis** : Chancre induré indolore. TPHA + VDRL. Benzathine péni G IM.\n\n"
        "**Lyme** : Érythème migrant pathognomonique. Amoxicilline phase I, ceftriaxone phases II-III."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Infectiologie",
        annee="2025-2026",
        item="Items 148, 151, 166, 169, 171, 173, 326",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()

    # Images : charger depuis image_captions.json si disponible
    captions_file = PROJECT_ROOT / "output" / ".work" / "infectiologie" / "image_captions.json"
    if captions_file.exists():
        # Image loading code placeholder
        pass

    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Medecine_generale_infectiologie_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out} ({pdf_out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()

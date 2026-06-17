"""Génère la fiche de l'Item 225 - Artériopathie de l'aorte, des artères viscérales et des membres inférieurs ; anévrismes (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Artériopathie de l'aorte et des artères viscérales", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités"),
            PlanSousPartie(lettre="B", titre="Ischémie mésentérique chronique"),
            PlanSousPartie(lettre="C", titre="Ischémie mésentérique aiguë"),
        ]),
        PlanPartie(numero="II", titre="Artériopathie oblitérante des membres inférieurs (AOMI)", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et épidémiologie"),
            PlanSousPartie(lettre="B", titre="Clinique"),
            PlanSousPartie(lettre="C", titre="Examens paracliniques"),
            PlanSousPartie(lettre="D", titre="Diagnostics différentiel et étiologique"),
            PlanSousPartie(lettre="E", titre="Traitement, stratégie et pronostic"),
        ]),
        PlanPartie(numero="III", titre="Ischémie aiguë des membres inférieurs", sous_parties=[
            PlanSousPartie(lettre="A", titre="Physiopathologie"),
            PlanSousPartie(lettre="B", titre="Diagnostic positif et étiologique"),
            PlanSousPartie(lettre="C", titre="Évaluation du terrain"),
            PlanSousPartie(lettre="D", titre="Traitement"),
        ]),
        PlanPartie(numero="IV", titre="Anévrismes", sous_parties=[
            PlanSousPartie(lettre="A", titre="Anévrisme de l'aorte abdominale (AAA)"),
            PlanSousPartie(lettre="B", titre="Anévrisme de l'artère poplitée (AP)"),
        ]),
    ]

    # ── PARTIE I : ARTÉRIOPATHIE DE L'AORTE ET ARTÈRES VISCÉRALES ──
    partie_i = Partie(numero="I", titre="Artériopathie de l'aorte et des artères viscérales", sous_parties=[
        SousPartie(lettre="A", titre="Généralités", rows=[
            FicheRow(concept="◆ Athérome aortique", detail_md=(
                "- L'aorte peut être le siège de lésions d'**athérome dès le jeune âge** "
                "(stries lipidiques, plaques jeunes)\n"
                "- Tous les segments de l'aorte peuvent être atteints, sièges préférentiels :\n"
                "  - Bifurcation aortique (naissance des artères iliaques)\n"
                "  - Origine de toute branche naissante de l'aorte\n"
                "- À l'imagerie : plaques chez **25 % des hommes** et **20 % des femmes** de 40-55 ans\n"
                "- Le **tabagisme** est le facteur le plus fortement associé à ces lésions"
            )),
            FicheRow(concept="Expression clinique", detail_md=(
                "- Le plus souvent asymptomatiques\n"
                "- Traduction clinique possible :\n"
                "  - Ulcération de la paroi\n"
                "  - **Phénomènes emboliques** (matériel fibrinocruorique) → cerveau (aorte ascendante/horizontale), "
                "membres ou viscères abdominales\n"
                "- Le plus souvent découverte fortuite sur imagerie thoracique/abdominale (calcifications)"
            )),
            FicheRow(concept="◆ Marqueur de risque CV", detail_md=(
                "- La présence de plaques aortiques est un **marqueur de risque cardiovasculaire**\n"
                "- Le risque CV global augmente avec la présence et l'extension des calcifications, "
                "même asymptomatiques\n"
                "- Souvent associées à d'autres atteintes (coronaires, digestives, rénales)"
            )),
            FicheRow(concept="Sténoses des branches viscérales", detail_md=(
                "- **Artères rénales** : sténose → ischémie rénale → activation du SRAA → "
                "**HTA rénovasculaire** (étiologie d'HTA secondaire, cf. chapitre 4)\n"
                "- Tronc cœliaque, artère mésentérique supérieure, inférieure : "
                "ischémie digestive (mésentérique) chronique ou aiguë"
            )),
        ]),
        SousPartie(lettre="B", titre="Ischémie mésentérique chronique", rows=[
            FicheRow(concept="◆ Signes cliniques", detail_md=(
                "- **Angor digestif** typique : douleurs abdominales après le repas\n"
                "- Formes graves : altération de l'état général et amaigrissement "
                "(patient limite ses repas pour éviter la douleur)\n"
                "- Signes physiques limités : éventuel souffle abdominal évoquant une sténose viscérale"
            )),
            FicheRow(concept="Examens paracliniques", detail_md=(
                "- Diagnostic de sténose par :\n"
                "  - Échodoppler des artères digestives\n"
                "  - Angioscanner ou angio-IRM\n"
                "- **Artériographie** : réservée à la procédure de revascularisation endovasculaire"
            )),
            FicheRow(concept="Prise en charge et traitement", detail_md=(
                "- **Revascularisation** dans les meilleurs délais\n"
                "  - Préférentiellement endovasculaire (angioplastie + stenting) si possible\n"
                "  - Chirurgie à ciel ouvert si endovasculaire impossible\n"
                "- Prise en charge nutritionnelle si nécessaire en post-revascularisation\n"
                "- **Antiplaquettaire au long cours**"
            )),
        ]),
        SousPartie(lettre="C", titre="Ischémie mésentérique aiguë", rows=[
            FicheRow(concept="⚠ Définition - Urgence vitale", detail_md=(
                "- Interruption brutale de perfusion d'une partie des intestins par occlusion artérielle\n"
                "- Mécanismes : thrombose in situ ou embolie\n"
                "- Infarctus digestif rare (nombreuses collatéralités)\n"
                "- **Urgence vitale** : pronostic dépend de la rapidité de la prise en charge"
            )),
            FicheRow(concept="◆ Triade clinique", detail_md=(
                "- Occlusion mésentérique typique = triade associant :\n"
                "  - Douleur abdominale aiguë avec **paucité de signes physiques**\n"
                "  - Vidange digestive accélérée (vomissements et/ou diarrhée)\n"
                "  - Indices d'étiologie embolique (notamment **fibrillation atriale**)\n"
                "- Signes d'embolie dans d'autres territoires renforcent la présomption embolique\n"
                "- Formes frustes possibles → errances diagnostiques"
            )),
            FicheRow(concept="Examens paracliniques", detail_md=(
                "- D-dimères augmentés (non spécifique) → leur dosage ne doit pas retarder l'imagerie\n"
                "- **Lactates** augmentés : signe **tardif** évoquant la nécrose digestive\n"
                "- ASP ou échographie abdominale : normales ou stase digestive (peu spécifique)\n"
                "- **Angioscanner = examen de référence** :\n"
                "  - Interruption de produit de contraste dans une artère proximale\n"
                "  - Épaississement de la paroi intestinale avec œdème, dilatation\n"
                "  - Pneumatose intestinale, air dans la veine porte\n"
                "  - Présence d'ascite"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Résection** des segments intestinaux infarcis\n"
                "- Geste de revascularisation quand possible (endovasculaire ou chirurgicale)"
            )),
            FicheRow(concept="", detail_md=(
                "- L'ischémie mésentérique aiguë est une **urgence chirurgicale**.\n"
                "- Triade : douleur abdominale + troubles digestifs + cause embolique (FA).\n"
                "- **Angioscanner** confirme le diagnostic.\n"
                "- Traitement = résection des nécroses + revascularisation."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE II : ARTÉRIOPATHIE OBLITÉRANTE DES MEMBRES INFÉRIEURS (AOMI) ──
    partie_ii = Partie(numero="II", titre="Artériopathie oblitérante des membres inférieurs (AOMI)", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et épidémiologie", rows=[
            FicheRow(concept="◆ Définition", detail_md=(
                "- **AOMI** = toute atteinte athéromateuse significative touchant les artères entre "
                "l'aorte terminale et les artères digitales (orteils)\n"
                "- Lésions d'aspect et de développement semblables aux autres localisations athéromateuses\n"
                "- **3e localisation** de l'athérosclérose (après coronarienne et cérébrale)"
            )),
            FicheRow(concept="Épidémiologie", detail_md=(
                "- Forme symptomatique : plus fréquente chez l'homme que chez la femme\n"
                "- Pic de présentation : 60-75 ans chez l'homme, 70-80 ans chez la femme\n"
                "- Prévalence clinique : **1 à 5 % après 60 ans**\n"
                "- Avec formes asymptomatiques incluses : **10-15 %** dans cette tranche d'âge\n"
                "- Pour 1 cas symptomatique → 2 à 4 patients infracliniques (intérêt du dépistage)\n"
                "- > 1 million de personnes affectées en France\n"
                "- Incidence : **2-5 %**"
            )),
            FicheRow(concept="◆ Facteurs de risque", detail_md=(
                "- **Tabagisme** : principal FDR, plus fréquent chez le sujet jeune\n"
                "- **Diabète** : plus souvent responsable de formes graves d'emblée, "
                "atteinte plus distale et pronostic sévère\n"
                "- Hypercholestérolémie et HTA : autres FDR fréquemment associés"
            )),
        ]),
        SousPartie(lettre="B", titre="Clinique", rows=[
            FicheRow(concept="◆ Histoire naturelle - 2 stades", detail_md=(
                "- Phase asymptomatique prolongée (collatéralité compensatrice)\n"
                "- **Stade d'ischémie d'effort** : symptômes à l'effort (hypoxie musculaire = débit insuffisant)\n"
                "- **Stade d'ischémie permanente** : souffrance hypoxique permanente "
                "(douleurs de décubitus, troubles trophiques)"
            )),
            FicheRow(concept="◆ Classifications", detail_md=(
                "- **Leriche et Fontaine** (historique) :\n"
                "  - Stade I : asymptomatique\n"
                "  - Stade II : claudication intermittente\n"
                "  - Stade III : douleurs de décubitus\n"
                "  - Stade IV : troubles trophiques (ulcères, gangrène)\n"
                "- **Rutherford** (classification internationale, supplante Leriche-Fontaine de nos jours)"
            )),
            FicheRow(concept="◆ Claudication intermittente typique", detail_md=(
                "- Douleur de type crampe au mollet apparaissant à la marche\n"
                "- Distance de gêne puis distance de marche (arrêt forcé)\n"
                "- **Disparition en < 5 min** au repos\n"
                "- Distance classiquement stable (terrain plat ou test de marche)\n"
                "- **Claudication sévère** si distance de marche **< 100 m**"
            )),
            FicheRow(concept="Formes atypiques", detail_md=(
                "- Distances variables d'un jour à l'autre\n"
                "- Autres localisations : pied, cuisse, fessière (atteintes aorto-iliaques)\n"
                "- Douleurs faibles, parfois de repos et d'effort\n"
                "- Paresthésie ou engourdissement d'effort\n"
                "- Sujet ralentit le pas sans s'arrêter"
            )),
            FicheRow(concept="⚠ AOMI masquée (forme grave)", detail_md=(
                "- Atteinte sévère peut rester asymptomatique :\n"
                "  - Circulation collatérale très développée\n"
                "  - Sujet âgé avec comorbidités l'empêchant de marcher (IC, IR, atteintes articulaires)\n"
                "  - **Neuropathie** altérant la sensibilité (diabète, insuffisance rénale, âge avancé)\n"
                "- Le patient peut présenter d'emblée une forme grave d'ischémie permanente\n"
                "- À distinguer de la forme purement asymptomatique → intérêt du **dépistage**"
            )),
            FicheRow(concept="◆ Ischémie permanente (stades III-IV)", detail_md=(
                "- **Stade III - Douleurs de décubitus** :\n"
                "  - Brûlures des orteils et avant-pied\n"
                "  - Apparaissent après quelques minutes/heures de décubitus\n"
                "  - **Amélioration en position déclive** → patient laisse jambes pendantes au bord du lit\n"
                "  - Douleurs intenses, insomnie, AEG, antalgiques croissants\n"
                "  - Examen : pied froid, pâle ou cyanosé, œdème de déclivité possible\n"
                "- **Stade IV - Troubles trophiques** :\n"
                "  - Peau mince, fragile, perte de pilosité\n"
                "  - Plaies, ulcères, gangrène très algiques\n"
                "  - Porte d'entrée à infections (cellulite, arthrite, ostéite, septicémie)"
            )),
            FicheRow(concept="Ulcères et gangrène artériels", detail_md=(
                "- **Ulcères** :\n"
                "  - Zones de frottement/appui : orteil, dos et bord externe du pied, talon\n"
                "  - Face antérieure de jambe (ulcère « suspendu »)\n"
                "  - Apparition spontanée ou post-traumatique mineur (pédicure agressive)\n"
                "  - Faible surface mais creusants (aponévrose, os)\n"
                "- **Gangrène** :\n"
                "  - Orteils ou talon, extension à l'avant-pied/jambe\n"
                "  - Plus fréquente chez le **diabétique**, souvent infectée"
            )),
            FicheRow(concept="◆ Ischémie critique", detail_md=(
                "- Englobe les stades III et IV avec douleurs durant > **15 jours**, résistant aux antalgiques\n"
                "- Définie par effondrement des pressions de perfusion :\n"
                "  - **Pression cheville < 50 mmHg**\n"
                "  - OU **pression hallux < 30 mmHg**\n"
                "- **Pronostic vital du membre engagé**"
            )),
            FicheRow(concept="◆ Syndrome de Leriche", detail_md=(
                "- Chez l'homme atteint d'AOMI\n"
                "- Associe :\n"
                "  - Claudication fessière et/ou fatigabilité à la marche\n"
                "  - **Impuissance** (troubles d'érection)\n"
                "- En rapport avec une **atteinte aorto-iliaque**"
            )),
            FicheRow(concept="Signes physiques (examen bilatéral et comparatif)", detail_md=(
                "- **Inspection** : couleur (normale, pâle, cyanosée), troubles trophiques (espaces interdigitaux)\n"
                "- **Palpation** :\n"
                "  - Pied froid\n"
                "  - Douleur à la pression des masses musculaires = ischémie sévère\n"
                "  - Pouls : fémoral, poplité, tibial postérieur, pédieux "
                "(absent dans **5 % de la population** de manière congénitale)\n"
                "  - Temps de recoloration cutanée allongé (normal **< 3 sec**)\n"
                "  - Recherche d'anévrisme abdominal et poplité systématique\n"
                "- **Auscultation** : souffle sur trajets vasculaires"
            )),
            FicheRow(concept="◆ Index de pression systolique (IPS)", detail_md=(
                "- Définition : rapport **PAS cheville / PAS bras**\n"
                "- Technique : brassard tensionnel + doppler de poche\n"
                "  - Mesure aux tibial postérieur et pédieux (chevilles)\n"
                "  - Fibulaire non mesurée (repérage difficile)\n"
                "  - Pression de cheville = pression la plus élevée des 2 artères\n"
                "  - Pression brachiale aux 2 bras\n"
                "- Valeurs :\n"
                "  - **Sain : IPS 1,00-1,40**\n"
                "  - **AOMI : IPS < 0,90** (sur au moins 1 cheville)\n"
                "  - **AOMI sévère : IPS < 0,70**\n"
                "  - **IPS > 1,40 = médiacalcose** (rigidité, calcification de la média sans rétrécissement, "
                "≠ athérosclérose, fréquente chez diabétique âgé/dialysé)\n"
                "- En cas de médiacalcose : remplacer par pression d'orteil (manchon adapté)\n"
                "  - **Index orteil < 0,70** = AOMI\n"
                "  - **Pression d'orteil < 30 mmHg** = ischémie critique\n"
                "- IPS aussi marqueur de risque CV : IPS < 0,90 = haut risque"
            )),
            FicheRow(concept="", detail_md=(
                "- L'examen clinique d'un AOMI **complète systématiquement** par interrogatoire et examen "
                "cardiovasculaire général.\n"
                "- Forte fréquence d'**atteintes coronarienne et cérébrovasculaire associées**."
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Examens paracliniques", rows=[
            FicheRow(concept="Objectifs", detail_md=(
                "- Évaluer objectivement le handicap fonctionnel\n"
                "- Apprécier la sévérité hémodynamique\n"
                "- Localiser les lésions artérielles"
            )),
            FicheRow(concept="◆ Test de marche", detail_md=(
                "- **Test de marche de 6 minutes** : non spécifique de l'AOMI (aussi IC, etc.), "
                "évaluation du handicap fonctionnel global\n"
                "- **Test sur tapis roulant (protocole de Strandness)** : "
                "**vitesse 3,2 km/h, pente 10 %**\n"
                "  - Évalue distance de gêne et distance de marche (suivi)\n"
                "  - Réévalue les pressions de cheville post-effort\n"
                "  - Sensibilise le diagnostic si IPS de repos > 0,90\n"
                "  - AOMI évoquée si **baisse PAS cheville > 30 mmHg** et/ou "
                "**baisse IPS > 20 %** après marche"
            )),
            FicheRow(concept="◆ Mesure de la TcPO₂", detail_md=(
                "- **TcPO₂** = pression transcutanée en oxygène\n"
                "- Évalue l'oxygénation cutanée\n"
                "- À l'état basal : PO₂ cutanée très basse (3-4 mmHg) → hyperémie par chaleur "
                "nécessaire pour artérialiser le flux\n"
                "- **Sujet sain : TcPO₂ dos du pied > 50 mmHg**\n"
                "- Interprétation :\n"
                "  - **> 35 mmHg** : bonne compensation métabolique\n"
                "  - **10-35 mmHg** : hypoxie continue\n"
                "  - **< 10 mmHg** : hypoxie critique"
            )),
            FicheRow(concept="◆ Échodoppler artériel des MI", detail_md=(
                "- **Exploration la plus utilisée** (non invasif)\n"
                "- Combine :\n"
                "  - Échographie : informations anatomiques (localisation, types de lésions)\n"
                "  - Doppler : données hémodynamiques (flux)\n"
                "- Identifie et quantifie la sévérité des lésions dans l'immense majorité des cas\n"
                "- Doppler normal : **flux triphasique**\n"
                "- Doppler pathologique : flux laminaire puis turbulent (en mosaïque) en cas de sténose"
            )),
            FicheRow(concept="Autres techniques d'imagerie", detail_md=(
                "- Indiquées seulement si revascularisation envisagée (étude faisabilité et modalités)\n"
                "- **Angioscanner** :\n"
                "  - Non invasif performant, étude chenal + paroi\n"
                "  - Nécessite PCI iodé → vérifier allergies, fonction rénale\n"
                "- **ARM (Angio-IRM)** :\n"
                "  - Alternative, évite radiations ionisantes\n"
                "  - **Gadolinium CI si clairance < 30 mL/min/1,73 m²**\n"
                "  - Limite : ne visualise pas les calcifications (gênant si pontage)\n"
                "- Sensibilité / spécificité angioscanner et ARM ≈ **95 %** (vs artériographie)\n"
                "- **Artériographie** :\n"
                "  - Examen invasif (ponction artérielle + PCI)\n"
                "  - Limitée aux procédures de revascularisation\n"
                "  - Souvent nécessaire pour réseau jambier et pédieux distal"
            )),
        ]),
        SousPartie(lettre="D", titre="Diagnostics différentiel et étiologique", rows=[
            FicheRow(concept="Diagnostics différentiels - Douleurs à la marche", detail_md=(
                "- **Neurologique** : canal lombaire étroit (paresthésies mollet/pied à l'effort, cèdent au repos), "
                "sciatalgie, atteinte médullaire\n"
                "- **Rhumatologique** : tendinite, arthrose, rhumatismes, anomalies posturostaturales\n"
                "- **Veineux** : claudication veineuse (post-thrombotique)\n"
                "- Piège poplité, kyste poplité, endofibrose iliaque\n"
                "- Syndrome des loges\n"
                "- Malformations vasculaires (artère ischiatique, fistules artérioveineuses)\n"
                "- **Musculaire** : douleurs musculaires sous statines (intrication possible)"
            )),
            FicheRow(concept="Diagnostics différentiels - Douleurs de décubitus", detail_md=(
                "- Neuropathie sensorielle (diabétiques, toxiques, carencielle)\n"
                "- Syndromes douloureux régionaux complexes (anciennes algodystrophies, causalgies)\n"
                "- Compression radiculaire"
            )),
            FicheRow(concept="Diagnostics différentiels - Ulcères", detail_md=(
                "- Veineux\n"
                "- Microcirculatoire\n"
                "- Neuropathique\n"
                "- Traumatique"
            )),
            FicheRow(concept="◆ Diagnostic étiologique - AOMI = athérome (> 95 %)", detail_md=(
                "- **AOMI = atteinte athéromateuse** des membres inférieurs (**> 95 %** des artériopathies "
                "oblitérantes des MI)"
            )),
            FicheRow(concept="Artériopathies non athéromateuses des MI", detail_md=(
                "- **Inflammatoires** :\n"
                "  - Maladie de Buerger\n"
                "  - Maladie de Takayasu\n"
                "  - Maladie de Horton\n"
                "  - Collagénoses : PAN (périartérite noueuse), lupus\n"
                "- Dysplasie fibromusculaire (iliaque ou poplité)\n"
                "- Coarctation de l'aorte (hypodébit en aval)\n"
                "- Atteintes postradiques\n"
                "- Atteintes post-traumatiques\n"
                "- Atteintes toxiques : dérivés de l'ergot de seigle\n"
                "- Gelures\n"
                "- Compressions extrinsèques\n"
                "- **Atteintes spécifiques de l'artère poplitée** :\n"
                "  - Artère poplitée piégée\n"
                "  - Kyste poplité sous-adventiciel"
            )),
        ]),
        SousPartie(lettre="E", titre="Traitement, stratégie et pronostic", rows=[
            FicheRow(concept="Principes généraux", detail_md=(
                "- **Traitement à visée générale** : améliorer pronostic CV et vital\n"
                "- **Traitement à visée locale** : résoudre symptômes, traiter ischémie, "
                "améliorer pronostic du membre"
            )),
            FicheRow(concept="◆ Traitement à visée générale - Contrôle des FDR", detail_md=(
                "- **Arrêt du tabac** : essentiel\n"
                "- **Contrôle du diabète** : essentiel\n"
                "- Cibles tensionnelles :\n"
                "  - **PAS ≤ 120-129 mmHg**\n"
                "  - **PAD ≤ 70-79 mmHg**\n"
                "  - IEC ou sartan peuvent être considérés quel que soit le niveau de PA (sauf CI)\n"
                "- **HbA1c < 7 %**\n"
                "- **LDL-C < 0,55 g/L (< 1,4 mmol/L)**\n"
                "- Régime méditerranéen\n"
                "- IMC entre 20 et 25 kg/m²\n"
                "- Exercice modéré\n"
                "- **Réentraînement : 3 fois/semaine pendant 12 semaines**"
            )),
            FicheRow(concept="◆ Traitement à visée générale - Médicaments", detail_md=(
                "- **Antiagrégant plaquettaire** (aspirine ou clopidogrel) :\n"
                "  - Systématique en AOMI symptomatique (réduit complications CV)\n"
                "  - AOMI asymptomatique : débattu, sauf si autre atteinte athéromateuse associée\n"
                "- Bithérapie **aspirine 75-100 mg/j + rivaroxaban 2,5 mg × 2/j** :\n"
                "  - Indication européenne, non remboursée en France\n"
                "  - En France : possible uniquement dans les 10 jours post-revascularisation MI\n"
                "- En cas d'anticoagulation curative indiquée + AOMI : "
                "conserver uniquement l'anticoagulation\n"
                "- **Statines systématiques** : objectif LDL-C < 0,55 g/L et réduction ≥ 50 %\n"
                "- **IEC** : intérêt pronostique, PA < 140/90 mmHg\n"
                "- **Bêtabloquants** : si indication formelle (cardiopathie ischémique, IC à FEVG altérée, "
                "arythmies). Prudence en ischémie critique non revascularisable"
            )),
            FicheRow(concept="◆ Traitement à visée locale - Arrêt tabac et marche", detail_md=(
                "- **Marche régulière** favorise :\n"
                "  - Développement de la circulation collatérale\n"
                "  - Amélioration de l'état métabolique musculaire (augmentation pool mitochondrial)\n"
                "  - Allongement de la distance de marche, voire disparition de la claudication\n"
                "- Marche supervisée > marche non supervisée (rééducation)\n"
                "- **Au minimum : 30-45 min, ≥ 3 fois/semaine**, ralentir/arrêter au seuil de la douleur\n"
                "- Réadaptation supervisée en milieu spécialisé complétée par "
                "**éducation thérapeutique du patient**"
            )),
            FicheRow(concept="Traitement médicamenteux symptomatique", detail_md=(
                "- **Statines** : augmentation possible du périmètre de marche\n"
                "- Vasoactifs (ex : pentoxifylline) : amélioration modeste, sans bénéfice pronostique "
                "(plusieurs retirés du marché pour futilité, d'autres déremboursés)\n"
                "- **Prostaglandines** : ischémie critique non revascularisable\n"
                "  - Perfusions quotidiennes plusieurs semaines en milieu spécialisé"
            )),
            FicheRow(concept="◆ Revascularisation - Indications", detail_md=(
                "- Autant que possible lors d'une **ischémie permanente**\n"
                "- **Claudication intermittente sévère** altérant la qualité de vie :\n"
                "  - Après échec de traitement médical bien conduit (incluant réadaptation)\n"
                "  - D'emblée si périmètre de marche **< 100 m** avec handicap fonctionnel (professionnel)\n"
                "  - D'emblée si atteintes aorto-iliaques sévères (collatéralité illusoire)"
            )),
            FicheRow(concept="◆ Revascularisation - Techniques", detail_md=(
                "- **Endovasculaire** :\n"
                "  - Angioplastie intraluminale par ballonnet ± stent\n"
                "  - Angioplastie sous-adventicielle possible (occlusions longues)\n"
                "  - Résultats meilleurs si lésions courtes et proximales\n"
                "  - Angioplastie distale (pied) en développement\n"
                "  - **Bithérapie antiplaquettaire 1 à 6 mois** post-angioplastie\n"
                "- **Chirurgie** :\n"
                "  - Pontage : veineux de préférence, sinon prothèse vasculaire\n"
                "  - Types : aorto-bi-iliaque (ou bifémoral), fémoropoplité, fémorojambier\n"
                "  - Pontages extra-anatomiques : fémorofémoral croisé, axillofémoral\n"
                "  - **Endartériectomie** (souvent associée au pontage), notamment bifurcation fémorale\n"
                "- **Techniques hybrides** : chirurgie + endovasculaire (ex : pontage aortobifémoral + "
                "angioplastie poplitée)\n"
                "- Surveillance (clinique + échodoppler) systématique : risque de thrombose, "
                "dégradation des pontages et anastomoses"
            )),
            FicheRow(concept="Soins de plaies", detail_md=(
                "- Sous supervision d'une équipe multidisciplinaire spécialisée en plaies et cicatrisation"
            )),
            FicheRow(concept="Amputation", detail_md=(
                "- **Geste ultime**, à défaut de toute revascularisation possible\n"
                "- Buts :\n"
                "  - Traiter la douleur\n"
                "  - Éviter/limiter les complications infectieuses\n"
                "- En zone saine et bien oxygénée (intérêt **TcPO₂**)\n"
                "- Sauvegarder l'appui (amputation d'orteil, transmétatarsienne)\n"
                "- Sauvegarder l'articulation du genou pour appareillage prothétique"
            )),
            FicheRow(concept="Stratégies de prise en charge", detail_md=(
                "- Toujours : contrôle des FDR + antiplaquettaire (si symptomatique)\n"
                "- Recherche systématique d'autres atteintes (coronarienne, cérébrovasculaire) orientée "
                "par la clinique\n"
                "- **Claudication intermittente** : algorithme dédié (fig. 7.6)\n"
                "- **Ischémie critique** : revascularisation maximale, amputation en dernier recours"
            )),
            FicheRow(concept="◆ Pronostic", detail_md=(
                "- Pronostic grave de l'AOMI\n"
                "- Espérance de vie en ischémie permanente = équivalente à certains cancers\n"
                "- Claudication intermittente : espérance de vie réduite de **10 ans en moyenne**\n"
                "- À 5 ans chez le claudicant :\n"
                "  - **20 %** ont des complications CV\n"
                "  - **20 %** décèdent (moitié de causes CV)\n"
                "  - **25 %** voient leur AOMI s'aggraver, dont 1/5 amputation majeure\n"
                "  - Risque d'amputation à 5 ans : ~5 %\n"
                "- **Ischémie critique** : mortalité à 5 ans **~ 70 %**\n"
                "- → Importance des mesures préventives même après revascularisation"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ **Médiacalcose** (IPS > 1,40) chez diabétique âgé ou dialysé : "
                "IPS ininterprétable, recourir à la **pression d'orteil**.\n"
                "- ⚠ Une **AOMI peut être masquée** par neuropathie ou comorbidités empêchant la marche : "
                "le patient peut se révéler d'emblée par une ischémie permanente."
            ), kind="piege"),
        ]),
    ])

    # ── PARTIE III : ISCHÉMIE AIGUË DES MEMBRES INFÉRIEURS ──
    partie_iii = Partie(numero="III", titre="Ischémie aiguë des membres inférieurs", sous_parties=[
        SousPartie(lettre="A", titre="Physiopathologie", rows=[
            FicheRow(concept="⚠ Définition - Urgence vasculaire", detail_md=(
                "- Interruption brutale du flux artériel d'un membre\n"
                "- Responsable d'une hypoxie tissulaire abrupte pouvant aboutir à la nécrose tissulaire\n"
                "- **Urgence vasculaire** : pronostic vital du membre (voire du patient) engagé"
            )),
            FicheRow(concept="◆ Baisse du débit artériel - Facteurs de gravité", detail_md=(
                "- Pression artérielle systémique (à maintenir à niveau correct)\n"
                "- Abondance de la circulation collatérale\n"
                "- Qualité du réseau artériel d'aval"
            )),
            FicheRow(concept="◆ Délais de souffrance tissulaire", detail_md=(
                "- **Cellules nerveuses** : souffrent en premier (**dans les 2 heures**)\n"
                "- **Cellules musculaires** : nécrose en **6-8 heures** (rhabdomyolyse)\n"
                "- **Nécrose cutanée** : à partir de la **24e heure**"
            )),
            FicheRow(concept="◆ Syndrome des loges", detail_md=(
                "- Anoxie musculaire → vasodilatation capillaire → œdème → augmentation pression "
                "interstitielle\n"
                "- → stase veineuse et lymphatique → autoaggravation œdème et hypoxie\n"
                "- Muscles dans loges aponévrotiques inextensibles → compression tissulaire\n"
                "- → arrêt total de la circulation = **syndrome des loges**\n"
                "- Hypoxie → anaérobiose → libération de métabolites acides → vasodilatation capillaire\n"
                "- **Seule l'aponévrotomie de décharge** libère le tissu musculaire et restaure la circulation capillaire"
            )),
            FicheRow(concept="◆ Syndrome de revascularisation", detail_md=(
                "- Atteinte cellulaire aggravée à la remise en circulation : relargage acides et radicaux libres\n"
                "- **Troubles métaboliques** : hyperkaliémie, acidose métabolique, hyperuricémie, "
                "myoglobinémie, myoglobinurie, augmentation créatinémie, hypocalcémie, hyperphosphorémie\n"
                "- **CIVD** possible\n"
                "- **Insuffisance rénale aiguë** :\n"
                "  - Nécrose tubulaire aiguë (choc, instabilité hémodynamique)\n"
                "  - Précipitation intratubulaire de myoglobine\n"
                "  - Toxicité directe (myoglobine en milieu acide, produits de contraste)\n"
                "- Plus rarement : choc hypovolémique (exsudation) ou infectieux (colonisation musculaire)"
            )),
        ]),
        SousPartie(lettre="B", titre="Diagnostic positif et étiologique", rows=[
            FicheRow(concept="◆ Diagnostic clinique - Signes fonctionnels", detail_md=(
                "- **Douleur d'apparition brutale** (parfois quelques heures dans la forme subaiguë)\n"
                "- Intense, à type de broiement\n"
                "- Impotence fonctionnelle du membre"
            )),
            FicheRow(concept="◆ Diagnostic clinique - Signes physiques", detail_md=(
                "- Examen comparatif avec membre controlatéral\n"
                "- Membre froid, livide\n"
                "- Douleurs à la palpation des masses musculaires\n"
                "- **Abolition des pouls** en aval de l'occlusion\n"
                "- **Examen neurologique** :\n"
                "  - Anesthésie et paralysie\n"
                "  - Notamment **nerf fibulaire commun** (impossibilité de relever le pied)\n"
                "- Sévérité graduée selon Rutherford (cf. tableau 7.2)"
            )),
            FicheRow(concept="Topographie et formes sévères", detail_md=(
                "- Localisation de la froideur + abolition des pouls = topographie de l'occlusion\n"
                "- **Cas le plus grave** : occlusion de la bifurcation aortique → "
                "ischémie bilatérale sévère + paralysie sensitivomotrice\n"
                "- Signes généraux au premier plan : **collapsus cardiovasculaire**"
            )),
            FicheRow(concept="⚠ Diagnostic paraclinique - Pas d'examen retardant !", detail_md=(
                "- Diagnostic d'ischémie aiguë **reste clinique**\n"
                "- Équipe chirurgicale alertée au plus tôt\n"
                "- **Aucune exploration ne doit retarder l'intervention** (surtout grade II avec atteinte neuro)\n"
                "- Échodoppler possible sans perte de temps si conditions locales et tableau le permettent "
                "(grade I, sans atteinte neuro)\n"
                "- **Artériographie** : le plus souvent réalisée au bloc opératoire pour orienter le geste\n"
                "  - Localise l'oblitération\n"
                "  - Caractérise l'aspect (athérome, anévrisme, dissection)\n"
                "  - Apprécie le réseau artériel d'aval (essentiel pour pontage)\n"
                "  - Embolie : révèle d'autres emboles homo/controlatéraux asymptomatiques"
            )),
            FicheRow(concept="◆ Diagnostic étiologique - Thrombose in situ", detail_md=(
                "- **Sujet âgé** avec FDR CV voire AOMI préexistante (à rechercher controlatéral)\n"
                "- Douleur d'intensité moyenne, survenue progressive ou rapide "
                "(collatéralité préalable)\n"
                "- Étiologies :\n"
                "  - AOMI\n"
                "  - Artériopathies non athéromateuses (inflammatoires, radiques)\n"
                "  - Anévrisme poplité thrombosé\n"
                "  - Déshydratation / hémoconcentration chez sujet âgé\n"
                "  - Causes sur artères saines : kyste adventiciel, dissection aorto-iliaque, "
                "thrombophlébite ischémique, coagulopathies\n"
                "  - **Iatrogéniques** : cathétérisme, **thrombopénie à l'héparine**, ergotisme"
            )),
            FicheRow(concept="◆ Diagnostic étiologique - Embolie sur artères saines", detail_md=(
                "- **Sujet jeune** sans antécédent vasculaire connu (mais cardiopathie possible)\n"
                "- Douleur brutale, aiguë et sévère (absence de collatérales)\n"
                "- Souvent précédée de palpitations (arythmie)\n"
                "- Causes :\n"
                "  - **Cardiaques** :\n"
                "    - **Fibrillation atriale**\n"
                "    - Foramen ovale perméable et anévrisme du septum interatrial\n"
                "    - IDM avec faux anévrisme de paroi\n"
                "    - Endocardite infectieuse\n"
                "    - Valvulopathies et prothèses valvulaires\n"
                "    - Tumeurs cardiaques (myxome de l'atrium)\n"
                "    - Dyskinésie / anévrisme ventriculaire gauche\n"
                "  - **Atteintes aortiques** : athérome aortique, anévrisme, aortites, tumeurs aortiques\n"
                "  - Pièges vasculaires"
            )),
            FicheRow(concept="", detail_md=(
                "- Les **deux tableaux ne sont pas toujours distincts** :\n"
                "- Une embolie peut survenir sur AOMI préexistante.\n"
                "- Une thrombose in situ peut survenir sur rupture de plaque non occlusive "
                "chez un sujet sans signe préalable d'AOMI."
            ), kind="piege"),
            FicheRow(concept="Examens complémentaires (après revascularisation)", detail_md=(
                "- Examen clinique = auscultation cardiaque + ECG + palpation abdominale "
                "(recherche anévrisme aortique)\n"
                "- **Bilan de coagulation** d'emblée\n"
                "- Après revascularisation :\n"
                "  - **Bilan cardiaque** : Holter ECG, ETT, voire ETO ou IRM\n"
                "  - **Bilan artériel** : échodoppler aorte + MI, voire angioscanner ou artériographie"
            )),
        ]),
        SousPartie(lettre="C", titre="Évaluation du terrain", rows=[
            FicheRow(concept="Recherche d'autres localisations", detail_md=(
                "- Recherche d'autres localisations ischémiques (embolies multiples)\n"
                "- État général du patient (pathologie incurable, handicap)\n"
                "- Évaluation rapide :\n"
                "  - Fonction cardiaque\n"
                "  - Comorbidités\n"
                "- Prise en charge palliative parfois seule solution chez malade très âgé/moribond"
            )),
        ]),
        SousPartie(lettre="D", titre="Traitement", rows=[
            FicheRow(concept="◆ Traitement médical", detail_md=(
                "- **Anticoagulation par HNF (héparine non fractionnée)** dès le diagnostic, après bilan coagulation :\n"
                "  - **Bolus 5 000 UI**\n"
                "  - Puis **perfusion continue 500 UI/kg/j**\n"
                "  - **TCA cible : 2-3**\n"
                "- **Antalgiques niveau 3** souvent nécessaires d'emblée\n"
                "- Oxygénothérapie nasale\n"
                "- Équilibration hémodynamique si nécessaire (remplissage macromoléculaire)\n"
                "- **Soins locaux immédiats** :\n"
                "  - Protection (mousse ou coton)\n"
                "  - Position légèrement déclive\n"
                "  - Éviction de tout frottement ou traumatisme cutané"
            )),
            FicheRow(concept="◆ Revascularisation", detail_md=(
                "- **Embolectomie par sonde de Fogarty** sous contrôle angiographique :\n"
                "  - Méthode de référence pour embolies sur artère saine\n"
                "  - Parfois utilisée sur artères athéromateuses\n"
                "- **Thrombolyse in situ intra-artérielle ± thromboaspiration** :\n"
                "  - Indiqué si lit d'aval jambier de mauvaise qualité et ischémie peu sévère\n"
                "  - Injection de fibrinolytique directement dans le thrombus\n"
                "  - Cathéter laissé en place plusieurs heures, surveillance et contrôles angiographiques répétés\n"
                "- En cas de sténose résiduelle : angioplastie complémentaire\n"
                "- Pontage (souvent distal) : en dernier ressort\n"
                "- **Aponévrotomie de décompression** :\n"
                "  - Systématique en cas de revascularisation tardive\n"
                "  - Le plus souvent loge antéro-externe de jambe (autres régions possibles, y compris pied)\n"
                "  - Évite le **syndrome des loges**\n"
                "- **Amputation** :\n"
                "  - D'emblée si ischémie dépassée\n"
                "  - Pour limiter les désordres métaboliques du syndrome de revascularisation\n"
                "  - Après échec de revascularisation, sur terrain débilité"
            )),
            FicheRow(concept="◆ Traitement des conséquences métaboliques de la revascularisation", detail_md=(
                "- Surveillance :\n"
                "  - Diurèse (sonde urinaire, diurèse horaire)\n"
                "  - Ionogramme sanguin, urée, créatininémie, CPK\n"
                "- Recherche **acidose métabolique hyperkaliémique** et **IRA**\n"
                "- Compensation progressive de l'acidose : bicarbonates IV (alcalinisation)\n"
                "- Kaliémie :\n"
                "  - Chélateur de potassium : polystyrène sulfonate de sodium (**Kayexalate®**)\n"
                "  - Voire dialyse rénale\n"
                "  - Lavage de membre au sérum physiologique\n"
                "- À long terme :\n"
                "  - **Embolie** : traitement étiologique (ex : anticoagulation au long cours si FA)\n"
                "  - **Thrombose** : antiplaquettaire + contrôle FDR CV"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ **Ischémie aiguë de membre = urgence absolue**.\n"
                "- Diagnostic essentiellement **clinique** : douleur brutale + froideur + pâleur + "
                "abolition pouls + signes neuro.\n"
                "- **Aucun examen ne doit retarder la revascularisation**."
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE IV : ANÉVRISMES ──
    partie_iv = Partie(numero="IV", titre="Anévrismes", sous_parties=[
        SousPartie(lettre="A", titre="Anévrisme de l'aorte abdominale (AAA)", rows=[
            FicheRow(concept="★ ◆ Définition", detail_md=(
                "- **Anévrisme** = dilatation focale et permanente de l'artère avec perte de parallélisme "
                "des parois et **augmentation de diamètre > 50 %** par rapport au diamètre d'amont\n"
                "- En dehors des artères cérébrales, localisations préférentielles : aorte (sous-rénale ++, "
                "ascendante), artères poplitées, iliaques"
            )),
            FicheRow(concept="◆ Physiopathologie", detail_md=(
                "- Altération de la **média aortique** :\n"
                "  - Destruction des fibres élastiques\n"
                "  - Fragmentation des fibres de collagène\n"
                "  - Perte progressive de la capacité à lutter contre la distension\n"
                "- Favorisée par suractivité d'enzymes détruisant la matrice collagénique (métalloprotéases)\n"
                "- AAA localisé sous les artères rénales dans la grande majorité des cas"
            )),
            FicheRow(concept="◆ Épidémiologie", detail_md=(
                "- Prévalence en baisse dans les populations occidentales\n"
                "- **2 à 5 %** des hommes > 65 ans\n"
                "- 75-84 ans : **5 % chez l'homme**, **3 % chez la femme**\n"
                "- FDR principaux (hors âge) :\n"
                "  - **Tabagisme**\n"
                "  - **Antécédents familiaux d'anévrisme**\n"
                "- Risque accru : autres localisations aortiques (thoracique) ou artérielle périphérique\n"
                "- Diabétiques : moins souvent atteints\n"
                "- **12 000 décès/an en Europe** par rupture (12e cause de décès)\n"
                "- ⚠ Sujet AAA = **haut risque CV** : 10 fois plus de risque de décéder "
                "d'une autre atteinte CV (coronaire, AVC) que de rupture d'AAA"
            )),
            FicheRow(concept="◆ Risque de rupture selon le diamètre", detail_md=(
                "- Risque **exponentiel** :\n"
                "  - **< 40 mm** : **0,4 %/an**\n"
                "  - **50-59 mm** : **3 %/an**\n"
                "  - **> 60 mm** : **15 %/an**\n"
                "- À diamètre égal : risque **~ 4 fois plus important chez la femme**"
            )),
            FicheRow(concept="◆ Étiologie", detail_md=(
                "- **80-90 %** : maladie athéromateuse (notamment AOMI, coronarienne, carotidienne)\n"
                "- **Formes familiales** :\n"
                "  - Entités génétiques identifiées (maladies des tissus élastiques) :\n"
                "    - Maladie de Marfan\n"
                "    - Maladie d'Ehlers-Danlos\n"
                "    - Syndrome de Loeys-Dietz\n"
                "- **Aortites** : maladies de Takayasu, Behçet, Horton\n"
                "- Historiquement : aortites infectieuses (syphilis)"
            )),
            FicheRow(concept="★ ◆ Forme asymptomatique - Diagnostic clinique", detail_md=(
                "- Le plus souvent découverte fortuite :\n"
                "  - **Palpation abdominale** : masse battante et expansive paraombilicale ± souffle\n"
                "  - Imagerie abdominale (échographie, scanner, IRM)\n"
                "- **Dépistage** par échographie chez les patients à risque :\n"
                "  - **Hommes > 65 ans**\n"
                "  - Plus jeunes avec FDR : tabagisme, maladie athéromateuse, ATCD familiaux d'anévrismes"
            )),
            FicheRow(concept="⚠ Anévrisme symptomatique - Rupture / fissuration", detail_md=(
                "- Découverte au stade de complication :\n"
                "  - Douleur abdominale ou lombaire\n"
                "  - ± Tableau de **choc hémorragique**\n"
                "- **Urgence vitale**\n"
                "- **Anévrisme douloureux = rupture imminente** → centre de chirurgie vasculaire urgent → "
                "scanner abdominal confirme et précise la localisation\n"
                "- Rupture intrapéritonéale : tableau cataclysmique souvent sans temps d'intervenir\n"
                "- Plus rarement, fissuration dans un organe adjacent :\n"
                "  - Fistule aortocave → insuffisance cardiaque à débit élevé\n"
                "  - Fistule aortodigestive → hémorragie digestive"
            )),
            FicheRow(concept="Autres manifestations", detail_md=(
                "- Embolie à partir du thrombus intra-anévrismal\n"
                "- **Compression des tissus/organes adjacents** :\n"
                "  - Érosion vertébrale\n"
                "  - Compression cave\n"
                "  - Compression urétérale\n"
                "- Syndrome inflammatoire clinico-biologique : fièvre, AEG, augmentation VS et CRP"
            )),
            FicheRow(concept="★ ◆ Diagnostic paraclinique", detail_md=(
                "- **Échographie abdominale** :\n"
                "  - Dépistage, mesure du diamètre maximal, suivi\n"
                "  - Dépiste autres localisations (poplitées, iliaques)\n"
                "- **Scanner abdominopelvien avec PCI** :\n"
                "  - Demandé si intervention envisagée\n"
                "  - Précise diamètre et anatomie\n"
                "  - **Examen préthérapeutique de référence**\n"
                "- IRM abdominale : alternative au scanner si CI\n"
                "- Artériographie : non utile (révèle seulement la lumière, pas de mesure fiable à cause "
                "du thrombus mural intra-anévrismal)"
            )),
            FicheRow(concept="★ ◆ Prise en charge - Forme asymptomatique", detail_md=(
                "- **Diamètre = principal facteur prédictif** du risque de rupture\n"
                "- **Vitesse de croissance moyenne : 2-4 mm/an** (non linéaire, variations individuelles)\n"
                "- Croissance plus rapide si :\n"
                "  - Homme\n"
                "  - Fumeur\n"
                "  - Diamètre anévrismal important\n"
                "- **Surveillance échographique** : plus rapprochée si calibre important\n"
                "  - **Tous les 6 mois** si diamètre **> 45 mm**\n"
                "- Pendant le suivi : contrôle des FDR indispensable\n"
                "- ⚠ Progression **3 fois plus rapide** si poursuite du tabagisme\n"
                "- **Seuil d'intervention : > 50-55 mm** → intervention « à froid » programmée"
            )),
            FicheRow(concept="★ ◆ Techniques d'intervention - AAA asymptomatique", detail_md=(
                "- **Chirurgie conventionnelle à ciel ouvert** = mise à plat-greffe :\n"
                "  - Exclusion de la zone anévrismale\n"
                "  - Interposition d'une prothèse vasculaire (pontage)\n"
                "- **Traitement endovasculaire** :\n"
                "  - Endoprothèse déployée dans l'anévrisme par voie fémorale\n"
                "  - Moins invasif : proposé aux sujets à haut risque chirurgical\n"
                "  - Nécessite des conditions anatomiques particulières\n"
                "  - Possible même chez patients à bas risque (anatomie favorable, information éclairée)\n"
                "  - Surveillance par imageries répétées (scanner, échographie de contraste) : "
                "évolution du sac et positionnement"
            )),
            FicheRow(concept="⚠ Forme symptomatique - Anévrisme rompu", detail_md=(
                "- **Urgence absolue**\n"
                "- Aucune imagerie autre que le scanner diagnostique ne doit retarder l'intervention\n"
                "- Survie d'autant plus grande que prise en charge rapide\n"
                "- **Traitement par endoprothèse** également proposé pour AAA rompu :\n"
                "  - Résultats satisfaisants dans équipes expérimentées\n"
                "  - D'autant plus proposé si haut risque périopératoire (comorbidités)\n"
                "- Ischémie aiguë par embolie depuis AAA : revascularisation du membre en urgence, "
                "secondairement cure de l'AAA"
            )),
            FicheRow(concept="Suivi à long terme", detail_md=(
                "- Patient reste à **haut risque CV** : surveillance, contrôle des FDR\n"
                "- **Prothèses chirurgicales** : surveillance échodoppler\n"
                "  - Risque de faux anévrismes anastomotiques\n"
                "  - Thrombose exceptionnelle\n"
                "- **Endoprothèses** : surveillance scanner ou échographie\n"
                "  - Détection des **endofuites** :\n"
                "    - Défaut de coaptation des extrémités avec la paroi aortique\n"
                "    - Défaut d'hermétisme entre 2 endoprothèses\n"
                "    - Porosité de l'endoprothèse\n"
                "    - Flux d'une branche artérielle connectée (ex : artères lombaires)\n"
                "  - Endofuites = poursuite d'évolutivité, risque de rupture\n"
                "- Prothèse artérielle : **antibioprophylaxie** lors d'actes thérapeutiques à risque bactérien"
            )),
        ]),
        SousPartie(lettre="B", titre="Anévrisme de l'artère poplitée (AP)", rows=[
            FicheRow(concept="◆ Associations et bilatéralité", detail_md=(
                "- Fréquemment associés aux **AAA (30 % des cas)**\n"
                "- **Bilatéraux dans près de 50 % des cas**"
            )),
            FicheRow(concept="Circonstances de découverte", detail_md=(
                "- **Période asymptomatique** :\n"
                "  - Palpation d'une masse battante (pouls trop bien perçu) au creux poplité\n"
                "  - Échodoppler notamment chez patients à risque (AAA ou AP controlatéral)\n"
                "- **Stade symptomatique** :\n"
                "  - Artériopathie progressive\n"
                "  - Ischémie aiguë"
            )),
            FicheRow(concept="◆ Indication chirurgicale", detail_md=(
                "- **AP > 20 mm** : opérés (exclusion de l'anévrisme + pontage)\n"
                "- D'autant plus que l'anévrisme est thrombosé\n"
                "- Sous réserve d'un bon réseau artériel sous-jacent permettant le pontage"
            )),
            FicheRow(concept="⚠ Complications - Embolie >> Rupture", detail_md=(
                "- **Complication la plus fréquente : embolie** (≠ AAA où c'est la rupture)\n"
                "- Embolies répétées à bas bruit → tableau ischémique\n"
                "- Pronostic sombre : occlusion de l'ensemble de l'arbre artériel distal, "
                "peu de possibilités de revascularisation\n"
                "- Ischémie aussi possible par thrombose de l'AP\n"
                "- Rarement : compression de tissus adjacents (nerfs, thrombose veineuse compressive)"
            )),
            FicheRow(concept="", detail_md=(
                "- AP : penser à rechercher un AAA associé (30 %).\n"
                "- AP : bilatéraux dans **50 %** des cas → toujours explorer l'autre côté.\n"
                "- AP : risque dominant = **embolie distale**, pas la rupture."
            ), kind="mnemo"),
        ]),
    ])

    tableaux = [
        TableauSynthese(titre="Synthèse - Classifications cliniques de l'AOMI", markdown=(
            "| Stade Leriche-Fontaine | Description | Équivalent Rutherford |\n"
            "|------------------------|-------------|----------------------|\n"
            "| I | Asymptomatique | Cat. 0 |\n"
            "| II | Claudication intermittente (a/b : > ou < 200 m) | Cat. 1-3 |\n"
            "| III | Douleur de décubitus | Cat. 4 |\n"
            "| IV | Troubles trophiques (ulcères, gangrène) | Cat. 5-6 |"
        )),
        TableauSynthese(titre="Synthèse - Interprétation de l'IPS", markdown=(
            "| IPS | Interprétation | Conduite |\n"
            "|-----|----------------|----------|\n"
            "| 1,00 - 1,40 | Normal | RAS |\n"
            "| < 0,90 | AOMI diagnostiquée | Bilan |\n"
            "| < 0,70 | AOMI sévère | PEC active |\n"
            "| > 1,40 | Médiacalcose (rigidité) | Recourir à l'index orteil |\n"
            "| Pression cheville < 50 mmHg | Ischémie critique | Urgence vasculaire |\n"
            "| Pression hallux < 30 mmHg | Ischémie critique | Urgence vasculaire |\n"
            "| Index orteil < 0,70 | AOMI (en cas de médiacalcose) | Bilan |"
        )),
        TableauSynthese(titre="Synthèse - TcPO₂ dans l'AOMI", markdown=(
            "| TcPO₂ dos du pied | Interprétation |\n"
            "|-------------------|----------------|\n"
            "| > 50 mmHg | Sujet sain |\n"
            "| > 35 mmHg | Bonne compensation métabolique |\n"
            "| 10 - 35 mmHg | Hypoxie continue |\n"
            "| < 10 mmHg | Hypoxie critique |"
        )),
        TableauSynthese(titre="Synthèse - Ischémie aiguë : thrombose in situ vs embolie", markdown=(
            "| Critère | Thrombose in situ | Embolie sur artère saine |\n"
            "|---------|-------------------|--------------------------|\n"
            "| Terrain | Sujet âgé, FDR CV, AOMI préexistante | Sujet jeune, sans ATCD vasculaire |\n"
            "| Douleur | Intensité moyenne, progressive | Brutale, aiguë, sévère |\n"
            "| Collatéralité | Préalable (atténue la sévérité) | Absente |\n"
            "| Cardiopathie | Parfois | Souvent (FA, IDM, valvulopathie) |\n"
            "| Autre membre | AOMI parfois | Normal en règle |\n"
            "| Causes principales | AOMI, artériopathies inflammatoires, déshydratation, iatrogénie | FA, FOP, IDM, endocardite, valves, tumeurs, athérome aortique, anévrisme |"
        )),
        TableauSynthese(titre="Synthèse - Classification de Rutherford de l'ischémie aiguë de membre", markdown=(
            "| Grade | Catégorie | Déficit sensitif | Déficit moteur | Pronostic |\n"
            "|-------|-----------|------------------|----------------|-----------|\n"
            "| I | Viable | Absent | Absent | Pas de menace immédiate, urgence relative |\n"
            "| IIa | Ischémie discrètement menaçante | Absent ou limité aux orteils | Absent | Récupérable si prise en charge |\n"
            "| IIb | Ischémie immédiatement menaçante | Présent au-delà des orteils | Modéré | Récupération possible si prise en charge immédiate |\n"
            "| III | Irréversible | Anesthésie importante | Important, paralysie | Perte de tissus et déficit séquellaire inévitables |"
        )),
        TableauSynthese(titre="Synthèse - Risque de rupture d'AAA selon le diamètre", markdown=(
            "| Diamètre AAA | Risque annuel de rupture |\n"
            "|--------------|--------------------------|\n"
            "| < 40 mm | 0,4 %/an |\n"
            "| 50-59 mm | 3 %/an |\n"
            "| > 60 mm | 15 %/an |\n"
            "| Femme à diamètre égal | Risque × 4 vs homme |\n"
            "| Croissance moyenne | 2-4 mm/an (×3 si poursuite tabac) |\n"
            "| Seuil d'intervention | > 50-55 mm (chirurgie ou endoprothèse) |"
        )),
        TableauSynthese(titre="Synthèse - AAA vs AP : comparatif", markdown=(
            "| Critère | AAA | AP |\n"
            "|---------|-----|----|\n"
            "| Localisation | Aorte sous-rénale ++ | Creux poplité |\n"
            "| Association AAA | - | 30 % des cas |\n"
            "| Bilatéralité | - | ~ 50 % |\n"
            "| Étiologie | Athérome (80-90 %) | Athérome |\n"
            "| Complication redoutée | Rupture | Embolie distale |\n"
            "| Seuil opératoire | > 50-55 mm | > 20 mm (ou si thrombosé) |\n"
            "| Technique | Mise à plat-greffe ou endoprothèse | Exclusion + pontage |"
        )),
    ]

    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Plaques aortiques 40-55 ans | 25 % H / 20 % F | Imagerie |\n"
        "| Prévalence AOMI > 60 ans | 1-5 % symptomatique / 10-15 % toutes formes | Atteinte |\n"
        "| Incidence AOMI | 2-5 % | Population |\n"
        "| Patients AOMI en France | > 1 million | Estimation |\n"
        "| Pic AOMI | H : 60-75 ans / F : 70-80 ans | Présentation |\n"
        "| Pouls pédieux congénitalement absent | 5 % population | Examen physique |\n"
        "| Temps de recoloration cutanée normal | < 3 sec | Examen |\n"
        "| Claudication sévère | < 100 m | Distance de marche |\n"
        "| Disparition douleur après arrêt | < 5 min | Claudication |\n"
        "| Ischémie critique | PAS cheville < 50 mmHg ou PAS hallux < 30 mmHg | Définition |\n"
        "| Durée ischémie critique | > 15 jours | Définition |\n"
        "| IPS sain | 1,00 - 1,40 | Diagnostic |\n"
        "| IPS AOMI | < 0,90 | Au moins 1 cheville |\n"
        "| IPS AOMI sévère | < 0,70 | Diagnostic |\n"
        "| IPS médiacalcose | > 1,40 | Diabétique, dialysé |\n"
        "| Index orteil AOMI | < 0,70 | Si médiacalcose |\n"
        "| Test marche - chute IPS | > 20 % | Diagnostic |\n"
        "| Test marche - chute PAS | > 30 mmHg | Diagnostic |\n"
        "| Strandness | 3,2 km/h, pente 10 % | Protocole tapis |\n"
        "| TcPO₂ saine | > 50 mmHg | Dos du pied |\n"
        "| TcPO₂ hypoxie critique | < 10 mmHg | Définition |\n"
        "| TcPO₂ 10-35 mmHg | Hypoxie continue | Interprétation |\n"
        "| Sensibilité angioscanner/ARM | ~ 95 % | vs artériographie |\n"
        "| Gadolinium ARM CI | Clairance < 30 mL/min/1,73 m² | IRS sévère |\n"
        "| Cible PAS AOMI | ≤ 120-129 mmHg | Traitement |\n"
        "| Cible PAD AOMI | ≤ 70-79 mmHg | Traitement |\n"
        "| Cible HbA1c | < 7 % | Diabète |\n"
        "| Cible LDL-C | < 0,55 g/L (< 1,4 mmol/L) avec réduction ≥ 50 % | Statines |\n"
        "| IMC cible | 20-25 kg/m² | Hygiène |\n"
        "| Réentraînement | 3×/semaine × 12 semaines | Cible |\n"
        "| Marche supervisée | 30-45 min, ≥ 3×/semaine | Pratique |\n"
        "| Aspirine + rivaroxaban | 75-100 mg/j + 2,5 mg × 2/j | Non remboursé France (sauf J+10 post-revasc.) |\n"
        "| Bithérapie antiplaquettaire post-angioplastie | 1-6 mois | Selon le geste |\n"
        "| Mortalité 5 ans - claudicants | 20 % | Pronostic |\n"
        "| Aggravation AOMI 5 ans | 25 % (1/5 amputation majeure) | Pronostic |\n"
        "| Risque amputation 5 ans | ~ 5 % | Pronostic |\n"
        "| Mortalité 5 ans - ischémie critique | ~ 70 % | Pronostic |\n"
        "| Souffrance neuro ischémie aiguë | < 2 h | Cellules nerveuses |\n"
        "| Rhabdomyolyse | 6-8 h | Cellules musculaires |\n"
        "| Nécrose cutanée | > 24 h | Délai |\n"
        "| Bolus HNF | 5 000 UI | Anticoagulation |\n"
        "| Perfusion HNF | 500 UI/kg/j | Anticoagulation |\n"
        "| TCA cible HNF | 2-3 | Surveillance |\n"
        "| Définition anévrisme | + 50 % du diamètre d'amont | Dilatation focale |\n"
        "| Prévalence AAA H > 65 ans | 2-5 % | Épidémiologie |\n"
        "| AAA 75-84 ans | 5 % H / 3 % F | Épidémiologie |\n"
        "| Rupture AAA < 40 mm | 0,4 %/an | Risque |\n"
        "| Rupture AAA 50-59 mm | 3 %/an | Risque |\n"
        "| Rupture AAA > 60 mm | 15 %/an | Risque |\n"
        "| Risque rupture femme | × 4 vs homme à diamètre égal | Pronostic |\n"
        "| Décès AAA en Europe | 12 000/an (12e rang) | Mortalité |\n"
        "| Mortalité CV vs rupture AAA | × 10 plus de décès CV | Polyathéromateux |\n"
        "| Vitesse croissance AAA | 2-4 mm/an (× 3 si tabac poursuivi) | Suivi |\n"
        "| Surveillance échographique AAA | 6 mois si > 45 mm | Suivi |\n"
        "| Seuil opératoire AAA | > 50-55 mm | Décision |\n"
        "| AAA athéromateux | 80-90 % | Étiologie |\n"
        "| AP associé à AAA | 30 % | Association |\n"
        "| AP bilatéraux | ~ 50 % | Bilatéralité |\n"
        "| Seuil opératoire AP | > 20 mm (ou thrombosé) | Décision |"
    ))

    points_cles = [
        "**AOMI** = athérome (> **95 %**) entre aorte et orteils ; FDR clés : **tabac** et **diabète**",
        "Claudication typique : crampe mollet, **< 5 min** au repos ; sévère si **< 100 m**",
        "**IPS** : sain **1,00-1,40** ; AOMI **< 0,90** ; sévère **< 0,70** ; médiacalcose **> 1,40** → index orteil",
        "**Ischémie critique** = douleurs > 15 j + PAS cheville **< 50 mmHg** ou hallux **< 30 mmHg**",
        "Bilan : **échodoppler** en 1re intention ; angioscanner/ARM si revascularisation envisagée",
        "Traitement AOMI : arrêt tabac, **marche supervisée**, antiplaquettaire, **statines** (LDL < 0,55 g/L), IEC",
        "**Ischémie aiguë MI** = urgence : clinique seule, **HNF 5 000 UI bolus** + 500 UI/kg/j (TCA 2-3)",
        "Étiologies aiguë : **thrombose in situ** (âgé, AOMI) vs **embolie** (jeune, **FA**, brutale)",
        "**AAA** = dilatation **> 50 %**, sous-rénale ; rupture exponentielle ; seuil opératoire **> 50-55 mm**",
        "**Anévrisme poplité** : 30 % associés à AAA, 50 % bilatéraux ; risque dominant = **embolie distale**",
    ]

    fiche_eclair_md = (
        "**Athérome aortique** : 25 % H, 20 % F (40-55 ans). Tabagisme++. Marqueur de risque CV. Sténoses rénales → HTA rénovasculaire ; digestives → ischémie mésentérique.\n\n"
        "**Ischémie mésentérique chronique** : angor digestif post-repas. Échodoppler/angioscanner. Revascularisation endovasculaire + antiplaquettaire.\n\n"
        "**Ischémie mésentérique aiguë** : urgence chirurgicale. Triade : douleur abdo + vidange + FA. Lactates tardifs. Angioscanner = référence. Résection + revascularisation.\n\n"
        "**AOMI** : 3e localisation athérome. > 95 % athéromateuse. FDR : tabac + diabète. Claudication intermittente = crampe mollet, distance stable, sévère si < 100 m. Stades Leriche-Fontaine I-IV ou Rutherford.\n\n"
        "**Ischémie critique** : douleurs décubitus > 15 j + PAS cheville < 50 mmHg ou hallux < 30 mmHg.\n\n"
        "**IPS** : sain 1,00-1,40 ; AOMI < 0,90 ; sévère < 0,70 ; médiacalcose > 1,40 → index orteil. TcPO₂ sain > 50, critique < 10 mmHg.\n\n"
        "**Bilan** : échodoppler en 1re intention. Angioscanner/ARM si revascularisation. Artériographie = procédure.\n\n"
        "**Traitement AOMI** : arrêt tabac, marche supervisée 30-45 min ≥ 3×/sem × 12 sem. Antiplaquettaire si symptomatique. Statines (LDL < 0,55 g/L). IEC. HbA1c < 7 %, PA ≤ 130/80. Revascularisation si ischémie permanente ou claudication sévère. Mortalité claudicant 20 %/5 ans ; ischémie critique 70 %.\n\n"
        "**Ischémie aiguë MI** : urgence vasculaire. Clinique (douleur brutale, froideur, pâleur, abolition pouls, atteinte neuro fibulaire). HNF bolus 5 000 UI + 500 UI/kg/j (TCA 2-3). Aucun examen ne retarde la revascularisation. 2 tableaux : thrombose in situ (âgé, AOMI) vs embolie (jeune, FA, brutale). Fogarty. Aponévrotomie si tardive (syndrome des loges).\n\n"
        "**Syndrome de revascularisation** : hyperkaliémie + acidose + IRA + CIVD. Bicarbonates, Kayexalate®, dialyse.\n\n"
        "**AAA** = dilatation > 50 %, sous-rénale++. Athérome 80-90 %. FDR : tabac + ATCD familiaux. Rupture exponentielle : 0,4 %/an < 40 mm, 3 %/an 50-59, 15 %/an > 60 mm. × 4 chez la femme. Dépistage écho H > 65 ans. Suivi écho 6 mois si > 45 mm. Seuil intervention > 50-55 mm. Rompu = urgence absolue (scanner seul).\n\n"
        "**Anévrisme poplité** : 30 % associés à AAA, 50 % bilatéraux. Complication = embolie distale (≠ AAA). Chirurgie si > 20 mm ou thrombosé."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 225 - Artériopathie de l'aorte, des artères viscérales et des membres inférieurs ; anévrismes",
        annee="2025-2026",
        item="Item 225",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv],
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 225",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-225_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

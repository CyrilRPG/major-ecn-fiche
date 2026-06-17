"""Génère la fiche exhaustive d'ORL à partir du PDF source."""

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
from major_ecn.docx_generator import render_docx


def build_fiche() -> FicheData:
    plan = [
        PlanPartie(numero="I", titre="Altération de la fonction auditive", sous_parties=[
            PlanSousPartie(lettre="A", titre="Anatomie, physiologie et interrogatoire"),
            PlanSousPartie(lettre="B", titre="Explorations de l'audition"),
            PlanSousPartie(lettre="C", titre="Surdité de transmission"),
            PlanSousPartie(lettre="D", titre="Surdités de perception"),
        ]),
        PlanPartie(numero="II", titre="Angines", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et tableau clinique"),
            PlanSousPartie(lettre="B", titre="Angine érythémato-pultacée et prise en charge"),
            PlanSousPartie(lettre="C", titre="Complications des angines à SBHA"),
            PlanSousPartie(lettre="D", titre="Angines pseudo-membraneuses, vésiculeuses et ulcéreuses"),
            PlanSousPartie(lettre="E", titre="Amygdalectomie"),
        ]),
        PlanPartie(numero="III", titre="Dysphonie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Tableau clinique et orientation étiologique"),
            PlanSousPartie(lettre="B", titre="Lésions laryngées"),
            PlanSousPartie(lettre="C", titre="Anomalies des mouvements des cordes vocales"),
        ]),
        PlanPartie(numero="IV", titre="Épistaxis", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et étiologies"),
            PlanSousPartie(lettre="B", titre="Conduite à tenir"),
        ]),
        PlanPartie(numero="V", titre="Infections naso-sinusiennes", sous_parties=[
            PlanSousPartie(lettre="A", titre="Rhinite aiguë et sinusite aiguë"),
            PlanSousPartie(lettre="B", titre="Rhinite chronique et sinusite chronique"),
            PlanSousPartie(lettre="C", titre="Ethmoïdite aiguë et rhinopharyngite"),
        ]),
        PlanPartie(numero="VI", titre="Otites", sous_parties=[
            PlanSousPartie(lettre="A", titre="Otite externe"),
            PlanSousPartie(lettre="B", titre="Otite moyenne aiguë"),
            PlanSousPartie(lettre="C", titre="Otite séro-muqueuse"),
            PlanSousPartie(lettre="D", titre="Otite cholestéatomateuse"),
        ]),
    ]

    # ── PARTIE I : ALTERATION DE LA FONCTION AUDITIVE ──
    partie_i = Partie(numero="I", titre="Altération de la fonction auditive", sous_parties=[
        SousPartie(lettre="A", titre="Anatomie, physiologie et interrogatoire", rows=[
            FicheRow(concept="Anatomie de l'oreille", detail_md=(
                "| Voie | Partie anatomique | Contenu |\n"
                "|------|-------------------|----------|\n"
                "| Aerienne | Oreille externe | Pavillon, conduit auditif externe |\n"
                "| Aerienne | Oreille moyenne | **Tympan**, chaine ossiculaire (malleus, incus, stapes) |\n"
                "| Aerienne | Oreille interne | **Cochlee** |\n"
                "| Aerienne | Centres nerveux | Nerfs auditifs, voie auditive centrale |\n"
                "| Osseuse | Os temporal | Cochlee, nerf auditif, voie auditive centrale |\n"
            )),
            FicheRow(concept="Interrogatoire", detail_md=(
                "- **ATCD** : traumatisme cranien, barotraumatisme, profession bruyante, "
                "FDR CV (HTA, hypercoagulabilite), medicaments **ototoxiques** (sels de platine, furosemide), "
                "ATCD familiaux de surdite\n"
                "- **Histoire maladie** : circonstances de survenue, type (uni/bilaterale, "
                "intensite, brusque ou progressive)\n"
                "- **Signes associes** : acouphenes, vertiges, sensation de plenitude, "
                "otorrhee, otalgie, paralysie faciale, cephalees, signes neurologiques"
            )),
            FicheRow(concept="Examen clinique", detail_md=(
                "- Examen ORL : **otoscopie bilaterale**, acoumétrie au diapason, examen vestibulaire\n"
                "- Examen neurologique : paires craniennes, syndrome cerebelleux, signes neurologiques focaux\n"
                "- Examen CV : recherche HTA, souffle vasculaire, FA\n"
                "- Examen ophtalmologique : acuite et oculomotricite"
            )),
            FicheRow(concept="", detail_md=(
                "- Deux types de surdite :\n"
                "  - **Surdite de transmission** : atteinte oreille externe/moyenne\n"
                "  - **Surdite de perception** : endo-cochleaire (oreille interne) ou retro-cochleaire (nerf/voies centrales)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Explorations de l'audition", rows=[
            FicheRow(concept="Triade acoumétrique", detail_md=(
                "- Diapasons calibres a differentes frequences\n"
                "- Etudie conduction aerienne (Ca) et osseuse (Co)\n"
                "- **Test de Weber** :\n"
                "  - Diapason au centre du front\n"
                "  - Sujet sain : vibrations au milieu du front (Weber indifferent)\n"
                "  - Surdite de perception : **lateralise cote sain**\n"
                "  - Surdite de transmission : **lateralise cote atteint**\n"
                "- **Test de Rinne** (Ca - Co) :\n"
                "  - Normal : Rinne positif (Ca > Co)\n"
                "  - Surdite de perception : Rinne **positif**\n"
                "  - Surdite de transmission : Rinne **negatif** (Ca < Co)"
            )),
            FicheRow(concept="", detail_md=(
                "- Weber lateralise cote sain = surdite de **perception**\n"
                "- Weber lateralise cote atteint = surdite de **transmission**\n"
                "- Rinne negatif = **transmission** ; Rinne positif = **perception** ou normal"
            ), kind="a_retenir"),
            FicheRow(concept="Explorations fonctionnelles", detail_md=(
                "| Type | Objectif | Critere |\n"
                "|------|----------|----------|\n"
                "| Subjectifs | Necessitent cooperation patient | Audiometrie tonale, audiometrie vocale |\n"
                "| Objectifs | Independants de la perception | PEA, OEA, tympanometrie, reflexes stapediens |\n"
            )),
            FicheRow(concept="Audiométrie tonale liminaire", detail_md=(
                "- Recherche seuils minimaux d'audition : ecouteurs (voie aerienne) et vibrations (voie osseuse)\n"
                "- Commence par meilleure oreille puis seconde\n"
                "- **Assourdissement** meilleure oreille si difference > **60 dB** "
                "(risque de sous-estimer surdite par transmission trans-cranienne)"
            )),
            FicheRow(concept="Audiométrie vocale", detail_md=(
                "- Recherche seuil d'intelligibilite de mots-test (retentissement reel)\n"
                "- **Seuil intelligibilite** : intensite a laquelle on entend 50% des mots\n"
                "- Normal : courbes en S italique entre 0-20 dB, seuil a 10 dB\n"
                "- Distorsions (courbe en cloche) = atteinte **endo-cochleaire** (appareillage peu efficace)"
            )),
            FicheRow(concept="Tympanométrie", detail_md=(
                "- Mesure compliance chaine tympano-ossiculaire\n"
                "- **CI si perforation tympanique**\n"
                "- Resultats :\n"
                "  - Normale : pic symetrique centre sur le zero pressionnel\n"
                "  - Cheminee (tour Eiffel) : rupture chaine / hyper-laxite\n"
                "  - Type C (non centree) : **dysfonction tubaire**\n"
                "  - Type B (plate) : **epanchement retro-tympanique**\n"
                "  - Aucune courbe : **perforation tympanique**\n"
                "  - Pic bifide : tympan cicatriciel non homogene"
            )),
            FicheRow(concept="Réflexe stapédien et PEA", detail_md=(
                "- **Reflexe stapedien** : se declenche vers 80-90 dB chez sujet normal\n"
                "  - Present bilateralement = elimine cophose\n"
                "  - Absent dans l'**otospongiose** (ankylose chaine)\n"
                "  - Aboli si PF en amont de sa 2e portion\n"
                "- **PEA** : exploration electrophysiologique des voies nerveuses\n"
                "  - Mesure objective du seuil auditif\n"
                "  - Localisation topographique : 5 pics (I=cochlee, II=nerf auditif, III-V=tronc cerebral)"
            )),
        ]),
        SousPartie(lettre="C", titre="Surdité de transmission", rows=[
            FicheRow(concept="Caractéristiques", detail_md=(
                "- Intensite legere/moyenne (**perte max 60 dB**)\n"
                "- Pas de modification qualitative de la voix\n"
                "- **Amelioree par le bruit** et au telephone (paracousie)\n"
                "- Patients n'elevent pas la voix ; autophonie\n"
                "- Weber lateralise cote sourd, Rinne negatif\n"
                "- Audiometrie : CO normale, CA abaissee, toujours **dissociation CA-CO**"
            )),
            FicheRow(concept="Otospongiose", detail_md=(
                "- **Osteodystrophie** du labyrinthe osseux par ankylose de la platine de l'etrier sur la fenetre ovale\n"
                "- Terrain : **femme jeune**, ATCD familiaux dans 50% des cas\n"
                "- Surdite bilaterale asymetrique, progressive, aggravee par episodes de vie genitale\n"
                "- Otoscopie : tympans **normaux**\n"
                "- Audiometrie : surdite de transmission puis mixte, **encoche de Carhart a 2000 Hz**\n"
                "- Reflexe stapedien **aboli**, tympanogramme normal\n"
                "- TDM rochers : hypodensites osseuses en avant de la fenetre ovale\n"
                "- Traitement : **stapedectomie/stapedotomie** ou prothese auditive si CI operatoire"
            )),
            FicheRow(concept="", detail_md=(
                "- L'otospongiose associe : femme jeune + surdite de transmission + tympans normaux + "
                "encoche de Carhart + reflexe stapedien aboli"
            ), kind="a_retenir"),
            FicheRow(concept="Autres causes", detail_md=(
                "- **Bouchon de cerumen** : surdite apres bain, extraction par lavage/aspiration\n"
                "- **Sequelles d'otites** : perforation tympanique, lyse ossiculaire, OSM ; "
                "traitement par tympanoplastie (50-70% rehabilitation)\n"
                "- **Aplasies d'oreille** : malformations congenitales, surdite fixee non evolutive ; "
                "chirurgie apres 7 ans\n"
                "- **Surdites traumatiques** : fracture rocher (hemotympan reversible, luxation ossiculaire permanente), "
                "barotraumatisme oreille moyenne\n"
                "- **Tumorales** (rares) : glomus tympano-jugulaire, carcinomes CAE"
            )),
        ]),
        SousPartie(lettre="D", titre="Surdités de perception", rows=[
            FicheRow(concept="Caractéristiques", detail_md=(
                "- Intensite variable (legere a **cophose**)\n"
                "- Si bilaterale : elevation de la voix\n"
                "- Intelligibilite **diminuee par le bruit** et au telephone (cocktail party)\n"
                "- Acouphenes aigus mal toleres, parfois vertiges\n"
                "- Weber lateralise cote le moins sourd, Rinne positif\n"
                "- Audiometrie : CO et CA abaissees, **non dissociees** ; alterations qualitatives "
                "(diplacousie, recrutement)"
            )),
            FicheRow(concept="Surdité unilatérale brusque (SUB)", detail_md=(
                "- **URGENCE** : survenue brutale en quelques secondes/minutes\n"
                "- Sifflements unilateraux +/- vertiges, examen ORL normal\n"
                "- Bilan etiologique souvent negatif (suspicion virale/vasculaire)\n"
                "- Pronostic pejoratif : **50-75% ne recuperent pas**\n"
                "- Traitement en urgence (effet nul apres **J10**) pendant 6-8 jours :\n"
                "  - Repos general et auditif\n"
                "  - **Corticotherapie** (1 mg/kg PO voire IV)\n"
                "  - Perfusions vasodilatateurs\n"
                "- **10% des SUB** = neurinome de l'acoustique : recherche systematique par PEA/IRM"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant toute surdite brusque :\n"
                "  - Eliminer **AVC** (signes neurologiques associes)\n"
                "  - Enfant : penser aux **oreillons**\n"
                "  - Bilaterale : penser MAI, ototoxicite\n"
                "  - Toujours rechercher un **neurinome** (10% des SUB)"
            ), kind="piege"),
            FicheRow(concept="Maladie de Ménière", detail_md=(
                "- Cause : **hydrops labyrinthique**\n"
                "- Terrain : jeune femme, stress\n"
                "- Clinique : vertiges intenses en heure, acouphenes graves et surdite\n"
                "- Diagnostic : eliminer autres causes (IRM)\n"
                "- Se bilateralise chez **10%** des sujets\n"
                "- Traitement : crise (**acetylleucine** et anxiolytique) ; fond (**betahistine**)"
            )),
            FicheRow(concept="Neurinome de l'acoustique", detail_md=(
                "- Tumeur benigne du **nerf VIII**\n"
                "- Risque : surdite unilaterale progressive et compression (PF)\n"
                "- Traitement chirurgical (neurochirurgie et ORL)"
            )),
            FicheRow(concept="Presbyacousie", detail_md=(
                "- Vieillissement normal des structures auditives neurosensorielles\n"
                "- Terrain : age > **60 ans** (precoce si facteurs genetiques, DT, toxiques)\n"
                "- Gene progressive de la communication, perte intelligibilite\n"
                "- Tympans normaux\n"
                "- Audiogramme : surdite de perception pure, bilaterale, symetrique en **pente douce** "
                "(frequences aigues puis conversationnelles)\n"
                "- Si asymetrique : rechercher **neurinome**\n"
                "- Traitement : prothese auditive bilaterale precoce des perte > **30 dB** sur 2000 Hz, "
                "reeducation orthophonique"
            )),
            FicheRow(concept="Traumatismes sonores", detail_md=(
                "- **Chronique professionnel** : zone alarme > **85 dB** pendant 8h/j\n"
                "  - Scotome auditif bilateral sur **4000 Hz**, extension vers frequences conversationnelles\n"
                "  - Arret d'evolution apres eviction ; pas de traitement mais **prevention++**\n"
                "- **Aigu accidentel** : surdite bilaterale a 4000 Hz, traitement identique SUB\n"
                "- **Barotraumatisme oreille interne** : surdite + vertiges rotatoires, "
                "traitement en urgence (corticotherapie + vasoconstricteurs nasaux)"
            )),
            FicheRow(concept="Surdités toxiques", detail_md=(
                "- Predomine sur frequences aigues, **irreversible et incurable**\n"
                "- **Aminosides+++** : ototoxiques sur cochlee et vestibule\n"
                "  - Terrain a risque : surdosage, insuffisants renaux, predisposition genetique\n"
                "  - Prevention : surveillance renale, adaptation doses, audiogramme systematique\n"
                "- Autres : furosemide, cisplatine, quinine, retinoides, CO/Hg/Pb"
            )),
        ]),
    ])

    # ── PARTIE II : ANGINES ──
    partie_ii = Partie(numero="II", titre="Angines", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et tableau clinique", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- **Amygdalites aigues** : inflammations aigues des amygdales palatines\n"
                "- Terrain : surtout enfant et adolescent (rares avant 18 mois)\n"
                "- Origine **virale dans 80%** (rhinovirus, coronavirus, EBV)\n"
                "- Origine **bacterienne dans 20%** (**SBHA** +++)"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Signes fonctionnels : douleurs pharyngees, fievre, asthenie, odynophagie, dysphagie, "
                "parfois otalgie et vomissements\n"
                "- Examen : hypertrophie amygdalienne, inflammation pharynx, aspect de l'angine\n"
                "- ADP cervicales douloureuses, otoscopie, rhinoscopie anterieure"
            )),
            FicheRow(concept="Angine SBHA vs virale", detail_md=(
                "| Critere | Angine SBHA | Angine virale |\n"
                "|---------|-------------|---------------|\n"
                "| Epidemio | Hiver/printemps, pic 5-15 ans | Toute saison |\n"
                "| Debut | **Brusque** | Progressif |\n"
                "| Odynophagie | Intense | Moderee/absente |\n"
                "| Toux | **Absente** | Presente, coryza, enrouement |\n"
                "| Fievre | **Elevee** | Variable |\n"
                "| Examen | Erytheme intense, purpura voile, exsudat | Vesicules, conjonctivite |\n"
                "| ADP | Satellites sensibles | Variables |\n"
                "| Eruption | Scarlatiniforme | Pied-main-bouche |\n"
            )),
        ]),
        SousPartie(lettre="B", titre="Angine érythémato-pultacée et prise en charge", rows=[
            FicheRow(concept="Angine érythémateuse", detail_md=(
                "- Amygdales et pharynx congestifs\n"
                "- Origine virale+++ : peut accompagner oreillons, grippe, rougeole, rubeole, VIH\n"
                "- Origine bacterienne dont **scarlatine** (SBHA)"
            )),
            FicheRow(concept="Angine érythémato-pultacée", detail_md=(
                "- Exsudat pultace gris jaunatre, punctiforme, mince et friable\n"
                "- Facilement dissocie, ne deborde pas la surface amygdalienne\n"
                "- Virale+++ (dont EBV) ou bacterienne (SBHA, staphylocoque, pneumocoque)"
            )),
            FicheRow(concept="Stratégie diagnostique", detail_md=(
                "- **Enfant < 3 ans** : traitement symptomatique seul (pas de TDR)\n"
                "- **Enfant > 3 ans** : **TDR systematique** (Sp > 95%, Se > 90%)\n"
                "- **Adulte** : score de **Mc Isaac** (Sp 90%, Se 80%) :\n"
                "  - Score < 2 : < 5% probabilite SBHA, pas de TDR ni ATB\n"
                "  - Score >= 2 : faire TDR"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Symptomatique (systematique)** : antipyretiques, antalgiques, "
                "alimentation fractionnee froide\n"
                "- **Pas d'AINS**++\n"
                "- **ATB** si TDR positif :\n"
                "  - 1ere intention : **amoxicilline** 2 g/j pendant **6 jours**\n"
                "  - Enfant : 50 mg/kg/j pendant 6 jours\n"
                "  - Allergie penicillines : cefpodoxime proxetil 200 mg/j 5 jours\n"
                "  - CI aux BL : azithromycine 500 mg/j sur 3 jours\n"
                "- Eviction collectivite obligatoire jusqu'a **48h d'ATB**\n"
                "- Surveillance : clinique et BU a **J15** si TDR positif"
            )),
            FicheRow(concept="", detail_md=(
                "- TDR positif = ATB par **amoxicilline** 6 jours\n"
                "- Jamais d'AINS dans les angines\n"
                "- But ATB : prevenir complications post-streptococciques (**RAA**) "
                "et suppuration locoregionale"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Complications des angines à SBHA", rows=[
            FicheRow(concept="Phlegmon péri-amygdalien", detail_md=(
                "- Cellulite suppuree entre capsule amygdalienne et paroi pharyngee\n"
                "- Clinique : T > 38 C, dysphagie accentuee et unilaterale, **trismus+++**, "
                "haleine fetide, voix sourde et nasonnee\n"
                "- Malade pale, tete inclinee du cote malade, laisse couler la salive\n"
                "- Examen : oedeme puis voussure unilaterale du pilier anterieur, "
                "amygdale refoulee, luette oedemateuse\n"
                "- Traitement :\n"
                "  - Presuppuratif : ATB (amoxicilline +/- ac. clavulanique)\n"
                "  - Collecte : **evacuation chirurgicale**"
            )),
            FicheRow(concept="Autres complications locales", detail_md=(
                "- **Abces retropharynge** : fievre, dysphagie douloureuse, dyspnee\n"
                "- **Adenophlegmon** : torticolis douloureux, empatement cervical, "
                "fievre ; traitement par drainage chirurgical\n"
                "- Cellulites cervicales (rares)"
            )),
            FicheRow(concept="RAA", detail_md=(
                "- Survient 15-20 jours apres infection amygdalienne (peut survenir malgre ATB)\n"
                "- FDR : ATCD personnel RAA, age **5-25 ans**, precarite, "
                "zone d'endemie, episodes multiples angines a SGA\n"
                "- Manifestations : AEG, fievre\n"
                "  - **Articulaires** : polyarthrite migratrice asymetrique des grosses articulations\n"
                "  - **Cardiaques** : endocardique (sequelles valvulaires), myocardique (IC), pericardique\n"
                "  - **Cutanees** : nodosites de Meynet, erytheme margine\n"
                "  - **Nerveuses** : choree de Sydenham"
            )),
            FicheRow(concept="Autres complications générales", detail_md=(
                "- **Erytheme noueux**\n"
                "- **Glomerulonephrite post-streptococcique** : 10-20 jours apres angine\n"
                "- Complications toxiniques : scarlatine, choc toxinique streptococcique"
            )),
            FicheRow(concept="", detail_md=(
                "- Le RAA touche le coeur, les articulations, la peau et le systeme nerveux\n"
                "- L'atteinte cardiaque (endocardite) peut laisser des **sequelles valvulaires definitives**"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Angines pseudo-membraneuses, vésiculeuses et ulcéreuses", rows=[
            FicheRow(concept="MNI (EBV)", detail_md=(
                "- Diagnostic par **MNI test** en premiere intention\n"
                "- Pas d'antibiotique (traitement symptomatique seul)\n"
                "- Risque de **rash cutane** si mis sous penicilline"
            )),
            FicheRow(concept="Diphtérie", detail_md=(
                "- Corynebacterium diphteriae (bacille de Loffler), incubation < 7 jours\n"
                "- Terrain : sujet **non vaccine**, zone d'endemie (Europe de l'Est)\n"
                "- Pseudo-membranes : grisatres, **adherentes**, extensives, "
                "saignant a la tentative de soulevement, debordant sur le voile\n"
                "- ADP sous-angulo-maxillaire, AEG, rhinorrhee muco-purulente\n"
                "- Traitement en urgence : hospitalisation en **isolement respiratoire**, "
                "serotherapie antitoxine, ATB (amoxicilline IV), **declaration obligatoire**\n"
                "- Prophylaxie sujets contacts, vaccination obligatoire\n"
                "- Complications : **croup** (extension), **myocardite** (ECG systematique), "
                "paralysie velo-palatine puis polyradiculonevrite"
            )),
            FicheRow(concept="Angine vésiculeuse", detail_md=(
                "- Toujours **virale** : enterovirus (coxsackie), HSV, VZV\n"
                "- **Herpangine** (coxsackie) : enfant 1-17 ans, ete, fievre 39-40 C, "
                "petites vesicules douloureuses a base inflammatoire, guerison spontanee 5-7 jours\n"
                "- Primo-infection herpetique : gingivo-stomatite herpetique"
            )),
            FicheRow(concept="Angine de Vincent", detail_md=(
                "- Germe : association **fuso-spirillaire**\n"
                "- Terrain : adulte jeune tabagique, mauvais etat bucco-dentaire, "
                "deficit immunitaire\n"
                "- Ulceration amygdalienne unilaterale profonde, enduit grisatre, "
                "bords irreguliers et sureleves, **souple au toucher** (non induree)\n"
                "- Dysphagie, haleine fetide, asthenie, fievre moderee\n"
                "- Complication principale : **syndrome de Lemierre** "
                "(thrombose jugulaire interne + embols pulmonaires)\n"
                "- Traitement : amoxicilline (metronidazole PO) 8 jours"
            )),
            FicheRow(concept="Autres angines ulcéreuses", detail_md=(
                "- Chancre syphilitique\n"
                "- Primo-infection VIH\n"
                "- Cancer amygdale\n"
                "- **Agranulocytose** / hemopathie (toujours faire NFS devant angine ulcereuse)"
            )),
            FicheRow(concept="", detail_md=(
                "- Angine pseudo-membraneuse : penser **MNI** (pas d'ATB, risque rash) "
                "et **diphterie** (urgence, DO)\n"
                "- Angine ulcereuse unilaterale : evoquer **cancer** et **hemopathie**"
            ), kind="piege"),
        ]),
        SousPartie(lettre="E", titre="Amygdalectomie", rows=[
            FicheRow(concept="Indications", detail_md=(
                "- Hypertrophie amygdalienne avec troubles respiratoires obstructifs (**SAOS**)\n"
                "- Hypertrophie sans trouble respiratoire : dysphagie, troubles phonation, "
                "troubles developpement oro-facial\n"
                "- Amygdalites aigues recidivantes : > **3 episodes/an pendant 3 ans** OU "
                "> **5 episodes/an pendant 2 ans**\n"
                "- Amygdalite chronique > 3 mois resistante au traitement medical\n"
                "- Syndromes post-streptococciques (sauf GNA)\n"
                "- ATCD phlegmon amygdalien apres 2 episodes\n"
                "- Tumefaction amygdalienne unilaterale suspecte de malignite"
            )),
            FicheRow(concept="CI et complications", detail_md=(
                "- CI relatives : troubles coagulation, enfant < 3 ans\n"
                "- Complications : **hemorragies immédiates et retardees**++, "
                "dysphagie douloureuse prolongee, persistance obstruction respiratoire"
            )),
        ]),
    ])

    # ── PARTIE III : DYSPHONIE ──
    partie_iii = Partie(numero="III", titre="Dysphonie", sous_parties=[
        SousPartie(lettre="A", titre="Tableau clinique et orientation étiologique", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Trouble de la voix parlee\n"
                "- **Aigu** (< 3 mois) / **chronique** (> 3 mois)\n"
                "- Diagnostics differentiels : hypophonie des insuffisances respiratoires, "
                "rhinolalie fermee/ouverte, dysarthrie (SLA++), aphasie"
            )),
            FicheRow(concept="Orientation étiologique", detail_md=(
                "- **Interrogatoire** : sexe, age, profession, intoxication OH-tabagique, "
                "ATCD traumatisme larynge/chirurgie cervico-thoracique, RGO\n"
                "- Modification voix : intensite, timbre, hauteur, voix bitonale/spastique\n"
                "- Signes associes : dysphagie, dyspnee, toux, **otalgie reflexe**, "
                "fausses routes, AEG\n"
                "- Examen : **laryngoscopie indirecte** / fibroscopie naso-laryngee, "
                "examen ORL complet (NC IX, X, XI, XII), palpation thyroide"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- Lesion suspecte : **laryngoscopie directe sous AG** pour biopsie-exerese "
                "(laryngoscopie en suspension)\n"
                "- Lesions benignes : stroboscopie, bilan phoniatrique\n"
                "- EMG cordes vocales si difficulte diagnostique (paralysie vs blocage mecanique)\n"
                "- Bilan lesionnel : IRM / TDM"
            )),
            FicheRow(concept="", detail_md=(
                "- Toute dysphonie > 3 semaines chez un sujet OH-tabagique = "
                "**laryngoscopie** pour eliminer un cancer"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Lésions laryngées", rows=[
            FicheRow(concept="Laryngite aiguë", detail_md=(
                "- Infection virale ou bacterienne\n"
                "- Dysphonie brutale type enrouement (voix rauque et voilee)\n"
                "- Cordes vocales rouges, oedematiees +/- secretions purulentes, febricule\n"
                "- Facteurs : periode hivernale, tabac, OH, malmenage vocal, infections ORL\n"
                "- Traitement : **repos vocal**, aérosols corticoides, ATB non systematiques ; "
                "evolution favorable en quelques jours"
            )),
            FicheRow(concept="Laryngite chronique", detail_md=(
                "- Installation progressive (voix rauque/grave), toux, hemmage\n"
                "- Causes : tabac, vapeurs toxiques, infections ORL repetees, RGO, surmenage vocal\n"
                "- Laryngite hypertrophique **rouge** (erythroplasie) ou **blanche** (leucoplasie)\n"
                "- **Lesions pre-cancereuses** : biopsie +/- exerese complete\n"
                "- Dysplasie legere/moderee : surveillance ; severe : ablation chirurgicale\n"
                "- Orthophonie : bilan et reeducation"
            )),
            FicheRow(concept="", detail_md=(
                "- Toute laryngite chronique est une **lesion pre-cancereuse** : "
                "biopsie systematique au moindre doute"
            ), kind="piege"),
            FicheRow(concept="Cancer du larynx", detail_md=(
                "- A suspecter si **homme d'age mur OH-tabagique**\n"
                "- Surtout tiers posterieur des CV\n"
                "- **Biopsies au moindre doute**"
            )),
            FicheRow(concept="Lésions bénignes", detail_md=(
                "| Lesion | Localisation | Terrain | Traitement |\n"
                "|--------|-------------|---------|------------|\n"
                "| Nodules CV | 1/3 anterieur, symetriques (kissing nodules) | Forcage vocal (professeur, chanteur) | Reeducation puis microchirurgie si echec |\n"
                "| Polypes / oedeme de Reinke | 2/3 anterieurs, uni/bilateraux | Tabac + forcage vocal | Laryngoscopie directe + microchirurgie |\n"
                "| Granulomes | 1/3 posterieur, pediculees | RGO, intubation prolongee | Traitement de la cause |\n"
                "| Papillomatose | CV et trachee, lesions muriformes | HPV | Exerese chirurgicale (risque degenerescence) |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Toute lesion meme d'allure benigne doit etre **biopsiee** "
                "si contexte a risque de cancer ORL"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Anomalies des mouvements des cordes vocales", rows=[
            FicheRow(concept="Paralysie laryngée unilatérale", detail_md=(
                "- Position ouverte : voix tres faible et soufflee/**bitonale**, "
                "fausses routes par inhalation\n"
                "- Position fermee : semiologie discrete, pas de gene respiratoire\n"
                "- **Causes nerveuses** : cancer (thyroidien, oesophagien, pulmonaire, mediastin), "
                "tumeur retro-stylienne, chirurgie du nerf vague (thyroidectomie), AVC du tronc, SEP, "
                "idiopathique (20%), causes cardiaques\n"
                "- **Causes mecaniques** : cancer larynge/sinus piriforme, "
                "post-intubation (ankylose crico-arytenoidienne), fibrose post-radique, PR"
            )),
            FicheRow(concept="Paralysie laryngée bilatérale", detail_md=(
                "- 2 CV immobiles en position **fermee** : **dyspnee** au 1er plan\n"
                "- 2 CV immobiles en position **ouverte** : dysphonie importante, "
                "voix quasi-inaudible, fausses routes\n"
                "- TDM injecte base crane au thorax systematique\n"
                "- Causes : thyroidectomie, cancer base crane/thyroidien/oesophagien, "
                "causes neurologiques, idiopathique"
            )),
            FicheRow(concept="", detail_md=(
                "- EMG laryngee pour differencier **paralysie** (atteinte nerf) "
                "de **blocage mecanique** (articulation crico-arytenoidienne)"
            ), kind="a_retenir"),
            FicheRow(concept="Dysphonies à CV normales", detail_md=(
                "- Troubles endocriniens : hypothyroidie, hyperandrogenisme\n"
                "- Surmenage vocal++\n"
                "- Dysphonie psychique\n"
                "- Dysphonie spasmodique : voix serree/etranglee, "
                "hyperactivite CV en phonation uniquement\n"
                "- Dysphonie myasthenique : s'aggrave au fil de la journee\n"
                "- Kystes intra-cordaux (stroboscopie seule les decele)"
            )),
        ]),
    ])

    # ── PARTIE IV : EPISTAXIS ──
    partie_iv = Partie(numero="IV", titre="Épistaxis", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et étiologies", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Hemorragie de sang rouge** provenant des fosses nasales\n"
                "- Deux systemes arteriels :\n"
                "  - Carotide interne : arteres ethmoidales anterieure et posterieure\n"
                "  - Carotide externe : artere spheno-palatine (branche maxillaire interne), "
                "artere de la sous-cloison (branche faciale)"
            )),
            FicheRow(concept="Examen clinique", detail_md=(
                "- Interrogatoire : age, ATCD (HTA, hemorragiques, CV), "
                "medicaments (**AAP/anticoagulants**), duree et abondance, ATCD epistaxis\n"
                "- Constantes : PA, FC, FR\n"
                "- Rhinoscopie et examen pharynge : abondance, jetage posterieur, "
                "origine localisee ou diffuse\n"
                "- DD : hemoptysie, hematemese, saignement base crane"
            )),
            FicheRow(concept="Causes générales", detail_md=(
                "- **Maladies hemorragiques** :\n"
                "  - Capillarites (purpura rhumatoide, infectieux)\n"
                "  - Thrombopenies/thrombopathies : Glanzmann, Willebrand, medicamenteuses (aspirine, AAP)\n"
                "  - Facteurs de coagulation : hemophilie, anticoagulants, insuffisance hepatique, CIVD\n"
                "- **Maladies vasculaires** :\n"
                "  - **Rendu-Osler** : angiomatose hemorragique familiale\n"
                "  - Rupture anevrisme carotidien intra-caverneux\n"
                "- **HTA** : a rechercher **systematiquement**\n"
                "- Epistaxis essentielle : grattage, exposition solaire, facteurs endocriniens"
            )),
            FicheRow(concept="Causes locorégionales", detail_md=(
                "- **Tumorales** :\n"
                "  - Fibrome naso-pharyngien : garcon 7-15 ans, obstruction nasale + epistaxis recidivant, "
                "**pas de biopsie++**, TDM/IRM, embolisation puis chirurgie\n"
                "  - Cancers rhino-sinusiens, cancers du cavum\n"
                "- **Traumatiques** : corps etranger, chirurgie, fracture nez/face, grattage tache vasculaire\n"
                "- **Infectieuses** : rhinopharyngite, sinusite\n"
                "- **Inflammatoire** : corticoides locaux"
            )),
            FicheRow(concept="", detail_md=(
                "- Fibrome naso-pharyngien : **jamais de biopsie** (tumeur hypervascularisee)\n"
                "- Toujours rechercher une **HTA** devant une epistaxis\n"
                "- Interdit d'emboliser les **ethmoidales** (risque de cecite)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Conduite à tenir", rows=[
            FicheRow(concept="Signes de gravité", detail_md=(
                "- Cliniques : tachycardie, hypotension, sueurs, paleur\n"
                "- Biologiques : taux Hb anormalement bas\n"
                "- Contexte : coronaropathie/stenose carotidienne associee, "
                "troubles de la coagulation\n"
                "- Examens si indication : NFS, plaquettes, Gr, Rh, RAI, TP, TCA"
            )),
            FicheRow(concept="Premiers gestes", detail_md=(
                "- Mouchage / nettoyage fosses nasales\n"
                "- Tete surelevee et penchee en **avant**\n"
                "- **Compression bi-digitale** (environ 10 minutes)\n"
                "- Sucer des glacons\n"
                "- Recherche tache vasculaire (anterieure) avec coton imbibe xylocaine naphazolinee\n"
                "- Si localisee et active (80% cas) : **cauterisation** "
                "(nitrate d'argent / bipolaire)"
            )),
            FicheRow(concept="Escalade thérapeutique", detail_md=(
                "| Etape | Technique | Modalites |\n"
                "|-------|-----------|----------|\n"
                "| 1 | **Tamponnement anterieur** | Resorbable (Surgicel) au mieux ; non resorbable (Merocel) 48-72h max ; Augmentin tant que meche + 5j apres |\n"
                "| 2 | **Tamponnement antero-posterieur** par ballonnet | En place 72h max, degonfler toutes les 6-8h |\n"
                "| 3 | **PEC interventionnelle** | Coagulation endonasale spheno-palatines / embolisation spheno-palatines / ligature ethmoidales voie externe |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Tamponnement non resorbable : **CI dans Rendu-Osler** (risque saignement au retrait)\n"
                "- **Interdit d'emboliser les ethmoidales** (risque cecite) : "
                "ligature par voie externe (canthus interne)\n"
                "- Seuils transfusion : < **7 g/dL** sans FDR, < **10 g/dL** si coronarien"
            ), kind="a_retenir"),
            FicheRow(concept="HTA et épistaxis", detail_md=(
                "- Repeter mesures apres avoir tari hemorragie et calme patient\n"
                "- Si persiste : regulation rapide de la TA necessaire\n"
                "- Angiomatose diffuse/coagulopathie : tampons **resorbables** (Surgicel)"
            )),
        ]),
    ])

    # ── PARTIE V : INFECTIONS NASO-SINUSIENNES ──
    partie_v = Partie(numero="V", titre="Infections naso-sinusiennes", sous_parties=[
        SousPartie(lettre="A", titre="Rhinite aiguë et sinusite aiguë", rows=[
            FicheRow(concept="Rhinite aiguë", detail_md=(
                "- Affection contagieuse surtout automne/hiver, liee a baisse transitoire immunite\n"
                "- Prodromes : lassitude, frissonnement, pesanteur tete\n"
                "- Obstruction nasale, rhinorrhee (sereuse puis purulente), "
                "cephalees frontales\n"
                "- Duree 8-20 jours\n"
                "- Traitement symptomatique : lavage fosses nasales serum physiologique, "
                "antalgiques, vasoconstricteurs nasaux si obstruction invalidante"
            )),
            FicheRow(concept="Sinusite aiguë - généralités", detail_md=(
                "- Germes : **H. influenzae**, pneumocoques, M. catarrhalis, S. aureus, anaerobies\n"
                "- Genese des cavites sinusiennes :\n"
                "  - Sinus ethmoidal : premiers mois de vie\n"
                "  - Sinus maxillaire : vers 3-4 ans (**pas de sinusite maxillaire < 3 ans**)\n"
                "  - Sinus frontal : vers 5-10 ans\n"
                "  - Sinus sphenoidal : 10-15 ans\n"
                "- Facteurs favorisants : infection VRS, polypose, deviation cloison, "
                "allergie, infection dentaire, immunodepression"
            )),
            FicheRow(concept="Sinusites de l'adulte", detail_md=(
                "| | Maxillaire++ | Frontale | Sphenoidale |\n"
                "|--|-------------|---------|-------------|\n"
                "| Douleur | Pulsatile, sous-orbitaire, augmentee flexion tete, cyclique vespérale | Violente, frontale en barre, irradiant tout crane | Retro-orbitaire, vertex, nuque, invalidante |\n"
                "| Pus | Meat moyen | Meat moyen | Ecoulement posterieur |\n"
                "| Complications | Sinusite bloquee, osteites, orbitaires, endocraniennes | Neuro-meningees++ (empyeme, abces, thrombophlebite) | Neuro-meningees++ (empyeme, abces, meningite) |\n"
                "| Examens | **Aucun++** | Scanner si besoin | **Scanner++** |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Sinusite maxillaire aigue non compliquee : **aucun examen** complementaire\n"
                "- Sinusite frontale et sphénoidale : complications neuro-meningees++"
            ), kind="a_retenir"),
            FicheRow(concept="Traitement sinusite", detail_md=(
                "- Symptomatique : antalgiques (pas d'AINS), antipyretiques\n"
                "- Mesures associees : arret tabac, lavages fosses nasales, "
                "vasoconstricteurs nasaux (max 5 jours), corticotherapie cure courte si hyperalgie\n"
                "- ATB probabiliste si indication : amoxicilline 1ere intention\n"
                "- Echec : FQ actives sur pneumocoque, ponction drainage"
            )),
        ]),
        SousPartie(lettre="B", titre="Rhinite chronique et sinusite chronique", rows=[
            FicheRow(concept="Rhinite chronique", detail_md=(
                "- **Allergique** : perannuelle ou saisonniere, rechercher terrain atopique et asthme\n"
                "- **Non allergique** : hypertrophique, crouteuse, NARES, "
                "medicamenteuse, vasomotrice, hormonale, atrophique\n"
                "- Obstruction nasale, rhinorrhee, eternuements\n"
                "- TDM normal ; bilan allergologique si allergique\n"
                "- Traitement : lavage fosses nasales, corticoides locaux (lors exacerbations), "
                "anti-H1 si allergique, desensibilisation possible"
            )),
            FicheRow(concept="Sinusite chronique unilatérale antérieure", detail_md=(
                "| Mecanisme | Dentaire+++ | Blocage ostio-meatal |\n"
                "|-----------|-----------|----------------------|\n"
                "| Étiologie | Foyer infectieux premolaires/molaires superieures, amalgame dentaire +/- greffe aspergillaire | Malformation meat moyen, deviation cloison, tumeur sinusienne |\n"
                "| Clinique | Signes classiques + **cacosmie**, odeur fetide | Signes classiques |\n"
                "| TDM | Kyste dentaire apical, pate dentaire, calcifications aspergillaires | Variable |\n"
                "| Traitement | ATB + eradication foyer dentaire + lavages ; si truffe aspergillaire : exerese chirurgicale | ATB + traitement chirurgical etiologique |\n"
            )),
            FicheRow(concept="Polypose naso-sinusienne", detail_md=(
                "- Pansinusite chronique avec polypes bilateraux\n"
                "- **Anosmie++**, douleurs/pesanteurs faciales, rhinorrhee chronique\n"
                "- Syndrome de **Widal** : asthme + intolerance aspirine + polypose\n"
                "- TDM : atteinte bilaterale, sinus combles isodenses\n"
                "- Toujours rechercher **asthme associe** et RGO\n"
                "- Traitement : lavage fosses nasales pluriquotidien, "
                "corticotherapie locale 3 mois, corticotherapie generale si poussee "
                "(1 mg/kg 7 jours, max 3x/an)\n"
                "- Si > 3 poussees/an : chirurgie (meatotomie, ethmoidectomie)"
            )),
        ]),
        SousPartie(lettre="C", titre="Ethmoïdite aiguë et rhinopharyngite", rows=[
            FicheRow(concept="Ethmoïdite aiguë", detail_md=(
                "- **Urgence diagnostique et therapeutique**\n"
                "- Enfants des 6 mois, surtout 2-5 ans, fait souvent suite a rhinopharyngite\n"
                "- AEG, fievre 39-40 C\n"
                "- **Oedeme douloureux comblant canthus interne** unilateral, suppuration nasale\n"
                "- Scanner sinus avec injection en **urgence** :\n"
                "  - Comblement sinus, recherche complications, DD (dacryocystite, cellulite dentaire)\n"
                "- Bilan : NFS, CRP, hemocultures, PL si signes meninges"
            )),
            FicheRow(concept="Complications ethmoïdite", detail_md=(
                "- **Orbitaires** : cellulite aigue orbitaire (exophtalmie, douleur), "
                "abces sous-perioste puis intra-orbitaire (immobilite globe, paralysie oculomotrice, **BAV**)\n"
                "- **Neurologiques** : meningites, encephalites, abces cerebraux, "
                "thrombophlebite sinus caverneux\n"
                "- **Generales** : septicemie, choc septique"
            )),
            FicheRow(concept="Traitement ethmoïdite", detail_md=(
                "- Hospitalisation en urgence\n"
                "- ATB probabiliste IV, au moins double, bactericide et synergique\n"
                "  - Type : **CG3 + clindamycine**\n"
                "  - Relai PO a J5 si evolution favorable (Augmentin/CG3)\n"
                "- Antipyretiques, antalgiques, soins locaux (desinfection rhinopharyngee, collyres)\n"
                "- Chirurgie si complications"
            )),
            FicheRow(concept="Rhinopharyngite", detail_md=(
                "- **Premiere pathologie infectieuse** et cause de consultation pediatrique\n"
                "- Exclusivement virale : rhinovirus, coronavirus, VRS, Influenzae\n"
                "- Contamination interhumaine voie aerienne\n"
                "- Rhinite + pharyngite, fievre < 38,5 C, ADP sous-angulo-maxillaires\n"
                "- Complications : **OMA purulente**, conjonctivite purulente, sinusite (rare)\n"
                "- Traitement ambulatoire : desobstruction rhinopharyngee au serum physiologique, "
                "traitement fievre si inconfort\n"
                "- ATB seulement si complication bacterienne\n"
                "- Evolution favorable en 7-10 jours"
            )),
            FicheRow(concept="", detail_md=(
                "- Ethmoidite aigue de l'enfant = **urgence** : scanner en urgence, ATB IV\n"
                "- Rhinopharyngite : exclusivement virale, **pas d'ATB** sauf complication bacterienne"
            ), kind="a_retenir"),
        ]),
    ])

    # ── PARTIE VI : OTITES ──
    partie_vi = Partie(numero="VI", titre="Otites", sous_parties=[
        SousPartie(lettre="A", titre="Otite externe", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Dermo-epidermite aigue du canal auditif externe\n"
                "- Germes : **S. aureus** et **P. aeruginosa**\n"
                "- Facteurs favorisants : maceration (prothese), lesion cutanee CAE (eczema, grattage)"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Otalgie intense et lancinante, otorrhee purulente parfois, hypoacousie moderee\n"
                "- **Apyrexie**\n"
                "- Douleur a la pression du **tragus** / traction du pavillon\n"
                "- CAE : erytheme +/- stenose\n"
                "- Otoscopie : tympan normal ou inflammatoire"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Local** : aspiration secretions, gouttes ATB (ofloxacine 3x/j 8 jours)\n"
                "- Si stenose CAE : mechage par Pop Ear a retirer a 48h\n"
                "- Antalgiques (eviter AINS)\n"
                "- Eviter facteurs favorisants"
            )),
            FicheRow(concept="Otite maligne externe", detail_md=(
                "- **Osteite aigue du rocher**\n"
                "- Terrain : **diabetique/immunodeprime**\n"
                "- Germe : **P. aeruginosa**\n"
                "- Otite externe avancee + otorrhee profuse + polype satellite CAE\n"
                "- Complications : PFP (testing systematique), paralysie NC, meningite\n"
                "- Scanner rocher avec injection : lyse osseuse\n"
                "- Traitement : ATB IV anti-pyocyanique (**Tazocilline + Ciprofloxacine**), "
                "duree plusieurs mois, equilibration diabete\n"
                "- Chirurgie (mastoidectomie) si echec"
            )),
            FicheRow(concept="", detail_md=(
                "- Otite externe + diabetique/immunodeprime = penser a l'**otite maligne externe** "
                "(P. aeruginosa, osteite du rocher)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Otite moyenne aiguë", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Inflammation aigue infectieuse de la muqueuse de l'oreille moyenne\n"
                "- Contamination par rhinopharynx via trompe d'Eustache\n"
                "- Surtout enfant **1-6 ans** (exceptionnelle avant 3 mois)\n"
                "- Germes bacteriens :\n"
                "  - **H. influenzae** (40%) dont 45% producteurs beta-lactamase\n"
                "  - **S. pneumoniae** (30%) dont 35% PSDP\n"
                "  - **M. catarrhalis** (10%) dont 90% producteurs beta-lactamase"
            )),
            FicheRow(concept="Stades otoscopiques", detail_md=(
                "| Stade | Symptomes | Otoscopie |\n"
                "|-------|-----------|-----------|\n"
                "| **Congestive** | Otalgies a repetition, pulsatiles | Tympan hypervascularise, respect triangle lumineux |\n"
                "| **Collectee** | Otalgies permanentes, fievre elevee | Tympan bombant **rouge cerise**, disparition relief ossiculaire |\n"
                "| **Perforee** | Otalgies et fievre diminuees, otorrhee | Perforation tympanique (postero-inferieure) |\n"
            )),
            FicheRow(concept="Orientation étiologique", detail_md=(
                "- Otite + **conjonctivite** = **H. influenzae** (AUGMENTIN)\n"
                "- Otalgie tres douloureuse + fievre > 38,5 C = **S. pneumoniae**"
            )),
            FicheRow(concept="", detail_md=(
                "- Otite + conjonctivite purulente = **H. influenzae** : amoxicilline-acide clavulanique\n"
                "- Sinusite maxillaire < **3 ans** = impossible (sinus non forme)"
            ), kind="a_retenir"),
            FicheRow(concept="Paracentèse", detail_md=(
                "- Incision quadrant postero-inferieur du tympan\n"
                "- A but antalgique, therapeutique et bacteriologique\n"
                "- Indications : otite compliquee, hyperalgique, enfant < **3 mois**, "
                "resistance malgre traitement bien conduit, immunodeprime"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- **Symptomatique systematique** : paracetamol (eviter AINS), "
                "DRP au serum physiologique 4-6x/j\n"
                "- Reconsulter si persistance fievre/otalgie a **72h**\n"
                "- Echec = aggravation > 48h apres debut ATB OU reapparition dans 4 jours apres fin ATB"
            )),
            FicheRow(concept="Complications OMA", detail_md=(
                "- **Mastoidite** (1/10 000) : pus au travers corticale os mastoidien, "
                "tumefaction inflammatoire retro-auriculaire, decollement pavillon ; "
                "TDM + tri-ATB IV (**Cefotaxime + Fosfomycine + Flagyl**)\n"
                "- **PF** (5/1 000) : tri-ATB IV + corticotherapie 1 mg/kg/j a J2, "
                "mastoidectomie si persistance\n"
                "- **Labyrinthite** : vertiges, syndrome vestibulaire peripherique, surdite brusque\n"
                "- Meningite, abces cerebral, thrombophlebite sinus lateral\n"
                "- OSM (10-20%)"
            )),
        ]),
        SousPartie(lettre="C", titre="Otite séro-muqueuse", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Otite chronique a tympan ferme : epanchement non infectieux retro-tympanique > **3 mois**\n"
                "- Touche **50% des enfants**, age moyen 5 ans, bilaterale dans 85%\n"
                "- FDR : division velaire, tumeur cavum (OSM souvent **unilaterale**), "
                "hypertrophie adenoidienne, OMA mal traitee, "
                "vie en collectivite, tabagisme passif, RGO"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- **Hypoacousie**, sensation de plenitude, otalgie type tension fugace\n"
                "- Otoscopie : tympan epaissi, depoli, **mat/ambre/jaunatre** ou bleu, "
                "retracte ou bombant, bulles seriques retro-tympaniques, "
                "immobile aux manoeuvres de Valsalva\n"
                "- Fibroscopie **systematique si OSM unilaterale** chez l'adulte (cancer cavum)"
            )),
            FicheRow(concept="", detail_md=(
                "- OSM unilaterale chez l'adulte = rechercher **cancer du cavum** "
                "(fibroscopie systematique)"
            ), kind="piege"),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- Tympanometrie : **courbe plate++**, abolition reflexe stapedien\n"
                "- Audiometrie tonale : surdite de **transmission**\n"
                "- +/- Bilan orthophonique"
            )),
            FicheRow(concept="Traitement", detail_md=(
                "- Corticoides PO (1 mg/kg 5 jours) +/- nasaux\n"
                "- Desobstruction rhinopharyngee, PEC facteurs favorisants\n"
                "- Pas d'ATB (sauf persistance > 3 mois + avis ORL)\n"
                "- Indications d'**ATT** (+/- adenoidectomie) :\n"
                "  - Surdite bilaterale transmission > **30 dB** avec retard langage\n"
                "  - OSM avec poche de retraction tympanique fixee\n"
                "  - Duree d'evolution prolongee previsible\n"
                "- Suivi otologique tous les **6 mois**"
            )),
            FicheRow(concept="Évolution et complications OSM", detail_md=(
                "- Le plus souvent favorable apres 3 mois\n"
                "- Surinfection (OMA)\n"
                "- **Tympanosclerose** : transformation hyaline muqueuse oreille moyenne\n"
                "- **Otite atelectasique** : poche de retraction tympanique "
                "(risque evolution en cholesteatome)\n"
                "- Otite fibro-adhesive : comblement caisse tympan par tissu fibreux"
            )),
        ]),
        SousPartie(lettre="D", titre="Otite cholestéatomateuse", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Proliferation epidermique benigne a **tendance destructrice** dans l'oreille moyenne\n"
                "- Formes acquises : perforation tympanique marginale, traumatisme, otite atelectasique\n"
                "- Forme congenitale\n"
                "- Frequente surinfection : **P. aeruginosa**"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Hypoacousie discrete progressivement installee\n"
                "- Otorrhee purulente, minime, **verdatre avec debris epidermiques**\n"
                "- Otoscopie : perforation/PR marginale atticale (postero-superieure), "
                "**debris blanchatres** (squames epidermiques), "
                "destruction paroi postero-superieure CAE\n"
                "- Recherche complications : signe de la fistule (vertige a la pression CAE), "
                "testing PF, examen neurologique, audiometrie"
            )),
            FicheRow(concept="Examens et traitement", detail_md=(
                "- Scanner des rochers (IRM si doute) : hyperdensité caisse, "
                "lyse parois/chaine ossiculaire, fistule CSC lateral\n"
                "- Bilan audiometrique medico-legal\n"
                "- Traitement **chirurgical** :\n"
                "  - Exerese complete + tympanoplastie +/- ossiculoplastie\n"
                "  - Souvent antro-mastoidectomie associee\n"
                "  - Controle a 1 an (IRM)\n"
                "- Surinfection : ATB IV anti-pyocyaniques + locaux\n"
                "- Surveillance clinique et paraclinique pendant au moins **10 ans**"
            )),
            FicheRow(concept="Complications cholestéatome", detail_md=(
                "- Recidive / cholesteatome residuel\n"
                "- **Mastoidite**\n"
                "- **Labyrinthite** : surdite de perception + vertiges\n"
                "- **PFP**\n"
                "- **Fistule labyrinthique**\n"
                "- Complications endocraniennes : meningite, abces cerebral, "
                "thrombophlebite sinus lateral, otorrhee cerebro-spinale"
            )),
            FicheRow(concept="", detail_md=(
                "- Le cholesteatome est une lesion **benigne mais destructrice** : "
                "traitement toujours chirurgical, surveillance au long cours (10 ans)"
            ), kind="a_retenir"),
        ]),
    ])

    # ── TABLEAUX DE SYNTHESE ──
    tableaux = [
        TableauSynthese(titre="Surdité de transmission vs surdité de perception", markdown=(
            "| Critere | Transmission | Perception |\n"
            "|---------|-------------|------------|\n"
            "| Atteinte | Oreille externe/moyenne | Oreille interne/nerf/voies centrales |\n"
            "| Perte max | 60 dB | Variable (jusqu'a cophose) |\n"
            "| Voix | Non modifiee | Elevee si bilaterale |\n"
            "| Bruit ambiant | Ameliore l'audition (paracousie) | Diminue l'intelligibilite (cocktail party) |\n"
            "| Weber | Lateralise cote atteint | Lateralise cote sain |\n"
            "| Rinne | Negatif (Ca < Co) | Positif |\n"
            "| Audiometrie | CO normale, CA abaissee (dissociation) | CO et CA abaissees (non dissociees) |\n"
        )),
        TableauSynthese(titre="Types d'angines et orientations diagnostiques", markdown=(
            "| Type | Aspect | Étiologies principales |\n"
            "|------|--------|----------------------|\n"
            "| Erythemateuse | Amygdales congestives | Virale+++, SBHA |\n"
            "| Erythemato-pultacee | Exsudat pultace ne debordant pas | Virale (EBV), SBHA |\n"
            "| Pseudo-membraneuse | Fausses membranes adherentes | MNI, diphterie |\n"
            "| Vesiculeuse | Vesicules a base inflammatoire | Coxsackie (herpangine), HSV |\n"
            "| Ulcereuse unilaterale | Ulceration profonde | Vincent, chancre syphilitique, cancer, hemopathie |\n"
        )),
        TableauSynthese(titre="Sinusites aiguës de l'adulte", markdown=(
            "| | Maxillaire | Frontale | Sphenoidale |\n"
            "|--|-----------|---------|-------------|\n"
            "| Douleur | Sous-orbitaire, pulsatile, cyclique | Frontale en barre, violente | Retro-orbitaire, vertex |\n"
            "| Complications | Osteites, orbitaires | Neuro-meningees++ | Neuro-meningees++ |\n"
            "| Examens | Aucun | Scanner | Scanner++ |\n"
        )),
        TableauSynthese(titre="Tympanométrie - Interprétation", markdown=(
            "| Courbe | Signification |\n"
            "|--------|---------------|\n"
            "| Pic normal centre sur 0 | Normal |\n"
            "| Cheminee (tour Eiffel) | Rupture chaine / hyper-laxite |\n"
            "| Type C (decentree) | Dysfonction tubaire |\n"
            "| Type B (plate) | Épanchement retro-tympanique |\n"
            "| Aucune courbe | Perforation tympanique |\n"
            "| Pic bifide | Tympan cicatriciel non homogene |\n"
        )),
        TableauSynthese(titre="Otites moyennes aiguës - Stades otoscopiques", markdown=(
            "| Stade | Otalgies | Fievre | Otoscopie |\n"
            "|-------|----------|--------|-----------|\n"
            "| Congestive | A repetition, pulsatiles | Variable | Tympan hypervascularise |\n"
            "| Collectee | Permanentes | Elevee | Bombant rouge cerise |\n"
            "| Perforee | Diminuees | Diminuee | Perforation + otorrhee purulente |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Parametre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Perte max surdite transmission | **60 dB** | Transmission |\n"
        "| Assourdissement audiometrie | Difference > **60 dB** | Transmission trans-cranienne |\n"
        "| Reflexe stapedien normal | **80-90 dB** | Seuil declenchement |\n"
        "| Encoche de Carhart | **2000 Hz** | Otospongiose |\n"
        "| Prothese auditive presbyacousie | Perte > **30 dB** a 2000 Hz | Indication |\n"
        "| Zone alarme bruit professionnel | > **85 dB** pendant 8h/j | Traumatisme sonore |\n"
        "| Scotome auditif professionnel | **4000 Hz** | Frequence touchee |\n"
        "| SUB pronostic | **50-75%** ne recuperent pas | Surdite brusque |\n"
        "| SUB neurinome | **10%** des SUB | Recherche systematique |\n"
        "| ATB angine SBHA | Amoxicilline **6 jours** | 1ere intention |\n"
        "| Eviction collectivite angine | **48h** d'ATB | SBHA |\n"
        "| Amygdalectomie recidives | > **3/an x 3 ans** ou > **5/an x 2 ans** | Indication |\n"
        "| Sinusite maxillaire enfant | Pas avant **3 ans** | Sinus non forme |\n"
        "| Tamponnement anterieur | **48-72h** max | Non resorbable |\n"
        "| Tamponnement posterieur | **72h** max | Ballonnet |\n"
        "| Transfusion epistaxis | < **7 g/dL** ou < **10 g/dL** coronarien | Seuils Hb |\n"
        "| OSM enfant | **50%** des enfants | Épidémiologie |\n"
        "| ATT indication | Surdite > **30 dB** bilaterale | Avec retard langage |\n"
        "| Surveillance cholesteatome | **10 ans** minimum | Post-chirurgie |\n"
    ))

    points_cles = [
        "Surdite de transmission : Weber lateralise cote atteint, Rinne negatif, perte max 60 dB, CO normale",
        "Surdite de perception : Weber lateralise cote sain, Rinne positif, intelligibilite diminuee par le bruit",
        "Otospongiose : femme jeune + tympans normaux + encoche de Carhart + reflexe stapedien aboli",
        "Surdite brusque = URGENCE : corticotherapie < J10, toujours rechercher neurinome (10% des SUB)",
        "Angine a SBHA : TDR positif = amoxicilline 6 jours ; jamais d'AINS ; prevenir le RAA",
        "Dysphonie > 3 semaines chez sujet OH-tabagique = laryngoscopie pour eliminer cancer",
        "Epistaxis : compression bi-digitale puis tamponnement puis PEC interventionnelle ; jamais emboliser les ethmoidales",
        "Sinusite maxillaire aigue non compliquee : aucun examen complementaire",
        "Ethmoidite aigue de l'enfant = urgence : scanner + ATB IV (CG3 + clindamycine)",
        "OSM unilaterale chez l'adulte = rechercher cancer du cavum ; cholesteatome = chirurgie + surveillance 10 ans",
    ]

    fiche_eclair_md = (
        "**Surdites** : Transmission (oreille ext/moy, Weber cote atteint, Rinne negatif, max 60 dB) "
        "vs Perception (oreille int/nerf, Weber cote sain, cocktail party). "
        "Otospongiose = femme jeune + encoche Carhart. "
        "SUB = urgence, corticotherapie < J10, 10% neurinome.\n\n"
        "**Angines** : 80% virales. SBHA : TDR + amoxicilline 6j. "
        "Pseudo-membraneuse : MNI (pas ATB) ou diphterie (urgence, DO). "
        "Ulcereuse : Vincent (Lemierre) ou cancer/hemopathie. "
        "Complications SBHA : phlegmon, RAA (coeur+articulations).\n\n"
        "**Dysphonie** : Aigue = laryngite (repos vocal). Chronique > 3 mois = "
        "laryngoscopie systematique. Laryngite chronique = pre-cancereuse. "
        "Paralysie laryngee : chercher cancer sur trajet du X.\n\n"
        "**Epistaxis** : compression bi-digitale > tamponnement anterieur > posterieur > "
        "interventionnel. Jamais emboliser ethmoidales. HTA a rechercher. "
        "Fibrome naso-pharyngien : garcon, pas de biopsie.\n\n"
        "**Sinusites** : Maxillaire aigue = aucun examen. Frontale/sphenoidale = scanner + "
        "complications neuro-meningees. Polypose = anosmie + Widal. "
        "Ethmoidite enfant = urgence (CG3+clindamycine IV).\n\n"
        "**Otites** : OE = otalgie + tragus douloureux + apyrexie. "
        "OMA : H. influenzae (40%), pneumocoque (30%). "
        "Congestive > collectee > perforee. "
        "Mastoidite = urgence (tri-ATB). "
        "OSM unilaterale adulte = cancer cavum. "
        "Cholesteatome = chirurgie + surveillance 10 ans."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="ORL",
        annee="2025-2026",
        item="Items 85, 86, 87, 127, 145, 147",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi],
        tableaux=tableaux,
        chiffres_cles=chiffres_cles,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        usage=UsageStats(),
    )


def main():
    output_dir = PROJECT_ROOT / "output"
    output_dir.mkdir(exist_ok=True)

    fiche = build_fiche()

    docx_path = output_dir / "Medecine_generale_ORL_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Medecine_generale_ORL_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path}")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

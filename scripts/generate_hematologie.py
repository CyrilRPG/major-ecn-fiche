"""Genere la fiche exhaustive d'Hematologie a partir du texte source."""

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


def build_hematologie_fiche() -> FicheData:
    plan = [
        PlanPartie(numero="I", titre="Anemie : orientation diagnostique", sous_parties=[
            PlanSousPartie(lettre="A", titre="Syndrome anemique et orientation clinique"),
            PlanSousPartie(lettre="B", titre="Hemogramme et examens complementaires"),
            PlanSousPartie(lettre="C", titre="Anemie microcytaire"),
            PlanSousPartie(lettre="D", titre="Anemie normo/macrocytaire regenerative"),
            PlanSousPartie(lettre="E", titre="Anemie normo-macrocytaire aregenerative"),
        ]),
        PlanPartie(numero="II", titre="Hemogramme et variations", sous_parties=[
            PlanSousPartie(lettre="A", titre="Valeurs normales de l'hemogramme"),
            PlanSousPartie(lettre="B", titre="Anomalies des lignees blanches et plaquettaires"),
        ]),
        PlanPartie(numero="III", titre="Hemopathies malignes", sous_parties=[
            PlanSousPartie(lettre="A", titre="Leucemie aigue"),
            PlanSousPartie(lettre="B", titre="Leucemie lymphoide chronique"),
            PlanSousPartie(lettre="C", titre="Myelome multiple des os"),
            PlanSousPartie(lettre="D", titre="Lymphome non hodgkinien et lymphome de Hodgkin"),
        ]),
        PlanPartie(numero="IV", titre="Syndromes myeloproliferatifs", sous_parties=[
            PlanSousPartie(lettre="A", titre="Leucemie myeloide chronique"),
            PlanSousPartie(lettre="B", titre="Polyglobulie de Vaquez"),
            PlanSousPartie(lettre="C", titre="Thrombocytemie essentielle"),
        ]),
        PlanPartie(numero="V", titre="Thrombopenie et adenopathie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Thrombopenie"),
            PlanSousPartie(lettre="B", titre="Adenopathie superficielle"),
            PlanSousPartie(lettre="C", titre="Splenomegalie"),
        ]),
        PlanPartie(numero="VI", titre="Anticoagulants, transfusion et divers", sous_parties=[
            PlanSousPartie(lettre="A", titre="Prescription et surveillance des anticoagulants"),
            PlanSousPartie(lettre="B", titre="Accidents des anticoagulants"),
            PlanSousPartie(lettre="C", titre="Transfusion sanguine et produits derives du sang"),
            PlanSousPartie(lettre="D", titre="Hypereosinophilie et syndrome mononucleosique"),
        ]),
    ]

    # -- PARTIE I : ANEMIE --
    partie_i = Partie(numero="I", titre="Anemie : orientation diagnostique", sous_parties=[
        SousPartie(lettre="A", titre="Syndrome anemique et orientation clinique", rows=[
            FicheRow(concept="Syndrome anemique", detail_md=(
                "- Symptomatologie dependante de la **vitesse d'installation** ++\n"
                "- **Paleur cutaneo-muqueuse**\n"
                "- Manifestations fonctionnelles de l'anoxie :\n"
                "  - Asthenie, dyspnee d'effort\n"
                "  - Troubles neurosensoriels : vertiges, acouphenes\n"
                "  - Tachycardie\n"
                "- Complications graves : **IDM**, confusion, detresse respiratoire aigue"
            )),
            FicheRow(concept="Interrogatoire et examen physique", detail_md=(
                "- Preciser le syndrome anemique : signes fonctionnels, contexte de decouverte, rapidite d'installation\n"
                "- Recueil des **hemogrammes anterieurs**\n"
                "- Cinetique d'installation, ATCD personnels et familiaux"
            )),
            FicheRow(concept="Orientation diagnostique clinique", detail_md=(
                "| Signes cliniques | Orientation |\n"
                "|-----------------|-------------|\n"
                "| Ictere, SMG | Anemie hemolytique |\n"
                "| Signes de sidéropathie | Carence martiale |\n"
                "| Ascite, CVC abdominale, HSMG | Cirrhose |\n"
                "| Glossite, troubles neurologiques | Carence B12 |\n"
                "| Syndrome hemorragique cutaneo-muqueux | Insuffisance medullaire |\n"
                "| ADP, SMG | Hemopathie maligne |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- L'anemie est definie par une **diminution de l'hemoglobine** et non par le nombre de GR\n"
                "- Toujours preciser : VGM, reticulocytes, et confronter aux signes cliniques"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Hemogramme et examens complementaires", rows=[
            FicheRow(concept="Definition de l'anemie", detail_md=(
                "| Population | Seuil Hb |\n"
                "|-----------|----------|\n"
                "| Nouveau-ne | < **14** g/dL |\n"
                "| Jeune enfant | < **11** g/dL |\n"
                "| Homme adulte | < **13** g/dL |\n"
                "| Femme adulte | < **12** g/dL |\n"
                "| Femme enceinte (> 2e trimestre) | < **10,5** g/dL |\n"
            )),
            FicheRow(concept="Orientation selon le VGM", detail_md=(
                "- **Microcytaire** (VGM < 80 fL) : carence martiale, inflammation, thalassemie\n"
                "- **Normocytaire/macrocytaire** : dosage des reticulocytes ++\n"
                "  - **Regenerative** (reticulocytes > 150 G/L) : hemorragie, hemolyse\n"
                "  - **Aregenerative** (reticulocytes < 150 G/L) : cause centrale"
            )),
            FicheRow(concept="", detail_md=(
                "- Le dosage des **reticulocytes** n'est indique que si l'anemie est **normo ou macrocytaire**\n"
                "- Pas de dosage reticulocytes si anemie microcytaire (toujours aregenerative)"
            ), kind="piege"),
            FicheRow(concept="Examens selon contexte", detail_md=(
                "- Bilan inflammatoire (CRP)\n"
                "- BHC\n"
                "- Bilan d'hemolyse (haptoglobine, bilirubine libre, LDH)\n"
                "- **Bilan martial** (fer serique + CST ou ferritinemie)\n"
                "- Groupe, Rh, RAI si transfusion envisagee"
            )),
        ]),
        SousPartie(lettre="C", titre="Anemie microcytaire", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Anemie avec **VGM < 80 fL**\n"
                "- Toujours **aregenerative** : pas de dosage reticulocytes\n"
                "- Microcytose par deficit quantitatif des composants de l'Hb (heme, globines)"
            )),
            FicheRow(concept="3 etiologies principales", detail_md=(
                "- **Carence martiale** (la plus frequente)\n"
                "- **Inflammation chronique**\n"
                "- **Thalassemie**"
            )),
            FicheRow(concept="Bilan complementaire", detail_md=(
                "- **1ere intention** : Fer serique + CST ou Ferritinemie + CRP\n"
                "- **2e intention** (si absence carence martiale et inflammation) : **Electrophorese de l'Hb**"
            )),
            FicheRow(concept="Anemie ferriprive", detail_md=(
                "- Syndrome anemique souvent bien tolere (installation progressive)\n"
                "- **Syndrome carentiel** (sideropenie) :\n"
                "  - Fragilite des phaneres : ongles cassants, chute capillaire\n"
                "  - Fragilite des muqueuses : glossite, perleche\n"
                "  - Trouble du comportement alimentaire : **PICA**\n"
                "- Hemogramme : anemie marquee **microcytaire hypochrome** + **thrombocytose** associee\n"
                "- Bilan martial (avant tout traitement) : fer serique et CST diminues OU ferritinemie diminuee"
            )),
            FicheRow(concept="Étiologie carence martiale", detail_md=(
                "- Rechercher un **saignement chronique** ++ :\n"
                "  - **Digestif** : toucher rectal, endoscopies digestives\n"
                "  - **Gynecologique** chez la femme : echographie genitale\n"
                "- Plus rarement : carence d'apport, malabsorption sur resection digestive etendue"
            )),
            FicheRow(concept="Traitement carence martiale", detail_md=(
                "- **Traitement etiologique indispensable** : traiter le saignement chronique ++\n"
                "- Sels ferreux PO (Tardyferon) : **2 cp/j pendant 4 mois** sans interruption\n"
                "- Surveillance : hemogramme + reticulocytes a **J10** (crise reticulocytaire) puis hemogramme/mois"
            )),
            FicheRow(concept="", detail_md=(
                "- Toujours rechercher la **cause du saignement** avant de traiter la carence\n"
                "- La crise reticulocytaire a J10 confirme l'efficacite du traitement"
            ), kind="a_retenir"),
            FicheRow(concept="Inflammation chronique", detail_md=(
                "| | Fer serique | CST |\n"
                "|--|-----------|-----|\n"
                "| **Carence martiale** | Diminue | Diminue |\n"
                "| **Inflammation chronique** | Diminue | **Normal** |\n\n"
                "- Observable dans tous les grands syndromes inflammatoires chroniques : cancers, arthrite rhumatoide\n"
                "- Traitement etiologique ++ de l'inflammation"
            )),
            FicheRow(concept="Thalassemie", detail_md=(
                "- Deficit quantitatif par mutation sur les chaines alpha ou beta de l'Hb\n"
                "- Transmission **autosomique recessive**\n"
                "- Hemogramme : anemie microcytaire **sans thrombocytose**\n"
                "- Stigmates d'**hemolyse** + anomalies a l'**electrophorese de l'Hb**\n"
                "- PEC : support transfusionnel si necessaire, chelateur fer des ferritine > 1000 ug/L, conseil genetique"
            )),
            FicheRow(concept="", detail_md=(
                "- La **thrombocytose** oriente vers la carence martiale (absente dans la thalassemie)\n"
                "- Le CST est **normal** dans l'inflammation (diminue dans la carence martiale)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Anemie normo/macrocytaire regenerative", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Hb diminuee avec **VGM > 80 fL** et **reticulocytes > 150 G/L**\n"
                "- En tout premier lieu : **eliminer une hemorragie** ++"
            )),
            FicheRow(concept="Signes biologiques d'hemolyse", detail_md=(
                "- **Haptoglobine effondree** (le plus specifique)\n"
                "- Bilirubine libre augmentee\n"
                "- LDH augmentee\n"
                "- En l'absence d'hemolyse : regeneration medullaire (post anemie carentielle traitee)"
            )),
            FicheRow(concept="Anemies hemolytiques corpusculaires", detail_md=(
                "- **Constitutionnelles** :\n"
                "  - Anomalies de la membrane du GR : **Minkowski-Chauffard**, elliptocytose\n"
                "  - Hemoglobinopathies : **thalassemies**, **drepanocytose**, hemoglobinose C/D/E\n"
                "  - Anomalies enzymatiques : deficit en **G6PD**, deficit en pyruvate kinase\n"
                "- **Acquise** : hemoglobinurie paroxystique nocturne"
            )),
            FicheRow(concept="Anemies hemolytiques extra-corpusculaires", detail_md=(
                "- **Immunologiques** :\n"
                "  - Hemolyse allo-immune post-transfusionnelle / maladie hemolytique du NN\n"
                "  - **AHAI** (test de Coombs direct positif)\n"
                "  - Anemie hemolytique immuno-allergique\n"
                "- **Mecaniques** : MAT, valves cardiaques, CEC\n"
                "- **Infections** : paludisme, septicemie\n"
                "- Autres : saturnisme, venin, toxiques"
            )),
            FicheRow(concept="Specificites diagnostiques", detail_md=(
                "- **Drepanocytose** : hemoglobine S a l'electrophorese de l'Hb, complications = CVO (micro-infarctus osseux douloureux)\n"
                "- **MAT** : presence de **schizocytes** au frottis sanguin (hemolyse mecanique)\n"
                "- **AHAI** : TDA positif (IgG +/- C3d, IgM), rechercher pathologie systemique ou syndrome lymphoproliferatif\n"
                "  - Traitement : corticotherapie si AHAI a Ac chaud, **Rituximab** si MAF"
            )),
            FicheRow(concept="Traitement commun", detail_md=(
                "- **Transfusion CGR** si urgence vitale\n"
                "- Supplementation folates : **Speciafoldine** 1 cp/j\n"
                "- Conseil genetique en cas de pathologies constitutionnelles"
            )),
        ]),
        SousPartie(lettre="E", titre="Anemie normo-macrocytaire aregenerative", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Hb diminuee avec **VGM > 80 fL** et **reticulocytes < 150 G/L**\n"
                "- Bilan systematique : **creatininemie**, BHC et **TSH** (eliminer IR, IH, insuffisance thyroidienne)\n"
                "- **Myelogramme systematique** dans cette situation"
            )),
            FicheRow(concept="Étiologies selon myelogramme", detail_md=(
                "| Moelle | Étiologies |\n"
                "|--------|------------|\n"
                "| **Pauvre** | Aplasie medullaire (acquise, post-chimio), myelofibrose |\n"
                "| **Riche** | Envahissement medullaire (LAM, SMD, lymphome, metastases), carence B9/B12 |\n"
            )),
            FicheRow(concept="★ Carence en B12 : tableau clinique", detail_md=(
                "- Syndrome anemique\n"
                "- **Syndrome carentiel** :\n"
                "  - Signes digestifs : glossite, dysphagie, dysgeusie, oesophagite\n"
                "  - Signes cutanes : peau seche, ongles cassants, perte de cheveux\n"
                "  - **Manifestations neurologiques** (uniquement B12) : sclerose combinee de la moelle "
                "(**syndrome cordonal posterieur** + **syndrome pyramidal**)"
            )),
            FicheRow(concept="", detail_md=(
                "- Les signes neurologiques (sclerose combinee) sont **specifiques de la carence en B12**\n"
                "- Absents dans la carence en folates"
            ), kind="piege"),
            FicheRow(concept="Examens complementaires B9/B12", detail_md=(
                "- NFS : anemie **megaloblastique** (VGM > 120 fL) aregenerative\n"
                "- Leuconeutropenie et thrombopenie possibles\n"
                "- Signes biologiques d'hemolyse **intra-medullaire**\n"
                "- Myelogramme : moelle riche **bleue** avec aspect megaloblastique\n"
                "- **Dosages vitaminiques** (B12 serique, folates seriques) avant tout traitement substitutif"
            )),
            FicheRow(concept="Étiologies des carences", detail_md=(
                "| | Carence en folates | Carence en B12 |\n"
                "|--|-------------------|----------------|\n"
                "| Apports < besoins | OH, nutrition parenterale, grossesse | Regime vegetalien |\n"
                "| Malabsorption | Maladie coeliaque, Crohn | **Anemie de Biermer**, gastrectomie, resection ileale |\n"
                "| Autres | Medicaments antifoliques (MTX, Bactrim) | Deficit congenital en transcobalamines |\n"
            )),
            FicheRow(concept="Maladie de Biermer", detail_md=(
                "- Diagnostic positif :\n"
                "  - Affirmer carence en B12 : dosage vit B12 diminuee\n"
                "  - Maladie gastrique : achlorhydrie totale, **dosage gastrine augmentee**\n"
                "  - Deficit en facteur intrinseque : recherche **Ac anti-facteur intrinseque** et Ac anti-estomac\n"
                "- Surveillance : hemogramme + bilan martial 6-8 semaines, **fibroscopie gastrique tous les 3 ans** (cancer gastrique)"
            )),
            FicheRow(concept="Traitement curatif", detail_md=(
                "- **Folates** : acide folique 30 mg/j pendant 2 mois (curatif), 5 mg/j (preventif)\n"
                "- **Vitamine B12** : cyanocobalamine/hydroxycobalamine IM/IV a vie :\n"
                "  - 1000 ug/j pendant 10 jours\n"
                "  - Puis 1000 ug/semaine jusqu'a normalisation Hb\n"
                "  - Puis **1000 ug/mois a vie**"
            )),
            FicheRow(concept="", detail_md=(
                "- Si carence en B12 **et** folates : commencer par traiter la **carence en B12**\n"
                "- Sinon risque d'aggravation/apparition des **troubles neurologiques**"
            ), kind="a_retenir"),
        ]),
    ])

    # -- PARTIE II : HEMOGRAMME --
    partie_ii = Partie(numero="II", titre="Hemogramme et variations", sous_parties=[
        SousPartie(lettre="A", titre="Valeurs normales de l'hemogramme", rows=[
            FicheRow(concept="Valeurs normales", detail_md=(
                "| Parametre | Homme | Femme |\n"
                "|-----------|-------|-------|\n"
                "| Hemoglobine (g/dL) | **13-17** | **12-16** |\n"
                "| VGM (fL) | 80-100 | 80-100 |\n"
                "| Plaquettes (G/L) | 150-400 | 150-400 |\n"
                "| Leucocytes (G/L) | 4-10 | 4-10 |\n"
                "| PNN (G/L) | 1,7-7 | 1,7-7 |\n"
                "| PNE (G/L) | < 500/mm3 | < 500/mm3 |\n"
                "| PNB (G/L) | < 200/mm3 | < 200/mm3 |\n"
                "| Lymphocytes (G/L) | 1,4-4 | 1,4-4 |\n"
                "| Monocytes (G/L) | 0,5-1 | 0,5-1 |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Attention aux unites : **4000/mm3 = 4 G/L**\n"
                "- Les valeurs de l'hemogramme sont a connaitre **par coeur**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Anomalies des lignees blanches et plaquettaires", rows=[
            FicheRow(concept="★ Thrombocytose", detail_md=(
                "- **Reactionnelles** ++ (taux souvent < 800 G/L) :\n"
                "  - Stress : chirurgie, accouchement\n"
                "  - Syndrome inflammatoire\n"
                "  - **Carence martiale**\n"
                "  - Splenectomie\n"
                "- **Primitives** : syndromes myeloproliferatifs (thrombocytemie essentielle, Vaquez, LMC, myelofibrose)"
            )),
            FicheRow(concept="Polynucleose neutrophile", detail_md=(
                "- **Secondaire** :\n"
                "  - Infection bacterienne ++\n"
                "  - Causes physiologiques : effort physique, post-prandial, fin grossesse, nouveau-ne\n"
                "  - Tabagisme, maladies inflammatoires, necroses tissulaires (IDM)\n"
                "  - Cancers, lymphomes\n"
                "  - Medicaments : corticoides, G-CSF, lithium\n"
                "- **Primitive** : syndromes myeloproliferatifs"
            )),
            FicheRow(concept="Neutropenie", detail_md=(
                "- Margination excessive selon l'origine ethnique (physiologique)\n"
                "- Infections virales\n"
                "- Maladies auto-immunes (lupus)\n"
                "- Hypersplenisme\n"
                "- Insuffisance medullaire : envahissement, carence B9/B12 (pancytopenie)"
            )),
            FicheRow(concept="Hyperlymphocytose", detail_md=(
                "- **Enfant** : reactionnelles et benignes (coqueluche, viroses)\n"
                "- **Adolescent** : syndrome mononucleosique\n"
                "- **Adulte > 40 ans** : **syndrome lymphoproliferatif** ++ (LLC)"
            )),
            FicheRow(concept="Lymphopenie", detail_md=(
                "- Infections virales : **VIH** ++\n"
                "- Maladie systemique : **lupus** ++\n"
                "- Étiologie congenitale chez l'enfant : deficit immunitaire primitif\n"
                "- Iatrogene : traitement immunosuppresseur, corticotherapie"
            )),
        ]),
    ])

    # -- PARTIE III : HEMOPATHIES MALIGNES --
    partie_iii = Partie(numero="III", titre="Hemopathies malignes", sous_parties=[
        SousPartie(lettre="A", titre="Leucemie aigue", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Proliferation maligne de cellules immatures (myeloides ou lymphoides)\n"
                "- Bloquees a un stade precoce de leur differenciation\n"
                "- Accumulation dans la moelle, le sang et eventuellement d'autres organes"
            )),
            FicheRow(concept="Quand evoquer : cliniquement", detail_md=(
                "- **Retentissement des cytopenies** :\n"
                "  - Asthenie, dyspnee (anemie)\n"
                "  - Saignements inhabituels (thrombopenie, CIVD)\n"
                "  - Infections recidivantes (neutropenie)\n"
                "- **Syndrome tumoral** :\n"
                "  - Syndrome de **leucostase** pulmonaire (hypoxie, detresse respiratoire) ou neurologique (confusion, convulsions)\n"
                "  - Adenopathies (LAL)\n"
                "  - Envahissement d'organes (os, testicule, peau)"
            )),
            FicheRow(concept="Quand evoquer : biologiquement", detail_md=(
                "- Cytopenies +/- blastose circulante\n"
                "- **Syndrome de lyse biologique** :\n"
                "  - Hyperkaliemie, insuffisance renale aigue, hyperuricemie\n"
                "- **CIVD** : TP effondre, fibrinogene abaisse, thrombopenie, D-Dimeres augmentes"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant des cytopenies avec ou sans blastose circulante :\n"
                "  - Realiser un **bilan de coagulation** (CIVD)\n"
                "  - Rechercher les **signes de gravite** : saignement actif, plaquettes < 20 G/L, leucostase, lyse\n"
                "  - Adresser aux urgences pour PEC hematologique"
            ), kind="a_retenir"),
            FicheRow(concept="Prise en charge", detail_md=(
                "- **Myelogramme** : diagnostic si > **20% de blastes medullaires**\n"
                "- Etude immunophenotypique, cytogenetique et moleculaire\n"
                "- Traitement adapte a l'age, aux comorbidites et au type de leucemie\n"
                "- Validation en **RCP**"
            )),
        ]),
        SousPartie(lettre="B", titre="Leucemie lymphoide chronique", rows=[
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Decouverte souvent **fortuite** sur hemogramme\n"
                "- **Hyperlymphocytose persistante > 3 mois**\n"
                "- Syndrome tumoral avec ADP **bilaterales, indolores et symetriques**"
            )),
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- Hemogramme :\n"
                "  - Hyperlymphocytose > **5000/mm3**\n"
                "  - Frottis sanguin : predominance petits lymphocytes matures, **ombres de Gumprecht** (lymphocytes lyses)\n"
                "- **Immunophenotypage lymphocytes circulants** : score de **Matutes > 3**"
            )),
            FicheRow(concept="", detail_md=(
                "- Toute lymphocytose isolee > 5000/mm3 persistant > **3 mois** chez un sujet adulte "
                "doit faire evoquer le diagnostic de LLC"
            ), kind="a_retenir"),
            FicheRow(concept="Bilan initial", detail_md=(
                "- EPP : hypogammaglobulinemie, pic monoclonal\n"
                "- **Test direct a l'antiglobuline** : recherche AHAI\n"
                "- Pronostic : caryotype sur sang (**del 17p**) et biologie moleculaire (mutation **TP53**)"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- **Surveillance simple** si absence d'evolutivite ou de retentissement clinique\n"
                "- Sinon : chimiotherapie (RFC) ou therapie ciblee (**ibrutinib**)\n"
                "- Prophylaxie infectieuse (amoxicilline), MAJ vaccins, IgIV si hypogammaglobulinemie symptomatique\n"
                "- Complications :\n"
                "  - Infectieuses : germes encapsules ++ (**pneumocoque**)\n"
                "  - AHAI\n"
                "  - Insuffisance medullaire\n"
                "  - Transformation : lymphome agressif B diffus a grandes cellules (**syndrome de Richter**)"
            )),
        ]),
        SousPartie(lettre="C", titre="Myelome multiple des os", rows=[
            FicheRow(concept="★ Généralités", detail_md=(
                "- Hemopathie maligne : proliferation d'un **clone plasmocytaire tumoral** "
                "responsable d'une secretion d'**Ig monoclonale**\n"
                "- **2e hemopathie maligne** en frequence\n"
                "- Terrain : sujet > **50 ans** (pic a 65 ans, sex-ratio = 1)\n"
                "- Esperance de vie : 6 ans"
            )),
            FicheRow(concept="Types de myelomes", detail_md=(
                "- Myelome multiple IgG, IgA, IgD, IgE avec chaines legeres kappa/lambda ++\n"
                "- Myelome a chaines legeres kappa/lambda\n"
                "- Myelome non excretant/secretant (hypogammaglobulinemie seule a l'EPP)"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- **Signes de resorption osseuse** :\n"
                "  - Douleurs osseuses souvent inaugurales (horaire mixte, nocturnes, insomniantes, localisees au rachis/bassin/cotes)\n"
                "  - Fractures pathologiques, radiculalgies\n"
                "- **Syndrome d'hyperviscosité** + insuffisance medullaire :\n"
                "  - AEG, anemie, signes neurologiques\n"
                "  - Cephalees, vertiges, somnolence, troubles visuels et auditifs\n"
                "- Risque d'infection augmente"
            )),
            FicheRow(concept="Diagnostic positif", detail_md=(
                "- **1. Proliferation plasmocytaire** :\n"
                "  - Myelogramme : plasmocytes medullaires > **10%**, cellules de **Mott** (plasmocytes tumoraux dystrophiques)\n"
                "  - Immunophenotypage medullaire si doute\n"
                "- **2. Ig monoclonale** :\n"
                "  - EPS : pic Ig monoclonal (++ IgG), hypogammaglobulinemie frequente\n"
                "  - Immunofixation : confirme caractere monoclonal, precise le type\n"
                "  - EPU + immunofixation urinaire : proteinurie de **Bence-Jones**\n"
                "  - Mesure chaines legeres libres seriques (CLL)\n"
                "- **3. Resorption osseuse** :\n"
                "  - RX squelette axial : demineralisation, **geodes** (lacunes a l'emporte-piece), fractures-tassements\n"
                "  - Hypercalcemie\n"
                "  - IRM rachis/bassin (urgence si compression medullaire)\n"
                "  - TEP-scanner"
            )),
            FicheRow(concept="Criteres CRAB", detail_md=(
                "| Lettre | Critere | Seuil |\n"
                "|--------|---------|-------|\n"
                "| **C** | Calcemie | > 2,75 mmol/L |\n"
                "| **R** | Atteinte renale | Creatinine > 177 umol/L ou DFG < 40 mL/min |\n"
                "| **A** | Anemie | Hb < 10 g/dL |\n"
                "| **B** | Bone lesion | Lesions osseuses lytiques |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Les criteres **CRAB** determinent l'indication therapeutique\n"
                "- CRAB 0 = myelome asymptomatique : pas de traitement, surveillance trimestrielle\n"
                "- Presence CRAB = traitement indique"
            ), kind="a_retenir"),
            FicheRow(concept="Score pronostique ISS", detail_md=(
                "| Stade | Criteres |\n"
                "|-------|----------|\n"
                "| I | Beta-2-microglobuline < 3,5 mg/L **ET** albuminemie > 35 g/L |\n"
                "| II | Intermediaire |\n"
                "| III | Beta-2-microglobuline > **5,5 mg/L** |\n"
            )),
            FicheRow(concept="Prise en charge", detail_md=(
                "- **Sujet jeune < 65 ans** : CT de reduction tumorale, prelevement CSH, intensification CT puis **autogreffe**\n"
                "- **Sujet age > 65 ans** : CT sans autogreffe\n"
                "- Objectif : obtention **remission complete** (disparition pic a l'immunofixation)\n"
                "- Education patient : prohibition **nephrotoxiques** (AINS++) et automedication"
            )),
            FicheRow(concept="Complications renales", detail_md=(
                "- **Nephropathie a cylindres myelomateux** (NCM) : la plus frequente\n"
                "  - IRA nue, proteinurie de fort debit a chaines legeres\n"
                "  - FDR : hypercalcemie, DEC, infections, nephrotoxiques, PDC iodes\n"
                "- Syndrome de Fanconi : glycosurie normoglycemique, hypo-uricemie, diabete phosphate\n"
                "- **Amylose AL** (< 20%)\n"
                "- **Syndrome de Randall** : depots non amyloides d'Ig monoclonales"
            )),
            FicheRow(concept="Autres complications", detail_md=(
                "- Infectieuses : bacteriennes ++\n"
                "- Hematologiques : insuffisance medullaire, leucemie a plasmocytes\n"
                "- Neurologiques : compression medullaire/radiculaire, neuropathies peripheriques\n"
                "- Syndrome d'hyperviscosité plasmatique\n"
                "- Osseuses : fractures pathologiques\n"
                "- Metaboliques : **hypercalcemie** ++, hyperuricemie\n"
                "- Cryoglobulinemie type I et II"
            )),
            FicheRow(concept="", detail_md=(
                "- Le myelome non excretant ne presente qu'une **hypogammaglobulinemie** a l'EPP\n"
                "- Ne pas oublier les criteres **SLIM** en plus des CRAB pour l'indication therapeutique"
            ), kind="piege"),
        ]),
        SousPartie(lettre="D", titre="Lymphome non hodgkinien et lymphome de Hodgkin", rows=[
            FicheRow(concept="LNH : generalites", detail_md=(
                "- Developpement a partir de cellules lymphoides **B (85%)** / T (15%)\n"
                "- Étiologies : infections chroniques (H. pylori, EBV, HHV8, HTLV1), deficits immunitaires (VIH), facteurs genetiques"
            )),
            FicheRow(concept="LNH : tableau clinique", detail_md=(
                "- **Signes generaux (signes B)** : fievre, sueurs nocturnes, amaigrissement\n"
                "- **Syndrome tumoral** :\n"
                "  - ADP superficielles persistantes, HSMG\n"
                "  - ADP profondes : urgence si **syndrome cave superieur** ou ADP abdominales compressives\n"
                "  - Masse tumorale palpable\n"
                "  - Infiltration cutanee dans les lymphomes T"
            )),
            FicheRow(concept="LNH : classification OMS", detail_md=(
                "| Type | Exemples |\n"
                "|------|----------|\n"
                "| **B indolent** | LF, LZM, LLC, LW, LCM |\n"
                "| **B agressif** | LBDGC, **Burkitt** |\n"
                "| **T** | LNH T peripherique, LTAI, anaplasie |\n"
            )),
            FicheRow(concept="LNH : diagnostic", detail_md=(
                "- **Biopsie organe atteint** : exerese chirurgicale totale si ganglion\n"
                "- Analyse anatomopathologique + immunohistochimique + cytogenetique\n"
                "- Syndrome de lyse tumorale : augmentation LDH, acide urique, hyperphosphoremie, hypocalcemie, hyperkaliemie"
            )),
            FicheRow(concept="LNH : bilan d'extension", detail_md=(
                "- Scanner TAP injecte\n"
                "- BOM : envahissement medullaire\n"
                "- PL si lymphomes agressifs\n"
                "- PET-scanner si LBDGC\n"
                "- Classification d'**Ann Arbor** (stades I a IV)"
            )),
            FicheRow(concept="LNH : traitement", detail_md=(
                "- Polychimiotherapie : **R-CHOP** si CD20+ (immunotherapie : Ac monoclonaux +++)\n"
                "- Radiotherapie ciblee si masse importante localisee\n"
                "- Intensification + autogreffe/allogreffe si necessaire\n"
                "- Decision en RCP, inclusion protocole d'etude\n"
                "- Surveillance tous les 3 mois pendant 2 ans, puis 6 mois, puis annuelle"
            )),
            FicheRow(concept="Lymphome de Hodgkin", detail_md=(
                "- Proliferation tumorale des cellules lymphoides de **Reed-Sternberg**\n"
                "- Signes specifiques : **hypereosinophilie**, douleur a l'ingestion d'alcool, **prurit**\n"
                "- Classification (Lukes-Rye/OMS) :\n"
                "  - LH classique (95%) : scleronodulaire (65%), cellularite mixte (30%), riche en lymphocytes, depletion lymphocytaire (1%)\n"
                "  - LH nodulaire a predominance lymphocytaire (paragranulome de Poppema, 5%)"
            )),
        ]),
    ])

    # -- PARTIE IV : SYNDROMES MYELOPROLIFERATIFS --
    partie_iv = Partie(numero="IV", titre="Syndromes myeloproliferatifs", sous_parties=[
        SousPartie(lettre="A", titre="Leucemie myeloide chronique", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Proliferation de cellules matures predominant sur la ligne des PNN\n"
                "- Mutation genetique acquise : proteine de fusion **BCR-ABL** (translocation chromosomes 9 et 22)"
            )),
            FicheRow(concept="Quand evoquer", detail_md=(
                "- **Cliniquement** : asthenie, **splenomegalie**, crise de goutte, thrombose arterielle ou veineuse\n"
                "- **Biologiquement** :\n"
                "  - **Hyperleucocytose > 50 G/L**\n"
                "  - PNN constamment augmentes\n"
                "  - PNB frequemment augmentes\n"
                "  - **Myelemie abondante**\n"
                "  - Thrombocytose frequente, hyperuricemie"
            )),
            FicheRow(concept="Conduite a tenir", detail_md=(
                "- Eliminer syndrome inflammatoire ou infection (polynucleose neutrophile)\n"
                "- Eliminer carence martiale (thrombocytose)\n"
                "- Dosage **BCR-ABL** et recherche translocation t(9;22)\n"
                "- Myelogramme : rechercher transformation en leucemie aigue\n"
                "- Traitement par **inhibiteur de tyrosine kinase** (ITK) : guerison complete sous traitement\n"
                "- **Observance complete primordiale**"
            )),
        ]),
        SousPartie(lettre="B", titre="Polyglobulie de Vaquez", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Exces de production de GR par la moelle osseuse\n"
                "- Mutation genetique touchant la voie **JAK2**"
            )),
            FicheRow(concept="Quand evoquer", detail_md=(
                "- **Cliniquement** :\n"
                "  - **Prurit aquagenique** : declenche par le contact de l'eau\n"
                "  - Erythrose faciale, erythromelalgie\n"
                "  - Splenomegalie\n"
                "  - Cephalees, phosphenes, acouphenes (hyperviscosité)\n"
                "  - Thrombose arterielle ou veineuse\n"
                "- **Biologiquement** :\n"
                "  - Homme : Hb > **16,5 g/dL** ou Ht > 49%\n"
                "  - Femme : Hb > **16 g/dL** ou Ht > 48%\n"
                "  - Polynucleose neutrophile et thrombocytose frequentes"
            )),
            FicheRow(concept="", detail_md=(
                "- Le **prurit aquagenique** est tres evocateur de la polyglobulie de Vaquez\n"
                "- Eliminer les fausses polyglobulies : deshydratation, tabagisme, SAS, androgenotherapie, EPO, sejour en altitude"
            ), kind="piege"),
            FicheRow(concept="Prise en charge", detail_md=(
                "- Recherche de la mutation **JAK2**\n"
                "- Echographie abdominale\n"
                "- Explorations complementaires pour confirmer polyglobulie vraie\n"
                "- Traitement antiagregant plaquettaire +/- cytoreducteur si indication"
            )),
        ]),
        SousPartie(lettre="C", titre="Thrombocytemie essentielle", rows=[
            FicheRow(concept="Definition", detail_md=(
                "- Exces de production de plaquettes par la moelle osseuse\n"
                "- Mutation genetique (JAK2, CALR ou MPL)"
            )),
            FicheRow(concept="Quand evoquer", detail_md=(
                "- **Cliniquement** : erythromelalgie, thromboses veineuses ou arterielles, splenomegalie\n"
                "- **Biologiquement** : thrombocytose > **450 G/L**, hyperleucocytose a PNN frequente, myelemie possible"
            )),
            FicheRow(concept="Conduite a tenir", detail_md=(
                "- Ecarter un syndrome inflammatoire\n"
                "- Echographie abdominale\n"
                "- Recherche mutation **JAK2, CALR ou MPL**\n"
                "- Traitement antiagregant plaquettaire +/- cytoreducteur"
            )),
        ]),
    ])

    # -- PARTIE V : THROMBOPENIE ET ADENOPATHIE --
    partie_v = Partie(numero="V", titre="Thrombopenie et adenopathie", sous_parties=[
        SousPartie(lettre="A", titre="Thrombopenie", rows=[
            FicheRow(concept="Thrombopenie peripherique immunologique", detail_md=(
                "- **PTI** (purpura thrombopenique immunologique) :\n"
                "  - Maladies auto-immunes : lupus, Sjogren\n"
                "  - Hemopathies lymphoides ++ : LLC, autres lymphomes\n"
                "  - Infections : VIH, infections virales benignes (enfant ++), H. pylori\n"
                "  - **Idiopathique** : diagnostic d'elimination\n"
                "- **Thrombopenie immuno-allergique** : TIH, quinine, digoxine, sulfamides\n"
                "- **Thrombopenie allo-immune** : post-transfusionnelle, neonatale"
            )),
            FicheRow(concept="Thrombopenie peripherique non immunologique", detail_md=(
                "- **Hyper-consommation** :\n"
                "  - CIVD (septicemie, endocardite, paludisme)\n"
                "  - **MAT** : anemie hemolytique mecanique + schizocytes\n"
                "  - Prothese valvulaire mecanique, CEC\n"
                "- **Trouble de repartition** : sequestration splenique (hypersplenisme), T3 grossesse"
            )),
            FicheRow(concept="Thrombopenie centrale", detail_md=(
                "- **Acquises** : insuffisance medullaire (aplasie, hemopathies, carences vitaminiques)\n"
                "- Amegacaryocytose acquise : intoxication OH aigue, chimio antimitotiques, virus (VIH, rubeole, CMV)\n"
                "- **Constitutionnelles** (rares) : maladie de Fanconi (AR), dystrophie thrombocytaire de Bernard-Soulier (AR)"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- Signes hemorragiques uniquement si thrombopenie **profonde** ou traitement AAP/anticoagulant :\n"
                "  - **Purpura plaquettaire**\n"
                "  - Epistaxis, hematurie, menorragies, hemorragies digestives/meningees\n"
                "- Signes de gravite ++ : choc hemorragique, saignement visceral, **hemorragie cerebrale**"
            )),
            FicheRow(concept="", detail_md=(
                "- Toujours eliminer une **fausse thrombopenie** en premier : controle tube nitrate ou frottis sanguin (amas plaquettaires)\n"
                "- Si purpura febrile : penser au **purpura fulminans** !!"
            ), kind="piege"),
            FicheRow(concept="Prise en charge", detail_md=(
                "- Support transfusionnel si plaquettes < **30 G/L**\n"
                "- Prevention hemorragies : CI injections IM, biopsies percutanees, chirurgie\n"
                "- Si < 20 000/L : CI PL, ponction pleurale/pericardique, sports violents\n"
                "- Controle tensionnel\n"
                "- Contraception orale continue (amenorrhee) chez femmes en periode genitale\n"
                "- Traitement etiologique ++"
            )),
        ]),
        SousPartie(lettre="B", titre="Adenopathie superficielle", rows=[
            FicheRow(concept="Étiologies", detail_md=(
                "- **Infections** :\n"
                "  - Bacteriennes : brucellose, pasteurellose, syphilis secondaire\n"
                "  - Virales : VIH, MNI, CMV\n"
                "  - Parasitaires : toxoplasmose\n"
                "  - Mycobacteriennes : BK\n"
                "- **Cancers** : hemopathies lymphoides (lymphomes, LLC), cancers solides (testicule, poumon)\n"
                "- **Inflammatoires** : lupus, sarcoidose\n"
                "- **Medicaments** : phenitoone, allopurinol, ceftriaxone, carbamazepine"
            )),
            FicheRow(concept="Examen clinique de l'ADP", detail_md=(
                "- Diagnostic positif ADP : ganglion taille > **1 cm**\n"
                "- Caracteristiques semiologiques :\n"
                "  - Taille, consistance (molle/dure/ferme), forme, caractere douloureux\n"
                "  - Adherence aux plans superficiels et profonds\n"
                "  - Etat de la peau en regard\n"
                "- Examen de **toutes les aires ganglionnaires** + rate + amygdales\n"
                "- Consigner dans un **schema date** ++"
            )),
            FicheRow(concept="Criteres de malignite d'une ADP", detail_md=(
                "- Taille > **2 cm**\n"
                "- **Non douloureuse**, non inflammatoire\n"
                "- **Dure**\n"
                "- **Adherente** aux plans profonds\n"
                "- Chronique (> 1 mois)\n"
                "- Associee a une splenomegalie\n"
                "- Non satellite d'une porte d'entree infectieuse\n"
                "- **Ganglion de Troisier**"
            )),
            FicheRow(concept="", detail_md=(
                "- Pas de **ponction a l'aiguille** pour les ADP !\n"
                "- Biopsie ganglionnaire avec analyse bacteriologique, mycobacteriologique, parasitologique et anatomopathologique avec immunohistochimie"
            ), kind="a_retenir"),
            FicheRow(concept="Territoires de drainage", detail_md=(
                "| Aire ganglionnaire | Territoire de drainage |\n"
                "|-------------------|------------------------|\n"
                "| Preauriculaires | Ophtalmique, oreille, cuir chevelu |\n"
                "| Sous-mentonniers/maxillaires | Bouche, langue |\n"
                "| Jugulocarotidiens | ORL, thyroide |\n"
                "| **Sus-claviculaires** | Organes sous-diaphragmatiques, pelvis, testicules, sein, poumon |\n"
                "| Axillaires | Seins, membres superieurs |\n"
                "| Epitrochleens | Avant-bras |\n"
                "| Inguinaux | Marge anale, organes genitaux, membres inferieurs |\n"
            )),
        ]),
        SousPartie(lettre="C", titre="Splenomegalie", rows=[
            FicheRow(concept="Généralités", detail_md=(
                "- Fonctions de la rate :\n"
                "  - Pulpe rouge : hematopoiese foeto-embryonnaire, stockage plaquettaire et leucocytaire\n"
                "  - Pulpe blanche : defense immunitaire (**bacteries encapsulees** ++)\n"
                "- **Toute rate palpable cliniquement est pathologique** !"
            )),
            FicheRow(concept="Étiologies", detail_md=(
                "- **HTP** : cirrhose, thrombose portale\n"
                "- **Infections** : endocardites, abces spleniques, paludisme\n"
                "- **Maladies dysimmunitaires** : lupus, sarcoidose\n"
                "- **Infiltration tumorale** : lymphomes, LAL\n"
                "- **Stimulation pulpe rouge** : myelofibrose, thalassemies\n"
                "- **Maladies de surcharge** : Gaucher, amylose"
            )),
            FicheRow(concept="Tableau clinico-biologique", detail_md=(
                "- Douleur HCG, satiete precoce\n"
                "- Rate palpable (debord costal gauche)\n"
                "- **Hypersplenisme** : cytopenies moderees de sequestration (anemie, thrombopenie, leucopenie)\n"
                "- Echographie abdominale si doute diagnostique"
            )),
        ]),
    ])

    # -- PARTIE VI : ANTICOAGULANTS, TRANSFUSION ET DIVERS --
    partie_vi = Partie(numero="VI", titre="Anticoagulants, transfusion et divers", sous_parties=[
        SousPartie(lettre="A", titre="Prescription et surveillance des anticoagulants", rows=[
            FicheRow(concept="Heparines", detail_md=(
                "- Formes : **HNF** (Calciparine) et **HBPM** (Tinzaparine)\n"
                "- **Prophylaxie TVP** : patients > 40 ans hospitalises > 3 jours (decompensation cardiaque/respiratoire, "
                "infection severe, affection rhumatologique inflammatoire) + FDR thromboembolique (age > 75 ans, cancer, ATCD MTEV)\n"
                "  - Lovenox 0,4 mL/j SC\n"
                "- **Traitement curatif** :\n"
                "  - HBPM : Tinzaparine 175 UI/kg/j SC en 1 injection\n"
                "  - HNF : perfusion continue 500 UI/kg/24h"
            )),
            FicheRow(concept="AVK", detail_md=(
                "- Mecanisme : interferent avec le cycle de la vitamine K hepatique\n"
                "- Empechent la transcription en forme active de **4 facteurs** (II, VII, IX, X) et **2 inhibiteurs** (proteines C et S)\n"
                "- Surveillance par **INR**\n"
                "- CI absolues : hypersensibilite, insuffisance hepatique severe, allaitement (indanediones), "
                "grossesse (autorise seulement T2 si heparine impossible)"
            )),
            FicheRow(concept="Cibles INR selon indication", detail_md=(
                "| Pathologie | INR cible |\n"
                "|-----------|----------|\n"
                "| TVP, EP | **2-3** |\n"
                "| FA avec FDR thromboembolique | **2-3** |\n"
                "| IDM complique thrombus mural | **2-3** |\n"
                "| Valvulopathie mitrale | **3-4,5** |\n"
                "| Prothese valvulaire mecanique | **2,5-4,5** |\n"
            )),
            FicheRow(concept="Surveillance AVK", detail_md=(
                "- 1er controle INR a **J2** (detecter hypersensibilite)\n"
                "- Modifier dose par paliers de **25%**, verifier INR 3-5 jours apres chaque modification\n"
                "- Dose d'equilibre : minimum **1 semaine** avec INR/3 jours\n"
                "- Puis controles espaces /15 jours, puis au moins **1/mois**\n"
                "- Carnet de surveillance pour le patient\n"
                "- Arret heparinotherapie apres **2 INR en zone therapeutique**"
            )),
            FicheRow(concept="", detail_md=(
                "- Lors de toute introduction d'un **nouveau medicament** sous AVK : dosage INR dans les 48-72h\n"
                "- Les interactions medicamenteuses sont tres frequentes avec les AVK"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Accidents des anticoagulants", rows=[
            FicheRow(concept="Surdosage AVK asymptomatique", detail_md=(
                "- FDR hemorragique des **INR > 4**\n"
                "- CAT : orientation ambulatoire si possible\n"
                "- Information du patient : risque hemorragique a court terme, signes d'alerte (saignement, tout nouveau symptome)"
            )),
            FicheRow(concept="Hemorragie sous AVK", detail_md=(
                "- **Non grave** : CAT identique aux surdosages, hemostase locale\n"
                "- **Grave** (defaillance hemodynamique ou consequence fonctionnelle) : hospitalisation en urgence\n"
                "- Ne pas oublier : controle bilan hemostase, rechercher cause du surdosage (education therapeutique, interactions)"
            )),
            FicheRow(concept="Saignements sous heparine", detail_md=(
                "- Risque : HNF > HBPM, augmente par insuffisance renale\n"
                "- Antidote : **sulfate de protamine** (risque bradycardie, hypotension)\n"
                "- Fondaparinux : **aucun antidote**"
            )),
            FicheRow(concept="★ Thrombopenie induite par heparine (TIH)", detail_md=(
                "- **Type II** ++\n"
                "- Survenue entre **J5 et J21** du traitement par heparine\n"
                "- **Thromboses arterielles et veineuses**\n"
                "- Diagnostic : mise en evidence **Ac anti-PF4** en ELISA et/ou tests fonctionnels\n"
                "- CAT :\n"
                "  - **Arret immediat et definitif** de l'heparine\n"
                "  - Anti-thrombotique de substitution : **danaparoide de sodium**\n"
                "  - Surveillance clinique et biologique (NFS, efficacite)"
            )),
            FicheRow(concept="", detail_md=(
                "- A evoquer devant **toute thrombopenie ou thrombose** apres introduction de l'heparine\n"
                "- L'arret de l'heparine doit etre **immediat et definitif**"
            ), kind="a_retenir"),
            FicheRow(concept="AOD", detail_md=(
                "- Molecules : **dabigatran**, **rivaroxaban**, **apixaban**\n"
                "- Risque hemorragique present\n"
                "- Aucun antidote specifique disponible (possibilite de dialyse pour dabigatran)"
            )),
        ]),
        SousPartie(lettre="C", titre="Transfusion sanguine et produits derives du sang", rows=[
            FicheRow(concept="CGR", detail_md=(
                "- Indication : anemie, sur la **tolerance clinique** ++ (et non sur le chiffre d'Hb)\n"
                "- Deux determinations du **groupe ABO**\n"
                "- Recherche d'agglutinines irregulieres (**RAI**)\n"
                "- Phenotypage erythrocytaire (etendu chez la femme jeune ou transfusions frequentes)"
            )),
            FicheRow(concept="Concentres plaquettaires", detail_md=(
                "- Conservation 5 jours max entre 20-24 C\n"
                "- Posologie : 1 unite pour 7-10 kg\n"
                "- Deleucocytation systematique, compatibilite ABO ++\n"
                "- Indications : thrombopenie centrale < 20 000/mm3, syndrome hemorragique, < 50 000 si geste invasif"
            )),
            FicheRow(concept="Plasma", detail_md=(
                "- Indications : coagulopathies de consommation graves, hemorragies aigues avec deficit global facteurs, deficit facteur coagulation, MAT"
            )),
            FicheRow(concept="Hemolyse intra-vasculaire aigue (incompatibilite ABO)", detail_md=(
                "- Debut **brutal** des le debut de la transfusion\n"
                "- Tableau de **choc** : frissons, sueurs, malaise, douleurs lombaires ++\n"
                "- CAT :\n"
                "  - **Arret immediat** de la transfusion\n"
                "  - Traitement du choc +/- CIVD\n"
                "  - Verification identite + groupe + carton de controle ultime\n"
                "  - Prelevements : verification groupage, Coombs direct, RAI\n"
                "  - **Declaration d'accident transfusionnel**"
            )),
            FicheRow(concept="Autres complications immunologiques", detail_md=(
                "- **Hemolyse retardee** : ictere J5-J7, liee a un Ac irregulier indetectable avant transfusion\n"
                "- **Syndrome frissons-hyperthermie** : allo-immunisation anti-HLA\n"
                "- **Reactions allergiques/anaphylactiques** : Ac anti-IgA chez sujets deficitaires\n"
                "- **Purpura thrombopenie post-transfusionnel** aigu : allo-immunisation anti-HPA-1a, J7"
            )),
            FicheRow(concept="Complications infectieuses et autres", detail_md=(
                "- **Choc endotoxinique** (< 1/10 000) : contamination bacterienne du produit\n"
                "- Transmission virale (VIH, VHB, VHC) : tres rare\n"
                "- **OAP hemodynamique** : transfusions massives, cardiopathie sous-jacente\n"
                "- **TRALI** : OAP lesionnel dans les 6h post-transfusion\n"
                "- Surcharge citratee : hypocalcemie\n"
                "- Hyperkaliemie (transfusions massives CGR)\n"
                "- **Hemochromatose post-transfusionnelle** : polytransfuses au long cours, prevention par chelateurs du fer"
            )),
            FicheRow(concept="", detail_md=(
                "- CAT si intolerance : arret transfusion, garder voie d'abord, appel medecin, HC sur poche, "
                "test de Beth-Vincent, envoi poche a l'EFS, **declaration HV**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Hypereosinophilie et syndrome mononucleosique", rows=[
            FicheRow(concept="Hypereosinophilie", detail_md=(
                "- Diagnostic positif : PNE > **500/mm3**\n"
                "- Retentissement visceral si PNE > 1 G/L\n"
                "- **HE secondaire** (la plus frequente) :\n"
                "  - Atopie (eczema, asthme, urticaire)\n"
                "  - Infection parasitaire : **helminthiases** ++\n"
                "  - Hemopathies : lymphomes T, lymphome de Hodgkin\n"
                "  - Iatrogenie : **DRESS syndrome**\n"
                "  - Maladies de systeme : lupus, colites inflammatoires\n"
                "- **HE primitive** (rare) : SMP a eosinophiles\n"
                "- Complications si HE importante : **fibrose endomyocardique** +++, infiltrats radiologiques, atteintes cutanees, HSM"
            )),
            FicheRow(concept="Syndrome mononucleosique", detail_md=(
                "- Definition : **hyperlymphocytose polymorphe benigne** frequente\n"
                "- Hemogramme : hyperleucocytose moderee jusqu'a 30 G/L\n"
                "- Frottis : lymphocytes de grande taille, hyperactives\n"
                "- **Étiologies de 1ere intention** :\n"
                "  - **Primo-infection EBV** : syndrome pseudo-grippal, ADP, angine erythemateuse (MNI test)\n"
                "  - **CMV** : fievre, HSM, atteinte viscerale (hepatite, colite, chorioretinite)\n"
                "  - **Toxoplasmose** : zoonose parasitaire, souvent asymptomatique, fievre + ADP\n"
                "  - **VIH**\n"
                "- Étiologies de 2e intention : coqueluche, hepatites virales, syphilis, listeriose"
            )),
        ]),
    ])

    # -- TABLEAUX DE SYNTHESE --
    tableaux = [
        TableauSynthese(titre="Anemies microcytaires : diagnostic differentiel", markdown=(
            "| Critere | Carence martiale | Inflammation | Thalassemie |\n"
            "|---------|-----------------|--------------|-------------|\n"
            "| Fer serique | Diminue | Diminue | Normal |\n"
            "| CST | Diminue | Normal | Normal |\n"
            "| Ferritine | Diminuee | N ou augmentee | N ou augmentee |\n"
            "| Thrombocytose | Oui | Non | Non |\n"
            "| Electrophorese Hb | Normale | Normale | Anormale |\n"
            "| Hemolyse | Non | Non | Oui |\n"
        )),
        TableauSynthese(titre="Orientation diagnostique des anemies selon VGM et reticulocytes", markdown=(
            "| VGM | Reticulocytes | Orientation |\n"
            "|-----|--------------|-------------|\n"
            "| < 80 fL | Non doses | Carence martiale, inflammation, thalassemie |\n"
            "| > 80 fL | > 150 G/L | Hemorragie, hemolyse, regeneration medullaire |\n"
            "| > 80 fL | < 150 G/L | Insuffisance renale/hepatique/thyroidienne, myelogramme |\n"
            "| > 120 fL | < 150 G/L | Carence B9/B12, SMD |\n"
        )),
        TableauSynthese(titre="Myelome : criteres CRAB et SLIM", markdown=(
            "| Critere CRAB | Definition |\n"
            "|-------------|------------|\n"
            "| C = Calcemie | > 2,75 mmol/L |\n"
            "| R = Renal | Creatinine > 177 umol/L ou DFG < 40 mL/min |\n"
            "| A = Anemie | Hb < 10 g/dL |\n"
            "| B = Bone | Lesions osseuses lytiques |\n\n"
            "| Critere SLIM | Definition |\n"
            "|-------------|------------|\n"
            "| Sixty percent | 60% plasmocytes medullaires |\n"
            "| Light chain | Ratio CLL > 100 (CLL en exces > 100 mg/L) |\n"
            "| MRI | > 1 lesion focale a l'IRM |\n"
        )),
        TableauSynthese(titre="Syndromes myeloproliferatifs : comparaison", markdown=(
            "| Critere | LMC | Vaquez | TE |\n"
            "|---------|-----|--------|----|\n"
            "| Mutation | BCR-ABL | JAK2 | JAK2/CALR/MPL |\n"
            "| Lignee predominante | PNN | GR | Plaquettes |\n"
            "| Signe clinique cle | Splenomegalie | Prurit aquagenique | Erythromelalgie |\n"
            "| Bio cle | Hyperleucocytose > 50 G/L | Polyglobulie | Thrombocytose > 450 G/L |\n"
            "| Traitement | ITK | Antiagregant +/- cytoreducteur | Antiagregant +/- cytoreducteur |\n"
        )),
        TableauSynthese(titre="Cibles INR des AVK", markdown=(
            "| Indication | INR cible |\n"
            "|-----------|----------|\n"
            "| TVP, EP | 2-3 |\n"
            "| FA + FDR | 2-3 |\n"
            "| IDM + thrombus mural | 2-3 |\n"
            "| Valvulopathie mitrale | 3-4,5 |\n"
            "| Prothese mecanique | 2,5-4,5 |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-cles", markdown=(
        "| Parametre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Hb homme | < **13** g/dL | Definition anemie |\n"
        "| Hb femme | < **12** g/dL | Definition anemie |\n"
        "| Hb femme enceinte | < **10,5** g/dL | > 2e trimestre |\n"
        "| VGM microcytaire | < **80** fL | Carence, inflammation, thalassemie |\n"
        "| Reticulocytes regeneratifs | > **150** G/L | Anemie regenerative |\n"
        "| VGM megaloblastique | > **120** fL | Carence B9/B12 |\n"
        "| Plasmocytes myelome | > **10%** | Myelogramme |\n"
        "| Blastes leucemie aigue | > **20%** | Myelogramme |\n"
        "| Lymphocytes LLC | > **5000**/mm3 | Persistant > 3 mois |\n"
        "| Hb Vaquez (H) | > **16,5** g/dL | Polyglobulie |\n"
        "| Plaquettes TE | > **450** G/L | Thrombocytemie essentielle |\n"
        "| Leucocytes LMC | > **50** G/L | Hyperleucocytose |\n"
        "| Ferritine chelation | > **1000** ug/L | Indication chelateur fer |\n"
        "| PNE hypereosinophilie | > **500**/mm3 | Diagnostic positif |\n"
        "| B2-microglobuline ISS III | > **5,5** mg/L | Mauvais pronostic myelome |\n"
        "| INR cible TVP/EP | **2-3** | Sous AVK |\n"
        "| TIH : delai survenue | **J5-J21** | Thrombopenie induite heparine |\n"
    ))

    points_cles = [
        "L'anemie est definie par la diminution de l'Hb : < 13 g/dL (homme), < 12 g/dL (femme), < 10,5 g/dL (femme enceinte)",
        "Le dosage des reticulocytes n'est indique que si l'anemie est normo ou macrocytaire (jamais si microcytaire)",
        "Les 3 causes d'anemie microcytaire : **carence martiale** (CST diminue), **inflammation** (CST normal), **thalassemie** (electrophorese Hb anormale)",
        "Si carence B12 et folates associees : traiter d'abord la **B12** (risque neurologique)",
        "Myelome : criteres **CRAB** pour l'indication therapeutique, score **ISS** pour le pronostic",
        "LLC : hyperlymphocytose > 5000/mm3 persistant > 3 mois, score de **Matutes** > 3, ombres de **Gumprecht**",
        "LMC : translocation **BCR-ABL** t(9;22), traitement par **ITK**",
        "TIH type II : arret **immediat et definitif** de l'heparine, substitution par danaparoide",
        "Transfusion : la decision repose sur la **tolerance clinique** et non sur le chiffre d'Hb",
        "Toute rate palpable est **pathologique** ; les criteres de malignite d'une ADP incluent taille > 2 cm, dure, adherente, chronique > 1 mois",
    ]

    fiche_eclair_md = (
        "**Anemie microcytaire** (VGM < 80 fL) : 3 causes = carence martiale (fer/CST bas, "
        "thrombocytose), inflammation (fer bas, CST normal), thalassemie (electrophorese Hb). "
        "Carence martiale : sels ferreux 4 mois, crise reticulocytaire J10.\n\n"
        "**Anemie regenerative** (reticulocytes > 150 G/L) : eliminer hemorragie, "
        "puis bilan hemolyse (haptoglobine effondree). Corpusculaire (Minkowski-Chauffard, "
        "drepanocytose, G6PD) vs extra-corpusculaire (AHAI, MAT, paludisme).\n\n"
        "**Anemie aregenerative** : myelogramme systematique. Moelle pauvre = aplasie. "
        "Moelle riche = envahissement ou carence B9/B12. Biermer : Ac anti-FI, "
        "B12 IM a vie, fibroscopie/3 ans.\n\n"
        "**Hemopathies** : LA > 20% blastes. LLC > 5000 lymphocytes/mm3, Matutes > 3. "
        "Myelome : plasmocytes > 10%, pic Ig monoclonal, CRAB. LNH : biopsie exerese, "
        "R-CHOP si CD20+. Hodgkin : Reed-Sternberg, prurit.\n\n"
        "**SMP** : LMC = BCR-ABL + ITK. Vaquez = JAK2, prurit aquagenique. "
        "TE = plaquettes > 450 G/L, JAK2/CALR/MPL.\n\n"
        "**Thrombopenie** : eliminer fausse thrombopenie. PTI = elimination. "
        "TIH = arret heparine + danaparoide.\n\n"
        "**Anticoagulants** : INR cible 2-3 (TVP/EP/FA), 3-4,5 (valvulopathie mitrale). "
        "1er INR a J2. TIH entre J5-J21.\n\n"
        "**Transfusion** : indication sur tolerance clinique. Incompatibilite ABO = arret + choc. "
        "TRALI = OAP lesionnel < 6h. Hemochromatose si polytransfuse."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Hematologie",
        annee="2025-2026",
        item="Items 208, 209, 210, 212, 213, 215, 216, 272, 312, 315, 316, 317, 325, 326",
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

    fiche = build_hematologie_fiche()

    docx_path = output_dir / "Medecine_generale_Hematologie_2025-2026.docx"
    print(f"Generating DOCX: {docx_path}")
    render_docx(fiche, docx_path, LOGO_PATH)
    print(f"DOCX generated: {docx_path}")

    try:
        from major_ecn.pdf_generator import render_pdf
        pdf_path = output_dir / "Medecine_generale_Hematologie_2025-2026.pdf"
        print(f"Generating PDF: {pdf_path}")
        render_pdf(fiche, pdf_path)
        print(f"PDF generated: {pdf_path}")
    except Exception as e:
        print(f"PDF generation skipped: {e}")


if __name__ == "__main__":
    main()

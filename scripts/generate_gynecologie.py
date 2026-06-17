"""Génère la fiche Gynécologie."""
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
        PlanPartie(numero="I", titre="Aménorrhée", sous_parties=[
            PlanSousPartie(lettre="A", titre="Aménorrhée primaire"),
            PlanSousPartie(lettre="B", titre="Aménorrhée secondaire"),
        ]),
        PlanPartie(numero="II", titre="Contraception", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et première prescription"),
            PlanSousPartie(lettre="B", titre="Contraception oestroprogestative"),
            PlanSousPartie(lettre="C", titre="Contraception progestative et autres méthodes"),
            PlanSousPartie(lettre="D", titre="DIU et contraception d'urgence"),
            PlanSousPartie(lettre="E", titre="Situations cliniques particulières et stérilisation"),
        ]),
        PlanPartie(numero="III", titre="Grossesse extra-utérine", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et facteurs de risque"),
            PlanSousPartie(lettre="B", titre="Tableau clinique et examens complémentaires"),
            PlanSousPartie(lettre="C", titre="Prise en charge"),
        ]),
        PlanPartie(numero="IV", titre="Grossesse normale", sous_parties=[
            PlanSousPartie(lettre="A", titre="Modifications physiologiques"),
            PlanSousPartie(lettre="B", titre="Datation et suivi de grossesse"),
            PlanSousPartie(lettre="C", titre="Consultations du 2e et 3e trimestre"),
        ]),
        PlanPartie(numero="V", titre="Hémorragies génitales de la femme", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définitions et classification"),
            PlanSousPartie(lettre="B", titre="Métrorragies et ménorragies"),
            PlanSousPartie(lettre="C", titre="Étiologies selon la période de vie"),
        ]),
        PlanPartie(numero="VI", titre="Infections génitales hautes", sous_parties=[
            PlanSousPartie(lettre="A", titre="Généralités et tableau clinique"),
            PlanSousPartie(lettre="B", titre="Complications et prise en charge"),
        ]),
        PlanPartie(numero="VII", titre="Leucorrhées et ménopause", sous_parties=[
            PlanSousPartie(lettre="A", titre="Leucorrhées"),
            PlanSousPartie(lettre="B", titre="Ménopause et traitement hormonal"),
        ]),
    ]

    # ── PARTIE I : AMÉNORRHÉE ──
    partie_i = Partie(numero="I", titre="Aménorrhée", sous_parties=[
        SousPartie(lettre="A", titre="Aménorrhée primaire", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **Aménorrhée primaire** : absence de ménarche chez jeune fille > **16 ans**\n"
                "- En France : âge moyen de la ménarche = **12,5 ans**"
            )),
            FicheRow(concept="Démarche diagnostique", detail_md=(
                "- **Interrogatoire** : âge, ATCD personnels/familiaux, âge puberté mère/sœurs, "
                "traitements (neuroleptiques, corticoïdes, RT, CT), mode de vie (alimentation, sport, "
                "contexte psychologique)\n"
                "- **Signes fonctionnels** : anosmie, céphalées/troubles visuels, galactorrhée, "
                "douleurs pelviennes cycliques\n"
                "- **Examen clinique** :\n"
                "  - Poids, taille, IMC, courbe de croissance\n"
                "  - Recherche dysmorphie (syndrome de **Turner**)\n"
                "  - Stade pubertaire de **Tanner**\n"
                "  - Signes d'hyperandrogénie (hirsutisme, acné)\n"
                "  - Examen gynécologique : inspection OGE, spéculum de vierge, pas de TV si vierge, +/- TR"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- Si absence de caractères sexuels secondaires : **âge osseux** (RX main/poignet gauche, "
                "os sésamoïde du pouce)\n"
                "- Si présence CSS : courbe de **température**\n"
                "- **Échographie pelvienne** : visualisation et mesures utérus/ovaires\n"
                "- **Dosages hormonaux** : FSH, LH, œstradiolémie, prolactinémie\n"
                "- **HCG** au moindre doute\n"
                "- Selon orientation : tests olfactifs, testostérone, 17-OHP, SDHEA, IRM hypophysaire, "
                "caryotype sanguin"
            )),
            FicheRow(concept="Étiologies sans CSS", detail_md=(
                "| Sésamoïde pouce | Diagnostic | Bilan |\n"
                "|-----------------|-----------|-------|\n"
                "| **Absent** | Retard pubertaire simple | Âge osseux < âge chronologique |\n"
                "| **Présent** + FSH/LH élevées | **Hypogonadisme hypergonadotrope** | Turner, dysgénésies, "
                "causes acquises (CT/RT, auto-immune) |\n"
                "| **Présent** + FSH/LH basses | **Hypogonadisme hypogonadotrope** | Tumeurs HTHP, anorexie, "
                "sport intensif, **Kallmann-De-Morsier** |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Le **syndrome de Kallmann-De-Morsier** associe hypogonadisme hypogonadotrope + **anosmie** "
                "(anomalie de migration des neurones à GnRH de la placode olfactive)"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Étiologies avec CSS normaux", detail_md=(
                "- **Anomalies utéro-vaginales** (courbe T biphasique = cause anatomique) :\n"
                "  - **Imperforation hymen** : douleurs cycliques, bombement hymen, hématocolpos → "
                "traitement chirurgical (incision radiaire)\n"
                "  - **Cloison vaginale transversale** : vagin court, col non visible → exérèse chirurgicale\n"
                "  - **Aplasie vaginale** : vagin absent mais OGI présents → création cavité vaginale\n"
                "  - **Syndrome de Rokitansky-Küster-Hauser** : aplasie vaginale + utérine +/- aplasie/ectopie "
                "rénale unilatérale, trompes et ovaires normaux\n"
                "- **Tuberculose génitale prépubertaire** : synéchies en feuille de trèfle à l'hystéroscopie\n"
                "- **Causes hormonales** (courbe T monophasique) : insensibilité aux androgènes, "
                "hyperprolactinémie, tumeurs HTHP, craniopharyngiome"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Devant une aménorrhée primaire avec CSS normaux, toujours penser aux **causes "
                "anatomiques** (imperforation hymen, Rokitansky) avant les causes hormonales"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Aménorrhée secondaire", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- Absence de règles > **3 mois** chez femme antérieurement réglée\n"
                "- Beaucoup plus **fréquente** que l'aménorrhée primaire"
            )),
            FicheRow(concept="Démarche diagnostique", detail_md=(
                "- **Interrogatoire** : ATCD familiaux (insuffisance ovarienne précoce), âge premières règles, "
                "prise médicamenteuse, mode de vie (régime carencé, sport, choc psycho-affectif), mode de "
                "contraception\n"
                "- **Examen clinique** : poids/taille/IMC/TA, examen gynécologique complet, recherche "
                "galactorrhée, signes d'hyperandrogénie, examen ophtalmologique (hémianopsie bitemporale)"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- **HCG plasmatiques** +++ (1re intention systématique)\n"
                "- **Courbe de température** : biphasique (ovulation = cause utérine) vs monophasique "
                "(anovulation = cause ovarienne/HTHP)\n"
                "- **Test aux progestatifs** (didrogestérone 10j) :\n"
                "  - **Positif** (hémorragie de privation) = sécrétion œstrogénique suffisante\n"
                "  - **Négatif** = carence œstrogénique ou anomalie de l'endomètre\n"
                "- **Bilan hormonal** : FSH, LH, œstradiolémie, prolactinémie\n"
                "- Si hyperandrogénie : testostérone totale, SDHEA, 17-OHP\n"
                "- **Échographie pelvienne** si cause basse évoquée\n"
                "- **IRM HTHP** si FSH normal/bas ou hyperprolactinémie"
            )),
            FicheRow(concept="", detail_md=(
                "- Devant toute aménorrhée secondaire, le **1er réflexe** est le dosage **HCG plasmatique** "
                "pour éliminer une grossesse"
            ), kind="a_retenir"),
            FicheRow(concept="◆ Causes utérines", detail_md=(
                "- **Synéchie utérine** : accolement parois utérines, favorisée par gestes endo-utérins "
                "traumatiques ou tuberculose → traitement par hystéroscopie opératoire\n"
                "- **Sténose cicatricielle du col** : secondaire à geste traumatique, douleurs cycliques "
                "par hématométrie → dilatation cervicale chirurgicale\n"
                "- **Iatrogène** : contraception progestative seule"
            )),
            FicheRow(concept="Insuffisance ovarienne précoce", detail_md=(
                "- ATCD familiaux de ménopause précoce\n"
                "- Signes de carence œstrogénique\n"
                "- Courbe thermique monophasique\n"
                "- **Hypogonadisme hypergonadotrope** : FSH très élevée (2 dosages), œstradiol bas\n"
                "- Échographie : atrophie endomètre, diminution/absence follicules antraux"
            )),
            FicheRow(concept="◆ Causes centrales", detail_md=(
                "- **Hypophysaires** : hyperprolactinémie, tumeurs, syndrome de **Sheehan** "
                "(nécrose hypophysaire du post-partum), hypophysite auto-immune\n"
                "- **Hypothalamiques** : aménorrhée post-pilule, aménorrhée psychogène, sportives "
                "de haut niveau, **anorexie mentale**, hypothyroïdie sévère, Cushing, Addison"
            )),
        ]),
    ])

    # ── PARTIE II : CONTRACEPTION ──
    partie_ii = Partie(numero="II", titre="Contraception", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et première prescription", rows=[
            FicheRow(concept="Épidémiologie", detail_md=(
                "- Accès anonyme et gratuit pour les mineurs, sans autorisation parentale\n"
                "- Sur 1 000 000 grossesses/an : **330 000 non désirées**\n"
                "- 2/3 des grossesses non prévues surviennent malgré prise de contraception "
                "(mauvaise utilisation)\n"
                "- Efficacité mesurée par l'**indice de Pearl** : nombre de grossesses pour "
                "100 années-femme (plus l'indice est bas, plus c'est efficace)"
            )),
            FicheRow(concept="Première prescription", detail_md=(
                "- Consultation spécifique dédiée : contraception + prévention IST\n"
                "- Si adolescente : la recevoir **sans les parents**\n"
                "- Prescription adaptée : recommandations ANSM, FDR thromboembolique, "
                "capacité d'observance, conditions socio-économiques\n"
                "- Vérification statut vaccinal **HPV** +/- rattrapage\n"
                "- Pas de partenaire stable : conseiller protection IST\n"
                "- Proposer **bilan de dépistage IST** (patiente + partenaire)"
            )),
        ]),
        SousPartie(lettre="B", titre="Contraception oestroprogestative", rows=[
            FicheRow(concept="Pilule oestroprogestative (POP)", detail_md=(
                "- **1re intention** chez femme jeune nullipare (IP **0,3%**)\n"
                "- Composition : éthinylestradiol (EE) + progestatif de synthèse\n"
                "- **Mécanisme principal** : inhibition sécrétion FSH/LH → blocage ovulation "
                "par rétrocontrôle négatif HTHP\n"
                "- **Actions périphériques** : atrophie endométriale, coagulation glaire cervicale, "
                "inhibition croissance folliculaire"
            )),
            FicheRow(concept="◆ Générations de progestatifs", detail_md=(
                "| Génération | Progestatif | Particularité |\n"
                "|-----------|------------|---------------|\n"
                "| 1re | — | Mal tolérée, effets androgéniques |\n"
                "| **2e** | **Lévonorgestrel/norgestrel** | **1re intention** |\n"
                "| 3e | Désogestrel, gestodène, norgestimate | Sur-risque thrombotique |\n"
                "| 4e | Drospirénone, diénogest | — |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- Toujours prescrire en **1re intention** une POP de **2e génération** "
                "(ex : Leeloo/Lovavulo au lévonorgestrel)"
            ), kind="a_retenir"),
            FicheRow(concept="Contre-indications absolues POP", detail_md=(
                "- **MTEV** : ATCD TVP-EP, chirurgie majeure, thrombophilie héréditaire "
                "(mutation facteur V Leiden, déficit protéine C/S)\n"
                "- **FDR CV** : HTA sévère, tabac ≥ 15 cig/j après 35 ans, ATCD IDM-AVC, "
                "valvulopathies sévères, **migraine avec aura**, diabète compliqué ou > 20 ans\n"
                "- **Néoplasies** : cancer sein/endomètre (confirmé ou suspecté)\n"
                "- Hépatite virale active, affection hépatique sévère, tumeur bénigne hépatique\n"
                "- Grossesse, allaitement < 6S post-partum, dyslipidémie sévère, lupus\n"
                "- ATCD de diabète gestationnel, pré-éclampsie/HTAG, ictère cholestatique"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ La **migraine avec aura** est une CI **absolue** aux oestroprogestatifs "
                "(risque AVC)\n"
                "- ⚠ Le risque thromboembolique veineux est **maximal la 1re année** de prise"
            ), kind="piege"),
            FicheRow(concept="◆ Effets secondaires POP", detail_md=(
                "- Hypercoagulabilité avec risque TE artériel et veineux "
                "(**x3** par rapport population générale, soit 5-12/10 000)\n"
                "- Risque TE veineux : maximal la 1re année, diminue avec réduction dose EE, "
                "moindre avec lévonorgestrel\n"
                "- Augmentation risque cancer sein et col utérus\n"
                "- Modifications métabolisme lipidique : augmentation TG et HDL-CT, baisse LDL-CT\n"
                "- HTA, spottings"
            )),
            FicheRow(concept="Modalités de prescription", detail_md=(
                "- Interrogatoire : CI, âge, ATCD gynéco-obstétricaux, statut vaccinal HPV\n"
                "- Examen clinique : **poids, IMC, TA++**, examen membres inférieurs (capital veineux)\n"
                "- **Pas d'examen gynécologique** lors de la 1re prescription chez femme jeune\n"
                "- **Pas de bilan sanguin** nécessaire si pas d'ATCD particuliers\n"
                "- Si ATCD : bilan thrombophilie (protéine C/S, facteur V Leiden, facteur II, "
                "antithrombine)\n"
                "- Information orale et écrite sur risque de **thrombose** artérielle et veineuse"
            )),
            FicheRow(concept="Surveillance", detail_md=(
                "- Dans les **3 mois** : EAL, glycémie à jeun\n"
                "- **Visite annuelle** : tolérance, observance, tabagisme, poids, TA, palpation foie, "
                "examen gynécologique et seins\n"
                "- Hors signe d'appel : bilan tous les **5 ans**"
            )),
            FicheRow(concept="Autres voies OP", detail_md=(
                "- **Patch contraceptif** : délivrance transdermique EE + progestatif 3e gén, "
                "1 patch/semaine × 3 sem + 1 sem de pause. Sur-risque thrombose **x2** vs POP. "
                "Non remboursé. 2e intention\n"
                "- **Anneau vaginal** : anneau souple in situ 3 sem + 1 sem de retrait. "
                "Bonne tolérance (pas de 1er passage hépatique). Non remboursé"
            )),
        ]),
        SousPartie(lettre="C", titre="Contraception progestative et autres méthodes", rows=[
            FicheRow(concept="Micro-progestatifs", detail_md=(
                "- **2e intention** si CI aux OP (ou 1re intention si désir d'aménorrhée)\n"
                "- **Mécanisme principal** : périphérique (modification glaire cervicale, "
                "atrophie endométriale, modification mobilité tubaire)\n"
                "- CI : cancer sein/endomètre, hépatopathie sévère, accident TE évolutif, "
                "inducteurs enzymatiques associés\n"
                "- EI : troubles du cycle (métrorragies, spotting, aménorrhée), kystes fonctionnels"
            )),
            FicheRow(concept="◆ Micropilules progestatives", detail_md=(
                "| Pilule | Composition | IP | Tolérance oubli | CPAM |\n"
                "|--------|------------|-----|-----------------|------|\n"
                "| Microval | 30 µg lévonorgestrel | 1% | **3h** | Remboursée |\n"
                "| Cerazette | 75 µg désogestrel | 0,52% | **12h** | Non remboursée |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Pour **Microval**, la tolérance à l'oubli n'est que de **3 heures** "
                "(vs 12h pour Cerazette et 12h pour les OP)"
            ), kind="piege"),
            FicheRow(concept="Implant sous-cutané (Nexplanon)", detail_md=(
                "- Bâtonnet délivrant en continu de l'étonogestrel, inséré en SC face interne "
                "bras non dominant sous AL\n"
                "- Efficace **3 ans** (IP **0,05%**)\n"
                "- CI et EI identiques aux micro-progestatifs"
            )),
            FicheRow(concept="Contraception locale", detail_md=(
                "- **Préservatif masculin** (IP 2%) : seule méthode protégeant contre les IST\n"
                "- Préservatif féminin, diaphragme/capes (IP 6%)\n"
                "- Spermicides (IP 18%) : ovules/crèmes placées au fond du vagin, efficaces 8h"
            )),
            FicheRow(concept="Méthodes naturelles (IP 1-9%)", detail_md=(
                "- Retrait, courbe de température, méthode **Ogino-Knaus**\n"
                "- Méthode de **Billings** (glaire cervicale)\n"
                "- Tests d'ovulation\n"
                "- Méthode **MAMA** (allaitement maternel et aménorrhée)"
            )),
        ]),
        SousPartie(lettre="D", titre="DIU et contraception d'urgence", rows=[
            FicheRow(concept="DIU — Généralités", detail_md=(
                "- Méthode contraceptive de **1re intention**\n"
                "- Efficace longue durée (**5-10 ans**)\n"
                "- Pose dans conditions d'asepsie rigoureuses, après hystérométrie, "
                "pendant les règles (dans les 7 jours suivant leur début)"
            )),
            FicheRow(concept="DIU : cuivre vs progestérone", detail_md=(
                "| Critère | DIU au cuivre | DIU à la progestérone |\n"
                "|---------|-------------|---------------------|\n"
                "| Mécanisme | Toxicité directe cuivre sur SPZ | Modification glaire + atrophie endomètre |\n"
                "| IP | **0,6%** | **0,1%** |\n"
                "| EI principaux | **Ménorragies**, anémie ferriprive, dysménorrhée | Aménorrhée, spotting, "
                "métrorragies, acné |\n"
                "| Avantage spécifique | Pas d'hormones | Efficacité supérieure + intérêt si ménorragies, "
                "adénomyose, mastodynies |\n"
            )),
            FicheRow(concept="CI du DIU", detail_md=(
                "- Grossesse existante/soupçonnée\n"
                "- **Infection génitale haute** actuelle ou récente < 3 mois\n"
                "- Cervicite purulente\n"
                "- Malformation utérine majeure\n"
                "- Saignement utéro-vaginal non exploré\n"
                "- CI spécifiques DIU progestérone : cancer sein, accident TE évolutif, "
                "hépatopathie sévère"
            )),
            FicheRow(concept="Contraception d'urgence", detail_md=(
                "| Méthode | Délai | Efficacité | Accès |\n"
                "|---------|-------|-----------|-------|\n"
                "| **Norlevo** (lévonorgestrel) | < **72h** | Modérée | Vente libre, gratuit mineurs |\n"
                "| **EllaOne** (ulipristal acétate) | < **5 jours** | 2-3x > Norlevo | Ordonnance obligatoire |\n"
                "| **DIU cuivre** | < **5 jours** | Taux échec **0,1%** | Pose médicale |\n"
            )),
            FicheRow(concept="◆ Conduite si oubli de pilule", detail_md=(
                "- **Oubli < 12h** (CEP) ou < 3h (microprogestative) : prendre immédiatement le "
                "comprimé oublié, prendre le suivant à l'heure habituelle\n"
                "- **Oubli > 12h** (CEP) ou > 3h (microprogestative) :\n"
                "  - Prendre immédiatement le comprimé oublié\n"
                "  - Prendre le suivant à l'heure habituelle\n"
                "  - **Contraception d'urgence** si rapports dans les 5 jours précédents\n"
                "  - **Contraception mécanique** pendant 7-14 jours"
            )),
            FicheRow(concept="", detail_md=(
                "- **EllaOne** (ulipristal) est **2-3 fois plus efficace** que Norlevo et reste "
                "efficace jusqu'à **5 jours** après le rapport, mais nécessite une ordonnance\n"
                "- Le **DIU cuivre** est la méthode de contraception d'urgence **la plus efficace** "
                "(taux d'échec 0,1%)"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="E", titre="Situations cliniques particulières et stérilisation", rows=[
            FicheRow(concept="Diabète", detail_md=(
                "- **DT1** : DIU en 1re intention. POP possible si bilan lipidique normal, "
                "TA normale, pas de néphropathie, pas de tabac, DT1 < 15 ans\n"
                "- **DT2** : DIU +++ ou micro-progestatifs\n"
                "- **ATCD diabète gestationnel** : pas de CI aux OP si absence de FDRCV"
            )),
            FicheRow(concept="Autres situations", detail_md=(
                "- **ATCD accident TE** : OP **formellement et définitivement CI** → "
                "DIU, micro-progestatifs, implant SC, contraceptifs locaux\n"
                "- **HTA** : micro-progestatifs ou DIU. Si HTA secondaire à POP → arrêt POP\n"
                "- **Obésité** (risque grossesse non désirée x4) : OP possible si < 35 ans "
                "sans FDRCV, sinon DIU ou micro-progestatifs. Après chirurgie bariatrique/by-pass : "
                "éviter contraceptifs oraux → patch/anneau, implant, DIU\n"
                "- **Post-IVG** : toutes contraceptions utilisables, méthodes hormonales "
                "démarrées le jour de l'IVG chirurgicale"
            )),
            FicheRow(concept="Stérilisation féminine", detail_md=(
                "- Loi du 4 juillet 2001 : toute personne **majeure** peut en faire la demande\n"
                "- Information éclairée, libre de sa volonté\n"
                "- **Délai de réflexion de 4 mois** après 1re consultation\n"
                "- **Consentement écrit** nécessaire\n"
                "- Méthode : cœlioscopie avec ligature de trompes (salpingectomie partielle/totale)"
            )),
        ]),
    ])

    # ── PARTIE III : GROSSESSE EXTRA-UTÉRINE ──
    partie_iii = Partie(numero="III", titre="Grossesse extra-utérine", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et facteurs de risque", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **GEU** : implantation et développement d'une grossesse en dehors de la cavité utérine\n"
                "- **Grossesse hétérotopique** : coexistence GIU + GEU (FDR principal = PMA)\n"
                "- Incidence : **2%** des grossesses"
            )),
            FicheRow(concept="FDR", detail_md=(
                "- **ATCD IGH** (RR = 6), dont ++ *C. trachomatis*\n"
                "- ATCD de GEU\n"
                "- **Tabac** (relation dose-effet)\n"
                "- ATCD chirurgie tubaire/abdomino-pelvienne (adhérences)\n"
                "- Âge maternel élevé\n"
                "- Contraception : **DIU**, pilule micro-progestative\n"
                "- **FIV**\n"
                "- Malformation utérine/tubaire, endométriose tubaire"
            )),
            FicheRow(concept="◆ Localisations", detail_md=(
                "| Localisation | Fréquence |\n"
                "|-------------|----------|\n"
                "| **Ampullaire** | **75%** |\n"
                "| Isthmique | 20% |\n"
                "| Pavillonnaire | 3% |\n"
                "| Interstitielle | 2% |\n"
                "| Ovarienne/abdominale/cervicale | Exceptionnelle |\n"
            )),
        ]),
        SousPartie(lettre="B", titre="Tableau clinique et examens complémentaires", rows=[
            FicheRow(concept="Triade clinique", detail_md=(
                "- **Retard de règles**\n"
                "- **Métrorragies** peu abondantes, sépia\n"
                "- **Douleurs pelviennes latéralisées**\n"
                "- Possibles signes sympathiques de grossesse, douleurs scapulaires "
                "(formes évoluées)\n"
                "- Préciser groupe, Rhésus"
            )),
            FicheRow(concept="Examen clinique", detail_md=(
                "- Constantes : TA, FC, FR, T\n"
                "- Recherche syndrome anémique, signes d'irritation péritonéale\n"
                "- **Spéculum** : confirme origine endo-utérine des saignements\n"
                "- **TV** : utérus plus petit que le terme théorique, douleur latéro-utérine (90%), "
                "masse latéro-utérine douloureuse (50%), empâtement cul-de-sac de Douglas"
            )),
            FicheRow(concept="", detail_md=(
                "- ⚠ Jusqu'à preuve du contraire, penser à une **rupture tubaire** si : douleur à "
                "la mobilisation utérine, douleur à la décompression, défense abdominale, "
                "scapulalgies, lipothymies, instabilité hémodynamique → **hospitalisation systématique**"
            ), kind="piege"),
            FicheRow(concept="HCG quantitative", detail_md=(
                "- Cinétique perturbée à 48h : stagnation ou élévation insuffisante\n"
                "- **Élimine le diagnostic si négatif**\n"
                "- Si < 1 500 UI/L sans signes de gravité : répéter dosage + écho à 48h"
            )),
            FicheRow(concept="Échographie pelvienne", detail_md=(
                "- Par voie abdominale **et endo-vaginale**\n"
                "- **Signes directs** : masse latéro-utérine, sac gestationnel extra-utérin, "
                "embryon avec activité cardiaque (5%), hématosalpinx\n"
                "- **Signes indirects** : vacuité utérine, **pseudo-sac** (image trompeuse "
                "sans couronne trophoblastique), endomètre épais/gravide, épanchement Douglas\n"
                "- **Espace de Morrison** (hépato-rénal) : hémopéritoine de grande abondance"
            )),
            FicheRow(concept="", detail_md=(
                "- Le **pseudo-sac** est un piège échographique : image lacunaire centée dans "
                "la cavité, sans couronne trophoblastique, qui simule une GIU. Ne pas confondre "
                "avec un vrai sac gestationnel !"
            ), kind="piege"),
        ]),
        SousPartie(lettre="C", titre="Prise en charge", rows=[
            FicheRow(concept="Choix thérapeutique", detail_md=(
                "- Aide au choix : **score de Fernandez** (si score < 13 → traitement médical)\n"
                "- Laisser le choix à la patiente\n"
                "- Prévenir si chirurgie : risque laparoconversion, salpingectomie, transfusion, "
                "pronostic fertilité"
            )),
            FicheRow(concept="Traitement chirurgical", detail_md=(
                "- **Indications** : hémodynamique instable, défense abdominale, HCG > 5 000 mUI/L, "
                "hématosalpinx > 4 cm, CI traitement médical, impossibilité suivi ambulatoire\n"
                "- **Cœlioscopie** = référence (laparotomie si CI/complications)\n"
                "- Temps diagnostique → pronostique → thérapeutique :\n"
                "  - **Conservateur** : salpingotomie + aspiration grossesse\n"
                "  - **Non conservateur** : salpingectomie (si trompe très endommagée "
                "ET trompe controlatérale saine)"
            )),
            FicheRow(concept="Traitement médical ambulatoire", detail_md=(
                "- But : lyse chimique de la grossesse\n"
                "- Indications : absence d'indications chirurgicales\n"
                "- Bilan pré-MTX : NFS, bilan rénal, bilan hépatique, TP-TCA\n"
                "- **Méthotrexate 1 mg/kg IM** injection unique\n"
                "- Surveillance prolongée de la **décroissance HCG** jusqu'à négativation\n"
                "- Si échec (20%) : 2e injection ou cœlioscopie"
            )),
            FicheRow(concept="◆ À distance", detail_md=(
                "- Risque de récidive : **10-30%** → consultation précoce si nouvelle grossesse\n"
                "- Risque de stérilité tubaire\n"
                "- **Sevrage tabagique**\n"
                "- Contraception OP à privilégier\n"
                "- Prévention AMF si Rh négatif"
            )),
        ]),
    ])

    # ── PARTIE IV : GROSSESSE NORMALE ──
    partie_iv = Partie(numero="IV", titre="Grossesse normale", sous_parties=[
        SousPartie(lettre="A", titre="Modifications physiologiques", rows=[
            FicheRow(concept="◆ Prise de poids conseillée", detail_md=(
                "| IMC avant grossesse | Prise de poids conseillée |\n"
                "|--------------------|-------------------------|\n"
                "| < 18,5 | 12,5-18 kg |\n"
                "| 18,5-24,9 | 11,5-16 kg |\n"
                "| 25-29,9 | 7-11,5 kg |\n"
                "| > 30 | 5-9 kg |\n"
            )),
            FicheRow(concept="Modifications métaboliques", detail_md=(
                "- Augmentation métabolisme basal de 15-30%\n"
                "- Augmentation TG (2-3x la normale), CT augmenté\n"
                "- Diminution glycémie, augmentation sécrétion/résistance insuline"
            )),
            FicheRow(concept="Modifications circulatoires", detail_md=(
                "- Augmentation **volémie** dès 3e mois\n"
                "- Augmentation Dc de **30-50%** (augmentation FC et VES)\n"
                "- Diminution résistances artérielles systémiques\n"
                "- **Syndrome de compression aorto-cave** : compression VCI par utérus gravide → "
                "prévention par **DLG**"
            )),
            FicheRow(concept="Modifications respiratoires et digestives", detail_md=(
                "- Augmentation besoins O2 de 20-30%, augmentation FR et volume courant, "
                "baisse PaCO2\n"
                "- NV entre 4-12 SA, pyrosis fréquent\n"
                "- À partir T2 : **estomac plein même à jeun**"
            )),
            FicheRow(concept="Modifications urinaires et cutanées", detail_md=(
                "- Augmentation DFG, dilatation pyélocalicielle (+ prononcée à droite), "
                "glycosurie physiologique\n"
                "- Hyperpigmentation (aréoles, ligne médiane abdomen)\n"
                "- **Masque de grossesse** (chloasma) : nappe maculeuse visage/cou → éviter soleil"
            )),
            FicheRow(concept="Modifications biologiques", detail_md=(
                "- **Hémodilution** : Hb jusqu'à 11 g/dL, Ht jusqu'à 32%\n"
                "- Hyperleucocytose physiologique (jusqu'à 15 000/mm3)\n"
                "- Légère diminution plaquettes\n"
                "- **Augmentation risque thromboembolique**\n"
                "- Augmentation VS (non interprétable pendant grossesse)"
            )),
        ]),
        SousPartie(lettre="B", titre="Datation et suivi de grossesse", rows=[
            FicheRow(concept="Datation", detail_md=(
                "- **SA** : calculées depuis le 1er jour des DDR\n"
                "- **DDG** = DDR + 14 jours\n"
                "- **Terme théorique** = DDG + 9 mois = **41 SA**\n"
                "- En FIV : DDG = jour de ponction\n"
                "- **LCC** (11-14 SA) : moyen le **plus fiable** pour dater la grossesse"
            )),
            FicheRow(concept="1re consultation (avant 15 SA)", detail_md=(
                "- Confirmation grossesse, datation, terme théorique\n"
                "- Classification du suivi : A (bas risque) → A1 → A2 → B (haut risque)\n"
                "- **Examens obligatoires** : sérologies rubéole/toxoplasmose/syphilis, AgHBs, "
                "Gr-Rh-Kell-RAI, BU\n"
                "- **À proposer** : NFS-plaquettes, VIH 1+2, VHC, FCU si > 3 ans, glycémie à jeun "
                "si FDR diabète gestationnel, marqueurs sériques T21\n"
                "- **Inutiles** : sérologie CMV, bilan lipidique, protéine S"
            )),
            FicheRow(concept="", detail_md=(
                "- La sérologie **CMV** est un examen **inutile** au 1er trimestre\n"
                "- Ne pas oublier que la **VS** est non interprétable pendant la grossesse"
            ), kind="piege"),
            FicheRow(concept="Échographie T1 (11-13 SA + 6j)", detail_md=(
                "- Non obligatoire mais à proposer systématiquement\n"
                "- Permet : nombre de fœtus, chorionicité, évolutivité, LCC, mesure **clarté nucale**, "
                "dépistage malformations majeures"
            )),
            FicheRow(concept="Dépistage combiné T21", detail_md=(
                "- Non obligatoire mais doit être **proposé à toutes les femmes enceintes**\n"
                "- Consentement écrit nécessaire\n"
                "- Calcul du risque combiné : âge maternel + marqueurs sériques T1 "
                "(**PAPP-A** diminuée, **β-HCG libre** élevée si T21) + clarté nucale\n"
                "- Risque 1/50-1/1000 : **DPANI** (ADN libre circulant sang maternel)\n"
                "- Risque > 1/50 ou nuque épaisse : **caryotype fœtal** (villosités choriales/amniocentèse)"
            )),
            FicheRow(concept="◆ Déclaration et conseils", detail_md=(
                "- Déclaration avant **15 SA** (3 volets : 2 CAF, 1 CPAM)\n"
                "- Prise en charge à 100% des 7 consultations prénatales\n"
                "- Conseils : arrêt OH/tabac, pas d'automédication, alimentation équilibrée\n"
                "- Éviter fromages non pasteurisés/charcuterie artisanale (prévention **listériose**)\n"
                "- Prévention **toxoplasmose** si sérologie négative"
            )),
        ]),
        SousPartie(lettre="C", titre="Consultations du 2e et 3e trimestre", rows=[
            FicheRow(concept="Hauteur utérine", detail_md=(
                "| Mois | HU normale |\n"
                "|------|----------|\n"
                "| 4 mois | 16 cm |\n"
                "| 5 mois | 20 cm |\n"
                "| 6 mois | 24 cm |\n"
                "| 7 mois | 28 cm |\n"
                "| 8 mois | 30 cm |\n"
                "| 9 mois | 32 cm |\n"
            )),
            FicheRow(concept="", detail_md=(
                "- **HU insuffisante** : erreur de terme, RCIU, oligoamnios, mort fœtale\n"
                "- **HU excessive** : erreur de terme, grossesse multiple, macrosomie, "
                "hydramnios, utérus fibromateux"
            ), kind="a_retenir"),
            FicheRow(concept="Consultations clés", detail_md=(
                "- **4e mois** (16-20 SA) : entretien prénatal précoce (EPP), prescription écho T2 "
                "(22 SA : morphologie fœtale + croissance + placenta + LA)\n"
                "- **6e mois** (24-28 SA) : dépistage diabète gestationnel si FDR, AgHBs obligatoire, "
                "NFS-plaquettes, RAI si Rh-. Orientation maternité\n"
                "- **7e mois** (28-32 SA) : 2e détermination Gr-Rh-RAI, prévention AMF si Rh- "
                "et fœtus RHD+, UVEDOSE (vit D), écho T3 (32 SA : présentation + croissance + "
                "malformations tardives + score de Manning)\n"
                "- **8e mois** (33-37 SA) : PV streptocoque B, consultation anesthésie, "
                "congé prénatal (35 SA)\n"
                "- **9e mois** (37-41 SA) : présentation fœtale, RDV jour du terme"
            )),
            FicheRow(concept="◆ Congé maternité", detail_md=(
                "- 1er/2e enfant : **6 semaines** prénatales (+14j si grossesse pathologique) + "
                "**10 semaines** postnatales\n"
                "- Durée augmente pour 3e enfant/grossesses multiples\n"
                "- Congé paternité : **11 jours** payés par sécurité sociale\n"
                "- Possibilité réduire congé prénatal de 3 semaines (ajoutées au postnatal)"
            )),
            FicheRow(concept="Niveaux de maternité", detail_md=(
                "| Niveau | Équipement | Part |\n"
                "|--------|-----------|------|\n"
                "| 1 | Grossesses bas risque, pas de néonat | 49% |\n"
                "| 2a | Unité de néonatalogie | 23% |\n"
                "| 2b | Soins intensifs néonatals | 16% |\n"
                "| 3 | **Réanimation néonatale** + réa adulte | 12% |\n"
            )),
            FicheRow(concept="Consultation postnatale", detail_md=(
                "- **Obligatoire** dans les 6-8 semaines après accouchement\n"
                "- État psychologique, examen périnée, seins\n"
                "- Prescription : 10 séances rééducation abdominale/périnéale + contraception"
            )),
            FicheRow(concept="Diagnostic de grossesse", detail_md=(
                "- HCG détectable dès **J9** post-fécondation\n"
                "- Taux HCG **double toutes les 48h**\n"
                "- Sac gestationnel visible pour HCG = **1 500 UI/L**\n"
                "- Se négative dans les 5 jours suivant l'accouchement"
            )),
        ]),
    ])

    # ── PARTIE V : HÉMORRAGIES GÉNITALES ──
    partie_v = Partie(numero="V", titre="Hémorragies génitales de la femme", sous_parties=[
        SousPartie(lettre="A", titre="Définitions et classification", rows=[
            FicheRow(concept="Définitions", detail_md=(
                "- **Hémorragies génitales** : pertes de sang provenant de l'appareil génital féminin, "
                "extériorisées par l'orifice vulvaire\n"
                "- **Hémorragies génitales basses** : vulvaires, vaginales, cervicales\n"
                "- **Hémorragies génitales hautes** : d'origine utérine, extériorisées par le col, "
                "classées selon rapport aux règles"
            )),
            FicheRow(concept="Métrorragies", detail_md=(
                "- Saignement d'origine endo-utérine survenant **en dehors des règles**\n"
                "- **Fonctionnelles** : anovulation par absence du pic pré-ovulatoire LH, "
                "dysfonctionnement HTHP. Diagnostic d'**élimination**\n"
                "- **Organiques bénignes** : fibromes, hyperplasie endomètre, polype endométrial, "
                "adénomyose, troubles hémostase\n"
                "- **Organiques malignes** : cancer endomètre, cancer col, tumeurs ovariennes "
                "œstrogéno-sécrétantes"
            )),
            FicheRow(concept="Ménorragies", detail_md=(
                "- Hémorragie utérine coïncidant avec les règles, plus longues/abondantes "
                "(> **80 mL** et durée > **7 jours**)\n"
                "- **Polyménorrhées** : anomalies durée et abondance\n"
                "- **Hyperménorrhées** : durée normale mais trop abondantes (> 80 mL)\n"
                "- **Macroménorrhées** : trop longues (> 6j) mais abondance normale\n"
                "- **Pollakiménorrhées** : règles trop fréquentes (cycles trop courts)"
            )),
        ]),
        SousPartie(lettre="B", titre="Métrorragies et ménorragies", rows=[
            FicheRow(concept="Bilan étiologique", detail_md=(
                "- **Interrogatoire** : différencier méno/métrorragies, DDR, ATCD utérins, "
                "traitements (oubli contraceptif, anticoagulants), tabagisme, "
                "score de **Higham** (nombre de protections)\n"
                "- **Examen clinique** : constantes, signes d'anémie, examen gynécologique "
                "(spéculum + TV)\n"
                "- **Examens complémentaires** :\n"
                "  - **HCG plasmatique** +++ (systématique)\n"
                "  - NFS-plaquettes, TP-TCA\n"
                "  - Échographie pelvienne (sus-pubienne + endovaginale + doppler)\n"
                "  - FCU pour éliminer pathologie cervicale"
            )),
            FicheRow(concept="◆ Examens de 2e intention", detail_md=(
                "- Hystéroscopie diagnostique + biopsie endomètre si FDR cancer endomètre "
                "ou patiente > 45 ans\n"
                "- IRM pelvienne si utérus polymyomateux volumineux, suspicion adénomyose\n"
                "- TSH si suspicion hypothyroïdie\n"
                "- Bilan hormonal si irrégularités menstruelles associées"
            )),
            FicheRow(concept="PEC ménorragies fonctionnelles", detail_md=(
                "- **Sans désir de grossesse** (du + au - efficace) :\n"
                "  - **DIU lévonorgestrel** (le plus efficace)\n"
                "  - Acide tranexamique\n"
                "  - Contraceptifs OP/progestatifs\n"
                "  - AINS\n"
                "- **Avec désir de grossesse immédiat** ou CI hormonaux : acide tranexamique\n"
                "- Si échec : traitement chirurgical conservateur (destruction endomètre)\n"
                "- Traitement martial si anémie ferriprive"
            )),
        ]),
        SousPartie(lettre="C", titre="Étiologies selon la période de vie", rows=[
            FicheRow(concept="Période péri-pubertaire", detail_md=(
                "- **Causes fonctionnelles** ++ (immaturité SNC → anovulation) : "
                "progestatif lutéomimétique 10j/mois en 2e partie de cycle\n"
                "- Causes organiques : grossesse, GEU, troubles hémostase, "
                "infections (vulvo-vaginite, cervicite, IGH), hypothyroïdie"
            )),
            FicheRow(concept="Période d'activité génitale", detail_md=(
                "- Causes gravidiques (toujours HCG)\n"
                "- **Causes endo-utérines** : fibrome sous-muqueux/interstitiel, hyperplasie "
                "endomètre, cancer endomètre, polype endométrial, adénomyose\n"
                "- Causes cervicales : cancer col, polype, endométriose cervicale\n"
                "- Causes iatrogènes : DIU, POP, progestatifs, anticoagulants"
            )),
            FicheRow(concept="", detail_md=(
                "- Chez la femme **ménopausée**, toute métrorragie est un **cancer de "
                "l'endomètre** jusqu'à preuve du contraire"
            ), kind="a_retenir"),
            FicheRow(concept="Femme ménopausée", detail_md=(
                "- **Cancer endomètre** +++ (à éliminer en priorité)\n"
                "- Vaginite sénile (atrophie par carence œstrogénique → traitement par "
                "œstrogènes locaux)\n"
                "- Cancer vulve/vagin, cancer col\n"
                "- Polype endométrial, sarcome utérin\n"
                "- Causes iatrogènes : THS mal équilibré, anticoagulants\n"
                "- Causes fonctionnelles : atrophie endomètre, hyperplasie endomètre"
            )),
        ]),
    ])

    # ── PARTIE VI : IGH ──
    partie_vi = Partie(numero="VI", titre="Infections génitales hautes", sous_parties=[
        SousPartie(lettre="A", titre="Généralités et tableau clinique", rows=[
            FicheRow(concept="Définition", detail_md=(
                "- **IGH** : infections secondaires à l'ascension de germes vaginaux à travers le col\n"
                "- **Non compliquée** : endométrites, salpingites\n"
                "- **Compliquée** : pyosalpinx, abcès tubo-ovariens, pelvipéritonite, échec traitement "
                "ambulatoire"
            )),
            FicheRow(concept="FDR", detail_md=(
                "- Femme jeune (**≤ 25 ans**)\n"
                "- Précocité des 1ers rapports, partenaires multiples (≥ 2/an)\n"
                "- Bas niveau socio-économique\n"
                "- ATCD IST/IGH, IST chez le partenaire\n"
                "- Gestes endo-utérins, post-partum, post-abortum"
            )),
            FicheRow(concept="Germes", detail_md=(
                "- **IST** : *C. trachomatis* (**60%**), *N. gonorrhoeae* (10%), *M. genitalium*\n"
                "- **Opportunistes** (flore vaginale) : streptocoques, staphylocoques, entérocoques, "
                "entérobactéries (*E. coli*, Klebsiella), anaérobies (*Bacteroides fragilis*)\n"
                "- Rarement : tuberculose, bilharziose"
            )),
            FicheRow(concept="Tableau clinique", detail_md=(
                "- **Douleurs pelviennes spontanées > 4 jours**\n"
                "- Dyspareunies\n"
                "- Douleur hypochondre droit (**Fitz-Hugh-Curtis**)\n"
                "- Leucorrhée (50%), métrorragies (40%)\n"
                "- Syndrome rectal si abcès du Douglas\n"
                "- **Examen clinique** : douleur hypogastrique +/- défense, leucorrhée au spéculum, "
                "cervicite, **douleur à la mobilisation utérine** au TV, douleur annexielle"
            )),
            FicheRow(concept="Examens complémentaires", detail_md=(
                "- NFS-CRP (souvent normaux si non compliquée), **HCG** (éliminer GEU)\n"
                "- **PV + prélèvement endocervical** : examen direct, culture, "
                "TAAN *C. trachomatis*, *N. gonorrhoeae*, *M. genitalium*\n"
                "- BU/ECBU, hémocultures si T > 38,5 ou frissons\n"
                "- Bilan IST complet : VIH, syphilis, VHB, VHC\n"
                "- **Échographie pelvienne** (++ endovaginale) : épaississement pariétal tubaire > 5 mm, "
                "signe de la **roue dentée**, masse latéro-utérine, épanchement Douglas"
            )),
            FicheRow(concept="Diagnostic différentiel", detail_md=(
                "- GEU, torsion d'annexe, appendicite aiguë pelvienne, infection urinaire, "
                "sigmoïdite diverticulaire"
            )),
        ]),
        SousPartie(lettre="B", titre="Complications et prise en charge", rows=[
            FicheRow(concept="Complications aiguës", detail_md=(
                "- **Abcès pelviens** (10-35% des IGH) : pyosalpinx, abcès tubo-ovarien, "
                "abcès du Douglas. Fièvre, AEG, masse pelvienne au TV → drainage chirurgical "
                "par cœlioscopie\n"
                "- **Pelvipéritonite aiguë** : péritonite à point de départ tubaire\n"
                "- **Syndrome de Fitz-Hugh-Curtis** : péri-hépatite (inflammation capsule de Glisson). "
                "Tableau de cholécystite. Germes : *C. trachomatis* (80%), gonocoque (20%). "
                "VS élevée, hyperleucocytose, BH normal. Cœlioscopie : adhérences en **corde de violon**"
            )),
            FicheRow(concept="Complications tardives", detail_md=(
                "- **Stérilité tubaire** : 1re cause de stérilité tubaire\n"
                "- **GEU** : RR **x10**\n"
                "- Récidive (**20%**)\n"
                "- Salpingite chronique : asymptomatique, adhérences tubo-pelviennes\n"
                "- Algies pelviennes chroniques (15%)\n"
                "- Avortements spontanés précoces"
            )),
            FicheRow(concept="", detail_md=(
                "- Les IGH sont la **1re cause de stérilité tubaire** et multiplient le risque "
                "de **GEU par 10**"
            ), kind="a_retenir"),
            FicheRow(concept="Traitement IGH non compliquée", detail_md=(
                "- **Ambulatoire** : ATB probabiliste PO, synergique, bactéricide, large spectre\n"
                "- 1re intention : **doxycycline** 100 mg x2/j PO + **métronidazole** 500 mg x2/j PO "
                "+ **ceftriaxone** 1g IM\n"
                "- Durée totale : **14 jours**\n"
                "- Adaptation secondaire à l'ATBG\n"
                "- Réévaluation à **3-5 jours** : si pas d'amélioration → hospitalisation"
            )),
            FicheRow(concept="Traitement IGH compliquée", detail_md=(
                "- **Hospitalisation**\n"
                "- ATB **IV** pendant 14-21 jours\n"
                "- Relais PO après 48h d'apyrexie\n"
                "- Drainage chirurgical : cœlioscopie ou ponction transvaginale si abcès > 3 cm\n"
                "- Retrait DIU si IGH compliquée, pose récente responsable, ou échec ambulatoire"
            )),
            FicheRow(concept="Mesures associées", detail_md=(
                "- Dépistage IST et traitement du partenaire\n"
                "- PV de contrôle à 3-6 mois si IGH à IST"
            )),
        ]),
    ])

    # ── PARTIE VII : LEUCORRHÉES ET MÉNOPAUSE ──
    partie_vii = Partie(numero="VII", titre="Leucorrhées et ménopause", sous_parties=[
        SousPartie(lettre="A", titre="Leucorrhées", rows=[
            FicheRow(concept="Écosystème vaginal", detail_md=(
                "- Flore dominante : **bacille de Döderlein** (lactobacille) → transforme "
                "glycogène en acide lactique → pH vaginal acide = protection contre "
                "pullulation microbienne\n"
                "- Flore vaginale varie selon : âge (moins de Döderlein en péripuberté/ménopause), "
                "cycle, contraception (augmentation anaérobies si DIU)"
            )),
            FicheRow(concept="Leucorrhées physiologiques vs pathologiques", detail_md=(
                "| Critère | Physiologique | Pathologique |\n"
                "|---------|-------------|-------------|\n"
                "| Aspect | Blanche/transparente, inodore | Aspect anormal |\n"
                "| Signes fonctionnels | Aucun | Prurit, brûlure, dyspareunie, SFU |\n"
                "| Variation au cycle | Oui (surtout pré-ovulatoire) | Non |\n"
                "| PV | Peu de PNN, Döderlein abondant | PNN altérés, Döderlein absent, "
                "agent pathogène |\n"
            )),
            FicheRow(concept="Vulvo-vaginite à C. albicans", detail_md=(
                "- **FDR** : grossesse, diabète, ATB++, POP, corticoïdes, hygiène inadaptée "
                "(toilettes excessives, sous-vêtements synthétiques)\n"
                "- **Clinique** : leucorrhée blanchâtre **grumeleuse** (aspect lait caillé), "
                "prurit/brûlures vulvaires, vulvo-vaginite avec œdème\n"
                "- **Pas d'examens complémentaires** sauf doute ou récidive "
                "(culture milieu de **Sabouraud**)\n"
                "- **Traitement** : antifongique local (ovule sertaconazole/fenticonazole), "
                "pommade vulvaire. Traitement partenaire seulement si balanite ou récidive\n"
                "- Si > **4 épisodes/an** : recherche FDR, myogramme, traitement prolongé "
                "+/- décontamination digestive"
            )),
            FicheRow(concept="Trichomonas vaginalis", detail_md=(
                "- IST parasitaire. FDR : alcalinisation milieu vaginal, hypo-œstrogénie\n"
                "- **Clinique** : leucorrhée **verdâtre, spumeuse, nauséabonde, bulleuse**, "
                "prurit variable, brûlures mictionnelles/coïtales, cervicite avec piqueté "
                "hémorragique (**col rouge framboise**)\n"
                "- Examen extemporané : protozoaire **flagellé** et mobile\n"
                "- **Traitement** : **métronidazole** 2g prise unique PO (ou 500 mg x2/j 10j), "
                "savon acide. Traitement **systématique** du partenaire"
            )),
            FicheRow(concept="", detail_md=(
                "- Le traitement du partenaire est **systématique** pour le Trichomonas (IST) "
                "mais **non systématique** pour la candidose (seulement si balanite/récidive)"
            ), kind="a_retenir"),
            FicheRow(concept="Vaginose bactérienne", detail_md=(
                "- Germe : **Gardnerella vaginalis** (BGN), anaérobies\n"
                "- Leucorrhée abondante, **grisâtre, nauséabonde**, peu d'irritation locale\n"
                "- Diagnostic de certitude :\n"
                "  - Test à la potasse positif (**odeur de poisson pourri**)\n"
                "  - pH vaginal alcalin\n"
                "  - **Clue cells** à l'examen extemporané (pathognomonique)"
            )),
            FicheRow(concept="◆ Cervicites (IST)", detail_md=(
                "- *C. trachomatis* : portage asymptomatique fréquent, diagnostic par **PCR**\n"
                "- Gonocoque : souvent asymptomatique, leucorrhée purulente possible, "
                "diagnostic par **PCR**"
            )),
        ]),
        SousPartie(lettre="B", titre="Ménopause et traitement hormonal", rows=[
            FicheRow(concept="Périménopause", detail_md=(
                "- Période de perturbation du cycle survenant **5-10 ans** avant la ménopause\n"
                "- Liée à un état d'**hyperoestrogénie relative**\n"
                "- Clinique : cycles irréguliers, méno/métrorragies, aggravation syndrome prémenstruel\n"
                "- Traitement : progestatifs de synthèse du 15e au 25e jour du cycle "
                "(réduction hyperplasie endomètre) +/- DIU à la progestérone"
            )),
            FicheRow(concept="Ménopause — Définition et diagnostic", detail_md=(
                "- Disparition définitive du cycle menstruel par épuisement du capital folliculaire\n"
                "- Survient en moyenne à **50-52 ans**\n"
                "- **Diagnostic clinique** : aménorrhée secondaire > **12 mois**\n"
                "- Pas de dosage hormonal nécessaire sauf doute (hystérectomie, contraception) "
                "ou ménopause précoce (< 40 ans) → FSH très augmentée, œstradiol très diminué"
            )),
            FicheRow(concept="Syndrome climatérique", detail_md=(
                "- **Bouffées de chaleur** : sensation de chaleur intense, brutale, transitoire, "
                "rougeur face/tronc, sueurs profuses (surtout nocturnes)\n"
                "- Troubles neuropsychiques : irritabilité, dépression, insomnie, anxiété\n"
                "- Conséquences à long terme : atrophie vulvo-vaginale, sécheresse muqueuse, "
                "disparition flore de Döderlein, IUE +/- prolapsus, **ostéoporose**, "
                "disparition protection vasculaire, prise poids androïde"
            )),
            FicheRow(concept="◆ Bilan hormonal (si nécessaire)", detail_md=(
                "| Paramètre | Périménopause | Ménopause confirmée |\n"
                "|-----------|-------------|--------------------|\n"
                "| FSH | Augmentée | **Très augmentée** |\n"
                "| LH | Normale/augmentée | Augmentée |\n"
                "| Œstrogènes | Diminuée | **Très diminuée** |\n"
                "| Progestérone | Diminuée | **Très diminuée** |\n"
            )),
            FicheRow(concept="THM — Modalités", detail_md=(
                "- **Indications** : seulement si plainte fonctionnelle (non systématique)\n"
                "- Durée limitée à **5 ans** à dose minimale efficace\n"
                "- Voie **transdermique** préférée (patch/crème) : diminue les ES\n"
                "- **Schéma séquentiel** (avec règles) : œstrogènes J1-J25 + progestatif J14-J25\n"
                "- **Schéma continu** (sans règles) : œstrogènes + progestatif (1/2 dose) J1-J31\n"
                "- **Progestatifs** : 12j/mois obligatoires sauf si hystérectomie "
                "(prévention cancer endomètre)\n"
                "- Bilan pré-THM : examen clinique, glycémie à jeun, EAL, mammographie"
            )),
            FicheRow(concept="CI absolues du THM", detail_md=(
                "- ATCD avec risque CV élevé\n"
                "- Insuffisance hépatique sévère\n"
                "- Maladies rares : lupus, porphyries"
            )),
            FicheRow(concept="Balance bénéfice/risque THM", detail_md=(
                "| Bénéfices | Risques |\n"
                "|-----------|--------|\n"
                "| Traitement effets ménopause | Maladies thromboemboliques (++ si PO) |\n"
                "| Diminution risque ostéoporose | Augmentation légère cancer sein si > 5 ans |\n"
                "| +/- Diminution risque CV | +/- Augmentation risque cancer endomètre |\n"
                "| Diminution probable cancer colon | — |\n"
            )),
            FicheRow(concept="Surveillance THM", detail_md=(
                "- À 3 mois puis tous les 6-12 mois : tolérance, efficacité, "
                "recherche signes de surdosage (tension mammaire, règles abondantes) "
                "ou sous-dosage (réapparition syndrome climatérique)\n"
                "- Paraclinique : EAL + glycémie (3 puis 6 mois puis tous les 3 ans), "
                "mammographie de dépistage tous les **2 ans**"
            )),
            FicheRow(concept="◆ Insuffisance ovarienne précoce", detail_md=(
                "- Ménopause survenant avant **40 ans** (< 5% des femmes)\n"
                "- Étiologies : génétique (ATCD familiaux), iatrogène (chirurgie, RT, CT)\n"
                "- Diagnostic confirmé par dosages hormonaux\n"
                "- **THS prolongé** généralement bien accepté"
            )),
            FicheRow(concept="Alternatives au THM", detail_md=(
                "- Bonne hygiène de vie, supplémentation vitamino-calcique\n"
                "- Œstrogènes locaux (sécheresse vaginale)\n"
                "- Tibolone (Livial) : efficacité sur syndrome climatérique, amélioration libido\n"
                "- Autres (discutés) : phyto-œstrogènes, β-alanine, véralipride, clonidine"
            )),
        ]),
    ])

    # ── TABLEAUX DE SYNTHÈSE ──
    tableaux = [
        TableauSynthese(titre="Comparaison des contraceptions hormonales", markdown=(
            "| Méthode | IP | Avantage | Inconvénient |\n"
            "|---------|-----|----------|-------------|\n"
            "| POP 2e gén | 0,3% | 1re intention, remboursée | Observance quotidienne |\n"
            "| Patch OP | 0,3% | Bonne observance | Sur-risque TE x2, non remboursé |\n"
            "| Anneau vaginal | 0,3% | Pas 1er passage hépatique | Non remboursé |\n"
            "| Microval | 1% | Remboursée | Tolérance oubli 3h |\n"
            "| Cerazette | 0,52% | Tolérance oubli 12h | Non remboursée |\n"
            "| Implant (Nexplanon) | 0,05% | 3 ans, très efficace | Troubles du cycle |\n"
            "| DIU cuivre | 0,6% | 5-10 ans, pas d'hormones | Ménorragies |\n"
            "| DIU progestérone | 0,1% | Le plus efficace | Aménorrhée, spotting |\n"
        )),
        TableauSynthese(titre="Étiologies des aménorrhées primaires", markdown=(
            "| CSS | Bilan hormonal | Diagnostic |\n"
            "|-----|---------------|------------|\n"
            "| Absents, âge osseux retardé | — | Retard pubertaire simple |\n"
            "| Absents, FSH/LH élevées | Hypogonadisme hypergonadotrope | Turner, dysgénésies |\n"
            "| Absents, FSH/LH basses | Hypogonadisme hypogonadotrope | Kallmann, anorexie |\n"
            "| Normaux, courbe T biphasique | — | Cause anatomique (imperforation hymen, Rokitansky) |\n"
            "| Normaux, courbe T monophasique | — | Cause hormonale (hyperprolactinémie, tumeurs) |\n"
        )),
        TableauSynthese(titre="Principales leucorrhées pathologiques", markdown=(
            "| Étiologie | Leucorrhée | Signe clé | Traitement |\n"
            "|-----------|-----------|-----------|------------|\n"
            "| C. albicans | Blanche, grumeleuse (lait caillé) | Prurit vulvaire | Antifongique local |\n"
            "| Trichomonas | Verdâtre, spumeuse, nauséabonde | Col framboise | Métronidazole + ttt partenaire |\n"
            "| Vaginose (Gardnerella) | Grisâtre, nauséabonde | Clue cells, sniff test + | Métronidazole |\n"
            "| C. trachomatis | Variable | Asymptomatique ++ | Doxycycline |\n"
        )),
        TableauSynthese(titre="GEU — Traitement chirurgical vs médical", markdown=(
            "| Critère | Chirurgical | Médical |\n"
            "|---------|-----------|--------|\n"
            "| Indications | Instabilité hémodynamique, HCG > 5000, hématosalpinx > 4 cm | "
            "Absence indications chirurgicales |\n"
            "| Méthode | Cœlioscopie (salpingotomie/salpingectomie) | Méthotrexate 1 mg/kg IM |\n"
            "| Taux échec | Faible | 20% (2e injection ou chirurgie) |\n"
            "| Surveillance | Post-op standard | Décroissance HCG jusqu'à négativation |\n"
        )),
        TableauSynthese(titre="Suivi de grossesse — Examens obligatoires par trimestre", markdown=(
            "| Trimestre | Examens obligatoires |\n"
            "|-----------|--------------------|\n"
            "| T1 (< 15 SA) | Sérologies rubéole/toxo/syphilis, AgHBs, Gr-Rh-Kell-RAI, BU |\n"
            "| T2 (6e mois) | AgHBs, NFS-plaquettes, RAI si Rh- |\n"
            "| T3 (8e mois) | PV streptocoque B |\n"
            "| Mensuel | Toxoplasmose si négative |\n"
        )),
    ]

    chiffres_cles = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Aménorrhée primaire | > **16 ans** | Absence de ménarche |\n"
        "| Aménorrhée secondaire | > **3 mois** | Absence de règles |\n"
        "| GEU — incidence | **2%** des grossesses | — |\n"
        "| GEU — localisation principale | Ampullaire **75%** | — |\n"
        "| Score Fernandez | < **13** | Traitement médical GEU |\n"
        "| Indice de Pearl POP | **0,3%** | Pilule OP |\n"
        "| IP DIU progestérone | **0,1%** | Le plus efficace |\n"
        "| IP implant Nexplanon | **0,05%** | Très efficace |\n"
        "| Thrombose veineuse sous OP | **5-12/10 000** | x3 vs population générale |\n"
        "| Terme théorique | **41 SA** | DDG + 9 mois |\n"
        "| Sac gestationnel visible | HCG = **1 500 UI/L** | Échographie |\n"
        "| Ménorragies | > **80 mL** et > **7 jours** | Définition |\n"
        "| Ménopause | **50-52 ans** | Âge moyen |\n"
        "| THM durée max | **5 ans** | Dose minimale efficace |\n"
        "| IGH — C. trachomatis | **60%** | 1er germe IST |\n"
        "| Stérilisation — délai réflexion | **4 mois** | Loi du 4 juillet 2001 |\n"
    ))

    points_cles = [
        "Devant toute aménorrhée secondaire : 1er réflexe = dosage **HCG plasmatique**",
        "POP de **2e génération** (lévonorgestrel) en 1re intention chez la femme jeune nullipare",
        "La **migraine avec aura** est une CI absolue aux oestroprogestatifs",
        "Le **DIU cuivre** est la contraception d'urgence la plus efficace (IP 0,1%)",
        "GEU : triade retard de règles + métrorragies sépia + douleurs pelviennes latéralisées",
        "Chez la femme ménopausée, toute métrorragie = **cancer endomètre** jusqu'à preuve du contraire",
        "Les IGH sont la 1re cause de **stérilité tubaire** et multiplient le risque de GEU par 10",
        "Le THM est limité à **5 ans** par voie transdermique, non systématique, uniquement si plainte fonctionnelle",
    ]

    fiche_eclair_md = (
        "**Aménorrhée** : primaire > 16 ans, secondaire > 3 mois. "
        "1er réflexe = HCG. Primaire sans CSS : retard pubertaire (sésamoïde absent), "
        "hypogonadisme hyper/hypogonadotrope. Avec CSS : cause anatomique (Rokitansky) "
        "ou hormonale.\n\n"
        "**Contraception** : POP 2e gén en 1re intention (IP 0,3%). CI absolues : MTEV, "
        "migraine avec aura, tabac > 35 ans, cancer sein. DIU = 1re intention aussi. "
        "Urgence : EllaOne < 5j > Norlevo < 72h. DIU cuivre le plus efficace.\n\n"
        "**GEU** : 2% des grossesses, 75% ampullaire. FDR : ATCD IGH (RR=6), tabac. "
        "Triade : retard de règles + métrorragies sépia + douleur pelvienne. "
        "Écho : vacuité utérine + masse latéro-utérine. "
        "Score Fernandez < 13 = MTX. Sinon cœlioscopie.\n\n"
        "**Grossesse normale** : terme = 41 SA. LCC = meilleur datation (11-14 SA). "
        "Dépistage T21 combiné proposé à toutes. "
        "Sérologies obligatoires : rubéole, toxo, syphilis, AgHBs.\n\n"
        "**Hémorragies génitales** : HCG systématique. Ménopausée = cancer endomètre "
        "jusqu'à preuve du contraire. Score de Higham. "
        "Ménorragies fonctionnelles : DIU lévonorgestrel le plus efficace.\n\n"
        "**IGH** : C. trachomatis 60%. Douleur pelvienne > 4j + douleur mobilisation "
        "utérine. Non compliquée = ambulatoire : doxycycline + métronidazole + ceftriaxone "
        "14j. Complications : stérilité tubaire, GEU x10.\n\n"
        "**Leucorrhées** : C. albicans (lait caillé, prurit), Trichomonas (verdâtre, "
        "col framboise, ttt partenaire systématique), vaginose (grisâtre, clue cells).\n\n"
        "**Ménopause** : aménorrhée > 12 mois, 50-52 ans. THM si plainte fonctionnelle, "
        "5 ans max, voie transdermique. CI : risque CV, hépatopathie."
    )

    return FicheData(
        matiere="Médecine Générale",
        nom_cours="Gynécologie",
        annee="2025-2026",
        item="Items 24, 35, 36, 40, 158",
        plan=plan,
        parties=[partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi, partie_vii],
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
    captions_file = PROJECT_ROOT / "output" / ".work" / "gynecologie" / "image_captions.json"
    if captions_file.exists():
        # ... (image loading code)
        pass

    output_dir = PROJECT_ROOT / "output" / "fiches"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Medecine_generale_gynecologie_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out} ({pdf_out.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()

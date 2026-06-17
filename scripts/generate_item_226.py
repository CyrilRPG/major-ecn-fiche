"""Génère la fiche de l'Item 226 - Thrombose veineuse profonde et embolie pulmonaire (Cardiologie)."""

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
        PlanPartie(numero="I", titre="Généralités et physiopathologie", sous_parties=[
            PlanSousPartie(lettre="A", titre="Définitions"),
            PlanSousPartie(lettre="B", titre="Épidémiologie"),
            PlanSousPartie(lettre="C", titre="Facteurs prédisposants"),
            PlanSousPartie(lettre="D", titre="Physiopathologie"),
            PlanSousPartie(lettre="E", titre="Histoire naturelle"),
        ]),
        PlanPartie(numero="II", titre="Thrombose veineuse profonde", sous_parties=[
            PlanSousPartie(lettre="A", titre="Diagnostic clinique"),
            PlanSousPartie(lettre="B", titre="Score de Wells et D-dimères"),
            PlanSousPartie(lettre="C", titre="Échodoppler veineux et stratégie"),
            PlanSousPartie(lettre="D", titre="Diagnostic étiologique"),
            PlanSousPartie(lettre="E", titre="Formes particulières et complications"),
        ]),
        PlanPartie(numero="III", titre="Embolie pulmonaire — diagnostic", sous_parties=[
            PlanSousPartie(lettre="A", titre="Clinique et examens standards"),
            PlanSousPartie(lettre="B", titre="Scores de probabilité"),
            PlanSousPartie(lettre="C", titre="Examens paracliniques"),
            PlanSousPartie(lettre="D", titre="Stratégie diagnostique"),
        ]),
        PlanPartie(numero="IV", titre="Embolie pulmonaire — pronostic et formes", sous_parties=[
            PlanSousPartie(lettre="A", titre="Stratification du risque"),
            PlanSousPartie(lettre="B", titre="Évolution et complications"),
            PlanSousPartie(lettre="C", titre="Formes cliniques particulières"),
        ]),
        PlanPartie(numero="V", titre="Traitement curatif", sous_parties=[
            PlanSousPartie(lettre="A", titre="Anticoagulation initiale"),
            PlanSousPartie(lettre="B", titre="Relais et durée du traitement"),
            PlanSousPartie(lettre="C", titre="Compression et mobilisation"),
            PlanSousPartie(lettre="D", titre="Stratégies et cas particuliers"),
            PlanSousPartie(lettre="E", titre="Filtre cave"),
        ]),
        PlanPartie(numero="VI", titre="Traitement préventif", sous_parties=[
            PlanSousPartie(lettre="A", titre="Principes généraux"),
            PlanSousPartie(lettre="B", titre="Situations à risque"),
        ]),
    ]

    # PARTIE I : Généralités et physiopathologie
    partie_i = Partie(numero="I", titre="Généralités et physiopathologie", sous_parties=[
        SousPartie(lettre="A", titre="Définitions", rows=[
            FicheRow(concept="◆ MTEV — vue d'ensemble", detail_md=(
                "- **TVP** et **EP** = deux présentations cliniques de la **MTEV** "
                "(maladie thromboembolique veineuse)\n"
                "- Mêmes facteurs prédisposants pour les deux entités\n"
                "- EP secondaire à une TVP dans 70 % des cas"
            )),
            FicheRow(concept="◆ TVP — définition et topographie", detail_md=(
                "- Obstruction thrombotique d'un tronc veineux profond, le plus souvent aux "
                "**membres inférieurs**\n"
                "- **TVP proximales** : veine poplitée, fémorale, iliaque ou cave\n"
                "- **TVP distales** : veines jambières (tibiale postérieure, fibulaire) et surales "
                "(soléaire, gastrocnémienne)\n"
                "- Risque d'EP beaucoup plus important si TVP proximale que distale"
            )),
            FicheRow(concept="◆ EP — définition", detail_md=(
                "- Obstruction des artères pulmonaires ou de leurs branches par des thrombi\n"
                "- 50 % des patients ayant une TVP proximale ont aussi une EP à l'angioscanner "
                "(souvent cliniquement asymptomatique)"
            )),
            FicheRow(concept="Objectifs de la prise en charge", detail_md=(
                "- **TVP** : prévenir l'EP (précoce) et le **syndrome post-thrombotique** (tardif)\n"
                "- **EP** : diminuer mortalité, morbidité, risque de cœur pulmonaire postembolique "
                "et de récidive"
            )),
            FicheRow(concept="", detail_md=(
                "- TVP et EP = **même maladie (MTEV)** avec deux expressions cliniques\n"
                "- 70 % des EP sont secondaires à une TVP"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="B", titre="Épidémiologie", rows=[
            FicheRow(concept="Incidence de la MTEV", detail_md=(
                "- Incidence **MTEV ≈ 1,83 / 1 000 / an** (étude franco-britannique)\n"
                "- Incidence **EP ≈ 0,60 / 1 000 / an**\n"
                "- Environ 100 000 cas / an en France"
            )),
            FicheRow(concept="◆ Mortalité", detail_md=(
                "- EP = **3e cause de décès** après maladies cardiovasculaires et cancer\n"
                "- 5 000 à 10 000 décès / an en France"
            )),
            FicheRow(concept="Prévalence autopsique", detail_md=(
                "- 20 à 40 % dans les études d'autopsie\n"
                "- Stable dans le temps malgré la réduction des TVP postopératoires "
                "(grâce aux mesures prophylactiques)\n"
                "- Lié à l'augmentation de l'espérance de vie et aux polypathologies"
            )),
        ]),
        SousPartie(lettre="C", titre="Facteurs prédisposants", rows=[
            FicheRow(concept="◆ Facteurs temporaires MAJEURS (3 derniers mois)", detail_md=(
                "- **Chirurgie avec AG > 30 min** dans les 3 derniers mois\n"
                "- **Fracture des membres inférieurs** dans les 3 derniers mois\n"
                "- **Immobilisation > 3 jours** pour motif médical aigu\n"
                "- Contraception œstroprogestative, grossesse, post-partum, "
                "traitement hormonal de la ménopause"
            )),
            FicheRow(concept="Facteurs temporaires MINEURS (2 derniers mois)", detail_md=(
                "- Chirurgie avec AG < 30 min dans les 2 derniers mois\n"
                "- Traumatisme d'un membre inférieur non plâtré avec mobilité réduite ≥ 3 jours\n"
                "- Immobilisation < 3 jours pour motif médical aigu\n"
                "- Voyage > 6 heures"
            )),
            FicheRow(concept="◆ Facteurs permanents", detail_md=(
                "- **Cancer actif**\n"
                "- **Maladies inflammatoires chroniques** digestives ou articulaires "
                "(Crohn, rectocolite hémorragique)"
            )),
            FicheRow(concept="Notion de MTEV provoquée vs non provoquée", detail_md=(
                "- **MTEV provoquée** : facteurs transitoires (postopératoire, obstétrical, médical)\n"
                "  - TVP plus fréquente en postopératoire de chirurgie orthopédique que générale\n"
                "  - Risque postopératoire élevé pendant 2 semaines, reste haut pendant 2 à 3 mois\n"
                "- **MTEV non provoquée** : facteurs persistants propres au patient "
                "(cliniques, biologiques, prédispositions génétiques)"
            )),
            FicheRow(concept="", detail_md=(
                "- Niveau de risque = facteurs liés au patient + contexte de survenue\n"
                "- Distinction provoquée / non provoquée conditionne la **durée du traitement**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="D", titre="Physiopathologie", rows=[
            FicheRow(concept="◆ Triade de Virchow", detail_md=(
                "- **Stase veineuse**\n"
                "- **Lésions pariétales**\n"
                "- **Anomalies de l'hémostase**\n"
                "- Point de départ le plus souvent distal dans les zones de ralentissement du flux "
                "(veines soléaires, valvules, abouchement de collatérales)"
            )),
            FicheRow(concept="Évolution du thrombus", detail_md=(
                "- Aggravation de l'obstruction et/ou extension\n"
                "- Migration embolique possible\n"
                "- Lyse spontanée si thrombus peu volumineux et facteur étiologique disparaissant "
                "rapidement\n"
                "- Sous traitement : recanalisation progressive avec séquelles possibles "
                "(thrombus résiduel, épaississement pariétal, reflux veineux profond)"
            )),
            FicheRow(concept="◆ EP — conséquences hémodynamiques", detail_md=(
                "- Apparition des symptômes quand **30-50 % du lit artériel pulmonaire** occlus\n"
                "- Augmentation rapide des résistances artérielles pulmonaires → mort subite, "
                "HTAP, **cœur pulmonaire aigu** (dilatation VD)\n"
                "- Septum paradoxal avec baisse du débit cardiaque systémique → dysfonction VG\n"
                "- En l'absence de dysfonction VD : compensation par stimulation sympathique "
                "(augmentation des PAP) et vasoconstriction systémique (stabilisation de la PA)"
            )),
            FicheRow(concept="Seconde phase hémodynamique (24-48 h)", detail_md=(
                "- Possible par embolies récurrentes et/ou aggravation de la dysfonction VD\n"
                "- Augmentation de la demande en O₂ du VD + baisse de la perfusion coronarienne "
                "droite → **ischémie VD**\n"
                "- Issue possiblement fatale\n"
                "- Une pathologie cardiovasculaire préexistante altère le pronostic"
            )),
            FicheRow(concept="Conséquences respiratoires", detail_md=(
                "- **Hypoxie** par : modification du rapport ventilation/perfusion (effet shunt), "
                "baisse du débit cardiaque, shunt droite-gauche sur **foramen ovale perméable** "
                "(plus rare)\n"
                "- Embolies distales : hémorragies intra-alvéolaires → hémoptysies, "
                "épanchement pleural, **infarctus pulmonaire**"
            )),
            FicheRow(concept="", detail_md=(
                "- Une diminution de la PA systémique altère le débit coronarien et la fonction VG : "
                "spirale délétère\n"
                "- **30-50 % d'obstruction** = seuil d'apparition des symptômes"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="E", titre="Histoire naturelle", rows=[
            FicheRow(concept="Classification des TVP", detail_md=(
                "- Selon localisation : distale (sous-poplitée) vs proximale (sus-poplitée)\n"
                "- Selon expression clinique : asymptomatique, TVP ou EP symptomatique, SPT"
            )),
            FicheRow(concept="◆ Évolution des TVP distales", detail_md=(
                "- Asymptomatiques (postopératoires) : plus fréquentes après chirurgie orthopédique\n"
                "- **Extension proximale dans 20 %** des cas\n"
                "- Symptomatiques : récidive dans 30 % des cas sans traitement, "
                "9 % à 3 mois après 6 semaines d'anticoagulation\n"
                "- Anticoagulation recommandée dès qu'elles sont mises en évidence"
            )),
            FicheRow(concept="◆ TVP proximales symptomatiques", detail_md=(
                "- Risque évolutif extrême\n"
                "- Nécessitent une **anticoagulation précoce et adéquate**"
            )),
            FicheRow(concept="Syndrome post-thrombotique (SPT)", detail_md=(
                "- Incidence en diminution grâce à une meilleure prise en charge\n"
                "- Délai d'apparition plus précoce : moyenne dans les 2 premières années\n"
                "- **Contention veineuse** dès la phase initiale et pendant au moins 3 mois : "
                "réduit de 50 % le risque de SPT"
            )),
            FicheRow(concept="◆ EP — données évolutives", detail_md=(
                "- Survenue 3 à 7 jours après le début d'une TVP\n"
                "- **Mortelle dans 10 %** des cas dès la 1re heure\n"
                "- EP avec choc ou hypotension : 5-10 % des cas\n"
                "- Signes biologiques ou échographiques de gravité : 50 % des cas\n"
                "- Reperfusion pulmonaire complète chez 2/3 des patients après EP\n"
                "- **> 90 % des décès** : diagnostic de MTEV non porté\n"
                "- HTP postembolique chronique : 0,5-5 % des patients traités"
            )),
            FicheRow(concept="Récidives", detail_md=(
                "- Souvent de même nature que le premier épisode (TVP ou EP)\n"
                "- Plus fréquentes en cas de **MTEV non provoquée**\n"
                "- Sans anticoagulation : 50 % de récidive dans les 3 mois\n"
                "- Récidive à 1 an : 9 % (non provoquée) vs 3 % (provoquée)"
            )),
            FicheRow(concept="", detail_md=(
                "- Une TVP distale apparemment isolée doit être anticoagulée (extension proximale 20 %)\n"
                "- > 90 % des décès par EP surviennent faute de diagnostic"
            ), kind="piege"),
        ]),
    ])

    # PARTIE II : Thrombose veineuse profonde
    partie_ii = Partie(numero="II", titre="Thrombose veineuse profonde", sous_parties=[
        SousPartie(lettre="A", titre="Diagnostic clinique", rows=[
            FicheRow(concept="◆ Valeur de la clinique", detail_md=(
                "- Interrogatoire + examen clinique + recherche de contexte thrombogène : "
                "**valeur d'orientation uniquement**\n"
                "- Ne permet pas de confirmer le diagnostic"
            )),
            FicheRow(concept="Signes évocateurs", detail_md=(
                "- Douleur spontanée ou provoquée du membre inférieur\n"
                "- Œdème unilatéral de la jambe ou de l'ensemble du MI, d'autant plus étendu que la "
                "TV est proximale (**différence de circonférence > 3 cm** avec le MI controlatéral)\n"
                "- Signes inflammatoires\n"
                "- Dilatation des veines superficielles"
            )),
            FicheRow(concept="Phlegmatia alba dolens", detail_md=(
                "- Tableau le plus évocateur de TVP des MI\n"
                "- Atteinte typiquement unilatérale ou asymétrique\n"
                "- Plus évocatrice si survenue brutale"
            )),
            FicheRow(concept="Formes asymptomatiques", detail_md=(
                "- La TVP peut être totalement asymptomatique\n"
                "- Découverte alors dans le bilan d'une EP"
            )),
            FicheRow(concept="Diagnostic différentiel clinique", detail_md=(
                "- Lésion musculaire ou tendineuse (traumatisme, claquage)\n"
                "- Affection ostéoarticulaire (kyste synovial)\n"
                "- SPT, insuffisance veineuse primaire\n"
                "- Sciatique, compression extrinsèque (adénopathie, tumeur, utérus gravide)\n"
                "- Érysipèle, lymphangite, cellulite\n"
                "- Lymphœdème\n"
                "- Insuffisance cardiaque droite, rénale ou hépatique"
            )),
            FicheRow(concept="", detail_md=(
                "- La clinique seule ne suffit JAMAIS au diagnostic de TVP\n"
                "- Un œdème bilatéral oriente vers une cause systémique (insuffisance cardiaque, rénale)"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Score de Wells et D-dimères", rows=[
            FicheRow(concept="◆ Score de Wells (TVP)", detail_md=(
                "- Score clinique pour patients hospitalisés ou ambulatoires\n"
                "- Classe l'épisode en probabilité **faible (3 %)**, **intermédiaire (17 %)** "
                "ou **forte (75 %)** de TVP\n"
                "- Analyse a priori avant les tests paracliniques\n"
                "- Renforce la valeur des tests lorsqu'elle va dans le même sens"
            )),
            FicheRow(concept="◆ D-dimères — généralités", detail_md=(
                "- Produits de dégradation **spécifiques de la fibrine**\n"
                "- Issus de la formation puis de la lyse d'un thrombus évolutif\n"
                "- Dosage par méthode **Elisa** (sensibilité > 95 %) ou méthode latex\n"
                "- En cas de test négatif Elisa : risque d'erreur < 5 % (VPN > 95 %)"
            )),
            FicheRow(concept="Faible spécificité des D-dimères", detail_md=(
                "- Élevés également dans : âge avancé, inflammation, cancer, "
                "traumatisme, hématome, postopératoire, grossesse, post-partum"
            )),
            FicheRow(concept="◆ Utilisation pratique des D-dimères", detail_md=(
                "- **Seuil < 500 ng/mL** : test Elisa rapide\n"
                "- Utiles pour éliminer le diagnostic\n"
                "- Si test positif → recours à l'échodoppler veineux pour confirmer\n"
                "- Tenir compte du niveau de probabilité clinique pour demander et interpréter"
            )),
            FicheRow(concept="", detail_md=(
                "- D-dimères = **test d'exclusion** (VPN forte), pas un test de confirmation\n"
                "- Toujours interpréter en fonction du score de probabilité"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Échodoppler veineux et stratégie", rows=[
            FicheRow(concept="◆ Échodoppler veineux des MI", detail_md=(
                "- Examen de **1re intention** pour confirmer ou infirmer le diagnostic de TVP\n"
                "- **Sensibilité et spécificité > 95 %**\n"
                "- Exploration morphologique (échographie) et hémodynamique (doppler)"
            )),
            FicheRow(concept="Technique de l'examen", detail_md=(
                "- Axe veineux observé en coupe transversale puis longitudinale, sous compression\n"
                "- De la veine cave inférieure jusqu'aux veines distales\n"
                "- Système profond et superficiel\n"
                "- Doppler aux confluents (fémoro-iliaque, poplité)\n"
                "- Doppler couleur pour territoires de repérage difficile"
            )),
            FicheRow(concept="Critères d'une veine normale", detail_md=(
                "- Absence de matériel endoluminal\n"
                "- Compressibilité sous la sonde\n"
                "- Signal doppler rythmé par la respiration et augmenté par la chasse veineuse "
                "manuelle"
            )),
            FicheRow(concept="◆ Critères de TVP", detail_md=(
                "- **Image directe du thrombus** : signe très fréquent et spécifique\n"
                "- **Incompressibilité** de la veine à la pression sous la sonde "
                "(limitée aux axes fémoral et poplité, examen rapide)\n"
                "- Modifications du signal doppler : diminution ou abolition du signal spontané ou "
                "provoqué\n"
                "- En doppler couleur : remplissage partiel ou absent au sein du thrombus\n"
                "- Signes indirects : calibre veineux, cinétique paroi/valvules, circulation collatérale"
            )),
            FicheRow(concept="Limites de l'échodoppler", detail_md=(
                "- Exigences d'appareillage (haute résolution, sonde adaptée)\n"
                "- Exigences d'opérateur (expérimenté)\n"
                "- Conditions techniques optimales (absence de contractions musculaires)"
            )),
            FicheRow(concept="Examens d'appoint", detail_md=(
                "- **Phlébographie** : plus utilisée (60 mL d'iode dans veine dorsale du pied + garrots)\n"
                "  - Critères : lacune (image radioclaire) et arrêt en cupule\n"
                "  - Coûteuse, peu confortable, contre-indications à respecter\n"
                "- **Angioscanner abdominopelvien** : complément si l'échodoppler ne conclut pas"
            )),
            FicheRow(concept="Stratégie diagnostique TVP", detail_md=(
                "| Probabilité clinique | Conduite |\n"
                "|----------------------|---------|\n"
                "| **Faible / intermédiaire** | D-dimères : si **négatifs** → exclut TVP ; "
                "si **positifs** → échodoppler |\n"
                "| **Forte** | Échodoppler **d'emblée** |"
            )),
        ]),
        SousPartie(lettre="D", titre="Diagnostic étiologique", rows=[
            FicheRow(concept="Facteur déclenchant transitoire", detail_md=(
                "- Chirurgie ou fracture des MI dans les 3 mois\n"
                "- Immobilisation > 3 jours\n"
                "- → TVP **provoquée**\n"
                "- En l'absence de ces facteurs : TVP **non provoquée** → bilan étiologique"
            )),
            FicheRow(concept="★ ◆ Bilan de thrombophilie — indications", detail_md=(
                "- **PAS de bilan systématique** après un 1er épisode de MTEV\n"
                "- Pas de bilan chez patients ayant un 1er épisode de TVP proximale ou d'EP "
                "après 50 ans, provoquée ou non\n"
                "- **À RÉALISER** si :\n"
                "  - 1er épisode TVP proximale / EP non provoqué, avant 50 ans, avec ATCD familial "
                "au 1er degré\n"
                "  - MTEV récidivant (≥ 1 TVP proximale ou EP + ≥ 1 épisode non provoqué avant 50 ans)\n"
                "  - Thrombose non provoquée en site atypique (splanchnique, MS, cérébral)\n"
                "- Sinon : avis d'un centre expert multidisciplinaire"
            )),
            FicheRow(concept="Anomalies recherchées", detail_md=(
                "- Déficits en **AT** (antithrombine), **PC** et **PS** (protéines C et S)\n"
                "- Mutations : **Leiden du FV** et **G20210A du FII**\n"
                "- Bilan entre 3 et 6 mois après le diagnostic, après **arrêt 72 h des AOD**"
            )),
            FicheRow(concept="★ ◆ Thrombophilies acquises (SAPL)", detail_md=(
                "- **Syndrome des antiphospholipides**\n"
                "- Anticoagulants circulants\n"
                "- Ac anticardiolipines IgG et IgM\n"
                "- Ac anti-β2GP1 IgG et IgM"
            )),
            FicheRow(concept="Bilan chez les apparentés", detail_md=(
                "- Indiqué si thrombophilie sévère chez le propositus "
                "(déficit AT/PC/PS, double hétérozygote, homozygote FV/FII)\n"
                "- À adresser dans un centre expert agréé\n"
                "- Limité en 1re intention à l'anomalie identifiée chez le propositus"
            )),
            FicheRow(concept="◆ Recherche d'une néoplasie", detail_md=(
                "- Incidence cancer associée à TVP : 6 à 28 %\n"
                "- Risque plus élevé en cas de TVP idiopathique ou récidivante\n"
                "- Surtout dans les 6-12 premiers mois\n"
                "- Bilan **après 40 ans** ou si bilan de thrombophilie négatif"
            )),
            FicheRow(concept="Examens du bilan néoplasique", detail_md=(
                "- Homme : PSA\n"
                "- Femme : examen gynécologique, mammographie, échographie pelvienne\n"
                "- Les deux sexes : recherche de sang dans les selles, radiographie thoracique\n"
                "- Endoscopies digestives, écho abdominopelvienne, bodyscanner : non systématiques, "
                "utiles si signes d'orientation\n"
                "- Surveillance clinique répétée sur au moins 1 an"
            )),
            FicheRow(concept="", detail_md=(
                "- Sous héparine : dosage antithrombine perturbé, anticoagulant lupique perturbé\n"
                "- Sous AVK : dosages PC et PS modifiés\n"
                "- FVIII : perturbé par l'inflammation\n"
                "- Œstrogènes / grossesse : modifient AT, FVIII, PS, RPCA\n"
                "- AOD : modifient anticoagulants circulants et déficits en inhibiteurs"
            ), kind="piege"),
        ]),
        SousPartie(lettre="E", titre="Formes particulières et complications", rows=[
            FicheRow(concept="◆ TVP distales", detail_md=(
                "- Si diagnostiquées, prises en charge comme une TVP proximale"
            )),
            FicheRow(concept="Thromboses veineuses superficielles (TVS)", detail_md=(
                "- Siège habituel : trajet de la grande veine saphène\n"
                "- Douleur, rougeur, inflammation, cordon induré\n"
                "- Échodoppler : confirme, localise, vérifie l'extension au réseau profond "
                "(**TVP associée dans 10 %**)\n"
                "- TVS sur veines saines non variqueuses : rechercher cancer, Buerger, Behçet, "
                "hémopathie, auto-immune, thrombophilie"
            )),
            FicheRow(concept="TVP pelviennes", detail_md=(
                "- Utéro-ovariennes, hypogastriques\n"
                "- Signes urinaires, utéro-vaginaux, digestifs (douleurs abdominales, masse "
                "sensible du flanc, iléus), tableau fébrile voire septique\n"
                "- Contextes : prostatectomie, hystérectomie, grossesse, post-partum"
            )),
            FicheRow(concept="Thrombose de la veine cave inférieure", detail_md=(
                "- Typiquement **signes bilatéraux** d'emblée ou par alternance\n"
                "- Possibilité de signes unilatéraux et découverte aux explorations\n"
                "- Rechercher malformation veineuse congénitale\n"
                "- VCI sus-rénale : thromboses néoplasiques par extension d'un cancer du rein\n"
                "- Hospitalisation initiale justifiée"
            )),
            FicheRow(concept="TVP au cours de la grossesse", detail_md=(
                "- Signes cliniques difficiles à interpréter (stase veineuse physiologique)\n"
                "- Échodoppler : test habituel, souvent suffisant (peut être gêné au niveau iliocave)\n"
                "- **Bilan de thrombophilie systématique** chez femme en âge de procréer avec ATCD "
                "personnels/familiaux de MTEV"
            )),
            FicheRow(concept="MTEV et cancer", detail_md=(
                "- Témoin de l'activité de la maladie cancéreuse\n"
                "- À traiter par **HBPM au long cours**"
            )),
            FicheRow(concept="⚠ Phlegmatia caerulea (phlébite bleue)", detail_md=(
                "- Très rare mais grave\n"
                "- Associe **signes d'ischémie** (à la douleur et à l'œdème), cyanose, "
                "parfois état de choc\n"
                "- Ischémie liée à : importance de l'obstruction, étendue de la TV, œdème compressif, "
                "spasme"
            )),
            FicheRow(concept="Complications de la TVP", detail_md=(
                "- Évolution favorable sans séquelle sous traitement bien conduit (le plus souvent)\n"
                "- Récidive : toujours présente, surtout si facteur permanent\n"
                "- **Syndrome post-thrombotique** :\n"
                "  - Lourdeur de jambe, dilatations veineuses superficielles, œdème de cheville\n"
                "  - Troubles trophiques sans ulcère (hypodermite, dermite ocre, atrophie "
                "blanche)\n"
                "  - Ulcères sus-malléolaires\n"
                "  - Claudication veineuse de cuisse (exceptionnelle)\n"
                "- EP (cf. partie III)"
            )),
        ]),
    ])

    # PARTIE III : Embolie pulmonaire - diagnostic
    partie_iii = Partie(numero="III", titre="Embolie pulmonaire — diagnostic", sous_parties=[
        SousPartie(lettre="A", titre="Clinique et examens standards", rows=[
            FicheRow(concept="★ ◆ Triade clinique évocatrice (90 % des EP)", detail_md=(
                "- **Dyspnée** : brutale ou progressive sur plusieurs semaines, ou aggravation d'une "
                "dyspnée chronique\n"
                "- **Douleur thoracique** : typiquement pleurale (point de côté brutal) ; "
                "douleur prolongée si irritation pleurale (embolies distales)\n"
                "- **Syncope** : rare mais témoigne d'une réduction sévère du flux systémique"
            )),
            FicheRow(concept="Autres signes", detail_md=(
                "- Crachats hémoptoïques : infarctus pulmonaire\n"
                "- EP asymptomatique : non rare\n"
                "- 20 à 30 % des EP sont spontanées ou idiopathiques"
            )),
            FicheRow(concept="Examen clinique", detail_md=(
                "- Tachycardie\n"
                "- Signes de retentissement hémodynamique : hypotension, signes d'insuffisance "
                "cardiaque droite\n"
                "- Recherche de signes de TVP associée (souvent négative)"
            )),
            FicheRow(concept="Radiographie thoracique", detail_md=(
                "- Habituellement anormale mais signes aspécifiques\n"
                "- Atélectasies en bande, épanchement pleural, élévation d'une coupole "
                "diaphragmatique, opacité triangulaire à base pleurale (infarctus), "
                "élargissement des artères pulmonaires\n"
                "- Utile pour éliminer une autre cause de dyspnée\n"
                "- **Une radiographie normale n'élimine pas le diagnostic d'EP**"
            )),
            FicheRow(concept="Gazométrie artérielle", detail_md=(
                "- **Hypoxémie + hypocapnie** (effet shunt paradoxal)\n"
                "- Normale dans 20 % des cas\n"
                "- Quasiment plus pratiquée sauf si **SaO₂ < 90 %** en air ambiant"
            )),
            FicheRow(concept="★ ◆ ECG", detail_md=(
                "- Normal ou tachycardie sinusale\n"
                "- Signes de **souffrance VD** :\n"
                "  - **Aspect S1Q3** (onde S en D1, onde Q en D3) → déviation axiale droite\n"
                "  - BBD complet ou incomplet\n"
                "  - Arythmie supraventriculaire\n"
                "  - **Inversion des ondes T de V1 à V4** (ischémie VD)\n"
                "- Peut faussement orienter vers un SCA"
            )),
            FicheRow(concept="", detail_md=(
                "- Les signes cliniques et examens de routine précisent la suspicion mais "
                "ne confirment ni n'éliminent une EP\n"
                "- Évoquer une EP devant toute dyspnée, douleur thoracique ou syncope inexpliquée"
            ), kind="a_retenir"),
            FicheRow(concept="", detail_md=(
                "- ECG d'EP peut mimer un SCA (T négatives V1-V4) — attention au piège diagnostique"
            ), kind="piege"),
        ]),
        SousPartie(lettre="B", titre="Scores de probabilité", rows=[
            FicheRow(concept="◆ Deux scores validés", detail_md=(
                "- **Score de Wells simplifié**\n"
                "- **Score révisé de Genève**\n"
                "- Permettent d'estimer la probabilité d'EP avant tout examen paraclinique complexe"
            )),
            FicheRow(concept="Probabilité estimée", detail_md=(
                "| Niveau de suspicion | Probabilité d'EP |\n"
                "|---------------------|------------------|\n"
                "| Faible | **10 %** |\n"
                "| Modérée | **30 %** |\n"
                "| Forte | **65 %** |"
            )),
            FicheRow(concept="Diagnostic différentiel de l'EP", detail_md=(
                "- Devant une douleur thoracique : infarctus du myocarde, péricardite, "
                "dissection aortique, pneumothorax\n"
                "- Devant une dyspnée aiguë : OAP, crise d'asthme, décompensation de BPCO, "
                "pneumopathie"
            )),
        ]),
        SousPartie(lettre="C", titre="Examens paracliniques", rows=[
            FicheRow(concept="★ ◆ D-dimères dans l'EP", detail_md=(
                "- Très spécifiques de la fibrine\n"
                "- Élevés si caillot aigu (coagulation + fibrinolyse simultanées)\n"
                "- **VPN forte** : taux normal → MTEV peu probable\n"
                "- VPP faible : élevés dans âge, cancer, inflammation, infection, nécrose, "
                "dissection aortique, grossesse\n"
                "- Test **Elisa** : sensibilité > 95 %, spécificité 40 %\n"
                "- **Seuil = 500 µg/L**\n"
                "- **Adapter à l'âge après 50 ans** : âge × 10 (probabilité faible ou intermédiaire)"
            )),
            FicheRow(concept="Quand demander les D-dimères ?", detail_md=(
                "- Utiles : probabilité faible ou intermédiaire\n"
                "- Inutiles : probabilité forte → **angioscanner d'emblée**"
            )),
            FicheRow(concept="★ ◆ Angioscanner pulmonaire", detail_md=(
                "- **Examen le plus performant** (scanners multibarrettes)\n"
                "- **Sensibilité 83 %, spécificité > 90 %** (4 barrettes)\n"
                "- Angioscanner négatif exclut une EP si probabilité faible ou intermédiaire\n"
                "- Si probabilité forte + scanner négatif : autre examen (scintigraphie, "
                "voire angiographie)"
            )),
            FicheRow(concept="Échodoppler veineux des MI", detail_md=(
                "- Origine de la TVP au niveau des MI dans 90 % des EP\n"
                "- Sensibilité > 90 %, spécificité ≈ 95 %\n"
                "- EDV retrouve une TVP dans 30-50 % des EP\n"
                "- **TVP proximale = suffisante** pour confirmer le diagnostic et traiter\n"
                "- TVP distale : pas suffisante → autres examens\n"
                "- **EDV normal n'élimine pas l'EP**\n"
                "- Sert aussi à évaluer le risque de récidive"
            )),
            FicheRow(concept="Scintigraphie pulmonaire V/Q", detail_md=(
                "- Tc99m couplé à albumine (perfusion) + traceur inhalé (ventilation)\n"
                "- En cas d'EP : **défaut de perfusion + ventilation normale** "
                "(mismatch ventilation-perfusion)\n"
                "- Limité si pathologie cardiorespiratoire (ventilation perturbée)\n"
                "- 3 niveaux : élevée, non diagnostique, normale\n"
                "- **Scintigraphie normale + probabilité faible = exclusion d'EP**\n"
                "- Scintigraphie positive + probabilité faible = autres examens"
            )),
            FicheRow(concept="★ ◆ Échocardiographie transthoracique (ETT)", detail_md=(
                "- Signes indirects : **dilatation VD**, septum paradoxal, hypokinésie VD, "
                "élévation des PAP\n"
                "- Plus rarement : thrombus dans les cavités droites ou les troncs pulmonaires\n"
                "- Réalisable au lit du patient\n"
                "- En **EP grave** (choc / hypotension) si angioscanner indisponible ou patient "
                "instable :\n"
                "  - Élimine autres causes de choc cardiogénique\n"
                "  - Signes de surcharge VD : suffisants pour diagnostic + **fibrinolyse en urgence**\n"
                "- En l'absence de choc : signes ETT = risque intermédiaire"
            )),
            FicheRow(concept="Examens abandonnés", detail_md=(
                "- Phléboscanner + angioscanner : étudié mais irradiation trop élevée\n"
                "- Angiographie pulmonaire conventionnelle : n'est plus pratiquée"
            )),
        ]),
        SousPartie(lettre="D", titre="Stratégie diagnostique", rows=[
            FicheRow(concept="◆ Distinction des deux algorithmes", detail_md=(
                "- **EP à haut risque** : choc ou hypotension persistante\n"
                "- **EP non à haut risque** : tous les autres cas\n"
                "- Stratégies diagnostiques et thérapeutiques différentes"
            )),
            FicheRow(concept="EP à haut risque", detail_md=(
                "- **Angioscanner d'emblée** pour confirmation\n"
                "- Si scanner indisponible ou patient instable : **ETT**\n"
                "  - Souffrance VD → diagnostic d'EP retenu → fibrinolyse\n"
                "  - ETT normale → choc d'autre étiologie"
            )),
            FicheRow(concept="EP non à haut risque", detail_md=(
                "| Probabilité (Wells/Genève) | Conduite |\n"
                "|----------------------------|---------|\n"
                "| **Faible / intermédiaire** | **D-dimères** : si négatifs → exclusion ; "
                "si positifs → angioscanner |\n"
                "| **Forte** | **Angioscanner d'emblée** |"
            )),
            FicheRow(concept="Place de l'EDV", detail_md=(
                "- En l'absence de scanner ou si contre-indication (insuffisance rénale, "
                "allergie à l'iode)\n"
                "- Pour apprécier le risque de récidive (EP avec TVP récidive plus que EP sans TVP)\n"
                "- Peut aider aussi dans les EP à haut risque"
            )),
            FicheRow(concept="", detail_md=(
                "- Score **Wells/Genève d'abord**, puis adapter examens selon probabilité\n"
                "- Reconnaître rapidement un état de choc ou une hypotension : guide la stratégie"
            ), kind="a_retenir"),
        ]),
    ])

    # PARTIE IV : EP - pronostic et formes
    partie_iv = Partie(numero="IV", titre="Embolie pulmonaire — pronostic et formes", sous_parties=[
        SousPartie(lettre="A", titre="Stratification du risque", rows=[
            FicheRow(concept="★ ◆ EP à HAUT RISQUE (mortalité > 15 %)", detail_md=(
                "- **État de choc** ou **hypotension artérielle** définie par :\n"
                "  - **PAS < 90 mmHg** ou\n"
                "  - **Baisse de la PAS > 40 mmHg pendant > 15 min**\n"
                "  - Sans cause rythmique, hypovolémique ou septique"
            )),
            FicheRow(concept="★ ◆ EP à risque intermédiaire (mortalité 3-15 %)", detail_md=(
                "- **Marqueurs de dysfonction VD** :\n"
                "  - ETT : dilatation VD, hypokinésie, rapport VD/VG augmenté, augmentation "
                "de la vitesse du flux d'IT (au moins 25 % des cas)\n"
                "  - Angioscanner : rapport diamètres VD/VG augmenté\n"
                "  - Autres : distension des veines jugulaires, souffle d'IT, signes ECG "
                "(T négatives V1-V4, S1Q3, BBD)\n"
                "- **Marqueurs d'ischémie myocardique** : troponine T ou I corrélée à l'ischémie VD"
            )),
            FicheRow(concept="Foramen ovale perméable et thrombus intracardiaques", detail_md=(
                "- Foramen ovale perméable : peut aggraver l'hypoxie\n"
                "- Thrombus dans les cavités droites : associé à augmentation du risque de récidive"
            )),
            FicheRow(concept="★ ◆ Score PESI simplifié (sPESI)", detail_md=(
                "- **1 point pour chaque item présent** :\n"
                "  - Âge > 80 ans\n"
                "  - SaO₂ < 90 %\n"
                "  - PAS < 100 mmHg\n"
                "  - FC > 110 bpm\n"
                "  - Cancer\n"
                "  - Insuffisance cardiaque ou maladie pulmonaire chronique\n"
                "- **Mnémo : 80, 90, 100, 110**\n"
                "- **Score 0** : mortalité 1 %\n"
                "- **Score ≥ 1** : mortalité ≈ 10 %"
            )),
            FicheRow(concept="Autres signes de gravité", detail_md=(
                "- Âge élevé, sexe masculin\n"
                "- Cancer, insuffisance cardiaque, pathologie pulmonaire chronique\n"
                "- Tachycardie > 110 bpm, PAS < 100 mmHg, FR ≥ 30 / min\n"
                "- Hypothermie < 36 °C\n"
                "- Trouble de conscience\n"
                "- SaO₂ < 90 %"
            )),
            FicheRow(concept="Classification finale ESC 2019", detail_md=(
                "| Catégorie | Définition |\n"
                "|-----------|-----------|\n"
                "| **Haut risque** | Choc / hypotension persistante |\n"
                "| **Risque intermédiaire haut** | PESI ≥ 1 + ≥ 2 signes de souffrance VD "
                "(écho, BNP ou tropo) |\n"
                "| **Risque intermédiaire faible** | PESI ≥ 1 + ≤ 1 signe de souffrance VD |\n"
                "| **Bas risque** | PESI = 0 |"
            )),
        ]),
        SousPartie(lettre="B", titre="Évolution et complications", rows=[
            FicheRow(concept="Évolution favorable", detail_md=(
                "- Le plus souvent favorable sous traitement"
            )),
            FicheRow(concept="◆ Complications de l'EP", detail_md=(
                "- **Choc cardiogénique réfractaire** → décès (court terme)\n"
                "- Récidive (court et moyen terme)\n"
                "- **HTAP chronique postembolique** : rare mais grave (moyen terme) si persistance "
                "d'obstruction significative"
            )),
            FicheRow(concept="HTAP postembolique", detail_md=(
                "- Complication rare mais grave\n"
                "- **Endartériectomie pulmonaire** : bons résultats par équipes entraînées\n"
                "- Traitement de choix\n"
                "- Avant d'arrêter un traitement anticoagulant, toujours éliminer une HTP postembolique"
            )),
        ]),
        SousPartie(lettre="C", titre="Formes cliniques particulières", rows=[
            FicheRow(concept="EP au cours du cancer", detail_md=(
                "- Cf. partie TVP : traitement par **HBPM au long cours**"
            )),
            FicheRow(concept="◆ EP au cours de la grossesse", detail_md=(
                "- D-dimères faussement positifs\n"
                "- **EDV en 1re intention**\n"
                "- Si non contributif : scanner ou scintigraphie possibles sans risque fœtal\n"
                "- HBPM dès confirmation diagnostique\n"
                "- **AVK non recommandées** aux 1er et 3e trimestres"
            )),
            FicheRow(concept="Thrombus intracardiaques", detail_md=(
                "- Surtout si mobiles\n"
                "- **Haut risque de mortalité précoce**\n"
                "- Traitement urgent recommandé\n"
                "- Place de la thrombolyse ou embolectomie non encore bien validée"
            )),
            FicheRow(concept="EP non thrombotiques", detail_md=(
                "- Septique, gazeuse, graisseuse, amniotique, tumorale\n"
                "- Prise en charge par traitement étiologique"
            )),
        ]),
    ])

    # PARTIE V : Traitement curatif
    partie_v = Partie(numero="V", titre="Traitement curatif", sous_parties=[
        SousPartie(lettre="A", titre="Anticoagulation initiale", rows=[
            FicheRow(concept="◆ Objectifs du traitement", detail_md=(
                "- Améliorer les symptômes\n"
                "- Éviter l'extension et les récidives\n"
                "- Prévenir : EP, SPT, HTAP, EP fatale\n"
                "- Repose sur une **anticoagulation rapide et efficace**, identique TVP/EP"
            )),
            FicheRow(concept="Quand débuter le traitement ?", detail_md=(
                "- Diagnostic à confirmer en raison du risque hémorragique\n"
                "- En l'absence de risque hémorragique important : possible dès suspicion en cas "
                "de probabilité forte ou intermédiaire\n"
                "- Bilan préalable : hémogramme + plaquettes, TQ + TCA + fibrinogène, "
                "**créatininémie + DFG**"
            )),
            FicheRow(concept="◆ Options thérapeutiques initiales", detail_md=(
                "- **HNF** (héparine non fractionnée)\n"
                "- **HBPM** (héparine de bas poids moléculaire)\n"
                "- **Fondaparinux**\n"
                "- **AOD anti-Xa** (rivaroxaban, apixaban)\n"
                "- **Fibrinolytiques** si choc ou hypotension"
            )),
            FicheRow(concept="◆ HNF — modalités", detail_md=(
                "- Voie sous-cutanée ou IV continue\n"
                "- Posologie adaptée au poids : **500 UI/kg/j**\n"
                "- Surveillance par **TCA** (cible 1,5-2,5 × témoin) ou anti-Xa "
                "(cible 0,3-0,7 U)\n"
                "- Prélèvement TCA/anti-Xa :\n"
                "  - Entre 2 injections si SC\n"
                "  - 4 h après le début et 4 h après chaque modification si IV continue"
            )),
            FicheRow(concept="◆ HNF — indications spécifiques", detail_md=(
                "- **Insuffisance rénale sévère** (clairance < 30 mL/min)\n"
                "- Patients instables\n"
                "- Patients susceptibles de subir des interventions nécessitant un arrêt temporaire\n"
                "- Patients traités par **fibrinolyse**"
            )),
            FicheRow(concept="◆ HNF — TIH", detail_md=(
                "- Surveillance des **plaquettes 2 fois / semaine pendant 21 jours**\n"
                "- TIH : plaquettes **< 150 G/L** ou baisse **≥ 50 %** par rapport à l'avant-traitement\n"
                "- Numération plaquettaire AVANT tout traitement héparinique\n"
                "- Surveillance non nécessaire au-delà d'un mois"
            )),
            FicheRow(concept="★ ◆ HBPM — posologies (curatif)", detail_md=(
                "**2 injections SC / 24 h :**\n"
                "- **Daltéparine (Fragmine®)** : 100 UI/kg/12 h\n"
                "- **Nadroparine (Fraxiparine®)** : 85 UI/kg/12 h\n"
                "- **Énoxaparine (Lovenox®)** : 100 UI/kg/12 h (= 1 mg/kg/12 h)\n"
                "\n"
                "**1 injection SC / 24 h :**\n"
                "- **Nadroparine (Fraxodi®)** : 171 UI/kg/24 h\n"
                "- **Tinzaparine (Innohep®)** : 175 UI/kg/24 h\n"
                "\n"
                "AMM EP : énoxaparine et tinzaparine uniquement (mêmes posologies)"
            )),
            FicheRow(concept="Fondaparinux (Arixtra®)", detail_md=(
                "- 1 injection SC / 24 h\n"
                "- **7,5 mg / 24 h** pour un poids 50-100 kg"
            )),
            FicheRow(concept="HBPM / fondaparinux — surveillance", detail_md=(
                "- Pas de surveillance systématique de l'activité anti-Xa\n"
                "- Anti-Xa suggéré si risque d'accumulation : IR modéré, âge élevé, petit poids, "
                "obésité (4 h après initiation)\n"
                "- **Créatininémie** avant traitement (CI si **DFG < 30 mL/min**)\n"
                "- Plaquettes non systématiques sauf : MTEV postopératoire, HBPM après HNF, "
                "nouvel épisode thromboembolique, lésion cutanée douloureuse au site d'injection"
            )),
            FicheRow(concept="★ ◆ AOD anti-Xa — posologies", detail_md=(
                "- **Rivaroxaban (Xarelto®)** : 15 mg × 2/j × 21 j, puis 20 mg 1×/j\n"
                "- **Apixaban (Eliquis®)** : 10 mg × 2/j × 7 j, puis 5 mg × 2/j\n"
                "- Prescrits d'emblée, sans héparine préalable, sans relais AVK\n"
                "- Pas de surveillance biologique particulière\n"
                "- **Contre-indiqués si DFGe < 30 mL/min**\n"
                "- Référence dans la prise en charge de la MTEV"
            )),
            FicheRow(concept="◆ Thrombolytiques (fibrinolyse)", detail_md=(
                "- **Recommandés** dans l'EP grave (choc / hypotension sévère)\n"
                "- Non recommandés systématiquement dans l'EP de gravité intermédiaire\n"
                "- Si CI à la thrombolyse : **embolectomie en urgence**\n"
                "- TVP : non recommandés en 1re intention sauf syndrome obstructif sévère "
                "ou **phlegmatia caerulea** (sauvetage de membre)"
            )),
        ]),
        SousPartie(lettre="B", titre="Relais et durée du traitement", rows=[
            FicheRow(concept="◆ Relais par AVK", detail_md=(
                "- Recommandé après HNF, HBPM ou fondaparinux\n"
                "- **Démarrage dès le 1er jour** du traitement parentéral\n"
                "- Doses initiales :\n"
                "  - **Warfarine (Coumadine®) 5 mg**\n"
                "  - **Acénocoumarol (Sintrom®) 4 mg**\n"
                "  - Posologie plus faible chez le sujet âgé\n"
                "- **Fluindione (Préviscan®) déconseillée** par l'ANSM "
                "(risque d'atteinte rénale immuno-allergique)\n"
                "- Arrêt de l'HNF/HBPM/fondaparinux après **5 jours** ET **2 INR consécutifs > 2 à 24 h "
                "d'intervalle**"
            )),
            FicheRow(concept="Surveillance des AVK", detail_md=(
                "- **INR cible = 2,5** (intervalle 2-3)\n"
                "- À l'initiation : 2-3 fois / semaine\n"
                "- Stabilisation : toutes les 3-4 semaines\n"
                "- Éducation thérapeutique et carnet de suivi"
            )),
            FicheRow(concept="★ ◆ Durée d'anticoagulation — règles", detail_md=(
                "- **Minimum 3 mois** en cas de TVP proximale et/ou EP\n"
                "- Au-delà : prendre en compte localisation, contexte de survenue, risque "
                "hémorragique"
            )),
            FicheRow(concept="Durée selon le contexte", detail_md=(
                "| Situation | Durée |\n"
                "|-----------|-------|\n"
                "| TVP proximale ou EP + facteur transitoire majeur, ou **TVP distale** | **3 mois** |\n"
                "| TVP proximale ou EP **sans facteur transitoire majeur** | **6 mois** |\n"
                "| Facteur de risque **majeur persistant** ou récidive proximale | **> 6 mois / "
                "long cours** |\n"
                "| TVP proximale / EP **récidivantes**, **HTP postembolique** | **Au long cours** |\n"
                "| MTEV + **cancer actif** | **Prolongé tant que cancer actif** |"
            )),
            FicheRow(concept="Facteurs de risque majeurs persistants", detail_md=(
                "- **Thrombophilie majeure connue** : déficit en AT, FV Leiden homozygote, "
                "mutation homozygote prothrombine, thrombophilie multiple\n"
                "- Filtre cave permanent\n"
                "- HTAP\n"
                "- EP grave (associée à un état de choc)"
            )),
            FicheRow(concept="Suivi imagerie", detail_md=(
                "- Pas nécessaire sauf HTAP au cours de l'EP : contrôle de la PAP par "
                "ETT\n"
                "- Échodoppler veineux de contrôle en fin de traitement pour évaluer les séquelles"
            )),
            FicheRow(concept="", detail_md=(
                "- Avant d'arrêter un traitement anticoagulant : **toujours éliminer une HTP "
                "postembolique**"
            ), kind="a_retenir"),
        ]),
        SousPartie(lettre="C", titre="Compression et mobilisation", rows=[
            FicheRow(concept="◆ Compression veineuse élastique", detail_md=(
                "- **Chaussettes / bas de compression classe 3** (30-40 mmHg à la cheville)\n"
                "- Dès que possible après le diagnostic et l'instauration du traitement\n"
                "- Durée minimum 6 mois (ou plus si symptômes persistants)"
            )),
            FicheRow(concept="Mobilisation", detail_md=(
                "- Alitement systématique non recommandé\n"
                "- **Mobilisation précoce** (lever)\n"
                "- En cas d'EP : après **24 h d'anticoagulation efficace**"
            )),
            FicheRow(concept="◆ Contre-indications à la compression", detail_md=(
                "- **AOMI avec IPS < 0,6**\n"
                "- Microangiopathie diabétique pour pression > 30 mmHg\n"
                "- Phlegmatia caerulea dolens\n"
                "- Thrombose septique"
            )),
            FicheRow(concept="Traitement complémentaire EP grave / risque intermédiaire haut", detail_md=(
                "- Oxygénothérapie, voire ventilation invasive\n"
                "- Remplissage / inotropes\n"
                "- Surveillance USIC / réanimation (monitoring FC, PA, SaO₂)"
            )),
        ]),
        SousPartie(lettre="D", titre="Stratégies et cas particuliers", rows=[
            FicheRow(concept="◆ Indications d'hospitalisation pour TVP proximale", detail_md=(
                "- **Insuffisance rénale sévère** (clairance < 30 mL/min)\n"
                "- Anticoagulation + pathologie à risque hémorragique\n"
                "- TVP proximale avec syndrome obstructif sévère ou localisation iliocave\n"
                "- Contexte psychosocial / géographique / médical ne permettant pas une prise "
                "en charge à domicile\n"
                "- Sinon : HBPM ou AOD en ambulatoire ou après courte hospitalisation"
            )),
            FicheRow(concept="◆ Stratégie EP", detail_md=(
                "- **Hospitalisation = règle**\n"
                "- Peut être discutée dans les EP de faible gravité (**PESI = 0**) "
                "et en l'absence des autres facteurs\n"
                "- Si ambulatoire : diagnostic de certitude, éducation, surveillance organisée avec "
                "médecin traitant/IDE, évaluation des risques de récidive et hémorragique"
            )),
            FicheRow(concept="◆ TVP distales — traitement spécifique", detail_md=(
                "- Anticoagulation à dose curative suggérée\n"
                "- En phase initiale : HBPM ou fondaparinux préférables à l'HNF\n"
                "- Relais précoce par AVK\n"
                "- **AOD = traitement de référence**\n"
                "- **Durée** :\n"
                "  - **6 semaines** : 1er épisode + facteur déclenchant évident, "
                "sans facteur persistant\n"
                "  - **≥ 3 mois** : idiopathique, ou + facteur persistant, ou récidive, ou cancer\n"
                "- Contention élastique ≥ 2 ans si TVP étendue tibiales postérieures/fibulaires\n"
                "- Traitement ambulatoire sauf cas particulier"
            )),
            FicheRow(concept="Thromboses veineuses superficielles (TVS)", detail_md=(
                "**Non recommandés en 1re intention** :\n"
                "- AINS par voie générale (effet antalgique seulement par voie locale)\n"
                "- Anticoagulants à dose curative\n"
                "- Chirurgie sans atteinte de la jonction grandes saphènes – veines fémorales\n"
                "\n"
                "**Recommandés ou possibles** :\n"
                "- Compression (bandage) à la phase aiguë\n"
                "- Anticoagulation curative ou chirurgie si extension à la jonction "
                "grandes saphènes – veines fémorales\n"
                "- HBPM à dose prophylactique\n"
                "- **Fondaparinux à dose prophylactique × 6 semaines** (étude CALISTO)\n"
                "- Si anticoagulation : 7 à 30 jours"
            )),
            FicheRow(concept="◆ MTEV + cancer", detail_md=(
                "- AVK moins efficace, moins bien toléré que chez patients sans cancer\n"
                "- **HBPM = recommandées en relais**\n"
                "- Posologies évaluées :\n"
                "  - **Daltéparine** : 200 UI/kg 1×/j × 1 mois puis 150 UI/kg 1×/j\n"
                "  - **Tinzaparine** : 175 UI/kg 1×/j\n"
                "  - **Énoxaparine** : 150 UI/kg 1×/j\n"
                "- Thrombopénie chimio-induite (plaq < 50 G/L) : interrompre HBPM, reprise "
                "quand plaq remontées\n"
                "- Durée idéale : 3 à 6 mois selon tolérance et évolution\n"
                "- Au-delà de 6 mois :\n"
                "  - Cancer toujours traité + tolérance OK → poursuivre HBPM\n"
                "  - Sinon → relais AVK\n"
                "- AOD : possibles en 1re intention sauf cancers digestifs / génito-urinaires "
                "(risque hémorragique)"
            )),
            FicheRow(concept="MTEV chez la femme", detail_md=(
                "- En cas de MTEV : **contraception œstroprogestative arrêtée et contre-indiquée**\n"
                "- Alternatives : progestatif continu ou DIU\n"
                "- THM contre-indiqué\n"
                "- Grossesse : diagnostic difficile (axe iliocave peu accessible), traitement par "
                "**HBPM**"
            )),
            FicheRow(concept="TVP du membre supérieur", detail_md=(
                "- Souvent favorisée par matériel : cathéter central, sonde de pacemaker\n"
                "- Confirmation : échodoppler veineux ou scanner\n"
                "- Traitement identique à la TVP des MI"
            )),
        ]),
        SousPartie(lettre="E", titre="Filtre cave", rows=[
            FicheRow(concept="◆ Indications d'un filtre cave (temporaire ou permanent)", detail_md=(
                "- **Contre-indication au traitement anticoagulant**\n"
                "- **Récidive sous traitement bien conduit**\n"
                "- Suites d'une embolectomie pour embolie aiguë massive"
            )),
            FicheRow(concept="Filtre temporaire", detail_md=(
                "- À retirer lorsque la contre-indication aux anticoagulants n'a plus lieu d'être\n"
                "- Sinon : risque augmenté de récidive thrombotique"
            )),
            FicheRow(concept="", detail_md=(
                "- Un filtre cave laissé en place est lui-même thrombogène : retrait dès que possible"
            ), kind="piege"),
        ]),
    ])

    # PARTIE VI : Traitement préventif
    partie_vi = Partie(numero="VI", titre="Traitement préventif", sous_parties=[
        SousPartie(lettre="A", titre="Principes généraux", rows=[
            FicheRow(concept="◆ Principes de la prévention", detail_md=(
                "- Adapter au niveau de risque thrombotique et hémorragique et à la fonction "
                "rénale\n"
                "- Comprend :\n"
                "  - Mobilisation précoce\n"
                "  - Compression élastique\n"
                "  - Traitement injectable (parfois associé)\n"
                "- **L'aspirine n'est PAS indiquée** dans la prévention de la MTEV"
            )),
        ]),
        SousPartie(lettre="B", titre="Situations à risque", rows=[
            FicheRow(concept="Voyage > 6 heures", detail_md=(
                "- Ne pas porter de vêtements serrés\n"
                "- S'hydrater\n"
                "- Contraction active et régulière des mollets\n"
                "- Si facteurs prédisposants : chaussettes de contention classe 2 ou 3 "
                "± injection préventive d'HBPM avant le départ"
            )),
            FicheRow(concept="◆ Hospitalisation en milieu médical", detail_md=(
                "- Dépend de la pathologie, possibilité d'un lever précoce, terrain "
                "(âgé, cancer, ATCD MTEV, obésité)\n"
                "- Repose sur :\n"
                "  - **Énoxaparine 0,4 mL / 24 h SC**\n"
                "  - ou **Fondaparinux 2,5 mg / 24 h**"
            )),
            FicheRow(concept="◆ Intervention chirurgicale", detail_md=(
                "- Niveau de prévention selon type de chirurgie\n"
                "- Durée : couvrir toute la période d'immobilisation\n"
                "- **Chirurgie orthopédique lourde (prothèse de hanche)** : prolongée 4 à 6 semaines\n"
                "- **Prothèse de genou** : 10-15 jours\n"
                "- Médicaments : énoxaparine, fondaparinux ou AOD (protocoles établis "
                "en postopératoire)"
            )),
            FicheRow(concept="", detail_md=(
                "- **L'aspirine n'a aucune place** dans la prévention de la MTEV — c'est un piège classique"
            ), kind="piege"),
        ]),
    ])

    parties = [partie_i, partie_ii, partie_iii, partie_iv, partie_v, partie_vi]

    # TABLEAUX DE SYNTHESE
    tableaux = [
        TableauSynthese(titre="Score de Wells (TVP)", markdown=(
            "| Variable | Points |\n"
            "|----------|--------|\n"
            "| **Facteurs prédisposants** |  |\n"
            "| Parésie, paralysie ou immobilisation plâtrée récente d'un MI | 1 |\n"
            "| Chirurgie récente < 4 semaines ou alitement récent > 3 jours | 1 |\n"
            "| Cancer évolutif connu (traitement en cours, < 6 mois, ou palliatif) | 1 |\n"
            "| Antécédent de TVP (ou d'EP) | 1 |\n"
            "| **Signes cliniques** |  |\n"
            "| Sensibilité le long du trajet veineux profond | 1 |\n"
            "| Œdème généralisé du MI | 1 |\n"
            "| Œdème du mollet > 3 cm vs controlatéral (mesuré 10 cm sous tubérosité tibiale) | 1 |\n"
            "| Œdème unilatéral prenant le godet | 1 |\n"
            "| Circulation collatérale superficielle non variqueuse | 1 |\n"
            "| **Diagnostic différentiel de TVP au moins aussi probable** | **−2** |\n"
            "| **Interprétation** | **Score** |\n"
            "| **Faible** | 0 |\n"
            "| **Intermédiaire** | 1 ou 2 |\n"
            "| **Forte** | ≥ 3 |"
        )),
        TableauSynthese(titre="Scores de Genève révisé et de Wells (EP)", markdown=(
            "| Variable (Genève révisé) | Points | Variable (Wells) | Points |\n"
            "|--------------------------|--------|------------------|--------|\n"
            "| Âge > 65 ans | 1 | — | — |\n"
            "| ATCD de TVP ou d'EP | 1 | ATCD de TVP ou d'EP | 1 |\n"
            "| Chirurgie ou fracture dans le mois | 1 | Chirurgie / immobilisation < 4 semaines | 1 |\n"
            "| Néoplasie active | 1 | Cancer actif | 1 |\n"
            "| Hémoptysie | 1 | Hémoptysie | 1 |\n"
            "| Douleur unilatérale du MI | 1 | — | — |\n"
            "| FC 75-94 bpm | 1 | **FC > 100 bpm** | 1 |\n"
            "| FC ≥ 95 bpm | 2 | — | — |\n"
            "| Douleur palpation MI + œdème unilatéral | 1 | Signes cliniques de TVP | 1 |\n"
            "| — | — | Diagnostic différentiel peu probable | 1 |\n"
            "| **Probabilité Genève** | **Total** | **Probabilité Wells (2 niveaux)** | **Total** |\n"
            "| Faible < 10 % | 0-1 | Peu probable | 0-1 |\n"
            "| Intermédiaire 30-40 % | 2-4 | Probable | ≥ 2 |\n"
            "| Forte > 60 % | ≥ 5 |  |  |"
        )),
        TableauSynthese(titre="TVP distale vs proximale", markdown=(
            "| Caractéristique | TVP distale | TVP proximale |\n"
            "|-----------------|-------------|---------------|\n"
            "| Localisation | Sous-poplitée (tibiale postérieure, fibulaire, soléaire, "
            "gastrocnémienne) | Sus-poplitée (poplitée, fémorale, iliaque, cave) |\n"
            "| Symptomatique | Souvent non | **80 % symptomatiques** |\n"
            "| Risque d'EP | Faible | **Élevé** |\n"
            "| Extension proximale | **20 %** (asymptomatiques) | — |\n"
            "| Récidive sans tt | **30 %** | **50 % à 3 mois** |\n"
            "| Récidive après 6 sem d'AC | 9 % à 3 mois | — |\n"
            "| Anticoagulation | Recommandée si mise en évidence | Précoce et adéquate |"
        )),
        TableauSynthese(titre="Scores et probabilités cliniques", markdown=(
            "| Score | Pathologie | Probabilité faible | Modérée | Forte |\n"
            "|-------|-----------|---------------------|---------|-------|\n"
            "| **Wells (TVP)** | TVP | 3 % | 17 % | 75 % |\n"
            "| **Wells / Genève (EP)** | EP | 10 % | 30 % | 65 % |\n"
            "| **sPESI** | EP — pronostic | 0 = mortalité 1 % | — | ≥ 1 = mortalité 10 % |"
        )),
        TableauSynthese(titre="Stratification du risque EP (ESC 2019)", markdown=(
            "| Catégorie | Critères | Mortalité | Prise en charge |\n"
            "|-----------|----------|-----------|------------------|\n"
            "| **Haut risque** | Choc / hypotension persistante | > 15 % | Réa / USIC + "
            "**fibrinolyse** |\n"
            "| **Intermédiaire haut** | PESI ≥ 1 + ≥ 2 signes de souffrance VD | 3-15 % | Réa / "
            "USIC + anticoagulant |\n"
            "| **Intermédiaire faible** | PESI ≥ 1 + ≤ 1 signe de souffrance VD | 3-15 % | "
            "Hospitalisation conventionnelle + anticoagulant |\n"
            "| **Bas risque** | PESI = 0 | < 3 % | Hospitalisation courte ou ambulatoire + "
            "anticoagulant |"
        )),
        TableauSynthese(titre="Durées d'anticoagulation", markdown=(
            "| Situation | Durée |\n"
            "|-----------|-------|\n"
            "| **TVP proximale ou EP + facteur transitoire majeur** | **3 mois** |\n"
            "| **TVP distale** | **3 mois** (6 sem si 1er épisode + facteur déclenchant évident) |\n"
            "| **TVP proximale / EP sans facteur transitoire majeur** | **6 mois** |\n"
            "| **Facteur majeur persistant ou récidive proximale** | **> 6 mois, voire long cours** |\n"
            "| **TVP / EP récidivantes, HTP postembolique** | **Au long cours** |\n"
            "| **Cancer actif** | **Prolongé tant que cancer actif** |\n"
            "| **TVS** | **7 à 30 jours** (fondaparinux 6 semaines : étude CALISTO) |"
        )),
        TableauSynthese(titre="Anticoagulants — posologies curatives MTEV", markdown=(
            "| Molécule | Posologie | Voie |\n"
            "|----------|-----------|------|\n"
            "| **HNF** | 500 UI/kg/j (TCA 1,5-2,5 × témoin) | SC ou IV continue |\n"
            "| **Énoxaparine (Lovenox®)** | 100 UI/kg = 1 mg/kg/12 h | SC |\n"
            "| **Daltéparine (Fragmine®)** | 100 UI/kg/12 h | SC |\n"
            "| **Nadroparine (Fraxiparine®)** | 85 UI/kg/12 h | SC |\n"
            "| **Tinzaparine (Innohep®)** | 175 UI/kg/24 h | SC |\n"
            "| **Nadroparine (Fraxodi®)** | 171 UI/kg/24 h | SC |\n"
            "| **Fondaparinux (Arixtra®)** | 7,5 mg/24 h (50-100 kg) | SC |\n"
            "| **Rivaroxaban (Xarelto®)** | 15 mg × 2/j × 21 j puis 20 mg 1×/j | PO |\n"
            "| **Apixaban (Eliquis®)** | 10 mg × 2/j × 7 j puis 5 mg × 2/j | PO |\n"
            "| **AVK (Warfarine)** | INR cible 2,5 (2-3) | PO |"
        )),
    ]

    # CHIFFRES CLES
    chiffres = TableauSynthese(titre="Chiffres-clés", markdown=(
        "| Paramètre | Valeur | Contexte |\n"
        "|-----------|--------|----------|\n"
        "| Incidence MTEV | 1,83 / 1 000 / an | Étude franco-britannique |\n"
        "| Incidence EP | 0,60 / 1 000 / an | — |\n"
        "| Décès EP / an en France | 5 000 à 10 000 | 3e cause de décès après CV et cancer |\n"
        "| Prévalence MTEV (autopsie) | 20 à 40 % | — |\n"
        "| EP secondaire à TVP | 70 % | — |\n"
        "| TVP proximale + EP asymptomatique | 50 % | À l'angioscanner |\n"
        "| Asymétrie de circonférence | > 3 cm | Critère clinique TVP |\n"
        "| % obstruction artère pulmonaire | 30-50 % | Seuil d'apparition des symptômes |\n"
        "| Extension proximale TVP distale asympto | 20 % | — |\n"
        "| Récidive TVP distale sans tt | 30 % | — |\n"
        "| Récidive TVP/EP sans tt | 50 % à 3 mois | — |\n"
        "| Récidive non provoquée à 1 an | 9 % | vs 3 % si provoquée |\n"
        "| EP mortelle dès la 1re heure | 10 % | — |\n"
        "| EP avec choc / hypotension | 5-10 % | — |\n"
        "| HTAP postembolique | 0,5-5 % | Après traitement |\n"
        "| EP : triade clinique | 90 % | Dyspnée + douleur + syncope |\n"
        "| EP spontanées / idiopathiques | 20-30 % | — |\n"
        "| EP : gazométrie normale | 20 % | — |\n"
        "| Délai EP après TVP | 3 à 7 jours | — |\n"
        "| Sensibilité D-dimères Elisa | > 95 % | Spécificité ≈ 40 % |\n"
        "| Seuil D-dimères | 500 ng/mL (µg/L) | < 500 = exclusion |\n"
        "| Adaptation D-dimères > 50 ans | âge × 10 | Probabilité faible/intermédiaire |\n"
        "| Sensibilité angioscanner | 83 % | Spécificité > 90 % |\n"
        "| Sensibilité / spécificité EDV | > 95 % | — |\n"
        "| TVP retrouvée en EDV lors d'EP | 30-50 % | — |\n"
        "| TVS associée à TVP | 10 % | — |\n"
        "| TIH | Plaq < 150 G/L ou baisse ≥ 50 % | — |\n"
        "| Surveillance plaquettes HNF | 2×/sem × 21 j | — |\n"
        "| Bilan thrombophilie | 3-6 mois après thrombose | Arrêt AOD 72 h |\n"
        "| Recherche cancer | > 40 ans | — |\n"
        "| Compression classe 3 | 30-40 mmHg cheville | Minimum 6 mois |\n"
        "| Compression TVP distale étendue | ≥ 2 ans | — |\n"
        "| AOD CI si DFGe | < 30 mL/min | — |\n"
        "| HBPM CI si DFG | < 30 mL/min | — |\n"
        "| HNF si clairance | < 30 mL/min | — |\n"
        "| AVK : INR cible | 2,5 (2-3) | — |\n"
        "| Arrêt héparine après AVK | 5 j + 2 INR > 2 à 24 h | — |\n"
        "| Mobilisation après EP | Après 24 h AC efficace | — |\n"
        "| Prévention chir orthopédique lourde | 4-6 semaines | Prothèse hanche |\n"
        "| Prévention prothèse genou | 10-15 jours | — |\n"
        "| sPESI : seuils | 80 ans / 90 % SaO₂ / 100 mmHg PAS / 110 bpm | + cancer / IC / pneumopathie |\n"
        "| sPESI = 0 vs ≥ 1 | Mortalité 1 % vs 10 % | — |\n"
        "| EP haut risque PAS | < 90 mmHg ou baisse > 40 mmHg > 15 min | — |\n"
        "| Mortalité EP haut risque | > 15 % | — |\n"
        "| Mortalité EP risque intermédiaire | 3-15 % | — |\n"
        "| Énoxaparine préventive (médecine) | 0,4 mL = 4 000 UI/24 h | — |\n"
        "| Fondaparinux préventif | 2,5 mg/24 h | — |\n"
        "| HBPM cancer — daltéparine | 200 UI/kg × 1 mois, puis 150 UI/kg | — |\n"
        "| HBPM cancer — tinzaparine | 175 UI/kg/j | — |\n"
        "| HBPM cancer — énoxaparine | 150 UI/kg/j | — |"
    ))

    points_cles = [
        "TVP + EP = **MTEV** ; **70 %** des EP secondaires à une TVP, 50 % des TVP proximales ont une EP",
        "**Triade de Virchow** : stase + lésion pariétale + anomalies de l'hémostase ; départ distal",
        "Clinique seule = orientation ; confirmation par **D-dimères + échodoppler** (TVP) ou **angioscanner** (EP)",
        "**D-dimères** : test d'exclusion (**VPN forte**, seuil 500 µg/L, âge × 10 si > 50 ans)",
        "**Angioscanner** = référence EP (Se 83 %, Sp > 90 %) ; négatif exclut EP si proba faible/intermédiaire",
        "**EP haut risque** : choc/hypotension → **fibrinolyse** ; sinon **sPESI** (80/90/100/110 + cancer/IC/pneumo)",
        "Anticoag initiale : **HBPM**, fondaparinux ou **AOD anti-Xa** ; HNF si IR sévère, instable, fibrinolyse",
        "**Fibrinolyse** : EP grave (choc) ; pas dans EP intermédiaire ni TVP (sauf **phlegmatia caerulea**)",
        "**Durée AC** : 3 mois (transitoire) ; 6 mois (idiopathique) ; long cours (persistant/récidive/cancer)",
        "**Compression classe 3** (30-40 mmHg) ≥ 6 mois + mobilisation précoce ; **aspirine non indiquée** en prévention",
    ]

    fiche_eclair_md = (
        "**MTEV** : TVP + EP, même maladie. 70 % des EP issues d'une TVP. Triade "
        "Virchow.\n\n"
        "**FdR majeurs** : chirurgie > 30 min, fracture MI, immobilisation > 3 j, COP, "
        "grossesse, cancer.\n\n"
        "**Clinique TVP** : douleur + œdème unilatéral > 3 cm. Jamais suffisante seule.\n\n"
        "**Clinique EP** : dyspnée + douleur thoracique + syncope (90 %). ECG : S1Q3, "
        "BBD, T négatives V1-V4 (piège SCA).\n\n"
        "**Dg TVP** : D-dimères < 500 µg/L = exclusion si proba faible/inter. "
        "Échodoppler 1re intention.\n\n"
        "**Dg EP** : Wells/Genève + D-dimères (âge × 10 si > 50 ans). Angioscanner = "
        "référence. ETT si choc + scanner indispo.\n\n"
        "**Stratification EP** : haut risque (choc, mortalité > 15 %) → fibrinolyse + "
        "USIC. sPESI : 80/90/100/110 + cancer + IC/pneumo.\n\n"
        "**Traitement** : HBPM (énoxa 1 mg/kg/12 h), fondaparinux, AOD (rivaro 15 × 2 × "
        "21 j puis 20 ; apixa 10 × 2 × 7 j puis 5 × 2). Fibrinolyse si choc.\n\n"
        "**HNF** : si IR sévère, instable, fibrinolyse. TCA 1,5-2,5. Plaquettes 2×/sem "
        "× 21 j (TIH).\n\n"
        "**Durée** : 3 mois (transitoire/distale) ; 6 mois (idiopathique) ; long cours "
        "(persistant/récidive/HTP) ; tant que cancer actif (HBPM).\n\n"
        "**Mesures** : compression classe 3 ≥ 6 mois, mobilisation précoce. Filtre "
        "cave si CI AC ou récidive.\n\n"
        "**Prévention** : énoxa 4 000 UI/24 h ou fondaparinux 2,5 mg. PTH 4-6 sem. "
        "**Aspirine NON indiquée**.\n\n"
        "**Pièges** : ECG EP mime SCA ; AVK CI grossesse T1-T3 ; phlegmatia caerulea = "
        "urgence."
    )

    return FicheData(
        matiere="Cardiologie",
        nom_cours="Item 226 - Thrombose veineuse profonde et embolie pulmonaire",
        annee="2025-2026",
        item="Item 226",
        plan=plan,
        parties=parties,
        tableaux=tableaux,
        chiffres_cles=chiffres,
        points_cles=points_cles,
        fiche_eclair_md=fiche_eclair_md,
        images=[],
        fiche_numero="Item 226",
        usage=UsageStats(),
    )


def main():
    fiche = build_fiche()
    output_dir = PROJECT_ROOT / "output" / "fiches" / "cardiologie"
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = output_dir / "Cardiologie_Item-226_2025-2026.pdf"
    render_pdf(fiche, pdf_out)
    print(f"PDF: {pdf_out}")


if __name__ == "__main__":
    main()

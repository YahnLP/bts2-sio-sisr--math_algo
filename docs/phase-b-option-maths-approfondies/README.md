# Option mathématiques approfondies

**Pour aller plus loin, et pour qui veut préparer l'unité facultative UF2.** Cette phase est **optionnelle** : elle ne fait pas partie du parcours obligatoire et n'est jamais nécessaire pour l'épreuve E3. Elle s'adresse aux étudiants qui souhaitent présenter l'option « mathématiques approfondies » ou poursuivre en licence, en école d'ingénieurs ou en classe préparatoire ATS.

> [!NOTE]
> **Ce que dit le référentiel.** L'unité facultative UF2 « mathématiques approfondies » (arrêté du 29 avril 2019 modifié le 8 juillet 2024) est évaluée par une **épreuve écrite ponctuelle de 2 heures**. Son programme reprend six modules du programme de mathématiques des BTS (arrêté du 4 juin 2013) : suites numériques ; fonctions d'une variable réelle ; calcul intégral ; statistique descriptive ; probabilités 1 ; probabilités 2. Le référentiel précise que la compréhension d'une modélisation et son interprétation comptent plus que l'agilité de calcul, et recommande la calculatrice et l'ordinateur.

## Les modules du référentiel et où les travailler

| Module du référentiel | Où le travailler sur ce site |
|---|---|
| Suites numériques | [Phase 1 – Suites numériques](../phase-1-suites-numeriques/README.md) (S01 à S05), commune à tous |
| Fonctions d'une variable réelle | M1 (cours 1 à 3) et M2 (cours 1, 2 et 4 : dérivées, limites, asymptotes) |
| Calcul intégral | M2 (cours 3 et 5 : primitives, intégrales, aires, valeur moyenne, méthodes numériques) |
| Statistique descriptive | M3 |
| Probabilités 1 | M4 (cours 1 à 4 : conditionnement, indépendance, lois binomiale, de Poisson, uniforme, exponentielle et normale, approximation) |
| Probabilités 2 | M4 et M5 (loi exponentielle et ses applications) |

> [!WARNING]
> **À valider.** Le texte du référentiel ne donne que les **noms** des modules ; leur contenu détaillé est celui du programme de 2013. La correspondance ci-dessus en est notre lecture : le contenu exact de chaque module et la forme du sujet sont à vérifier avec ton enseignant.

## Les cours, module par module

Chaque cours part d'une situation, présente les notions pas à pas, avec des exemples résolus en détail, un bloc « À retenir » et quelques questions pour se tester. Les exercices viennent ensuite.

| Module | Thème | Cours | Exercices |
|---|---|---|---|
| M1 | Fonctions d'une variable réelle | [1. Fonctions et modèles](M1-fonctions/01-fonctions-et-modeles.md)<br>[2. Exponentielle et logarithme](M1-fonctions/02-exponentielle-et-logarithme.md)<br>[3. Racine carrée et résolution approchée](M1-fonctions/04-racine-et-resolution-approchee.md) | [Exercices](M1-fonctions/03-exercices.md) |
| M2 | Dérivation et calcul intégral | [1. Dérivée et variations](M2-derivees-integrales/01-derivee-et-variations.md)<br>[2. Limites et asymptotes](M2-derivees-integrales/02-limites-et-asymptotes.md)<br>[3. Primitives et intégrales](M2-derivees-integrales/03-primitives-et-integrales.md)<br>[4. Dérivées composées et asymptotes](M2-derivees-integrales/05-derivees-composees-et-asymptotes.md)<br>[5. Primitives, aires, méthodes numériques](M2-derivees-integrales/06-primitives-aires-methodes-numeriques.md) | [Exercices](M2-derivees-integrales/04-exercices.md) |
| M3 | Statistique descriptive | [1. Position et dispersion](M3-statistique/01-indicateurs-de-position-et-de-dispersion.md)<br>[2. Régression et ajustement](M3-statistique/02-regression-et-ajustement.md) | [Exercices](M3-statistique/03-exercices.md) |
| M4 | Probabilités | [1. Variable aléatoire et loi binomiale](M4-probabilites/01-variable-aleatoire-et-loi-binomiale.md)<br>[2. Poisson et normale](M4-probabilites/02-poisson-et-normale.md)<br>[3. Conditionnement et indépendance](M4-probabilites/04-conditionnement-et-independance.md)<br>[4. Loi uniforme, exponentielle, approximation normale](M4-probabilites/05-uniforme-et-approximation-normale.md) | [Exercices](M4-probabilites/03-exercices.md) |
| M5 | Application : loi exponentielle et fiabilité | [1. Fiabilité et loi exponentielle](M5-fiabilite/01-fiabilite-et-loi-exponentielle.md)<br>[2. Systèmes et disponibilité](M5-fiabilite/02-systemes-et-disponibilite.md) | [Exercices](M5-fiabilite/03-exercices.md) |

Un [aide-mémoire calculatrice](aide-memoire-calculatrice.md) (NumWorks, Casio, TI et Python) accompagne les modules, et un [sujet de 2 heures](sujets/sujet-1.md) clôt la phase.

> [!TIP]
> **Ordre conseillé.** Phase 1 (suites) si elle n'est pas déjà faite, puis M1, M2, M3 et M4. Le module M5 réutilise l'exponentielle (M1) et les probabilités (M4) : fais-le en dernier. Compte environ une heure et demie par cours, puis une heure d'exercices par module.

## Ce qui est exclu par le référentiel

- Dans les fonctions : les fonctions sinus et cosinus, l'approximation locale d'une fonction, les courbes paramétrées.
- Dans le calcul intégral : les primitives de \(t \mapsto \cos(\omega t + \varphi)\) et \(t \mapsto \sin(\omega t + \varphi)\), la formule d'intégration par parties.
- Dans les probabilités : le théorème de la limite centrée et les exemples de processus aléatoires (chaînes de Markov, par exemple).

Ce site ajoute deux sujets **hors référentiel**, signalés comme tels : la disponibilité d'un système (culture professionnelle, M5) et quelques exercices « pour aller plus loin ».

## Comment travailler

Pour chaque module, lis le cours **crayon en main** : refais les exemples résolus sans regarder la solution, puis teste-toi. Les exercices comportent trois niveaux : **socle**, **format épreuve**, **pour aller plus loin**. Cherche d'abord sur papier, puis ouvre le corrigé. Utilise la calculatrice (ou Python) pour les calculs lourds, et **commente toujours le résultat** : unité, ordre de grandeur, solution acceptable ou à rejeter.

# Parcours « cœur » et « complément »

Les 19 séances de 4 h représentent **76 h** par an. Pour mémoire, la grille sous statut scolaire (annexe III.A du référentiel) prévoit en deuxième année **72 h** de mathématiques pour l'informatique (enseignement obligatoire) et **48 h** de mathématiques approfondies (enseignement facultatif). Le contenu de ce site est **proposé par l'enseignant** et ne correspond pas au programme obligatoire (voir [Programme de la 2e année](programme-2a.md)) : le cadre dans lequel il est enseigné reste à valider. Quand le temps manque, ce parcours indique **quelles séances garder en priorité**.

> [!NOTE]
> Ce classement est une **proposition de l'auteur, à valider** par l'équipe pédagogique. Il ne retire rien du site : chaque séance reste disponible, et son statut est rappelé dans sa fiche.

## Pourquoi un seul complément

Les prérequis forment une **chaîne presque linéaire** : chaque séance repose sur la précédente, des suites (S01 à S05) à la récursivité (S06 à S10), puis à l'analyse d'algorithmes (S11 à S15) et aux structures de données (S16, S17). J'ai vérifié les renvois entre séances : la somme arithmétique et les suites géométriques servent à compter les opérations en S12 et S13, la récurrence de S04 sert à S05, et S05 est un prérequis déclaré de S06. Seule **S15** n'est le prérequis d'aucune séance : S16 la cite pour un contrôle de coût, S18 et S19 la citent dans leurs listes de révision.

## Principe

Une séance est **cœur** si l'une au moins de ces conditions est vraie :

1. elle est la **seule** à traiter une notion du programme proposé ;
2. elle est un **prérequis** d'une autre séance cœur (le site l'indique dans chaque fiche) ;
3. elle prépare directement la **méthode et l'épreuve blanche** (S18 et S19).

Sinon elle est **complément**.

## Résultat

- **18 séances cœur** (72 h) ;
- **1 séance complément** (4 h) : S15.

| Séance | Thème | Parcours | Pourquoi |
|---|---|---|---|
| S01 | Suites numériques : définition et programmation | **Cœur** | Suites par récurrence : prérequis de S02 et de S06, S07 (récurrence) ; repris en S18 et S19. |
| S02 | Suites arithmétiques | **Cœur** | Suites arithmétiques : prérequis de S03 ; la somme arithmétique sert à compter les opérations en S13. |
| S03 | Suites géométriques | **Cœur** | Suites géométriques : prérequis de S04 et S05 ; sert à étudier le coût en S12 et S13. |
| S04 | Sommes et applications : intérêts, amortissement, croissance de données | **Cœur** | Sommes et applications : prérequis de S05 (récurrence « pourcentage plus ajout »). |
| S05 | Comportement à long terme et algorithmes de seuil | **Cœur** | Comportement à long terme et seuils : prérequis de S06 (suites récurrentes, terminaison d'une boucle). |
| S06 | Récursivité : principe | **Cœur** | Récursivité, principe : prérequis de S07 à S09 et de S11. |
| S07 | Récursivité, suites et pile d'appels | **Cœur** | Récursivité et pile d'appels : prérequis de S08 ; repris en S16. |
| S08 | Récursivité sur les tableaux et les chaînes | **Cœur** | Récursivité sur tableaux et chaînes : prérequis de S09 et S10. |
| S09 | Diviser pour régner | **Cœur** | Diviser pour régner : prérequis de S10 ; sert aux tris de S14. |
| S10 | Structures arborescentes et parcours en profondeur | **Cœur** | Arbres et parcours : prérequis de S11 et S16. |
| S11 | Terminaison et correction d'un algorithme | **Cœur** | Terminaison et correction : prérequis de S12 ; cité par S18. |
| S12 | Coût d'un algorithme : compter les opérations | **Cœur** | Coût d'un algorithme : prérequis de S13. |
| S13 | Complexité asymptotique | **Cœur** | Complexité asymptotique : prérequis de S14. |
| S14 | Tris et recherches : comparaison | **Cœur** | Tris et recherches : prérequis de S16. |
| S15 | Mesurer et connaître les limites | **Complément** | Mesures et limites : n'est le prérequis d'aucune séance ; seul le test de doublement est cité en S16 et S19. |
| S16 | Piles, files et dictionnaires | **Cœur** | Piles, files, dictionnaires : prérequis de S17. |
| S17 | Graphes en Python : parcours et plus court chemin | **Cœur** | Graphes : parcours et plus court chemin ; prépare S18. |
| S18 | Méthode : de l'énoncé au programme testé | **Cœur** | Méthode « de l'énoncé au programme testé » : prépare directement l'épreuve blanche. |
| S19 | Révisions et épreuve blanche | **Cœur** | Révisions et épreuve blanche. |

## Si l'on saute S15

S16 renvoie au test de doublement et S19 révise « mesures et explosions ». Garder, dans S14 ou en lecture seule (environ 1 h), le **test de doublement** et l'**explosion exponentielle** (parties II et III du cours de S15) : on double la taille de l'entrée et on observe le rapport des temps.

## Pour aller plus loin si le temps manque encore

Un seul complément libère 4 h. Au-delà, il faut alléger **à l'intérieur** des séances cœur (par exemple ne garder que les exercices essentiels d'une séance) ou retirer un bloc entier de la progression, ce qui casse la chaîne de prérequis. Le plus raisonnable est alors de **s'arrêter à S14** puis de passer directement à S18 et S19, en acceptant de ne pas faire les structures de données (S16) et les graphes (S17) ; à décider avec l'enseignant.

## Utilisation

- Si **toutes** les séances sont faites, rien ne change.
- Si le temps manque, retirer d'abord S15.
- Les prérequis écrits dans chaque fiche ont été relus pour que ce classement ne casse aucune dépendance entre séances cœur.

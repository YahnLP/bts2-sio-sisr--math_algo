# Cours – De l'énoncé au programme testé

*BTS SIO SISR 2e année – Pour aller plus loin – S18 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** tout le programme de la 2e année (S01 à S17), en particulier variants/invariants (S11), coût (S12 à S15), structures (S16).
> - **Outils :** Papier, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Analyser** un énoncé (entrées, sorties, contraintes) ;
- [ ] **Décomposer** en petites fonctions ;
- [ ] **Choisir** structures et algorithmes ;
- [ ] **Tester** et corriger ;
- [ ] **Rédiger** une justification.

## I. Cinq étapes

| Étape | Question | Production |
|---|---|---|
| 1. Comprendre | Que donne-t-on ? Que demande-t-on ? | entrées, sorties, un exemple à la main |
| 2. Décomposer | Quelles sous-tâches ? | liste de fonctions, une idée par fonction |
| 3. Choisir | Quelles structures, quels algorithmes ? | tableau de choix avec le coût visé |
| 4. Programmer et tester | Ça marche ? | tests typiques et limites |
| 5. Justifier | Pourquoi est-ce correct et suffisamment rapide ? | invariant, coût, limites |

## II. Exemple suivi : journal de connexions

**Énoncé.** Chaque ligne d'un journal a la forme `"adresse;statut"` avec le statut `OK` ou `ECHEC`. On veut repérer les adresses **suspectes** : celles qui ont au moins `seuil` échecs.

**1. Comprendre.**

- Entrées : une liste de lignes (chaînes), un entier `seuil`.
- Sortie : la liste triée des adresses suspectes.
- Exemple à la main avec `["a;OK", "b;ECHEC", "b;ECHEC", "a;ECHEC"]` et `seuil = 2` : `b` a 2 échecs, `a` en a 1 : résultat `["b"]`.

**2. Décomposer.**

| Fonction | Rôle |
|---|---|
| `parse_ligne` | coupe une ligne en (adresse, statut) |
| `echecs_par_ip` | compte les échecs de chaque adresse |
| `suspectes` | garde celles qui atteignent le seuil |

**3. Choisir.** Un **dictionnaire** adresse → nombre d'échecs : un passage sur les lignes, coût de l'ordre de \(n\) pour \(n\) lignes (accès en \(O(1)\) en moyenne, S16). Un tri final des adresses retenues.

**4. Programmer et tester.** On écrit chaque fonction et ses tests **avant** de passer à la suivante.

**5. Justifier.** Invariant de `echecs_par_ip` : après avoir lu \(k\) lignes, le dictionnaire contient, pour chaque adresse, le nombre d'échecs parmi ces \(k\) lignes. À la fin \(k = n\) : le dictionnaire est correct.

## III. Bien tester

| Catégorie | Exemples |
|---|---|
| Typique | quelques lignes variées |
| Limite | liste vide, une seule ligne, `seuil = 1` |
| Piège | espaces autour des champs, adresse qui apparaît avec `OK` et `ECHEC` |
| Résultat attendu | écrit **avant** d'exécuter |

> [!TIP]
> En cas d'échec d'un test, relis d'abord **ton test** : l'erreur peut être dans le résultat attendu.

## IV. Rédiger la justification

Trois phrases suffisent :

1. **Idée** : « on compte les échecs avec un dictionnaire » ;
2. **Correction** : l'invariant ;
3. **Coût** : « un passage, donc de l'ordre de \(n\) opérations ».

**Test flash.** Quelle est l'étape 1 de la méthode ?

<details markdown="1">
<summary>Voir la réponse</summary>

Comprendre : identifier entrées, sorties, contraintes et traiter un exemple à la main.

</details>

## À retenir

- Cinq étapes : comprendre, décomposer, choisir, programmer et tester, justifier.
- Une fonction = une idée ; tests avant le code suivant.
- Justification : idée, invariant, coût.

# Synthèse – Algorithmique appliquée et programmation

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – R5*

> [!NOTE]
> **Rôle de cette page.** Ce qu'il faut savoir lire, écrire et tester pour l'exercice « programmer » de l'épreuve : forme d'un algorithme, instructions, données, fonctions, tests. Les cours détaillés sont dans le [site de 1re année](https://yahnlp.github.io/bts1-sio-sisr-math_algo/) (séances S03, S04, S12, S15, S18). Langage de ce site : **Python**.

## I. Écrire un algorithme lisible

Un algorithme se présente avec un **en-tête** : **nom**, **rôle**, **données d'entrée**, **données de sortie**, **variables locales typées**. Le corps est **indenté**, avec des mots de début et de fin explicites. Des **commentaires** précisent le rôle des variables.

```text
Fonction somme_chiffres(n)
  Rôle    : calcule la somme des chiffres décimaux de n
  Entrée  : n, entier naturel
  Sortie  : s, entier naturel
  Locales : s (entier)
Début
  s ← 0
  TANT QUE n > 0 FAIRE
     s ← s + (n MOD 10)        # dernier chiffre
     n ← n DIV 10              # on retire le dernier chiffre
  FIN TANT QUE
  Retourner s
Fin
```

## II. Données et instructions

| Élément | À savoir |
|---|---|
| Types simples | entier naturel, entier relatif, réel, booléen, chaîne de caractères |
| Tableaux | une ou deux dimensions ; indices à partir de 0 en Python ; tableau de tableaux pour une matrice |
| Opérateurs | \(+ - \times /\), **quotient** (`//`) et **reste** (`%`), comparaisons, `non`, `et`, `ou`, `oux` |
| Chaînes | concaténation, extraction (début, milieu, fin), recherche d'un motif, conversion de type |
| Entrées-sorties | lecture, écriture |
| Affectation | `x ← x + 1` : la variable affectée participe à l'expression évaluée |

**Opérateurs bit à bit** : `&` (ET), `|` (OU), `^` (OU exclusif), `<<` et `>>` (décalages). Masques : tester un bit `(x >> k) & 1`, le mettre à 1 `x | (1 << k)`, le mettre à 0 `x & ~(1 << k)`, l'inverser `x ^ (1 << k)`.

**Σ et Π.** \(\sum_{i=a}^{b} u_i\) se traduit par une boucle avec un accumulateur initialisé à **0** ; \(\prod_{i=a}^{b} u_i\) par un accumulateur initialisé à **1**.

## III. Structures de contrôle

- **Séquence**, **condition** (`SI … ALORS … SINON`), **boucle déterministe** (`POUR`, nombre de tours connu), **boucle indéterministe** (`TANT QUE`, `RÉPÉTER … JUSQU'À`).
- **Construire une boucle** : initialisation, condition d'arrêt, mise à jour **qui rapproche de l'arrêt**, cas indésirables neutralisés, résultat final mis en forme.
- **Structures imbriquées** autorisées (limiter à deux boucles imbriquées dépendantes).

## IV. Fonctions et variables

Une fonction a des **paramètres** d'entrée et une **valeur retournée**. Une variable **locale** n'existe que dans la fonction ; une variable **globale** existe partout mais complique les tests : on évite d'en modifier une depuis une fonction.

## V. Tester et déboguer

- **Suivi de variables** : un tableau avec une colonne par variable et une ligne par tour de boucle.
- **Jeux de tests** : un cas **typique**, les **limites** (liste vide, un seul élément, valeur minimale ou maximale), un cas **erroné**.
- **Effets indésirables** à connaître : effet de bord (modifier un argument), évaluation partielle d'une expression booléenne, **dépassement** de capacité, approximation des réels, mauvais **transtypage**, **indice hors domaine**.

## VI. Compléments (au programme de l'algorithmique appliquée)

- **Récursivité** : une fonction qui s'appelle elle-même. Il faut un **cas de base** (sans appel), un appel sur un problème **plus petit**, et la **finitude**. Pas de récursivité mutuelle.
- **Coût** : on compte, en fonction de la taille \(n\), un nombre **minimal** et **maximal** d'opérations significatives (comparaisons).

## À retenir pour le jour de l'épreuve

1. **En-tête** et **commentaires** : ils rapportent des points et clarifient votre pensée.
2. Écrire d'abord **ce que la fonction doit retourner** pour deux ou trois exemples, **puis** le code.
3. **Tester à la main** avec un suivi de variables avant de conclure.

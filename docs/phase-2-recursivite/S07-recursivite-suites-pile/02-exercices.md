# Exercices – Récursivité, suites et pile d'appels

*BTS SIO SISR 2e année – Pour aller plus loin – S07*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**. Ouvre ensuite « Voir la réponse » pour te corriger. **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Suite récursive

Écrire une fonction récursive pour \(u_0 = 3\), \(u_{n+1} = 2u_n - 1\), puis calculer \(u_1, \dots, u_4\). Trouver une formule explicite pour contrôler.

<details markdown="1">
<summary>Voir la réponse</summary>

`def u(n): return 3 if n == 0 else 2 * u(n - 1) - 1`. Termes : 5, 9, 17, 33. Formule : \(u_n = 2^{n+1} + 1\) (contrôle : \(u_4 = 32 + 1 = 33\)). On peut la démontrer avec le point fixe \(L = 1\) (S05) : \(u_n - 1 = 2 \times 2^n\).

</details>

## Exercice 2 – Dessiner la pile

Dessiner la pile d'appels au moment le plus profond pour `fact(3)`. Quelle est la profondeur pour `fact(n)` ?

<details markdown="1">
<summary>Voir la réponse</summary>

Au plus profond : `fact(0)` (sommet), `fact(1)`, `fact(2)`, `fact(3)` : **4** cadres. Pour `fact(n)` : \(n + 1\) cadres.

</details>

## Exercice 3 – Fibonacci

Calculer \(F_2, \dots, F_{10}\) puis le nombre d'appels \(C(6)\) et \(C(7)\) de la version naïve.

<details markdown="1">
<summary>Voir la réponse</summary>

\(F_2 = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55\) (\(F_{10} = 55\)). \(C(6) = 1 + C(5) + C(4) = 1 + 15 + 9 = 25\) ; \(C(7) = 1 + 25 + 15 = 41\).

</details>

## Exercice 4 – Recalculs

Dans `fib(5)` (version naïve), combien de fois `fib(2)` est-il calculé ? Combien de fois `fib(3)` ?

<details markdown="1">
<summary>Voir la réponse</summary>

`fib(5)` appelle `fib(4)` et `fib(3)`. `fib(4)` appelle `fib(3)` et `fib(2)`. Donc `fib(3)` est calculé **2 fois** (une depuis `fib(5)`, une depuis `fib(4)`). `fib(2)` est calculé **3 fois** (depuis `fib(4)`, depuis chaque `fib(3)`).

</details>

## Exercice 5 – Mémoïsation

Avec la mémoïsation, combien d'appels pour `fib_memo(30)` ? Pourquoi un tel écart avec 2 692 537 ?

<details markdown="1">
<summary>Voir la réponse</summary>

**59** appels (\(2 \times 30 - 1\)). Chaque valeur est calculée une seule fois et les appels suivants lisent le dictionnaire : on passe d'un coût exponentiel à un coût proportionnel à \(n\).

</details>

## Exercice 6 – Erreur de profondeur

Pourquoi `fact(5000)` échoue-t-il ? Que proposer pour calculer \(5\,000!\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

La pile contient 5 001 cadres, au-delà de la limite (environ 1 000 par défaut) : `RecursionError`. On écrit une **version itérative** (une boucle qui multiplie), sans pile. Relever la limite de récursion est possible mais déconseillé : cela risque de saturer la mémoire.

</details>

## Exercice 7 – Version itérative

Dérouler `fib_iter(6)` en donnant `a` et `b` après chaque tour.

<details markdown="1">
<summary>Voir la réponse</summary>

| Tour | `a` | `b` |
|---|---|---|
| départ | 0 | 1 |
| 1 | 1 | 1 |
| 2 | 1 | 2 |
| 3 | 2 | 3 |
| 4 | 3 | 5 |
| 5 | 5 | 8 |
| 6 | 8 | 13 |

`fib_iter(6)` renvoie 8 (\(F_6 = 8\)).

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Écrire une suite récurrente en récursif
- [ ] Dessiner la pile d'appels
- [ ] Expliquer l'explosion des appels de Fibonacci
- [ ] Utiliser un dictionnaire pour mémoïser

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

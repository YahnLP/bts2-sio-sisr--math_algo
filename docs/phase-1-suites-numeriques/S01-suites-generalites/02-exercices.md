# Exercices – Suites : définition, calcul, variation

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S01*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Formule explicite

Soit \(u_n = 4n - 3\). Calculer \(u_0, u_1, u_2, u_3, u_4\) puis \(u_{10}\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(u_0 = -3\), \(u_1 = 1\), \(u_2 = 5\), \(u_3 = 9\), \(u_4 = 13\). Et \(u_{10} = 4 \times 10 - 3 = 37\).

</details>

## Exercice 2 – Récurrence

Soit \(u_0 = 2\) et \(u_{n+1} = 3u_n - 1\). Calculer \(u_1, u_2, u_3, u_4\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(u_1 = 5\), \(u_2 = 14\), \(u_3 = 41\), \(u_4 = 122\).

</details>

## Exercice 3 – Modéliser un stockage

Un serveur de fichiers contient 120 Go à la fin du mois 0. Chaque mois, 15 Go de données s'ajoutent. On note \(u_n\) la quantité de données (en Go) à la fin du mois \(n\).

1. Écrire une relation de récurrence.
2. Trouver une formule explicite et calculer \(u_6\).
3. Le disque a une capacité de 300 Go. À la fin de quel mois est-il plein pour la première fois ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(u_0 = 120\) et \(u_{n+1} = u_n + 15\).
2. À chaque mois on ajoute 15 : \(u_n = 120 + 15n\). Donc \(u_6 = 120 + 90 = 210\) Go.
3. On cherche le plus petit \(n\) tel que \(120 + 15n \ge 300\), soit \(15n \ge 180\), soit \(n \ge 12\). Le disque est plein à la fin du mois **12** (\(u_{12} = 300\)).

</details>

## Exercice 4 – Sens de variation

Étudier le sens de variation de \(u_n = n^2 - 6n\) en calculant \(u_{n+1} - u_n\). Donner les premiers termes pour contrôler.

<details markdown="1">
<summary>Voir la réponse</summary>

\(u_{n+1} - u_n = (n+1)^2 - 6(n+1) - n^2 + 6n = 2n + 1 - 6 = 2n - 5\).
Ce nombre est négatif pour \(n \le 2\) (la suite décroît) et positif pour \(n \ge 3\) (elle croît).
Contrôle : \(u_0 = 0\), \(u_1 = -5\), \(u_2 = -8\), \(u_3 = -9\), \(u_4 = -8\), \(u_5 = -5\), \(u_6 = 0\). La suite décroît jusqu'à \(u_3\), puis croît.

</details>

## Exercice 5 – Trace d'une boucle

```text
u ← 2
POUR k DE 1 À 4 FAIRE
  u ← 2 × u + 1
FIN POUR
```

Dérouler l'algorithme. Quel terme de quelle suite `u` contient-il à la fin ?

<details markdown="1">
<summary>Voir la réponse</summary>

| Tour | `k` | `u` après |
|---|---|---|
| 0 (départ) | – | 2 |
| 1 | 1 | 5 |
| 2 | 2 | 11 |
| 3 | 3 | 23 |
| 4 | 4 | 47 |

`u` vaut 47 : c'est le terme \(u_4\) de la suite \(u_0 = 2\), \(u_{n+1} = 2u_n + 1\).

</details>

## Exercice 6 – Choisir sa méthode

On a \(u_0 = 4\) et \(u_{n+1} = u_n + 7\).

1. Calculer \(u_1, u_2, u_3\) et deviner une formule explicite.
2. En déduire \(u_{100}\) sans calculer 100 termes.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(u_1 = 11\), \(u_2 = 18\), \(u_3 = 25\). On ajoute 7 à chaque rang à partir de 4 : \(u_n = 4 + 7n\).
2. \(u_{100} = 4 + 700 = 704\).

(Cette formule sera **démontrée** en S02 pour les suites de ce type.)

</details>

## Exercice 7 – Une suite à deux termes

Soit \(u_0 = 1\), \(u_1 = 1\) et \(u_{n+2} = u_{n+1} + u_n\). Calculer \(u_2, \dots, u_6\). Comment faut-il adapter la boucle Python ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(u_2 = 2\), \(u_3 = 3\), \(u_4 = 5\), \(u_5 = 8\), \(u_6 = 13\). Il faut **garder deux termes** : on remplace `(a, b)` par `(b, a + b)` à chaque tour.

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Calculer des termes avec une formule explicite et avec une récurrence
- [ ] Écrire une relation de récurrence à partir d'un énoncé
- [ ] Étudier le signe de \(u_{n+1} - u_n\)
- [ ] Dérouler une boucle qui calcule une suite

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

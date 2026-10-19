# Aide-mémoire – Terminaison, invariant et tests

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S11*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Les deux questions

| Question | Outil |
|---|---|
| Termine-t-il ? | **Variant** : entier, \(\ge 0\), strictement décroissant |
| Est-il correct ? | **Invariant** : vrai au départ, conservé, utile à la sortie |

Spécification : **précondition** (entrée) et **postcondition** (sortie).

## Preuve en trois étapes

1. Initialisation : l'invariant est vrai avant le premier tour.
2. Conservation : vrai avant un tour, donc vrai après.
3. Conclusion : invariant + condition d'arrêt = postcondition.

## Modèles

| Boucle | Variant | Invariant |
|---|---|---|
| `while n > 0: n //= 2` | `n` | — |
| Somme `s += i` | `n - k` | \(s = k(k+1)/2\) |
| Maximum | éléments restants | `m` = max des éléments examinés |
| Puissance | `n - k` | \(p = x^k\) |
| Euclide | `b` | \(\text{PGCD}(a, b)\) inchangé |

## Tests

Typique, taille minimale, répétitions, valeurs extrêmes, déjà ordonné, inversé, cas interdit. Un test réussi ne prouve rien pour les autres cas.

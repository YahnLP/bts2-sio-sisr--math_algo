# Cours – Récursivité, suites et pile d'appels

*BTS SIO SISR 2e année – Pour aller plus loin – S07 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S06 (cas de base, cas récursif, variant) ; S01 (suites par récurrence).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Traduire** une suite récurrente en fonction récursive ;
- [ ] **Représenter** la pile d'appels ;
- [ ] **Reconnaître** la limite de profondeur ;
- [ ] **Éviter** les recalculs (mémoïsation) ;
- [ ] **Comparer** les versions récursive et itérative.

## I. Une suite récurrente est une fonction récursive

La suite \(u_0 = 3\), \(u_{n+1} = 2u_n - 1\) s'écrit directement :

```python
def u(n):
    if n == 0:
        return 3
    return 2 * u(n - 1) - 1
```

Les termes sont \(3, 5, 9, 17, 33, \dots\) : `u(4)` renvoie 33. Cette fonction ne fait **qu'un** appel récursif par niveau, comme la factorielle.

## II. La pile d'appels

Quand une fonction appelle une autre, Python **met en attente** la première : il garde son contexte (valeurs de ses variables, endroit où reprendre) dans une **pile**. Chaque appel en cours occupe un **cadre** de la pile. Pour `fact(3)`, la pile contient jusqu'à 4 cadres :

```text
fact(0)   <- sommet : appel en cours, renvoie 1
fact(1)   en attente de fact(0)
fact(2)   en attente de fact(1)
fact(3)   en attente de fact(2)
```

Quand `fact(0)` renvoie 1, son cadre est retiré et `fact(1)` reprend, etc. La **profondeur** de la pile pour `fact(n)` est \(n + 1\).

La pile a une **taille limitée**. En Python, la limite par défaut est d'environ 1 000 appels imbriqués : `fact(5000)` déclenche `RecursionError`. Le nombre exact dépend de l'environnement ; on ne s'appuie pas dessus, on **évite les profondeurs excessives**.

## III. Quand la récursivité devient lente : Fibonacci

La suite de Fibonacci : \(F_0 = 0\), \(F_1 = 1\), \(F_{n} = F_{n-1} + F_{n-2}\), soit \(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \dots\)

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

Ici chaque appel en fait **deux** : on recalcule les mêmes valeurs. Le nombre d'appels \(C(n)\) vérifie \(C(0) = C(1) = 1\) et \(C(n) = 1 + C(n-1) + C(n-2)\) :

| \(n\) | 0 | 1 | 2 | 3 | 4 | 5 | 10 | 20 | 30 |
|---|---|---|---|---|---|---|---|---|---|
| \(C(n)\) | 1 | 1 | 3 | 5 | 9 | 15 | 177 | 21 891 | 2 692 537 |

Le nombre d'appels **explose** : il est plus que multiplié par 1,6 à chaque rang. `fib(30)` fait presque 2,7 millions d'appels pour calculer un nombre.

## IV. Mémoïsation

On **mémorise** les résultats déjà calculés dans un dictionnaire pour ne jamais recalculer :

```python
def fib_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n < 2:
        return n
    if n not in cache:
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]
```

Chaque valeur n'est calculée qu'une fois : `fib_memo(30)` fait **59 appels** au lieu de 2,7 millions (soit \(2n - 1\)).

> [!WARNING]
> N'écris pas `def f(n, cache={})` : un dictionnaire par défaut est **partagé** entre tous les appels. On met `cache=None` et on crée le dictionnaire dans la fonction.

## V. La version itérative

```python
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

\(n\) tours de boucle, deux variables, aucune pile : c'est la solution la plus économe. Elle correspond à l'invariant « après \(k\) tours, `a` vaut \(F_k\) et `b` vaut \(F_{k+1}\) ».

| Version | Nombre d'opérations | Mémoire |
|---|---|---|
| Récursive naïve | exponentiel (millions d'appels pour \(n = 30\)) | profondeur \(n\) |
| Récursive mémoïsée | \(2n - 1\) appels | profondeur \(n\) et dictionnaire |
| Itérative | \(n\) tours | 2 variables |

**Test flash.** `fib(5)` fait combien d'appels ? Quelle valeur renvoie-t-il ?

<details markdown="1">
<summary>Voir la réponse</summary>

15 appels (tableau ci-dessus) ; `fib(5)` renvoie 5.

</details>

## À retenir

- Une suite \(u_{n+1} = f(u_n)\) se traduit en une fonction à un appel récursif.
- Chaque appel en attente occupe un cadre de la pile : profondeur limitée.
- Plusieurs appels récursifs sur les mêmes données : recalculs, coût exponentiel.
- Mémoïsation (dictionnaire) ou boucle : on supprime les recalculs.

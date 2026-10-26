# Aide-mémoire – Récursivité, suites et pile d'appels

*BTS SIO SISR 2e année – Pour aller plus loin – S07*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Suite → fonction

\(u_0\) donné, \(u_{n+1} = f(u_n)\) : cas de base `n == 0`, cas récursif `f(u(n - 1))`.

## Pile d'appels

Un cadre par appel en attente ; profondeur de `fact(n)` : \(n + 1\). Limite d'environ 1 000 en Python : au-delà, `RecursionError`.

## Fibonacci

\(F_0 = 0\), \(F_1 = 1\), \(F_n = F_{n-1} + F_{n-2}\) : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.

| Version | Appels / tours pour \(n\) |
|---|---|
| Naïve | \(C(n) = 1 + C(n-1) + C(n-2)\) : 177 pour \(n = 10\), 2 692 537 pour \(n = 30\) |
| Mémoïsée | \(2n - 1\) |
| Itérative | \(n\) tours |

## Mémoïsation

```python
def f(n, cache=None):
    if cache is None:
        cache = {}
    ...
    if n not in cache:
        cache[n] = ...
    return cache[n]
```

Jamais `cache={}` en paramètre par défaut.

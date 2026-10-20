# Corrigé S02

## Exercices

1. (a) arithmétique, \(r = 5\) ; (b) non ; (c) arithmétique, \(r = -4\).
2. \(u_n = 12 + 5n\) ; \(u_{20} = 112\) ; somme \(= 1\,302\).
3. \(r = 4\) ; \(u_0 = 2\) ; \(u_n = 2 + 4n\) ; \(u_{20} = 82\).
4. \(u_{30} = 825\) Mo ; cumul \(= 13\,875\) Mo.
5. \(5\,050\) ; \(2\,500\).
6. 61 ​adresses.
7. \(n = 21\).

## TP Python – solutions

```python
def terme_arith(u0, r, n):
    return u0 + n * r

def somme_arith(u0, r, n):
    return (n + 1) * (2 * u0 + n * r) // 2

def est_arithmetique(liste):
    if len(liste) <= 2:
        return True
    raison = liste[1] - liste[0]
    for i in range(1, len(liste) - 1):
        if liste[i + 1] - liste[i] != raison:
            return False
    return True

def nb_termes(a, b, pas):
    if b < a:
        return 0
    return (b - a) // pas + 1

def rang_moins_cher(a0, ra, b0, rb):
    n = 0
    while not (b0 + rb * n < a0 + ra * n):
        n = n + 1
    return n
```

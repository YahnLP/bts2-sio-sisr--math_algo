# Corrigé S12

## Exercices

1. \(n\) ; \(n^2\) (100 ; 10 000).
2. 499 500.
3. 1 ; \(n\) ; \((n+1)/2\).
4. 9 ; 19.
5. \(n = 32\).
6. ≈ 0,5 s ; ≈ 5,79 jours (hypothèse fictive de 1 µs par comparaison).

## TP Python – solutions

```python
def somme_compte(n):
    s = 0
    nb = 0
    for i in range(n):
        s = s + i
        nb = nb + 1
    return (s, nb)

def recherche_compte(L, x):
    nb = 0
    for i in range(len(L)):
        nb = nb + 1
        if L[i] == x:
            return (i, nb)
    return (-1, nb)

def doublons_compte(L):
    nb = 0
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            nb = nb + 1
            if L[i] == L[j]:
                return (True, nb)
    return (False, nb)

def tours_log2(n):
    tours = 0
    while n > 1:
        n = n // 2
        tours = tours + 1
    return tours

def premier_n_pire(f, g):
    n = 1
    while not g(n) > f(n):
        n = n + 1
    return n
```

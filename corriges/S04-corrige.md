# Corrigé S04

## Exercices

1. Simples 7 000 € ; composés 7 401,22 € ; écart 401,22 €.
2. 2 433,28 €.
3. \(M \approx 531{,}85\) € ; lignes (60,00 ; 471,85 ; 11 528,15), (57,64 ; 474,21 ; 11 053,95), (55,27 ; 476,58 ; 10 577,37) ; intérêts \(\approx 764{,}34\) €.
4. \(u_{n+1} = 1{,}1u_n + 50\) ; 270, 347, 431,7 ; mois 8.
5. (a) arithmétique ; (b) géométrique ; (c) récurrence mixte.
6. \(K_{24} \approx 0\) aux arrondis près.

## TP Python – solutions

```python
def capital_compose(c0, taux, n):
    return round(c0 * (1 + taux / 100) ** n, 2)

def epargne(versement, taux, n):
    capital = 0
    for _ in range(n):
        capital = capital * (1 + taux / 100) + versement
    return round(capital, 2)

def mensualite(capital, taux, n):
    t = taux / 100
    if t == 0:
        return round(capital / n, 2)
    return round(capital * t / (1 - (1 + t) ** (-n)), 2)

def capital_restant(capital, taux, n, k):
    t = taux / 100
    if t == 0:
        m = capital / n
    else:
        m = capital * t / (1 - (1 + t) ** (-n))
    reste = capital
    for _ in range(k):
        reste = reste * (1 + t) - m
    return round(reste, 2)

def mois_stockage_plein(u0, taux, ajout, capacite):
    u = u0
    n = 0
    while u < capacite:
        u = u * (1 + taux / 100) + ajout
        n = n + 1
    return n
```

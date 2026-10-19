# Corrigé S03

## Exercices

1. (a) \(q = 2\) ; (b) \(q = 1/2\) ; (c) non ; (d) \(q = -3\).
2. \(u_{10} = 3\,072\) ; somme \(= 6\,141\).
3. \(q = 2\) ; \(u_0 = 3\) ; \(u_n = 3 \times 2^n\).
4. 864 Go ; mois 8.
5. 1 044,01 €.
6. 1 023 Go.
7. \(n = 29\).

## TP Python – solutions

```python
def terme_geo(u0, q, n):
    return u0 * q ** n

def somme_geo(u0, q, n):
    if q == 1:
        return u0 * (n + 1)
    return u0 * (q ** (n + 1) - 1) // (q - 1)

from fractions import Fraction

def est_geometrique(liste):
    if len(liste) <= 1:
        return True
    if liste[0] == 0:
        return all(x == 0 for x in liste)
    q = Fraction(liste[1], liste[0])
    for i in range(len(liste) - 1):
        if liste[i + 1] != q * liste[i]:
            return False
    return True

def valeur_apres(valeur, taux, periodes):
    return round(valeur * (1 + taux / 100) ** periodes, 2)

def rang_depasse(u0, q, seuil):
    terme = u0
    n = 0
    while terme < seuil:
        terme = terme * q
        n = n + 1
    return n
```

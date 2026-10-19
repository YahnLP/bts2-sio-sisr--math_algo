# Corrigé S09

## Exercices

1. 23 : indice 5, 3 comparaisons ; 40 : absent, 4 comparaisons.
2. 10 ; 20 ; 1 000 et 1 000 000 au pire.
3. 5 multiplications contre 10.
4. [1, 2, 5, 6, 7, 9, 10].
5. [1, 2, 5, 7, 9].
6. 15 appels ; 4 niveaux.
7. 4 est jugé absent (liste non triée).

## TP Python – solutions

```python
def dicho(L, x):
    bas = 0
    haut = len(L) - 1
    while bas <= haut:
        milieu = (bas + haut) // 2
        if L[milieu] == x:
            return milieu
        if L[milieu] < x:
            bas = milieu + 1
        else:
            haut = milieu - 1
    return -1

def etapes_dicho(L, x):
    bas = 0
    haut = len(L) - 1
    etapes = 0
    while bas <= haut:
        milieu = (bas + haut) // 2
        etapes = etapes + 1
        if L[milieu] == x:
            return etapes
        if L[milieu] < x:
            bas = milieu + 1
        else:
            haut = milieu - 1
    return etapes

def puissance_rapide(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        y = puissance_rapide(x, n // 2)
        return y * y
    return x * puissance_rapide(x, n - 1)

def fusion(A, B):
    resultat = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            resultat.append(A[i])
            i = i + 1
        else:
            resultat.append(B[j])
            j = j + 1
    return resultat + A[i:] + B[j:]

def fusion(A, B):
    resultat = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            resultat.append(A[i])
            i = i + 1
        else:
            resultat.append(B[j])
            j = j + 1
    return resultat + A[i:] + B[j:]

def tri_fusion(L):
    if len(L) <= 1:
        return L
    milieu = len(L) // 2
    return fusion(tri_fusion(L[:milieu]), tri_fusion(L[milieu:]))

def nb_mult(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 1 + nb_mult(n // 2)
    return 1 + nb_mult(n - 1)
```

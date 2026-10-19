# Corrigé S14

## Exercices

1. 10 comparaisons ; `[1, 2, 5, 7, 9]`.
2. 7 comparaisons.
3. 5 ; 15.
4. 10 ; 20.
5. \(k = 11\).
6. \(10^8\) contre 1 677 964.

## TP Python – solutions

```python
def tri_selection(L):
    L = list(L)
    for i in range(len(L) - 1):
        m = i
        for j in range(i + 1, len(L)):
            if L[j] < L[m]:
                m = j
        L[i], L[m] = L[m], L[i]
    return L

def tri_insertion(L):
    L = list(L)
    for i in range(1, len(L)):
        x = L[i]
        j = i
        while j > 0 and L[j - 1] > x:
            L[j] = L[j - 1]
            j = j - 1
        L[j] = x
    return L

def comparaisons_selection(L):
    n = len(L)
    return n * (n - 1) // 2

def comparaisons_insertion(L):
    L = list(L)
    nb = 0
    for i in range(1, len(L)):
        x = L[i]
        j = i
        while j > 0:
            nb = nb + 1
            if L[j - 1] > x:
                L[j] = L[j - 1]
                j = j - 1
            else:
                break
        L[j] = x
    return nb

import math


def cout_recherches(n, k):
    seq = k * n
    tri = round(n * math.log2(n)) + k * (n.bit_length() - 1 + 1)
    return (seq, tri)

import math


def meilleur_choix(n, k):
    seq = k * n
    tri = round(n * math.log2(n)) + k * (n.bit_length() - 1 + 1)
    if seq <= tri:
        return "sequentielle"
    return "tri+dicho"
```

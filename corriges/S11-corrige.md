# Corrigé S11

## Exercices

1. Variant `n` ; 7 tours.
2. Boucle infinie ; `while i < 10`.
3. \(s = k(k+1)/2\) ​après \(k\) tours.
4. `m` = plus grand des \(k\) premiers.
5. \(p = x^k\).
6. Six tests dont un élément, répétitions, négatifs.
7. Non : `est_trie([1, 2, 0])` renvoie `True`.

## TP Python – solutions

```python
def tours_division(n):
    tours = 0
    while n > 0:
        n = n // 2
        tours = tours + 1
    return tours

def etats_somme(n):
    s = 0
    etats = [s]
    for i in range(1, n + 1):
        s = s + i
        etats.append(s)
    return etats

def maximum_boucle(L):
    m = L[0]
    for x in L:
        if x > m:
            m = x
    return m

def est_trie(L):
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            return False
    return True

def pgcd_boucle(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

# Corrigé S08

## Exercices

1. 12 (4 appels).
2. Cas de base : 1 élément ; `maximum([3, 9, 4]) = 9`.
3. `"radar"` vrai ; `"reseau"` faux ; variant `len(s)`.
4. `"cba"`.
5. 3.
6. 499 500 éléments copiés ; 0 avec indice ; profondeur 1 001 > limite.
7. 8.

## TP Python – solutions

```python
def somme_liste(L):
    if L == []:
        return 0
    return L[0] + somme_liste(L[1:])

def maximum(L):
    if len(L) == 1:
        return L[0]
    m = maximum(L[1:])
    if L[0] > m:
        return L[0]
    return m

def compte(L, x):
    if L == []:
        return 0
    if L[0] == x:
        return 1 + compte(L[1:], x)
    return compte(L[1:], x)

def est_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and est_palindrome(s[1:-1])

def inverse(s):
    if s == "":
        return ""
    return inverse(s[1:]) + s[0]

def somme_chiffres(n):
    if n < 10:
        return n
    return n % 10 + somme_chiffres(n // 10)
```

# Corrigé S06

## Exercices

1. 24 ; 5 appels.
2. \(S(0) = 0\), \(S(n) = n^2 + S(n-1)\) ; \(S(4) = 30\).
3. `f` : pas de cas de base ; `g` : `g(n - 1)`.
4. 21 ; variant `b`.
5. 11 appels ; \(n + 1\).
6. `"1101"` ; `"1010"`.
7. Version itérative ; récursive risque `RecursionError` pour \(n = 5\,000\).

## TP Python – solutions

```python
def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)

def somme_carres(n):
    if n == 0:
        return 0
    return n * n + somme_carres(n - 1)

def puissance(x, n):
    if n == 0:
        return 1
    return x * puissance(x, n - 1)

def pgcd(a, b):
    if b == 0:
        return a
    return pgcd(b, a % b)

def binaire(n):
    if n < 2:
        return str(n)
    return binaire(n // 2) + str(n % 2)
```

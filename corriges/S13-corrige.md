# Corrigé S13

## Exercices

1. \(O(n^2)\), \(O(n)\), \(O(1)\), \(O(n\log n)\).
2. \(c = 4\), \(n_0 = 5\).
3. 12 s ; 300 s.
4. \(O(n^2)\) ; \(O(n\log n)\).
5. ≈ 13,33.
6. ≈ 13 344 jours ≈ 36,5 ans (hypothèse \(10^9\) op/s).

## TP Python – solutions

```python
def ratio_doublement(f, n):
    return f(2 * n) / f(n)

def estime_ordre(f):
    r = f(128) / f(64)
    if r < 1.05:
        return "O(1)"
    if r < 1.5:
        return "O(log n)"
    if r < 2.1:
        return "O(n)"
    if r < 3:
        return "O(n log n)"
    if r < 5:
        return "O(n^2)"
    if r < 9:
        return "O(n^3)"
    return "O(2^n)"

def duree_jours(ops, par_seconde):
    return ops / par_seconde / 86400

def facteur_croissance(f, a, b):
    return f(b) / f(a)
```

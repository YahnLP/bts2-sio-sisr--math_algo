# Corrigé S07

## Exercices

1. 5, 9, 17, 33 ; \(u_n = 2^{n+1} + 1\).
2. 4 cadres ; \(n + 1\).
3. \(1, 2, 3, 5, 8, 13, 21, 34, 55\) ; \(C(6) = 25\), \(C(7) = 41\).
4. `fib(3)` 2 fois ; `fib(2)` 3 fois.
5. 59 appels.
6. 5 001 cadres : `RecursionError` ; ​version itérative.
7. Tableau \(a, b\) ; `fib_iter(6) = 8`.

## TP Python – solutions

```python
def u_rec(n):
    if n == 0:
        return 3
    return 2 * u_rec(n - 1) - 1

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def appels_fib(n):
    if n < 2:
        return 1
    return 1 + appels_fib(n - 1) + appels_fib(n - 2)

def fib_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n < 2:
        return n
    if n not in cache:
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

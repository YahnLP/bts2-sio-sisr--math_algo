# Corrigé S05

## Exercices

1. (a) \(\to 0\) ; (b) \(\to +\infty\) ; (c) \(\to -\infty\) ; (d) aucune limite.
2. \(10, 15, 17{,}5, 18{,}75\) ; \(L = 20\) ; \(u_n = 20 - 20 \times 0{,}5^n\) ; \(u_{10} = 19{,}98046875\).
3. Rang 8.
4. \(L = 150\) Go ; 120 Go insuffisant, plein au mois 6 ; 200 Go suffit.
5. \(n = 45\).
6. La boucle ne s'arrête pas (limite 20 < 25) ; garde-fou.

## TP Python – solutions

```python
def limite_geo(u0, q):
    if u0 == 0 or abs(q) < 1:
        return 0
    if q == 1:
        return u0
    if q > 1:
        return "+inf" if u0 > 0 else "-inf"
    return "aucune"

def point_fixe(a, b):
    return b / (1 - a)

def terme_affine(a, b, u0, n):
    L = point_fixe(a, b)
    return L + (u0 - L) * a ** n

def rang_seuil(f, u0, seuil, nmax):
    u = u0
    n = 0
    while u < seuil and n < nmax:
        u = f(u)
        n = n + 1
    if u >= seuil:
        return n
    return None

def rang_somme(seuil):
    n = 0
    somme = 0
    while somme < seuil:
        n = n + 1
        somme = somme + n
    return n

def rang_stable(f, u0, eps, nmax):
    u = u0
    for n in range(nmax + 1):
        suivant = f(u)
        if abs(suivant - u) < eps:
            return n
        u = suivant
    return None
```

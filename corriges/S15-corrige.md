# Corrigé S15

## Exercices

1. \(O(n^2)\) probable.
2. \(26^8 = 208\,827\,064\,576\) ; ≈ 209 s.
3. \(26^{12}\) ; ≈ 1 105 jours ≈ 3,03 ans.
4. \(62^{12}\) ; facteur ≈ 33 800.
5. 5 040 ; 362 880 ; 87 178 291 200.
6. ​Quasi linéaire contre quadratique ; coût en mémoire.

## TP Python – solutions

```python
import time


def temps_min(f, repetitions):
    meilleur = None
    for _ in range(repetitions):
        debut = time.perf_counter()
        f()
        duree = time.perf_counter() - debut
        if meilleur is None or duree < meilleur:
            meilleur = duree
    return meilleur

def essais_force_brute(taille_alphabet, longueur):
    return taille_alphabet ** longueur

def jours_force_brute(taille_alphabet, longueur, par_seconde):
    return taille_alphabet ** longueur / par_seconde / 86400

def nb_tournees(n):
    r = 1
    for k in range(2, n):
        r = r * k
    return r

def doublons_set(L):
    vus = set()
    for x in L:
        if x in vus:
            return True
        vus.add(x)
    return False
```

# Corrigé S10

## Exercices

1. `archives` 1 150 ; `docs` 1 300 ; racine 2 105.
2. 6 fichiers ; profondeur 3.
3. Liste des 6 ​chemins.
4. A, B, D, C, E ; {B, D}.
5. Récursion infinie (`RecursionError`).
6. Depuis R1 : R1, R2, R3, R4 ; depuis R5 : toutes.
7. 0, 0, 1.

## TP Python – solutions

```python
def taille(a):
    if isinstance(a, int):
        return a
    total = 0
    for v in a.values():
        total = total + taille(v)
    return total

def nb_fichiers(a):
    if isinstance(a, int):
        return 1
    total = 0
    for v in a.values():
        total = total + nb_fichiers(v)
    return total

def profondeur(a):
    if isinstance(a, int):
        return 0
    meilleur = 0
    for v in a.values():
        p = profondeur(v)
        if p > meilleur:
            meilleur = p
    return 1 + meilleur

def chemins(a, prefixe=""):
    resultat = []
    for nom, v in a.items():
        if isinstance(v, int):
            resultat.append(prefixe + nom)
        else:
            resultat = resultat + chemins(v, prefixe + nom + "/")
    return resultat

def dfs(g, sommet, visites=None):
    if visites is None:
        visites = []
    visites.append(sommet)
    for voisin in g[sommet]:
        if voisin not in visites:
            dfs(g, voisin, visites)
    return visites

def dfs(g, sommet, visites=None):
    if visites is None:
        visites = []
    visites.append(sommet)
    for voisin in g[sommet]:
        if voisin not in visites:
            dfs(g, voisin, visites)
    return visites

def atteignables(g, depart):
    return sorted(dfs(g, depart))
```

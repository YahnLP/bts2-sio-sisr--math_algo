# Corrigé S01

## Exercices

1. \(-3, 1, 5, 9, 13\) ; \(u_{10} = 37\).
2. \(5, 14, 41, 122\).
3. \(u_{n+1} = u_n + 15\) ; \(u_n = 120 + 15n\) ; \(u_6 = 210\) ; mois 12.
4. \(u_{n+1} - u_n = 2n - 5\) ; décroît jusqu'à \(u_3 = -9\) puis croît.
5. \(u = 47 = u_4\).
6. \(u_n = 4 + 7n\) ; \(u_{100} = 704\).
7. \(2, 3, 5, 8, 13\) ; garder deux termes.

## TP Python – solutions

```python
def terme_explicite(n):
    return 3 * n * n - n + 2

def terme_recurrent(u0, n):
    terme = u0
    for _ in range(n):
        terme = 2 * terme + 1
    return terme

def premiers_termes(f, u0, n):
    termes = [u0]
    for _ in range(n):
        termes.append(f(termes[-1]))
    return termes

def est_croissante(liste):
    for i in range(len(liste) - 1):
        if liste[i + 1] < liste[i]:
            return False
    return True

def mois_plein(depart, ajout, capacite):
    quantite = depart
    mois = 0
    while quantite < capacite:
        quantite = quantite + ajout
        mois = mois + 1
    return mois
```

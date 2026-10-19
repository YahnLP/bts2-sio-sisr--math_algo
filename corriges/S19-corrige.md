# Corrigé S19

## Exercices

### Sujet blanc (30 points)

**A1.** \(u_{n+1} = 1{,}03\,u_n\) : suite **géométrique** de raison 1,03, \(u_n = 200 \times 1{,}03^n\).

**A2.** \(u_{12} = 200 \times 1{,}03^{12} \approx 285{,}15\) Go.

**A3.** \(u_{13} \approx 293{,}71\) et \(u_{14} \approx 302{,}52\). La suite est croissante : le plus petit \(n\) est **14**. (Par logarithme : \(1{,}03^n > 1{,}5\) donne \(n > 13{,}7\).)

**A4.** `mois_seuil` (boucle `while u <= seuil`). La suite est strictement croissante et non majorée (raison > 1), donc elle dépasse tout seuil après un nombre fini de tours.

**B1.** Cas de base : liste vide, somme 0. Récursion : `L[0] + somme_rec(L[1:])`. Variant : la longueur de la liste.

**B2.** `somme_rec([4,1,3])` → `4 + somme_rec([1,3])` → `1 + somme_rec([3])` → `3 + somme_rec([])` → 0. Retours : 3, 4, 8. Résultat **8**.

**B3.** \(C(2) = 3\), \(C(3) = 5\), \(C(4) = 9\), \(C(5) = 15\).

**B4.** a) \(n^2 > 50n \iff n > 50\), donc \(n = 51\) (pour \(n = 50\) il y a égalité : 2500). b) \(\lfloor\log_2 10^6\rfloor + 1 = 20\) comparaisons ; 1 000 000 au pire en séquentielle.

**C1.** `rx = {"R1": {"R2": 3, "R3": 1}, "R2": {"R4": 2}, "R3": {"R2": 1, "R4": 6}, "R4": {"R5": 1}, "R5": {}}`.

**C2.** Parcours en largeur (file), car il visite par nombre de sauts croissant. Voir `sommets_a_k_sauts`.

**C3.** Dijkstra. R1 → R3 → R2 → R4 → R5 : \(1 + 1 + 2 + 1 = 5\) ms.

**C4.** La largeur minimise le **nombre de liaisons**, pas la somme des latences (R1 → R2 → R4 → R5 coûte 6, R1 → R3 → R2 → R4 → R5 coûte 5). Avec une latence négative, Dijkstra a déjà fixé des distances qui peuvent encore baisser : il n'est plus correct.

## TP Python – solutions

```python
def mois_seuil(u0, taux, seuil):
    n = 0
    u = u0
    while u <= seuil:
        u = u * (1 + taux)
        n = n + 1
    return n

def somme_rec(L):
    if len(L) == 0:
        return 0
    return L[0] + somme_rec(L[1:])

def appels_fib(n):
    if n < 2:
        return 1
    return appels_fib(n - 1) + appels_fib(n - 2) + 1

from collections import deque


def sommets_a_k_sauts(g, depart, k):
    dist = {depart: 0}
    file = deque([depart])
    while file:
        s = file.popleft()
        for v in g[s]:
            if v not in dist:
                dist[v] = dist[s] + 1
                file.append(v)
    return sorted(s for s in dist if dist[s] == k)

import heapq


def plus_court_cout(g, a, b):
    dist = {a: 0}
    tas = [(0, a)]
    while tas:
        d, s = heapq.heappop(tas)
        if d > dist[s]:
            continue
        for v, w in g[s].items():
            nd = d + w
            if v not in dist or nd < dist[v]:
                dist[v] = nd
                heapq.heappush(tas, (nd, v))
    return dist.get(b)
```

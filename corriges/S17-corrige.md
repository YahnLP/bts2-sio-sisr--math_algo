# Corrigé S17

## Exercices

1. `["C", "D", "E", "A", "B"]`.
2. A 0, B 1, C 1, D 2, E 2.
3. A → C (1 saut).
4. S 0, B 2, A 5, C 6.
5. Distances fixées trop tôt.
6. Dijkstra ; largeur.

## TP Python – solutions

```python
from collections import deque


def bfs(g, depart):
    vus = [depart]
    file = deque([depart])
    while file:
        s = file.popleft()
        for v in g[s]:
            if v not in vus:
                vus.append(v)
                file.append(v)
    return vus

from collections import deque


def distances_bfs(g, depart):
    dist = {depart: 0}
    file = deque([depart])
    while file:
        s = file.popleft()
        for v in g[s]:
            if v not in dist:
                dist[v] = dist[s] + 1
                file.append(v)
    return dist

from collections import deque


def chemin_bfs(g, a, b):
    parent = {a: None}
    file = deque([a])
    while file:
        s = file.popleft()
        for v in g[s]:
            if v not in parent:
                parent[v] = s
                file.append(v)
    if b not in parent:
        return None
    chemin = []
    s = b
    while s is not None:
        chemin.append(s)
        s = parent[s]
    chemin.reverse()
    return chemin

import heapq


def dijkstra(g, depart):
    dist = {depart: 0}
    tas = [(0, depart)]
    while tas:
        d, s = heapq.heappop(tas)
        if d > dist[s]:
            continue
        for v, w in g[s].items():
            nd = d + w
            if v not in dist or nd < dist[v]:
                dist[v] = nd
                heapq.heappush(tas, (nd, v))
    return dist

import heapq


def chemin_dijkstra(g, a, b):
    dist = {a: 0}
    parent = {a: None}
    tas = [(0, a)]
    while tas:
        d, s = heapq.heappop(tas)
        if d > dist[s]:
            continue
        for v, w in g[s].items():
            nd = d + w
            if v not in dist or nd < dist[v]:
                dist[v] = nd
                parent[v] = s
                heapq.heappush(tas, (nd, v))
    if b not in dist:
        return None
    chemin = []
    s = b
    while s is not None:
        chemin.append(s)
        s = parent[s]
    chemin.reverse()
    return (dist[b], chemin)
```

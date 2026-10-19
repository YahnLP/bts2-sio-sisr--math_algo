# Aide-mémoire – Graphes : parcours et plus court chemin

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S17*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Représentations

```python
g  = {"A": ["B", "C"], "B": []}              # non pondéré
gp = {"A": {"B": 4, "C": 1}, "B": {}}       # pondéré (poids)
```

## Algorithmes

| Besoin | Outil |
|---|---|
| Explorer, atteignabilité | profondeur (pile ou récursion) |
| Plus court en sauts | largeur (**file**) |
| Plus court en coût, poids \(\ge 0\) | Dijkstra (**tas** `heapq`) |

## Dijkstra en 3 lignes

1. `dist[départ] = 0`.
2. Traiter le sommet de plus petite distance.
3. `dist[v] = min(dist[v], dist[s] + poids)` pour chaque voisin.

Chemin : mémoriser le **parent**, puis remonter du but vers le départ.

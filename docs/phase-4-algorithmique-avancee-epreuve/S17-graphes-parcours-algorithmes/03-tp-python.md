---
render_macros: true
---

# TP Python – Largeur, chemins et Dijkstra

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S17*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Parcours en largeur

Écris `bfs(g, depart)` qui renvoie la liste des sommets dans l'ordre du parcours en largeur (avec une `deque`). Les voisins sont pris dans l'ordre de la liste.

**J'anticipe.** Reprends la trace de l'exercice 1.

{{ IDE('bfs', MAX="+") }}

## Exercice B – Distances en sauts

Écris `distances_bfs(g, depart)` qui renvoie un dictionnaire `sommet -> nombre de sauts minimal` pour les sommets atteignables (le départ est à 0).

**J'anticipe.** Écris les distances de l'exercice 2.

{{ IDE('distances_bfs', MAX="+") }}

## Exercice C – Chemin le plus court en sauts

Écris `chemin_bfs(g, a, b)` qui renvoie la liste des sommets d'un plus court chemin de `a` à `b` (en nombre de sauts), ou `None` si `b` n'est pas atteignable. Mémorise le parent de chaque sommet.

{{ IDE('chemin_bfs', MAX="+") }}

**Je comprends.** Pourquoi remonte-t-on du but vers le départ ?

## Exercice D – Dijkstra

Écris `dijkstra(g, depart)` pour un graphe pondéré (poids positifs ou nuls) : renvoie un dictionnaire `sommet -> distance minimale` pour les sommets atteignables. Utilise `heapq`.

**J'anticipe.** Reprends les traces du cours et de l'exercice 4.

{{ IDE('dijkstra', MAX="+") }}

## Exercice E – Dijkstra avec chemin

Écris `chemin_dijkstra(g, a, b)` qui renvoie `(distance, chemin)` pour un plus court chemin pondéré de `a` à `b`, ou `None` si `b` n'est pas atteignable. Mémorise les parents lors de chaque amélioration.

{{ IDE('chemin_dijkstra', MAX="+") }}

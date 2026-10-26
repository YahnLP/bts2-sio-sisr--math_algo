---
render_macros: true
---

# TP Python – Programmation du sujet blanc

*BTS SIO SISR 2e année – Pour aller plus loin – S19*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

> [!NOTE]
> Ce TP reprend les questions de programmation du [sujet blanc](02-exercices.md). Fais d'abord le sujet **sur papier**, dans le temps imparti, puis utilise ces éditeurs pour **vérifier** tes fonctions.


## Exercice A – Dossier A4 : mois de saturation

Écris `mois_seuil(u0, taux, seuil)` qui renvoie le plus petit entier `n` tel que `u0 * (1 + taux) ** n > seuil`, en calculant la suite **par une boucle** (sans logarithme). On suppose `u0 > 0` et `taux > 0`.

**J'anticipe.** Que vaut le résultat pour `200`, `0.03`, `300` (question A3) ?

{{ IDE('mois_seuil', MAX="+") }}

**Je comprends.** Pourquoi la boucle s'arrête-t-elle ? (la suite est strictement croissante et n'est pas majorée)

## Exercice B – Dossier B1 : somme récursive

Écris `somme_rec(L)` **récursive** (sans boucle ni `sum`) qui renvoie la somme des éléments de `L`.

**J'anticipe.** Écris la pile d'appels pour `[4, 1, 3]` (question B2).

{{ IDE('somme_rec', MAX="+") }}

## Exercice C – Dossier B3 : nombre d'appels

Écris `appels_fib(n)` qui renvoie le nombre d'appels \(C(n)\) de la question B3, **par récursivité** : `1` si `n < 2`, sinon `appels_fib(n - 1) + appels_fib(n - 2) + 1`.

{{ IDE('appels_fib', MAX="+") }}

## Exercice D – Dossier C2 : sommets à k sauts

Écris `sommets_a_k_sauts(g, depart, k)` : liste **triée** des sommets à exactement `k` sauts de `depart`. Le graphe `g` peut être un dictionnaire de listes ou un dictionnaire de dictionnaires (`for v in g[s]` donne les voisins dans les deux cas). Utilise un parcours en largeur.

**J'anticipe.** Pour le réseau `rx` du sujet, quels sommets sont à 2 sauts de R1 ?

{{ IDE('sommets_a_k_sauts', MAX="+") }}

## Exercice E – Dossier C3 : plus faible latence

Écris `plus_court_cout(g, a, b)` : latence minimale de `a` à `b` dans un graphe pondéré (poids positifs ou nuls), ou `None` si `b` est inatteignable. Utilise l'algorithme de Dijkstra avec `heapq`.

{{ IDE('plus_court_cout', MAX="+") }}

**Je comprends.** Donne la latence minimale de R1 à R5 et le chemin correspondant.

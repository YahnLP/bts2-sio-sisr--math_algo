# Synthèse – Graphes et ordonnancement

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – R4*

> [!NOTE]
> **Rôle de cette page.** Le vocabulaire, les représentations, les méthodes de calcul (puissances de la matrice d'adjacence, niveaux, MPM et PERT, chemin optimal) et les pièges. Le cours complet est dans le [site de 1re année](https://yahnlp.github.io/bts1-sio-sisr-math_algo/) (séances S16 et S17).

## I. Graphe orienté fini

Un graphe orienté est formé de **sommets** et d'**arcs** \((x, y)\) (flèche de \(x\) vers \(y\)). Pour un arc \((x, y)\), \(y\) est un **successeur** de \(x\) et \(x\) un **prédécesseur** de \(y\).

| Notion | Définition |
|---|---|
| **Chemin** | Suite d'arcs consécutifs ; sa **longueur** est le nombre d'arcs |
| **Circuit** | Chemin de longueur \(\ge 1\) dont le dernier sommet est le premier |
| **Boucle** | Circuit de longueur 1 (arc \((x, x)\)) |
| **Chemin hamiltonien** | Chemin qui passe **une fois et une seule** par chaque sommet |

**Représentations.** (1) Dessin. (2) **Tableau des successeurs** (ou des prédécesseurs). (3) **Matrice d'adjacence** \(M\) : \(m_{ij} = 1\) s'il existe un arc de \(i\) vers \(j\), 0 sinon.

## II. Calculs avec la matrice d'adjacence

- Le coefficient \((i, j)\) de \(M^p\) est le **nombre de chemins de longueur \(p\)** de \(i\) vers \(j\).
- **Fermeture transitive** : le graphe où l'on ajoute un arc \((x, y)\) dès qu'il existe un chemin de \(x\) vers \(y\). Sa matrice est obtenue en cumulant, en **arithmétique booléenne** (\(1 + 1 = 1\)), \(M \vee M^2 \vee \dots \vee M^n\).
- Un graphe **sans circuit** a une matrice \(M^p\) nulle pour \(p\) assez grand (au plus le nombre de sommets).

## III. Niveaux d'un graphe sans circuit

**Méthode.** Niveau 0 : les sommets sans prédécesseur. On les retire ; niveau 1 : les sommets qui deviennent sans prédécesseur ; et ainsi de suite jusqu'à épuisement. Si l'on est bloqué avant d'avoir tout retiré, **il y a un circuit**.

## IV. Ordonnancement : MPM et PERT

Un **projet** est un ensemble de **tâches** de durées \(d\) liées par des contraintes d'antériorité.

- **MPM** : une tâche est un **sommet** ; **PERT** : une tâche est un **arc**, les sommets sont des étapes, et un **arc fictif** (durée 0) rend compte d'une contrainte quand elle ne se lit pas directement. Les deux méthodes donnent les mêmes résultats.
- **Date au plus tôt** \(t(x) = \max_p\,(t(p) + d(p))\) sur les prédécesseurs (0 au début).
- **Durée du projet** : plus grand \(t(x) + d(x)\).
- **Date au plus tard** \(T(x) = \min_s T(s) - d(x)\) sur les successeurs (on remonte depuis la fin).
- **Marge totale** \(M_T = T - t\) ; **marge libre** \(M_L = \min_s t(s) - t(x) - d(x)\) ; **marge certaine** \(M_C = \max(0,\ \min_s t(s) - \max_p (T(p) + d(p)) - d(x))\). On a \(M_C \le M_L \le M_T\).
- **Tâche critique** : \(M_T = 0\). Le **chemin critique** les relie du début à la fin : tout retard sur lui retarde le projet.

> [!NOTE]
> Les noms « marge libre » et « marge certaine » varient selon les ouvrages : un énoncé d'examen rappelle la définition attendue. Le raisonnement reste le même.

## V. Graphe valué et chemin optimal

Un graphe est **valué** quand chaque arc porte un nombre (distance, coût, durée). La **valeur d'un chemin** est la somme des valeurs de ses arcs. Pour des valeurs positives, la **méthode de Dijkstra** donne le chemin de valeur minimale depuis un sommet : à chaque étape, on fixe le sommet non fixé de plus petite valeur provisoire et on met à jour ses successeurs.

> [!WARNING]
> **Pièges.** Confondre le sens des arcs ; oublier le sommet de départ de la numérotation des niveaux ; confondre **longueur** (nombre d'arcs) et **valeur** (somme des poids) ; mal ordonner les facteurs dans \(M^p\) (le produit n'est pas commutatif) ; oublier les **arcs fictifs** en PERT.

## À retenir pour le jour de l'épreuve

1. Donner **toujours le sens** de lecture (ligne = départ, colonne = arrivée).
2. Pour MPM : **tableau des tâches** (durée, prédécesseurs, \(t\), \(T\), marge), puis chemin critique et durée du projet.
3. Interpréter par une phrase (« il y a 3 chemins… », « le projet dure 14 jours… »).

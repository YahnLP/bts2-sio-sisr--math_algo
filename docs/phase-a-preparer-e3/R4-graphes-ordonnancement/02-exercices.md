# Exercices – Graphes et ordonnancement

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – R4*

> [!NOTE]
> **Comment travailler.** Cherche sur papier (dessins et tableaux), puis compare. Trois niveaux : **socle**, **format épreuve**, **pour aller plus loin** (au-delà du programme de l'épreuve).

## Niveau 1 – Socle

### Exercice 1 – Représenter un graphe

Un réseau de six services est décrit par les arcs suivants : \(1 \to 2\), \(1 \to 3\), \(2 \to 4\), \(3 \to 4\), \(3 \to 5\), \(4 \to 6\), \(5 \to 6\).

<figure class="graphe diagramme">
<svg viewBox="0 0 400 200" role="img" aria-label="Graphe orienté à 6 sommets et 7 arcs">
<line class="dg-line" x1="54.9" y1="91.8" x2="124.2" y2="53.7"/>
<polygon class="dg-ah" points="124.2,53.7 118.3,61.5 114.4,54.5"/>
<line class="dg-line" x1="54.9" y1="108.2" x2="124.2" y2="146.3"/>
<polygon class="dg-ah" points="124.2,146.3 114.4,145.5 118.3,138.5"/>
<line class="dg-line" x1="157.0" y1="45.0" x2="232.0" y2="45.0"/>
<polygon class="dg-ah" points="232.0,45.0 223.0,49.0 223.0,41.0"/>
<line class="dg-line" x1="152.0" y1="143.0" x2="237.3" y2="57.7"/>
<polygon class="dg-ah" points="237.3,57.7 233.7,66.9 228.1,61.3"/>
<line class="dg-line" x1="157.0" y1="155.0" x2="232.0" y2="155.0"/>
<polygon class="dg-ah" points="232.0,155.0 223.0,159.0 223.0,151.0"/>
<line class="dg-line" x1="264.9" y1="53.2" x2="334.2" y2="91.3"/>
<polygon class="dg-ah" points="334.2,91.3 324.4,90.5 328.3,83.5"/>
<line class="dg-line" x1="264.9" y1="146.8" x2="334.2" y2="108.7"/>
<polygon class="dg-ah" points="334.2,108.7 328.3,116.5 324.4,109.5"/>
<circle class="dg-box" cx="40" cy="100" r="17"/><text class="dg-t" x="40" y="105" text-anchor="middle">1</text>
<circle class="dg-box" cx="140" cy="45" r="17"/><text class="dg-t" x="140" y="50" text-anchor="middle">2</text>
<circle class="dg-box" cx="140" cy="155" r="17"/><text class="dg-t" x="140" y="160" text-anchor="middle">3</text>
<circle class="dg-box" cx="250" cy="45" r="17"/><text class="dg-t" x="250" y="50" text-anchor="middle">4</text>
<circle class="dg-box" cx="250" cy="155" r="17"/><text class="dg-t" x="250" y="160" text-anchor="middle">5</text>
<circle class="dg-box" cx="350" cy="100" r="17"/><text class="dg-t" x="350" y="105" text-anchor="middle">6</text>
</svg>
</figure>

1. Dresser le tableau des successeurs et celui des prédécesseurs.
2. Écrire la matrice d'adjacence \(M\) (sommets pris dans l'ordre 1 à 6).

<details markdown="1">
<summary>Voir la réponse</summary>

1.

| Sommet | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Successeurs | 2, 3 | 4 | 4, 5 | 6 | 6 | — |
| Prédécesseurs | — | 1 | 1 | 2, 3 | 3 | 4, 5 |

2. \(M = \begin{pmatrix} 0&1&1&0&0&0 \\ 0&0&0&1&0&0 \\ 0&0&0&1&1&0 \\ 0&0&0&0&0&1 \\ 0&0&0&0&0&1 \\ 0&0&0&0&0&0 \end{pmatrix}\), la ligne est le sommet de départ, la colonne le sommet d'arrivée.

</details>

### Exercice 2 – Vocabulaire

<figure class="graphe diagramme">
<svg viewBox="0 0 420 170" role="img" aria-label="Graphe orienté avec un circuit">
<line class="dg-line" x1="74.6" y1="91.3" x2="144.6" y2="49.3"/>
<polygon class="dg-ah" points="144.6,49.3 138.9,57.3 134.8,50.5"/>
<line class="dg-line" x1="174.6" y1="48.7" x2="244.6" y2="90.7"/>
<polygon class="dg-ah" points="244.6,90.7 234.8,89.5 238.9,82.7"/>
<line class="dg-line" x1="243.0" y1="100.0" x2="78.0" y2="100.0"/>
<polygon class="dg-ah" points="78.0,100.0 87.0,96.0 87.0,104.0"/>
<line class="dg-line" x1="277.0" y1="100.0" x2="342.0" y2="100.0"/>
<polygon class="dg-ah" points="342.0,100.0 333.0,104.0 333.0,96.0"/>
<circle class="dg-box" cx="60" cy="100" r="17"/><text class="dg-t" x="60" y="105" text-anchor="middle">1</text>
<circle class="dg-box" cx="160" cy="40" r="17"/><text class="dg-t" x="160" y="45" text-anchor="middle">2</text>
<circle class="dg-box" cx="260" cy="100" r="17"/><text class="dg-t" x="260" y="105" text-anchor="middle">3</text>
<circle class="dg-box" cx="360" cy="100" r="17"/><text class="dg-t" x="360" y="105" text-anchor="middle">4</text>
</svg>
</figure>

Dans ce graphe (arcs \(1 \to 2\), \(2 \to 3\), \(3 \to 1\), \(3 \to 4\)), citer un chemin de longueur 3 de 1 à 4, un circuit, et dire s'il y a une boucle. Existe-t-il un chemin hamiltonien ?

<details markdown="1">
<summary>Voir la réponse</summary>

Chemin de longueur 3 de 1 à 4 : \(1 \to 2 \to 3 \to 4\). Circuit : \(1 \to 2 \to 3 \to 1\) (longueur 3). **Pas de boucle** (aucun arc \((x, x)\)). Chemin hamiltonien : \(1 \to 2 \to 3 \to 4\) passe une fois par chacun des 4 sommets : **oui**.

</details>

### Exercice 3 – Nombre de chemins

Pour le graphe de l'exercice 1, on donne \(M^2\) et \(M^3\) (seuls les coefficients non nuls sont indiqués) : \(M^2\) a pour coefficients non nuls \((1,4) = 2\), \((1,5) = 1\), \((2,6) = 1\), \((3,6) = 2\) ; \(M^3\) n'a qu'un coefficient non nul, \((1,6) = 3\).

1. Combien y a-t-il de chemins de longueur 3 du sommet 1 au sommet 6 ? Les citer.
2. Que signifie \((1,4) = 2\) dans \(M^2\) ?
3. Que dire de \(M^4\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. **3 chemins** : \(1 \to 2 \to 4 \to 6\), \(1 \to 3 \to 4 \to 6\), \(1 \to 3 \to 5 \to 6\).
2. Il y a 2 chemins de longueur 2 de 1 à 4 : \(1 \to 2 \to 4\) et \(1 \to 3 \to 4\).
3. Le plus long chemin a une longueur 3, donc \(M^4 = 0\) : **le graphe n'a pas de circuit**.

</details>

### Exercice 4 – Niveaux

Déterminer les niveaux du graphe de l'exercice 1.

<details markdown="1">
<summary>Voir la réponse</summary>

Niveau 0 : \(\{1\}\) (aucun prédécesseur). On retire 1 : niveau 1 : \(\{2, 3\}\). On retire 2 et 3 : niveau 2 : \(\{4, 5\}\). Niveau 3 : \(\{6\}\). Tous les sommets sont placés : pas de circuit. Chaque arc va d'un niveau vers un niveau supérieur.

</details>

## Niveau 2 – Format épreuve

### Exercice 5 – Fermeture transitive

Pour le graphe de l'exercice 2, donner la matrice de la fermeture transitive et la décrire par des phrases.

<details markdown="1">
<summary>Voir la réponse</summary>

Les sommets 1, 2, 3 forment un circuit : chacun atteint les deux autres et lui-même, ainsi que 4. Le sommet 4 n'a aucun successeur.

\[
\begin{pmatrix} 1&1&1&1 \\ 1&1&1&1 \\ 1&1&1&1 \\ 0&0&0&0 \end{pmatrix}
\]

Les 1 sur la diagonale des lignes 1 à 3 traduisent l'existence d'un **circuit** passant par ces sommets.

</details>

### Exercice 6 – Ordonnancement MPM

Une migration de messagerie est découpée en 7 tâches (durées en jours).

| Tâche | Désignation | Durée | Prédécesseurs |
|---|---|---|---|
| A | Cadrage | 2 | — |
| B | Sauvegarde | 3 | A |
| C | Installation du serveur | 4 | A |
| D | Migration des comptes | 5 | B, C |
| E | Formation des utilisateurs | 3 | C |
| F | Tests | 2 | D |
| G | Bascule | 1 | E, F |

1. Déterminer les dates au plus tôt, la durée minimale du projet, puis les dates au plus tard.
2. Calculer les marges totales. En déduire les tâches critiques et le chemin critique.
3. Calculer la marge libre et la marge certaine de B et de E. Interpréter pour E.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Dates au plus tôt \(t\) : A 0 ; B 2 ; C 2 ; D \(\max(2+3,\ 2+4) = 6\) ; E 6 ; F \(6 + 5 = 11\) ; G \(\max(6 + 3,\ 11 + 2) = 13\). Fin : \(13 + 1 = \mathbf{14}\) **jours**. Dates au plus tard \(T\) (en remontant depuis 14) : G \(14 - 1 = 13\) ; F \(13 - 2 = 11\) ; E \(13 - 3 = 10\) ; D \(11 - 5 = 6\) ; C \(\min(6,\ 10) - 4 = 2\) ; B \(6 - 3 = 3\) ; A \(\min(3,\ 2) - 2 = 0\).
2.

| Tâche | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| \(t\) | 0 | 2 | 2 | 6 | 6 | 11 | 13 |
| \(T\) | 0 | 3 | 2 | 6 | 10 | 11 | 13 |
| \(M_T = T - t\) | 0 | 1 | 0 | 0 | 4 | 0 | 0 |

Tâches critiques (\(M_T = 0\)) : A, C, D, F, G. **Chemin critique : A → C → D → F → G** (\(2 + 4 + 5 + 2 + 1 = 14\)).
3. B : \(M_L = t(D) - t(B) - d(B) = 6 - 2 - 3 = 1\) ; \(M_C = \max(0,\ 6 - (T(A) + d(A)) - 3) = 6 - 2 - 3 = 1\). E : \(M_L = t(G) - t(E) - d(E) = 13 - 6 - 3 = 4\) ; \(M_C = \max(0,\ 13 - (T(C) + d(C)) - 3) = 13 - 6 - 3 = 4\). La formation (E) peut **glisser de 4 jours** sans retarder la bascule, même si l'installation (C) se termine au plus tard.

</details>

### Exercice 7 – Lire et construire un PERT

Quatre tâches : A (3 jours, sans prédécesseur), B (2 jours, après A), C (4 jours, après A), D (1 jour, après B **et** C).

1. Représenter le projet en PERT (étapes numérotées). Justifier l'arc fictif.
2. Calculer la durée du projet et le chemin critique.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Étapes : 1 (début), 2 (fin de A), 3 (fin de B), 4 (fin de C), 5 (fin du projet). Arcs : A : \(1 \to 2\) ; B : \(2 \to 3\) ; C : \(2 \to 4\) ; D : \(4 \to 5\) ; **arc fictif** \(3 \to 4\) de durée 0, car D ne peut commencer qu'après B **et** C : B et C se terminent en deux étapes différentes, et le fictif impose que l'étape 4 attende aussi la fin de B.
2. Dates des étapes : 1 : 0 ; 2 : 3 ; 3 : \(3 + 2 = 5\) ; 4 : \(\max(3 + 4,\ 5 + 0) = 7\) ; 5 : \(7 + 1 = 8\). Durée : **8 jours**. Chemin critique : \(A \to C \to D\) (\(3 + 4 + 1 = 8\)). La tâche B a 2 jours de marge.

</details>

### Exercice 8 – Chemin de valeur minimale (Dijkstra)

Un réseau relie six sites. Valeurs des arcs (en ms) : A→B 4, A→C 2, B→C 1, B→D 5, C→B 1, C→D 8, C→E 10, D→E 2, D→F 6, E→F 3.

1. Appliquer la méthode de Dijkstra depuis A.
2. Donner le chemin de valeur minimale de A à F et sa valeur.

<details markdown="1">
<summary>Voir la réponse</summary>

1. On fixe un sommet à chaque étape (valeur provisoire entre parenthèses) :

| Étape | Sommet fixé | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 0 | A (0) | 4 | 2 | — | — | — |
| 1 | C (2) | 3 | | 10 | 12 | — |
| 2 | B (3) | | | 8 | 12 | — |
| 3 | D (8) | | | | 10 | 14 |
| 4 | E (10) | | | | | 13 |
| 5 | F (13) | | | | | |

2. En remontant les prédécesseurs : F ← E ← D ← B ← C ← A. Chemin **A → C → B → D → E → F**, de valeur \(2 + 1 + 5 + 2 + 3 = \mathbf{13}\) ms.

</details>

## Niveau 3 – Pour aller plus loin

> [!NOTE]
> Hors programme de l'épreuve : algorithme de Warshall et parcours en largeur. Ils sont au programme des cours d'algorithmique de licence.

### Exercice 9 – L'algorithme de Warshall

La fermeture transitive peut se calculer sans puissances de matrices.

```python
def warshall(M):
    n = len(M)
    R = [ligne[:] for ligne in M]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                R[i][j] = R[i][j] or (R[i][k] and R[k][j])
    return R
```

1. Exécuter `warshall` sur la matrice du graphe de l'exercice 2. Que retrouve-t-on ?
2. Quel est le nombre d'opérations en fonction de \(n\) ? Comparer avec le calcul de \(M^p\) pour \(p = 1, \dots, n\).
3. Que signifie la valeur `R[i][k] and R[k][j]` ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. Sur \(M = \begin{pmatrix} 0&1&0&0 \\ 0&0&1&0 \\ 1&0&0&1 \\ 0&0&0&0 \end{pmatrix}\), on obtient \(\begin{pmatrix} 1&1&1&1 \\ 1&1&1&1 \\ 1&1&1&1 \\ 0&0&0&0 \end{pmatrix}\), la matrice de l'exercice 5.
2. Trois boucles imbriquées de \(n\) tours : \(n^3\) opérations. Calculer \(M^2, \dots, M^n\) demande \(n - 1\) produits de \(n^3\) opérations chacun, soit de l'ordre de \(n^4\) : Warshall est plus économe.
3. Il existe un chemin de \(i\) à \(j\) passant par le sommet intermédiaire \(k\) : un chemin de \(i\) à \(k\), puis un chemin de \(k\) à \(j\). À l'étape \(k\), on autorise \(0, \dots, k\) comme intermédiaires.

</details>

### Exercice 10 – Parcours en largeur

```python
from collections import deque

def parcours_largeur(succ, depart):
    dist = {depart: 0}
    file = deque([depart])
    while file:
        x = file.popleft()
        for y in succ[x]:
            if y not in dist:
                dist[y] = dist[x] + 1
                file.append(y)
    return dist
```

1. Exécuter `parcours_largeur` sur le graphe de l'exercice 1 avec `succ = {1: [2, 3], 2: [4], 3: [4, 5], 4: [6], 5: [6], 6: []}` depuis le sommet 1.
2. Que représente `dist[y]` ? Le comparer aux niveaux de l'exercice 4.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Le résultat est `{1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3}`.
2. `dist[y]` est le **nombre minimal d'arcs** d'un chemin de 1 à \(y\). Ici ils coïncident avec les niveaux, parce que tous les chemins de 1 vers un sommet ont la même longueur. En général, ce n'est pas le cas : dans un graphe sans circuit, le niveau d'un sommet est la longueur du **plus long** chemin qui y arrive, la distance en largeur celle du **plus court**.

</details>

## Auto-évaluation

- [ ] Je passe sans erreur entre dessin, tableaux et matrice d'adjacence.
- [ ] Je lis dans \(M^p\) le nombre de chemins de longueur \(p\).
- [ ] Je calcule les niveaux d'un graphe sans circuit.
- [ ] Je construis le tableau MPM complet (\(t\), \(T\), marges) et le chemin critique.
- [ ] Je traduis un projet en PERT avec un arc fictif.
- [ ] J'applique la méthode de Dijkstra et je justifie le chemin obtenu.

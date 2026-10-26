# Sujet 4 – La migration vers un nouveau centre de données (2 heures, 20 points)

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – sujet d'entraînement de l'auteur, **non officiel***

> [!NOTE]
> **Conditions.** Compose ce sujet **sans aide** et **chronométré** (2 heures). Les trois exercices sont indépendants. Calculatrice : selon les règles de la session. Chaque réponse est **justifiée**. Le corrigé et le barème sont dans les blocs « Voir le corrigé ».
>
> **Répartition indicative :** exercice 1 (graphes) 7 points, exercice 2 (matrices) 5 points, exercice 3 (programmation) 8 points.

## Exercice 1 – Le réseau inter-sites (7 points)

Six sites sont reliés par des liaisons à sens unique. Le graphe ci-dessous indique, sur chaque arc, la latence en millisecondes.

<figure class="graphe diagramme">
<svg viewBox="0 0 430 210" role="img" aria-label="Graphe valué de six sites">
<line class="dg-line" x1="54.6" y1="91.4" x2="134.5" y2="44.2"/>
<polygon class="dg-ah" points="134.5,44.2 128.8,52.2 124.7,45.3"/>
<text class="dg-s" x="100.2" y="81.2" text-anchor="middle">7</text>
<line class="dg-line" x1="54.6" y1="108.6" x2="134.5" y2="155.8"/>
<polygon class="dg-ah" points="134.5,155.8 124.7,154.7 128.8,147.8"/>
<text class="dg-s" x="89.0" y="145.7" text-anchor="middle">3</text>
<line class="dg-line" x1="150.0" y1="148.0" x2="150.0" y2="53.0"/>
<polygon class="dg-ah" points="150.0,53.0 154.0,62.0 146.0,62.0"/>
<text class="dg-s" x="161.0" y="104.5" text-anchor="middle">2</text>
<line class="dg-line" x1="166.2" y1="40.2" x2="257.9" y2="69.5"/>
<polygon class="dg-ah" points="257.9,69.5 248.1,70.6 250.5,63.0"/>
<text class="dg-s" x="208.7" y="69.3" text-anchor="middle">4</text>
<line class="dg-line" x1="163.8" y1="155.1" x2="260.4" y2="85.5"/>
<polygon class="dg-ah" points="260.4,85.5 255.4,94.0 250.8,87.5"/>
<text class="dg-s" x="218.5" y="133.2" text-anchor="middle">9</text>
<line class="dg-line" x1="166.9" y1="166.4" x2="257.1" y2="173.6"/>
<polygon class="dg-ah" points="257.1,173.6 247.8,176.8 248.4,168.9"/>
<text class="dg-s" x="211.1" y="184.9" text-anchor="middle">6</text>
<line class="dg-line" x1="290.7" y1="81.4" x2="368.3" y2="113.2"/>
<polygon class="dg-ah" points="368.3,113.2 358.5,113.5 361.5,106.1"/>
<text class="dg-s" x="325.4" y="111.5" text-anchor="middle">3</text>
<line class="dg-line" x1="275.0" y1="158.0" x2="275.0" y2="93.0"/>
<polygon class="dg-ah" points="275.0,93.0 279.0,102.0 271.0,102.0"/>
<text class="dg-s" x="286.0" y="129.5" text-anchor="middle">1</text>
<line class="dg-line" x1="290.2" y1="167.4" x2="368.9" y2="128.0"/>
<polygon class="dg-ah" points="368.9,128.0 362.6,135.7 359.1,128.5"/>
<text class="dg-s" x="334.5" y="161.6" text-anchor="middle">8</text>
<circle class="dg-box" cx="40" cy="100" r="17"/><text class="dg-t" x="40" y="105" text-anchor="middle">S1</text>
<circle class="dg-box" cx="150" cy="35" r="17"/><text class="dg-t" x="150" y="40" text-anchor="middle">S2</text>
<circle class="dg-box" cx="150" cy="165" r="17"/><text class="dg-t" x="150" y="170" text-anchor="middle">S3</text>
<circle class="dg-box" cx="275" cy="75" r="17"/><text class="dg-t" x="275" y="80" text-anchor="middle">S4</text>
<circle class="dg-box" cx="275" cy="175" r="17"/><text class="dg-t" x="275" y="180" text-anchor="middle">S5</text>
<circle class="dg-box" cx="385" cy="120" r="17"/><text class="dg-t" x="385" y="125" text-anchor="middle">S6</text>
</svg>
</figure>

**1. (2 points)**

a) Dresser le tableau des successeurs de chaque site.
b) Déterminer les niveaux du graphe (il n'a pas de circuit).

**2. (4 points)** Par la méthode de Dijkstra, déterminer la latence minimale de S1 à chacun des autres sites. Présenter le déroulement dans un tableau. Donner un chemin de latence minimale de S1 à S6 et sa valeur.

**3. (1 point)** Combien y a-t-il de chemins **de longueur 2** (deux arcs) de S1 à S4 ? Les citer.

<details markdown="1">
<summary>Voir le corrigé de l'exercice 1</summary>

**1. (2 pts)**

a) *(1)*

| Site | S1 | S2 | S3 | S4 | S5 | S6 |
|---|---|---|---|---|---|---|
| Successeurs | S2, S3 | S4 | S2, S4, S5 | S6 | S4, S6 | — |

b) *(1)* Niveau 0 : S1. On retire S1 : niveau 1 : S3. On retire S3 : niveau 2 : S2, S5. On retire S2, S5 : niveau 3 : S4. Niveau 4 : S6. **Niveaux : \(\{S1\}\), \(\{S3\}\), \(\{S2, S5\}\), \(\{S4\}\), \(\{S6\}\).**

**2. (4 pts)** On fixe à chaque étape le site non fixé de plus petite valeur provisoire.

| Étape | Site fixé | S2 | S3 | S4 | S5 | S6 |
|---|---|---|---|---|---|---|
| 0 | S1 (0) | 7 | 3 | — | — | — |
| 1 | S3 (3) | 5 | | 12 | 9 | — |
| 2 | S2 (5) | | | 9 | 9 | — |
| 3 | S4 (9) | | | | 9 | 12 |
| 4 | S5 (9) | | | | | 12 |
| 5 | S6 (12) | | | | | |

Détail : après S3, \(S2 = \min(7,\ 3 + 2) = 5\), \(S4 = 3 + 9 = 12\), \(S5 = 3 + 6 = 9\). Après S2, \(S4 = \min(12,\ 5 + 4) = 9\). Après S4, \(S6 = 9 + 3 = 12\). Après S5 (9), \(S4 = \min(9,\ 9 + 1) = 9\) et \(S6 = \min(12,\ 9 + 8) = 12\) : rien ne change.

Latences minimales depuis S1 : S2 : 5 ; S3 : 3 ; S4 : 9 ; S5 : 9 ; S6 : 12. En remontant les prédécesseurs : S6 ← S4 ← S2 ← S3 ← S1. Chemin **S1 → S3 → S2 → S4 → S6**, de valeur \(3 + 2 + 4 + 3 = \mathbf{12}\) ms.

*Barème : initialisation et choix du sommet (1), mises à jour correctes (1,5), table complète (0,5), chemin et valeur (1).*

**3. (1 pt)** Il y en a **2** : \(S1 \to S2 \to S4\) et \(S1 \to S3 \to S4\) (le coefficient \((S1, S4)\) de \(M^2\) vaut 2).

</details>

## Exercice 2 – Facturation et système (5 points)

**1. (2 points)** Un hébergeur facture trois ressources : des heures de calcul, des gigaoctets de stockage et des gigaoctets transférés. Le tableau donne la consommation de deux services ; les tarifs par unité sont 10 €, 20 € et 5 €.

| | Calcul (h) | Stockage (Go) | Transfert (Go) |
|---|---|---|---|
| Web | 2 | 1 | 4 |
| Messagerie | 1 | 3 | 2 |

a) Écrire la matrice \(C\) des consommations et la matrice colonne \(T\) des tarifs. Quelle est la taille de \(CT\) ?
b) Calculer \(CT\) et interpréter chaque coefficient.

**2. (3 points)** Trois licences ont pour prix \(x\), \(y\), \(z\) (en euros). Trois commandes donnent :

\[
\begin{cases} x + 2y = 8 \\ y + 3z = 15 \\ z = 4 \end{cases}
\]

On donne \(N = \begin{pmatrix} 1 & -2 & 6 \\ 0 & 1 & -3 \\ 0 & 0 & 1 \end{pmatrix}\) et \(A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \\ 0 & 0 & 1 \end{pmatrix}\).

a) Écrire le système sous la forme \(AX = B\).
b) Vérifier que \(N\) est l'inverse de \(A\).
c) Calculer \(X\) et vérifier le résultat.

<details markdown="1">
<summary>Voir le corrigé de l'exercice 2</summary>

**1. (2 pts)**

a) *(0,75)* \(C = \begin{pmatrix} 2 & 1 & 4 \\ 1 & 3 & 2 \end{pmatrix}\) (\(2 \times 3\)) et \(T = \begin{pmatrix} 10 \\ 20 \\ 5 \end{pmatrix}\) (\(3 \times 1\)). Le produit \(CT\) est défini (3 colonnes, 3 lignes) et de taille \(2 \times 1\).
b) *(1,25)* \(CT = \begin{pmatrix} 2 \cdot 10 + 1 \cdot 20 + 4 \cdot 5 \\ 1 \cdot 10 + 3 \cdot 20 + 2 \cdot 5 \end{pmatrix} = \begin{pmatrix} 60 \\ 80 \end{pmatrix}\). Le service Web est facturé **60 €** et la messagerie **80 €**.

**2. (3 pts)**

a) *(0,75)* \(X = \begin{pmatrix} x \\ y \\ z \end{pmatrix}\), \(B = \begin{pmatrix} 8 \\ 15 \\ 4 \end{pmatrix}\), \(AX = B\).
b) *(1,25)* \(AN\) : ligne 1 de \(A\) par les colonnes de \(N\) : \((1, 2, 0) \cdot (1, 0, 0) = 1\) ; \((1, 2, 0) \cdot (-2, 1, 0) = 0\) ; \((1, 2, 0) \cdot (6, -3, 1) = 0\). Ligne 2 \((0, 1, 3)\) : \(0\) ; \(1\) ; \(-3 + 3 = 0\). Ligne 3 \((0, 0, 1)\) : \(0\) ; \(0\) ; \(1\). On obtient \(I_3\) : \(N = A^{-1}\).
c) *(1)* \(X = NB = \begin{pmatrix} 8 - 30 + 24 \\ 15 - 12 \\ 4 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \\ 4 \end{pmatrix}\) : **2 €, 3 € et 4 €**. Vérification : \(2 + 6 = 8\) ; \(3 + 12 = 15\) ; \(4 = 4\).

</details>

## Exercice 3 – Relevés, tableaux à deux dimensions et débogage (8 points)

**1. (2 points)** On donne la fonction suivante.

```python
def mystere(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

a) Dresser le tableau de suivi pour `mystere(252, 198)` et donner la valeur retournée.
b) Quel est le rôle de cette fonction ?

**2. (3 points)** Un tableau `T` à deux dimensions contient les températures relevées (en °C) : chaque **ligne** est une baie, chaque **colonne** une heure.

```python
T = [[21, 23, 22, 25],
     [30, 31, 29, 33],
     [24, 26, 27, 25]]
```

a) Écrire `moyennes(T)` qui retourne la liste des moyennes de chaque ligne. Que retourne-t-elle pour `T` ?
b) Écrire `baies_en_alerte(T, seuil)` qui retourne la liste des numéros de lignes dont le **maximum** dépasse **strictement** `seuil`. Que retourne `baies_en_alerte(T, 28)` ?

**3. (3 points)** Un développeur écrit une fonction qui crée une matrice nulle.

```python
def zeros(p, q):
    return [[0] * q] * p

M = zeros(2, 3)
M[0][1] = 5
print(M)
```

a) Que s'affiche-t-il ? Pourquoi est-ce surprenant ?
b) Expliquer la cause (indication : combien de listes distinctes existe-t-il ?).
c) Corriger la fonction.

<details markdown="1">
<summary>Voir le corrigé de l'exercice 3</summary>

**1. (2 pts)**

a) *(1,5)*

| Tour | `a` avant | `b` avant | `a % b` | `a`, `b` après |
|---|---|---|---|---|
| 1 | 252 | 198 | 54 | 198, 54 |
| 2 | 198 | 54 | 36 | 54, 36 |
| 3 | 54 | 36 | 18 | 36, 18 |
| 4 | 36 | 18 | 0 | 18, 0 |

Retour : **18**.
b) *(0,5)* La fonction calcule le **PGCD** de `a` et `b` (algorithme d'Euclide).

**2. (3 pts)**

a) *(1,5)*

```python
def moyennes(T):
    resultat = []
    for ligne in T:
        total = 0
        for v in ligne:
            total = total + v
        resultat.append(total / len(ligne))
    return resultat
```

`moyennes(T)` retourne `[22.75, 30.75, 25.5]`.
b) *(1,5)*

```python
def baies_en_alerte(T, seuil):
    numeros = []
    for i in range(len(T)):
        if max(T[i]) > seuil:
            numeros.append(i)
    return numeros
```

`baies_en_alerte(T, 28)` retourne `[1]` : seule la ligne 1 (maximum 33) dépasse 28.

**3. (3 pts)**

a) *(1)* Le programme affiche `[[0, 5, 0], [0, 5, 0]]` : **les deux lignes** ont été modifiées alors qu'on n'a affecté qu'une seule case.
b) *(1)* L'expression `[[0] * q] * p` construit **une seule** liste `[0] * q`, puis répète **p fois la même référence** : les \(p\) « lignes » désignent le même objet. Modifier une ligne modifie donc toutes les autres (effet de bord par partage de référence).
c) *(1)*

```python
def zeros(p, q):
    return [[0] * q for _ in range(p)]
```

Cette version crée une **nouvelle** liste à chaque tour. `zeros(2, 3)` suivie de `M[0][1] = 5` donne `[[0, 5, 0], [0, 0, 0]]`.

</details>

## Barème récapitulatif

| Exercice | Points |
|---|---|
| 1. Graphes | 7 |
| 2. Matrices | 5 |
| 3. Programmation | 8 |
| **Total** | **20** |

> [!NOTE]
> **Auto-évaluation.** Sous 10 points : reprendre R4 (graphes), R2 (matrices) et R5 (programmation). Au-dessus de 15 : refaire un sujet complet en conditions réelles, puis passer aux exercices « pour aller plus loin ».

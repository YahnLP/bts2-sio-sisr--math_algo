# Synthèse – Calcul matriciel

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – R2*

> [!NOTE]
> **Rôle de cette page.** L'essentiel du programme (définitions, opérations, inverse, systèmes), les méthodes et les pièges. Le cours complet est dans le [site de 1re année](https://yahnlp.github.io/bts1-sio-sisr-math_algo/) (séances S13 et S14).

## I. Matrices et opérations

Une matrice \(A\) de taille \(p \times n\) a \(p\) **lignes** et \(n\) **colonnes** ; \(a_{ij}\) est le coefficient de la ligne \(i\), colonne \(j\). Une matrice est **carrée** si \(p = n\), **nulle** si tous ses coefficients sont nuls ; la **matrice identité** \(I_n\) a des 1 sur la diagonale et des 0 ailleurs.

| Opération | Condition | Résultat |
|---|---|---|
| \(A + B\), \(A - B\) | Mêmes tailles | Coefficient par coefficient |
| \(\lambda A\) | Aucune | Chaque coefficient multiplié par \(\lambda\) |
| \(A \times B\) | Colonnes de \(A\) = lignes de \(B\) : \((p \times n)(n \times q)\) | Matrice \(p \times q\) ; \(c_{ij} = \sum_k a_{ik}\,b_{kj}\) |

**Ligne par colonne.** Pour \(c_{ij}\) : on multiplie la ligne \(i\) de \(A\) par la colonne \(j\) de \(B\), terme à terme, puis on additionne.

> [!WARNING]
> **Pièges.** Le produit **n'est pas commutatif** : \(AB \ne BA\) en général (et l'un peut exister sans l'autre). \(AI = IA = A\). Il n'y a **pas de division** de matrices. \(AB = 0\) n'implique pas \(A = 0\) ou \(B = 0\).

## II. Inverse d'une matrice carrée

\(B\) est l'**inverse** de \(A\) (carrée) si \(AB = BA = I\) ; on la note \(A^{-1}\). Si elle existe, elle est **unique**, et \(A\) commute avec \(A^{-1}\). Toutes les matrices carrées ne sont pas inversibles. Pour **vérifier** qu'une matrice est l'inverse d'une autre, on calcule le produit et on trouve \(I\).

**Méthode itérative (opérations sur les lignes).** On écrit \([A \mid I]\) puis on transforme, par opérations sur les lignes, \(A\) en \(I\) ; la partie droite devient \(A^{-1}\). Si l'on obtient une ligne de zéros à gauche, \(A\) n'est pas inversible.

Opérations autorisées : échanger deux lignes ; multiplier une ligne par un nombre non nul ; ajouter à une ligne un multiple d'une autre.

## III. Systèmes d'équations

Un système de \(n\) équations à \(n\) inconnues s'écrit \(AX = B\). Si \(A\) est inversible, la solution est **unique** (système de Cramer) :

\[
X = A^{-1}B .
\]

**Rédaction type.** (1) Poser les inconnues avec leur unité ; (2) écrire \(AX = B\) ; (3) vérifier que l'inverse donné convient (\(AA^{-1} = I\)) ; (4) calculer \(A^{-1}B\) ; (5) **vérifier** dans les équations de départ ; (6) conclure par une phrase.

## IV. Calculatrice

Le produit de matrices et l'inverse peuvent être obtenus à la **calculatrice** lors de l'épreuve, sans justification du calcul. En revanche, il faut savoir **écrire le système sous forme matricielle** et **interpréter** le résultat. Le **déterminant** n'est pas au programme : l'inversibilité se constate par la méthode des lignes ou par le calcul de \(AA^{-1}\).

## À retenir pour le jour de l'épreuve

1. Contrôler les **tailles** avant tout produit.
2. Écrire l'ordre des facteurs (\(A^{-1}B\), pas \(BA^{-1}\)).
3. **Toujours vérifier** la solution d'un système dans les équations d'origine.

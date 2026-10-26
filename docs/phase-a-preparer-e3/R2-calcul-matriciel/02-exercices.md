# Exercices – Calcul matriciel

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – R2*

> [!NOTE]
> **Comment travailler.** Cherche sur papier en écrivant les étapes, puis compare. Trois niveaux : **socle**, **format épreuve**, **pour aller plus loin** (au-delà du programme de l'épreuve).

## Niveau 1 – Socle

### Exercice 1 – Addition et multiplication par un nombre

On donne \(A = \begin{pmatrix} 2 & -1 & 0 \\ 1 & 3 & 4 \end{pmatrix}\) et \(B = \begin{pmatrix} 1 & 0 & 2 \\ -2 & 5 & 1 \end{pmatrix}\). Calculer \(A + B\) et \(3A - 2B\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(A + B = \begin{pmatrix} 3 & -1 & 2 \\ -1 & 8 & 5 \end{pmatrix}\).

\(3A = \begin{pmatrix} 6 & -3 & 0 \\ 3 & 9 & 12 \end{pmatrix}\), \(2B = \begin{pmatrix} 2 & 0 & 4 \\ -4 & 10 & 2 \end{pmatrix}\), donc \(3A - 2B = \begin{pmatrix} 4 & -3 & -4 \\ 7 & -1 & 10 \end{pmatrix}\).

</details>

### Exercice 2 – Produits possibles

On a \(P\) de taille \(2 \times 3\), \(Q\) de taille \(3 \times 2\), \(R\) de taille \(2 \times 2\). Parmi \(PQ\), \(QP\), \(PR\), \(RP\), \(QR\), \(RQ\), lesquels sont définis ? Quelle est alors leur taille ?

<details markdown="1">
<summary>Voir la réponse</summary>

Le produit \(MN\) est défini si le nombre de colonnes de \(M\) égale le nombre de lignes de \(N\).

- \(PQ\) : \(3 = 3\), oui, taille \(2 \times 2\).
- \(QP\) : \(2 = 2\), oui, taille \(3 \times 3\).
- \(PR\) : \(3 \ne 2\), non.
- \(RP\) : \(2 = 2\), oui, taille \(2 \times 3\).
- \(QR\) : \(2 = 2\), oui, taille \(3 \times 2\).
- \(RQ\) : \(2 \ne 3\), non.

</details>

### Exercice 3 – Un produit à la main

Avec \(P = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \end{pmatrix}\) et \(Q = \begin{pmatrix} 2 & 1 \\ 0 & 1 \\ 4 & 0 \end{pmatrix}\), calculer \(PQ\) puis \(QP\). Comparer leurs tailles.

<details markdown="1">
<summary>Voir la réponse</summary>

\(PQ = \begin{pmatrix} 1\cdot 2 + 2 \cdot 0 + 0 \cdot 4 & 1 \cdot 1 + 2 \cdot 1 + 0 \cdot 0 \\ 0 \cdot 2 + 1 \cdot 0 + 3 \cdot 4 & 0 \cdot 1 + 1 \cdot 1 + 3 \cdot 0 \end{pmatrix} = \begin{pmatrix} 2 & 3 \\ 12 & 1 \end{pmatrix}\).

\(QP = \begin{pmatrix} 2 & 5 & 3 \\ 0 & 1 & 3 \\ 4 & 8 & 0 \end{pmatrix}\).

\(PQ\) est \(2 \times 2\), \(QP\) est \(3 \times 3\) : elles n'ont même pas la même taille, donc \(PQ \ne QP\).

</details>

### Exercice 4 – Non-commutativité

Avec \(A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\) et \(B = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}\), calculer \(AB\) et \(BA\). Que constate-t-on ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(AB = \begin{pmatrix} 7 & 2 \\ 3 & 1 \end{pmatrix}\) et \(BA = \begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}\). Deux matrices carrées de même taille peuvent donner \(AB \ne BA\) : **le produit n'est pas commutatif**.

</details>

## Niveau 2 – Format épreuve

### Exercice 5 – Recettes d'un hébergeur

Un hébergeur propose deux offres : « Pro » à 30 € par mois et « Premium » à 45 € par mois. Le tableau donne le nombre d'abonnements facturés chaque trimestre.

| | Pro | Premium |
|---|---|---|
| Mois 1 | 12 | 8 |
| Mois 2 | 15 | 10 |
| Mois 3 | 9 | 14 |

1. Écrire la matrice \(V\) des ventes et la matrice colonne \(C\) des prix. Quelles sont leurs tailles ?
2. Calculer \(VC\). Que représente chaque coefficient ?
3. En déduire la recette du trimestre.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(V = \begin{pmatrix} 12 & 8 \\ 15 & 10 \\ 9 & 14 \end{pmatrix}\) (\(3 \times 2\)) et \(C = \begin{pmatrix} 30 \\ 45 \end{pmatrix}\) (\(2 \times 1\)).
2. \(VC\) est de taille \(3 \times 1\) : \(\begin{pmatrix} 12 \cdot 30 + 8 \cdot 45 \\ 15 \cdot 30 + 10 \cdot 45 \\ 9 \cdot 30 + 14 \cdot 45 \end{pmatrix} = \begin{pmatrix} 720 \\ 900 \\ 900 \end{pmatrix}\). Chaque coefficient est la **recette du mois** correspondant, en euros.
3. \(720 + 900 + 900 = 2520\) : la recette du trimestre est de **2 520 €**.

</details>

### Exercice 6 – Un système sous forme matricielle

Un lot de 2 baies de type A et 3 baies de type B consomme 17 kW ; un lot de 3 baies de type A et 5 baies de type B consomme 28 kW. On note \(x\) et \(y\) la consommation (en kW) d'une baie A et d'une baie B.

1. Écrire le système sous la forme \(MX = S\).
2. Vérifier que \(N = \begin{pmatrix} 5 & -3 \\ -3 & 2 \end{pmatrix}\) est l'inverse de \(M\).
3. Résoudre le système et vérifier le résultat.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(\begin{cases} 2x + 3y = 17 \\ 3x + 5y = 28 \end{cases}\), soit \(M = \begin{pmatrix} 2 & 3 \\ 3 & 5 \end{pmatrix}\), \(X = \begin{pmatrix} x \\ y \end{pmatrix}\), \(S = \begin{pmatrix} 17 \\ 28 \end{pmatrix}\).
2. \(MN = \begin{pmatrix} 10 - 9 & -6 + 6 \\ 15 - 15 & -9 + 10 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2\) (et \(NM = I_2\) de même) : \(N = M^{-1}\).
3. \(X = M^{-1}S = \begin{pmatrix} 5 \cdot 17 - 3 \cdot 28 \\ -3 \cdot 17 + 2 \cdot 28 \end{pmatrix} = \begin{pmatrix} 1 \\ 5 \end{pmatrix}\). Une baie A consomme **1 kW** et une baie B **5 kW**. Vérification : \(2 \cdot 1 + 3 \cdot 5 = 17\) et \(3 \cdot 1 + 5 \cdot 5 = 28\).

</details>

### Exercice 7 – Système à trois inconnues

Trois licences ont pour prix \(x\), \(y\), \(z\) (en euros). Trois commandes donnent :

\[
\begin{cases} x + 2y + 3z = 13 \\ y + 4z = 13 \\ 5x + 6y = 16 \end{cases}
\]

On donne \(M^{-1} = \begin{pmatrix} -24 & 18 & 5 \\ 20 & -15 & -4 \\ -5 & 4 & 1 \end{pmatrix}\) pour \(M = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}\).

1. Écrire le système sous la forme \(MX = B\).
2. Vérifier la première ligne de \(M M^{-1}\) (les trois coefficients).
3. Calculer \(X\) et vérifier.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(X = \begin{pmatrix} x \\ y \\ z \end{pmatrix}\) et \(B = \begin{pmatrix} 13 \\ 13 \\ 16 \end{pmatrix}\).
2. Ligne 1 de \(M\) : \((1, 2, 3)\). Colonne 1 de \(M^{-1}\) : \(-24 + 40 - 15 = 1\). Colonne 2 : \(18 - 30 + 12 = 0\). Colonne 3 : \(5 - 8 + 3 = 0\). On trouve bien \((1, 0, 0)\), première ligne de \(I_3\).
3. \(X = M^{-1}B = \begin{pmatrix} -24 \cdot 13 + 18 \cdot 13 + 5 \cdot 16 \\ 20 \cdot 13 - 15 \cdot 13 - 4 \cdot 16 \\ -5 \cdot 13 + 4 \cdot 13 + 16 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix}\). Les prix sont **2 €, 1 € et 3 €**. Vérification : \(2 + 2 + 9 = 13\) ; \(1 + 12 = 13\) ; \(10 + 6 = 16\).

</details>

### Exercice 8 – Calculer un inverse par la méthode des lignes

Calculer l'inverse de \(A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\) à l'aide de \([A \mid I]\), puis le vérifier.

<details markdown="1">
<summary>Voir la réponse</summary>

\[
\left(\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 5 & 3 & 0 & 1 \end{array}\right)
\xrightarrow{L_2 \leftarrow 2L_2 - 5L_1}
\left(\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 0 & 1 & -5 & 2 \end{array}\right)
\xrightarrow{L_1 \leftarrow L_1 - L_2}
\left(\begin{array}{cc|cc} 2 & 0 & 6 & -2 \\ 0 & 1 & -5 & 2 \end{array}\right)
\xrightarrow{L_1 \leftarrow L_1 / 2}
\left(\begin{array}{cc|cc} 1 & 0 & 3 & -1 \\ 0 & 1 & -5 & 2 \end{array}\right)
\]

Donc \(A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}\). Vérification : \(A A^{-1} = \begin{pmatrix} 6 - 5 & -2 + 2 \\ 15 - 15 & -5 + 6 \end{pmatrix} = I_2\).

</details>

## Niveau 3 – Pour aller plus loin

> [!NOTE]
> Hors programme de l'épreuve : déterminant, chaînes de Markov, puissances de matrices. Ces outils sont au programme des classes préparatoires et des licences.

### Exercice 9 – Déterminant et inversibilité (2 × 2)

Pour \(A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}\), le **déterminant** est \(\det A = ad - bc\). La matrice est inversible si et seulement si \(\det A \ne 0\), et alors \(A^{-1} = \dfrac{1}{\det A}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}\).

1. Retrouver l'inverse de la matrice \(M\) de l'exercice 6 avec cette formule.
2. La matrice \(\begin{pmatrix} 4 & 2 \\ 6 & 3 \end{pmatrix}\) est-elle inversible ? Interpréter pour un système.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(\det M = 2 \cdot 5 - 3 \cdot 3 = 1\), donc \(M^{-1} = \begin{pmatrix} 5 & -3 \\ -3 & 2 \end{pmatrix}\), comme dans l'exercice 6.
2. \(\det = 4 \cdot 3 - 2 \cdot 6 = 0\) : **non inversible**. Les lignes sont proportionnelles (\(L_2 = 1{,}5\,L_1\)) : un système \(\begin{cases} 4x + 2y = a \\ 6x + 3y = b \end{cases}\) n'a ni solution unique, ni de solution du tout selon \(a\) et \(b\) (il en a une infinité si \(b = 1{,}5a\), aucune sinon).

</details>

### Exercice 10 – Disponibilité d'un service (chaîne de Markov)

Chaque jour, un service **disponible** le reste avec probabilité 0,9 et tombe en panne avec probabilité 0,1 ; un service **en panne** est réparé avec probabilité 0,5 dans la journée. On note \(P = \begin{pmatrix} 0{,}9 & 0{,}1 \\ 0{,}5 & 0{,}5 \end{pmatrix}\) (ligne = état de départ, colonne = état d'arrivée).

1. Le service est disponible aujourd'hui. Quelle est la probabilité qu'il le soit dans deux jours ?
2. Trouver la répartition \((\pi_1, \pi_2)\) vérifiant \(\pi P = \pi\) avec \(\pi_1 + \pi_2 = 1\). Interpréter.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(P^2 = \begin{pmatrix} 0{,}86 & 0{,}14 \\ 0{,}70 & 0{,}30 \end{pmatrix}\) : la probabilité est **0,86**.
2. \(\pi P = \pi\) donne \(0{,}9\pi_1 + 0{,}5\pi_2 = \pi_1\), soit \(0{,}5\pi_2 = 0{,}1\pi_1\), \(\pi_1 = 5\pi_2\). Avec \(\pi_1 + \pi_2 = 1\) : \(\pi = (5/6,\ 1/6)\). À long terme, le service est **disponible environ 83 % du temps**.

</details>

### Exercice 11 – Puissances de matrices et suite de Fibonacci

Soit \(F = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\). On admet que \(F^n = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}\) où \((F_n)\) est la suite de Fibonacci (\(F_0 = 0\), \(F_1 = 1\), \(F_{n+1} = F_n + F_{n-1}\)). Calculer \(F^{10}\) en élevant au carré, et en déduire \(F_{10}\). Combien de produits de matrices sont nécessaires ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(F^2 = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}\), \(F^4 = (F^2)^2 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}\), \(F^8 = (F^4)^2 = \begin{pmatrix} 34 & 21 \\ 21 & 13 \end{pmatrix}\), puis \(F^{10} = F^8 F^2 = \begin{pmatrix} 89 & 55 \\ 55 & 34 \end{pmatrix}\). Donc **\(F_{10} = 55\)**. Il faut 4 produits (3 élévations au carré, puis \(F^8 F^2\)), contre 9 additions par la récurrence directe : pour \(n\) grand, l'exponentiation rapide est beaucoup plus économe (de l'ordre de \(\log_2 n\) produits).

</details>

## Auto-évaluation

- [ ] Je vérifie les tailles avant un produit et je sais donner la taille du résultat.
- [ ] Je calcule un produit de matrices à la main (au plus \(3 \times 3\)) et à la calculatrice.
- [ ] Je vérifie qu'une matrice est l'inverse d'une autre.
- [ ] J'écris un système sous la forme \(AX = B\) et je le résous avec \(A^{-1}\).
- [ ] Je calcule un inverse par la méthode des lignes.

# Exercices – Statistique descriptive

*BTS SIO SISR 2e année – Option mathématiques approfondies – M3*

> [!NOTE]
> Trois niveaux : **socle**, **format épreuve**, **pour aller plus loin**. Conventions : quartiles par médiane de chaque moitié, variance sur \(n\) (pas \(n - 1\)).

## Niveau 1 – Socle

### Exercice 1 – Une série de temps de réponse

Douze temps de réponse d'un service (en millisecondes) : 12, 15, 15, 16, 18, 20, 21, 21, 22, 25, 27, 40.

1. Calculer la moyenne, la médiane, \(Q_1\), \(Q_3\) et l'étendue.
2. Calculer l'écart type (à \(10^{-2}\) près, à la calculatrice).
3. Que se passe-t-il si on supprime la valeur 40 ? Commenter.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Somme : 252, donc moyenne \(\dfrac{252}{12} = 21\) ms. La série est déjà ordonnée : la médiane est la moyenne des 6e et 7e valeurs, \(\dfrac{20 + 21}{2} = 20{,}5\) ms. Moitié inférieure : 12, 15, 15, 16, 18, 20, donc \(Q_1 = \dfrac{15 + 16}{2} = 15{,}5\). Moitié supérieure : 21, 21, 22, 25, 27, 40, donc \(Q_3 = \dfrac{22 + 25}{2} = 23{,}5\). Étendue : \(40 - 12 = 28\).
2. Variance sur \(n\) : \(\sigma \approx 7{,}08\) ms.
3. Sans le 40, il reste 11 valeurs : moyenne \(\dfrac{212}{11} \approx 19{,}27\) ms, médiane \(20\) ms (6e valeur). La moyenne baisse de près de 2 ms, la médiane de 0,5 ms : la **médiane est plus robuste** à une valeur aberrante.

</details>

### Exercice 2 – Série en classes

Durées de connexion de 40 sessions (en minutes) : \([0\,;\,10[\) : 4 ; \([10\,;\,20[\) : 10 ; \([20\,;\,30[\) : 18 ; \([30\,;\,40[\) : 8.

Calculer la moyenne et l'écart type en prenant les centres de classe, et donner la classe médiane.

<details markdown="1">
<summary>Voir la réponse</summary>

Centres : 5, 15, 25, 35. Moyenne : \(\dfrac{4 \times 5 + 10 \times 15 + 18 \times 25 + 8 \times 35}{40} = \dfrac{900}{40} = 22{,}5\) min.

Variance : \(\dfrac{4(5 - 22{,}5)^2 + 10(15 - 22{,}5)^2 + 18(25 - 22{,}5)^2 + 8(35 - 22{,}5)^2}{40} = 78{,}75\), donc \(\sigma \approx 8{,}87\) min.

Effectifs cumulés : 4, 14, 32, 40. La 20e et la 21e valeur se trouvent dans la classe \([20\,;\,30[\), qui est la classe médiane.

</details>

## Niveau 2 – Format épreuve

### Exercice 3 – Charge et nombre d'utilisateurs

Le nombre d'utilisateurs connectés \(x\) (en centaines) et la charge processeur \(y\) (en %) sont relevés : 

| \(x\) | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| \(y\) | 12 | 19 | 31 | 38 | 52 | 57 |

1. Déterminer à la calculatrice la droite de régression de \(y\) en \(x\) (coefficients à \(10^{-2}\) près) et le coefficient de corrélation.
2. Estimer la charge pour 8 centaines d'utilisateurs. Que penser de cette estimation ?
3. Interpréter le coefficient directeur.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(y \approx 9{,}46x + 1{,}73\) et \(r \approx 0{,}994\) : l'ajustement linéaire est très bon.
2. Pour \(x = 8\) : \(y \approx 9{,}46 \times 8 + 1{,}73 \approx 77{,}4\) %. C'est une **extrapolation** (on a observé jusqu'à \(x = 6\)) : elle est plausible, mais la charge ne peut pas dépasser 100 % et la relation peut changer près de la saturation.
3. Chaque centaine d'utilisateurs supplémentaires ajoute en moyenne environ **9,5 points** de charge processeur.

</details>

### Exercice 4 – Croissance exponentielle

Le nombre de comptes créés par semaine est : 

| semaine \(t\) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| comptes \(y\) | 100 | 148 | 225 | 340 | 512 | 770 |

1. Un ajustement affine de \(y\) en \(t\) convient-il ? Pourquoi un ajustement de \(\ln y\) en \(t\) est-il plus adapté ?
2. À la calculatrice, la droite de régression de \(\ln y\) en \(t\) est \(\ln y \approx 0{,}410\,t + 4{,}598\). En déduire un modèle \(y = C \cdot q^{t}\).
3. Estimer le nombre de comptes à la semaine 6.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Les rapports successifs \(\dfrac{148}{100}\), \(\dfrac{225}{148}\), \(\dfrac{340}{225}\), \(\dfrac{512}{340}\), \(\dfrac{770}{512}\) sont tous proches de 1,5 : la croissance est **multiplicative**, donc l'ajustement de \(\ln y\) en \(t\) est le bon (le nuage de \(\ln y\) est presque aligné, \(r \approx 0{,}9999\)).
2. \(y = e^{4{,}598}\,\left(e^{0{,}410}\right)^{t} \approx 99{,}3 \times 1{,}507^{t}\) : environ \(+50{,}7\) % par semaine.
3. \(y(6) \approx 99{,}3 \times 1{,}507^{6} \approx 1\,160\) comptes (valeur obtenue avec les coefficients non arrondis de la calculatrice ; extrapolation d'une unité hors de la série).

</details>

## Niveau 3 – Pour aller plus loin

### Exercice 5 – Transformation affine

Les temps d'une série sont mesurés en secondes : moyenne \(21\) s, écart type \(7{,}08\) s. On les convertit en millisecondes, puis on ajoute un délai fixe de 50 ms.

1. Quelles sont la nouvelle moyenne et le nouvel écart type ?
2. Démontrer que \(\overline{ax + b} = a\bar{x} + b\) et que \(V(ax + b) = a^2 V(x)\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(y = 1000x + 50\) : moyenne \(1000 \times 21 + 50 = 21\,050\) ms, écart type \(1000 \times 7{,}08 = 7\,080\) ms (le décalage de 50 ms ne change pas la dispersion).
2. \(\overline{ax + b} = \dfrac{1}{n}\sum (ax_i + b) = a\bar{x} + b\). Puis \(V(ax + b) = \dfrac{1}{n}\sum \big((ax_i + b) - (a\bar{x} + b)\big)^2 = \dfrac{1}{n}\sum a^2 (x_i - \bar{x})^2 = a^2 V(x)\), donc \(\sigma_{ax+b} = |a|\,\sigma_x\).

</details>

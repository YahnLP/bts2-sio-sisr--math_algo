# Exercices – Fonction d'une variable réelle

*BTS SIO SISR 2e année – Option mathématiques approfondies – M1*

> [!NOTE]
> Trois niveaux : **socle**, **format épreuve**, **pour aller plus loin**. Cherche sur papier, puis compare avec le corrigé.

## Niveau 1 – Socle

### Exercice 1 – Un second degré

Soit \(f(x) = 2x^2 - 8x + 6\). Calculer \(f(0)\), \(f(1)\), \(f(3)\), \(f(5)\). Trouver l'abscisse du sommet de la courbe et résoudre \(f(x) = 0\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(f(0) = 6\), \(f(1) = 2 - 8 + 6 = 0\), \(f(3) = 18 - 24 + 6 = 0\), \(f(5) = 50 - 40 + 6 = 16\).

Sommet : \(x = -\dfrac{-8}{2 \times 2} = 2\), avec \(f(2) = 8 - 16 + 6 = -2\). Le minimum de \(f\) vaut \(-2\).

Les valeurs \(f(1) = f(3) = 0\) donnent les solutions de \(f(x) = 0\) : \(x = 1\) et \(x = 3\). On retrouve la symétrie autour de \(x = 2\).

</details>

### Exercice 2 – Composition

On pose \(f(x) = x + 3\) et \(g(x) = x^2\). Donner \(f \circ g\) et \(g \circ f\), puis les calculer en \(x = 2\).

<details markdown="1">
<summary>Voir la réponse</summary>

\((f \circ g)(x) = f(x^2) = x^2 + 3\) et \((g \circ f)(x) = g(x + 3) = (x + 3)^2\).

En \(x = 2\) : \(7\) et \(25\). Les deux compositions sont différentes.

</details>

### Exercice 3 – Équations avec exponentielle et logarithme

Résoudre \(e^{0{,}2t} = 3\) et \(\ln x = 2\). Donner des valeurs approchées à \(10^{-2}\) près.

<details markdown="1">
<summary>Voir la réponse</summary>

\(0{,}2t = \ln 3\), donc \(t = 5 \ln 3 \approx 5{,}49\).

\(\ln x = 2\) donne \(x = e^{2} \approx 7{,}39\).

</details>

## Niveau 2 – Format épreuve

### Exercice 4 – Quel abonnement choisir ?

Un hébergeur propose deux offres pour \(x\) machines virtuelles : l'offre A coûte \(A(x) = 40 + 2{,}5x\) euros, l'offre B coûte \(B(x) = 6x\) euros.

1. Pour quelle valeur de \(x\) les deux offres coûtent-elles autant ?
2. Quelle offre choisir pour 8 machines ? pour 20 ?
3. À partir de combien de machines l'offre A est-elle la moins chère ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(40 + 2{,}5x = 6x\) équivaut à \(3{,}5x = 40\), donc \(x = \dfrac{40}{3{,}5} \approx 11{,}43\).
2. Pour \(x = 8\) : \(A = 60\), \(B = 48\) : l'offre B. Pour \(x = 20\) : \(A = 90\), \(B = 120\) : l'offre A.
3. Le nombre de machines est entier : \(x = 11\) donne \(A = 67{,}5\) et \(B = 66\) (B moins chère) ; \(x = 12\) donne \(A = 70\) et \(B = 72\). L'offre A est la moins chère **à partir de 12 machines**. La solution \(11{,}43\) n'est pas entière : on la discute et on arrondit dans le bon sens.

</details>

### Exercice 5 – Seuil de capacité

Un volume de données de 1 000 Go augmente de 5 % par an. Au bout de combien d'années dépasse-t-il 1 500 Go ?

<details markdown="1">
<summary>Voir la réponse</summary>

On cherche \(n\) entier avec \(1000 \times 1{,}05^{n} \ge 1500\), soit \(1{,}05^{n} \ge 1{,}5\).

Donc \(n \ge \dfrac{\ln 1{,}5}{\ln 1{,}05} \approx 8{,}31\).

Le plus petit entier convenable est \(n = 9\). Contrôle : \(1{,}05^{8} \approx 1{,}477\) (insuffisant) et \(1{,}05^{9} \approx 1{,}551\) (suffisant). Le seuil est atteint la **9e année**.

</details>

### Exercice 7 – Racine et dichotomie

1. Résoudre \(\sqrt{x + 3} = x - 3\) (penser à vérifier).
2. Un coût de traitement est modélisé par \(h(x) = \ln x + x - 4\) pour \(x > 0\) (\(h\) est croissante). Montrer que \(h(x) = 0\) a une solution unique dans \([2\,;\,3]\), puis l'encadrer par dichotomie avec une amplitude inférieure à 0,1.

<details markdown="1">
<summary>Voir la réponse</summary>

1. On élève au carré : \(x + 3 = x^{2} - 6x + 9\), soit \(x^{2} - 7x + 6 = 0\), de racines 1 et 6. Contrôle : pour \(x = 1\), \(\sqrt{4} = 2\) mais \(x - 3 = -2\) : **fausse solution**. Pour \(x = 6\), \(\sqrt{9} = 3 = 6 - 3\) : convient. Une seule solution : \(x = 6\).
2. \(h\) est croissante, \(h(2) = \ln 2 - 2 \approx -1{,}31 < 0\) et \(h(3) = \ln 3 - 1 \approx 0{,}10 > 0\) : une solution unique dans \([2\,;\,3]\).

| Étape | Intervalle | Milieu | Signe de \(h(m)\) |
|---|---|---|---|
| 1 | \([2\,;\,3]\) | 2,5 | \(-\) |
| 2 | \([2{,}5\,;\,3]\) | 2,75 | \(-\) |
| 3 | \([2{,}75\,;\,3]\) | 2,875 | \(-\) |
| 4 | \([2{,}875\,;\,3]\) | 2,9375 | \(+\) |

Après 4 étapes : \(2{,}875 < x < 2{,}9375\), amplitude \(0{,}0625 < 0{,}1\). (Valeur plus précise : \(x \approx 2{,}926\).)

</details>

## Niveau 3 – Pour aller plus loin

### Exercice 6 – Fonction réciproque

Soit \(g(x) = \dfrac{2x + 1}{x + 1}\) pour \(x \ge 0\). Résoudre \(g(x) = y\) pour \(y\) donné. Pour quelles valeurs de \(y\) y a-t-il une solution \(x \ge 0\) ? Que dit cela sur les valeurs prises par \(g\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(\dfrac{2x+1}{x+1} = y\) équivaut à \(2x + 1 = yx + y\), soit \(x(2 - y) = y - 1\), donc \(x = \dfrac{y - 1}{2 - y}\) (si \(y \ne 2\)).

Pour que \(x \ge 0\), il faut \(\dfrac{y-1}{2-y} \ge 0\), c'est-à-dire \(1 \le y < 2\). Donc \(g\) prend toutes les valeurs de \([1\,;\,2[\) et aucune autre : \(g(0) = 1\) et la valeur \(2\) n'est jamais atteinte (c'est une limite, voir M2).

Contrôle : \(y = 1{,}5\) donne \(x = \dfrac{0{,}5}{0{,}5} = 1\), et \(g(1) = \dfrac{3}{2} = 1{,}5\).

</details>

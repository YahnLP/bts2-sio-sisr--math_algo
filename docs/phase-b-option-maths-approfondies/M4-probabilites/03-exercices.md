# Exercices – Calcul des probabilités

*BTS SIO SISR 2e année – Option mathématiques approfondies – M4*

> [!NOTE]
> Trois niveaux : **socle**, **format épreuve**, **pour aller plus loin**. Les valeurs sont données à \(10^{-4}\) près ; utilise la calculatrice ou Python.

## Niveau 1 – Socle

### Exercice 1 – Une variable aléatoire discrète

Un incident coûte \(0\) € avec la probabilité \(0{,}7\), \(1\,000\) € avec \(0{,}2\) et \(5\,000\) € avec \(0{,}1\). Calculer l'espérance, la variance et l'écart type du coût.

<details markdown="1">
<summary>Voir la réponse</summary>

\(E = 0 \times 0{,}7 + 1000 \times 0{,}2 + 5000 \times 0{,}1 = 700\) €.

\(\sum p_i x_i^2 = 0{,}2 \times 10^{6} + 0{,}1 \times 25 \times 10^{6} = 2{,}7 \times 10^{6}\), donc \(V = 2\,700\,000 - 700^2 = 2\,210\,000\) et \(\sigma \approx 1\,487\) €.

Le coût moyen est de 700 € par incident, mais la dispersion est grande : le risque est loin d'être négligeable.

</details>

### Exercice 2 – Loi binomiale

Sur un lot de 20 disques, chacun est défectueux avec la probabilité \(0{,}03\), indépendamment. \(X\) est le nombre de disques défectueux.

1. Quelle est la loi de \(X\) ? Donner \(E(X)\) et \(\sigma(X)\).
2. Calculer \(P(X = 0)\) et \(P(X \ge 2)\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(X \sim \mathcal{B}(20\,;\,0{,}03)\), \(E = 20 \times 0{,}03 = 0{,}6\), \(V = 20 \times 0{,}03 \times 0{,}97 = 0{,}582\), \(\sigma \approx 0{,}763\).
2. \(P(X = 0) = 0{,}97^{20} \approx 0{,}5438\). \(P(X \ge 2) = 1 - P(X \le 1) \approx 0{,}1198\), soit environ 12 % de chances d'avoir au moins deux disques défectueux dans le lot.

</details>

## Niveau 2 – Format épreuve

### Exercice 3 – Loi de Poisson

Un service reçoit en moyenne 2 incidents par jour, modélisés par une loi de Poisson \(\mathcal{P}(2)\).

1. Calculer la probabilité de n'avoir aucun incident, puis exactement 3 incidents.
2. Calculer la probabilité d'avoir au moins 5 incidents.
3. L'équipe tient une permanence renforcée à partir de 5 incidents. À quelle fréquence est-elle déclenchée ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(P(X = 0) = e^{-2} \approx 0{,}1353\) ; \(P(X = 3) = e^{-2}\dfrac{2^3}{3!} \approx 0{,}1804\).
2. \(P(X \ge 5) = 1 - P(X \le 4) \approx 0{,}0527\).
3. Environ \(5{,}3\) % des jours, soit à peu près **un jour sur 19**, donc environ 19 fois par an : la permanence est rare mais pas exceptionnelle, il faut la prévoir.

</details>

### Exercice 4 – Loi normale

Le temps de réponse d'une application suit une loi normale de moyenne \(100\) ms et d'écart type \(8\) ms.

1. Calculer \(P(X \le 105)\) et \(P(90 \le X \le 110)\).
2. Quel temps \(t\) est dépassé dans seulement \(5\) % des cas ?
3. Le contrat impose 95 % des réponses sous 115 ms. Est-il respecté ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(P(X \le 105) \approx 0{,}7340\). Pour \(P(90 \le X \le 110)\), \(z = \pm 1{,}25\), donc \(P \approx 0{,}7887\).
2. On cherche \(t\) tel que \(P(X \le t) = 0{,}95\) : \(t = 100 + 1{,}645 \times 8 \approx 113{,}2\) ms.
3. Comme \(113{,}2 < 115\), au moins 95 % des réponses sont sous 115 ms : **le contrat est respecté**, avec une marge d'environ 2 ms.

</details>

## Niveau 3 – Pour aller plus loin

### Exercice 5 – De la binomiale à Poisson

Sur 200 transmissions, chacune échoue avec la probabilité \(0{,}01\). \(X\) est le nombre d'échecs.

1. Donner la loi exacte de \(X\), puis la loi de Poisson qui l'approche.
2. Comparer \(P(X = 0)\) et \(P(X = 3)\) pour les deux lois.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(X \sim \mathcal{B}(200\,;\,0{,}01)\), d'espérance \(200 \times 0{,}01 = 2\) : on approche par \(\mathcal{P}(2)\).
2. Binomiale : \(P(X = 0) = 0{,}99^{200} \approx 0{,}1340\), \(P(X = 3) \approx 0{,}1814\). Poisson : \(0{,}1353\) et \(0{,}1804\). Les valeurs sont très proches (écart inférieur à \(10^{-2}\)), ce qui justifie l'approximation quand \(n\) est grand et \(p\) petit.

</details>

### Exercice 6 – Deux états : un service en marche ou en panne

Un service est soit **en marche** (M), soit **en panne** (P). Chaque jour : s'il est en marche, il le reste avec la probabilité \(0{,}9\) ; s'il est en panne, il est réparé et en marche le lendemain avec la probabilité \(0{,}4\). La matrice de transition est \(T = \begin{pmatrix} 0{,}9 & 0{,}1 \\ 0{,}4 & 0{,}6 \end{pmatrix}\) (lignes : état du jour ; colonnes : état du lendemain, dans l'ordre M, P).

1. Calculer \(T^2\) et interpréter son coefficient \((P, M)\).
2. Trouver la répartition \((a\,;\,b)\), avec \(a + b = 1\), telle que \((a\,;\,b)\,T = (a\,;\,b)\). Interpréter.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(T^2 = \begin{pmatrix} 0{,}85 & 0{,}15 \\ 0{,}60 & 0{,}40 \end{pmatrix}\). Le coefficient \((P, M) = 0{,}60\) est la probabilité que le service, en panne aujourd'hui, soit en marche **dans deux jours**.
2. L'équation donne \(0{,}9a + 0{,}4b = a\), soit \(0{,}4b = 0{,}1a\), donc \(a = 4b\). Avec \(a + b = 1\) : \(a = 0{,}8\) et \(b = 0{,}2\). À long terme, le service est en marche **80 %** du temps et en panne 20 % du temps, quel que soit l'état de départ.

</details>

# Sujet – Option mathématiques approfondies (2 heures, 20 points)

*BTS SIO SISR 2e année – Option mathématiques approfondies – sujet d'entraînement de l'auteur, **non officiel***

> [!NOTE]
> **Conditions.** Compose ce sujet **sans aide** et **chronométré** (2 heures). Calculatrice formelle autorisée. Les trois exercices sont indépendants. Chaque résultat est **justifié et commenté** (unité, sens). Le corrigé et le barème sont dans les blocs « Voir le corrigé ».
>
> **Répartition indicative :** exercice 1 (analyse) 7 points, exercice 2 (statistique) 6 points, exercice 3 (probabilités et fiabilité) 7 points.

## Exercice 1 – La charge d'un service après une mise à jour (7 points)

Après une mise à jour, la charge d'un service (en milliers de requêtes par minute) est modélisée, pour \(x\) heures écoulées avec \(x \in [0\,;\,8]\), par
\[
f(x) = x\,e^{-x/2}.
\]

**1. (3 points)**

a) Montrer que \(f'(x) = \dfrac{2 - x}{2}\,e^{-x/2}\).
b) Dresser le tableau de variations de \(f\) sur \([0\,;\,8]\).
c) À quel moment la charge est-elle maximale, et quelle est sa valeur (à \(10^{-2}\) près) ?

**2. (1 point)** Calculer la limite de \(f(x)\) quand \(x \to +\infty\) (admise : \(x e^{-x/2} \to 0\)). Que représente-t-elle pour le service ?

**3. (3 points)**

a) Montrer que \(F(x) = -2(x + 2)e^{-x/2}\) est une primitive de \(f\).
b) En déduire \(\displaystyle\int_{0}^{4} f(x)\,dx\) (valeur exacte puis approchée à \(10^{-2}\) près).
c) Calculer la valeur moyenne de \(f\) sur \([0\,;\,4]\) et l'interpréter.

<details markdown="1">
<summary>Voir le corrigé et le barème</summary>

**1.** a) *(1 pt)* \(f'(x) = e^{-x/2} + x\left(-\dfrac{1}{2}\right)e^{-x/2} = \left(1 - \dfrac{x}{2}\right)e^{-x/2} = \dfrac{2 - x}{2}\,e^{-x/2}\).

b) *(1 pt)* \(e^{-x/2} > 0\), donc \(f'\) a le signe de \(2 - x\) : positif pour \(x < 2\), négatif pour \(x > 2\).

| \(x\) | 0 | 2 | 8 |
|---|---|---|---|
| \(f(x)\) | 0 | \(2e^{-1}\) (maximum) | \(8e^{-4}\) |

La fonction croît de \(0\) à \(2e^{-1}\) sur \([0\,;\,2]\), puis décroît sur \([2\,;\,8]\) ; \(f(8) = 8e^{-4} \approx 0{,}15\).

c) *(1 pt)* La charge est maximale **2 heures** après la mise à jour, pour \(f(2) = 2e^{-1} \approx 0{,}74\), soit environ 740 requêtes par minute.

**2.** *(1 pt)* \(\lim_{x \to +\infty} f(x) = 0\) : la droite \(y = 0\) est asymptote. La charge **revient vers 0** : le pic lié à la mise à jour se résorbe.

**3.** a) *(1 pt)* \(F'(x) = -2e^{-x/2} - 2(x + 2)\left(-\dfrac{1}{2}\right)e^{-x/2} = e^{-x/2}(-2 + x + 2) = x\,e^{-x/2} = f(x)\).

b) *(1 pt)* \(\displaystyle\int_{0}^{4} f(x)\,dx = F(4) - F(0) = -12e^{-2} - (-4) = 4 - 12e^{-2} \approx 2{,}38\) (milliers de requêtes par minute, sommées sur 4 heures).

c) *(1 pt)* Valeur moyenne : \(\dfrac{4 - 12e^{-2}}{4} = 1 - 3e^{-2} \approx 0{,}59\) : la charge moyenne sur les 4 premières heures est d'environ **590 requêtes par minute**, inférieure au pic de 740.

</details>

## Exercice 2 – Charge et utilisateurs (6 points)

On relève le nombre \(x\) de centaines d'utilisateurs connectés et la charge processeur \(y\) (en %) :

| \(x\) | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| \(y\) | 12 | 19 | 31 | 38 | 52 | 57 |

**1. (2 points)** Calculer la moyenne, la médiane et l'écart type de \(y\) (à \(10^{-2}\) près).

**2. (2 points)** Donner, à la calculatrice, l'équation de la droite de régression de \(y\) en \(x\) (coefficients à \(10^{-2}\) près) et le coefficient de corrélation. Que penser de l'ajustement ?

**3. (2 points)** Estimer la charge pour 800 utilisateurs. À partir de combien d'utilisateurs la charge prévue dépasse-t-elle 70 % ? Discuter la validité de ces prévisions.

<details markdown="1">
<summary>Voir le corrigé et le barème</summary>

**1.** *(2 pts)* Somme \(= 209\), moyenne \(\dfrac{209}{6} \approx 34{,}83\) %. Médiane : \(\dfrac{31 + 38}{2} = 34{,}5\) %. Écart type (sur \(n\)) \(\approx 16{,}24\) %.

**2.** *(2 pts)* \(y \approx 9{,}46x + 1{,}73\) et \(r \approx 0{,}994\). \(r\) est très proche de 1 : l'ajustement affine est **très bon**. *(1 pt pour la droite, 1 pt pour le commentaire de \(r\).)*

**3.** *(2 pts)* Pour 800 utilisateurs, \(x = 8\) : \(y \approx 9{,}46 \times 8 + 1{,}73 \approx 77{,}4\) %. Pour \(y > 70\) : \(x > \dfrac{70 - 1{,}73}{9{,}46} \approx 7{,}22\), soit **plus de 722 utilisateurs**. Ces prévisions sont des **extrapolations** : l'observation s'arrête à \(x = 6\), et la charge peut cesser d'être linéaire près de la saturation. *(1 pt pour les calculs, 1 pt pour la discussion.)*

</details>

## Exercice 3 – Fiabilité d'une baie de stockage (7 points)

**Partie A – Les disques (3 points).** Une baie contient 10 disques. Sur une année, chaque disque est défaillant avec la probabilité \(0{,}05\), indépendamment des autres. \(X\) est le nombre de disques défaillants.

**1.** Quelle est la loi de \(X\) ? Donner \(E(X)\). *(1 point)*

**2.** Calculer \(P(X = 0)\) et \(P(X \ge 2)\) (à \(10^{-4}\) près). *(2 points)*

**Partie B – Le serveur de contrôle (4 points).** La durée de vie \(T\) d'un serveur de contrôle suit une loi exponentielle de MTBF \(1\,500\) h.

**3.** Donner \(\lambda\) et calculer \(P(T > 1000)\). *(1 point)*

**4.** Deux serveurs identiques sont montés **en parallèle**. Calculer la fiabilité du montage à 1 000 h. *(1 point)*

**5.** La durée moyenne de réparation est de 6 h. Calculer la disponibilité d'un serveur et le temps d'arrêt annuel (8 760 h). *(2 points)*

<details markdown="1">
<summary>Voir le corrigé et le barème</summary>

**1.** *(1 pt)* \(X \sim \mathcal{B}(10\,;\,0{,}05)\) (10 épreuves indépendantes de même probabilité). \(E(X) = 10 \times 0{,}05 = 0{,}5\) disque par an.

**2.** *(2 pts)* \(P(X = 0) = 0{,}95^{10} \approx 0{,}5987\). \(P(X \ge 2) = 1 - P(X \le 1) \approx 0{,}0861\), soit environ 8,6 % de chances de perdre au moins deux disques dans l'année : la tolérance à **deux** pannes simultanées (RAID 6) se justifie.

**3.** *(1 pt)* \(\lambda = \dfrac{1}{1500} \approx 6{,}67 \times 10^{-4}\) h\(^{-1}\). \(P(T > 1000) = e^{-1000/1500} = e^{-2/3} \approx 0{,}5134\).

**4.** *(1 pt)* \(R = 1 - (1 - 0{,}5134)^2 \approx 0{,}7632\).

**5.** *(2 pts)* \(A = \dfrac{1500}{1500 + 6} = \dfrac{1500}{1506} \approx 0{,}9960\), soit \(99{,}60\) %. Arrêt annuel : \(8760 \times (1 - 0{,}99602) \approx 34{,}9\) h. *(1 pt pour la disponibilité, 1 pt pour l'arrêt annuel et son commentaire.)*

</details>

## Barème récapitulatif

| Exercice | Points |
|---|---|
| 1. Analyse | 7 |
| 2. Statistique | 6 |
| 3. Probabilités et fiabilité | 7 |
| **Total** | **20** |

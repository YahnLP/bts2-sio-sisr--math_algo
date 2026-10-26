# Cours 2 – Systèmes en série, en parallèle et disponibilité

*BTS SIO SISR 2e année – Option mathématiques approfondies – M5, seconde partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : calculer la fiabilité d'un système de composants **en série**, **en parallèle** et **mixte** ; comprendre l'intérêt de la **redondance** ; calculer une **disponibilité** à partir de la MTBF et de la durée de réparation ; relier un taux de disponibilité à un **temps d'arrêt annuel** (SLA).
>
> **Prérequis.** Le [cours 1](01-fiabilite-et-loi-exponentielle.md) et les [événements indépendants](../M4-probabilites/04-conditionnement-et-independance.md). Les composants sont supposés **indépendants**.
>
> **Programme.** Les montages en série et en parallèle sont des applications directes de l'indépendance (\(P(A \cap B) = P(A)\,P(B)\)) : ils relèvent du programme de probabilités. La **disponibilité** (section 6) est hors programme de l'unité UF2 : c'est une notion de culture professionnelle (contrats de service), utile en exploitation, qui ne sera pas exigée à l'épreuve facultative.

## 1. Pour démarrer : un service, plusieurs composants

Une application web dépend d'un serveur, d'une base de données, d'un lien réseau. Si l'un tombe, le service tombe. À l'inverse, deux serveurs identiques en secours peuvent maintenir le service si l'un d'eux tombe. La fiabilité du **système** dépend de la fiabilité de chaque composant et de la **façon dont ils sont assemblés**.

<figure class="fig-math">
<svg viewBox="0 0 520 230" role="img" aria-label="Montages en série et en parallèle">
<text class="fm-t fm-b" x="20" y="22">Série : il faut que tout marche</text>
<line class="fm-curve" x1="20" y1="58" x2="50" y2="58"/>
<rect class="fm-box" x="50" y="41" width="64" height="34" rx="6"/><text class="fm-t fm-b" x="82" y="63" text-anchor="middle">A</text>
<line class="fm-curve" x1="114" y1="58" x2="150" y2="58"/>
<rect class="fm-box" x="150" y="41" width="64" height="34" rx="6"/><text class="fm-t fm-b" x="182" y="63" text-anchor="middle">B</text>
<line class="fm-curve" x1="214" y1="58" x2="250" y2="58"/>
<text class="fm-t" x="258" y="63">R = R<tspan dy="4" font-size="10">A</tspan><tspan dy="-4"> × R</tspan><tspan dy="4" font-size="10">B</tspan></text>
<text class="fm-t fm-b" x="20" y="120">Parallèle : il suffit qu’un seul marche</text>
<line class="fm-curve" x1="20" y1="170" x2="50" y2="170"/>
<line class="fm-curve" x1="50" y1="148" x2="50" y2="192"/>
<line class="fm-curve" x1="50" y1="148" x2="70" y2="148"/>
<rect class="fm-box" x="70" y="131" width="64" height="34" rx="6"/><text class="fm-t fm-b" x="102" y="153" text-anchor="middle">A</text>
<line class="fm-curve" x1="134" y1="148" x2="160" y2="148"/>
<line class="fm-curve" x1="50" y1="192" x2="70" y2="192"/>
<rect class="fm-box" x="70" y="175" width="64" height="34" rx="6"/><text class="fm-t fm-b" x="102" y="197" text-anchor="middle">B</text>
<line class="fm-curve" x1="134" y1="192" x2="160" y2="192"/>
<line class="fm-curve" x1="160" y1="148" x2="160" y2="192"/>
<line class="fm-curve" x1="160" y1="170" x2="190" y2="170"/>
<text class="fm-t" x="200" y="175">R = 1 − (1 − R<tspan dy="4" font-size="10">A</tspan><tspan dy="-4">)(1 − R</tspan><tspan dy="4" font-size="10">B</tspan><tspan dy="-4">)</tspan></text>
</svg>
<figcaption>Deux composants A et B montés en série (à gauche, tous deux nécessaires) ou en parallèle (redondance : un seul suffit).</figcaption>
</figure>

## 2. Montage en série : il faut que tout marche

Le système fonctionne **si et seulement si tous** les composants fonctionnent. Comme les composants sont indépendants, on **multiplie** les fiabilités :

\[
R_{\text{série}} = R_1 \times R_2 \times \dots \times R_n.
\]

**Conséquence.** La fiabilité d'une chaîne est **toujours inférieure** à celle de son maillon le plus faible : **chaque composant ajouté en série dégrade le système**.

**Exemple.** Deux disques identiques, de fiabilité \(0{,}6065\) à 1 000 h, montés en série : \(R = 0{,}6065^2 = e^{-1} \approx 0{,}3679\).

**Taux et MTBF.** Pour \(n\) composants identiques de taux \(\lambda\) en série, le taux du système est \(n\lambda\) et sa MTBF vaut \(\dfrac{1}{n\lambda}\), soit la MTBF d'un composant **divisée par \(n\)**.

## 3. Montage en parallèle : il suffit qu'un seul marche

C'est la **redondance** : le système tombe **seulement si tous** les composants tombent. On calcule donc la probabilité que **tous soient en panne**, puis on prend le contraire :

\[
R_{\text{parallèle}} = 1 - (1 - R_1)(1 - R_2)\cdots(1 - R_n).
\]

**Exemple.** Deux disques en miroir, chacun de fiabilité \(0{,}6065\) à 1 000 h. Chacun tombe en panne avec la probabilité \(1 - 0{,}6065 = 0{,}3935\). Les deux tombent ensemble avec la probabilité \(0{,}3935^{2} \approx 0{,}1548\), donc \(R = 1 - 0{,}1548 \approx 0{,}8452\).

**Comparaison.** Un seul disque : 0,6065. Deux en série : 0,3679. Deux en parallèle : 0,8452. La redondance **augmente** la fiabilité de près de 24 points, la mise en série la **réduit**.

**MTBF d'un montage parallèle de deux composants identiques.** Elle vaut \(\dfrac{3}{2\lambda}\), soit **1,5 fois** celle d'un composant (3 000 h pour 2 000 h). Redonder ne double pas la MTBF.

> [!WARNING]
> **L'hypothèse d'indépendance est décisive.** Deux serveurs branchés sur la **même alimentation**, ou hébergés dans la **même baie**, ne tombent pas en panne indépendamment : la formule parallèle devient fausse (trop optimiste). C'est pourquoi on sépare les alimentations, les baies et les sites.

## 4. Systèmes mixtes : on réduit étape par étape

Pour un montage qui mêle séries et parallèles :

1. **Repérer** les blocs en parallèle ;
2. **remplacer** chaque bloc parallèle par un composant équivalent (sa fiabilité) ;
3. **appliquer** la formule série au résultat.

**Exemple résolu.** Un serveur A est en série avec un bloc de deux serveurs B et C en parallèle. Chaque serveur a une fiabilité de \(0{,}6065\) à 1 000 h. Calculer la fiabilité du système, puis dire quel composant dupliquer en priorité.

<details markdown="1">
<summary>Voir la solution détaillée</summary>

**Bloc \(\{B, C\}\).** \(R_{BC} = 1 - (1 - 0{,}6065)^{2} \approx 0{,}8452\).

**Système.** A est en série avec ce bloc : \(R = 0{,}6065 \times 0{,}8452 \approx 0{,}5126\).

**Où renforcer ?** Le serveur A est le **maillon faible** : seul en série, il limite le système à \(0{,}6065\) au mieux. Le dupliquer donnerait un second bloc parallèle de fiabilité \(0{,}8452\), et un système à \(0{,}8452^2 \approx 0{,}7143\) : une amélioration de plus de 20 points.

**Règle de bon sens.** On redonde **d'abord** le composant le moins fiable ou qui n'a aucun secours (le *point unique de défaillance*).

</details>

## 5. Combien de redondances ?

**Question.** Chaque serveur a une fiabilité de \(0{,}6065\). Combien en mettre en parallèle pour que le bloc dépasse \(0{,}99\) ?

On veut \(1 - q^{n} \ge 0{,}99\), avec \(q = 1 - 0{,}6065 = 0{,}3935\) (probabilité de panne d'un serveur). Donc \(q^{n} \le 0{,}01\), et en prenant les logarithmes (le logarithme de \(q < 1\) est négatif, donc le sens **change**) :

\[
n \ge \dfrac{\ln 0{,}01}{\ln 0{,}3935} \approx 4{,}94.
\]

Il faut **5 serveurs**. Contrôle : \(n = 4\) donne \(1 - 0{,}3935^{4} \approx 0{,}976\) (insuffisant) ; \(n = 5\) donne \(\approx 0{,}9906\). On retrouve la **méthode du seuil** du module M1.

Cinq serveurs coûtent cher : au-delà d'un certain point, chaque serveur apporte de moins en moins, et l'**indépendance des pannes** devient décisive.

## 6. La disponibilité (hors programme de l'épreuve)

La fiabilité parle d'un composant **non réparé**. Un équipement réparable alterne **marche** et **panne** : on s'intéresse à la proportion du temps pendant laquelle il fonctionne, la **disponibilité**.

Avec la **MTBF** (durée moyenne de bon fonctionnement entre deux pannes) et le **MTTR** (*Mean Time To Repair*, durée moyenne de réparation) :

\[
A = \dfrac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}.
\]

**Exemple résolu.** MTBF de 2 000 h, MTTR de 8 h. Disponibilité et arrêt annuel (une année compte 8 760 h) ?

<details markdown="1">
<summary>Voir la solution</summary>

\(A = \dfrac{2000}{2000 + 8} = \dfrac{2000}{2008} \approx 0{,}9960\), soit \(99{,}60\) %.

Arrêt annuel : \(8760 \times (1 - 0{,}99602) \approx 34{,}9\) heures.

**Contrat à 99,9 % ?** Non : \(99{,}60\) % est inférieur. Un contrat à 99,9 % autorise environ 8,8 h d'arrêt par an. Pour y parvenir, on peut réduire le MTTR (maintenance plus rapide, pièces en stock) ou augmenter la MTBF (redondance).

</details>

**Disponibilité et SLA : quelques repères.**

| Disponibilité | Arrêt annuel toléré |
|---|---|
| 99 % | environ 87,6 h (3,65 jours) |
| 99,9 % | environ 8,8 h |
| 99,99 % | environ 53 min |
| 99,999 % | environ 5 min |

> [!TIP]
> **Deux leviers.** Pour gagner en disponibilité, on peut **moins tomber en panne** (MTBF plus grande, redondance) ou **réparer plus vite** (MTTR plus petit). Souvent, réduire le MTTR est le moins coûteux.

## 7. Calculer avec Python

```python
from math import exp

r = exp(-1000 / 2000)                 # fiabilité d'un composant à 1000 h
serie = r * r
parallele = 1 - (1 - r) ** 2
mixte = r * (1 - (1 - r) ** 2)
print(round(serie, 4), round(parallele, 4), round(mixte, 4))  # 0.3679 0.8452 0.5126
```

## 8. À retenir

> [!NOTE]
> - **Série** : \(R = R_1 \times R_2 \times \dots\) ; chaque composant ajouté **dégrade** la fiabilité.
> - **Parallèle** : \(R = 1 - (1 - R_1)(1 - R_2)\cdots\) ; la redondance **améliore** la fiabilité (si les pannes sont indépendantes).
> - Système mixte : réduire les blocs parallèles, puis appliquer la formule série ; renforcer d'abord le **maillon faible**.
> - Disponibilité \(A = \dfrac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}\) ; arrêt annuel \(= 8760\,(1 - A)\).

## 9. Teste-toi

**Question 1.** Trois composants de fiabilité \(0{,}9\) sont montés en série. Quelle est la fiabilité du système ? Et si on les monte en parallèle ?

**Question 2.** Un équipement a une MTBF de 1 500 h et un MTTR de 6 h. Calculer sa disponibilité.

<details markdown="1">
<summary>Voir les réponses</summary>

1. Série : \(0{,}9^{3} = 0{,}729\). Parallèle : \(1 - (1 - 0{,}9)^{3} = 1 - 0{,}001 = 0{,}999\). Le même ensemble de composants peut donner 73 % ou 99,9 % selon le montage.
2. \(A = \dfrac{1500}{1500 + 6} = \dfrac{1500}{1506} \approx 0{,}9960\), soit \(99{,}60\) %.

</details>

**Pour continuer :** les [exercices du module](03-exercices.md), puis le [sujet de 2 heures](../sujets/sujet-1.md).

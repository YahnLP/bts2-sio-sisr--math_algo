# Cours 1 – La fiabilité et la loi exponentielle

*BTS SIO SISR 2e année – Option mathématiques approfondies – M5, première partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : définir la **fiabilité** d'un composant ; utiliser la **loi exponentielle** (taux de défaillance constant) ; calculer une probabilité de survie, une **MTBF** et une durée **médiane** ; expliquer la propriété **sans mémoire** et ses limites.
>
> **Prérequis.** L'exponentielle ([module M1](../M1-fonctions/02-exponentielle-et-logarithme.md)) et les probabilités ([module M4](../M4-probabilites/01-variable-aleatoire-et-loi-binomiale.md)).
>
> **Programme.** La loi exponentielle fait partie des modules de probabilités de l'unité UF2. La fiabilité n'est pas un module de l'unité : c'est ici une **application** de la loi exponentielle, très utile pour un technicien SISR. Le vocabulaire (fiabilité, MTBF) doit être rappelé par l'énoncé s'il est utilisé.

## 1. Pour démarrer : pourquoi parler de fiabilité ?

Un disque dur d'un serveur finira par tomber en panne. On ne sait pas **quand**, mais on peut dire **avec quelle probabilité** il tiendra 1 000 heures. C'est la **fiabilité**, un outil central en exploitation informatique : dimensionner la redondance, estimer les arrêts, négocier un **SLA** (accord de niveau de service).

## 2. La fonction de fiabilité

Soit \(T\) la **durée de bon fonctionnement** d'un composant, en heures (on la voit comme une variable aléatoire : elle varie d'un exemplaire à l'autre).

**Définition.** La **fiabilité** à l'instant \(t\) est la probabilité que le composant fonctionne **encore** à l'instant \(t\) :

\[
R(t) = P(T > t).
\]

Propriétés évidentes : \(R(0) = 1\) (à l'instant 0, le composant marche) ; \(R\) est **décroissante** (plus le temps passe, plus c'est improbable) ; \(R(t)\) tend vers 0 quand \(t\) devient très grand.

La probabilité qu'il soit **déjà tombé en panne** à l'instant \(t\) est le contraire : \(P(T \le t) = 1 - R(t)\).

## 3. La loi exponentielle : un taux de défaillance constant

**L'hypothèse.** Beaucoup de composants électroniques ne « s'usent » pas pendant leur vie utile : à chaque instant, ils ont la **même chance** de tomber en panne, quel que soit leur âge. On parle d'un **taux de défaillance constant**, noté \(\lambda\) (« lambda »), en pannes par heure (h\(^{-1}\)).

**La loi exponentielle de paramètre \(\lambda\)** décrit alors la durée de vie :

\[
R(t) = e^{-\lambda t}, \qquad P(T \le t) = 1 - e^{-\lambda t}.
\]

**La MTBF** (*Mean Time Between Failures*, durée moyenne de bon fonctionnement) est

\[
\text{MTBF} = E(T) = \dfrac{1}{\lambda}.
\]

Elle est liée à \(\lambda\) comme l'inverse : une MTBF de 2 000 h correspond à \(\lambda = \dfrac{1}{2000} = 0{,}0005\) panne par heure.

<figure class="fig-math">
<svg viewBox="0 0 520 320" role="img" aria-label="Fonction de fiabilité">
<line class="fm-grid" x1="52" y1="282.0" x2="502" y2="282.0"/>
<text class="fm-t" x="46" y="286.0" text-anchor="end">0,00</text>
<line class="fm-grid" x1="52" y1="218.7" x2="502" y2="218.7"/>
<text class="fm-t" x="46" y="222.7" text-anchor="end">0,25</text>
<line class="fm-grid" x1="52" y1="155.3" x2="502" y2="155.3"/>
<text class="fm-t" x="46" y="159.3" text-anchor="end">0,50</text>
<line class="fm-grid" x1="52" y1="92.0" x2="502" y2="92.0"/>
<text class="fm-t" x="46" y="96.0" text-anchor="end">0,75</text>
<line class="fm-grid" x1="52" y1="28.7" x2="502" y2="28.7"/>
<text class="fm-t" x="46" y="32.7" text-anchor="end">1,00</text>
<line class="fm-grid" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t" x="52.0" y="298" text-anchor="middle">0</text>
<line class="fm-grid" x1="127.0" y1="16" x2="127.0" y2="282"/>
<text class="fm-t" x="127.0" y="298" text-anchor="middle">1000</text>
<line class="fm-grid" x1="202.0" y1="16" x2="202.0" y2="282"/>
<text class="fm-t" x="202.0" y="298" text-anchor="middle">2000</text>
<line class="fm-grid" x1="277.0" y1="16" x2="277.0" y2="282"/>
<text class="fm-t" x="277.0" y="298" text-anchor="middle">3000</text>
<line class="fm-grid" x1="352.0" y1="16" x2="352.0" y2="282"/>
<text class="fm-t" x="352.0" y="298" text-anchor="middle">4000</text>
<line class="fm-grid" x1="427.0" y1="16" x2="427.0" y2="282"/>
<text class="fm-t" x="427.0" y="298" text-anchor="middle">5000</text>
<line class="fm-grid" x1="502.0" y1="16" x2="502.0" y2="282"/>
<text class="fm-t" x="502.0" y="298" text-anchor="middle">6000</text>
<line class="fm-axis" x1="52" y1="282.0" x2="502" y2="282.0"/>
<line class="fm-axis" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t fm-i" x="502" y="314" text-anchor="end">t (heures)</text>
<text class="fm-t fm-i" x="56" y="24">R(t)</text>
<polyline class="fm-curve" points="52.0,28.7 53.5,31.2 55.0,33.7 56.5,36.2 58.0,38.6 59.5,41.0 61.0,43.4 62.5,45.8 64.0,48.1 65.5,50.5 67.0,52.8 68.5,55.1 70.0,57.3 71.5,59.5 73.0,61.8 74.5,64.0 76.0,66.1 77.5,68.3 79.0,70.4 80.5,72.5 82.0,74.6 83.5,76.7 85.0,78.7 86.5,80.7 88.0,82.7 89.5,84.7 91.0,86.7 92.5,88.6 94.0,90.5 95.5,92.4 97.0,94.3 98.5,96.2 100.0,98.0 101.5,99.9 103.0,101.7 104.5,103.5 106.0,105.3 107.5,107.0 109.0,108.8 110.5,110.5 112.0,112.2 113.5,113.9 115.0,115.5 116.5,117.2 118.0,118.8 119.5,120.5 121.0,122.1 122.5,123.7 124.0,125.2 125.5,126.8 127.0,128.3 128.5,129.9 130.0,131.4 131.5,132.9 133.0,134.4 134.5,135.8 136.0,137.3 137.5,138.7 139.0,140.2 140.5,141.6 142.0,143.0 143.5,144.4 145.0,145.7 146.5,147.1 148.0,148.4 149.5,149.7 151.0,151.1 152.5,152.4 154.0,153.7 155.5,154.9 157.0,156.2 158.5,157.5 160.0,158.7 161.5,159.9 163.0,161.1 164.5,162.3 166.0,163.5 167.5,164.7 169.0,165.9 170.5,167.0 172.0,168.2 173.5,169.3 175.0,170.4 176.5,171.5 178.0,172.6 179.5,173.7 181.0,174.8 182.5,175.9 184.0,176.9 185.5,178.0 187.0,179.0 188.5,180.0 190.0,181.0 191.5,182.0 193.0,183.0 194.5,184.0 196.0,185.0 197.5,186.0 199.0,186.9 200.5,187.9 202.0,188.8 203.5,189.7 205.0,190.6 206.5,191.6 208.0,192.5 209.5,193.3 211.0,194.2 212.5,195.1 214.0,196.0 215.5,196.8 217.0,197.7 218.5,198.5 220.0,199.3 221.5,200.2 223.0,201.0 224.5,201.8 226.0,202.6 227.5,203.4 229.0,204.2 230.5,204.9 232.0,205.7 233.5,206.5 235.0,207.2 236.5,208.0 238.0,208.7 239.5,209.4 241.0,210.1 242.5,210.9 244.0,211.6 245.5,212.3 247.0,213.0 248.5,213.6 250.0,214.3 251.5,215.0 253.0,215.7 254.5,216.3 256.0,217.0 257.5,217.6 259.0,218.3 260.5,218.9 262.0,219.5 263.5,220.2 265.0,220.8 266.5,221.4 268.0,222.0 269.5,222.6 271.0,223.2 272.5,223.8 274.0,224.3 275.5,224.9 277.0,225.5 278.5,226.0 280.0,226.6 281.5,227.1 283.0,227.7 284.5,228.2 286.0,228.8 287.5,229.3 289.0,229.8 290.5,230.3 292.0,230.9 293.5,231.4 295.0,231.9 296.5,232.4 298.0,232.9 299.5,233.3 301.0,233.8 302.5,234.3 304.0,234.8 305.5,235.3 307.0,235.7 308.5,236.2 310.0,236.6 311.5,237.1 313.0,237.5 314.5,238.0 316.0,238.4 317.5,238.8 319.0,239.3 320.5,239.7 322.0,240.1 323.5,240.5 325.0,241.0 326.5,241.4 328.0,241.8 329.5,242.2 331.0,242.6 332.5,243.0 334.0,243.3 335.5,243.7 337.0,244.1 338.5,244.5 340.0,244.9 341.5,245.2 343.0,245.6 344.5,246.0 346.0,246.3 347.5,246.7 349.0,247.0 350.5,247.4 352.0,247.7 353.5,248.1 355.0,248.4 356.5,248.7 358.0,249.1 359.5,249.4 361.0,249.7 362.5,250.0 364.0,250.4 365.5,250.7 367.0,251.0 368.5,251.3 370.0,251.6 371.5,251.9 373.0,252.2 374.5,252.5 376.0,252.8 377.5,253.1 379.0,253.4 380.5,253.6 382.0,253.9 383.5,254.2 385.0,254.5 386.5,254.8 388.0,255.0 389.5,255.3 391.0,255.6 392.5,255.8 394.0,256.1 395.5,256.3 397.0,256.6 398.5,256.9 400.0,257.1 401.5,257.4 403.0,257.6 404.5,257.8 406.0,258.1 407.5,258.3 409.0,258.6 410.5,258.8 412.0,259.0 413.5,259.2 415.0,259.5 416.5,259.7 418.0,259.9 419.5,260.1 421.0,260.4 422.5,260.6 424.0,260.8 425.5,261.0 427.0,261.2 428.5,261.4 430.0,261.6 431.5,261.8 433.0,262.0 434.5,262.2 436.0,262.4 437.5,262.6 439.0,262.8 440.5,263.0 442.0,263.2 443.5,263.4 445.0,263.6 446.5,263.7 448.0,263.9 449.5,264.1 451.0,264.3 452.5,264.5 454.0,264.6 455.5,264.8 457.0,265.0 458.5,265.1 460.0,265.3 461.5,265.5 463.0,265.6 464.5,265.8 466.0,266.0 467.5,266.1 469.0,266.3 470.5,266.4 472.0,266.6 473.5,266.7 475.0,266.9 476.5,267.1 478.0,267.2 479.5,267.3 481.0,267.5 482.5,267.6 484.0,267.8 485.5,267.9 487.0,268.1 488.5,268.2 490.0,268.3 491.5,268.5 493.0,268.6 494.5,268.7 496.0,268.9 497.5,269.0 499.0,269.1 500.5,269.3 502.0,269.4"/>
<line class="fm-dash" x1="52.0" y1="155.3" x2="156.0" y2="155.3"/>
<line class="fm-dash" x1="156.0" y1="282.0" x2="156.0" y2="155.3"/>
<circle class="fm-pt2" cx="156.0" cy="155.3" r="4.5"/>
<text class="fm-t" x="166.0" y="145.3" text-anchor="start">médiane 1 386 h</text>
<line class="fm-dash" x1="202.0" y1="282.0" x2="202.0" y2="188.8"/>
<circle class="fm-pt" cx="202.0" cy="188.8" r="4.5"/>
<text class="fm-t" x="214.0" y="176.8" text-anchor="start">MTBF 2 000 h : R ≈ 0,37</text>
</svg>
<figcaption>Fonction de fiabilité R(t) = e^(−t/2000). À la MTBF (2 000 h), il reste environ 37 % des composants en état de marche ; la moitié est tombée en panne à la médiane (1 386 h).</figcaption>
</figure>

**Exemple résolu : un disque dur.** Son taux de défaillance est \(\lambda = 0{,}0005\) h\(^{-1}\) (MTBF 2 000 h). Calculer la probabilité qu'il fonctionne encore à 1 000 h, qu'il tombe en panne avant 500 h, et sa durée médiane.

<details markdown="1">
<summary>Voir la solution détaillée</summary>

**Fiabilité à 1 000 h.** \(R(1000) = e^{-0{,}0005 \times 1000} = e^{-0{,}5} \approx 0{,}6065\) : environ **61 %** des disques tiennent encore à 1 000 h.

**Panne avant 500 h.** \(P(T \le 500) = 1 - e^{-0{,}0005 \times 500} = 1 - e^{-0{,}25} \approx 0{,}2212\) : environ **22 %**.

**Durée médiane.** C'est la durée \(t_{1/2}\) telle que \(R(t_{1/2}) = 0{,}5\) (la moitié des disques tient encore) :

\[
e^{-\lambda t} = 0{,}5 \iff -\lambda t = \ln 0{,}5 \iff t = \dfrac{\ln 2}{\lambda} = 2000 \ln 2 \approx 1\,386 \text{ h}.
\]

**Interprétation.** La **médiane (1 386 h) est inférieure à la MTBF (2 000 h)** : la moitié des disques tombe en panne avant 1 386 h, alors que la moyenne est de 2 000 h, tirée vers le haut par les disques très durables.

</details>

> [!WARNING]
> **La MTBF n'est pas une durée de vie garantie.** Avec une MTBF de 2 000 h, la fiabilité à 2 000 h n'est que de \(e^{-1} \approx 37\) % : **63 %** des composants sont déjà en panne à la MTBF. Voir aussi la figure.

## 4. La propriété sans mémoire

Pour la loi exponentielle :

\[
P(T > s + t \mid T > s) = P(T > t).
\]

La probabilité de tenir **encore** \(t\) heures, sachant qu'on a déjà fonctionné \(s\) heures, est la même que pour un composant **neuf**. Le composant « ne vieillit pas ».

**Exemple.** Un disque a déjà fonctionné 500 h. Probabilité de tenir 1 000 h de plus ? C'est \(R(1000) = e^{-0{,}5} \approx 0{,}6065\), comme pour un disque neuf. Le calcul direct le confirme : \(\dfrac{R(1500)}{R(500)} = \dfrac{e^{-0{,}75}}{e^{-0{,}25}} = e^{-0{,}5}\).

> [!WARNING]
> **Une limite du modèle.** Un vrai disque **s'use** : sa fiabilité après plusieurs années est moindre que celle d'un disque neuf. Le modèle exponentielle décrit bien la « vie utile » (la période où les pannes sont aléatoires), pas le **vieillissement** en fin de vie ni la **jeunesse** (défauts de fabrication au début). Savoir le dire est une marque de sens critique.

## 5. Un lien avec la loi de Poisson

Si les pannes surviennent au hasard à un **rythme moyen de \(\lambda\) pannes par heure**, alors :

- le **nombre** de pannes sur une période suit une loi de **Poisson** (module M4) ;
- le **temps** qui sépare deux pannes successives suit une loi **exponentielle** de paramètre \(\lambda\).

Ce sont deux manières de décrire le même phénomène : l'une compte, l'autre mesure l'attente.

## 6. Calculer avec Python

```python
from math import exp, log

lam = 1 / 2000
print(exp(-lam * 1000))      # fiabilité à 1000 h : 0.6065...
print(1 - exp(-lam * 500))   # panne avant 500 h : 0.2212...
print(log(2) / lam)          # médiane : 1386.29...
```

## 7. À retenir

> [!NOTE]
> - Fiabilité : \(R(t) = P(T > t)\) ; décroissante, \(R(0) = 1\).
> - Loi exponentielle de taux \(\lambda\) : \(R(t) = e^{-\lambda t}\), **MTBF** \(= \dfrac{1}{\lambda}\), médiane \(= \dfrac{\ln 2}{\lambda}\).
> - À la MTBF, seulement \(37\) % des composants fonctionnent encore.
> - **Sans mémoire** : le composant ne vieillit pas (hypothèse à discuter).
> - Pannes aléatoires à taux \(\lambda\) : nombre de pannes → Poisson ; durée entre pannes → exponentielle.

## 8. Teste-toi

**Question 1.** Un composant a une MTBF de 500 h. Calculer son taux \(\lambda\) et sa fiabilité à 100 h.

**Question 2.** Pour ce composant, quelle est la probabilité de panne avant 100 h ?

**Question 3.** Pourquoi une MTBF de 500 h ne veut-elle pas dire que le composant dure 500 h ?

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(\lambda = \dfrac{1}{500} = 0{,}002\) h\(^{-1}\). \(R(100) = e^{-0{,}002 \times 100} = e^{-0{,}2} \approx 0{,}8187\).
2. \(P(T \le 100) = 1 - 0{,}8187 \approx 0{,}1813\), soit environ 18 %.
3. La MTBF est une **durée moyenne**, pas une garantie : à \(t = 500\) h, \(R(500) = e^{-1} \approx 0{,}37\) : environ 63 % des composants sont déjà en panne. Certains tombent en panne très vite, d'autres durent très longtemps.

</details>

**Pour continuer :** le [cours 2 sur les systèmes et la disponibilité](02-systemes-et-disponibilite.md).

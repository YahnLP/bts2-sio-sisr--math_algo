# Cours 2 – Lier deux grandeurs : la régression

*BTS SIO SISR 2e année – Option mathématiques approfondies – M3, seconde partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : représenter une série à deux variables par un **nuage de points** ; déterminer la **droite de régression** (à la calculatrice ou en Python) ; interpréter son coefficient directeur et le **coefficient de corrélation** ; faire une **prévision** en distinguant interpolation et extrapolation ; ajuster une croissance **exponentielle** par un changement de variable.
>
> **Prérequis.** Le [cours 1](01-indicateurs-de-position-et-de-dispersion.md) et les fonctions affines du module M1.

## 1. Pour démarrer : la charge dépend-elle du nombre d'utilisateurs ?

On relève, pour six moments de la journée, le nombre \(x\) de centaines d'utilisateurs connectés et la charge processeur \(y\) (en %) :

| \(x\) | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| \(y\) | 12 | 19 | 31 | 38 | 52 | 57 |

Chaque ligne est un **couple** \((x_i\,;\,y_i)\). On veut savoir s'il existe un lien, le chiffrer, et **prévoir** la charge pour un nombre d'utilisateurs qu'on n'a pas mesuré.

## 2. Le nuage de points

On place chaque couple comme un point dans un repère : c'est le **nuage de points**.

<figure class="fig-math">
<svg viewBox="0 0 520 320" role="img" aria-label="Nuage de points et droite de régression">
<line class="fm-grid" x1="52" y1="282.0" x2="502" y2="282.0"/>
<text class="fm-t" x="46" y="286.0" text-anchor="end">0</text>
<line class="fm-grid" x1="52" y1="219.4" x2="502" y2="219.4"/>
<text class="fm-t" x="46" y="223.4" text-anchor="end">20</text>
<line class="fm-grid" x1="52" y1="156.8" x2="502" y2="156.8"/>
<text class="fm-t" x="46" y="160.8" text-anchor="end">40</text>
<line class="fm-grid" x1="52" y1="94.2" x2="502" y2="94.2"/>
<text class="fm-t" x="46" y="98.2" text-anchor="end">60</text>
<line class="fm-grid" x1="52" y1="31.6" x2="502" y2="31.6"/>
<text class="fm-t" x="46" y="35.6" text-anchor="end">80</text>
<line class="fm-grid" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t" x="52.0" y="298" text-anchor="middle">0</text>
<line class="fm-grid" x1="102.0" y1="16" x2="102.0" y2="282"/>
<text class="fm-t" x="102.0" y="298" text-anchor="middle">1</text>
<line class="fm-grid" x1="152.0" y1="16" x2="152.0" y2="282"/>
<text class="fm-t" x="152.0" y="298" text-anchor="middle">2</text>
<line class="fm-grid" x1="202.0" y1="16" x2="202.0" y2="282"/>
<text class="fm-t" x="202.0" y="298" text-anchor="middle">3</text>
<line class="fm-grid" x1="252.0" y1="16" x2="252.0" y2="282"/>
<text class="fm-t" x="252.0" y="298" text-anchor="middle">4</text>
<line class="fm-grid" x1="302.0" y1="16" x2="302.0" y2="282"/>
<text class="fm-t" x="302.0" y="298" text-anchor="middle">5</text>
<line class="fm-grid" x1="352.0" y1="16" x2="352.0" y2="282"/>
<text class="fm-t" x="352.0" y="298" text-anchor="middle">6</text>
<line class="fm-grid" x1="402.0" y1="16" x2="402.0" y2="282"/>
<text class="fm-t" x="402.0" y="298" text-anchor="middle">7</text>
<line class="fm-grid" x1="452.0" y1="16" x2="452.0" y2="282"/>
<text class="fm-t" x="452.0" y="298" text-anchor="middle">8</text>
<line class="fm-grid" x1="502.0" y1="16" x2="502.0" y2="282"/>
<text class="fm-t" x="502.0" y="298" text-anchor="middle">9</text>
<line class="fm-axis" x1="52" y1="282.0" x2="502" y2="282.0"/>
<line class="fm-axis" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t fm-i" x="502" y="314" text-anchor="end">x (centaines)</text>
<text class="fm-t fm-i" x="56" y="24">y (%)</text>
<polyline class="fm-acc" points="52.0,276.6 53.5,275.7 55.0,274.8 56.5,273.9 58.0,273.0 59.5,272.1 61.0,271.2 62.5,270.4 64.0,269.5 65.5,268.6 67.0,267.7 68.5,266.8 70.0,265.9 71.5,265.0 73.0,264.1 74.5,263.3 76.0,262.4 77.5,261.5 79.0,260.6 80.5,259.7 82.0,258.8 83.5,257.9 85.0,257.0 86.5,256.2 88.0,255.3 89.5,254.4 91.0,253.5 92.5,252.6 94.0,251.7 95.5,250.8 97.0,249.9 98.5,249.1 100.0,248.2 101.5,247.3 103.0,246.4 104.5,245.5 106.0,244.6 107.5,243.7 109.0,242.8 110.5,241.9 112.0,241.1 113.5,240.2 115.0,239.3 116.5,238.4 118.0,237.5 119.5,236.6 121.0,235.7 122.5,234.8 124.0,234.0 125.5,233.1 127.0,232.2 128.5,231.3 130.0,230.4 131.5,229.5 133.0,228.6 134.5,227.7 136.0,226.9 137.5,226.0 139.0,225.1 140.5,224.2 142.0,223.3 143.5,222.4 145.0,221.5 146.5,220.6 148.0,219.8 149.5,218.9 151.0,218.0 152.5,217.1 154.0,216.2 155.5,215.3 157.0,214.4 158.5,213.5 160.0,212.6 161.5,211.8 163.0,210.9 164.5,210.0 166.0,209.1 167.5,208.2 169.0,207.3 170.5,206.4 172.0,205.5 173.5,204.7 175.0,203.8 176.5,202.9 178.0,202.0 179.5,201.1 181.0,200.2 182.5,199.3 184.0,198.4 185.5,197.6 187.0,196.7 188.5,195.8 190.0,194.9 191.5,194.0 193.0,193.1 194.5,192.2 196.0,191.3 197.5,190.5 199.0,189.6 200.5,188.7 202.0,187.8 203.5,186.9 205.0,186.0 206.5,185.1 208.0,184.2 209.5,183.4 211.0,182.5 212.5,181.6 214.0,180.7 215.5,179.8 217.0,178.9 218.5,178.0 220.0,177.1 221.5,176.2 223.0,175.4 224.5,174.5 226.0,173.6 227.5,172.7 229.0,171.8 230.5,170.9 232.0,170.0 233.5,169.1 235.0,168.3 236.5,167.4 238.0,166.5 239.5,165.6 241.0,164.7 242.5,163.8 244.0,162.9 245.5,162.0 247.0,161.2 248.5,160.3 250.0,159.4 251.5,158.5 253.0,157.6 254.5,156.7 256.0,155.8 257.5,154.9 259.0,154.1 260.5,153.2 262.0,152.3 263.5,151.4 265.0,150.5 266.5,149.6 268.0,148.7 269.5,147.8 271.0,146.9 272.5,146.1 274.0,145.2 275.5,144.3 277.0,143.4 278.5,142.5 280.0,141.6 281.5,140.7 283.0,139.8 284.5,139.0 286.0,138.1 287.5,137.2 289.0,136.3 290.5,135.4 292.0,134.5 293.5,133.6 295.0,132.7 296.5,131.9 298.0,131.0 299.5,130.1 301.0,129.2 302.5,128.3 304.0,127.4 305.5,126.5 307.0,125.6 308.5,124.8 310.0,123.9 311.5,123.0 313.0,122.1 314.5,121.2 316.0,120.3 317.5,119.4 319.0,118.5 320.5,117.6 322.0,116.8 323.5,115.9 325.0,115.0 326.5,114.1 328.0,113.2 329.5,112.3 331.0,111.4 332.5,110.5 334.0,109.7 335.5,108.8 337.0,107.9 338.5,107.0 340.0,106.1 341.5,105.2 343.0,104.3 344.5,103.4 346.0,102.6 347.5,101.7 349.0,100.8 350.5,99.9 352.0,99.0 353.5,98.1 355.0,97.2 356.5,96.3 358.0,95.5 359.5,94.6 361.0,93.7 362.5,92.8 364.0,91.9 365.5,91.0 367.0,90.1 368.5,89.2 370.0,88.3 371.5,87.5 373.0,86.6 374.5,85.7 376.0,84.8 377.5,83.9 379.0,83.0 380.5,82.1 382.0,81.2 383.5,80.4 385.0,79.5 386.5,78.6 388.0,77.7 389.5,76.8 391.0,75.9 392.5,75.0 394.0,74.1 395.5,73.3 397.0,72.4 398.5,71.5 400.0,70.6 401.5,69.7 403.0,68.8 404.5,67.9 406.0,67.0 407.5,66.2 409.0,65.3 410.5,64.4 412.0,63.5 413.5,62.6 415.0,61.7 416.5,60.8 418.0,59.9 419.5,59.1 421.0,58.2 422.5,57.3 424.0,56.4 425.5,55.5 427.0,54.6 428.5,53.7 430.0,52.8 431.5,51.9 433.0,51.1 434.5,50.2 436.0,49.3 437.5,48.4 439.0,47.5 440.5,46.6 442.0,45.7 443.5,44.8 445.0,44.0 446.5,43.1 448.0,42.2 449.5,41.3 451.0,40.4 452.5,39.5 454.0,38.6 455.5,37.7 457.0,36.9 458.5,36.0 460.0,35.1 461.5,34.2 463.0,33.3 464.5,32.4 466.0,31.5 467.5,30.6 469.0,29.8 470.5,28.9 472.0,28.0 473.5,27.1 475.0,26.2 476.5,25.3 478.0,24.4 479.5,23.5 481.0,22.6 482.5,21.8 484.0,20.9 485.5,20.0 487.0,19.1 488.5,18.2 490.0,17.3 491.5,16.4 493.0,15.5 494.5,14.7 496.0,13.8 497.5,12.9 499.0,12.0 500.5,11.1"/>
<circle class="fm-pt" cx="102.0" cy="244.4" r="4.5"/>
<circle class="fm-pt" cx="152.0" cy="222.5" r="4.5"/>
<circle class="fm-pt" cx="202.0" cy="185.0" r="4.5"/>
<circle class="fm-pt" cx="252.0" cy="163.1" r="4.5"/>
<circle class="fm-pt" cx="302.0" cy="119.3" r="4.5"/>
<circle class="fm-pt" cx="352.0" cy="103.6" r="4.5"/>
<circle class="fm-pt2" cx="452.0" cy="39.8" r="4.5"/>
<text class="fm-t" x="442.0" y="27.8" text-anchor="end">prévision (8 ; 77,4)</text>
<text class="fm-t" x="367.0" y="129.6" text-anchor="start">6 points mesurés</text>
</svg>
<figcaption>Les six mesures sont presque alignées. La droite de régression y = 9,46x + 1,73 passe au plus près ; le point creux est une extrapolation (hors des mesures).</figcaption>
</figure>

Les six points sont **presque alignés** et la charge augmente avec le nombre d'utilisateurs. Cela suggère un **ajustement affine** : on cherche la droite qui passe « au plus près » des points.

## 3. La droite de régression (moindres carrés)

Parmi toutes les droites, on retient celle qui **minimise la somme des carrés des écarts verticaux** entre les points et la droite : c'est la **droite de régression de \(y\) en \(x\)**, d'équation \(y = ax + b\).

**Les formules.**

\[
a = \dfrac{\operatorname{cov}(x, y)}{V(x)}, \qquad b = \bar{y} - a\,\bar{x},
\]

avec \(\operatorname{cov}(x, y) = \overline{xy} - \bar{x}\,\bar{y}\) (moyenne des produits moins produit des moyennes) et \(V(x)\) la variance de \(x\).

**Le calcul pas à pas** (pour comprendre, car la calculatrice le fait seule) :

| Quantité | Calcul | Résultat |
|---|---|---|
| \(\bar{x}\) | \(\dfrac{1+2+3+4+5+6}{6}\) | \(3{,}5\) |
| \(\bar{y}\) | \(\dfrac{209}{6}\) | \(\approx 34{,}83\) |
| \(V(x)\) | \(\dfrac{1+4+9+16+25+36}{6} - 3{,}5^2 = 15{,}17 - 12{,}25\) | \(\approx 2{,}917\) |
| \(\overline{xy}\) | \(\dfrac{12 + 38 + 93 + 152 + 260 + 342}{6} = \dfrac{897}{6}\) | \(149{,}5\) |
| \(\operatorname{cov}(x,y)\) | \(149{,}5 - 3{,}5 \times 34{,}83\) | \(\approx 27{,}58\) |
| \(a\) | \(\dfrac{27{,}58}{2{,}917}\) | \(\approx 9{,}46\) |
| \(b\) | \(34{,}83 - 9{,}46 \times 3{,}5\) | \(\approx 1{,}73\) |

La droite de régression est donc \(y \approx 9{,}46\,x + 1{,}73\).

> [!TIP]
> **La droite passe toujours par le point moyen** \((\bar{x}\,;\,\bar{y}) = (3{,}5\,;\,34{,}83)\) : c'est un bon contrôle. Vérification : \(9{,}46 \times 3{,}5 + 1{,}73 = 34{,}84\) ✔.

**Interprétation de \(a\) et \(b\).** Chaque **centaine** d'utilisateurs supplémentaires ajoute en moyenne environ **9,5 points** de charge ; \(b \approx 1{,}73\) est la charge « de fond » du modèle sans utilisateur.

## 4. Le coefficient de corrélation : la droite est-elle un bon modèle ?

Le **coefficient de corrélation linéaire** \(r\) est un nombre compris entre \(-1\) et \(1\).

| Valeur de \(r\) | Lecture |
|---|---|
| proche de \(1\) | forte liaison linéaire, \(y\) augmente avec \(x\) |
| proche de \(-1\) | forte liaison linéaire, \(y\) diminue quand \(x\) augmente |
| proche de \(0\) | pas de liaison **linéaire** |

Ici \(r \approx 0{,}994\) : le nuage est presque parfaitement aligné, l'ajustement affine est **très bon**. Le nombre \(r^2 \approx 0{,}989\) s'interprète : environ **99 %** des variations de la charge sont expliquées par la droite.

> [!WARNING]
> **Corrélation n'est pas causalité.** Un \(r\) proche de 1 dit que deux grandeurs évoluent ensemble, pas que l'une **cause** l'autre. Ici le lien de cause est plausible (plus d'utilisateurs, plus de calculs) ; mais deux grandeurs peuvent évoluer ensemble à cause d'une troisième.

## 5. Prévoir : interpolation et extrapolation

La droite permet d'estimer \(y\) pour un \(x\) donné.

- **Interpolation :** \(x\) est **dans l'intervalle** des mesures (entre 1 et 6). La prévision est en général fiable.
- **Extrapolation :** \(x\) est **hors de l'intervalle**. Elle suppose que la tendance continue, ce qui est incertain.

**Exemple.** Pour 800 utilisateurs (\(x = 8\)) : \(y \approx 9{,}46 \times 8 + 1{,}73 \approx 77{,}4\) %. C'est une **extrapolation** (on n'a pas mesuré au-delà de \(x = 6\)). Elle est plausible, mais la charge ne peut pas dépasser 100 %, et le comportement peut changer près de la saturation. Il faut le **dire**.

**Prévision inverse.** À partir de combien d'utilisateurs la charge dépasse-t-elle 70 % ? On résout \(9{,}46x + 1{,}73 > 70\), donc \(x > \dfrac{70 - 1{,}73}{9{,}46} \approx 7{,}22\), soit **plus de 722 utilisateurs**.

## 6. Quand la droite ne convient pas : le changement de variable

**Situation.** Le nombre de comptes créés par semaine :

| semaine \(t\) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| comptes \(y\) | 100 | 148 | 225 | 340 | 512 | 770 |

La croissance s'accélère : ce n'est pas une droite. Regardons les **rapports** successifs : \(\dfrac{148}{100} = 1{,}48\), \(\dfrac{225}{148} \approx 1{,}52\), \(\dfrac{340}{225} \approx 1{,}51\), \(\dfrac{512}{340} \approx 1{,}51\), \(\dfrac{770}{512} \approx 1{,}50\). Ils sont **presque constants** : la croissance est **multiplicative** (environ \(+50\) % par semaine), donc exponentielle.

**Astuce.** Si \(y = C\,q^{t}\), alors \(\ln y = \ln C + t\ln q\) : c'est une **fonction affine de \(t\)**. On ajuste donc **\(\ln y\) en fonction de \(t\)** par une droite. À la calculatrice, on obtient \(\ln y \approx 0{,}410\,t + 4{,}598\), avec \(r \approx 0{,}9999\) : l'ajustement est excellent.

On revient à \(y\) : \(y = e^{4{,}598}\left(e^{0{,}410}\right)^{t} \approx 99{,}3 \times 1{,}507^{\,t}\), soit environ \(+50{,}7\) % par semaine. Prévision pour la semaine 6 : environ **1 160 comptes**.

> [!TIP]
> **Comment choisir ?** Trace le nuage. S'il est aligné, ajuste \(y\) en \(x\). Si les valeurs **multiplient** d'une période à l'autre (rapports presque constants), ajuste \(\ln y\) en \(x\).

## 7. Calculer avec Python

```python
from statistics import linear_regression, correlation

x = [1, 2, 3, 4, 5, 6]
y = [12, 19, 31, 38, 52, 57]
droite = linear_regression(x, y)
print(droite.slope, droite.intercept)   # 9.457...  1.733...
print(correlation(x, y))                # 0.9944...
```

## 8. À retenir

> [!NOTE]
> - Le **nuage de points** montre si un ajustement affine est raisonnable.
> - Droite de régression \(y = ax + b\) : \(a = \dfrac{\operatorname{cov}(x,y)}{V(x)}\), \(b = \bar{y} - a\bar{x}\) ; elle passe par le point moyen.
> - \(r\) proche de \(\pm 1\) : bon ajustement linéaire ; **corrélation n'est pas causalité**.
> - Prévoir : l'**interpolation** est fiable, l'**extrapolation** est à commenter.
> - Croissance multiplicative : ajuster \(\ln y\) en fonction de \(t\).

## 9. Teste-toi

**Question 1.** Une droite de régression est \(y = 2{,}5x + 10\) avec \(r = 0{,}98\), pour des mesures entre \(x = 0\) et \(x = 20\). Estimer \(y\) pour \(x = 12\), puis pour \(x = 50\). Que dire de chaque estimation ?

**Question 2.** Pourquoi la droite de régression passe-t-elle par \((\bar{x}\,;\,\bar{y})\) ?

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(x = 12\) : \(y = 2{,}5 \times 12 + 10 = 40\), une **interpolation** (12 est entre 0 et 20), fiable car \(r\) est grand. \(x = 50\) : \(y = 135\), une **extrapolation** très éloignée des mesures : à prendre avec beaucoup de précautions.
2. Parce que \(b = \bar{y} - a\bar{x}\) : en remplaçant \(x\) par \(\bar{x}\), on obtient \(a\bar{x} + b = \bar{y}\).

</details>

**Pour continuer :** les [exercices du module](03-exercices.md), puis le [module M4 sur les probabilités](../M4-probabilites/01-variable-aleatoire-et-loi-binomiale.md).

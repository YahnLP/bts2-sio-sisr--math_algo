# Cours 1 – La dérivée et les variations

*BTS SIO SISR 2e année – Option mathématiques approfondies – M2, première partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : expliquer ce que mesure la dérivée ; calculer la dérivée de fonctions simples ; étudier le signe de la dérivée pour **dresser un tableau de variations** ; trouver un **extremum** et l'interpréter dans un problème.
>
> **Prérequis.** Le module M1 (fonctions, exponentielle, logarithme).
>
> **Programme.** La dérivée comme interprétation cinématique (vitesse) n'est pas au programme : on la voit comme **vitesse de variation** d'une grandeur quelconque, et comme **pente de la tangente**.

## 1. Pour démarrer : à quelle vitesse la grandeur change-t-elle ?

Le stock d'un serveur de fichiers évolue au cours du temps. Entre deux dates, on peut calculer la **variation moyenne** :

\[
\text{taux de variation entre } a \text{ et } b = \dfrac{f(b) - f(a)}{b - a}.
\]

C'est la **pente de la droite** qui joint les deux points de la courbe. Mais comment connaître la vitesse **à un instant précis** ? On resserre l'intervalle : \(b\) se rapproche de \(a\). La limite de ce taux, quand l'intervalle devient minuscule, est le **nombre dérivé**.

**Exemple.** Pour \(f(x) = x^2\) autour de \(a = 1\), on calcule le taux de variation entre \(1\) et \(1 + h\), pour des \(h\) de plus en plus petits :

| \(h\) | 1 | 0,1 | 0,01 |
|---|---|---|---|
| \(\dfrac{f(1+h) - f(1)}{h}\) | 3 | 2,1 | 2,01 |

Le taux se rapproche de **2** : on dit que le **nombre dérivé** de \(f\) en 1 vaut 2, et on écrit \(f'(1) = 2\).

## 2. Le nombre dérivé : la pente de la tangente

<figure class="fig-math">
<svg viewBox="0 0 520 320" role="img" aria-label="Tangente à y=x² en x=1">
<line class="fm-grid" x1="52" y1="282.0" x2="502" y2="282.0"/>
<text class="fm-t" x="46" y="286.0" text-anchor="end">−1</text>
<line class="fm-grid" x1="52" y1="244.0" x2="502" y2="244.0"/>
<text class="fm-t" x="46" y="248.0" text-anchor="end">0</text>
<line class="fm-grid" x1="52" y1="206.0" x2="502" y2="206.0"/>
<text class="fm-t" x="46" y="210.0" text-anchor="end">1</text>
<line class="fm-grid" x1="52" y1="168.0" x2="502" y2="168.0"/>
<text class="fm-t" x="46" y="172.0" text-anchor="end">2</text>
<line class="fm-grid" x1="52" y1="130.0" x2="502" y2="130.0"/>
<text class="fm-t" x="46" y="134.0" text-anchor="end">3</text>
<line class="fm-grid" x1="52" y1="92.0" x2="502" y2="92.0"/>
<text class="fm-t" x="46" y="96.0" text-anchor="end">4</text>
<line class="fm-grid" x1="52" y1="54.0" x2="502" y2="54.0"/>
<text class="fm-t" x="46" y="58.0" text-anchor="end">5</text>
<line class="fm-grid" x1="52" y1="16.0" x2="502" y2="16.0"/>
<text class="fm-t" x="46" y="20.0" text-anchor="end">6</text>
<line class="fm-grid" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t" x="52.0" y="298" text-anchor="middle">−1</text>
<line class="fm-grid" x1="164.5" y1="16" x2="164.5" y2="282"/>
<text class="fm-t" x="164.5" y="298" text-anchor="middle">0</text>
<line class="fm-grid" x1="277.0" y1="16" x2="277.0" y2="282"/>
<text class="fm-t" x="277.0" y="298" text-anchor="middle">1</text>
<line class="fm-grid" x1="389.5" y1="16" x2="389.5" y2="282"/>
<text class="fm-t" x="389.5" y="298" text-anchor="middle">2</text>
<line class="fm-grid" x1="502.0" y1="16" x2="502.0" y2="282"/>
<text class="fm-t" x="502.0" y="298" text-anchor="middle">3</text>
<line class="fm-axis" x1="52" y1="244.0" x2="502" y2="244.0"/>
<line class="fm-axis" x1="164.5" y1="16" x2="164.5" y2="282"/>
<text class="fm-t fm-i" x="502" y="314" text-anchor="end">x</text>
<text class="fm-t fm-i" x="56" y="24">y</text>
<polyline class="fm-curve" points="52.0,206.0 53.5,207.0 55.0,208.0 56.5,209.0 58.0,209.9 59.5,210.9 61.0,211.8 62.5,212.8 64.0,213.7 65.5,214.6 67.0,215.5 68.5,216.3 70.0,217.2 71.5,218.0 73.0,218.9 74.5,219.7 76.0,220.5 77.5,221.3 79.0,222.1 80.5,222.8 82.0,223.6 83.5,224.3 85.0,225.0 86.5,225.7 88.0,226.4 89.5,227.1 91.0,227.8 92.5,228.4 94.0,229.1 95.5,229.7 97.0,230.3 98.5,230.9 100.0,231.5 101.5,232.1 103.0,232.6 104.5,233.2 106.0,233.7 107.5,234.2 109.0,234.8 110.5,235.2 112.0,235.7 113.5,236.2 115.0,236.6 116.5,237.1 118.0,237.5 119.5,237.9 121.0,238.3 122.5,238.7 124.0,239.1 125.5,239.4 127.0,239.8 128.5,240.1 130.0,240.4 131.5,240.7 133.0,241.0 134.5,241.3 136.0,241.6 137.5,241.8 139.0,242.0 140.5,242.3 142.0,242.5 143.5,242.7 145.0,242.9 146.5,243.0 148.0,243.2 149.5,243.3 151.0,243.5 152.5,243.6 154.0,243.7 155.5,243.8 157.0,243.8 158.5,243.9 160.0,243.9 161.5,244.0 163.0,244.0 164.5,244.0 166.0,244.0 167.5,244.0 169.0,243.9 170.5,243.9 172.0,243.8 173.5,243.8 175.0,243.7 176.5,243.6 178.0,243.5 179.5,243.3 181.0,243.2 182.5,243.0 184.0,242.9 185.5,242.7 187.0,242.5 188.5,242.3 190.0,242.0 191.5,241.8 193.0,241.6 194.5,241.3 196.0,241.0 197.5,240.7 199.0,240.4 200.5,240.1 202.0,239.8 203.5,239.4 205.0,239.1 206.5,238.7 208.0,238.3 209.5,237.9 211.0,237.5 212.5,237.1 214.0,236.6 215.5,236.2 217.0,235.7 218.5,235.2 220.0,234.8 221.5,234.2 223.0,233.7 224.5,233.2 226.0,232.6 227.5,232.1 229.0,231.5 230.5,230.9 232.0,230.3 233.5,229.7 235.0,229.1 236.5,228.4 238.0,227.8 239.5,227.1 241.0,226.4 242.5,225.7 244.0,225.0 245.5,224.3 247.0,223.6 248.5,222.8 250.0,222.1 251.5,221.3 253.0,220.5 254.5,219.7 256.0,218.9 257.5,218.0 259.0,217.2 260.5,216.3 262.0,215.5 263.5,214.6 265.0,213.7 266.5,212.8 268.0,211.8 269.5,210.9 271.0,209.9 272.5,209.0 274.0,208.0 275.5,207.0 277.0,206.0 278.5,205.0 280.0,203.9 281.5,202.9 283.0,201.8 284.5,200.8 286.0,199.7 287.5,198.6 289.0,197.5 290.5,196.3 292.0,195.2 293.5,194.0 295.0,192.9 296.5,191.7 298.0,190.5 299.5,189.3 301.0,188.1 302.5,186.8 304.0,185.6 305.5,184.3 307.0,183.0 308.5,181.7 310.0,180.4 311.5,179.1 313.0,177.8 314.5,176.4 316.0,175.1 317.5,173.7 319.0,172.3 320.5,170.9 322.0,169.5 323.5,168.1 325.0,166.7 326.5,165.2 328.0,163.7 329.5,162.3 331.0,160.8 332.5,159.3 334.0,157.7 335.5,156.2 337.0,154.7 338.5,153.1 340.0,151.5 341.5,149.9 343.0,148.3 344.5,146.7 346.0,145.1 347.5,143.5 349.0,141.8 350.5,140.1 352.0,138.4 353.5,136.7 355.0,135.0 356.5,133.3 358.0,131.6 359.5,129.8 361.0,128.1 362.5,126.3 364.0,124.5 365.5,122.7 367.0,120.9 368.5,119.0 370.0,117.2 371.5,115.3 373.0,113.5 374.5,111.6 376.0,109.7 377.5,107.8 379.0,105.9 380.5,103.9 382.0,102.0 383.5,100.0 385.0,98.0 386.5,96.0 388.0,94.0 389.5,92.0 391.0,90.0 392.5,87.9 394.0,85.9 395.5,83.8 397.0,81.7 398.5,79.6 400.0,77.5 401.5,75.4 403.0,73.2 404.5,71.1 406.0,68.9 407.5,66.7 409.0,64.5 410.5,62.3 412.0,60.1 413.5,57.8 415.0,55.6 416.5,53.3 418.0,51.1 419.5,48.8 421.0,46.5 422.5,44.1 424.0,41.8 425.5,39.5 427.0,37.1 428.5,34.7 430.0,32.4 431.5,30.0 433.0,27.5 434.5,25.1 436.0,22.7 437.5,20.2 439.0,17.8 440.5,15.3 442.0,12.8"/>
<polyline class="fm-acc" points="156.6,287.3 157.9,286.5 159.1,285.6 160.3,284.8 161.6,284.0 162.8,283.1 164.1,282.3 165.3,281.5 166.5,280.6 167.8,279.8 169.0,279.0 170.2,278.1 171.5,277.3 172.7,276.5 173.9,275.6 175.2,274.8 176.4,273.9 177.7,273.1 178.9,272.3 180.1,271.4 181.4,270.6 182.6,269.8 183.8,268.9 185.1,268.1 186.3,267.3 187.6,266.4 188.8,265.6 190.0,264.7 191.3,263.9 192.5,263.1 193.8,262.2 195.0,261.4 196.2,260.6 197.5,259.7 198.7,258.9 199.9,258.1 201.2,257.2 202.4,256.4 203.6,255.6 204.9,254.7 206.1,253.9 207.4,253.0 208.6,252.2 209.8,251.4 211.1,250.5 212.3,249.7 213.5,248.9 214.8,248.0 216.0,247.2 217.3,246.4 218.5,245.5 219.7,244.7 221.0,243.8 222.2,243.0 223.4,242.2 224.7,241.3 225.9,240.5 227.2,239.7 228.4,238.8 229.6,238.0 230.9,237.2 232.1,236.3 233.3,235.5 234.6,234.7 235.8,233.8 237.1,233.0 238.3,232.1 239.5,231.3 240.8,230.5 242.0,229.6 243.3,228.8 244.5,228.0 245.7,227.1 247.0,226.3 248.2,225.5 249.4,224.6 250.7,223.8 251.9,222.9 253.1,222.1 254.4,221.3 255.6,220.4 256.9,219.6 258.1,218.8 259.3,217.9 260.6,217.1 261.8,216.3 263.0,215.4 264.3,214.6 265.5,213.8 266.8,212.9 268.0,212.1 269.2,211.2 270.5,210.4 271.7,209.6 272.9,208.7 274.2,207.9 275.4,207.1 276.7,206.2 277.9,205.4 279.1,204.6 280.4,203.7 281.6,202.9 282.9,202.0 284.1,201.2 285.3,200.4 286.6,199.5 287.8,198.7 289.0,197.9 290.3,197.0 291.5,196.2 292.8,195.4 294.0,194.5 295.2,193.7 296.5,192.9 297.7,192.0 298.9,191.2 300.2,190.3 301.4,189.5 302.6,188.7 303.9,187.8 305.1,187.0 306.4,186.2 307.6,185.3 308.8,184.5 310.1,183.7 311.3,182.8 312.5,182.0 313.8,181.1 315.0,180.3 316.3,179.5 317.5,178.6 318.7,177.8 320.0,177.0 321.2,176.1 322.4,175.3 323.7,174.5 324.9,173.6 326.2,172.8 327.4,172.0 328.6,171.1 329.9,170.3 331.1,169.4 332.4,168.6 333.6,167.8 334.8,166.9 336.1,166.1 337.3,165.3 338.5,164.4 339.8,163.6 341.0,162.8 342.2,161.9 343.5,161.1 344.7,160.2 346.0,159.4 347.2,158.6 348.4,157.7 349.7,156.9 350.9,156.1 352.2,155.2 353.4,154.4 354.6,153.6 355.9,152.7 357.1,151.9 358.3,151.1 359.6,150.2 360.8,149.4 362.0,148.5 363.3,147.7 364.5,146.9 365.8,146.0 367.0,145.2 368.2,144.4 369.5,143.5 370.7,142.7 371.9,141.9 373.2,141.0 374.4,140.2 375.7,139.3 376.9,138.5 378.1,137.7 379.4,136.8 380.6,136.0 381.8,135.2 383.1,134.3 384.3,133.5 385.6,132.7 386.8,131.8 388.0,131.0 389.3,130.2 390.5,129.3 391.8,128.5 393.0,127.6 394.2,126.8 395.5,126.0 396.7,125.1 397.9,124.3 399.2,123.5 400.4,122.6 401.7,121.8 402.9,121.0 404.1,120.1 405.4,119.3 406.6,118.4 407.8,117.6 409.1,116.8 410.3,115.9 411.5,115.1 412.8,114.3 414.0,113.4 415.3,112.6 416.5,111.8 417.7,110.9 419.0,110.1 420.2,109.3 421.4,108.4 422.7,107.6 423.9,106.7 425.2,105.9 426.4,105.1 427.6,104.2 428.9,103.4 430.1,102.6 431.3,101.7 432.6,100.9 433.8,100.1 435.1,99.2 436.3,98.4 437.5,97.5 438.8,96.7 440.0,95.9 441.2,95.0 442.5,94.2 443.7,93.4 445.0,92.5 446.2,91.7 447.4,90.9 448.7,90.0 449.9,89.2 451.1,88.4 452.4,87.5 453.6,86.7 454.9,85.8 456.1,85.0 457.3,84.2 458.6,83.3 459.8,82.5 461.1,81.7 462.3,80.8 463.5,80.0 464.8,79.2 466.0,78.3 467.2,77.5 468.5,76.6 469.7,75.8 470.9,75.0 472.2,74.1 473.4,73.3 474.7,72.5 475.9,71.6 477.1,70.8 478.4,70.0 479.6,69.1 480.8,68.3 482.1,67.5 483.3,66.6 484.6,65.8 485.8,64.9 487.0,64.1 488.3,63.3 489.5,62.4 490.8,61.6"/>
<line class="fm-dash" x1="277.0" y1="206.0" x2="389.5" y2="206.0"/>
<line class="fm-dash" x1="389.5" y1="206.0" x2="389.5" y2="130.0"/>
<circle class="fm-pt" cx="277.0" cy="206.0" r="4.5"/>
<text class="fm-t" x="333.2" y="222.0" text-anchor="middle">+1</text>
<text class="fm-t" x="397.5" y="172.0" text-anchor="start">+2</text>
<text class="fm-t fm-acc-t" x="316.4" y="263.0" text-anchor="start">tangente : y = 2x − 1</text>
<text class="fm-t" x="67.2" y="42.6" text-anchor="start">f(x) = x²</text>
</svg>
<figcaption>Au point d’abscisse 1, la tangente a pour pente 2 : quand x augmente de 1, la tangente monte de 2. C’est le nombre dérivé f′(1) = 2.</figcaption>
</figure>

Géométriquement, \(f'(a)\) est la **pente de la tangente** à la courbe au point d'abscisse \(a\). Sur la figure, la tangente en \(x = 1\) est la droite \(y = 2x - 1\) : quand \(x\) augmente de 1, elle monte de 2.

**Équation de la tangente en \(a\).** \(y = f'(a)\,(x - a) + f(a)\). Ici : \(y = 2(x - 1) + 1 = 2x - 1\).

**Ce que dit le signe de \(f'(a)\).**

- \(f'(a) > 0\) : la fonction **monte** près de \(a\) ;
- \(f'(a) < 0\) : la fonction **descend** près de \(a\) ;
- \(f'(a) = 0\) : tangente horizontale, c'est souvent la trace d'un **maximum** ou d'un **minimum**.

## 3. La fonction dérivée

Plutôt que de recalculer un nombre dérivé en chaque point, on définit la **fonction dérivée** \(f'\), qui donne la pente en tout point. Il suffit de connaître quelques dérivées usuelles et quelques règles.

**Dérivées usuelles.**

| \(f(x)\) | \(f'(x)\) |
|---|---|
| \(k\) (constante) | \(0\) |
| \(x\) | \(1\) |
| \(x^{n}\) | \(n\,x^{n-1}\) |
| \(\dfrac{1}{x}\) | \(-\dfrac{1}{x^{2}}\) |
| \(e^{x}\) | \(e^{x}\) |
| \(\ln x\) | \(\dfrac{1}{x}\) |

**Règles de calcul.**

| Opération | Règle |
|---|---|
| Somme | \((u + v)' = u' + v'\) |
| Multiple d'une constante | \((k\,u)' = k\,u'\) |
| Produit | \((u\,v)' = u'\,v + u\,v'\) |
| Quotient | \(\left(\dfrac{u}{v}\right)' = \dfrac{u'\,v - u\,v'}{v^{2}}\) |
| Exponentielle d'une fonction | \((e^{u})' = u'\,e^{u}\) |

**Exemples résolus.**

<details markdown="1">
<summary>1. Dériver \(f(x) = 3x^2 - 4x + 1\)</summary>

On dérive terme à terme : \((3x^2)' = 3 \times 2x = 6x\), \((-4x)' = -4\), \((1)' = 0\). Donc \(f'(x) = 6x - 4\).

</details>

<details markdown="1">
<summary>2. Dériver \(g(x) = x\,e^{x}\) (un produit)</summary>

Avec \(u = x\) et \(v = e^{x}\) : \(u' = 1\) et \(v' = e^{x}\). Donc \(g'(x) = 1 \times e^{x} + x \times e^{x} = (1 + x)e^{x}\).

</details>

<details markdown="1">
<summary>3. Dériver \(h(x) = \dfrac{2x + 1}{x + 1}\) (un quotient)</summary>

Avec \(u = 2x + 1\) (\(u' = 2\)) et \(v = x + 1\) (\(v' = 1\)) :

\[
h'(x) = \dfrac{2(x + 1) - (2x + 1) \times 1}{(x + 1)^2} = \dfrac{2x + 2 - 2x - 1}{(x + 1)^2} = \dfrac{1}{(x + 1)^2}.
\]

</details>

<details markdown="1">
<summary>4. Dériver \(k(x) = e^{-0{,}5x}\) (composée)</summary>

Ici \(u = -0{,}5x\), donc \(u' = -0{,}5\) et \(k'(x) = -0{,}5\,e^{-0{,}5x}\).

</details>

> [!TIP]
> **La calculatrice formelle dérive à ta place**, mais l'épreuve te demande souvent de **justifier** : sois capable de dériver à la main les cas ci-dessus. En revanche, il n'y a pas à retrouver une formule par lecture inverse du tableau.

## 4. Du signe de la dérivée aux variations

**Le théorème à connaître.** Sur un intervalle :

- si \(f'(x) > 0\) partout, alors \(f\) est **croissante** ;
- si \(f'(x) < 0\) partout, alors \(f\) est **décroissante** ;
- si \(f'(x) = 0\) partout, alors \(f\) est **constante**.

**Méthode en 5 étapes pour dresser un tableau de variations.**

1. Calculer \(f'(x)\).
2. **Factoriser** \(f'(x)\) pour pouvoir étudier son signe (produit de facteurs dont on connaît le signe).
3. Étudier le **signe** de \(f'(x)\) selon \(x\).
4. En déduire le **sens de variation** de \(f\).
5. Calculer les **valeurs** de \(f\) aux bornes et aux points où \(f'\) s'annule.

**Exemple résolu.** Étudier \(f(x) = x^3 - 6x^2 + 9x + 1\) sur \([0\,;\,5]\).

<figure class="fig-math">
<svg viewBox="0 0 520 320" role="img" aria-label="Courbe de x³−6x²+9x+1">
<line class="fm-grid" x1="52" y1="232.7" x2="502" y2="232.7"/>
<text class="fm-t" x="46" y="236.7" text-anchor="end">0</text>
<line class="fm-grid" x1="52" y1="183.5" x2="502" y2="183.5"/>
<text class="fm-t" x="46" y="187.5" text-anchor="end">5</text>
<line class="fm-grid" x1="52" y1="134.2" x2="502" y2="134.2"/>
<text class="fm-t" x="46" y="138.2" text-anchor="end">10</text>
<line class="fm-grid" x1="52" y1="85.0" x2="502" y2="85.0"/>
<text class="fm-t" x="46" y="89.0" text-anchor="end">15</text>
<line class="fm-grid" x1="52" y1="35.7" x2="502" y2="35.7"/>
<text class="fm-t" x="46" y="39.7" text-anchor="end">20</text>
<line class="fm-grid" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t" x="52.0" y="298" text-anchor="middle">0</text>
<line class="fm-grid" x1="142.0" y1="16" x2="142.0" y2="282"/>
<text class="fm-t" x="142.0" y="298" text-anchor="middle">1</text>
<line class="fm-grid" x1="232.0" y1="16" x2="232.0" y2="282"/>
<text class="fm-t" x="232.0" y="298" text-anchor="middle">2</text>
<line class="fm-grid" x1="322.0" y1="16" x2="322.0" y2="282"/>
<text class="fm-t" x="322.0" y="298" text-anchor="middle">3</text>
<line class="fm-grid" x1="412.0" y1="16" x2="412.0" y2="282"/>
<text class="fm-t" x="412.0" y="298" text-anchor="middle">4</text>
<line class="fm-grid" x1="502.0" y1="16" x2="502.0" y2="282"/>
<text class="fm-t" x="502.0" y="298" text-anchor="middle">5</text>
<line class="fm-axis" x1="52" y1="232.7" x2="502" y2="232.7"/>
<line class="fm-axis" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t fm-i" x="502" y="314" text-anchor="end">x</text>
<text class="fm-t fm-i" x="56" y="24">f(x)</text>
<polyline class="fm-curve" points="52.0,222.9 53.5,221.4 55.0,220.0 56.5,218.6 58.0,217.2 59.5,215.9 61.0,214.6 62.5,213.3 64.0,212.1 65.5,210.9 67.0,209.7 68.5,208.6 70.0,207.4 71.5,206.4 73.0,205.3 74.5,204.3 76.0,203.3 77.5,202.3 79.0,201.3 80.5,200.4 82.0,199.5 83.5,198.7 85.0,197.8 86.5,197.0 88.0,196.2 89.5,195.5 91.0,194.8 92.5,194.1 94.0,193.4 95.5,192.7 97.0,192.1 98.5,191.5 100.0,190.9 101.5,190.4 103.0,189.8 104.5,189.3 106.0,188.8 107.5,188.4 109.0,187.9 110.5,187.5 112.0,187.1 113.5,186.8 115.0,186.4 116.5,186.1 118.0,185.8 119.5,185.5 121.0,185.2 122.5,185.0 124.0,184.7 125.5,184.5 127.0,184.3 128.5,184.2 130.0,184.0 131.5,183.9 133.0,183.8 134.5,183.7 136.0,183.6 137.5,183.6 139.0,183.5 140.5,183.5 142.0,183.5 143.5,183.5 145.0,183.5 146.5,183.6 148.0,183.6 149.5,183.7 151.0,183.8 152.5,183.9 154.0,184.0 155.5,184.1 157.0,184.3 158.5,184.4 160.0,184.6 161.5,184.8 163.0,185.0 164.5,185.2 166.0,185.4 167.5,185.6 169.0,185.9 170.5,186.1 172.0,186.4 173.5,186.7 175.0,187.0 176.5,187.3 178.0,187.6 179.5,187.9 181.0,188.2 182.5,188.6 184.0,188.9 185.5,189.3 187.0,189.6 188.5,190.0 190.0,190.4 191.5,190.8 193.0,191.2 194.5,191.6 196.0,192.0 197.5,192.4 199.0,192.8 200.5,193.3 202.0,193.7 203.5,194.1 205.0,194.6 206.5,195.0 208.0,195.5 209.5,196.0 211.0,196.4 212.5,196.9 214.0,197.4 215.5,197.8 217.0,198.3 218.5,198.8 220.0,199.3 221.5,199.8 223.0,200.2 224.5,200.7 226.0,201.2 227.5,201.7 229.0,202.2 230.5,202.7 232.0,203.2 233.5,203.7 235.0,204.2 236.5,204.7 238.0,205.2 239.5,205.6 241.0,206.1 242.5,206.6 244.0,207.1 245.5,207.6 247.0,208.1 248.5,208.5 250.0,209.0 251.5,209.5 253.0,210.0 254.5,210.4 256.0,210.9 257.5,211.3 259.0,211.8 260.5,212.2 262.0,212.7 263.5,213.1 265.0,213.5 266.5,214.0 268.0,214.4 269.5,214.8 271.0,215.2 272.5,215.6 274.0,216.0 275.5,216.4 277.0,216.7 278.5,217.1 280.0,217.5 281.5,217.8 283.0,218.1 284.5,218.5 286.0,218.8 287.5,219.1 289.0,219.4 290.5,219.7 292.0,220.0 293.5,220.2 295.0,220.5 296.5,220.7 298.0,221.0 299.5,221.2 301.0,221.4 302.5,221.6 304.0,221.8 305.5,222.0 307.0,222.1 308.5,222.3 310.0,222.4 311.5,222.5 313.0,222.6 314.5,222.7 316.0,222.8 317.5,222.8 319.0,222.9 320.5,222.9 322.0,222.9 323.5,222.9 325.0,222.9 326.5,222.8 328.0,222.8 329.5,222.7 331.0,222.6 332.5,222.5 334.0,222.3 335.5,222.2 337.0,222.0 338.5,221.8 340.0,221.6 341.5,221.4 343.0,221.2 344.5,220.9 346.0,220.6 347.5,220.3 349.0,220.0 350.5,219.6 352.0,219.2 353.5,218.8 355.0,218.4 356.5,218.0 358.0,217.5 359.5,217.0 361.0,216.5 362.5,216.0 364.0,215.5 365.5,214.9 367.0,214.3 368.5,213.6 370.0,213.0 371.5,212.3 373.0,211.6 374.5,210.9 376.0,210.1 377.5,209.3 379.0,208.5 380.5,207.7 382.0,206.8 383.5,205.9 385.0,205.0 386.5,204.1 388.0,203.1 389.5,202.1 391.0,201.1 392.5,200.0 394.0,198.9 395.5,197.8 397.0,196.7 398.5,195.5 400.0,194.3 401.5,193.0 403.0,191.8 404.5,190.5 406.0,189.1 407.5,187.8 409.0,186.4 410.5,184.9 412.0,183.5 413.5,182.0 415.0,180.5 416.5,178.9 418.0,177.3 419.5,175.7 421.0,174.0 422.5,172.3 424.0,170.6 425.5,168.8 427.0,167.0 428.5,165.2 430.0,163.3 431.5,161.4 433.0,159.4 434.5,157.5 436.0,155.4 437.5,153.4 439.0,151.3 440.5,149.2 442.0,147.0 443.5,144.8 445.0,142.5 446.5,140.3 448.0,137.9 449.5,135.6 451.0,133.2 452.5,130.7 454.0,128.2 455.5,125.7 457.0,123.1 458.5,120.5 460.0,117.9 461.5,115.2 463.0,112.5 464.5,109.7 466.0,106.9 467.5,104.0 469.0,101.1 470.5,98.2 472.0,95.2 473.5,92.1 475.0,89.1 476.5,86.0 478.0,82.8 479.5,79.6 481.0,76.3 482.5,73.0 484.0,69.7 485.5,66.3 487.0,62.8 488.5,59.4 490.0,55.8 491.5,52.2 493.0,48.6 494.5,44.9 496.0,41.2 497.5,37.5 499.0,33.6 500.5,29.8 502.0,25.9"/>
<circle class="fm-pt" cx="142.0" cy="183.5" r="4.5"/>
<circle class="fm-pt" cx="322.0" cy="222.9" r="4.5"/>
<circle class="fm-pt2" cx="502.0" cy="25.9" r="4.5"/>
<text class="fm-t" x="152.0" y="175.5" text-anchor="start">maximum local (1 ; 5)</text>
<text class="fm-t" x="322.0" y="248.5" text-anchor="middle">minimum local (3 ; 1)</text>
<text class="fm-t" x="492.0" y="41.9" text-anchor="end">(5 ; 21)</text>
</svg>
<figcaption>La fonction monte jusqu’à x = 1, descend jusqu’à x = 3, puis remonte : f′ change de signe en 1 et en 3.</figcaption>
</figure>

<details markdown="1">
<summary>Voir la solution détaillée</summary>

**Étape 1.** \(f'(x) = 3x^2 - 12x + 9\).

**Étape 2 (factorisation).** On met 3 en facteur : \(f'(x) = 3(x^2 - 4x + 3)\). Le trinôme \(x^2 - 4x + 3\) a pour discriminant \(16 - 12 = 4\), donc deux racines : \(\dfrac{4 - 2}{2} = 1\) et \(\dfrac{4 + 2}{2} = 3\). Ainsi \(f'(x) = 3(x - 1)(x - 3)\).

**Étape 3 (signe).** Le facteur 3 est positif. Pour \((x - 1)(x - 3)\) : positif si \(x < 1\) (les deux facteurs sont négatifs), négatif si \(1 < x < 3\) (un facteur négatif et un positif), positif si \(x > 3\).

**Étapes 4 et 5 (tableau).**

| \(x\) | 0 | | 1 | | 3 | | 5 |
|---|---|---|---|---|---|---|---|
| Signe de \(f'(x)\) | | \(+\) | \(0\) | \(-\) | \(0\) | \(+\) | |
| Variations de \(f\) | 1 | croît | 5 | décroît | 1 | croît | 21 |

Valeurs : \(f(0) = 1\) ; \(f(1) = 1 - 6 + 9 + 1 = 5\) ; \(f(3) = 27 - 54 + 27 + 1 = 1\) ; \(f(5) = 125 - 150 + 45 + 1 = 21\).

**Lecture.** La courbe monte de 1 à 5, descend jusqu'à 1, puis remonte jusqu'à 21. Le point \((1\,;\,5)\) est un **maximum local**, le point \((3\,;\,1)\) un **minimum local**. Sur tout l'intervalle \([0\,;\,5]\), le plus grand résultat est 21 (atteint au bord, en \(x = 5\)) et le plus petit est 1 (atteint en \(x = 0\) et en \(x = 3\)).

</details>

> [!WARNING]
> **Piège.** \(f'(x) = 0\) ne suffit **pas** pour affirmer qu'il y a un extremum : il faut que le **signe de \(f'\) change** de part et d'autre. Par exemple, pour \(f(x) = x^3\), \(f'(0) = 0\) mais \(f'\) reste positive des deux côtés : il n'y a ni maximum ni minimum en 0.

## 5. Optimiser : trouver le meilleur choix

Un **extremum** répond aux questions du type « pour quelle valeur le coût est-il minimal ? » ou « quand la charge est-elle maximale ? ». C'est l'une des applications les plus fréquentes.

**Exemple résolu.** Le coût moyen de production, en euros par unité, de \(q\) unités est \(CM(q) = q + \dfrac{100}{q}\) pour \(q > 0\). Pour quelle quantité est-il minimal ?

<details markdown="1">
<summary>Voir la solution détaillée</summary>

**Dérivée.** \(CM'(q) = 1 - \dfrac{100}{q^{2}} = \dfrac{q^{2} - 100}{q^{2}}\).

**Signe.** Pour \(q > 0\), le dénominateur \(q^2\) est positif : le signe est celui de \(q^2 - 100\), négatif pour \(q < 10\), positif pour \(q > 10\).

**Variations.** \(CM\) **décroît** jusqu'à \(q = 10\), puis **croît**. Le minimum est donc en \(q = 10\), de valeur \(CM(10) = 10 + 10 = 20\) euros par unité.

**Contrôle.** \(CM(5) = 25\) et \(CM(20) = 25\), tous deux supérieurs à 20 : le minimum est confirmé.

**Interprétation.** Produire **10 unités** minimise le coût moyen, à 20 € l'unité. Au-delà, le coût moyen remonte (par exemple à 25 € pour 20 unités), car les coûts qui grandissent avec la quantité l'emportent sur la répartition des frais fixes.

</details>

## 6. À retenir

> [!NOTE]
> - \(f'(a)\) est la **pente de la tangente** en \(a\) et mesure la **vitesse de variation** instantanée.
> - Dérivées usuelles : \((x^{n})' = nx^{n-1}\), \((e^{x})' = e^{x}\), \((\ln x)' = \dfrac{1}{x}\) ; règles de la somme, du produit, du quotient, de \((e^{u})'\).
> - \(f' > 0\) : \(f\) croît ; \(f' < 0\) : \(f\) décroît.
> - Méthode du tableau : **dériver, factoriser, signe, variations, valeurs**.
> - Un extremum demande que \(f'\) **s'annule en changeant de signe**.
> - Toujours **interpréter** le résultat dans le contexte (unité, valeur acceptable).

## 7. Teste-toi

**Question 1.** Dériver \(f(x) = 5x^2 - 3x + 2\) et \(g(x) = x^2 e^{x}\).

**Question 2.** Étudier les variations de \(f(x) = x^2 - 4x\) et donner son minimum.

**Question 3.** Pour \(f(x) = x^2\), écrire l'équation de la tangente en \(x = 3\).

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(f'(x) = 10x - 3\). Pour \(g\), produit de \(u = x^2\) (\(u' = 2x\)) et \(v = e^{x}\) : \(g'(x) = 2x\,e^{x} + x^2 e^{x} = (2x + x^2)e^{x}\).
2. \(f'(x) = 2x - 4 = 2(x - 2)\), négatif pour \(x < 2\), positif pour \(x > 2\) : \(f\) décroît puis croît, avec un minimum en \(x = 2\) valant \(f(2) = 4 - 8 = -4\).
3. \(f'(3) = 6\) et \(f(3) = 9\), donc \(y = 6(x - 3) + 9 = 6x - 9\).

</details>

**Pour continuer :** le [cours 2 sur les limites et les asymptotes](02-limites-et-asymptotes.md).

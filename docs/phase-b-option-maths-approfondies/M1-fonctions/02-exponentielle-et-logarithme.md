# Cours 2 – Exponentielle et logarithme

*BTS SIO SISR 2e année – Option mathématiques approfondies – M1, seconde partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : reconnaître une croissance ou une décroissance exponentielle ; utiliser les puissances et la fonction exponentielle ; comprendre le logarithme comme l'outil qui **retrouve un exposant** ; résoudre une équation d'exposant ; calculer un **seuil** (le plus petit entier qui dépasse une valeur).
>
> **Prérequis.** Le [cours 1](01-fonctions-et-modeles.md) et les puissances entières.

## 1. Pour démarrer : une croissance qui s'emballe

Le stockage d'une entreprise augmente de 5 % chaque année. Il vaut 1 000 Go aujourd'hui. Chaque année, on **multiplie** par \(1{,}05\) :

| Année \(n\) | 0 | 1 | 2 | 3 | 10 |
|---|---|---|---|---|---|
| Stockage (Go) | 1 000 | 1 050 | 1 102,5 | 1 157,6 | 1 628,9 |

La formule est \(S(n) = 1000 \times 1{,}05^{\,n}\). Ce n'est **pas** une fonction affine : on n'ajoute pas toujours la même quantité (50 Go), on multiplie toujours par le même facteur (1,05). Plus le stock est grand, plus il grandit vite : c'est la **croissance exponentielle**.

## 2. Les fonctions exponentielles

**Définition.** Pour un nombre \(a > 0\), la fonction \(x \mapsto a^{x}\) est une fonction exponentielle de **base** \(a\).

- Si \(a > 1\), elle est **croissante** (croissance : \(a = 1{,}05\) pour \(+5\) %).
- Si \(0 < a < 1\), elle est **décroissante** (décroissance : \(a = 0{,}85\) pour \(-15\) %).
- Elle est **toujours strictement positive** : \(a^{x} > 0\), quelle que soit la valeur de \(x\).
- \(a^{0} = 1\) : toutes ces courbes passent par le point \((0\,;\,1)\).

**Lien avec les pourcentages.** Une évolution de \(t\) % par période se traduit par un **coefficient multiplicateur** \(a = 1 + \dfrac{t}{100}\). Pour une baisse, \(t\) est négatif.

| Évolution | Coefficient \(a\) |
|---|---|
| \(+5\) % | \(1{,}05\) |
| \(+20\) % | \(1{,}2\) |
| \(-15\) % | \(0{,}85\) |
| \(-50\) % | \(0{,}5\) |

**Exemple résolu.** Un serveur acheté 2 000 € perd 15 % de sa valeur chaque année. Quelle est sa valeur après 3 ans ?

<details markdown="1">
<summary>Voir la solution</summary>

Chaque année, on multiplie par \(0{,}85\). Après \(n\) années : \(V(n) = 2000 \times 0{,}85^{\,n}\). Pour \(n = 3\) : \(0{,}85^{3} = 0{,}614125\), donc \(V(3) = 1\,228{,}25\) €.

**Contrôle :** perdre 15 % trois fois ne fait pas perdre 45 % (ce serait \(1\,100\) €) : la perte se calcule à chaque fois sur la valeur restante, d'où une valeur finale supérieure.

</details>

### Le nombre e et la fonction exponentielle

Parmi toutes les bases possibles, une est privilégiée en sciences : le nombre \(e \approx 2{,}718\). La fonction \(x \mapsto e^{x}\) (touche **exp** ou \(e^{x}\) de la calculatrice) est **la** fonction exponentielle. Elle a une propriété remarquable : sa **dérivée est elle-même** (on le verra dans le module M2), ce qui la rend naturelle pour décrire les phénomènes où la vitesse de variation est proportionnelle à la quantité présente (pannes, désintégration, charge d'un condensateur).

**Règles de calcul** (valables pour toutes les bases) :

\[
e^{a+b} = e^{a}\,e^{b}, \qquad e^{a-b} = \dfrac{e^{a}}{e^{b}}, \qquad (e^{a})^{n} = e^{na}, \qquad e^{-a} = \dfrac{1}{e^{a}}.
\]

> [!TIP]
> **Astuce.** Si tu hésites sur une règle, teste-la sur des nombres simples : \(e^{1+1} = e^{2}\) et \(e^{1} \times e^{1} = e^{2}\). Ça marche ; en revanche \(e^{1} + e^{1} = 2e\), qui n'est **pas** \(e^{2}\) : l'exponentielle transforme les **sommes d'exposants** en **produits**, pas les sommes de puissances.

## 3. Le logarithme népérien : retrouver un exposant

**Le problème.** Dans l'exemple du stockage, on veut savoir **au bout de combien d'années** on atteint 1 500 Go. Il faut résoudre \(1{,}05^{\,n} = 1{,}5\) : l'inconnue est **dans l'exposant**. Aucune opération simple (addition, multiplication, racine) ne permet de « descendre » l'exposant. Il faut un nouvel outil.

**Définition.** Pour \(x > 0\), le **logarithme népérien** de \(x\), noté \(\ln x\), est **l'exposant auquel il faut élever \(e\) pour obtenir \(x\)** :

\[
\ln x = y \iff e^{y} = x.
\]

Exemples : \(\ln(e^{3}) = 3\) ; \(\ln(1) = 0\) car \(e^{0} = 1\) ; \(\ln(e) = 1\). Le logarithme n'existe **que pour \(x > 0\)** : l'exponentielle étant toujours positive, on ne peut obtenir un nombre négatif ou nul.

<figure class="fig-math">
<svg viewBox="0 0 520 320" role="img" aria-label="Exponentielle et logarithme">
<line class="fm-grid" x1="52" y1="282.0" x2="502" y2="282.0"/>
<text class="fm-t" x="46" y="286.0" text-anchor="end">−2</text>
<line class="fm-grid" x1="52" y1="237.7" x2="502" y2="237.7"/>
<text class="fm-t" x="46" y="241.7" text-anchor="end">−1</text>
<line class="fm-grid" x1="52" y1="193.3" x2="502" y2="193.3"/>
<text class="fm-t" x="46" y="197.3" text-anchor="end">0</text>
<line class="fm-grid" x1="52" y1="149.0" x2="502" y2="149.0"/>
<text class="fm-t" x="46" y="153.0" text-anchor="end">1</text>
<line class="fm-grid" x1="52" y1="104.7" x2="502" y2="104.7"/>
<text class="fm-t" x="46" y="108.7" text-anchor="end">2</text>
<line class="fm-grid" x1="52" y1="60.3" x2="502" y2="60.3"/>
<text class="fm-t" x="46" y="64.3" text-anchor="end">3</text>
<line class="fm-grid" x1="52" y1="16.0" x2="502" y2="16.0"/>
<text class="fm-t" x="46" y="20.0" text-anchor="end">4</text>
<line class="fm-grid" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t" x="52.0" y="298" text-anchor="middle">−2</text>
<line class="fm-grid" x1="127.0" y1="16" x2="127.0" y2="282"/>
<text class="fm-t" x="127.0" y="298" text-anchor="middle">−1</text>
<line class="fm-grid" x1="202.0" y1="16" x2="202.0" y2="282"/>
<text class="fm-t" x="202.0" y="298" text-anchor="middle">0</text>
<line class="fm-grid" x1="277.0" y1="16" x2="277.0" y2="282"/>
<text class="fm-t" x="277.0" y="298" text-anchor="middle">1</text>
<line class="fm-grid" x1="352.0" y1="16" x2="352.0" y2="282"/>
<text class="fm-t" x="352.0" y="298" text-anchor="middle">2</text>
<line class="fm-grid" x1="427.0" y1="16" x2="427.0" y2="282"/>
<text class="fm-t" x="427.0" y="298" text-anchor="middle">3</text>
<line class="fm-grid" x1="502.0" y1="16" x2="502.0" y2="282"/>
<text class="fm-t" x="502.0" y="298" text-anchor="middle">4</text>
<line class="fm-axis" x1="52" y1="193.3" x2="502" y2="193.3"/>
<line class="fm-axis" x1="202.0" y1="16" x2="202.0" y2="282"/>
<text class="fm-t fm-i" x="502" y="314" text-anchor="end">x</text>
<text class="fm-t fm-i" x="56" y="24">y</text>
<line class="fm-dash" x1="52.0" y1="282.0" x2="502.0" y2="16.0"/>
<polyline class="fm-curve" points="52.0,187.3 53.5,187.2 55.0,187.1 56.5,187.0 58.0,186.8 59.5,186.7 61.0,186.6 62.5,186.4 64.0,186.3 65.5,186.2 67.0,186.0 68.5,185.9 70.0,185.7 71.5,185.6 73.0,185.4 74.5,185.2 76.0,185.1 77.5,184.9 79.0,184.7 80.5,184.6 82.0,184.4 83.5,184.2 85.0,184.0 86.5,183.8 88.0,183.6 89.5,183.4 91.0,183.2 92.5,183.0 94.0,182.8 95.5,182.6 97.0,182.4 98.5,182.2 100.0,182.0 101.5,181.7 103.0,181.5 104.5,181.3 106.0,181.0 107.5,180.8 109.0,180.5 110.5,180.2 112.0,180.0 113.5,179.7 115.0,179.4 116.5,179.2 118.0,178.9 119.5,178.6 121.0,178.3 122.5,178.0 124.0,177.7 125.5,177.3 127.0,177.0 128.5,176.7 130.0,176.4 131.5,176.0 133.0,175.7 134.5,175.3 136.0,174.9 137.5,174.6 139.0,174.2 140.5,173.8 142.0,173.4 143.5,173.0 145.0,172.6 146.5,172.2 148.0,171.8 149.5,171.3 151.0,170.9 152.5,170.4 154.0,170.0 155.5,169.5 157.0,169.0 158.5,168.5 160.0,168.0 161.5,167.5 163.0,167.0 164.5,166.4 166.0,165.9 167.5,165.3 169.0,164.8 170.5,164.2 172.0,163.6 173.5,163.0 175.0,162.4 176.5,161.8 178.0,161.1 179.5,160.5 181.0,159.8 182.5,159.2 184.0,158.5 185.5,157.8 187.0,157.0 188.5,156.3 190.0,155.6 191.5,154.8 193.0,154.0 194.5,153.2 196.0,152.4 197.5,151.6 199.0,150.7 200.5,149.9 202.0,149.0 203.5,148.1 205.0,147.2 206.5,146.3 208.0,145.3 209.5,144.3 211.0,143.3 212.5,142.3 214.0,141.3 215.5,140.3 217.0,139.2 218.5,138.1 220.0,137.0 221.5,135.8 223.0,134.7 224.5,133.5 226.0,132.3 227.5,131.0 229.0,129.8 230.5,128.5 232.0,127.2 233.5,125.9 235.0,124.5 236.5,123.1 238.0,121.7 239.5,120.2 241.0,118.8 242.5,117.3 244.0,115.7 245.5,114.2 247.0,112.6 248.5,110.9 250.0,109.3 251.5,107.6 253.0,105.8 254.5,104.1 256.0,102.3 257.5,100.4 259.0,98.5 260.5,96.6 262.0,94.7 263.5,92.7 265.0,90.6 266.5,88.6 268.0,86.5 269.5,84.3 271.0,82.1 272.5,79.8 274.0,77.5 275.5,75.2 277.0,72.8 278.5,70.4 280.0,67.9 281.5,65.4 283.0,62.8 284.5,60.1 286.0,57.5 287.5,54.7 289.0,51.9 290.5,49.1 292.0,46.1 293.5,43.2 295.0,40.1 296.5,37.0 298.0,33.9 299.5,30.7 301.0,27.4 302.5,24.0 304.0,20.6 305.5,17.1 307.0,13.6"/>
<polyline class="fm-curve2" points="211.1,287.0 212.1,282.3 213.1,278.1 214.1,274.3 215.1,270.8 216.1,267.5 217.1,264.5 218.1,261.6 219.1,259.0 220.1,256.4 221.1,254.0 222.1,251.8 223.1,249.6 224.1,247.6 225.1,245.6 226.1,243.7 227.1,241.9 228.1,240.2 229.1,238.5 230.1,236.9 231.1,235.4 232.1,233.9 233.1,232.4 234.1,231.0 235.1,229.6 236.1,228.3 237.1,227.0 238.1,225.8 239.1,224.6 240.1,223.4 241.1,222.2 242.1,221.1 243.1,220.0 244.1,219.0 245.1,217.9 246.1,216.9 247.1,215.9 248.1,214.9 249.1,214.0 250.1,213.1 251.1,212.1 252.1,211.3 253.1,210.4 254.1,209.5 255.1,208.7 256.1,207.8 257.1,207.0 258.1,206.2 259.1,205.5 260.1,204.7 261.1,203.9 262.1,203.2 263.1,202.4 264.1,201.7 265.1,201.0 266.1,200.3 267.1,199.6 268.1,199.0 269.1,198.3 270.1,197.6 271.1,197.0 272.1,196.4 273.1,195.7 274.1,195.1 275.1,194.5 276.1,193.9 277.1,193.3 278.1,192.7 279.1,192.1 280.1,191.6 281.1,191.0 282.1,190.4 283.1,189.9 284.1,189.3 285.1,188.8 286.1,188.3 287.1,187.8 288.1,187.2 289.1,186.7 290.1,186.2 291.1,185.7 292.1,185.2 293.1,184.7 294.1,184.3 295.1,183.8 296.1,183.3 297.1,182.8 298.1,182.4 299.1,181.9 300.1,181.5 301.1,181.0 302.0,180.6 303.0,180.1 304.0,179.7 305.0,179.2 306.0,178.8 307.0,178.4 308.0,178.0 309.0,177.6 310.0,177.1 311.0,176.7 312.0,176.3 313.0,175.9 314.0,175.5 315.0,175.1 316.0,174.8 317.0,174.4 318.0,174.0 319.0,173.6 320.0,173.2 321.0,172.9 322.0,172.5 323.0,172.1 324.0,171.7 325.0,171.4 326.0,171.0 327.0,170.7 328.0,170.3 329.0,170.0 330.0,169.6 331.0,169.3 332.0,168.9 333.0,168.6 334.0,168.3 335.0,167.9 336.0,167.6 337.0,167.3 338.0,166.9 339.0,166.6 340.0,166.3 341.0,166.0 342.0,165.6 343.0,165.3 344.0,165.0 345.0,164.7 346.0,164.4 347.0,164.1 348.0,163.8 349.0,163.5 350.0,163.2 351.0,162.9 352.0,162.6 353.0,162.3 354.0,162.0 355.0,161.7 356.0,161.4 357.0,161.1 358.0,160.9 359.0,160.6 360.0,160.3 361.0,160.0 362.0,159.7 363.0,159.5 364.0,159.2 365.0,158.9 366.0,158.6 367.0,158.4 368.0,158.1 369.0,157.8 370.0,157.6 371.0,157.3 372.0,157.0 373.0,156.8 374.0,156.5 375.0,156.3 376.0,156.0 377.0,155.8 378.0,155.5 379.0,155.3 380.0,155.0 381.0,154.8 382.0,154.5 383.0,154.3 384.0,154.0 385.0,153.8 386.0,153.5 387.0,153.3 388.0,153.1 389.0,152.8 390.0,152.6 391.0,152.4 392.0,152.1 393.0,151.9 394.0,151.7 395.0,151.4 396.0,151.2 397.0,151.0 398.0,150.7 399.0,150.5 400.0,150.3 401.0,150.1 402.0,149.8 403.0,149.6 404.0,149.4 405.0,149.2 406.0,149.0 407.0,148.8 408.0,148.5 409.0,148.3 410.0,148.1 411.0,147.9 412.0,147.7 413.0,147.5 414.0,147.3 415.0,147.1 416.0,146.8 417.0,146.6 418.0,146.4 419.0,146.2 420.0,146.0 421.0,145.8 422.0,145.6 423.0,145.4 424.0,145.2 425.0,145.0 426.0,144.8 427.0,144.6 428.0,144.4 429.0,144.2 430.0,144.0 431.0,143.8 432.0,143.7 433.0,143.5 434.0,143.3 435.0,143.1 436.0,142.9 437.0,142.7 438.0,142.5 439.0,142.3 440.0,142.1 441.0,141.9 442.0,141.8 443.0,141.6 444.0,141.4 445.0,141.2 446.0,141.0 447.0,140.9 448.0,140.7 449.0,140.5 450.0,140.3 451.0,140.1 452.0,140.0 453.0,139.8 454.0,139.6 455.0,139.4 456.0,139.3 457.0,139.1 458.0,138.9 459.0,138.7 460.0,138.6 461.0,138.4 462.0,138.2 463.0,138.0 464.0,137.9 465.0,137.7 466.0,137.5 467.0,137.4 468.0,137.2 469.0,137.0 470.0,136.9 471.0,136.7 472.0,136.5 473.0,136.4 474.0,136.2 475.0,136.1 476.0,135.9 477.0,135.7 478.0,135.6 479.0,135.4 480.0,135.2 481.0,135.1 482.0,134.9 483.0,134.8 484.0,134.6 485.0,134.5 486.0,134.3 487.0,134.1 488.0,134.0 489.0,133.8 490.0,133.7 491.0,133.5 492.0,133.4 493.0,133.2 494.0,133.1 495.0,132.9 496.0,132.8 497.0,132.6 498.0,132.5 499.0,132.3 500.0,132.2 501.0,132.0 502.0,131.9"/>
<circle class="fm-pt" cx="202.0" cy="149.0" r="4.5"/>
<circle class="fm-pt2" cx="277.0" cy="193.3" r="4.5"/>
<circle class="fm-pt" cx="277.0" cy="72.8" r="4.5"/>
<text class="fm-t" x="210.0" y="141.0" text-anchor="start">(0 ; 1)</text>
<text class="fm-t" x="283.0" y="211.3" text-anchor="start">(1 ; 0)</text>
<text class="fm-t fm-i" x="397.0" y="47.0" text-anchor="start">y = x</text>
<text class="fm-t fm-b" x="284.5" y="29.3" text-anchor="start">e<tspan dy="-6" font-size="11">x</tspan></text>
<text class="fm-t fm-b2" x="427.0" y="133.5" text-anchor="start">ln x</text>
</svg>
<figcaption>La courbe de ln est le symétrique de celle de exp par rapport à la droite y = x (pointillés) : les deux fonctions « se défont ».</figcaption>
</figure>

Sur la figure, la courbe de \(\ln\) est la **symétrique** de celle de \(\exp\) par rapport à la droite \(y = x\) : les deux fonctions s'annulent mutuellement.

\[
\ln(e^{x}) = x \quad (x \text{ quelconque}), \qquad e^{\ln x} = x \quad (x > 0).
\]

**Règles de calcul du logarithme** :

\[
\ln(ab) = \ln a + \ln b, \qquad \ln\!\left(\dfrac{a}{b}\right) = \ln a - \ln b, \qquad \ln(a^{n}) = n \ln a.
\]

> [!WARNING]
> **Piège classique.** \(\ln(a + b)\) n'est **pas** \(\ln a + \ln b\). Le logarithme transforme les **produits** en sommes, pas les sommes. Par exemple \(\ln(2 \times 3) = \ln 2 + \ln 3 \approx 1{,}79\), alors que \(\ln(2 + 3) = \ln 5 \approx 1{,}61\).

## 4. Résoudre une équation d'exposant

On applique la même idée : **le logarithme défait l'exponentielle, l'exponentielle défait le logarithme**.

| Équation | On applique | Solution |
|---|---|---|
| \(e^{u} = k\) (\(k > 0\)) | \(\ln\) des deux côtés | \(u = \ln k\) |
| \(\ln x = k\) | \(\exp\) des deux côtés | \(x = e^{k}\) |
| \(a^{x} = k\) (\(a > 0\), \(a \ne 1\), \(k > 0\)) | \(\ln\) des deux côtés | \(x = \dfrac{\ln k}{\ln a}\) |

**Exemple résolu.** Résoudre \(e^{0{,}2t} = 3\) et \(\ln x = 2\).

<details markdown="1">
<summary>Voir la solution</summary>

**Première équation.** On prend le logarithme : \(0{,}2t = \ln 3\), donc \(t = \dfrac{\ln 3}{0{,}2} = 5\ln 3 \approx 5{,}49\).

**Seconde équation.** \(\ln x = 2\) signifie \(x = e^{2} \approx 7{,}39\).

**Contrôle :** \(e^{0{,}2 \times 5{,}49} = e^{1{,}098} \approx 3\) ✔.

</details>

## 5. Les seuils : « au bout de combien de temps dépasse-t-on... »

C'est la question la plus fréquente à l'épreuve. On cherche **le plus petit entier** \(n\) tel qu'une suite géométrique dépasse un seuil.

**Méthode en 4 étapes.**

1. Écrire l'**inéquation** : par exemple \(1000 \times 1{,}05^{\,n} \ge 1500\).
2. **Isoler** la puissance : \(1{,}05^{\,n} \ge 1{,}5\).
3. Prendre le **logarithme** des deux côtés. Comme \(\ln\) est croissante, le sens de l'inégalité est conservé : \(n \ln 1{,}05 \ge \ln 1{,}5\). On divise par \(\ln 1{,}05\), qui est **positif** (car \(1{,}05 > 1\)), donc le sens reste le même : \(n \ge \dfrac{\ln 1{,}5}{\ln 1{,}05} \approx 8{,}31\).
4. **Conclure avec un entier** : le plus petit entier supérieur ou égal à \(8{,}31\) est \(9\).

> [!WARNING]
> **Attention au sens.** Quand on divise par un **logarithme négatif**, l'inégalité change de sens. Cela arrive pour une base \(a\) **entre 0 et 1** (décroissance) : \(\ln a < 0\). Exemple : \(0{,}85^{\,n} \le 0{,}5\) donne \(n \ge \dfrac{\ln 0{,}5}{\ln 0{,}85}\), car on a divisé par \(\ln 0{,}85 < 0\).

**Contrôle systématique.** Calcule la valeur à \(n = 8\) et à \(n = 9\) pour vérifier : \(1{,}05^{8} \approx 1{,}477\) (trop petit) et \(1{,}05^{9} \approx 1{,}551\) (assez grand). Le seuil est bien atteint la **9e année**.

**Exemple résolu.** Au bout de combien d'années le stockage double-t-il (taux de 5 % par an) ?

<details markdown="1">
<summary>Voir la solution</summary>

On cherche \(n\) entier avec \(1{,}05^{\,n} \ge 2\), donc \(n \ge \dfrac{\ln 2}{\ln 1{,}05} \approx 14{,}21\).

Le plus petit entier convenable est **15 ans**. Contrôle : \(1{,}05^{14} \approx 1{,}980 < 2\) et \(1{,}05^{15} \approx 2{,}079 \ge 2\).

</details>

**Variante avec Python.** Une boucle donne le même seuil sans logarithme, et sert de contrôle :

```python
n = 0
valeur = 1000
while valeur < 1500:
    valeur = valeur * 1.05
    n = n + 1
print(n)   # 9
```

## 6. Interpréter : quand le résultat n'est pas « propre »

Les valeurs \(8{,}31\) ou \(14{,}21\) ne sont pas des années entières : on les **arrondit au plus petit entier supérieur**, car le seuil est atteint **à la fin** de la période concernée. L'arrondi dépend du contexte : pour « au bout de combien d'années **au plus** reste-t-il moins de... », on arrondit selon le sens de l'inégalité, toujours en **vérifiant** avec les deux entiers voisins.

## 7. À retenir

> [!NOTE]
> - Évolution de \(t\) % : coefficient multiplicateur \(a = 1 + \dfrac{t}{100}\) ; après \(n\) périodes, on multiplie par \(a^{n}\).
> - \(a^{x}\) est croissante si \(a > 1\), décroissante si \(0 < a < 1\), toujours **strictement positive**.
> - \(\ln x\) est l'exposant qui donne \(x\) en base \(e\) ; \(\ln\) n'existe que pour \(x > 0\).
> - \(\ln(ab) = \ln a + \ln b\), \(\ln(a^{n}) = n\ln a\), mais \(\ln(a+b) \ne \ln a + \ln b\).
> - Résoudre \(a^{n} \ge c\) : \(n \ge \dfrac{\ln c}{\ln a}\) (si \(a > 1\)), puis **arrondir à l'entier** et **contrôler**.

## 8. Teste-toi

**Question 1.** Un trafic de 800 Go par mois augmente de 10 % par mois. Quel trafic au bout de 3 mois ?

**Question 2.** Simplifier \(\ln 8 - \ln 2\).

**Question 3.** Au bout de combien de mois le trafic de départ de 3 To, avec \(+10\) % par mois, dépasse-t-il 10 To ?

**Question 4.** Résoudre \(e^{x} = 0{,}5\).

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(800 \times 1{,}1^{3} = 800 \times 1{,}331 = 1\,064{,}8\) Go.
2. \(\ln 8 - \ln 2 = \ln\dfrac{8}{2} = \ln 4 \approx 1{,}386\).
3. \(3 \times 1{,}1^{\,n} \ge 10\) donne \(n \ge \dfrac{\ln(10/3)}{\ln 1{,}1} \approx 12{,}63\) : **13 mois**. Contrôle : \(3 \times 1{,}1^{12} \approx 9{,}41\) et \(3 \times 1{,}1^{13} \approx 10{,}36\).
4. \(x = \ln 0{,}5 \approx -0{,}693\).

</details>

**Pour continuer :** le [cours 3](04-racine-et-resolution-approchee.md), puis les [exercices du module](03-exercices.md) et le [module M2 sur la dérivée](../M2-derivees-integrales/01-derivee-et-variations.md).

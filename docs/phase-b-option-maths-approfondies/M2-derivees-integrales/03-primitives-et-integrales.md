# Cours 3 – Primitives et intégrales

*BTS SIO SISR 2e année – Option mathématiques approfondies – M2, troisième partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : expliquer l'intégrale comme **cumul** (aire sous une courbe) ; **vérifier** qu'une fonction est une primitive en la dérivant ; calculer une intégrale avec une primitive ; calculer et interpréter une **valeur moyenne**.
>
> **Programme.** On ne calcule **pas** une primitive par une lecture « à l'envers » du tableau des dérivées : on **justifie** une primitive proposée en la **dérivant**, ou on la demande à la calculatrice formelle. Les fonctions périodiques ne sont pas au programme.

## 1. Pour démarrer : cumuler une grandeur

Un lien transfère des données à un débit **constant** de 2 Go par heure. En 3 heures, la quantité transférée est \(2 \times 3 = 6\) Go. Sur un graphique du débit en fonction du temps, c'est l'**aire d'un rectangle** de largeur 3 et de hauteur 2.

Mais si le débit **varie** (par exemple \(d(t) = e^{-t/2}\) Go par heure, qui décroît), la quantité totale est toujours une **aire** : celle de la zone comprise entre la courbe du débit et l'axe du temps. Cette aire s'appelle l'**intégrale** du débit.

<figure class="fig-math">
<svg viewBox="0 0 520 320" role="img" aria-label="Aire sous x e^(-x/2)">
<polygon class="fm-fill" points="52.0,282.0 52.0,282.0 53.9,272.3 55.8,262.9 57.6,253.9 59.5,245.1 61.4,236.7 63.2,228.5 65.1,220.6 67.0,213.0 68.9,205.7 70.8,198.6 72.6,191.8 74.5,185.2 76.4,178.9 78.2,172.8 80.1,166.9 82.0,161.3 83.9,155.8 85.8,150.6 87.6,145.6 89.5,140.8 91.4,136.2 93.2,131.8 95.1,127.6 97.0,123.5 98.9,119.6 100.8,115.9 102.6,112.4 104.5,109.0 106.4,105.8 108.2,102.7 110.1,99.8 112.0,97.1 113.9,94.4 115.8,91.9 117.6,89.6 119.5,87.4 121.4,85.3 123.2,83.3 125.1,81.4 127.0,79.7 128.9,78.0 130.8,76.5 132.6,75.1 134.5,73.8 136.4,72.6 138.2,71.5 140.1,70.4 142.0,69.5 143.9,68.7 145.8,67.9 147.6,67.2 149.5,66.7 151.4,66.1 153.2,65.7 155.1,65.3 157.0,65.0 158.9,64.8 160.8,64.7 162.6,64.6 164.5,64.5 166.4,64.6 168.2,64.7 170.1,64.8 172.0,65.0 173.9,65.3 175.8,65.6 177.6,65.9 179.5,66.3 181.4,66.8 183.2,67.2 185.1,67.8 187.0,68.4 188.9,69.0 190.8,69.6 192.6,70.3 194.5,71.0 196.4,71.8 198.2,72.6 200.1,73.4 202.0,74.2 203.9,75.1 205.8,76.0 207.6,77.0 209.5,77.9 211.4,78.9 213.2,79.9 215.1,80.9 217.0,82.0 218.9,83.1 220.8,84.2 222.6,85.3 224.5,86.4 226.4,87.5 228.2,88.7 230.1,89.9 232.0,91.1 233.9,92.3 235.8,93.5 237.6,94.7 239.5,95.9 241.4,97.2 243.2,98.4 245.1,99.7 247.0,101.0 248.9,102.2 250.8,103.5 252.6,104.8 254.5,106.1 256.4,107.4 258.2,108.7 260.1,110.1 262.0,111.4 263.9,112.7 265.8,114.0 267.6,115.3 269.5,116.7 271.4,118.0 273.2,119.3 275.1,120.7 277.0,122.0 277.0,282.0"/>
<line class="fm-grid" x1="52" y1="282.0" x2="502" y2="282.0"/>
<text class="fm-t" x="46" y="286.0" text-anchor="end">0</text>
<line class="fm-grid" x1="52" y1="222.9" x2="502" y2="222.9"/>
<text class="fm-t" x="46" y="226.9" text-anchor="end">0,2</text>
<line class="fm-grid" x1="52" y1="163.8" x2="502" y2="163.8"/>
<text class="fm-t" x="46" y="167.8" text-anchor="end">0,4</text>
<line class="fm-grid" x1="52" y1="104.7" x2="502" y2="104.7"/>
<text class="fm-t" x="46" y="108.7" text-anchor="end">0,6</text>
<line class="fm-grid" x1="52" y1="45.6" x2="502" y2="45.6"/>
<text class="fm-t" x="46" y="49.6" text-anchor="end">0,8</text>
<line class="fm-grid" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t" x="52.0" y="298" text-anchor="middle">0</text>
<line class="fm-grid" x1="164.5" y1="16" x2="164.5" y2="282"/>
<text class="fm-t" x="164.5" y="298" text-anchor="middle">2</text>
<line class="fm-grid" x1="277.0" y1="16" x2="277.0" y2="282"/>
<text class="fm-t" x="277.0" y="298" text-anchor="middle">4</text>
<line class="fm-grid" x1="389.5" y1="16" x2="389.5" y2="282"/>
<text class="fm-t" x="389.5" y="298" text-anchor="middle">6</text>
<line class="fm-grid" x1="502.0" y1="16" x2="502.0" y2="282"/>
<text class="fm-t" x="502.0" y="298" text-anchor="middle">8</text>
<line class="fm-axis" x1="52" y1="282.0" x2="502" y2="282.0"/>
<line class="fm-axis" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t fm-i" x="502" y="314" text-anchor="end">x</text>
<text class="fm-t fm-i" x="56" y="24">f(x)</text>
<polyline class="fm-curve" points="52.0,282.0 53.5,274.2 55.0,266.7 56.5,259.3 58.0,252.1 59.5,245.1 61.0,238.3 62.5,231.7 64.0,225.3 65.5,219.1 67.0,213.0 68.5,207.1 70.0,201.4 71.5,195.8 73.0,190.4 74.5,185.2 76.0,180.1 77.5,175.2 79.0,170.4 80.5,165.8 82.0,161.3 83.5,156.9 85.0,152.7 86.5,148.6 88.0,144.6 89.5,140.8 91.0,137.1 92.5,133.5 94.0,130.1 95.5,126.7 97.0,123.5 98.5,120.4 100.0,117.4 101.5,114.5 103.0,111.7 104.5,109.0 106.0,106.4 107.5,103.9 109.0,101.6 110.5,99.3 112.0,97.1 113.5,94.9 115.0,92.9 116.5,91.0 118.0,89.1 119.5,87.4 121.0,85.7 122.5,84.1 124.0,82.5 125.5,81.1 127.0,79.7 128.5,78.4 130.0,77.1 131.5,75.9 133.0,74.8 134.5,73.8 136.0,72.8 137.5,71.9 139.0,71.0 140.5,70.3 142.0,69.5 143.5,68.8 145.0,68.2 146.5,67.6 148.0,67.1 149.5,66.7 151.0,66.2 152.5,65.9 154.0,65.6 155.5,65.3 157.0,65.0 158.5,64.9 160.0,64.7 161.5,64.6 163.0,64.6 164.5,64.5 166.0,64.6 167.5,64.6 169.0,64.7 170.5,64.8 172.0,65.0 173.5,65.2 175.0,65.4 176.5,65.7 178.0,66.0 179.5,66.3 181.0,66.7 182.5,67.0 184.0,67.5 185.5,67.9 187.0,68.4 188.5,68.8 190.0,69.4 191.5,69.9 193.0,70.4 194.5,71.0 196.0,71.6 197.5,72.3 199.0,72.9 200.5,73.6 202.0,74.2 203.5,74.9 205.0,75.7 206.5,76.4 208.0,77.2 209.5,77.9 211.0,78.7 212.5,79.5 214.0,80.3 215.5,81.2 217.0,82.0 218.5,82.9 220.0,83.7 221.5,84.6 223.0,85.5 224.5,86.4 226.0,87.3 227.5,88.2 229.0,89.2 230.5,90.1 232.0,91.1 233.5,92.0 235.0,93.0 236.5,94.0 238.0,94.9 239.5,95.9 241.0,96.9 242.5,97.9 244.0,98.9 245.5,99.9 247.0,101.0 248.5,102.0 250.0,103.0 251.5,104.0 253.0,105.1 254.5,106.1 256.0,107.2 257.5,108.2 259.0,109.3 260.5,110.3 262.0,111.4 263.5,112.4 265.0,113.5 266.5,114.5 268.0,115.6 269.5,116.7 271.0,117.7 272.5,118.8 274.0,119.9 275.5,120.9 277.0,122.0 278.5,123.1 280.0,124.1 281.5,125.2 283.0,126.3 284.5,127.3 286.0,128.4 287.5,129.5 289.0,130.5 290.5,131.6 292.0,132.6 293.5,133.7 295.0,134.8 296.5,135.8 298.0,136.9 299.5,137.9 301.0,139.0 302.5,140.0 304.0,141.0 305.5,142.1 307.0,143.1 308.5,144.1 310.0,145.2 311.5,146.2 313.0,147.2 314.5,148.3 316.0,149.3 317.5,150.3 319.0,151.3 320.5,152.3 322.0,153.3 323.5,154.3 325.0,155.3 326.5,156.3 328.0,157.3 329.5,158.3 331.0,159.2 332.5,160.2 334.0,161.2 335.5,162.1 337.0,163.1 338.5,164.1 340.0,165.0 341.5,166.0 343.0,166.9 344.5,167.8 346.0,168.8 347.5,169.7 349.0,170.6 350.5,171.6 352.0,172.5 353.5,173.4 355.0,174.3 356.5,175.2 358.0,176.1 359.5,177.0 361.0,177.9 362.5,178.7 364.0,179.6 365.5,180.5 367.0,181.4 368.5,182.2 370.0,183.1 371.5,183.9 373.0,184.8 374.5,185.6 376.0,186.4 377.5,187.3 379.0,188.1 380.5,188.9 382.0,189.7 383.5,190.5 385.0,191.3 386.5,192.1 388.0,192.9 389.5,193.7 391.0,194.5 392.5,195.3 394.0,196.0 395.5,196.8 397.0,197.6 398.5,198.3 400.0,199.1 401.5,199.8 403.0,200.6 404.5,201.3 406.0,202.0 407.5,202.8 409.0,203.5 410.5,204.2 412.0,204.9 413.5,205.6 415.0,206.3 416.5,207.0 418.0,207.7 419.5,208.4 421.0,209.0 422.5,209.7 424.0,210.4 425.5,211.1 427.0,211.7 428.5,212.4 430.0,213.0 431.5,213.7 433.0,214.3 434.5,214.9 436.0,215.6 437.5,216.2 439.0,216.8 440.5,217.4 442.0,218.0 443.5,218.6 445.0,219.2 446.5,219.8 448.0,220.4 449.5,221.0 451.0,221.6 452.5,222.2 454.0,222.7 455.5,223.3 457.0,223.9 458.5,224.4 460.0,225.0 461.5,225.5 463.0,226.1 464.5,226.6 466.0,227.1 467.5,227.7 469.0,228.2 470.5,228.7 472.0,229.2 473.5,229.7 475.0,230.3 476.5,230.8 478.0,231.3 479.5,231.8 481.0,232.2 482.5,232.7 484.0,233.2 485.5,233.7 487.0,234.2 488.5,234.6 490.0,235.1 491.5,235.6 493.0,236.0 494.5,236.5 496.0,236.9 497.5,237.4 499.0,237.8 500.5,238.3 502.0,238.7"/>
<line class="fm-dash" x1="277.0" y1="282.0" x2="277.0" y2="122.0"/>
<circle class="fm-pt" cx="164.5" cy="64.5" r="4.5"/>
<text class="fm-t" x="174.5" y="56.5" text-anchor="start">maximum (2 ; 0,74)</text>
<text class="fm-t fm-b" x="164.5" y="237.7" text-anchor="middle">aire = intégrale de 0 à 4</text>
</svg>
<figcaption>L’intégrale de 0 à 4 est l’aire de la zone colorée, entre la courbe et l’axe des abscisses.</figcaption>
</figure>

## 2. Primitive : l'opération « inverse » de la dérivation

**Définition.** Une **primitive** de \(f\) est une fonction \(F\) dont la dérivée est \(f\) : \(F' = f\).

Une fonction qui a une primitive en a **une infinité** : si \(F\) est une primitive, \(F + k\) (avec \(k\) constante) en est une aussi, car la dérivée d'une constante est nulle.

**Comment on procède ici.** On ne cherche pas la primitive par une recette de lecture inverse : l'énoncé (ou la calculatrice formelle) la **propose**, et on la **justifie en dérivant**.

**Exemple résolu.** Montrer que \(F(x) = x\,e^{x} - e^{x}\) est une primitive de \(f(x) = x\,e^{x}\).

<details markdown="1">
<summary>Voir la solution</summary>

On dérive \(F\). Pour \(x\,e^{x}\), la règle du produit donne \(e^{x} + x\,e^{x}\) ; pour \(-e^{x}\), on obtient \(-e^{x}\). Donc

\[
F'(x) = e^{x} + x\,e^{x} - e^{x} = x\,e^{x} = f(x).
\]

\(F\) est bien une primitive de \(f\). ✔

</details>

> [!TIP]
> **Les primitives simples à connaître.** Elles se vérifient toutes en dérivant : une primitive de \(x^{n}\) est \(\dfrac{x^{n+1}}{n+1}\) (pour \(n \ne -1\)) ; de \(e^{x}\) est \(e^{x}\) ; de \(e^{kx}\) est \(\dfrac{1}{k}e^{kx}\) ; de \(\dfrac{1}{x}\) est \(\ln x\) (pour \(x > 0\)). Ne les « devine » pas : **dérive pour contrôler**.

## 3. L'intégrale : aire et cumul

**Définition.** Si \(F\) est une primitive de \(f\) sur \([a\,;\,b]\), l'**intégrale** de \(f\) de \(a\) à \(b\) est

\[
\int_{a}^{b} f(x)\,dx = F(b) - F(a) = \big[F(x)\big]_{a}^{b}.
\]

Le résultat ne dépend pas de la primitive choisie (la constante \(k\) disparaît dans la soustraction).

**Ce que représente l'intégrale.**

- Si \(f \ge 0\) sur \([a\,;\,b]\), c'est l'**aire** sous la courbe entre \(a\) et \(b\) ;
- c'est surtout un **cumul** : si \(f\) est un débit, l'intégrale est le **volume total** écoulé ; si \(f\) est un coût par unité (coût marginal), c'est le **coût total** ajouté.

**Propriétés utiles.**

| Propriété | Écriture |
|---|---|
| Linéarité | \(\displaystyle\int_a^b (f + g) = \int_a^b f + \int_a^b g\) et \(\displaystyle\int_a^b k f = k \int_a^b f\) |
| Relation de Chasles | \(\displaystyle\int_a^c f = \int_a^b f + \int_b^c f\) |
| Positivité | si \(f \ge 0\) sur \([a\,;\,b]\), alors \(\displaystyle\int_a^b f \ge 0\) |

**Exemple résolu 1.** Calculer \(\displaystyle\int_{0}^{2} (3x^2 - 4x + 1)\,dx\).

<details markdown="1">
<summary>Voir la solution</summary>

On propose \(F(x) = x^3 - 2x^2 + x\). **Vérification :** \(F'(x) = 3x^2 - 4x + 1\) ✔. Donc

\[
\int_{0}^{2} (3x^2 - 4x + 1)\,dx = F(2) - F(0) = (8 - 8 + 2) - 0 = 2.
\]

</details>

**Exemple résolu 2 : un débit qui décroît.** Le débit d'un transfert est \(d(t) = e^{-t/2}\) (en Go par heure). Quelle quantité est transférée de \(t = 0\) à \(t = 4\) ?

<details markdown="1">
<summary>Voir la solution</summary>

Primitive proposée : \(D(t) = -2e^{-t/2}\). **Vérification :** \(D'(t) = -2 \times \left(-\dfrac{1}{2}\right)e^{-t/2} = e^{-t/2}\) ✔.

\[
\int_{0}^{4} e^{-t/2}\,dt = D(4) - D(0) = -2e^{-2} + 2 = 2 - 2e^{-2} \approx 1{,}73.
\]

**Interprétation.** Il est transféré environ **1,73 Go** en 4 heures. Contrôle d'ordre de grandeur : le débit passe de 1 Go/h à 0,14 Go/h en 4 heures, donc le cumul doit être entre 0,14 × 4 et 1 × 4, soit entre 0,6 et 4 : 1,73 est plausible.

</details>

## 4. La valeur moyenne

**Définition.** La **valeur moyenne** de \(f\) sur \([a\,;\,b]\) est

\[
\mu = \dfrac{1}{b - a}\int_{a}^{b} f(x)\,dx.
\]

C'est la hauteur du **rectangle** de même base \([a\,;\,b]\) et de même aire que la zone sous la courbe : la valeur constante qui donnerait le même cumul.

**Exemple résolu.** Calculer la valeur moyenne de \(f(x) = x^2 + 1\) sur \([0\,;\,3]\).

<details markdown="1">
<summary>Voir la solution</summary>

Primitive proposée : \(F(x) = \dfrac{x^3}{3} + x\). **Vérification :** \(F'(x) = x^2 + 1\) ✔.

\(\displaystyle\int_0^3 (x^2 + 1)\,dx = F(3) - F(0) = (9 + 3) - 0 = 12\). La valeur moyenne est \(\mu = \dfrac{12}{3} = 4\).

**Interprétation.** Si \(f\) représente une charge, elle vaut en moyenne 4 sur l'intervalle (elle part de 1 et finit à 10).

</details>

## 5. Vérifier une intégrale avec Python

Une somme de petits rectangles approche l'aire :

```python
from math import exp

def integrale(f, a, b, n=100000):
    h = (b - a) / n
    return sum(f(a + (i + 0.5) * h) for i in range(n)) * h

print(integrale(lambda t: exp(-t / 2), 0, 4))   # 1.7293...
```

On retrouve \(2 - 2e^{-2} \approx 1{,}7293\). Ce calcul numérique sert de **contrôle** du calcul exact.

## 6. À retenir

> [!NOTE]
> - Une primitive \(F\) de \(f\) vérifie \(F' = f\). On la **justifie par dérivation**.
> - \(\displaystyle\int_a^b f(x)\,dx = F(b) - F(a)\) : c'est l'**aire** sous la courbe (si \(f \ge 0\)) et surtout un **cumul**.
> - Valeur moyenne : \(\dfrac{1}{b-a}\displaystyle\int_a^b f(x)\,dx\).
> - Toujours donner l'**unité** et **interpréter** : volume transféré, coût total, charge moyenne.

## 7. Teste-toi

**Question 1.** Montrer que \(F(x) = \dfrac{x^3}{3}\) est une primitive de \(x^2\), puis calculer \(\displaystyle\int_1^3 x^2\,dx\).

**Question 2.** Calculer \(\displaystyle\int_0^1 e^{x}\,dx\).

**Question 3.** Une consommation instantanée est \(p(t) = 2t\) (en kW) entre \(t = 0\) et \(t = 5\) heures. Quelle énergie cumulée (en kWh) ? Quelle puissance moyenne ?

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(F'(x) = \dfrac{3x^2}{3} = x^2\) ✔. \(\displaystyle\int_1^3 x^2\,dx = F(3) - F(1) = 9 - \dfrac{1}{3} = \dfrac{26}{3} \approx 8{,}67\).
2. \(\displaystyle\int_0^1 e^{x}\,dx = e^{1} - e^{0} = e - 1 \approx 1{,}72\).
3. Primitive \(P(t) = t^2\) (dérivée \(2t\)). Énergie : \(P(5) - P(0) = 25\) kWh. Puissance moyenne : \(\dfrac{25}{5} = 5\) kW (c'est la moyenne de 0 et 10, car la puissance est affine).

</details>

**Pour continuer :** les [exercices du module](04-exercices.md), puis le [module M3 sur la statistique](../M3-statistique/01-indicateurs-de-position-et-de-dispersion.md).

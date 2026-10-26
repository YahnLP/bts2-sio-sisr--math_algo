# Cours 2 – Lois de Poisson et normale

*BTS SIO SISR 2e année – Option mathématiques approfondies – M4, seconde partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : reconnaître quand utiliser la **loi de Poisson** (événements rares) et la **loi normale** (mesures continues) ; calculer des probabilités avec la calculatrice ; **retrouver un seuil** (par exemple « 95 % des cas sous quel temps ? ») ; **choisir la bonne loi** selon la situation.
>
> **Prérequis.** Le [cours 1](01-variable-aleatoire-et-loi-binomiale.md).

## 1. Pour démarrer : deux situations, deux modèles

**Situation A.** Un service reçoit en moyenne 2 incidents par jour. Quelle est la probabilité qu'un jour donné il n'y en ait aucun ? Au moins 5 ? Ici, on **compte des événements** qui surviennent au hasard dans le temps.

**Situation B.** Le temps de réponse d'une application est de 100 ms en moyenne, avec une dispersion de 8 ms. Quelle est la probabilité qu'il dépasse 115 ms ? Ici, on **mesure une grandeur** qui peut prendre n'importe quelle valeur dans un intervalle.

La situation A relève de la **loi de Poisson**, la situation B de la **loi normale**.

## 2. La loi de Poisson : compter des événements rares

**Quand l'utiliser.** On compte le nombre d'événements (pannes, requêtes rares, incidents) qui se produisent **au hasard**, **indépendamment** les uns des autres, à un **rythme moyen constant** sur une période donnée.

**La loi.** Si le nombre moyen d'événements est \(\lambda\) (« lambda »), la variable \(X\) qui compte les événements suit la loi de Poisson \(\mathcal{P}(\lambda)\) :

\[
P(X = k) = e^{-\lambda}\,\dfrac{\lambda^{k}}{k!}, \qquad E(X) = V(X) = \lambda.
\]

Le symbole \(k!\) (« factorielle \(k\) ») vaut \(1 \times 2 \times \dots \times k\), avec \(0! = 1\). Une particularité : **l'espérance et la variance sont égales** à \(\lambda\).

**Exemple.** Avec \(\lambda = 2\) incident par jour :

| \(k\) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| \(P(X = k)\) | 0,1353 | 0,2707 | 0,2707 | 0,1804 | 0,0902 | 0,0361 |

<figure class="fig-math">
<svg viewBox="0 0 520 320" role="img" aria-label="Loi de Poisson P(2)">
<line class="fm-grid" x1="52" y1="282.0" x2="502" y2="282.0"/>
<text class="fm-t" x="46" y="286.0" text-anchor="end">0,0</text>
<line class="fm-grid" x1="52" y1="193.3" x2="502" y2="193.3"/>
<text class="fm-t" x="46" y="197.3" text-anchor="end">0,1</text>
<line class="fm-grid" x1="52" y1="104.7" x2="502" y2="104.7"/>
<text class="fm-t" x="46" y="108.7" text-anchor="end">0,2</text>
<line class="fm-grid" x1="52" y1="16.0" x2="502" y2="16.0"/>
<text class="fm-t" x="46" y="20.0" text-anchor="end">0,3</text>
<line class="fm-grid" x1="81.3" y1="16" x2="81.3" y2="282"/>
<text class="fm-t" x="81.3" y="298" text-anchor="middle">0</text>
<line class="fm-grid" x1="130.3" y1="16" x2="130.3" y2="282"/>
<text class="fm-t" x="130.3" y="298" text-anchor="middle">1</text>
<line class="fm-grid" x1="179.2" y1="16" x2="179.2" y2="282"/>
<text class="fm-t" x="179.2" y="298" text-anchor="middle">2</text>
<line class="fm-grid" x1="228.1" y1="16" x2="228.1" y2="282"/>
<text class="fm-t" x="228.1" y="298" text-anchor="middle">3</text>
<line class="fm-grid" x1="277.0" y1="16" x2="277.0" y2="282"/>
<text class="fm-t" x="277.0" y="298" text-anchor="middle">4</text>
<line class="fm-grid" x1="325.9" y1="16" x2="325.9" y2="282"/>
<text class="fm-t" x="325.9" y="298" text-anchor="middle">5</text>
<line class="fm-grid" x1="374.8" y1="16" x2="374.8" y2="282"/>
<text class="fm-t" x="374.8" y="298" text-anchor="middle">6</text>
<line class="fm-grid" x1="423.7" y1="16" x2="423.7" y2="282"/>
<text class="fm-t" x="423.7" y="298" text-anchor="middle">7</text>
<line class="fm-grid" x1="472.7" y1="16" x2="472.7" y2="282"/>
<text class="fm-t" x="472.7" y="298" text-anchor="middle">8</text>
<line class="fm-axis" x1="52" y1="282.0" x2="502" y2="282.0"/>
<line class="fm-axis" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t fm-i" x="502" y="314" text-anchor="end">k (incidents dans la journée)</text>
<text class="fm-t fm-i" x="56" y="24">probabilité</text>
<rect class="fm-bar" x="64.2" y="162.0" width="34.2" height="120.0"/>
<text class="fm-t" x="81.3" y="157.0" text-anchor="middle">0,135</text>
<rect class="fm-bar" x="113.1" y="42.0" width="34.2" height="240.0"/>
<text class="fm-t" x="130.3" y="37.0" text-anchor="middle">0,271</text>
<rect class="fm-bar" x="162.1" y="42.0" width="34.2" height="240.0"/>
<text class="fm-t" x="179.2" y="37.0" text-anchor="middle">0,271</text>
<rect class="fm-bar" x="211.0" y="122.0" width="34.2" height="160.0"/>
<text class="fm-t" x="228.1" y="117.0" text-anchor="middle">0,180</text>
<rect class="fm-bar" x="259.9" y="202.0" width="34.2" height="80.0"/>
<text class="fm-t" x="277.0" y="197.0" text-anchor="middle">0,090</text>
<rect class="fm-bar" x="308.8" y="250.0" width="34.2" height="32.0"/>
<text class="fm-t" x="325.9" y="245.0" text-anchor="middle">0,036</text>
<rect class="fm-bar" x="357.7" y="271.3" width="34.2" height="10.7"/>
<text class="fm-t" x="374.8" y="266.3" text-anchor="middle">0,012</text>
<rect class="fm-bar" x="406.6" y="279.0" width="34.2" height="3.0"/>
<text class="fm-t" x="423.7" y="274.0" text-anchor="middle">0,003</text>
<rect class="fm-bar" x="455.5" y="281.2" width="34.2" height="0.8"/>
<text class="fm-t" x="472.7" y="276.2" text-anchor="middle">0,001</text>
</svg>
<figcaption>Loi de Poisson de paramètre 2 : la valeur la plus probable est 1 ou 2 incidents par jour, mais 5 ou plus reste possible (environ 5 %).</figcaption>
</figure>

**Exemple résolu.** Pour \(\lambda = 2\), calculer \(P(X = 0)\), \(P(X = 3)\) et \(P(X \ge 5)\). À quelle fréquence atteint-on au moins 5 incidents par jour ?

<details markdown="1">
<summary>Voir la solution</summary>

\(P(X = 0) = e^{-2} \approx 0{,}1353\). \(P(X = 3) = e^{-2}\dfrac{2^{3}}{3!} = e^{-2} \times \dfrac{8}{6} \approx 0{,}1804\).

Pour \(P(X \ge 5)\), on utilise l'événement contraire : \(P(X \ge 5) = 1 - P(X \le 4) \approx 1 - 0{,}9473 = 0{,}0527\).

**Interprétation.** Environ **5,3 %** des jours, soit à peu près **un jour sur 19** (environ 19 jours par an) : une permanence renforcée déclenchée à partir de 5 incidents est rare, mais pas exceptionnelle.

</details>

**Lien avec la loi binomiale.** Quand \(n\) est **grand** et \(p\) **petit**, \(\mathcal{B}(n\,;\,p)\) est très proche de \(\mathcal{P}(\lambda)\) avec \(\lambda = np\). Par exemple, 200 transmissions échouant chacune avec la probabilité \(0{,}01\) : \(\lambda = 2\), et \(P(X = 0)\) vaut \(0{,}1340\) (binomiale) contre \(0{,}1353\) (Poisson). La loi de Poisson est plus simple à manier.

## 3. La loi normale : la « cloche »

**Variable continue.** Un temps de réponse peut valoir 100 ms, 100,3 ms, 100,3257 ms... : il prend **toutes les valeurs** d'un intervalle. On ne peut plus lister des probabilités ponctuelles : la probabilité d'une valeur **exacte** est nulle, et on calcule des probabilités **d'intervalles** : \(P(X \le 105)\), \(P(90 \le X \le 110)\).

**La densité.** Une probabilité d'intervalle est une **aire sous une courbe**, la **courbe de densité** (comme l'intégrale du module M2 : le cumul d'une quantité).

**La loi normale** \(\mathcal{N}(m\,;\,\sigma)\) a une courbe de densité en **cloche**, symétrique autour de \(m\) (la moyenne), plus ou moins étalée selon \(\sigma\) (l'écart type).

<figure class="fig-math">
<svg viewBox="0 0 520 320" role="img" aria-label="Loi normale N(100;8)">
<polygon class="fm-fill" points="212.7,282.0 212.7,138.3 213.8,135.9 214.9,133.5 215.9,131.2 217.0,128.8 218.1,126.4 219.1,124.0 220.2,121.6 221.3,119.3 222.4,116.9 223.4,114.6 224.5,112.3 225.6,110.0 226.6,107.7 227.7,105.4 228.8,103.2 229.9,101.0 230.9,98.8 232.0,96.6 233.1,94.4 234.1,92.3 235.2,90.2 236.3,88.2 237.4,86.1 238.4,84.1 239.5,82.2 240.6,80.3 241.6,78.4 242.7,76.5 243.8,74.7 244.9,73.0 245.9,71.2 247.0,69.6 248.1,67.9 249.1,66.4 250.2,64.8 251.3,63.3 252.4,61.9 253.4,60.5 254.5,59.2 255.6,57.9 256.6,56.7 257.7,55.6 258.8,54.4 259.9,53.4 260.9,52.4 262.0,51.5 263.1,50.6 264.1,49.8 265.2,49.1 266.3,48.4 267.4,47.8 268.4,47.2 269.5,46.7 270.6,46.3 271.6,45.9 272.7,45.7 273.8,45.4 274.9,45.3 275.9,45.2 277.0,45.1 278.1,45.2 279.1,45.3 280.2,45.4 281.3,45.7 282.4,45.9 283.4,46.3 284.5,46.7 285.6,47.2 286.6,47.8 287.7,48.4 288.8,49.1 289.9,49.8 290.9,50.6 292.0,51.5 293.1,52.4 294.1,53.4 295.2,54.4 296.3,55.6 297.4,56.7 298.4,57.9 299.5,59.2 300.6,60.5 301.6,61.9 302.7,63.3 303.8,64.8 304.9,66.4 305.9,67.9 307.0,69.6 308.1,71.2 309.1,73.0 310.2,74.7 311.3,76.5 312.4,78.4 313.4,80.3 314.5,82.2 315.6,84.1 316.6,86.1 317.7,88.2 318.8,90.2 319.9,92.3 320.9,94.4 322.0,96.6 323.1,98.8 324.1,101.0 325.2,103.2 326.3,105.4 327.4,107.7 328.4,110.0 329.5,112.3 330.6,114.6 331.6,116.9 332.7,119.3 333.8,121.6 334.9,124.0 335.9,126.4 337.0,128.8 338.1,131.2 339.1,133.5 340.2,135.9 341.3,138.3 341.3,282.0"/>
<polygon class="fm-fill2" points="148.4,282.0 148.4,249.9 150.6,247.8 152.7,245.5 154.9,243.0 157.0,240.5 159.1,237.9 161.3,235.1 163.4,232.3 165.6,229.3 167.7,226.2 169.9,222.9 172.0,219.6 174.1,216.1 176.3,212.6 178.4,208.9 180.6,205.1 182.7,201.2 184.9,197.2 187.0,193.1 189.1,188.9 191.3,184.6 193.4,180.2 195.6,175.8 197.7,171.3 199.9,166.7 202.0,162.1 204.1,157.4 206.3,152.7 208.4,147.9 210.6,143.1 212.7,138.3 214.9,133.5 217.0,128.8 219.1,124.0 221.3,119.3 223.4,114.6 225.6,110.0 227.7,105.4 229.9,101.0 232.0,96.6 234.1,92.3 236.3,88.2 238.4,84.1 240.6,80.3 242.7,76.5 244.9,73.0 247.0,69.6 249.1,66.4 251.3,63.3 253.4,60.5 255.6,57.9 257.7,55.6 259.9,53.4 262.0,51.5 264.1,49.8 266.3,48.4 268.4,47.2 270.6,46.3 272.7,45.7 274.9,45.3 277.0,45.1 279.1,45.3 281.3,45.7 283.4,46.3 285.6,47.2 287.7,48.4 289.9,49.8 292.0,51.5 294.1,53.4 296.3,55.6 298.4,57.9 300.6,60.5 302.7,63.3 304.9,66.4 307.0,69.6 309.1,73.0 311.3,76.5 313.4,80.3 315.6,84.1 317.7,88.2 319.9,92.3 322.0,96.6 324.1,101.0 326.3,105.4 328.4,110.0 330.6,114.6 332.7,119.3 334.9,124.0 337.0,128.8 339.1,133.5 341.3,138.3 343.4,143.1 345.6,147.9 347.7,152.7 349.9,157.4 352.0,162.1 354.1,166.7 356.3,171.3 358.4,175.8 360.6,180.2 362.7,184.6 364.9,188.9 367.0,193.1 369.1,197.2 371.3,201.2 373.4,205.1 375.6,208.9 377.7,212.6 379.9,216.1 382.0,219.6 384.1,222.9 386.3,226.2 388.4,229.3 390.6,232.3 392.7,235.1 394.9,237.9 397.0,240.5 399.1,243.0 401.3,245.5 403.4,247.8 405.6,249.9 405.6,282.0"/>
<line class="fm-grid" x1="52" y1="282.0" x2="502" y2="282.0"/>
<text class="fm-t" x="46" y="286.0" text-anchor="end">0,00</text>
<line class="fm-grid" x1="52" y1="234.5" x2="502" y2="234.5"/>
<text class="fm-t" x="46" y="238.5" text-anchor="end">0,01</text>
<line class="fm-grid" x1="52" y1="187.0" x2="502" y2="187.0"/>
<text class="fm-t" x="46" y="191.0" text-anchor="end">0,02</text>
<line class="fm-grid" x1="52" y1="139.5" x2="502" y2="139.5"/>
<text class="fm-t" x="46" y="143.5" text-anchor="end">0,03</text>
<line class="fm-grid" x1="52" y1="92.0" x2="502" y2="92.0"/>
<text class="fm-t" x="46" y="96.0" text-anchor="end">0,04</text>
<line class="fm-grid" x1="52" y1="44.5" x2="502" y2="44.5"/>
<text class="fm-t" x="46" y="48.5" text-anchor="end">0,05</text>
<line class="fm-grid" x1="84.1" y1="16" x2="84.1" y2="282"/>
<text class="fm-t" x="84.1" y="298" text-anchor="middle">76</text>
<line class="fm-grid" x1="148.4" y1="16" x2="148.4" y2="282"/>
<text class="fm-t" x="148.4" y="298" text-anchor="middle">84</text>
<line class="fm-grid" x1="212.7" y1="16" x2="212.7" y2="282"/>
<text class="fm-t" x="212.7" y="298" text-anchor="middle">92</text>
<line class="fm-grid" x1="277.0" y1="16" x2="277.0" y2="282"/>
<text class="fm-t" x="277.0" y="298" text-anchor="middle">100</text>
<line class="fm-grid" x1="341.3" y1="16" x2="341.3" y2="282"/>
<text class="fm-t" x="341.3" y="298" text-anchor="middle">108</text>
<line class="fm-grid" x1="405.6" y1="16" x2="405.6" y2="282"/>
<text class="fm-t" x="405.6" y="298" text-anchor="middle">116</text>
<line class="fm-grid" x1="469.9" y1="16" x2="469.9" y2="282"/>
<text class="fm-t" x="469.9" y="298" text-anchor="middle">124</text>
<line class="fm-axis" x1="52" y1="282.0" x2="502" y2="282.0"/>
<line class="fm-axis" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t fm-i" x="502" y="314" text-anchor="end">x (ms)</text>
<text class="fm-t fm-i" x="56" y="24">densité</text>
<polyline class="fm-curve" points="52.0,281.5 53.5,281.4 55.0,281.4 56.5,281.3 58.0,281.3 59.5,281.2 61.0,281.2 62.5,281.1 64.0,281.0 65.5,280.9 67.0,280.9 68.5,280.8 70.0,280.7 71.5,280.6 73.0,280.5 74.5,280.3 76.0,280.2 77.5,280.1 79.0,279.9 80.5,279.8 82.0,279.6 83.5,279.4 85.0,279.3 86.5,279.1 88.0,278.9 89.5,278.6 91.0,278.4 92.5,278.1 94.0,277.9 95.5,277.6 97.0,277.3 98.5,277.0 100.0,276.6 101.5,276.3 103.0,275.9 104.5,275.5 106.0,275.1 107.5,274.7 109.0,274.2 110.5,273.7 112.0,273.2 113.5,272.7 115.0,272.1 116.5,271.5 118.0,270.9 119.5,270.2 121.0,269.5 122.5,268.8 124.0,268.1 125.5,267.3 127.0,266.4 128.5,265.6 130.0,264.7 131.5,263.7 133.0,262.7 134.5,261.7 136.0,260.6 137.5,259.5 139.0,258.3 140.5,257.1 142.0,255.9 143.5,254.6 145.0,253.2 146.5,251.8 148.0,250.4 149.5,248.9 151.0,247.3 152.5,245.7 154.0,244.0 155.5,242.3 157.0,240.5 158.5,238.7 160.0,236.8 161.5,234.8 163.0,232.8 164.5,230.8 166.0,228.7 167.5,226.5 169.0,224.2 170.5,221.9 172.0,219.6 173.5,217.2 175.0,214.7 176.5,212.2 178.0,209.6 179.5,207.0 181.0,204.3 182.5,201.6 184.0,198.8 185.5,196.0 187.0,193.1 188.5,190.2 190.0,187.2 191.5,184.2 193.0,181.1 194.5,178.0 196.0,174.9 197.5,171.7 199.0,168.5 200.5,165.3 202.0,162.1 203.5,158.8 205.0,155.5 206.5,152.2 208.0,148.8 209.5,145.5 211.0,142.2 212.5,138.8 214.0,135.5 215.5,132.1 217.0,128.8 218.5,125.4 220.0,122.1 221.5,118.8 223.0,115.5 224.5,112.3 226.0,109.1 227.5,105.9 229.0,102.8 230.5,99.7 232.0,96.6 233.5,93.6 235.0,90.7 236.5,87.8 238.0,84.9 239.5,82.2 241.0,79.5 242.5,76.9 244.0,74.4 245.5,71.9 247.0,69.6 248.5,67.3 250.0,65.1 251.5,63.0 253.0,61.1 254.5,59.2 256.0,57.4 257.5,55.8 259.0,54.2 260.5,52.8 262.0,51.5 263.5,50.3 265.0,49.2 266.5,48.3 268.0,47.4 269.5,46.7 271.0,46.2 272.5,45.7 274.0,45.4 275.5,45.2 277.0,45.1 278.5,45.2 280.0,45.4 281.5,45.7 283.0,46.2 284.5,46.7 286.0,47.4 287.5,48.3 289.0,49.2 290.5,50.3 292.0,51.5 293.5,52.8 295.0,54.2 296.5,55.8 298.0,57.4 299.5,59.2 301.0,61.1 302.5,63.0 304.0,65.1 305.5,67.3 307.0,69.6 308.5,71.9 310.0,74.4 311.5,76.9 313.0,79.5 314.5,82.2 316.0,84.9 317.5,87.8 319.0,90.7 320.5,93.6 322.0,96.6 323.5,99.7 325.0,102.8 326.5,105.9 328.0,109.1 329.5,112.3 331.0,115.5 332.5,118.8 334.0,122.1 335.5,125.4 337.0,128.8 338.5,132.1 340.0,135.5 341.5,138.8 343.0,142.2 344.5,145.5 346.0,148.8 347.5,152.2 349.0,155.5 350.5,158.8 352.0,162.1 353.5,165.3 355.0,168.5 356.5,171.7 358.0,174.9 359.5,178.0 361.0,181.1 362.5,184.2 364.0,187.2 365.5,190.2 367.0,193.1 368.5,196.0 370.0,198.8 371.5,201.6 373.0,204.3 374.5,207.0 376.0,209.6 377.5,212.2 379.0,214.7 380.5,217.2 382.0,219.6 383.5,221.9 385.0,224.2 386.5,226.5 388.0,228.7 389.5,230.8 391.0,232.8 392.5,234.8 394.0,236.8 395.5,238.7 397.0,240.5 398.5,242.3 400.0,244.0 401.5,245.7 403.0,247.3 404.5,248.9 406.0,250.4 407.5,251.8 409.0,253.2 410.5,254.6 412.0,255.9 413.5,257.1 415.0,258.3 416.5,259.5 418.0,260.6 419.5,261.7 421.0,262.7 422.5,263.7 424.0,264.7 425.5,265.6 427.0,266.4 428.5,267.3 430.0,268.1 431.5,268.8 433.0,269.5 434.5,270.2 436.0,270.9 437.5,271.5 439.0,272.1 440.5,272.7 442.0,273.2 443.5,273.7 445.0,274.2 446.5,274.7 448.0,275.1 449.5,275.5 451.0,275.9 452.5,276.3 454.0,276.6 455.5,277.0 457.0,277.3 458.5,277.6 460.0,277.9 461.5,278.1 463.0,278.4 464.5,278.6 466.0,278.9 467.5,279.1 469.0,279.3 470.5,279.4 472.0,279.6 473.5,279.8 475.0,279.9 476.5,280.1 478.0,280.2 479.5,280.3 481.0,280.5 482.5,280.6 484.0,280.7 485.5,280.8 487.0,280.9 488.5,280.9 490.0,281.0 491.5,281.1 493.0,281.2 494.5,281.2 496.0,281.3 497.5,281.3 499.0,281.4 500.5,281.4 502.0,281.5"/>
<line class="fm-dash" x1="277.0" y1="282.0" x2="277.0" y2="45.1"/>
<text class="fm-t fm-b" x="277.0" y="187.0" text-anchor="middle">≈ 68 %</text>
<text class="fm-t" x="180.6" y="244.0" text-anchor="start">≈ 95 % entre 84 et 116</text>
</svg>
<figcaption>Loi normale de moyenne 100 et d’écart type 8 : environ 68 % des valeurs sont entre 92 et 108 (moyenne ± σ), environ 95 % entre 84 et 116 (moyenne ± 2σ).</figcaption>
</figure>

**À retenir sur la cloche.**

- \(P(m - \sigma \le X \le m + \sigma) \approx 0{,}68\) ;
- \(P(m - 2\sigma \le X \le m + 2\sigma) \approx 0{,}95\) ;
- la cloche est **symétrique** : \(P(X \le m) = 0{,}5\).

### Calculer une probabilité

**À la calculatrice** (voir l'[aide-mémoire](../aide-memoire-calculatrice.md)). On donne les bornes, la moyenne et l'écart type. Pour \(X \sim \mathcal{N}(100\,;\,8)\) :

- \(P(X \le 105) \approx 0{,}7340\) ;
- \(P(90 \le X \le 110) \approx 0{,}7887\).

**Par la variable centrée réduite** (pour comprendre). On se ramène à la loi \(\mathcal{N}(0\,;\,1)\) en posant \(Z = \dfrac{X - m}{\sigma}\) : on mesure l'écart en **nombre d'écarts types**. Par exemple \(X = 105\) correspond à \(z = \dfrac{105 - 100}{8} = 0{,}625\), et \(P(X \le 105) = P(Z \le 0{,}625) \approx 0{,}7340\).

### Retrouver un seuil

**Question.** Quel temps \(t\) n'est dépassé que dans 5 % des cas ? On cherche \(t\) tel que \(P(X \le t) = 0{,}95\). La calculatrice a une fonction de **loi normale inverse**. On trouve \(t \approx 113{,}16\) ms.

**Vérification par le calcul.** Pour 95 % à gauche, \(z \approx 1{,}645\), donc \(t = 100 + 1{,}645 \times 8 \approx 113{,}2\).

**Exemple résolu.** Le contrat impose que 95 % des réponses soient sous 115 ms. Est-il respecté ?

<details markdown="1">
<summary>Voir la solution</summary>

Le temps dépassé dans seulement 5 % des cas est \(113{,}16\) ms, **inférieur à 115 ms**. Donc au moins 95 % des réponses sont sous 115 ms : **le contrat est respecté**, avec une marge d'environ 2 ms.

(Contrôle direct : \(P(X \le 115)\) correspond à \(z = \dfrac{15}{8} = 1{,}875\), soit environ \(0{,}970\), supérieur à \(0{,}95\).)

</details>

## 4. Choisir la bonne loi

| Situation | Loi | Question à se poser |
|---|---|---|
| Nombre de succès sur \(n\) essais indépendants de probabilité \(p\) | binomiale \(\mathcal{B}(n\,;\,p)\) | combien d'essais ? quelle probabilité de succès ? |
| Nombre d'événements rares sur une période, moyenne \(\lambda\) | Poisson \(\mathcal{P}(\lambda)\) | quel rythme moyen ? |
| Mesure continue autour d'une moyenne (temps, taille) | normale \(\mathcal{N}(m\,;\,\sigma)\) | quelle moyenne ? quel écart type ? |
| Durée avant une panne sans vieillissement | exponentielle (module M5) | quel taux de défaillance ? |

## 5. À retenir

> [!NOTE]
> - **Poisson** \(\mathcal{P}(\lambda)\) : \(P(X = k) = e^{-\lambda}\dfrac{\lambda^{k}}{k!}\), \(E = V = \lambda\) ; approche la binomiale si \(n\) grand et \(p\) petit.
> - **Normale** \(\mathcal{N}(m\,;\,\sigma)\) : cloche symétrique ; \(\approx 68\) % à \(\pm\sigma\), \(\approx 95\) % à \(\pm 2\sigma\) ; probabilités d'intervalles par la calculatrice.
> - Seuil à \(p\) % : fonction de **loi normale inverse**.
> - Choisir la loi **avant** de calculer, et **interpréter** en une phrase.

## 6. Teste-toi

**Question 1.** \(X \sim \mathcal{P}(3)\). Calculer \(P(X = 0)\).

**Question 2.** \(X \sim \mathcal{N}(50\,;\,10)\). Calculer \(P(X \le 60)\) et \(P(40 \le X \le 60)\).

**Question 3.** Un composant a une probabilité \(0{,}01\) d'être défectueux ; on en contrôle 300. Quelle loi approchée utiliser pour le nombre de défectueux ? Quel est son paramètre ?

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(P(X = 0) = e^{-3} \approx 0{,}0498\) (environ 5 %).
2. \(60 = m + \sigma\), donc \(P(X \le 60) = P(Z \le 1) \approx 0{,}8413\). L'intervalle \([40\,;\,60] = [m - \sigma\,;\,m + \sigma]\) donne environ \(0{,}6827\) (la règle des 68 %).
3. La loi exacte est \(\mathcal{B}(300\,;\,0{,}01)\) (\(n\) grand, \(p\) petit), qu'on approche par \(\mathcal{P}(\lambda)\) avec \(\lambda = 300 \times 0{,}01 = 3\).

</details>

**Pour continuer :** les [exercices du module](03-exercices.md), puis le [module M5 sur la fiabilité](../M5-fiabilite/01-fiabilite-et-loi-exponentielle.md).

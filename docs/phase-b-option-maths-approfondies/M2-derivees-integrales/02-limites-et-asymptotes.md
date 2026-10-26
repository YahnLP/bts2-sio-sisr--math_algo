# Cours 2 – Limites et asymptotes

*BTS SIO SISR 2e année – Option mathématiques approfondies – M2, deuxième partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : expliquer ce qu'est une limite en \(+\infty\) ; connaître les limites usuelles ; reconnaître une **asymptote horizontale** ; **interpréter** une limite comme un régime stable (saturation, retour à zéro).
>
> **Programme.** Les calculs de limite restent élémentaires : on s'appuie sur les limites usuelles, sur des tableaux de valeurs et sur la calculatrice formelle. L'étude de la continuité est hors programme.

## 1. Pour démarrer : que se passe-t-il à long terme ?

Un service doit traiter des requêtes. Après un incident, la charge supplémentaire est \(f(x) = (x + 2)e^{-x}\) (en milliers de requêtes par minute), \(x\) heures après l'incident. Que devient la charge **à long terme** ?

On calcule à la calculatrice :

| \(x\) (heures) | 0 | 1 | 5 | 10 | 20 |
|---|---|---|---|---|---|
| \(f(x)\) | 2 | 1,10 | 0,047 | 0,00054 | 0,00000005 |

Les valeurs deviennent de plus en plus proches de 0 : on dit que \(f(x)\) **tend vers 0 quand \(x\) tend vers \(+\infty\)**, et on écrit \(\lim\limits_{x \to +\infty} f(x) = 0\).

## 2. Qu'est-ce qu'une limite ?

**Idée.** Dire que \(\lim\limits_{x \to +\infty} f(x) = \ell\) signifie : quand \(x\) devient de plus en plus grand, \(f(x)\) devient aussi proche qu'on veut du nombre \(\ell\) (sans forcément jamais l'atteindre).

On peut aussi avoir \(\lim\limits_{x \to +\infty} f(x) = +\infty\) : la fonction grandit **sans borne**.

**Limites usuelles à connaître** (quand \(x \to +\infty\)) :

| Fonction | Limite |
|---|---|
| \(\dfrac{1}{x}\) | \(0\) |
| \(x^{2}\) | \(+\infty\) |
| \(e^{x}\) | \(+\infty\) |
| \(e^{-x}\) | \(0\) |
| \(\ln x\) | \(+\infty\) (très lentement) |
| \(x\,e^{-x}\) | \(0\) |

**Pourquoi \(x\,e^{-x} \to 0\) ?** Le facteur \(x\) grandit, le facteur \(e^{-x}\) s'écrase vers 0, et c'est l'**exponentielle qui gagne** : elle décroît beaucoup plus vite que \(x\) ne croît. Vérifions sur des valeurs : \(1 \times e^{-1} \approx 0{,}368\), \(5e^{-5} \approx 0{,}034\), \(10e^{-10} \approx 0{,}00045\). C'est la règle de la **croissance comparée** : \(e^{x}\) l'emporte sur toute puissance de \(x\), et toute puissance de \(x\) l'emporte sur \(\ln x\).

> [!TIP]
> **Comment trouver une limite.** (1) Reconnaître une limite usuelle ; (2) sinon, remplir un tableau de valeurs avec de grandes valeurs de \(x\) ; (3) vérifier à la calculatrice formelle. Les opérations simples fonctionnent : la limite d'une somme est la somme des limites, celle d'un produit est le produit des limites (quand ça a un sens).

## 3. L'asymptote horizontale

**Définition.** Si \(\lim\limits_{x \to +\infty} f(x) = \ell\), la droite \(y = \ell\) est une **asymptote horizontale** à la courbe : la courbe s'en rapproche indéfiniment.

<figure class="fig-math">
<svg viewBox="0 0 520 320" role="img" aria-label="Asymptote y=2">
<line class="fm-grid" x1="52" y1="282.0" x2="502" y2="282.0"/>
<text class="fm-t" x="46" y="286.0" text-anchor="end">0</text>
<line class="fm-grid" x1="52" y1="228.8" x2="502" y2="228.8"/>
<text class="fm-t" x="46" y="232.8" text-anchor="end">0,5</text>
<line class="fm-grid" x1="52" y1="175.6" x2="502" y2="175.6"/>
<text class="fm-t" x="46" y="179.6" text-anchor="end">1</text>
<line class="fm-grid" x1="52" y1="122.4" x2="502" y2="122.4"/>
<text class="fm-t" x="46" y="126.4" text-anchor="end">1,5</text>
<line class="fm-grid" x1="52" y1="69.2" x2="502" y2="69.2"/>
<text class="fm-t" x="46" y="73.2" text-anchor="end">2</text>
<line class="fm-grid" x1="52" y1="16.0" x2="502" y2="16.0"/>
<text class="fm-t" x="46" y="20.0" text-anchor="end">2,5</text>
<line class="fm-grid" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t" x="52.0" y="298" text-anchor="middle">0</text>
<line class="fm-grid" x1="142.0" y1="16" x2="142.0" y2="282"/>
<text class="fm-t" x="142.0" y="298" text-anchor="middle">2</text>
<line class="fm-grid" x1="232.0" y1="16" x2="232.0" y2="282"/>
<text class="fm-t" x="232.0" y="298" text-anchor="middle">4</text>
<line class="fm-grid" x1="322.0" y1="16" x2="322.0" y2="282"/>
<text class="fm-t" x="322.0" y="298" text-anchor="middle">6</text>
<line class="fm-grid" x1="412.0" y1="16" x2="412.0" y2="282"/>
<text class="fm-t" x="412.0" y="298" text-anchor="middle">8</text>
<line class="fm-grid" x1="502.0" y1="16" x2="502.0" y2="282"/>
<text class="fm-t" x="502.0" y="298" text-anchor="middle">10</text>
<line class="fm-axis" x1="52" y1="282.0" x2="502" y2="282.0"/>
<line class="fm-axis" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t fm-i" x="502" y="314" text-anchor="end">x</text>
<text class="fm-t fm-i" x="56" y="24">g(x)</text>
<line class="fm-dash" x1="52.0" y1="69.2" x2="502.0" y2="69.2"/>
<polyline class="fm-curve" points="52.0,175.6 53.5,172.2 55.0,168.9 56.5,165.9 58.0,163.1 59.5,160.4 61.0,157.9 62.5,155.5 64.0,153.2 65.5,151.0 67.0,149.0 68.5,147.1 70.0,145.2 71.5,143.4 73.0,141.7 74.5,140.1 76.0,138.6 77.5,137.1 79.0,135.7 80.5,134.3 82.0,133.0 83.5,131.8 85.0,130.6 86.5,129.4 88.0,128.3 89.5,127.2 91.0,126.2 92.5,125.2 94.0,124.2 95.5,123.3 97.0,122.4 98.5,121.5 100.0,120.7 101.5,119.9 103.0,119.1 104.5,118.3 106.0,117.6 107.5,116.8 109.0,116.1 110.5,115.5 112.0,114.8 113.5,114.2 115.0,113.5 116.5,112.9 118.0,112.3 119.5,111.8 121.0,111.2 122.5,110.7 124.0,110.1 125.5,109.6 127.0,109.1 128.5,108.6 130.0,108.1 131.5,107.7 133.0,107.2 134.5,106.8 136.0,106.3 137.5,105.9 139.0,105.5 140.5,105.1 142.0,104.7 143.5,104.3 145.0,103.9 146.5,103.5 148.0,103.2 149.5,102.8 151.0,102.4 152.5,102.1 154.0,101.8 155.5,101.4 157.0,101.1 158.5,100.8 160.0,100.5 161.5,100.2 163.0,99.9 164.5,99.6 166.0,99.3 167.5,99.0 169.0,98.8 170.5,98.5 172.0,98.2 173.5,98.0 175.0,97.7 176.5,97.4 178.0,97.2 179.5,97.0 181.0,96.7 182.5,96.5 184.0,96.3 185.5,96.0 187.0,95.8 188.5,95.6 190.0,95.4 191.5,95.2 193.0,94.9 194.5,94.7 196.0,94.5 197.5,94.3 199.0,94.1 200.5,93.9 202.0,93.8 203.5,93.6 205.0,93.4 206.5,93.2 208.0,93.0 209.5,92.8 211.0,92.7 212.5,92.5 214.0,92.3 215.5,92.2 217.0,92.0 218.5,91.8 220.0,91.7 221.5,91.5 223.0,91.4 224.5,91.2 226.0,91.1 227.5,90.9 229.0,90.8 230.5,90.6 232.0,90.5 233.5,90.3 235.0,90.2 236.5,90.1 238.0,89.9 239.5,89.8 241.0,89.7 242.5,89.5 244.0,89.4 245.5,89.3 247.0,89.2 248.5,89.0 250.0,88.9 251.5,88.8 253.0,88.7 254.5,88.5 256.0,88.4 257.5,88.3 259.0,88.2 260.5,88.1 262.0,88.0 263.5,87.9 265.0,87.8 266.5,87.7 268.0,87.5 269.5,87.4 271.0,87.3 272.5,87.2 274.0,87.1 275.5,87.0 277.0,86.9 278.5,86.8 280.0,86.7 281.5,86.6 283.0,86.5 284.5,86.5 286.0,86.4 287.5,86.3 289.0,86.2 290.5,86.1 292.0,86.0 293.5,85.9 295.0,85.8 296.5,85.7 298.0,85.7 299.5,85.6 301.0,85.5 302.5,85.4 304.0,85.3 305.5,85.2 307.0,85.2 308.5,85.1 310.0,85.0 311.5,84.9 313.0,84.8 314.5,84.8 316.0,84.7 317.5,84.6 319.0,84.5 320.5,84.5 322.0,84.4 323.5,84.3 325.0,84.3 326.5,84.2 328.0,84.1 329.5,84.0 331.0,84.0 332.5,83.9 334.0,83.8 335.5,83.8 337.0,83.7 338.5,83.6 340.0,83.6 341.5,83.5 343.0,83.4 344.5,83.4 346.0,83.3 347.5,83.3 349.0,83.2 350.5,83.1 352.0,83.1 353.5,83.0 355.0,83.0 356.5,82.9 358.0,82.8 359.5,82.8 361.0,82.7 362.5,82.7 364.0,82.6 365.5,82.6 367.0,82.5 368.5,82.4 370.0,82.4 371.5,82.3 373.0,82.3 374.5,82.2 376.0,82.2 377.5,82.1 379.0,82.1 380.5,82.0 382.0,82.0 383.5,81.9 385.0,81.9 386.5,81.8 388.0,81.8 389.5,81.7 391.0,81.7 392.5,81.6 394.0,81.6 395.5,81.5 397.0,81.5 398.5,81.4 400.0,81.4 401.5,81.3 403.0,81.3 404.5,81.2 406.0,81.2 407.5,81.2 409.0,81.1 410.5,81.1 412.0,81.0 413.5,81.0 415.0,80.9 416.5,80.9 418.0,80.8 419.5,80.8 421.0,80.8 422.5,80.7 424.0,80.7 425.5,80.6 427.0,80.6 428.5,80.6 430.0,80.5 431.5,80.5 433.0,80.4 434.5,80.4 436.0,80.4 437.5,80.3 439.0,80.3 440.5,80.2 442.0,80.2 443.5,80.2 445.0,80.1 446.5,80.1 448.0,80.1 449.5,80.0 451.0,80.0 452.5,79.9 454.0,79.9 455.5,79.9 457.0,79.8 458.5,79.8 460.0,79.8 461.5,79.7 463.0,79.7 464.5,79.7 466.0,79.6 467.5,79.6 469.0,79.6 470.5,79.5 472.0,79.5 473.5,79.5 475.0,79.4 476.5,79.4 478.0,79.4 479.5,79.3 481.0,79.3 482.5,79.3 484.0,79.2 485.5,79.2 487.0,79.2 488.5,79.1 490.0,79.1 491.5,79.1 493.0,79.1 494.5,79.0 496.0,79.0 497.5,79.0 499.0,78.9 500.5,78.9 502.0,78.9"/>
<circle class="fm-pt" cx="52.0" cy="175.6" r="4.5"/>
<text class="fm-t" x="62.0" y="191.6" text-anchor="start">g(0) = 1</text>
<text class="fm-t" x="496.0" y="61.2" text-anchor="end">asymptote y = 2</text>
</svg>
<figcaption>g(x) = (2x + 1)/(x + 1) se rapproche de 2 sans jamais l’atteindre : la droite y = 2 est une asymptote horizontale.</figcaption>
</figure>

**Exemple résolu.** Étudier \(g(x) = \dfrac{2x + 1}{x + 1}\) pour \(x \ge 0\).

<details markdown="1">
<summary>Voir la solution détaillée</summary>

**Valeurs.** \(g(0) = 1\) ; \(g(1) = 1{,}5\) ; \(g(10) \approx 1{,}909\) ; \(g(100) \approx 1{,}990\) ; \(g(1000) \approx 1{,}999\). Les valeurs approchent 2 par en dessous.

**Limite, par le calcul.** On met \(x\) en facteur en haut et en bas : \(g(x) = \dfrac{x\left(2 + \frac{1}{x}\right)}{x\left(1 + \frac{1}{x}\right)} = \dfrac{2 + \frac{1}{x}}{1 + \frac{1}{x}}\). Quand \(x \to +\infty\), \(\dfrac{1}{x} \to 0\), donc \(g(x) \to \dfrac{2}{1} = 2\).

**Variations.** On a vu (cours 1) que \(g'(x) = \dfrac{1}{(x + 1)^2} > 0\) : \(g\) est croissante, de \(g(0) = 1\) vers 2.

**Conclusion.** La droite \(y = 2\) est une asymptote horizontale, et \(g\) ne l'atteint jamais : elle prend toutes les valeurs de \([1\,;\,2[\).

</details>

## 4. Interpréter une limite : le régime stable

Dans un problème, la limite décrit **ce qui se passe à long terme**. C'est souvent la question « que devient la grandeur ? » à laquelle il faut répondre **par une phrase**.

| Situation | Limite | Interprétation |
|---|---|---|
| Charge après un incident, \((x+2)e^{-x}\) | \(0\) | l'incident se résorbe, la charge revient à la normale |
| Remplissage d'un disque, \(100(1 - e^{-0{,}5t})\) | \(100\) | saturation : le disque se remplit à 100 %, sans le dépasser |
| Trafic, \(2x + 1\) | \(+\infty\) | croissance sans limite : il faudra augmenter les capacités |

**Exemple résolu : un remplissage qui sature.** Le taux de remplissage d'un volume (en %) est \(R(t) = 100\left(1 - e^{-0{,}5t}\right)\), avec \(t\) en heures. Calculer \(R(2)\), \(R(6)\) et la limite en \(+\infty\). Interpréter.

<details markdown="1">
<summary>Voir la solution</summary>

\(R(2) = 100(1 - e^{-1}) \approx 63{,}2\) % ; \(R(6) = 100(1 - e^{-3}) \approx 95{,}0\) %.

Quand \(t \to +\infty\), \(e^{-0{,}5t} \to 0\), donc \(R(t) \to 100\). La droite \(y = 100\) est asymptote.

**Interprétation.** Le volume se remplit vite au début (63 % en 2 heures), puis de plus en plus lentement ; il approche 100 % sans jamais le dépasser : c'est un **régime de saturation**. Au bout de 6 heures, il reste environ 5 % à remplir.

</details>

## 5. Explorer avec Python

On peut « sentir » une limite avec quelques lignes :

```python
from math import exp

for x in [1, 5, 10, 20]:
    print(x, (x + 2) * exp(-x))
```

Les valeurs affichées décroissent vers 0 : c'est ce qu'on a vu dans le tableau. Cette exploration **ne remplace pas** une justification (on invoque une limite usuelle), mais elle évite une erreur grossière.

## 6. À retenir

> [!NOTE]
> - \(\lim\limits_{x \to +\infty} f(x) = \ell\) : \(f(x)\) s'approche de \(\ell\) quand \(x\) devient très grand.
> - Limites usuelles : \(\dfrac{1}{x} \to 0\), \(e^{-x} \to 0\), \(e^{x} \to +\infty\), \(\ln x \to +\infty\), \(x\,e^{-x} \to 0\).
> - Une limite finie \(\ell\) donne l'**asymptote horizontale** \(y = \ell\).
> - **Interpréter** : la limite décrit le régime stable (retour à zéro, saturation, croissance sans borne).

## 7. Teste-toi

**Question 1.** Donner la limite en \(+\infty\) de \(5 + \dfrac{3}{x}\), de \(4e^{-2x}\) et de \(\ln x\).

**Question 2.** La charge d'un serveur est \(c(t) = 80 - 60e^{-t}\) (en %). Donner \(c(0)\), la limite en \(+\infty\) et interpréter.

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(5 + \dfrac{3}{x} \to 5\) ; \(4e^{-2x} \to 0\) ; \(\ln x \to +\infty\).
2. \(c(0) = 80 - 60 = 20\) %. Comme \(e^{-t} \to 0\), \(c(t) \to 80\) : la charge **augmente** de 20 % vers un plafond de 80 % et se stabilise à ce niveau (asymptote \(y = 80\)).

</details>

**Pour continuer :** le [cours 3 sur les primitives et l'intégrale](03-primitives-et-integrales.md).

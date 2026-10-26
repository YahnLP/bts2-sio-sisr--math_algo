# Cours 1 – Fonctions et modèles

*BTS SIO SISR 2e année – Option mathématiques approfondies – M1, première partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : lire une fonction donnée par une formule, un tableau ou une courbe ; reconnaître une fonction affine, du second degré, inverse ; résoudre une équation et comparer deux modèles ; composer deux fonctions ; **valider** un résultat dans son contexte.
>
> **Prérequis.** Le calcul littéral et les équations du premier degré (programme de l'unité de mathématiques de première année).
>
> **Durée conseillée.** 1 h 30 de lecture active (crayon en main), puis les exercices de niveau 1.

## 1. Pour démarrer : pourquoi des fonctions ?

Un hébergeur facture 40 € de frais fixes, plus 2,50 € par machine virtuelle. Combien coûtent 4 machines ? 10 ? 25 ?

| Nombre de machines | 4 | 10 | 25 |
|---|---|---|---|
| Coût (en €) | 50 | 65 | 102,5 |

À chaque nombre de machines correspond **un seul** coût : c'est une **fonction**. On la note par exemple \(C\) et on écrit \(C(x) = 40 + 2{,}5x\), où \(x\) est le nombre de machines. Une fonction est un **modèle** : une règle qui permet de prévoir une grandeur (le coût) à partir d'une autre (le nombre de machines), sans refaire le calcul à la main chaque fois.

## 2. Le vocabulaire à connaître

Pour une fonction \(f\) :

- \(x\) est la **variable** (la grandeur d'entrée) ;
- \(f(x)\) est l'**image** de \(x\) (la grandeur de sortie), lue « \(f\) de \(x\) » ;
- si \(f(a) = b\), on dit que \(a\) est **un antécédent** de \(b\). Un nombre peut avoir **plusieurs** antécédents, ou aucun.

Une fonction se présente de trois façons, qu'il faut savoir lire et relier :

| Présentation | Avantage | Exemple |
|---|---|---|
| **Formule** | calcule n'importe quelle valeur | \(C(x) = 40 + 2{,}5x\) |
| **Tableau de valeurs** | lecture rapide de quelques valeurs | le tableau ci-dessus |
| **Courbe** | vue d'ensemble : sens de variation, extremums | voir les figures ci-dessous |

> [!TIP]
> **Notation.** \(f(3)\) ne veut **pas** dire « \(f\) multiplié par 3 », mais « l'image de 3 par \(f\) ». Pour calculer \(f(3)\), on remplace partout \(x\) par 3.

**Exemple résolu.** Pour \(f(x) = x^2 - 4x\), calculer \(f(0)\), \(f(1)\), \(f(5)\), puis chercher un antécédent de 5.

<details markdown="1">
<summary>Voir la solution</summary>

On remplace \(x\) :

- \(f(0) = 0^2 - 4 \times 0 = 0\) ;
- \(f(1) = 1 - 4 = -3\) ;
- \(f(5) = 25 - 20 = 5\).

Comme \(f(5) = 5\), le nombre 5 est **un antécédent** de 5. On peut aussi vérifier que \(-1\) en est un autre : \(f(-1) = 1 + 4 = 5\). Le nombre 5 a donc au moins deux antécédents : c'est possible, car une fonction n'est pas obligée d'être « à sens unique » dans l'autre sens.

</details>

## 3. La fonction affine : le modèle le plus simple

**Définition.** Une fonction affine s'écrit \(f(x) = ax + b\). Sa courbe est une **droite**.

- \(a\) est la **pente** (ou coefficient directeur) : de combien \(f(x)\) varie quand \(x\) augmente de 1 ;
- \(b\) est l'**ordonnée à l'origine** : la valeur de \(f(0)\).

Dans le coût d'hébergement \(C(x) = 40 + 2{,}5x\), la pente \(2{,}5\) est le **prix d'une machine supplémentaire** et \(40\) est le **coût fixe**. Savoir donner ce sens aux deux nombres est souvent demandé à l'épreuve.

**Sens de variation.** Si \(a > 0\), la fonction est croissante (la droite monte) ; si \(a < 0\), elle est décroissante (la droite descend) ; si \(a = 0\), elle est constante.

**Retrouver \(a\) et \(b\) à partir de deux points.** Si la droite passe par \((x_1\,;\,y_1)\) et \((x_2\,;\,y_2)\), alors \(a = \dfrac{y_2 - y_1}{x_2 - x_1}\), puis \(b = y_1 - a x_1\).

**Exemple résolu.** Un serveur consomme 120 W à vide et 180 W avec 6 machines virtuelles, la consommation étant affine en le nombre de machines. Trouver la formule.

<details markdown="1">
<summary>Voir la solution</summary>

Deux points : \((0\,;\,120)\) et \((6\,;\,180)\). La pente est \(a = \dfrac{180 - 120}{6 - 0} = 10\) : chaque machine ajoute **10 W**. Comme \(f(0) = 120\), on a \(b = 120\). Donc \(f(x) = 10x + 120\).

Contrôle : \(f(6) = 60 + 120 = 180\). Prévision pour 10 machines : \(f(10) = 220\) W.

</details>

## 4. La fonction du second degré : la parabole

**Définition.** Une fonction du second degré s'écrit \(f(x) = ax^2 + bx + c\) avec \(a \ne 0\). Sa courbe est une **parabole**.

<figure class="fig-math">
<svg viewBox="0 0 520 320" role="img" aria-label="Parabole f(x)=2x²−8x+6">
<line class="fm-grid" x1="52" y1="261.5" x2="502" y2="261.5"/>
<text class="fm-t" x="46" y="265.5" text-anchor="end">−2</text>
<line class="fm-grid" x1="52" y1="220.6" x2="502" y2="220.6"/>
<text class="fm-t" x="46" y="224.6" text-anchor="end">0</text>
<line class="fm-grid" x1="52" y1="179.7" x2="502" y2="179.7"/>
<text class="fm-t" x="46" y="183.7" text-anchor="end">2</text>
<line class="fm-grid" x1="52" y1="138.8" x2="502" y2="138.8"/>
<text class="fm-t" x="46" y="142.8" text-anchor="end">4</text>
<line class="fm-grid" x1="52" y1="97.8" x2="502" y2="97.8"/>
<text class="fm-t" x="46" y="101.8" text-anchor="end">6</text>
<line class="fm-grid" x1="52" y1="56.9" x2="502" y2="56.9"/>
<text class="fm-t" x="46" y="60.9" text-anchor="end">8</text>
<line class="fm-grid" x1="52" y1="16.0" x2="502" y2="16.0"/>
<text class="fm-t" x="46" y="20.0" text-anchor="end">10</text>
<line class="fm-grid" x1="97.0" y1="16" x2="97.0" y2="282"/>
<text class="fm-t" x="97.0" y="298" text-anchor="middle">0</text>
<line class="fm-grid" x1="187.0" y1="16" x2="187.0" y2="282"/>
<text class="fm-t" x="187.0" y="298" text-anchor="middle">1</text>
<line class="fm-grid" x1="277.0" y1="16" x2="277.0" y2="282"/>
<text class="fm-t" x="277.0" y="298" text-anchor="middle">2</text>
<line class="fm-grid" x1="367.0" y1="16" x2="367.0" y2="282"/>
<text class="fm-t" x="367.0" y="298" text-anchor="middle">3</text>
<line class="fm-grid" x1="457.0" y1="16" x2="457.0" y2="282"/>
<text class="fm-t" x="457.0" y="298" text-anchor="middle">4</text>
<line class="fm-axis" x1="52" y1="220.6" x2="502" y2="220.6"/>
<line class="fm-axis" x1="97.0" y1="16" x2="97.0" y2="282"/>
<text class="fm-t fm-i" x="502" y="314" text-anchor="end">x</text>
<text class="fm-t fm-i" x="56" y="24">f(x)</text>
<line class="fm-dash" x1="277.0" y1="282.0" x2="277.0" y2="16.0"/>
<polyline class="fm-curve" points="55.0,12.5 56.5,15.9 58.0,19.2 59.5,22.5 61.0,25.8 62.5,29.1 64.0,32.3 65.5,35.5 67.0,38.7 68.5,41.9 70.0,45.1 71.5,48.2 73.0,51.3 74.5,54.4 76.0,57.4 77.5,60.5 79.0,63.5 80.5,66.5 82.0,69.4 83.5,72.4 85.0,75.3 86.5,78.2 88.0,81.1 89.5,83.9 91.0,86.8 92.5,89.6 94.0,92.3 95.5,95.1 97.0,97.8 98.5,100.6 100.0,103.3 101.5,105.9 103.0,108.6 104.5,111.2 106.0,113.8 107.5,116.4 109.0,118.9 110.5,121.5 112.0,124.0 113.5,126.5 115.0,128.9 116.5,131.4 118.0,133.8 119.5,136.2 121.0,138.6 122.5,140.9 124.0,143.3 125.5,145.6 127.0,147.9 128.5,150.1 130.0,152.4 131.5,154.6 133.0,156.8 134.5,158.9 136.0,161.1 137.5,163.2 139.0,165.3 140.5,167.4 142.0,169.5 143.5,171.5 145.0,173.5 146.5,175.5 148.0,177.5 149.5,179.4 151.0,181.3 152.5,183.2 154.0,185.1 155.5,187.0 157.0,188.8 158.5,190.6 160.0,192.4 161.5,194.1 163.0,195.9 164.5,197.6 166.0,199.3 167.5,201.0 169.0,202.6 170.5,204.2 172.0,205.8 173.5,207.4 175.0,209.0 176.5,210.5 178.0,212.0 179.5,213.5 181.0,215.0 182.5,216.4 184.0,217.8 185.5,219.2 187.0,220.6 188.5,222.0 190.0,223.3 191.5,224.6 193.0,225.9 194.5,227.2 196.0,228.4 197.5,229.6 199.0,230.8 200.5,232.0 202.0,233.1 203.5,234.2 205.0,235.3 206.5,236.4 208.0,237.5 209.5,238.5 211.0,239.5 212.5,240.5 214.0,241.5 215.5,242.4 217.0,243.4 218.5,244.2 220.0,245.1 221.5,246.0 223.0,246.8 224.5,247.6 226.0,248.4 227.5,249.2 229.0,249.9 230.5,250.6 232.0,251.3 233.5,252.0 235.0,252.6 236.5,253.3 238.0,253.9 239.5,254.4 241.0,255.0 242.5,255.5 244.0,256.0 245.5,256.5 247.0,257.0 248.5,257.4 250.0,257.9 251.5,258.3 253.0,258.6 254.5,259.0 256.0,259.3 257.5,259.6 259.0,259.9 260.5,260.2 262.0,260.4 263.5,260.6 265.0,260.8 266.5,261.0 268.0,261.1 269.5,261.3 271.0,261.4 272.5,261.4 274.0,261.5 275.5,261.5 277.0,261.5 278.5,261.5 280.0,261.5 281.5,261.4 283.0,261.4 284.5,261.3 286.0,261.1 287.5,261.0 289.0,260.8 290.5,260.6 292.0,260.4 293.5,260.2 295.0,259.9 296.5,259.6 298.0,259.3 299.5,259.0 301.0,258.6 302.5,258.3 304.0,257.9 305.5,257.4 307.0,257.0 308.5,256.5 310.0,256.0 311.5,255.5 313.0,255.0 314.5,254.4 316.0,253.9 317.5,253.3 319.0,252.6 320.5,252.0 322.0,251.3 323.5,250.6 325.0,249.9 326.5,249.2 328.0,248.4 329.5,247.6 331.0,246.8 332.5,246.0 334.0,245.1 335.5,244.2 337.0,243.4 338.5,242.4 340.0,241.5 341.5,240.5 343.0,239.5 344.5,238.5 346.0,237.5 347.5,236.4 349.0,235.3 350.5,234.2 352.0,233.1 353.5,232.0 355.0,230.8 356.5,229.6 358.0,228.4 359.5,227.2 361.0,225.9 362.5,224.6 364.0,223.3 365.5,222.0 367.0,220.6 368.5,219.2 370.0,217.8 371.5,216.4 373.0,215.0 374.5,213.5 376.0,212.0 377.5,210.5 379.0,209.0 380.5,207.4 382.0,205.8 383.5,204.2 385.0,202.6 386.5,201.0 388.0,199.3 389.5,197.6 391.0,195.9 392.5,194.1 394.0,192.4 395.5,190.6 397.0,188.8 398.5,187.0 400.0,185.1 401.5,183.2 403.0,181.3 404.5,179.4 406.0,177.5 407.5,175.5 409.0,173.5 410.5,171.5 412.0,169.5 413.5,167.4 415.0,165.3 416.5,163.2 418.0,161.1 419.5,158.9 421.0,156.8 422.5,154.6 424.0,152.4 425.5,150.1 427.0,147.9 428.5,145.6 430.0,143.3 431.5,140.9 433.0,138.6 434.5,136.2 436.0,133.8 437.5,131.4 439.0,128.9 440.5,126.5 442.0,124.0 443.5,121.5 445.0,118.9 446.5,116.4 448.0,113.8 449.5,111.2 451.0,108.6 452.5,105.9 454.0,103.3 455.5,100.6 457.0,97.8 458.5,95.1 460.0,92.3 461.5,89.6 463.0,86.8 464.5,83.9 466.0,81.1 467.5,78.2 469.0,75.3 470.5,72.4 472.0,69.4 473.5,66.5 475.0,63.5 476.5,60.5 478.0,57.4 479.5,54.4 481.0,51.3 482.5,48.2 484.0,45.1 485.5,41.9 487.0,38.7 488.5,35.5 490.0,32.3 491.5,29.1 493.0,25.8 494.5,22.5 496.0,19.2 497.5,15.9 499.0,12.5"/>
<circle class="fm-pt2" cx="187.0" cy="220.6" r="4.5"/>
<circle class="fm-pt2" cx="367.0" cy="220.6" r="4.5"/>
<circle class="fm-pt" cx="277.0" cy="261.5" r="4.5"/>
<text class="fm-t" x="287.0" y="279.5" text-anchor="start">sommet (2 ; −2)</text>
<text class="fm-t" x="175.0" y="212.6" text-anchor="end">1</text>
<text class="fm-t" x="379.0" y="212.6" text-anchor="start">3</text>
<text class="fm-t" x="285.0" y="36.5" text-anchor="start">axe de symétrie x = 2</text>
</svg>
<figcaption>Courbe de f(x) = 2x² − 8x + 6 : deux zéros (1 et 3), un minimum au sommet, une symétrie autour de x = 2.</figcaption>
</figure>

Ce qu'il faut savoir lire sur la parabole :

- **Le sens.** Si \(a > 0\), la parabole est « ouverte vers le haut » : elle a un **minimum**. Si \(a < 0\), elle est ouverte vers le bas : elle a un **maximum**.
- **Le sommet.** Il est à l'abscisse \(x_S = -\dfrac{b}{2a}\), et la courbe est **symétrique** autour de la droite verticale \(x = x_S\).
- **Les zéros** (les solutions de \(f(x) = 0\)), s'il y en a : on calcule le **discriminant** \(\Delta = b^2 - 4ac\).
    - Si \(\Delta > 0\) : deux solutions \(x = \dfrac{-b - \sqrt{\Delta}}{2a}\) et \(x = \dfrac{-b + \sqrt{\Delta}}{2a}\).
    - Si \(\Delta = 0\) : une seule solution \(x = -\dfrac{b}{2a}\).
    - Si \(\Delta < 0\) : aucune solution réelle (la courbe ne coupe pas l'axe des abscisses).

**Exemple résolu.** Étudier \(f(x) = 2x^2 - 8x + 6\) (la parabole de la figure).

<details markdown="1">
<summary>Voir la solution</summary>

Ici \(a = 2\), \(b = -8\), \(c = 6\).

1. Comme \(a > 0\), la parabole est ouverte vers le haut : il y a un minimum.
2. Le sommet est à \(x_S = -\dfrac{-8}{2 \times 2} = 2\), avec \(f(2) = 8 - 16 + 6 = -2\). Le minimum vaut \(-2\), atteint en \(x = 2\).
3. Discriminant : \(\Delta = (-8)^2 - 4 \times 2 \times 6 = 64 - 48 = 16 > 0\), donc deux zéros : \(x = \dfrac{8 - 4}{4} = 1\) et \(x = \dfrac{8 + 4}{4} = 3\).

**Contrôle avec la figure :** les zéros sont symétriques autour de 2 (1 et 3), et le sommet est bien en \((2\,;\,-2)\).

</details>

## 5. La fonction inverse : quand une grandeur diminue si l'autre augmente

**Situation.** Un fichier de 1 200 Mo est transféré à un débit \(d\) (en Mo/s). La durée vaut \(t(d) = \dfrac{1200}{d}\).

| Débit \(d\) (Mo/s) | 10 | 20 | 40 | 120 |
|---|---|---|---|---|
| Durée \(t\) (s) | 120 | 60 | 30 | 10 |

Quand le débit **double**, la durée est **divisée par deux** : c'est le comportement de la fonction inverse \(x \mapsto \dfrac{k}{x}\) (avec \(k > 0\) et \(x > 0\)). Elle est **décroissante** : plus \(x\) est grand, plus la valeur est petite, sans jamais atteindre 0.

> [!WARNING]
> **Piège.** On ne peut pas diviser par 0 : \(\dfrac{k}{x}\) n'a pas de sens pour \(x = 0\). Ici, un débit nul n'aurait d'ailleurs aucun sens non plus : la situation exclut cette valeur d'elle-même. On ne te demandera pas de chercher des domaines de définition en général, mais **tu dois toujours te demander si la valeur a un sens pour le problème**.

## 6. Comparer deux modèles

Souvent, on hésite entre deux offres. La méthode est toujours la même.

1. Écrire une fonction pour chaque offre.
2. Chercher quand elles **coïncident** : on résout \(f(x) = g(x)\).
3. Regarder de chaque côté de cette valeur quelle offre est la moins chère.
4. **Interpréter** : si \(x\) est un nombre entier d'objets, la solution doit être entière.

**Exemple résolu.** Offre A : \(A(x) = 40 + 2{,}5x\). Offre B : \(B(x) = 6x\), pour \(x\) machines.

<details markdown="1">
<summary>Voir la solution</summary>

**Point de rencontre.** \(40 + 2{,}5x = 6x\) équivaut à \(40 = 3{,}5x\), donc \(x = \dfrac{40}{3{,}5} \approx 11{,}43\).

**Comparaison.** L'offre B n'a pas de frais fixes mais un prix unitaire plus élevé : pour peu de machines elle est la moins chère, pour beaucoup l'offre A l'est. Contrôle sur deux valeurs : pour \(x = 8\), \(A = 60\) et \(B = 48\) (B gagne) ; pour \(x = 20\), \(A = 90\) et \(B = 120\) (A gagne).

**Interprétation.** Le nombre de machines est entier, donc la solution \(11{,}43\) ne se lit pas telle quelle : \(x = 11\) donne \(A = 67{,}5\) et \(B = 66\) (B moins chère) ; \(x = 12\) donne \(A = 70\) et \(B = 72\) (A moins chère). L'offre A est la moins chère **à partir de 12 machines**.

</details>

## 7. Composer deux fonctions : enchaîner deux transformations

Parfois, le résultat d'une fonction sert d'entrée à une autre. Un article coûte \(x\) euros HT. On applique d'abord la TVA à 20 % (\(g(x) = 1{,}2x\)), puis une remise de 10 € (\(f(x) = x - 10\)).

\[
x \xrightarrow{\;g\;} 1{,}2x \xrightarrow{\;f\;} 1{,}2x - 10.
\]

On note \(f \circ g\) (lire « \(f\) rond \(g\) ») la fonction « d'abord \(g\), puis \(f\) » : \((f \circ g)(x) = f(g(x))\).

> [!WARNING]
> **L'ordre compte.** En général, \(f \circ g \ne g \circ f\). Ici, \(g \circ f\) correspond à la remise **avant** la TVA : \((g \circ f)(x) = 1{,}2(x - 10)\). Pour \(x = 100\) : \((f \circ g)(100) = 110\) mais \((g \circ f)(100) = 108\). Les deux ne donnent pas le même prix.

**Méthode.** Pour calculer \(f(g(x))\), on **remplace** dans \(f\) la variable par l'expression de \(g(x)\), en la mettant entre parenthèses.

**Exemple résolu.** Avec \(f(x) = x + 3\) et \(g(x) = x^2\), donner \(f \circ g\) et \(g \circ f\).

<details markdown="1">
<summary>Voir la solution</summary>

\((f \circ g)(x) = f(x^2) = x^2 + 3\) et \((g \circ f)(x) = g(x + 3) = (x + 3)^2\).

En \(x = 2\), on trouve \(7\) et \(25\) : les deux sont bien différentes.

</details>

## 8. Valider un résultat : le réflexe qui fait gagner des points

Un résultat numérique n'est pas fini tant qu'on ne l'a pas **interprété**. Avant de conclure :

1. **L'unité** est-elle donnée ? (euros, Mo/s, heures…)
2. **L'ordre de grandeur** est-il plausible ? (un temps de transfert de 3 jours pour 1 Go est suspect)
3. **La valeur est-elle acceptable ?** Une solution négative, non entière alors qu'il s'agit d'objets, ou hors de l'intervalle étudié, se **rejette** ou se **discute**.
4. **Un contrôle** : on remplace dans l'énoncé de départ.

## 9. À retenir

> [!NOTE]
> - Une fonction associe à chaque valeur de la variable **une seule** image ; elle se donne par formule, tableau ou courbe.
> - Affine \(ax + b\) : droite, pente \(a\) (variation par unité), ordonnée à l'origine \(b\) (valeur de départ).
> - Second degré : parabole, sommet en \(-\dfrac{b}{2a}\), zéros par \(\Delta = b^2 - 4ac\).
> - Inverse \(\dfrac{k}{x}\) : décroissante pour \(x > 0\).
> - Comparer deux modèles : résoudre \(f(x) = g(x)\), puis **discuter** la solution.
> - \(f \circ g\) : d'abord \(g\), puis \(f\) ; l'ordre change le résultat.
> - Toujours **valider** : unité, ordre de grandeur, valeur acceptable.

## 10. Teste-toi

**Question 1.** Pour \(f(x) = 3x - 2\), calculer \(f(4)\) et trouver l'antécédent de 10.

**Question 2.** Une fonction affine vaut 5 en \(x = 0\) et 11 en \(x = 3\). Donner sa formule.

**Question 3.** Combien de zéros a \(x^2 + 2x + 5\) ?

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(f(4) = 12 - 2 = 10\). L'antécédent de 10 vérifie \(3x - 2 = 10\), donc \(x = 4\) (et on retrouve \(f(4) = 10\)).
2. Pente \(\dfrac{11 - 5}{3 - 0} = 2\) et \(b = 5\), donc \(f(x) = 2x + 5\).
3. \(\Delta = 4 - 20 = -16 < 0\) : **aucun** zéro réel. La parabole est au-dessus de l'axe des abscisses.

</details>

**Pour continuer :** [cours 2 sur l'exponentielle et le logarithme](02-exponentielle-et-logarithme.md), puis les [exercices du module](03-exercices.md).

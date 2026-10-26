# Cours 1 – Variable aléatoire et loi binomiale

*BTS SIO SISR 2e année – Option mathématiques approfondies – M4, première partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : définir une **variable aléatoire** discrète et sa loi ; calculer **espérance, variance, écart type** ; reconnaître une situation de **loi binomiale** ; calculer \(P(X = k)\), \(P(X \le k)\), \(P(X \ge k)\) à la calculatrice ; **interpréter** une probabilité en langage courant.
>
> **Prérequis.** Probabilités de première année (événement, probabilité d'un événement contraire), le [module M1](../M1-fonctions/01-fonctions-et-modeles.md) pour les puissances.
>
> **Programme.** Le théorème central limite et les distributions d'échantillonnage ne sont pas au programme de l'option.

## 1. Pour démarrer : un risque chiffré

Un incident sur un système d'information coûte \(0\) € (incident sans conséquence) avec la probabilité \(0{,}7\), \(1\,000\) € avec la probabilité \(0{,}2\), et \(5\,000\) € avec la probabilité \(0{,}1\). Quel est le **coût moyen** par incident ? Quelle est l'**incertitude** autour de ce coût ?

Pour répondre, on traduit la situation avec une **variable aléatoire**.

## 2. Variable aléatoire discrète et sa loi

**Définition.** Une **variable aléatoire** \(X\) associe un **nombre** à chaque issue d'une expérience aléatoire (le coût d'un incident, le nombre de pannes, le nombre de paquets perdus). Elle est **discrète** quand ses valeurs possibles sont isolées (0, 1, 2, ...).

**Loi de probabilité.** C'est le tableau des valeurs \(x_i\) et de leurs probabilités \(p_i = P(X = x_i)\). Leur somme vaut **toujours 1**.

| Coût \(x_i\) (€) | 0 | 1 000 | 5 000 |
|---|---|---|---|
| \(p_i\) | 0,7 | 0,2 | 0,1 |

Contrôle : \(0{,}7 + 0{,}2 + 0{,}1 = 1\) ✔.

**L'espérance** \(E(X)\) est la **valeur moyenne à long terme** si on répète l'expérience très souvent :

\[
E(X) = \sum p_i\,x_i = 0 \times 0{,}7 + 1000 \times 0{,}2 + 5000 \times 0{,}1 = 700.
\]

**La variance** et **l'écart type** mesurent la dispersion autour de l'espérance :

\[
V(X) = \sum p_i\,x_i^{2} - E(X)^{2}, \qquad \sigma(X) = \sqrt{V(X)}.
\]

Ici \(\sum p_i x_i^2 = 0{,}2 \times 10^{6} + 0{,}1 \times 25 \times 10^{6} = 2\,700\,000\), donc \(V = 2\,700\,000 - 700^2 = 2\,210\,000\) et \(\sigma \approx 1\,487\) €.

**Interprétation.** Un incident coûte **en moyenne 700 €**, mais l'écart type (1 487 €) est plus de **deux fois la moyenne** : le coût réel d'un incident est très variable, et un seul gros incident (5 000 €) pèse lourd. Savoir le dire en une phrase est attendu à l'épreuve.

## 3. Compter des succès : l'épreuve de Bernoulli et la loi binomiale

### Une expérience à deux issues

Une **épreuve de Bernoulli** n'a que deux issues : le **succès** (probabilité \(p\)) et l'**échec** (probabilité \(1 - p\)). Exemple : un disque est défectueux (succès, au sens « l'événement qu'on étudie ») avec la probabilité \(p = 0{,}03\).

### On répète

Un lot de 20 disques : on répète 20 fois l'épreuve, dans des **conditions identiques** et **indépendantes**. La variable \(X\) qui **compte le nombre de succès** (disques défectueux) suit la **loi binomiale** de paramètres \(n = 20\) et \(p = 0{,}03\), notée \(\mathcal{B}(20\,;\,0{,}03)\).

> [!WARNING]
> **Les trois conditions à vérifier avant d'écrire « loi binomiale ».**
> 1. Il y a un nombre **fixé** \(n\) d'épreuves ;
> 2. chaque épreuve a **deux issues** (succès ou échec) ;
> 3. la probabilité de succès \(p\) est la **même** à chaque épreuve et les épreuves sont **indépendantes**.
>
> Si les disques sortaient tous du même mauvais lot de fabrication, les pannes ne seraient plus indépendantes : le modèle ne conviendrait plus.

### La formule

\[
P(X = k) = \binom{n}{k}\,p^{k}\,(1 - p)^{n - k}.
\]

Le coefficient \(\binom{n}{k}\) (« \(k\) parmi \(n\) ») est le **nombre de façons de placer** \(k\) succès parmi \(n\) épreuves. La calculatrice le donne (touche **nCr**).

**Pourquoi cette formule ?** Chaque configuration avec \(k\) succès et \(n-k\) échecs a la probabilité \(p^{k}(1-p)^{n-k}\) (par indépendance), et il y a \(\binom{n}{k}\) configurations différentes.

**Espérance et écart type.**

\[
E(X) = np, \qquad V(X) = np(1 - p).
\]

**Exemple résolu.** Pour \(X \sim \mathcal{B}(20\,;\,0{,}03)\), calculer \(P(X = 0)\), \(P(X = 1)\), \(P(X \ge 2)\), \(E(X)\) et \(\sigma(X)\).

<details markdown="1">
<summary>Voir la solution détaillée</summary>

**\(P(X = 0)\)** : aucun disque défectueux. \(\binom{20}{0} = 1\), donc \(P(X = 0) = 0{,}97^{20} \approx 0{,}5438\).

**\(P(X = 1)\)** : \(\binom{20}{1} = 20\), donc \(P(X = 1) = 20 \times 0{,}03 \times 0{,}97^{19} \approx 0{,}3364\).

**\(P(X \ge 2)\)** : on passe par l'événement contraire, bien plus rapide que de sommer toutes les valeurs de 2 à 20 :

\[
P(X \ge 2) = 1 - P(X \le 1) = 1 - (0{,}5438 + 0{,}3364) \approx 0{,}1198.
\]

**Espérance et écart type.** \(E(X) = 20 \times 0{,}03 = 0{,}6\) ; \(V(X) = 20 \times 0{,}03 \times 0{,}97 = 0{,}582\) ; \(\sigma \approx 0{,}763\).

**Interprétation.** Dans un lot de 20 disques, on trouve **en moyenne 0,6 disque défectueux**. Il y a environ **54 % de chances qu'aucun** ne soit défectueux, et environ **12 % de chances d'en avoir au moins deux**.

</details>

<figure class="fig-math">
<svg viewBox="0 0 520 320" role="img" aria-label="Loi binomiale B(20 ; 0,03)">
<line class="fm-grid" x1="52" y1="282.0" x2="502" y2="282.0"/>
<text class="fm-t" x="46" y="286.0" text-anchor="end">0,0</text>
<line class="fm-grid" x1="52" y1="200.2" x2="502" y2="200.2"/>
<text class="fm-t" x="46" y="204.2" text-anchor="end">0,2</text>
<line class="fm-grid" x1="52" y1="118.3" x2="502" y2="118.3"/>
<text class="fm-t" x="46" y="122.3" text-anchor="end">0,4</text>
<line class="fm-grid" x1="52" y1="36.5" x2="502" y2="36.5"/>
<text class="fm-t" x="46" y="40.5" text-anchor="end">0,6</text>
<line class="fm-grid" x1="95.5" y1="16" x2="95.5" y2="282"/>
<text class="fm-t" x="95.5" y="298" text-anchor="middle">0</text>
<line class="fm-grid" x1="168.1" y1="16" x2="168.1" y2="282"/>
<text class="fm-t" x="168.1" y="298" text-anchor="middle">1</text>
<line class="fm-grid" x1="240.7" y1="16" x2="240.7" y2="282"/>
<text class="fm-t" x="240.7" y="298" text-anchor="middle">2</text>
<line class="fm-grid" x1="313.3" y1="16" x2="313.3" y2="282"/>
<text class="fm-t" x="313.3" y="298" text-anchor="middle">3</text>
<line class="fm-grid" x1="385.9" y1="16" x2="385.9" y2="282"/>
<text class="fm-t" x="385.9" y="298" text-anchor="middle">4</text>
<line class="fm-grid" x1="458.5" y1="16" x2="458.5" y2="282"/>
<text class="fm-t" x="458.5" y="298" text-anchor="middle">5</text>
<line class="fm-axis" x1="52" y1="282.0" x2="502" y2="282.0"/>
<line class="fm-axis" x1="52.0" y1="16" x2="52.0" y2="282"/>
<text class="fm-t fm-i" x="502" y="314" text-anchor="end">k (disques défectueux)</text>
<text class="fm-t fm-i" x="56" y="24">probabilité</text>
<rect class="fm-bar" x="70.1" y="59.5" width="50.8" height="222.5"/>
<text class="fm-t" x="95.5" y="54.5" text-anchor="middle">0,5438</text>
<rect class="fm-bar" x="142.7" y="144.3" width="50.8" height="137.7"/>
<text class="fm-t" x="168.1" y="139.3" text-anchor="middle">0,3364</text>
<rect class="fm-bar" x="215.3" y="241.6" width="50.8" height="40.4"/>
<text class="fm-t" x="240.7" y="236.6" text-anchor="middle">0,0988</text>
<rect class="fm-bar" x="287.9" y="274.5" width="50.8" height="7.5"/>
<text class="fm-t" x="313.3" y="269.5" text-anchor="middle">0,0183</text>
<rect class="fm-bar" x="360.5" y="281.0" width="50.8" height="1.0"/>
<text class="fm-t" x="385.9" y="276.0" text-anchor="middle">0,0024</text>
<rect class="fm-bar" x="433.0" y="281.9" width="50.8" height="0.1"/>
<text class="fm-t" x="458.5" y="276.9" text-anchor="middle">0,0002</text>
</svg>
<figcaption>Loi binomiale B(20 ; 0,03) pour k de 0 à 5 : presque toute la probabilité est sur les petites valeurs de k.</figcaption>
</figure>

La figure montre que presque toute la probabilité est concentrée sur les petites valeurs de \(k\).

> [!TIP]
> **Le réflexe « au moins ».** Pour \(P(X \ge k)\), calcule \(1 - P(X \le k - 1)\). Attention à l'**erreur d'un cran** : « au moins 2 » est le contraire de « au plus 1 ».

## 4. Calculer avec la calculatrice ou Python

La calculatrice propose deux fonctions : la valeur ponctuelle \(P(X = k)\) et la **répartition** \(P(X \le k)\) (voir l'[aide-mémoire](../aide-memoire-calculatrice.md)).

```python
from math import comb

def binom_pmf(n, p, k):
    return comb(n, k) * p**k * (1 - p)**(n - k)

print(binom_pmf(20, 0.03, 0))                          # 0.5437...
print(1 - binom_pmf(20, 0.03, 0) - binom_pmf(20, 0.03, 1))   # 0.1198...
```

## 5. À retenir

> [!NOTE]
> - Une variable aléatoire \(X\) a une loi : valeurs \(x_i\) et probabilités \(p_i\) de somme 1.
> - \(E(X) = \sum p_i x_i\) ; \(V(X) = \sum p_i x_i^2 - E(X)^2\) ; \(\sigma = \sqrt{V}\).
> - \(\mathcal{B}(n\,;\,p)\) : nombre de succès sur \(n\) épreuves **indépendantes** de même probabilité \(p\).
> - \(P(X = k) = \binom{n}{k}p^{k}(1-p)^{n-k}\) ; \(E = np\) ; \(V = np(1-p)\).
> - \(P(X \ge k) = 1 - P(X \le k - 1)\).
> - Toujours **interpréter** en une phrase (« au moins une chance sur dix »).

## 6. Teste-toi

**Question 1.** On lance 5 fois une pièce équilibrée. Quelle est la probabilité d'obtenir exactement 2 « face » ? Au moins un « face » ?

**Question 2.** Une variable aléatoire prend les valeurs \(-1\), \(0\) et \(2\) avec les probabilités \(0{,}3\), \(0{,}5\), \(0{,}2\). Calculer \(E(X)\).

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(X \sim \mathcal{B}(5\,;\,0{,}5)\). \(P(X = 2) = \binom{5}{2}0{,}5^{2}0{,}5^{3} = 10 \times \dfrac{1}{32} = 0{,}3125\). \(P(X \ge 1) = 1 - P(X = 0) = 1 - 0{,}5^{5} = 0{,}96875\).
2. \(E(X) = -1 \times 0{,}3 + 0 \times 0{,}5 + 2 \times 0{,}2 = -0{,}3 + 0{,}4 = 0{,}1\).

</details>

**Pour continuer :** le [cours 2 sur les lois de Poisson et normale](02-poisson-et-normale.md).

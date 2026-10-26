# Cours – Sommes et applications : intérêts, emprunt, croissance de données

*BTS SIO SISR 2e année – Pour aller plus loin – S04 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S02 et S03 (suites arithmétiques et géométriques, sommes).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Calculer** des intérêts simples et composés ;
- [ ] **Calculer** un capital d'épargne à versements réguliers ;
- [ ] **Calculer** la mensualité d'un emprunt et un tableau d'amortissement ;
- [ ] **Prévoir** l'évolution d'un volume de données ;
- [ ] **Choisir** le bon modèle et le programmer.

## I. Intérêts simples et composés

Un capital \(C_0\) placé au taux \(t\) par période (par exemple \(t = 0{,}03\) pour 3 %) :

| Type | Principe | Suite | Formule |
|---|---|---|---|
| **Intérêts simples** | les intérêts sont calculés toujours sur \(C_0\) | arithmétique, \(r = C_0\,t\) | \(C_n = C_0\,(1 + n\,t)\) |
| **Intérêts composés** | les intérêts s'ajoutent au capital et produisent des intérêts | géométrique, \(q = 1 + t\) | \(C_n = C_0\,(1 + t)^n\) |

Exemple : 10 000 € à 3 % pendant 5 ans. Simples : \(10\,000 \times (1 + 0{,}15) = 11\,500\) €. Composés : \(10\,000 \times 1{,}03^5 \approx 11\,592{,}74\) €.

## II. Épargne à versements réguliers

On verse \(v\) à la **fin** de chaque période, au taux \(t\). Le capital après \(n\) versements est la somme d'une suite géométrique :

\[ V_n = v\,\big(1 + (1+t) + \dots + (1+t)^{n-1}\big) = v\,\frac{(1+t)^n - 1}{t} \]

Exemple : 1 000 € par an à 4 % pendant 5 ans : \(1\,000 \times \dfrac{1{,}04^5 - 1}{0{,}04} \approx 5\,416{,}32\) €.

Le dernier versement ne produit pas d'intérêts, d'où l'exposant \(n - 1\) pour le premier terme de la somme.

## III. Emprunt à mensualités constantes

On emprunte \(C\) au taux \(t\) **par mois**, remboursé en \(n\) mensualités égales \(M\). Le capital restant dû \(K_k\) après \(k\) mois vérifie la récurrence

\[ K_0 = C, \qquad K_{k+1} = K_k\,(1 + t) - M \]

On choisit \(M\) pour que \(K_n = 0\). On obtient :

\[ M = \frac{C\,t}{1 - (1+t)^{-n}} \]

Exemple : \(C = 12\,000\) €, \(t = 0{,}5\,\%\) par mois, \(n = 24\) mois : \(M \approx 531{,}85\) €. Le coût des intérêts est \(24 M - C \approx 764{,}34\) €.

**Tableau d'amortissement** : chaque mois, intérêts \(= K_k \, t\), amortissement \(= M -\) intérêts, nouveau capital restant dû \(= K_k -\) amortissement.

| Mois | Intérêts | Amortissement | Capital restant dû |
|---|---|---|---|
| 1 | 60,00 | 471,85 | 11 528,15 |
| 2 | 57,64 | 474,21 | 11 053,95 |
| 3 | 55,27 | 476,58 | 10 577,37 |

Les intérêts diminuent, l'amortissement augmente, la mensualité reste constante.

> [!WARNING]
> Un taux **annuel** n'est pas divisé par 12 sans précaution : on utilise le taux **mensuel** fourni par l'énoncé (ou la banque). Les arrondis à chaque ligne peuvent laisser quelques centimes d'écart au dernier mois.

## IV. Croissance de données

Un volume de données qui grossit à la fois d'un pourcentage et d'un ajout fixe suit \(u_{n+1} = (1 + t)\,u_n + a\). Ce n'est ni arithmétique ni géométrique : on le **simule** par une boucle.

Exemple : \(u_0 = 200\) Go, \(t = 10\,\%\), \(a = 50\) Go par mois : \(u_1 = 270\), \(u_2 = 347\), \(u_3 = 431{,}7\), \(u_4 \approx 524{,}87\).

## V. Quel modèle ?

| Phénomène | Modèle |
|---|---|
| Ajout d'une quantité fixe | arithmétique |
| Évolution en pourcentage | géométrique |
| Pourcentage **et** ajout fixe (emprunt, stockage) | récurrence \(u_{n+1} = q\,u_n + a\), simulée |

**Test flash.** À taux égal, quel placement rapporte le plus à long terme, simples ou composés ?

<details markdown="1">
<summary>Voir la réponse</summary>

Les **composés** : la croissance est géométrique, donc finit par dépasser la croissance linéaire des intérêts simples (dès la 2e période, \(1 + 2t + t^2 > 1 + 2t\)).

</details>

## À retenir

- Simples : \(C_0(1 + nt)\) (arithmétique) ; composés : \(C_0(1 + t)^n\) (géométrique).
- Épargne : \(v\,\dfrac{(1+t)^n - 1}{t}\) ; emprunt : \(M = \dfrac{Ct}{1 - (1+t)^{-n}}\).
- Emprunt : \(K_{k+1} = K_k(1 + t) - M\) ; intérêts du mois \(= K_k\,t\).
- Mélange pourcentage + ajout : on simule.

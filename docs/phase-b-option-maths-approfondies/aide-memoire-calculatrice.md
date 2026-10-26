# Aide-mémoire calculatrice

*BTS SIO SISR 2e année – Option mathématiques approfondies*

> [!NOTE]
> **Comment s'en servir.** Les trois grandes familles de calculatrices (NumWorks, Casio Graph, TI-83/84) font les mêmes calculs sous des **noms différents**. Cette fiche donne, pour chaque calcul du parcours, le **nom de la fonction** et **l'ordre des paramètres**. Les chemins de menu varient selon le modèle et la version du système : repère le nom de la fonction, puis cherche-le dans les menus de ta calculatrice. Une colonne **Python** est aussi donnée : elle fonctionne partout et sert de contrôle.

## 1. Statistique descriptive (M3)

| Calcul | NumWorks | Casio Graph | TI-83/84 |
|---|---|---|---|
| Saisir la série | application **Statistiques**, colonne de valeurs | menu **STAT**, liste (List 1) | touche **stats**, **Modifier**, liste L1 |
| Moyenne, écart type, médiane, quartiles | onglet des statistiques de la série | **CALC**, **1VAR** | **stats**, **CALC**, **Stats 1 Var** |
| Droite de régression \(y = ax + b\) et \(r\) | onglet de régression, modèle linéaire | **CALC**, **REG**, **X**, \(ax+b\) | **stats**, **CALC**, **RégLin(ax+b)** |

> [!WARNING]
> **Écart type : lequel ?** Les calculatrices affichent deux écarts types : celui de la population (noté \(\sigma_x\), division par \(n\)) et celui de l'échantillon (\(s_x\), division par \(n - 1\)). Le parcours utilise \(\sigma_x\) (division par \(n\)). Les **quartiles** peuvent aussi différer d'une calculatrice à l'autre selon la convention ; on garde celle de l'énoncé.

> [!TIP]
> **Coefficient de corrélation.** Sur TI, le \(r\) n'apparaît que si l'option de diagnostic est activée (réglages de la calculatrice, « Diagnostic activé »). Sur les autres, il s'affiche avec la régression.

## 2. Lois de probabilité (M4 et M5)

Chaque fonction existe en deux versions : **densité ou valeur ponctuelle** \(P(X = k)\) et **répartition cumulée** \(P(X \le k)\).

| Calcul | NumWorks | Casio Graph (STAT, **DIST**) | TI-83/84 (**2nde** puis **distrib**) |
|---|---|---|---|
| Binomiale \(P(X = k)\) | loi **Binomiale**, paramètres \(n\) et \(p\) | **BINM**, **Bpd** : \(k\), \(n\), \(p\) | **binomFdp** : \(n\), \(p\), \(k\) |
| Binomiale \(P(X \le k)\) | idem, borne \(\le k\) | **BINM**, **Bcd** : \(k\), \(n\), \(p\) | **binomFRép** : \(n\), \(p\), \(k\) |
| Poisson \(P(X = k)\) | loi **Poisson**, paramètre \(\lambda\) | **POISSON**, **Ppd** : \(k\), \(\lambda\) | **poissonFdp** : \(\lambda\), \(k\) |
| Poisson \(P(X \le k)\) | idem, borne \(\le k\) | **POISSON**, **Pcd** : \(k\), \(\lambda\) | **poissonFRép** : \(\lambda\), \(k\) |
| Normale \(P(a \le X \le b)\) | loi **Normale**, paramètres \(m\) et \(\sigma\), bornes \(a\) et \(b\) | **NORM**, **Ncd** : \(a\), \(b\), **\(\sigma\)**, **\(m\)** | **normalFRép** : \(a\), \(b\), \(m\), \(\sigma\) |
| Normale inverse : \(t\) avec \(P(X \le t) = p\) | choisir la borne et saisir la probabilité | **NORM**, **InvN** : aire, \(\sigma\), \(m\) | **FracNormale** : \(p\), \(m\), \(\sigma\) |
| Exponentielle | à calculer avec la formule \(1 - e^{-\lambda t}\) | formule \(1 - e^{-\lambda t}\) | formule \(1 - e^{-\lambda t}\) |

> [!WARNING]
> **Pièges de saisie.**
>
> - L'**ordre des paramètres change** d'une marque à l'autre. Sur Casio, la normale demande \(\sigma\) **avant** \(m\) ; sur TI, c'est \(m\) puis \(\sigma\).
> - Pour une borne « infinie », saisis une grande valeur (par exemple \(m + 10\sigma\), ou \(-10^{99}\) et \(10^{99}\) sur TI).
> - Pour \(P(X \ge k)\), calcule \(1 - P(X \le k - 1)\) : l'erreur d'un cran est la plus fréquente.

## 3. Fonctions, dérivées, intégrales (M1 et M2)

| Calcul | NumWorks | Casio Graph | TI-83/84 |
|---|---|---|---|
| Tableau de valeurs | application **Fonctions**, tableau | menu **TABLE** | **tableau** (table) |
| Courbe, maximum, minimum | application **Fonctions**, graphique, recherche d'extremum | menu **GRAPH**, **G-Solve**, **MAX** ou **MIN** | **calculs** (touche **2nde** puis **trace**), **maximum** ou **minimum** |
| Résoudre \(f(x) = k\) | recherche d'intersection dans le graphique | **G-Solve**, **ISCT** | **calculs**, **intersection** |
| Dérivée en un point | application **Calculs**, fonction de dérivation | menu **RUN-MAT**, dérivée numérique | **math**, **nbreDérivé** |
| Intégrale \(\displaystyle\int_a^b f(x)\,dx\) | application **Calculs**, fonction d'intégration | menu **RUN-MAT**, intégrale numérique | **math**, **fonctionIntégrale** (ou **calculs**, \(\int f(x)dx\) sur le graphique) |

La calculatrice formelle (NumWorks, Casio ClassPad, TI-Nspire CX CAS) donne aussi dérivées et primitives **exactes** ; le référentiel demande de **justifier une primitive par dérivation**, pas de la lire.

## 4. Valeurs de contrôle

Avant un exercice, vérifie ta saisie sur une valeur connue. Ces résultats viennent des exercices du parcours.

| Calcul | Résultat attendu |
|---|---|
| \(P(X = 0)\), \(X \sim \mathcal{B}(20\,;\,0{,}03)\) | \(0{,}5438\) |
| \(P(X \ge 2)\), même loi | \(0{,}1198\) |
| \(P(X = 3)\), \(X \sim \mathcal{P}(2)\) | \(0{,}1804\) |
| \(P(X \ge 5)\), même loi | \(0{,}0527\) |
| \(P(X \le 105)\), \(X \sim \mathcal{N}(100\,;\,8)\) | \(0{,}7340\) |
| \(P(90 \le X \le 110)\), même loi | \(0{,}7887\) |
| \(t\) tel que \(P(X \le t) = 0{,}95\), même loi | \(113{,}16\) |
| \(e^{-0{,}5}\) (fiabilité à 1 000 h, MTBF 2 000 h) | \(0{,}6065\) |
| Régression des 6 points de l'exercice 3 de M3 | \(a \approx 9{,}46\), \(b \approx 1{,}73\), \(r \approx 0{,}994\) |

## 5. Le même travail en Python

Ce petit module n'utilise que la bibliothèque standard (`math` et `statistics`, Python 3.10 ou plus). Il redonne **toutes** les valeurs de contrôle ci-dessus et sert à vérifier une calculatrice.

```python
from math import comb, exp, factorial, erf, sqrt
from statistics import mean, median, pstdev, linear_regression, correlation

def binom_pmf(n, p, k):
    return comb(n, k) * p**k * (1 - p)**(n - k)

def binom_cdf(n, p, k):
    return sum(binom_pmf(n, p, i) for i in range(k + 1))

def poisson_pmf(lam, k):
    return exp(-lam) * lam**k / factorial(k)

def poisson_cdf(lam, k):
    return sum(poisson_pmf(lam, i) for i in range(k + 1))

def normale_cdf(x, m, sigma):
    return 0.5 * (1 + erf((x - m) / (sigma * sqrt(2))))

def exp_fiabilite(lam, t):
    return exp(-lam * t)

def quantile_normale(p, m, sigma):
    bas, haut = m - 10 * sigma, m + 10 * sigma
    for _ in range(100):
        milieu = (bas + haut) / 2
        if normale_cdf(milieu, m, sigma) < p:
            bas = milieu
        else:
            haut = milieu
    return (bas + haut) / 2

def quartiles(valeurs):
    v = sorted(valeurs); n = len(v)
    return median(v[:n // 2]), median(v), median(v[(n + 1) // 2:])
```

Exemples d'utilisation :

```python
print(binom_pmf(20, 0.03, 0))            # 0.5437...
print(1 - binom_cdf(20, 0.03, 1))        # 0.1198...
print(poisson_pmf(2, 3))                 # 0.1804...
print(1 - poisson_cdf(2, 4))             # 0.0527...
print(normale_cdf(105, 100, 8))          # 0.7340...
print(quantile_normale(0.95, 100, 8))    # 113.16...
print(exp_fiabilite(1 / 2000, 1000))     # 0.6065...

x = [1, 2, 3, 4, 5, 6]
y = [12, 19, 31, 38, 52, 57]
r = linear_regression(x, y)
print(r.slope, r.intercept, correlation(x, y))   # 9.46  1.73  0.994
```

> [!TIP]
> **À l'examen.** Entraîne-toi sur **ta** calculatrice, celle que tu auras le jour de l'épreuve, jusqu'à retrouver les valeurs de contrôle sans hésiter. Ne découvre jamais un menu le jour de l'épreuve.

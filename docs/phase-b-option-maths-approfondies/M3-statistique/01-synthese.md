# Synthèse – Statistique descriptive

*BTS SIO SISR 2e année – Option mathématiques approfondies – M3*

> [!NOTE]
> **Idée directrice.** Résumer un grand nombre de mesures (temps de réponse, volumes, pannes) par quelques indicateurs fiables, repérer les valeurs aberrantes, et relier deux grandeurs par un **ajustement**.

## 1. Indicateurs de position

Pour des valeurs \(x_1, \dots, x_n\) :

- **Moyenne** : \(\bar{x} = \dfrac{x_1 + \dots + x_n}{n}\). Sensible aux valeurs extrêmes.
- **Médiane** : valeur qui partage la série ordonnée en deux moitiés de même effectif. **Robuste** aux valeurs extrêmes.
- **Quartiles** \(Q_1\), \(Q_3\) : médianes de la moitié inférieure et de la moitié supérieure. Plusieurs conventions existent : **indique celle que tu utilises** (ici, médiane de chaque moitié).

## 2. Indicateurs de dispersion

- **Étendue** : maximum moins minimum. **Écart interquartile** : \(Q_3 - Q_1\).
- **Variance** : \(V = \dfrac{1}{n}\sum (x_i - \bar{x})^2 = \overline{x^2} - \bar{x}^2\).
- **Écart type** : \(\sigma = \sqrt{V}\), exprimé dans la **même unité** que les données.

Pour une série en **classes**, on remplace chaque classe par son centre, pondéré par l'effectif.

> [!TIP]
> **Effet d'un changement d'unité.** Si \(y = ax + b\), alors \(\bar{y} = a\bar{x} + b\) et \(\sigma_y = |a|\,\sigma_x\) : le décalage \(b\) ne change pas la dispersion.

## 3. Série à deux variables, ajustement affine

On dispose de couples \((x_i, y_i)\). La **droite de régression** de \(y\) en \(x\) (méthode des moindres carrés) est \(y = ax + b\) avec \(a = \dfrac{\operatorname{cov}(x, y)}{V(x)}\) et \(b = \bar{y} - a\bar{x}\).

Le **coefficient de corrélation** \(r\) mesure la qualité de l'ajustement linéaire : proche de \(\pm 1\), l'ajustement est bon. Les calculs se font à la calculatrice ou en Python.

## 4. Ajustement par changement de variable

Si les points évoluent par **multiplication** (croissance exponentielle), on ajuste \(\ln y\) en fonction de \(x\) : on obtient \(\ln y = ax + b\), donc \(y = e^{b}\,(e^{a})^{x}\).

## 5. Prévoir, avec prudence

- **Interpolation** (dans l'intervalle observé) : raisonnable.
- **Extrapolation** (hors intervalle) : à manier avec précaution, et à signaler comme telle.
- Une corrélation n'est **pas** une causalité.

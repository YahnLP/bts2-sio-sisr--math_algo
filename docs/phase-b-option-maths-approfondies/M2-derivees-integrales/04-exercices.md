# Exercices – Calcul différentiel et intégral

*BTS SIO SISR 2e année – Option mathématiques approfondies – M2*

> [!NOTE]
> Trois niveaux : **socle**, **format épreuve**, **pour aller plus loin**. Les calculs sont élémentaires ; la rédaction et l'interprétation comptent.

## Niveau 1 – Socle

### Exercice 1 – Dériver

Dériver : \(f(x) = 3x^2 - 4x + 1\), \(g(x) = x e^{x}\), \(h(x) = \dfrac{\ln x}{x}\), \(k(x) = \dfrac{2x + 1}{x + 1}\).

<details markdown="1">
<summary>Voir la réponse</summary>

- \(f'(x) = 6x - 4\).
- \(g'(x) = e^{x} + x e^{x} = (1 + x)e^{x}\) (produit).
- \(h'(x) = \dfrac{\frac{1}{x} \cdot x - \ln x \cdot 1}{x^{2}} = \dfrac{1 - \ln x}{x^{2}}\) (quotient).
- \(k'(x) = \dfrac{2(x + 1) - (2x + 1)}{(x + 1)^{2}} = \dfrac{1}{(x + 1)^{2}}\).

</details>

### Exercice 2 – Justifier une primitive

Montrer que \(F(x) = x e^{x} - e^{x}\) est une primitive de \(f(x) = x e^{x}\), puis calculer \(\displaystyle\int_{0}^{1} x e^{x}\,dx\).

<details markdown="1">
<summary>Voir la réponse</summary>

On dérive : \(F'(x) = (e^{x} + x e^{x}) - e^{x} = x e^{x} = f(x)\). \(F\) est bien une primitive de \(f\).

Donc \(\displaystyle\int_{0}^{1} x e^{x}\,dx = F(1) - F(0) = (e - e) - (0 - 1) = 1\).

</details>

## Niveau 2 – Format épreuve

### Exercice 3 – Étude d'une fonction

Soit \(f(x) = x^3 - 6x^2 + 9x + 1\) sur \([0\,;\,5]\).

1. Calculer \(f'(x)\) et la factoriser.
2. Dresser le tableau de variations.
3. Quels sont le maximum et le minimum de \(f\) sur \([0\,;\,5]\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(f'(x) = 3x^2 - 12x + 9 = 3(x^2 - 4x + 3) = 3(x - 1)(x - 3)\).
2. Signe de \(f'\) : positif pour \(x < 1\), négatif pour \(1 < x < 3\), positif pour \(x > 3\).

| \(x\) | 0 | 1 | 3 | 5 |
|---|---|---|---|---|
| \(f'(x)\) | | \(+\) \(0\) \(-\) | \(0\) \(+\) | |
| \(f(x)\) | 1 | 5 | 1 | 21 |

Valeurs : \(f(0) = 1\), \(f(1) = 1 - 6 + 9 + 1 = 5\), \(f(3) = 27 - 54 + 27 + 1 = 1\), \(f(5) = 125 - 150 + 45 + 1 = 21\).

3. Le maximum sur \([0\,;\,5]\) est \(21\), atteint en \(x = 5\) (c'est un extremum de bord) ; le minimum est \(1\), atteint en \(x = 0\) et en \(x = 3\). Le point \(x = 1\) est un maximum **local** de valeur \(5\).

</details>

### Exercice 4 – Coût moyen minimal

Le coût moyen de production, en euros par unité, de \(q\) unités est \(CM(q) = q + \dfrac{100}{q}\) pour \(q > 0\).

1. Calculer \(CM'(q)\) et étudier son signe.
2. En déduire la quantité qui minimise le coût moyen et ce coût minimal.
3. Comparer avec \(CM(5)\) et \(CM(20)\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(CM'(q) = 1 - \dfrac{100}{q^2} = \dfrac{q^2 - 100}{q^2}\). Pour \(q > 0\), le signe est celui de \(q^2 - 100\) : négatif pour \(q < 10\), positif pour \(q > 10\).
2. \(CM\) décroît puis croît : le minimum est en \(q = 10\), avec \(CM(10) = 10 + 10 = 20\) euros par unité.
3. \(CM(5) = 5 + 20 = 25\) et \(CM(20) = 20 + 5 = 25\) : les deux sont supérieurs à 20, ce qui confirme le minimum. Produire 10 unités est la quantité optimale pour le coût moyen.

</details>

### Exercice 5 – Régime stable

Un service reçoit des requêtes selon le modèle \(f(x) = (x + 2)e^{-x}\), où \(x\) est le temps en heures après un incident.

1. Calculer \(f(0)\) et la limite de \(f\) en \(+\infty\).
2. Montrer que \(f'(x) = -(x + 1)e^{-x}\) et en déduire le sens de variation.
3. Interpréter.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(f(0) = 2\). Quand \(x \to +\infty\), \(f(x) \to 0\) (l'exponentielle décroissante l'emporte sur \(x + 2\)). La droite \(y = 0\) est asymptote horizontale.
2. \(f'(x) = e^{-x} + (x + 2)(-e^{-x}) = e^{-x}(1 - x - 2) = -(x + 1)e^{-x}\), négatif pour \(x \ge 0\). Donc \(f\) est strictement décroissante.
3. Le trafic part de 2 (unité du modèle) et **diminue sans cesse** pour revenir vers 0 : l'incident se résorbe, sans jamais devenir exactement nul.

</details>

### Exercice 8 – Étude avec asymptote oblique

Soit \(f(x) = x + e^{-x}\) pour \(x \ge 0\).

1. Calculer \(f'(x)\) et dresser le tableau de variations.
2. Montrer que la droite \(y = x\) est asymptote oblique en \(+\infty\). Quelle est la position de la courbe par rapport à elle ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(f'(x) = 1 - e^{-x}\) (dérivée de \(e^{-x}\) : \(-e^{-x}\)). Pour \(x > 0\), \(e^{-x} < 1\) donc \(f'(x) > 0\) ; \(f'(0) = 0\). La fonction est **croissante** sur \([0\,;\,+\infty[\), de \(f(0) = 1\) jusqu'à \(+\infty\). Valeurs : \(f(1) \approx 1{,}368\), \(f(2) \approx 2{,}135\).
2. \(f(x) - x = e^{-x} \to 0\) quand \(x \to +\infty\) : la droite \(y = x\) est asymptote oblique. Comme \(e^{-x} > 0\), la courbe est **au-dessus** de l'asymptote.

</details>

### Exercice 9 – Primitives de la forme \(u'e^{u}\), \(\dfrac{u'}{u}\)

Calculer \(\displaystyle\int_{0}^{1} x\,e^{-x^{2}}\,dx\) et \(\displaystyle\int_{0}^{2} \dfrac{x}{x^{2}+1}\,dx\). Contrôler à la calculatrice.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(u = -x^{2}\), \(u' = -2x\) : \(x\,e^{-x^{2}} = -\dfrac{1}{2}\,u'\,e^{u}\). Primitive : \(-\dfrac{1}{2}e^{-x^{2}}\). Intégrale : \(-\dfrac{1}{2}\big(e^{-1} - 1\big) = \dfrac{1 - e^{-1}}{2} \approx 0{,}316\).
2. \(u = x^{2} + 1\), \(u' = 2x\) : \(\dfrac{x}{x^{2}+1} = \dfrac{1}{2}\,\dfrac{u'}{u}\). Primitive : \(\dfrac{1}{2}\ln(x^{2}+1)\). Intégrale : \(\dfrac{1}{2}\ln 5 \approx 0{,}805\).

</details>

## Niveau 3 – Pour aller plus loin

### Exercice 6 – Aire, valeur moyenne

1. Calculer \(\displaystyle\int_{0}^{2} (3x^2 - 4x + 1)\,dx\) (une primitive est \(x^3 - 2x^2 + x\), à justifier par dérivation).
2. Calculer la valeur moyenne de \(x^2 + 1\) sur \([0\,;\,3]\).
3. Un débit est modélisé par \(d(t) = e^{-t/2}\) (en Go par heure). Quelle quantité est transférée entre \(t = 0\) et \(t = 4\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. La dérivée de \(x^3 - 2x^2 + x\) est \(3x^2 - 4x + 1\), donc c'est une primitive. L'intégrale vaut \([x^3 - 2x^2 + x]_{0}^{2} = (8 - 8 + 2) - 0 = 2\).
2. Une primitive de \(x^2 + 1\) est \(\frac{x^3}{3} + x\) (dérivée : \(x^2 + 1\)). L'intégrale sur \([0\,;\,3]\) vaut \(9 + 3 = 12\), la valeur moyenne \(\dfrac{12}{3} = 4\).
3. Une primitive de \(e^{-t/2}\) est \(-2e^{-t/2}\) (dérivée : \(e^{-t/2}\)). Quantité : \([-2e^{-t/2}]_{0}^{4} = -2e^{-2} + 2 = 2 - 2e^{-2} \approx 1{,}73\) Go.

</details>

### Exercice 7 – Méthode de Newton

Pour approcher \(\sqrt{2}\), on résout \(f(x) = x^2 - 2 = 0\) par la suite \(x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}\).

1. Expliciter \(x_{n+1}\) en fonction de \(x_n\).
2. Calculer \(x_1\), \(x_2\), \(x_3\) à partir de \(x_0 = 1\).
3. Écrire une fonction Python qui arrête l'itération quand \(|x_{n+1} - x_n| < 10^{-10}\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(f'(x) = 2x\), donc \(x_{n+1} = x_n - \dfrac{x_n^2 - 2}{2x_n} = \dfrac{1}{2}\left(x_n + \dfrac{2}{x_n}\right)\).
2. \(x_1 = \dfrac{1}{2}(1 + 2) = 1{,}5\) ; \(x_2 = \dfrac{1}{2}\left(1{,}5 + \dfrac{2}{1{,}5}\right) \approx 1{,}41667\) ; \(x_3 \approx 1{,}414216\). La valeur exacte est \(\sqrt{2} \approx 1{,}414214\) : la convergence est très rapide.
3. Voici une version possible :

```python
def newton_racine2(x0=1.0, eps=1e-10):
    x = x0
    while True:
        suivant = (x + 2 / x) / 2
        if abs(suivant - x) < eps:
            return suivant
        x = suivant
```

</details>

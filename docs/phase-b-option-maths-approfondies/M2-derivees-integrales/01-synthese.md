# Synthèse – Calcul différentiel et intégral

*BTS SIO SISR 2e année – Option mathématiques approfondies – M2*

> [!NOTE]
> **Idée directrice.** La dérivée mesure la **vitesse de variation** d'une grandeur ; l'intégrale cumule une grandeur sur un intervalle. Le référentiel valorise la **modélisation et l'interprétation** plus que l'agilité de calcul : on dérive à la main des cas simples, on laisse la calculatrice formelle faire le reste.

## 1. Dérivées usuelles

| \(f(x)\) | \(f'(x)\) |
|---|---|
| \(k\) (constante) | \(0\) |
| \(x^{n}\) | \(n x^{n-1}\) |
| \(e^{x}\) | \(e^{x}\) |
| \(\ln x\) | \(\dfrac{1}{x}\) |
| \(\dfrac{1}{x}\) | \(-\dfrac{1}{x^{2}}\) |

Règles : \((u + v)' = u' + v'\), \((ku)' = ku'\), \((uv)' = u'v + uv'\), \(\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^{2}}\), \((e^{u})' = u'e^{u}\).

## 2. Variations et extremums

- Si \(f'(x) > 0\) sur un intervalle, \(f\) est croissante ; si \(f'(x) < 0\), décroissante.
- Un extremum local se cherche là où \(f'\) s'annule **et change de signe**.
- **Méthode** : calculer \(f'\), étudier son signe (factoriser), dresser le tableau de variations, calculer les valeurs aux bornes et aux extremums.

## 3. Limites et asymptotes

- Si \(\lim_{x \to +\infty} f(x) = \ell\), la droite \(y = \ell\) est **asymptote horizontale**.
- Limites utiles : \(e^{-x} \to 0\), \(\dfrac{1}{x} \to 0\) et \(\ln x \to +\infty\) quand \(x \to +\infty\) ; \(x e^{-x} \to 0\).
- Interprétation : la limite décrit un **régime stable** (saturation, valeur d'équilibre).

## 4. Primitives et intégrale

Une **primitive** de \(f\) est une fonction \(F\) telle que \(F' = f\). Ici on ne calcule **pas** de primitive par une recette de lecture inverse : on **justifie** qu'une fonction proposée est une primitive en la **dérivant**.

\[
\int_{a}^{b} f(x)\,dx = F(b) - F(a).
\]

- Si \(f \ge 0\), c'est l'**aire** sous la courbe entre \(a\) et \(b\).
- **Valeur moyenne** de \(f\) sur \([a\,;\,b]\) : \(\dfrac{1}{b-a}\displaystyle\int_{a}^{b} f(x)\,dx\).
- Interprétation : cumul d'un débit, d'un coût marginal, d'une charge sur un intervalle de temps.

> [!TIP]
> **Calculatrice formelle.** Elle donne dérivées, limites et intégrales. Ton rôle : poser le problème, choisir l'intervalle, **justifier** et **commenter** (unité, signe, ordre de grandeur).

## 5. Pièges fréquents

- Oublier de factoriser pour étudier le signe de \(f'\).
- Annuler la dérivée sans vérifier le changement de signe.
- Oublier l'unité ou l'interprétation d'une intégrale.

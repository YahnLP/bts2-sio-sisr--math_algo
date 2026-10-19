# Aide-mémoire – Complexité asymptotique

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S13*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Définition

\(f = O(g)\) : il existe \(c > 0\) et \(n_0\) tels que \(f(n) \le c\,g(n)\) pour \(n \ge n_0\).

## Règles

- Constantes multiplicatives supprimées.
- Terme dominant conservé.
- Boucles imbriquées : produit. Blocs successifs : somme (le plus grand l'emporte).

## Classes et effet de ×2

| Classe | ×2 sur \(n\) |
|---|---|
| \(O(1)\) | ×1 |
| \(O(\log n)\) | +1 |
| \(O(n)\) | ×2 |
| \(O(n\log n)\) | un peu plus de ×2 |
| \(O(n^2)\) | ×4 |
| \(O(2^n)\) | coût élevé au carré |

## Durée

\[ \text{durée} = \frac{\text{opérations}}{\text{opérations par seconde}} \]

Toujours annoncer l'**hypothèse** de vitesse.

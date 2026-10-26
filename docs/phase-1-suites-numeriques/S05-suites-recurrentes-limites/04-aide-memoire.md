# Aide-mémoire – Limites, point fixe et seuils

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S05*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Limites usuelles

| Suite | Cas | Limite |
|---|---|---|
| \(u_0 + nr\) | \(r > 0\) / \(r < 0\) | \(+\infty\) / \(-\infty\) |
| \(u_0 q^n\), \(u_0 > 0\) | \(q > 1\) | \(+\infty\) |
| | \(\lvert q \rvert < 1\) | \(0\) |
| | \(q = 1\) | \(u_0\) |
| | \(q \le -1\) | aucune |

## Suite affine uₙ₊₁ = a·uₙ + b (avec a ≠ 1)

| Objet | Formule |
|---|---|
| Point fixe | \(L = \dfrac{b}{1-a}\) |
| Suite auxiliaire | \(v_n = u_n - L\), géométrique de raison \(a\) |
| Terme général | \(u_n = L + (u_0 - L)a^n\) |
| Convergence | \(\lvert a \rvert < 1\) : \(u_n \to L\) |

## Seuil

1. La suite atteint-elle le seuil ? (limite \(+\infty\) ou au-delà du seuil)
2. Boucle `while u < seuil` avec compteur.
3. Sinon : garde-fou `nmax` et résultat `None`.

Variant avec garde-fou : `nmax - n`.

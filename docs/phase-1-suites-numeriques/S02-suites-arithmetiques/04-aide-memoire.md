# Aide-mémoire – Suites arithmétiques

*BTS SIO SISR 2e année – Pour aller plus loin – S02*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Formules

| Objet | Formule |
|---|---|
| Définition | \(u_{n+1} = u_n + r\) |
| Terme général | \(u_n = u_0 + nr\) ; \(u_n = u_p + (n-p)r\) |
| Raison | \(r = u_{n+1} - u_n\) ; \(r = \dfrac{u_n - u_p}{n - p}\) |
| Somme de \(k\) termes consécutifs | \(k \times \dfrac{\text{premier} + \text{dernier}}{2}\) |
| \(u_0 + \dots + u_n\) | \((n+1)\dfrac{u_0 + u_n}{2}\) |
| \(1 + 2 + \dots + n\) | \(\dfrac{n(n+1)}{2}\) |
| Nombre de termes de \(u_p\) à \(u_n\) | \(n - p + 1\) |

## Variation

\(r > 0\) : croissante ; \(r < 0\) : décroissante ; \(r = 0\) : constante.

## Python

| Besoin | Code |
|---|---|
| Terme | `u0 + n * r` |
| Somme (entiers) | `(n + 1) * (2 * u0 + n * r) // 2` |
| Contrôle | `sum(u0 + k * r for k in range(n + 1))` |
| Nombre de termes de `a` à `b` | `(b - a) // pas + 1` si `b >= a` |

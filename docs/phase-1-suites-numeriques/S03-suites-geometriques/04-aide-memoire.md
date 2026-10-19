# Aide-mémoire – Suites géométriques

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S03*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Formules

| Objet | Formule |
|---|---|
| Définition | \(u_{n+1} = q\,u_n\) |
| Terme général | \(u_n = u_0 q^n\) ; \(u_n = u_p q^{n-p}\) |
| Raison | \(q = \dfrac{u_{n+1}}{u_n}\) |
| Somme (\(q \ne 1\)) | \(u_0 + \dots + u_n = u_0 \dfrac{1 - q^{n+1}}{1 - q}\) |
| Somme (\(q = 1\)) | \((n+1)\,u_0\) |
| Puissances de 2 | \(1 + 2 + \dots + 2^n = 2^{n+1} - 1\) |
| Hausse de \(t\,\%\) | \(q = 1 + t/100\) |
| Baisse de \(t\,\%\) | \(q = 1 - t/100\) |

## Variation (\(u_0 > 0\))

\(q > 1\) croissante ; \(0 < q < 1\) décroissante ; \(q = 1\) constante ; \(q < 0\) alternée.

## Python

| Besoin | Code |
|---|---|
| Terme | `u0 * q ** n` |
| Somme (entiers) | `u0 * (q ** (n + 1) - 1) // (q - 1)` |
| Évolution en % | `round(v * (1 + t / 100) ** n, 2)` |
| Rapports exacts | `Fraction(b, a)` |

# Aide-mémoire – Intérêts, emprunt et croissance de données

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S04*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Formules (taux \(t\) par période, en décimal)

| Objet | Formule |
|---|---|
| Intérêts simples | \(C_n = C_0(1 + nt)\) |
| Intérêts composés | \(C_n = C_0(1 + t)^n\) |
| Épargne (versement \(v\) en fin de période) | \(V_n = v\,\dfrac{(1+t)^n - 1}{t}\) |
| Mensualité | \(M = \dfrac{Ct}{1 - (1+t)^{-n}}\) |
| Capital restant dû | \(K_{k+1} = K_k(1+t) - M\) |
| Intérêts du mois | \(K_k \, t\) |
| Amortissement du mois | \(M - K_k\,t\) |
| Coût des intérêts | \(nM - C\) |
| Pourcentage plus ajout | \(u_{n+1} = (1+t)u_n + a\) (simulation) |

## Python

| Besoin | Code |
|---|---|
| Composés | `round(c0 * (1 + t / 100) ** n, 2)` |
| Épargne | `cap = cap * (1 + t / 100) + v` dans une boucle |
| Mensualité | `C * t / (1 - (1 + t) ** (-n))` |
| Mixte | `u = u * (1 + t / 100) + a` |
| Test sur flottants | `abs(x - y) < 0.01`, pas `==` |

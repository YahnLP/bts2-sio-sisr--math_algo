# Aide-mémoire – Suites : définition et programmation

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S01*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Définitions

| Mode | Écriture | Exemple |
|---|---|---|
| Explicite | \(u_n = f(n)\) | \(u_n = 3n + 2\) |
| Récurrence | \(u_0\) donné, \(u_{n+1} = f(u_n)\) | \(u_0 = 1\), \(u_{n+1} = 2u_n + 1\) |

\(u_n\) : terme de rang \(n\) ; \(u_{n+1}\) : le suivant ; \(u_n + 1\) : \(u_n\) augmenté de 1.

## Sens de variation

Signe de \(u_{n+1} - u_n\) : positif ou nul : croissante ; négatif ou nul : décroissante ; nul : constante. Un contre-exemple suffit à réfuter ; une preuve est nécessaire pour affirmer.

## Python

| Besoin | Code |
|---|---|
| Explicite | `def u(n): return 3 * n + 2` |
| Récurrence | `t = u0` puis `for _ in range(n): t = f(t)` |
| Liste de termes | `termes = [u0]` puis `termes.append(f(termes[-1]))` |
| Deux termes | `a, b = b, a + b` |

Invariant : après \(k\) tours, `t` vaut \(u_k\).

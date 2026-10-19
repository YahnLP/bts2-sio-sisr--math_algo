# Formulaire

Tous les aide-mémoire du cours réunis sur une seule page, dans l'ordre des séances. Utilise la recherche ou le sommaire à droite pour retrouver une formule.

> [!NOTE]
> Chaque formule a été vérifiée par le calcul sur des exemples. Pour l'épreuve, vérifie dans le sujet ce qui est rappelé et ce qui est à connaître.

## S01 · Suites : définition et programmation

### Définitions

| Mode | Écriture | Exemple |
|---|---|---|
| Explicite | \(u_n = f(n)\) | \(u_n = 3n + 2\) |
| Récurrence | \(u_0\) donné, \(u_{n+1} = f(u_n)\) | \(u_0 = 1\), \(u_{n+1} = 2u_n + 1\) |

\(u_n\) : terme de rang \(n\) ; \(u_{n+1}\) : le suivant ; \(u_n + 1\) : \(u_n\) augmenté de 1.

### Sens de variation

Signe de \(u_{n+1} - u_n\) : positif ou nul : croissante ; négatif ou nul : décroissante ; nul : constante. Un contre-exemple suffit à réfuter ; une preuve est nécessaire pour affirmer.

### Python

| Besoin | Code |
|---|---|
| Explicite | `def u(n): return 3 * n + 2` |
| Récurrence | `t = u0` puis `for _ in range(n): t = f(t)` |
| Liste de termes | `termes = [u0]` puis `termes.append(f(termes[-1]))` |
| Deux termes | `a, b = b, a + b` |

Invariant : après \(k\) tours, `t` vaut \(u_k\).

## S02 · Suites arithmétiques

### Formules

| Objet | Formule |
|---|---|
| Définition | \(u_{n+1} = u_n + r\) |
| Terme général | \(u_n = u_0 + nr\) ; \(u_n = u_p + (n-p)r\) |
| Raison | \(r = u_{n+1} - u_n\) ; \(r = \dfrac{u_n - u_p}{n - p}\) |
| Somme de \(k\) termes consécutifs | \(k \times \dfrac{\text{premier} + \text{dernier}}{2}\) |
| \(u_0 + \dots + u_n\) | \((n+1)\dfrac{u_0 + u_n}{2}\) |
| \(1 + 2 + \dots + n\) | \(\dfrac{n(n+1)}{2}\) |
| Nombre de termes de \(u_p\) à \(u_n\) | \(n - p + 1\) |

### Variation

\(r > 0\) : croissante ; \(r < 0\) : décroissante ; \(r = 0\) : constante.

### Python

| Besoin | Code |
|---|---|
| Terme | `u0 + n * r` |
| Somme (entiers) | `(n + 1) * (2 * u0 + n * r) // 2` |
| Contrôle | `sum(u0 + k * r for k in range(n + 1))` |
| Nombre de termes de `a` à `b` | `(b - a) // pas + 1` si `b >= a` |

## S03 · Suites géométriques

### Formules

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

### Variation (\(u_0 > 0\))

\(q > 1\) croissante ; \(0 < q < 1\) décroissante ; \(q = 1\) constante ; \(q < 0\) alternée.

### Python

| Besoin | Code |
|---|---|
| Terme | `u0 * q ** n` |
| Somme (entiers) | `u0 * (q ** (n + 1) - 1) // (q - 1)` |
| Évolution en % | `round(v * (1 + t / 100) ** n, 2)` |
| Rapports exacts | `Fraction(b, a)` |

## S04 · Intérêts, emprunt et croissance de données

### Formules (taux \(t\) par période, en décimal)

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

### Python

| Besoin | Code |
|---|---|
| Composés | `round(c0 * (1 + t / 100) ** n, 2)` |
| Épargne | `cap = cap * (1 + t / 100) + v` dans une boucle |
| Mensualité | `C * t / (1 - (1 + t) ** (-n))` |
| Mixte | `u = u * (1 + t / 100) + a` |
| Test sur flottants | `abs(x - y) < 0.01`, pas `==` |

## S05 · Limites, point fixe et seuils

### Limites usuelles

| Suite | Cas | Limite |
|---|---|---|
| \(u_0 + nr\) | \(r > 0\) / \(r < 0\) | \(+\infty\) / \(-\infty\) |
| \(u_0 q^n\), \(u_0 > 0\) | \(q > 1\) | \(+\infty\) |
| | \(\lvert q \rvert < 1\) | \(0\) |
| | \(q = 1\) | \(u_0\) |
| | \(q \le -1\) | aucune |

### Suite affine \(u_{n+1} = au_n + b\) (\(a \ne 1\))

| Objet | Formule |
|---|---|
| Point fixe | \(L = \dfrac{b}{1-a}\) |
| Suite auxiliaire | \(v_n = u_n - L\), géométrique de raison \(a\) |
| Terme général | \(u_n = L + (u_0 - L)a^n\) |
| Convergence | \(\lvert a \rvert < 1\) : \(u_n \to L\) |

### Seuil

1. La suite atteint-elle le seuil ? (limite \(+\infty\) ou au-delà du seuil)
2. Boucle `while u < seuil` avec compteur.
3. Sinon : garde-fou `nmax` et résultat `None`.

Variant avec garde-fou : `nmax - n`.


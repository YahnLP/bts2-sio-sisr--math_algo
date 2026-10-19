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

## S06 · Récursivité : principe

### Structure

```python
def f(donnee):
    if cas_de_base:
        return resultat_direct
    return combiner(f(donnee_plus_petite))
```

| Ingrédient | Question à se poser |
|---|---|
| Cas de base | Quel est le plus petit problème, résolu directement ? |
| Cas récursif | Comment passer à un problème plus petit ? |
| Variant | Quel entier décroît strictement et reste \(\ge 0\) ? |

### Modèles

| Problème | Cas de base | Cas récursif |
|---|---|---|
| \(n!\) | \(0! = 1\) | \(n \times (n-1)!\) |
| \(1 + \dots + n\) | \(0\) | \(n + S(n-1)\) |
| \(x^n\) | \(1\) | \(x \times x^{n-1}\) |
| PGCD | \(b = 0\) : \(a\) | `pgcd(b, a % b)` |
| Binaire de \(n\) | \(n < 2\) : `str(n)` | `binaire(n // 2) + str(n % 2)` |

### Pièges

- Pas de cas de base ou appel qui ne se rapproche pas : `RecursionError`.
- `fact(n)` : \(n + 1\) appels. Profondeur limitée (environ 1 000 par défaut en Python).
- Récursif et itératif donnent le même résultat ; l'itératif ne risque pas la limite de profondeur.

## S07 · Récursivité, suites et pile d'appels

### Suite → fonction

\(u_0\) donné, \(u_{n+1} = f(u_n)\) : cas de base `n == 0`, cas récursif `f(u(n - 1))`.

### Pile d'appels

Un cadre par appel en attente ; profondeur de `fact(n)` : \(n + 1\). Limite d'environ 1 000 en Python : au-delà, `RecursionError`.

### Fibonacci

\(F_0 = 0\), \(F_1 = 1\), \(F_n = F_{n-1} + F_{n-2}\) : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.

| Version | Appels / tours pour \(n\) |
|---|---|
| Naïve | \(C(n) = 1 + C(n-1) + C(n-2)\) : 177 pour \(n = 10\), 2 692 537 pour \(n = 30\) |
| Mémoïsée | \(2n - 1\) |
| Itérative | \(n\) tours |

### Mémoïsation

```python
def f(n, cache=None):
    if cache is None:
        cache = {}
    ...
    if n not in cache:
        cache[n] = ...
    return cache[n]
```

Jamais `cache={}` en paramètre par défaut.

## S08 · Récursivité sur les tableaux et les chaînes

### Structure d'une liste ou d'une chaîne

Vide (ou courte) = cas de base ; `L[0]` + `L[1:]` = cas récursif. Variant : `len(L)`.

### Modèles

| Problème | Cas de base | Cas récursif |
|---|---|---|
| Somme | `[]` : 0 | `L[0] + somme(L[1:])` |
| Maximum | 1 élément : `L[0]` | comparer `L[0]` et `maximum(L[1:])` |
| Comptage | `[]` : 0 | `(L[0] == x)` + `compte(L[1:], x)` |
| Présence | `[]` : `False` | `L[0] == x or present(L[1:], x)` |
| Inversion | `""` : `""` | `inverse(s[1:]) + s[0]` |
| Palindrome | `len(s) <= 1` : `True` | `s[0] == s[-1] and est_palindrome(s[1:-1])` |
| Somme des chiffres | `n < 10` : `n` | `n % 10 + somme_chiffres(n // 10)` |

### Coût

- `L[1:]` copie : \(n(n-1)/2\) éléments copiés au total.
- Profondeur \(n + 1\) : une liste de 1 000 éléments dépasse la limite habituelle.
- Remède : passer un indice, ou utiliser une boucle.

## S09 · Diviser pour régner

### Principe

Diviser (moitiés) → résoudre → combiner. Environ \(\log_2 n\) niveaux.

### Dichotomie (liste **triée**)

`milieu = (bas + haut) // 2` ; égal : trouvé ; plus petit : `bas = milieu + 1` ; plus grand : `haut = milieu - 1` ; `bas > haut` : absent. Au plus \(\lfloor \log_2 n \rfloor + 1\) comparaisons (10 pour 1 000, 20 pour un million).

### Puissance rapide

| \(n\) | Calcul |
|---|---|
| 0 | 1 |
| pair | \(y = x^{n/2}\) (calculé **une fois**), puis \(y^2\) |
| impair | \(x \cdot x^{n-1}\) |

\(x^{1000}\) : 15 multiplications.

### Tri fusion

`fusion(A, B)` : deux indices, on prend le plus petit des deux fronts, puis on recopie le reste. `tri_fusion(L)` : cas de base `len(L) <= 1`, sinon fusion des deux moitiés triées. Environ \(n \log_2 n\) comparaisons ; \(2n - 1\) appels.

### Pièges

Dichotomie sur liste non triée ; appel dupliqué sur `n // 2` ; oublier le reste à recopier dans la fusion.

## S10 · Arborescences et parcours en profondeur

### Arborescence

Dictionnaire imbriqué : valeur entière = fichier (cas de base), dictionnaire = dossier (cas récursif). `isinstance(x, int)` teste un fichier.

| Fonction | Fichier | Dossier |
|---|---|---|
| Taille | la valeur | somme des éléments |
| Nombre de fichiers | 1 | somme des éléments |
| Profondeur | 0 | 1 + max des éléments (1 si vide) |
| Chemins | `préfixe + nom` | concaténation, préfixe `nom + "/"` |

### Graphe

`g = {sommet: [voisins]}`.

```python
def dfs(g, sommet, visites=None):
    if visites is None:
        visites = []
    visites.append(sommet)
    for voisin in g[sommet]:
        if voisin not in visites:
            dfs(g, voisin, visites)
    return visites
```

### Points de vigilance

- Cycle sans liste des sommets visités : `RecursionError`.
- Variant du DFS : nombre de sommets non visités.
- Atteignables = sommets visités. DFS ne donne pas le plus court chemin.
- Très grand graphe : pile explicite plutôt que récursivité (S16).


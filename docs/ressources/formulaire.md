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

## S11 · Terminaison, invariant et tests

### Les deux questions

| Question | Outil |
|---|---|
| Termine-t-il ? | **Variant** : entier, \(\ge 0\), strictement décroissant |
| Est-il correct ? | **Invariant** : vrai au départ, conservé, utile à la sortie |

Spécification : **précondition** (entrée) et **postcondition** (sortie).

### Preuve en trois étapes

1. Initialisation : l'invariant est vrai avant le premier tour.
2. Conservation : vrai avant un tour, donc vrai après.
3. Conclusion : invariant + condition d'arrêt = postcondition.

### Modèles

| Boucle | Variant | Invariant |
|---|---|---|
| `while n > 0: n //= 2` | `n` | — |
| Somme `s += i` | `n - k` | \(s = k(k+1)/2\) |
| Maximum | éléments restants | `m` = max des éléments examinés |
| Puissance | `n - k` | \(p = x^k\) |
| Euclide | `b` | \(\text{PGCD}(a, b)\) inchangé |

### Tests

Typique, taille minimale, répétitions, valeurs extrêmes, déjà ordonné, inversé, cas interdit. Un test réussi ne prouve rien pour les autres cas.

## S12 · Coût en opérations

### Compter

| Structure | Coût |
|---|---|
| `for i in range(n)` | \(n\) |
| Deux boucles imbriquées | \(n^2\) |
| Boucle triangulaire | \(\dfrac{n(n-1)}{2}\) |
| Division par 2 jusqu'à 1 | \(\lfloor\log_2 n\rfloor\) tours |

### Recherche séquentielle (n éléments)

| Cas | Comparaisons |
|---|---|
| Meilleur | 1 |
| Pire | \(n\) |
| Moyen | \((n+1)/2\) |

### Méthode

1. Choisir l'opération de référence.
2. Exprimer le nombre de passages en fonction de \(n\).
3. Raisonner sur le pire cas pour une garantie.
4. Comparer sur des valeurs de \(n\) réalistes.

## S13 · Complexité asymptotique

### Définition

\(f = O(g)\) : il existe \(c > 0\) et \(n_0\) tels que \(f(n) \le c\,g(n)\) pour \(n \ge n_0\).

### Règles

- Constantes multiplicatives supprimées.
- Terme dominant conservé.
- Boucles imbriquées : produit. Blocs successifs : somme (le plus grand l'emporte).

### Classes et effet de ×2

| Classe | ×2 sur \(n\) |
|---|---|
| \(O(1)\) | ×1 |
| \(O(\log n)\) | +1 |
| \(O(n)\) | ×2 |
| \(O(n\log n)\) | un peu plus de ×2 |
| \(O(n^2)\) | ×4 |
| \(O(2^n)\) | coût élevé au carré |

### Durée

\[ \text{durée} = \frac{\text{opérations}}{\text{opérations par seconde}} \]

Toujours annoncer l'**hypothèse** de vitesse.

## S14 · Tris et recherches

### Tris

| Tri | Principe | Comparaisons |
|---|---|---|
| Sélection | échanger avec le minimum du reste | toujours \(n(n-1)/2\) |
| Insertion | insérer dans la partie triée | de \(n-1\) à \(n(n-1)/2\) |
| Fusion | couper, trier, fusionner | \(O(n\log n)\) |

### Recherches

| Méthode | Pire cas |
|---|---|
| Séquentielle | \(n\) |
| Dichotomique (liste triée) | \(\lfloor\log_2 n\rfloor + 1\) |

### Trier avant de chercher ?

\[ k\,n \quad\text{contre}\quad n\log_2 n + k(\lfloor\log_2 n\rfloor + 1) \]

Pour \(n = 1000\), le tri devient rentable dès \(k = 11\).

## S15 · Mesurer et limites

### Mesure

```python
import time
d = time.perf_counter()
f()
duree = time.perf_counter() - d
```

Répéter, garder le **minimum**. Comparer seulement sur la même machine.

### Test de doublement

Rapport \(t(2n)/t(n)\) : \(\approx 2\) linéaire, \(\approx 4\) quadratique, \(\approx 8\) cubique.

### Explosions

| Situation | Nombre |
|---|---|
| Force brute | \(a^L\) |
| Tournées | \((n-1)!\) |
| Durée | \(\dfrac{\text{essais}}{\text{vitesse}}\) (hypothèse annoncée) |

### Gagner du temps

Ensemble (`set`), mémoïsation, réduction de l'espace de recherche.

## S16 · Piles, files et dictionnaires

### Structures

| Structure | Règle | Python |
|---|---|---|
| Pile | LIFO | `append`, `pop()` |
| File | FIFO | `deque`, `append`, `popleft()` |
| Dictionnaire | clé → valeur | `d[k]`, `d.get(k, 0)` |
| Ensemble | sans doublon | `set`, `x in s` |

### Coûts

| Opération | Coût |
|---|---|
| `pop()` à la fin, `append` | \(O(1)\) |
| `liste.pop(0)` | \(O(n)\) |
| `x in liste` | \(O(n)\) |
| `popleft()` | \(O(1)\) |
| dictionnaire, ensemble | \(O(1)\) en moyenne |

### Choisir

Annuler : pile. Ordre d'arrivée : file. Retrouver par identifiant : dictionnaire.

## S17 · Graphes : parcours et plus court chemin

### Représentations

```python
g  = {"A": ["B", "C"], "B": []}              # non pondéré
gp = {"A": {"B": 4, "C": 1}, "B": {}}       # pondéré (poids)
```

### Algorithmes

| Besoin | Outil |
|---|---|
| Explorer, atteignabilité | profondeur (pile ou récursion) |
| Plus court en sauts | largeur (**file**) |
| Plus court en coût, poids \(\ge 0\) | Dijkstra (**tas** `heapq`) |

### Dijkstra en 3 lignes

1. `dist[départ] = 0`.
2. Traiter le sommet de plus petite distance.
3. `dist[v] = min(dist[v], dist[s] + poids)` pour chaque voisin.

Chemin : mémoriser le **parent**, puis remonter du but vers le départ.

## S18 · Méthode

### Les cinq étapes

1. **Comprendre** : entrées, sorties, un exemple à la main.
2. **Décomposer** : une fonction, une idée.
3. **Choisir** : structure, algorithme, coût visé.
4. **Programmer et tester** : tests typiques et limites, écrits avant le résultat.
5. **Justifier** : idée, invariant, coût.

### Tests à ne pas oublier

Liste vide, un élément, répétitions, valeurs extrêmes, espaces parasites, cas où la réponse est « aucun ».

### Justification en trois phrases

Idée. Invariant (ou variant). Coût en \(n\).

## S19 · # Barème et auto-évaluation

### Barème du sujet blanc (30 points)

| Question | Points | Ce qui est attendu |
|---|---|---|
| A1 | 2 | relation \(u_{n+1} = 1{,}03\,u_n\) ; suite géométrique de raison 1,03 ; \(u_n = 200 \times 1{,}03^n\) |
| A2 | 2 | formule appliquée ; \(u_{12} \approx 285{,}15\) Go |
| A3 | 3 | valeurs de \(n = 13\) et \(n = 14\) (ou logarithme) ; réponse \(n = 14\) ; justification |
| A4 | 3 | fonction correcte (2) ; justification de l'arrêt (1) |
| B1 | 3 | cas de base (1) ; appel récursif (1) ; variant (1) |
| B2 | 2 | appels et retours (1) ; résultat 8 (1) |
| B3 | 2 | calcul de \(C(2)\) à \(C(5)\) (1) ; \(C(5) = 15\) (1) |
| B4 | 3 | a) \(n = 51\) (1,5) ; b) 20 et 1 000 000 (1,5) |
| C1 | 2 | dictionnaire complet et correct |
| C2 | 3 | algorithme (largeur, file) (1) ; code correct (2) |
| C3 | 3 | code correct (2) ; latence 5 ms (1) |
| C4 | 2 | la largeur ignore les poids (1) ; poids négatif : Dijkstra n'est plus correct (1) |
| **Total** | **30** | |

### Auto-évaluation par thème

| Thème | Points perdus | À revoir |
|---|---|---|
| Suites (A) | | S01 à S05 |
| Récursivité et coût (B) | | S06 à S15 |
| Réseau et programmation (C) | | S16 à S18 |

> [!NOTE]
> Il n'y a pas de seuil officiel associé à ce sujet. Une règle simple : un thème où tu as perdu plus de 3 points sur 10 mérite une révision ciblée.

### Avant de rendre sa copie

- Chaque réponse numérique a son calcul et son unité.
- Chaque fonction a un test.
- Les cas limites sont pensés (liste vide, valeur atteinte).


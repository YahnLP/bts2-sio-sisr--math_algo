# Cours – Diviser pour régner

*BTS SIO SISR 2e année – Pour aller plus loin – S09 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S06 à S08 (récursivité, listes, variant).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Décrire** le principe « diviser pour régner » ;
- [ ] **Écrire** la recherche dichotomique ;
- [ ] **Écrire** l'exponentiation rapide ;
- [ ] **Écrire** le tri fusion ;
- [ ] **Estimer** le nombre d'étapes.

## I. Le principe

Au lieu de réduire le problème d'**un seul** élément (S08), on le **coupe en deux** (environ) :

1. **Diviser** le problème en sous-problèmes de même nature, deux fois plus petits ;
2. **Résoudre** chaque sous-problème (récursivement) ;
3. **Combiner** les résultats.

Comme la taille est divisée par 2 à chaque niveau, il y a environ \(\log_2 n\) niveaux (\(n = 1\,000\) : 10 niveaux ; \(n = 1\,000\,000\) : 20 niveaux). C'est la source de l'efficacité.

## II. La recherche dichotomique

Dans une liste **triée**, on regarde l'élément du **milieu** : s'il est égal à la valeur cherchée, c'est fini ; s'il est plus petit, on cherche à droite ; sinon à gauche.

```python
def dicho(L, x, bas=0, haut=None):
    if haut is None:
        haut = len(L) - 1
    if bas > haut:
        return -1                      # absent
    milieu = (bas + haut) // 2
    if L[milieu] == x:
        return milieu
    if L[milieu] < x:
        return dicho(L, x, milieu + 1, haut)
    return dicho(L, x, bas, milieu - 1)
```

Variant : `haut - bas + 1`, le nombre d'éléments restant à examiner : il diminue strictement et le cas `bas > haut` arrête la recherche.

Exemple dans \(L = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]\), on cherche 23 : milieu d'indice 4 (valeur 16) < 23, on cherche à droite ; milieu d'indice 7 (56) > 23, on cherche à gauche ; milieu d'indice 5 : trouvé en **3** comparaisons. Pour 40 (absent) : 16, 56, 23, 38, puis la zone est vide : **4** comparaisons.

Le nombre maximal de comparaisons est \(\lfloor \log_2 n \rfloor + 1\) : 10 pour 1 000 éléments, 20 pour un million (contre un million de comparaisons au pire pour un parcours séquentiel).

> [!WARNING]
> La dichotomie n'a de sens que dans une liste **triée**. Dans une liste non triée, elle peut rater un élément présent.

## III. L'exponentiation rapide

\[ x^n = \begin{cases} 1 & \text{si } n = 0 \\ \left(x^{n/2}\right)^2 & \text{si } n \text{ est pair} \\ x \times x^{n-1} & \text{si } n \text{ est impair} \end{cases} \]

```python
def puissance_rapide(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        y = puissance_rapide(x, n // 2)
        return y * y
    return x * puissance_rapide(x, n - 1)
```

Il faut calculer `y` **une seule fois** (si on écrit `puissance_rapide(x, n // 2) * puissance_rapide(x, n // 2)`, on perd tout le gain). Pour \(n = 1\,000\), on fait **15 multiplications** au lieu de 1 000 avec la version de S06. Cette méthode sert en cryptographie, où les exposants ont des centaines de chiffres.

## IV. Le tri fusion

Pour trier une liste : on la coupe en deux moitiés, on trie chacune, on **fusionne** les deux listes triées.

```python
def fusion(A, B):                     # A et B triées
    resultat = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            resultat.append(A[i]); i = i + 1
        else:
            resultat.append(B[j]); j = j + 1
    return resultat + A[i:] + B[j:]

def tri_fusion(L):
    if len(L) <= 1:
        return L
    milieu = len(L) // 2
    return fusion(tri_fusion(L[:milieu]), tri_fusion(L[milieu:]))
```

Exemple de fusion : `fusion([2, 5, 9], [1, 6, 7, 10])` donne `[1, 2, 5, 6, 7, 9, 10]` : à chaque étape on prend le plus petit des deux premiers éléments restants.

Exemple de tri : `[5, 2, 9, 1, 7]` est coupée en `[5, 2]` et `[9, 1, 7]` ; `[5, 2]` donne `[2, 5]` ; `[9, 1, 7]` est coupée en `[9]` et `[1, 7]`, ce qui donne `[1, 7, 9]` ; la fusion finale donne `[1, 2, 5, 7, 9]`.

La fusion de deux listes de \(n\) éléments au total fait au plus \(n - 1\) comparaisons, et il y a environ \(\log_2 n\) niveaux : l'ordre de grandeur du tri fusion est \(n \log_2 n\) comparaisons (S13 précise cette notion).

**Test flash.** Combien de comparaisons au plus pour chercher dans une liste triée de 1 000 éléments ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(\lfloor \log_2 1\,000 \rfloor + 1 = 9 + 1 = \) **10** (car \(2^9 = 512 \le 1\,000 < 1\,024 = 2^{10}\)).

</details>

## À retenir

- Diviser pour régner : couper en deux, résoudre, combiner.
- Dichotomie : liste **triée**, au plus \(\lfloor \log_2 n \rfloor + 1\) comparaisons.
- Puissance rapide : \(x^n = (x^{n/2})^2\) (pair) ou \(x \cdot x^{n-1}\) (impair) ; ne calculer la moitié qu'une fois.
- Tri fusion : trier chaque moitié, puis fusionner ; environ \(n \log_2 n\) comparaisons.

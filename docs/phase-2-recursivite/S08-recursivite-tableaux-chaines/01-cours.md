# Cours – Récursivité sur les tableaux et les chaînes

*BTS SIO SISR 2e année – Pour aller plus loin – S08 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S06 et S07 ; listes et chaînes en Python (indices, tranches `L[1:]`).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Parcourir** récursivement une liste ;
- [ ] **Traiter** une chaîne récursivement (palindrome, inversion) ;
- [ ] **Écrire** une recherche récursive ;
- [ ] **Calculer** somme, maximum, comptage récursivement ;
- [ ] **Repérer** les copies coûteuses.

## I. Réduire une liste

Une liste est soit **vide**, soit un **premier élément** suivi d'une **liste plus courte**. C'est exactement la structure d'une définition récursive :

\[ \text{somme}([\,]) = 0 \qquad \text{somme}([x] + R) = x + \text{somme}(R) \]

```python
def somme(L):
    if L == []:               # cas de base : liste vide
        return 0
    return L[0] + somme(L[1:])   # premier élément + somme du reste
```

Variant : `len(L)`, qui diminue de 1 à chaque appel. Pour `somme([4, 7, 1])` : \(4 + (7 + (1 + 0)) = 12\).

## II. Maximum, comptage, présence

```python
def maximum(L):               # L non vide
    if len(L) == 1:
        return L[0]
    m = maximum(L[1:])
    return L[0] if L[0] > m else m

def compte(L, x):             # nombre d'occurrences de x
    if L == []:
        return 0
    return (1 if L[0] == x else 0) + compte(L[1:], x)

def present(L, x):            # x est-il dans L ?
    if L == []:
        return False
    return L[0] == x or present(L[1:], x)
```

Pour `maximum`, le cas de base est une liste à **un** élément : le maximum d'une liste vide n'existe pas.

## III. Chaînes de caractères

Une chaîne se réduit comme une liste : `s[0]` est le premier caractère, `s[1:]` le reste, `s[1:-1]` le milieu.

```python
def inverse(s):
    if s == "":
        return ""
    return inverse(s[1:]) + s[0]        # "abc" -> "cba"

def est_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and est_palindrome(s[1:-1])
```

Un **palindrome** se lit pareil dans les deux sens (`"radar"`). Ici le variant est `len(s)` : il diminue de 2 à chaque appel et reste \(\ge 0\) puisque les cas de longueur 0 ou 1 sont des cas de base.

Entiers comme chaînes de chiffres : la somme des chiffres de \(n\) est `n % 10 + somme_chiffres(n // 10)`, avec `n < 10` comme cas de base.

## IV. Le coût des copies et de la profondeur

> [!WARNING]
> `L[1:]` **copie** la liste. Pour une liste de \(n\) éléments, les copies successives totalisent \((n-1) + (n-2) + \dots + 1 + 0 = \dfrac{n(n-1)}{2}\) éléments copiés : \(499\,500\) pour \(n = 1\,000\). De plus la profondeur vaut \(n + 1\) : une liste de 1 000 éléments dépasse la limite de récursion habituelle.

On évite les copies en passant un **indice** :

```python
def somme_depuis(L, i):
    if i == len(L):
        return 0
    return L[i] + somme_depuis(L, i + 1)
```

Le variant est `len(L) - i`. Pour de longues listes, la **boucle** reste préférable.

**Test flash.** Que renvoie `compte([3, 1, 3, 3, 2], 3)` ?

<details markdown="1">
<summary>Voir la réponse</summary>

**3** : le premier élément vaut 3 (1), le reste `[1, 3, 3, 2]` en contient 2.

</details>

## À retenir

- Liste ou chaîne : vide (ou courte) = cas de base ; premier élément + reste = cas récursif.
- Palindrome : `s[0] == s[-1]` et le milieu est un palindrome.
- `L[1:]` copie ; l'indice évite les copies ; la boucle évite la pile.
- Le maximum d'une liste vide n'existe pas : le cas de base est la liste à un élément.

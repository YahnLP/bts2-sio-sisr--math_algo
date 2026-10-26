# Exercices – Algorithmique appliquée et programmation

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – R5*

> [!NOTE]
> **Comment travailler.** Écris d'abord ta réponse **sur papier** (en-tête, corps indenté, commentaires), puis teste-la dans l'éditeur Python de ton choix. Les résultats annoncés dans les réponses ont été obtenus par exécution. Trois niveaux : **socle**, **format épreuve**, **pour aller plus loin**.

## Niveau 1 – Socle

### Exercice 1 – Suivi de variables

```text
s ← 0
POUR i DE 1 À 5 FAIRE
    SI i MOD 2 = 0 ALORS
        s ← s + i × i
    SINON
        s ← s − i
    FIN SI
FIN POUR
```

Dresser le tableau de suivi (valeurs de \(i\) et de \(s\) à la fin de chaque tour) et donner la valeur finale de \(s\).

<details markdown="1">
<summary>Voir la réponse</summary>

| Tour | \(i\) | Test \(i\) pair ? | \(s\) après |
|---|---|---|---|
| 1 | 1 | non | \(0 - 1 = -1\) |
| 2 | 2 | oui | \(-1 + 4 = 3\) |
| 3 | 3 | non | \(3 - 3 = 0\) |
| 4 | 4 | oui | \(0 + 16 = 16\) |
| 5 | 5 | non | \(16 - 5 = 11\) |

Valeur finale : **\(s = 11\)**.

</details>

### Exercice 2 – Somme des chiffres

Écrire la fonction `somme_chiffres(n)` (entier naturel \(n\)) qui retourne la somme des chiffres décimaux de \(n\), sans convertir en chaîne. Dresser le suivi pour \(n = 2024\).

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def somme_chiffres(n):
    """Retourne la somme des chiffres décimaux de l'entier naturel n."""
    s = 0
    while n > 0:
        s = s + n % 10      # dernier chiffre
        n = n // 10         # on le retire
    return s
```

| Tour | \(n\) avant | chiffre | \(s\) | \(n\) après |
|---|---|---|---|---|
| 1 | 2024 | 4 | 4 | 202 |
| 2 | 202 | 2 | 6 | 20 |
| 3 | 20 | 0 | 6 | 2 |
| 4 | 2 | 2 | 8 | 0 |

`somme_chiffres(2024)` retourne **8** ; `somme_chiffres(0)` retourne 0 (aucun tour) ; `somme_chiffres(999)` retourne 27.

</details>

### Exercice 3 – Parcours d'un tableau

Écrire `statistiques(t, seuil)` qui, pour un tableau non vide de nombres, retourne le maximum, **l'indice** de sa première occurrence, la moyenne et le nombre d'éléments strictement supérieurs à `seuil`. Tester avec `t = [12, 7, 19, 4, 19, 8]` et `seuil = 10`.

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def statistiques(t, seuil):
    """t : liste non vide de nombres. Retourne (maximum, indice, moyenne, nb_au_dessus)."""
    maxi = t[0]
    indice = 0
    total = 0
    nb = 0
    for i in range(len(t)):
        total = total + t[i]
        if t[i] > maxi:          # strict : on garde la première occurrence
            maxi = t[i]
            indice = i
        if t[i] > seuil:
            nb = nb + 1
    return maxi, indice, total / len(t), nb
```

`statistiques([12, 7, 19, 4, 19, 8], 10)` retourne `(19, 2, 11.5, 3)` : maximum 19 à l'indice 2, moyenne 11,5, trois valeurs strictement supérieures à 10 (12, 19, 19).

</details>

### Exercice 4 – Chaînes de caractères

1. Écrire `voyelles(s)` qui compte les voyelles `a e i o u` (minuscules ou majuscules) d'une chaîne.
2. Écrire `palindrome(s)` qui indique si la chaîne se lit de la même façon dans les deux sens, **en ignorant** la casse et les caractères non alphanumériques.

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def voyelles(s):
    n = 0
    for c in s.lower():
        if c in "aeiou":
            n = n + 1
    return n

def palindrome(s):
    propre = ""
    for c in s.lower():
        if c.isalnum():
            propre = propre + c
    return propre == propre[::-1]
```

`voyelles("Administrateur reseau")` retourne 10 ; `palindrome("Esope reste ici et se repose")` retourne `True` ; `palindrome("reseau")` retourne `False`.

</details>

### Exercice 5 – Masques binaires

Écrire quatre fonctions : `bit(x, k)` (valeur du bit de rang \(k\), le rang 0 étant celui de poids faible), `mettre_a_1(x, k)`, `mettre_a_0(x, k)`, `inverser(x, k)`. Donner les résultats pour \(x = 10110110_2\).

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def bit(x, k):
    return (x >> k) & 1

def mettre_a_1(x, k):
    return x | (1 << k)

def mettre_a_0(x, k):
    return x & ~(1 << k)

def inverser(x, k):
    return x ^ (1 << k)
```

Pour `x = 0b10110110` : `bit(x, 0)` vaut 0 et `bit(x, 2)` vaut 1 ; `mettre_a_1(x, 0)` donne `0b10110111` ; `mettre_a_0(x, 2)` donne `0b10110010` ; `inverser(x, 7)` donne `0b00110110`.

</details>

## Niveau 2 – Format épreuve

### Exercice 6 – Nombres parfaits

Un entier \(n \ge 2\) est **parfait** s'il est égal à la somme de ses diviseurs **stricts** (6 = 1 + 2 + 3). Écrire `est_parfait(n)`, puis un programme qui affiche les nombres parfaits inférieurs à 1000.

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def est_parfait(n):
    if n < 2:
        return False
    somme = 0
    for d in range(1, n):
        if n % d == 0:
            somme = somme + d
    return somme == n

print([n for n in range(1, 1000) if est_parfait(n)])
```

Résultat : `[6, 28, 496]`. On peut accélérer en s'arrêtant à \(\sqrt{n}\) et en ajoutant les diviseurs par paires (\(d\) et \(n/d\)).

</details>

### Exercice 7 – La tirelire (boucle indéterministe)

Une association a 120 € en caisse et y ajoute 7 € par semaine. Elle vise 500 €. Écrire un programme qui calcule le nombre de semaines nécessaires et le montant atteint. Pourquoi une boucle `TANT QUE` est-elle adaptée ? Vérifier avec un calcul direct.

<details markdown="1">
<summary>Voir la réponse</summary>

```python
montant = 120
semaines = 0
while montant < 500:
    montant = montant + 7
    semaines = semaines + 1
print(semaines, montant)
```

Résultat : **55 semaines**, montant **505 €**. Le nombre de tours n'est pas connu à l'avance : la boucle s'arrête quand la condition `montant < 500` devient fausse. Vérification : il manque \(500 - 120 = 380\) € ; \(380 / 7 \approx 54{,}3\), donc 55 semaines entières ; \(120 + 55 \times 7 = 505\).

</details>

### Exercice 8 – Premiers palindromes

Écrire `est_premier(n)` et en déduire la liste des nombres premiers inférieurs à 200 dont l'écriture décimale est un palindrome.

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def est_premier(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True

print([n for n in range(1, 200)
       if est_premier(n) and str(n) == str(n)[::-1]])
```

Résultat : `[2, 3, 5, 7, 11, 101, 131, 151, 181, 191]`. On s'arrête quand \(d^2 > n\) : c'est le critère étudié en arithmétique.

</details>

### Exercice 9 – Clé de contrôle

Reprenant la clé de l'exercice 11 de la série R1, écrire `cle(N)` (retourne \(97 - (N \bmod 97)\)) et `est_valide(N, c)` (vrai si \(N + c\) est un multiple de 97). Tester avec \(N = 2\,910\,733\,118\,042\) et l'erreur de saisie du dernier chiffre.

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def cle(N):
    return 97 - N % 97

def est_valide(N, c):
    return (N + c) % 97 == 0
```

`cle(2910733118042)` retourne 4 ; `est_valide(2910733118042, 4)` retourne `True` ; `est_valide(2910733118043, 4)` retourne `False` : l'erreur de saisie est détectée.

</details>

### Exercice 10 – Produit de matrices

Écrire `produit(A, B)` qui retourne le produit de deux matrices représentées par des listes de listes, en vérifiant d'abord la compatibilité des tailles. Tester avec les matrices \(P\) et \(Q\) de l'exercice 3 de la série R2.

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def produit(A, B):
    p, n, q = len(A), len(B), len(B[0])
    if len(A[0]) != n:
        raise ValueError("tailles incompatibles")
    C = [[0] * q for _ in range(p)]
    for i in range(p):
        for j in range(q):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C
```

`produit([[1, 2, 0], [0, 1, 3]], [[2, 1], [0, 1], [4, 0]])` retourne `[[2, 3], [12, 1]]`, comme le calcul à la main. L'écriture `[[0] * q] * p` serait **fausse** : elle créerait \(p\) références vers la même ligne.

</details>

### Exercice 11 – Déboguer

```python
def moyenne_positifs(t):
    t.sort()                          # (1)
    s = 0
    n = 0
    for i in range(len(t) + 1):       # (2)
        if t[i] > 0:
            s = s + t[i]
            n = n + 1
    return s / n                      # (3)
```

La fonction doit retourner la moyenne des valeurs strictement positives de `t`. Trouver les trois défauts, expliquer ce qui se passe pour `t = [3, -1, 4, 0, 5]` et pour `t = []`, puis corriger.

<details markdown="1">
<summary>Voir la réponse</summary>

1. `t.sort()` **modifie la liste de l'appelant** (effet de bord) alors que le tri est inutile.
2. `range(len(t) + 1)` fait lire `t[len(t)]` : **indice hors domaine** (`IndexError`). Pour `[3, -1, 4, 0, 5]`, le programme plante au dernier tour.
3. `s / n` provoque une **division par zéro** quand aucune valeur n'est strictement positive (par exemple `[]` ou `[-2, 0]`).

Version corrigée :

```python
def moyenne_positifs(t):
    s = 0
    n = 0
    for v in t:
        if v > 0:
            s = s + v
            n = n + 1
    if n == 0:
        return None       # aucune valeur positive
    return s / n
```

Résultats : `moyenne_positifs([3, -1, 4, 0, 5])` retourne `4.0` ; `moyenne_positifs([])` et `moyenne_positifs([-2, 0])` retournent `None`.

</details>

### Exercice 12 – La suite de Syracuse

On part d'un entier \(n \ge 1\) ; tant que \(n \ne 1\), on remplace \(n\) par \(n/2\) s'il est pair et par \(3n + 1\) sinon. Écrire `syracuse(n)` qui retourne le **nombre d'étapes** et la **plus grande valeur atteinte**. Donner le résultat pour 6, 7 et 27.

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def syracuse(n):
    etapes = 0
    maxi = n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        etapes = etapes + 1
        if n > maxi:
            maxi = n
    return etapes, maxi
```

`syracuse(6)` retourne `(8, 16)` (6, 3, 10, 5, 16, 8, 4, 2, 1) ; `syracuse(7)` retourne `(16, 52)` ; `syracuse(27)` retourne **`(111, 9232)`**. Le programme **s'arrête** pour tous les entiers testés, mais on ne sait pas démontrer qu'il s'arrête pour tout \(n\) : c'est la conjecture de Syracuse.

</details>

## Niveau 3 – Pour aller plus loin (hors programme de l'épreuve)

Ces exercices dépassent ce que l'épreuve E3 demande (récursivité, coût d'un algorithme). Ils préparent les phases suivantes du site.

### Exercice 13 – Récursivité

Écrire en version récursive : `fact(n)` (factorielle), `somme_chiffres_rec(n)`, `puissance(a, n)` par la méthode « on élève \(a^{\lfloor n/2 \rfloor}\) au carré ». Identifier pour chacune le cas de base et ce qui décroît. Convertir en version itérative la fonction `pgcd(a, b)` récursive terminale.

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def fact(n):
    if n <= 1:                        # cas de base
        return 1
    return n * fact(n - 1)            # n diminue de 1 (non terminale : on multiplie après l'appel)

def somme_chiffres_rec(n):
    if n < 10:                        # cas de base
        return n
    return n % 10 + somme_chiffres_rec(n // 10)

def puissance(a, n):
    if n == 0:                        # cas de base
        return 1
    h = puissance(a, n // 2)          # n est divisé par 2
    return h * h if n % 2 == 0 else h * h * a

def pgcd(a, b):                       # récursive terminale
    if b == 0:
        return a
    return pgcd(b, a % b)

def pgcd_iteratif(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

`fact(5)` = 120 ; `somme_chiffres_rec(2024)` = 8 ; `puissance(3, 13)` = 1 594 323 = \(3^{13}\) ; `pgcd(1071, 462)` et `pgcd_iteratif(1071, 462)` retournent 21. La **terminaison** repose sur une quantité entière qui diminue strictement (\(n\), \(b\)) jusqu'au cas de base. La version terminale se transforme mécaniquement en boucle ; `fact` ne le permet pas directement (il faut un accumulateur).

</details>

### Exercice 14 – Coût d'une recherche

1. Une recherche séquentielle d'un élément dans un tableau de \(n\) éléments distincts : donner le nombre minimal et maximal de comparaisons.
2. Pour une recherche par dichotomie dans un tableau **trié**, le nombre maximal de comparaisons est \(\lfloor \log_2 n \rfloor + 1\). Calculer-le pour \(n = 1000\) et \(n = 10^6\). Que conclure ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. Minimum : **1** (l'élément est en première position). Maximum : **\(n\)** (en dernière position, ou absent).
2. \(n = 1000\) : \(\lfloor \log_2 1000 \rfloor + 1 = 9 + 1 = 10\) ; \(n = 10^6\) : \(\lfloor \log_2 10^6 \rfloor + 1 = 19 + 1 = 20\). En multipliant la taille par 1000, on ne **double** que le nombre de comparaisons : la dichotomie est incomparablement plus économe, au prix d'avoir un tableau trié.

</details>

### Exercice 15 – Exponentiation modulaire rapide

Écrire `pexp(a, n, m)` qui calcule \(a^n \bmod m\) sans jamais manipuler de grand nombre : on réduit modulo \(m\) à chaque produit, et on parcourt les bits de \(n\). Vérifier avec \(7^{100} \bmod 13\).

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def pexp(a, n, m):
    r = 1
    a = a % m
    while n > 0:
        if n & 1:                 # bit de poids faible de n égal à 1
            r = r * a % m
        a = a * a % m             # on élève au carré
        n = n >> 1                # on passe au bit suivant
    return r
```

`pexp(7, 100, 13)` retourne **9**, comme à l'exercice 8 de la série R1. Le nombre de tours est le nombre de bits de \(n\), soit \(\lfloor \log_2 n \rfloor + 1\). C'est l'opération de base du chiffrement RSA (Python propose `pow(a, n, m)`).

</details>

## Auto-évaluation

- [ ] Je dresse un tableau de suivi de variables et je retrouve le résultat annoncé.
- [ ] Je rédige un algorithme avec en-tête, commentaires et indentation.
- [ ] Je choisis entre `POUR` et `TANT QUE` en justifiant.
- [ ] Je manipule tableaux, chaînes et masques binaires.
- [ ] Je repère un effet de bord, un indice hors domaine, une division par zéro.
- [ ] J'écris une fonction récursive avec cas de base et justification de l'arrêt.

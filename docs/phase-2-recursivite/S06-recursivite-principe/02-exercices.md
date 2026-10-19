# Exercices – Récursivité : principe

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S06*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**. Ouvre ensuite « Voir la réponse » pour te corriger. **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Dérouler `fact(4)`

Écrire les appels successifs de `fact(4)` et la valeur renvoyée. Combien d'appels ?

<details markdown="1">
<summary>Voir la réponse</summary>

`fact(4) = 4 × fact(3)`, `fact(3) = 3 × fact(2)`, `fact(2) = 2 × fact(1)`, `fact(1) = 1 × fact(0)`, `fact(0) = 1`. Remontée : 1, 1, 2, 6, **24**. Il y a **5** appels (de 4 à 0).

</details>

## Exercice 2 – Une définition récursive

On veut calculer \(S(n) = 1^2 + 2^2 + \dots + n^2\). Donner le cas de base, le cas récursif, puis \(S(4)\).

<details markdown="1">
<summary>Voir la réponse</summary>

Cas de base : \(S(0) = 0\). Cas récursif : \(S(n) = n^2 + S(n-1)\). Donc \(S(1) = 1\), \(S(2) = 5\), \(S(3) = 14\), \(S(4) = 30\).

</details>

## Exercice 3 – Deux erreurs

Que se passe-t-il pour chaque fonction ? Corriger.

```python
def f(n):
    return n * f(n - 1)

def g(n):
    if n == 0:
        return 0
    return g(n + 1)
```

<details markdown="1">
<summary>Voir la réponse</summary>

`f` n'a **pas de cas de base** : les appels ne s'arrêtent jamais (`RecursionError`). Correction : ajouter `if n == 0: return 1`.
`g` a un cas de base mais l'appel `g(n + 1)` **s'éloigne** de 0 : le variant ne décroît pas. Correction : `g(n - 1)`.

</details>

## Exercice 4 – Algorithme d'Euclide

Dérouler `pgcd(252, 105)`. Quel est le variant ?

<details markdown="1">
<summary>Voir la réponse</summary>

`pgcd(252, 105) → pgcd(105, 42) → pgcd(42, 21) → pgcd(21, 0)` : renvoie **21**. Les seconds arguments 105, 42, 21, 0 décroissent strictement : le variant est `b`.

</details>

## Exercice 5 – Nombre d'appels

Combien d'appels (le premier compris) fait `puissance(2, 10)` ? Et `puissance(x, n)` ?

<details markdown="1">
<summary>Voir la réponse</summary>

Les appels portent sur `n = 10, 9, …, 0` : **11** appels. Pour `puissance(x, n)` : \(n + 1\) appels.

</details>

## Exercice 6 – Conversion binaire

Dérouler `binaire(13)`. Que renvoie `binaire(10)` ?

<details markdown="1">
<summary>Voir la réponse</summary>

`binaire(13) = binaire(6) + "1"`, `binaire(6) = binaire(3) + "0"`, `binaire(3) = binaire(1) + "1" = "11"`. Donc `"110"` puis **`"1101"`**. Pour 10 : `binaire(5) + "0"` avec `binaire(5) = binaire(2) + "1"` et `binaire(2) = binaire(1) + "0" = "10"` : on obtient **`"1010"`**.

</details>

## Exercice 7 – Version itérative

Écrire une version itérative de `puissance(x, n)`. Les deux versions donnent-elles le même résultat ? Laquelle risque une `RecursionError` pour `n = 5000` ?

<details markdown="1">
<summary>Voir la réponse</summary>

```python
def puissance_iter(x, n):
    p = 1
    for _ in range(n):
        p = p * x
    return p
```

Même résultat. La version **récursive** risque une `RecursionError` pour \(n = 5\,000\) (la limite par défaut de Python est d'environ 1 000 appels imbriqués). La version itérative n'a pas ce problème.

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Nommer cas de base, cas récursif et variant
- [ ] Dérouler une exécution récursive
- [ ] Repérer une erreur de terminaison
- [ ] Écrire la version itérative équivalente

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

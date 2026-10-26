# Exercices – Terminaison, invariant et tests

*BTS SIO SISR 2e année – Pour aller plus loin – S11*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**. Ouvre ensuite « Voir la réponse » pour te corriger. **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Variant

La boucle `while n > 0: n = n // 2` part de `n = 100`. Donner un variant et le nombre de tours.

<details markdown="1">
<summary>Voir la réponse</summary>

Variant : `n`, entier positif ou nul qui diminue strictement (`n // 2 < n` si `n > 0`). Valeurs : 100, 50, 25, 12, 6, 3, 1, 0. **7 tours.**

</details>

## Exercice 2 – Boucle qui ne s'arrête pas

Que fait `i = 0` puis `while i != 10: i = i + 3` ? Corriger.

<details markdown="1">
<summary>Voir la réponse</summary>

`i` vaut 0, 3, 6, 9, 12, 15, … : il saute par-dessus 10 et la condition `i != 10` reste vraie : **boucle infinie**. Correction : `while i < 10`, avec le variant `10 - i`.

</details>

## Exercice 3 – Invariant d'une somme

Pour `s = 0` puis `for i in range(1, n + 1): s = s + i`, énoncer l'invariant et vérifier les trois étapes.

<details markdown="1">
<summary>Voir la réponse</summary>

Invariant : après \(k\) tours, \(s = k(k+1)/2\). Initialisation : \(k = 0\), \(s = 0\). Conservation : \(\dfrac{k(k+1)}{2} + (k+1) = \dfrac{(k+1)(k+2)}{2}\). Conclusion : après \(n\) tours, \(s = n(n+1)/2\).

</details>

## Exercice 4 – Invariant du maximum

Énoncer un invariant pour la recherche du maximum d'une liste non vide `L` avec `m = L[0]` puis `for x in L: if x > m: m = x`. En déduire la postcondition.

<details markdown="1">
<summary>Voir la réponse</summary>

Invariant : après avoir examiné \(k\) éléments (\(k \ge 1\)), `m` est le plus grand de ces \(k\) éléments. Initialisation : `m = L[0]`, plus grand du seul élément `L[0]`. Conservation : si `x > m`, `m` devient `x`, sinon `m` reste plus grand. Conclusion : après avoir examiné tous les éléments, `m` est le plus grand de la liste.

</details>

## Exercice 5 – Invariant d'une puissance

Pour `p = 1` puis `for _ in range(n): p = p * x`, énoncer l'invariant.

<details markdown="1">
<summary>Voir la réponse</summary>

Après \(k\) tours, `p` vaut \(x^k\). Initialisation : \(k = 0\), `p = 1 = x^0`. Conservation : \(x^k \times x = x^{k+1}\). Conclusion : après \(n\) tours, `p` vaut \(x^n\).

</details>

## Exercice 6 – Choisir des tests

Proposer six tests pour une fonction `minimum(L)`.

<details markdown="1">
<summary>Voir la réponse</summary>

`[5]` (un élément) ; `[3, 1, 2]` (typique) ; `[2, 2]` (répétitions) ; `[-1, -5]` (négatifs) ; `[1, 2, 3]` et `[3, 2, 1]` (déjà ordonnée, inversée) ; la liste vide si la précondition ne l'exclut pas (la fonction doit alors lever une erreur claire ou renvoyer une valeur convenue).

</details>

## Exercice 7 – Un test qui ne suffit pas

La fonction ci-dessous passe les tests `est_trie([1, 2, 3]) == True` et `est_trie([2, 1]) == False`. Est-elle correcte ?

```python
def est_trie(L):
    return len(L) < 2 or L[0] <= L[1]
```

<details markdown="1">
<summary>Voir la réponse</summary>

Non : elle ne compare que les **deux premiers** éléments. `est_trie([1, 2, 0])` renvoie `True` à tort. Il fallait un test où le désordre est ailleurs qu'au début. Un invariant (« les éléments déjà examinés sont ordonnés ») aurait révélé l'erreur.

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Trouver un variant et compter les tours
- [ ] Énoncer et vérifier un invariant en trois étapes
- [ ] Distinguer précondition et postcondition
- [ ] Choisir des tests typiques et limites

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

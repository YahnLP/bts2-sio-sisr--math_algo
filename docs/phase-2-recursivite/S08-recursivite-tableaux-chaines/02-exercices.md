# Exercices – Récursivité sur les tableaux et les chaînes

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S08*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**. Ouvre ensuite « Voir la réponse » pour te corriger. **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Dérouler une somme

Dérouler `somme([4, 7, 1])`.

<details markdown="1">
<summary>Voir la réponse</summary>

`somme([4, 7, 1]) = 4 + somme([7, 1])`, `somme([7, 1]) = 7 + somme([1])`, `somme([1]) = 1 + somme([])`, `somme([]) = 0`. Remontée : 1, 8, **12**. 4 appels.

</details>

## Exercice 2 – Maximum

Écrire `maximum(L)` récursif pour une liste non vide et dérouler `maximum([3, 9, 4])`.

<details markdown="1">
<summary>Voir la réponse</summary>

Cas de base : un seul élément. Sinon on compare `L[0]` au maximum du reste. `maximum([3, 9, 4])` : `maximum([4]) = 4`, `maximum([9, 4]) = 9`, `maximum([3, 9, 4]) = 9`.

</details>

## Exercice 3 – Palindromes

`est_palindrome("radar")` et `est_palindrome("reseau")` : donner les appels. Quel est le variant ?

<details markdown="1">
<summary>Voir la réponse</summary>

`"radar"` : `'r' == 'r'`, puis `"ada"` : `'a' == 'a'`, puis `"d"` (longueur 1, cas de base) : **True**. `"reseau"` : `'r' != 'u'` : **False** dès le premier appel. Variant : `len(s)`, qui diminue de 2.

</details>

## Exercice 4 – Inversion

Dérouler `inverse("abc")`.

<details markdown="1">
<summary>Voir la réponse</summary>

`inverse("abc") = inverse("bc") + "a"`, `inverse("bc") = inverse("c") + "b"`, `inverse("c") = inverse("") + "c" = "c"`. Donc `"c"`, puis `"cb"`, puis **`"cba"`**.

</details>

## Exercice 5 – Comptage

Combien de fois `compte([3, 1, 3, 3, 2], 3)` ajoute-t-il 1 ? Écrire les appels.

<details markdown="1">
<summary>Voir la réponse</summary>

Le premier appel ajoute 1 (3 = 3), puis `[1, 3, 3, 2]` n'ajoute rien, `[3, 3, 2]` ajoute 1, `[3, 2]` ajoute 1, `[2]` n'ajoute rien, `[]` renvoie 0 : total **3**.

</details>

## Exercice 6 – Coût des copies

Une liste a 1 000 éléments. Combien d'éléments sont copiés au total par `somme(L)` avec `L[1:]` ? Et avec la version à indice ? Cette liste passe-t-elle la limite de récursion habituelle ?

<details markdown="1">
<summary>Voir la réponse</summary>

Avec `L[1:]` : \(999 + 998 + \dots + 0 = \dfrac{1\,000 \times 999}{2} = 499\,500\) éléments copiés. Avec l'indice : **aucune copie**. La profondeur est \(1\,001\), qui dépasse la limite par défaut d'environ 1 000 : `RecursionError` probable dans les deux cas. Pour une telle liste, on utilise une boucle ou `sum`.

</details>

## Exercice 7 – Somme des chiffres

Écrire `somme_chiffres(n)` récursive. Que renvoie `somme_chiffres(2024)` ?

<details markdown="1">
<summary>Voir la réponse</summary>

Cas de base : `n < 10` renvoie `n`. Sinon `n % 10 + somme_chiffres(n // 10)`. `somme_chiffres(2024) = 4 + somme_chiffres(202) = 4 + 2 + somme_chiffres(20) = 4 + 2 + 0 + 2 = ` **8**.

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Identifier le cas de base d'une liste ou d'une chaîne
- [ ] Écrire somme, maximum, comptage en récursif
- [ ] Dérouler un palindrome ou une inversion
- [ ] Estimer le coût des copies de tranches

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

# Exercices – Diviser pour régner

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S09*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**. Ouvre ensuite « Voir la réponse » pour te corriger. **Aucune réponse sans justification** n'est complète.

Dans les exercices 1 et 2 : \(L = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]\).

## Exercice 1 – Dichotomie

Dérouler la recherche dichotomique de 23 puis de 40 (indices `bas`, `haut`, `milieu`, valeur).

<details markdown="1">
<summary>Voir la réponse</summary>

**23** : (0, 9, 4, valeur 16 < 23) → (5, 9, 7, valeur 56 > 23) → (5, 6, 5, valeur 23) : trouvé à l'indice 5 en 3 comparaisons.
**40** : (0, 9, 4, 16) → (5, 9, 7, 56) → (5, 6, 5, 23 < 40) → (6, 6, 6, 38 < 40) → `bas = 7 > haut = 6` : absent, 4 comparaisons.

</details>

## Exercice 2 – Nombre maximal d'étapes

Combien de comparaisons au plus pour une liste triée de 1 000 éléments ? de 1 000 000 ? Et pour une recherche séquentielle au pire ?

<details markdown="1">
<summary>Voir la réponse</summary>

1 000 : \(2^9 = 512 \le 1\,000 < 2^{10}\), donc \(9 + 1 = 10\). 1 000 000 : \(2^{19} = 524\,288 \le 10^6 < 2^{20}\), donc \(19 + 1 = 20\). Au pire, la recherche séquentielle examine tous les éléments : 1 000 et 1 000 000.

</details>

## Exercice 3 – Puissance rapide

Combien de multiplications pour calculer \(x^{10}\) avec la méthode rapide ? Avec la méthode de S06 ?

<details markdown="1">
<summary>Voir la réponse</summary>

Appels : \(x^{10}\) (pair : 1 multiplication), \(x^5\) (impair : 1), \(x^4\) (pair : 1), \(x^2\) (pair : 1), \(x^1\) (impair : 1), \(x^0\) (cas de base : 0). Total **5** multiplications. La méthode de S06 en fait 10 (une par appel jusqu'à \(n = 0\)).

</details>

## Exercice 4 – Fusion

Fusionner \(A = [2, 5, 9]\) et \(B = [1, 6, 7, 10]\) en indiquant l'élément choisi à chaque étape.

<details markdown="1">
<summary>Voir la réponse</summary>

On compare les premiers éléments restants : 1 (B), 2 (A), 5 (A), 6 (B), 7 (B), 9 (A) ; A est épuisée, on recopie le reste de B : 10. Résultat : **[1, 2, 5, 6, 7, 9, 10]**.

</details>

## Exercice 5 – Tri fusion

Trier `[5, 2, 9, 1, 7]` en indiquant les découpages et les fusions.

<details markdown="1">
<summary>Voir la réponse</summary>

Découpage : `[5, 2]` | `[9, 1, 7]`. `[5, 2]` se découpe en `[5]` | `[2]` et se fusionne en `[2, 5]`. `[9, 1, 7]` se découpe en `[9]` | `[1, 7]`, `[1, 7]` en `[1]` | `[7]` ; fusion `[1, 7]` puis `[1, 7, 9]`. Fusion finale de `[2, 5]` et `[1, 7, 9]` : **[1, 2, 5, 7, 9]**.

</details>

## Exercice 6 – Nombre d'appels

Combien d'appels de `tri_fusion` pour une liste de 8 éléments ? Quelle est la profondeur ?

<details markdown="1">
<summary>Voir la réponse</summary>

Arbre binaire complet : 1 + 2 + 4 + 8 = **15** appels (\(2 \times 8 - 1\)). Il y a 4 niveaux : 3 niveaux de découpage (\(\log_2 8 = 3\)) plus le niveau des listes à un élément.

</details>

## Exercice 7 – Liste non triée

On applique la dichotomie à `[4, 1, 9, 3]` pour chercher 1. Que se passe-t-il ? Pourquoi ?

<details markdown="1">
<summary>Voir la réponse</summary>

Milieu d'indice 1 : valeur 1, trouvé par hasard. Mais pour chercher 4 : milieu 1 (valeur 1 < 4) → on cherche à droite (indices 2 à 3 : 9, 3) → milieu d'indice 2 (9 > 4) → à gauche, zone vide : **4 est jugé absent** alors qu'il est présent. La dichotomie suppose une liste **triée**.

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Dérouler une dichotomie et compter les comparaisons
- [ ] Écrire la puissance rapide en calculant la moitié une seule fois
- [ ] Fusionner deux listes triées
- [ ] Dérouler un tri fusion

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

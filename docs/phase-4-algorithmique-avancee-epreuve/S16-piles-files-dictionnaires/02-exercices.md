# Exercices – Piles, files et dictionnaires

*BTS SIO SISR 2e année – Pour aller plus loin – S16*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, puis ouvre « Voir la réponse ». **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Trace d'une pile

On empile 1, 2, 3, on dépile, on empile 4, on dépile deux fois. Quelles valeurs sont dépilées ? Que reste-t-il ?

<details markdown="1">
<summary>Voir la réponse</summary>

Dépilées : 3, puis 4, puis 2. Il reste `[1]`.

</details>

## Exercice 2 – Trace d'une file

On enfile `a`, `b`, `c`, on défile, on enfile `d`, on défile. Valeurs défilées ? État final ?

<details markdown="1">
<summary>Voir la réponse</summary>

Défilées : `a`, puis `b`. Il reste `c`, `d` (dans cet ordre).

</details>

## Exercice 3 – Parenthèses

Les chaînes `"{[()]}"`, `"([)]"`, `"(()"` sont-elles bien formées ? Justifier avec une pile.

<details markdown="1">
<summary>Voir la réponse</summary>

`"{[()]}"` : oui, la pile se vide. `"([)]"` : non, à `)` le sommet est `[`. `"(()"` : non, il reste une ouvrante dans la pile à la fin.

</details>

## Exercice 4 – Compter

Quel dictionnaire obtient-on en comptant les lettres de `"reseau"` ?

<details markdown="1">
<summary>Voir la réponse</summary>

`{"r": 1, "e": 2, "s": 1, "a": 1, "u": 1}`.

</details>

## Exercice 5 – Tourniquet

Trois tâches ont besoin de 5, 2 et 4 unités de temps. Chaque tâche s'exécute au plus 2 unités à son tour, puis retourne en fin de file si elle n'est pas finie. Dans quel ordre se terminent-elles ?

<details markdown="1">
<summary>Voir la réponse</summary>

Tour 1 : tâche 0 (reste 3, retourne en fin) ; tâche 1 (2, finie) ; tâche 2 (reste 2, retourne). Puis tâche 0 (reste 1, retourne) ; tâche 2 (finie). Puis tâche 0 (finie). Ordre de fin : **1, 2, 0**.

</details>

## Exercice 6 – Liste ou dictionnaire ?

On doit retrouver 100 000 fois une fiche parmi 100 000, par son identifiant. Comparer une liste (séquentielle) et un dictionnaire.

<details markdown="1">
<summary>Voir la réponse</summary>

Liste : au pire \(100\,000 \times 100\,000 = 10^{10}\) comparaisons. Dictionnaire : de l'ordre de \(10^5\) accès (coût moyen, d'après la documentation). Gain de l'ordre de 100 000 en nombre d'opérations ; la mémoire utilisée est plus grande.

</details>

## Je sais faire

- [ ] Dérouler une pile et une file
- [ ] Utiliser un dictionnaire pour compter
- [ ] Choisir la structure selon l'usage
- [ ] Comparer les coûts

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

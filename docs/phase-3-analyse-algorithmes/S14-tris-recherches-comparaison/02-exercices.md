# Exercices – Tris et recherches

*BTS SIO SISR 2e année – Pour aller plus loin – S14*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, puis ouvre « Voir la réponse ». **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Trace du tri par sélection

Dérouler le tri par sélection sur `[5, 2, 9, 1, 7]` et compter les comparaisons.

<details markdown="1">
<summary>Voir la réponse</summary>

`[1, 2, 9, 5, 7]`, `[1, 2, 9, 5, 7]`, `[1, 2, 5, 9, 7]`, `[1, 2, 5, 7, 9]`. Comparaisons : \(4 + 3 + 2 + 1 = 10\).

</details>

## Exercice 2 – Trace du tri par insertion

Même question pour le tri par insertion (on compte chaque évaluation de `L[j-1] > x`).

<details markdown="1">
<summary>Voir la réponse</summary>

Insérer 2 : 1 comparaison (`5 > 2`). Insérer 9 : 1 (`5 > 9` faux). Insérer 1 : 3 (`9`, `5`, `2`). Insérer 7 : 2 (`9 > 7` vrai, `5 > 7` faux). Total : **7**. Résultat `[1, 2, 5, 7, 9]`.

</details>

## Exercice 3 – Meilleur et pire cas de l'insertion

Combien de comparaisons pour une liste de 6 éléments déjà triée ? En ordre inverse ?

<details markdown="1">
<summary>Voir la réponse</summary>

Triée : \(n - 1 = 5\). Inverse : \(1 + 2 + 3 + 4 + 5 = 15 = 6 \times 5 / 2\).

</details>

## Exercice 4 – Dichotomie

Combien de comparaisons au plus pour chercher dans une liste triée de 1 000 éléments ? De 1 000 000 ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(\lfloor\log_2 1000\rfloor + 1 = 10\). \(\lfloor\log_2 10^6\rfloor + 1 = 20\).

</details>

## Exercice 5 – Rentabilité du tri

Pour \(n = 1000\), à partir de combien de recherches vaut-il mieux trier puis utiliser la dichotomie ? (On prend \(n\log_2 n \approx 9\,966\) et 10 comparaisons par dichotomie.)

<details markdown="1">
<summary>Voir la réponse</summary>

Séquentielle : \(1000k\). Tri + dicho : \(9\,966 + 10k\). On cherche \(1000k > 9\,966 + 10k\), soit \(990k > 9\,966\), \(k > 10{,}07\). Donc \(k = 11\) (10 000 contre 10 066 : non ; 11 000 contre 10 076 : oui).

</details>

## Exercice 6 – Grand volume

Pour \(n = 100\,000\) et \(k = 1000\) recherches, comparer les deux stratégies.

<details markdown="1">
<summary>Voir la réponse</summary>

Séquentielle : \(1000 \times 100\,000 = 10^8\). Tri + dicho : \(n\log_2 n \approx 1\,660\,964\), plus \(1000 \times 17 = 17\,000\), soit \(1\,677\,964\). Environ 60 fois moins.

</details>

## Je sais faire

- [ ] Dérouler un tri par sélection et par insertion
- [ ] Compter les comparaisons
- [ ] Décrire le tri fusion
- [ ] Décider s'il faut trier avant de chercher

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

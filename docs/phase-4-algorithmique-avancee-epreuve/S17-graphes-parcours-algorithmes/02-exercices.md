# Exercices – Graphes : parcours et plus court chemin

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S17*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, puis ouvre « Voir la réponse ». **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Trace du parcours en largeur

Dérouler le parcours en largeur de `g` (cours) depuis `"C"`.

<details markdown="1">
<summary>Voir la réponse</summary>

File : C. On défile C : on ajoute D, E. On défile D : rien. On défile E : on ajoute A. On défile A : on ajoute B (C est déjà vu). On défile B. Ordre : `["C", "D", "E", "A", "B"]`.

</details>

## Exercice 2 – Distances en sauts

Donner la distance en nombre de sauts de A à chaque sommet de `g`.

<details markdown="1">
<summary>Voir la réponse</summary>

A : 0 ; B : 1 ; C : 1 ; D : 2 ; E : 2.

</details>

## Exercice 3 – Profondeur ou largeur ?

Soit `h = {"A": ["B", "C"], "B": ["C"], "C": []}`. Le parcours en profondeur depuis A atteint C par un chemin de 2 sauts. Quel est le plus court chemin de A à C ?

<details markdown="1">
<summary>Voir la réponse</summary>

A → C directement : 1 saut. Le parcours en largeur le trouve, la profondeur (qui passe par B d'abord) ne le garantit pas.

</details>

## Exercice 4 – Trace de Dijkstra

Dérouler Dijkstra depuis S sur `{"S": {"A": 7, "B": 2}, "A": {"C": 1}, "B": {"A": 3, "C": 8}, "C": {}}`.

<details markdown="1">
<summary>Voir la réponse</summary>

S = 0. Traiter S : A = 7, B = 2. Traiter B (2) : A = 5 (2 + 3), C = 10. Traiter A (5) : C = 6. Traiter C (6). Résultat : S 0, B 2, A 5, C 6. Chemin vers C : S → B → A → C.

</details>

## Exercice 5 – Poids négatif

Pourquoi Dijkstra peut-il se tromper avec un poids négatif ?

<details markdown="1">
<summary>Voir la réponse</summary>

Il fixe la distance d'un sommet dès qu'il le traite, en supposant qu'aucun chemin plus long en poids ne peut devenir plus court. Avec un poids négatif, un chemin passant par d'autres sommets peut finalement coûter moins cher : la distance déjà fixée est alors fausse.

</details>

## Exercice 6 – Choisir

Réseau d'entreprise : on veut le chemin de **plus faible latence** entre deux routeurs. Quel algorithme ? Et pour le chemin qui traverse le **moins de routeurs** ?

<details markdown="1">
<summary>Voir la réponse</summary>

Latence : Dijkstra (poids = latence, positifs). Moins de routeurs : parcours en largeur.

</details>

## Je sais faire

- [ ] Représenter un graphe pondéré en dictionnaire
- [ ] Dérouler un parcours en largeur
- [ ] Dérouler Dijkstra
- [ ] Choisir l'algorithme adapté

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

# Exercices – Arborescences et parcours en profondeur

*BTS SIO SISR 2e année – Pour aller plus loin – S10*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**. Ouvre ensuite « Voir la réponse » pour te corriger. **Aucune réponse sans justification** n'est complète.

On utilise `arbo` du cours (exercices 1 à 3) et `g = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": ["A"]}` (exercices 4 et 5).

## Exercice 1 – Taille

Calculer la taille de `arbo` et celle du dossier `archives`.

<details markdown="1">
<summary>Voir la réponse</summary>

`archives` : \(500 + 650 = 1\,150\) Ko. `docs` : \(120 + 30 + 1\,150 = 1\,300\) Ko. Racine : \(1\,300 + 800 + 5 = \) **2 105** Ko.

</details>

## Exercice 2 – Fichiers et profondeur

Combien `arbo` contient-elle de fichiers ? Quelle est sa profondeur ?

<details markdown="1">
<summary>Voir la réponse</summary>

Fichiers : `rapport.txt`, `notes.txt`, `2023.zip`, `2024.zip`, `photo.png`, `config.ini` : **6**. Profondeur : `archives` = 1 + max(0, 0) = 1 ; `docs` = 1 + max(0, 0, 1) = 2 ; racine = 1 + max(2, 0, 0) = **3**.

</details>

## Exercice 3 – Chemins

Donner la liste des chemins renvoyée par `chemins(arbo)`.

<details markdown="1">
<summary>Voir la réponse</summary>

`["docs/rapport.txt", "docs/notes.txt", "docs/archives/2023.zip", "docs/archives/2024.zip", "photo.png", "config.ini"]`, dans l'ordre d'insertion des clés.

</details>

## Exercice 4 – Parcours en profondeur

Donner l'ordre de visite de `dfs(g, "A")`, puis l'ensemble des sommets atteignables depuis `"B"`.

<details markdown="1">
<summary>Voir la réponse</summary>

Depuis A : A, B (voisin de A), D (voisin de B, sans voisin), retour à A puis C, D déjà visité, E, dont le voisin A est visité. Ordre : **A, B, D, C, E**. Depuis B : B puis D, soit **{B, D}**.

</details>

## Exercice 5 – Le cycle

Que se passe-t-il si on supprime le test `voisin not in visites` ? Pourquoi ?

<details markdown="1">
<summary>Voir la réponse</summary>

Le parcours suit A → C → E → A → C → E → … sans fin : le cycle fait revenir au même sommet, et il n'y a pas de variant. Python s'arrête avec `RecursionError`. Le test sur les sommets visités rétablit le variant : le nombre de sommets non visités.

</details>

## Exercice 6 – Machines atteignables

Dans le réseau `{"R1": ["R2", "R3"], "R2": ["R4"], "R3": ["R4"], "R4": [], "R5": ["R1"]}` (liens orientés), quelles machines un message émis par R1 peut-il atteindre ? Et par R5 ?

<details markdown="1">
<summary>Voir la réponse</summary>

Depuis R1 : R1, R2, R3, R4 (R5 n'est pas atteignable : aucun lien n'y mène). Depuis R5 : R5, R1, R2, R3, R4 (**toutes**).

</details>

## Exercice 7 – Dossier vide

Que renvoient `taille({})`, `nb_fichiers({})` et `profondeur({})` ?

<details markdown="1">
<summary>Voir la réponse</summary>

`taille({}) = 0` (somme vide) ; `nb_fichiers({}) = 0` ; `profondeur({}) = 1` (un dossier vide existe encore). Pour que la formule générale \(1 + \max\) marche avec un dossier vide, on traite ce cas à part ou on utilise `max(..., default=0)`.

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Représenter une arborescence par des dictionnaires imbriqués
- [ ] Calculer taille, nombre de fichiers, profondeur récursivement
- [ ] Écrire un parcours en profondeur avec liste des sommets visités
- [ ] Expliquer pourquoi un cycle exige de mémoriser les sommets visités

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

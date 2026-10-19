# Cours – Structures arborescentes et parcours en profondeur

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S10 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S08 et S09 (récursivité sur des structures) ; dictionnaires Python (clé, valeur) ; graphes (sommets, arêtes, S16 de la 1re année).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Représenter** une arborescence en Python ;
- [ ] **Parcourir** récursivement une arborescence ;
- [ ] **Calculer** taille et profondeur ;
- [ ] **Écrire** un parcours en profondeur de graphe ;
- [ ] **Éviter** les cycles.

## I. Une arborescence de dossiers

Un dossier contient des fichiers **et d'autres dossiers**, qui en contiennent eux-mêmes : la structure est **récursive**. On la représente par un **dictionnaire** : la clé est un nom, la valeur est soit un **entier** (un fichier, avec sa taille en Ko), soit un **dictionnaire** (un sous-dossier).

```python
arbo = {
    "docs": {
        "rapport.txt": 120,
        "notes.txt": 30,
        "archives": {"2023.zip": 500, "2024.zip": 650},
    },
    "photo.png": 800,
    "config.ini": 5,
}
```

Le cas de base est le **fichier** (un entier). Le cas récursif est le **dossier** : on applique la même fonction à chacun de ses éléments.

## II. Parcours récursif

```python
def taille(a):
    if isinstance(a, int):                      # un fichier
        return a
    return sum(taille(v) for v in a.values())   # un dossier : somme de ses éléments
```

`taille(arbo)` vaut \(120 + 30 + 500 + 650 + 800 + 5 = 2\,105\) Ko.

Autres parcours sur le même modèle :

| Fonction | Fichier | Dossier |
|---|---|---|
| Nombre de fichiers | 1 | somme des nombres de fichiers des éléments |
| Profondeur | 0 | \(1 + \max\) des profondeurs des éléments (1 si vide) |
| Liste des chemins | `[préfixe + nom]` | concaténation des chemins des éléments |

Pour `arbo` : 6 fichiers ; profondeur 3 (la racine, `docs`, `archives`).

```python
def chemins(a, prefixe=""):
    resultat = []
    for nom, v in a.items():
        if isinstance(v, int):
            resultat.append(prefixe + nom)
        else:
            resultat += chemins(v, prefixe + nom + "/")
    return resultat
```

`chemins(arbo)` renvoie `["docs/rapport.txt", "docs/notes.txt", "docs/archives/2023.zip", "docs/archives/2024.zip", "photo.png", "config.ini"]`.

## III. Parcours en profondeur d'un graphe

Un réseau est un **graphe** : on le représente par un dictionnaire qui associe à chaque sommet la liste de ses voisins.

```python
g = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": ["A"]}
```

Le **parcours en profondeur** (DFS en anglais) explore un chemin **jusqu'au bout** avant de revenir en arrière.

```python
def dfs(g, sommet, visites=None):
    if visites is None:
        visites = []
    visites.append(sommet)
    for voisin in g[sommet]:
        if voisin not in visites:        # on ne repasse pas par un sommet déjà vu
            dfs(g, voisin, visites)
    return visites
```

Depuis `"A"` : A, puis B, puis D (impasse, retour), puis C, puis E (dont le voisin A est déjà visité). L'ordre est `["A", "B", "D", "C", "E"]`.

> [!WARNING]
> Un graphe peut avoir des **cycles** (ici \(A \to C \to E \to A\)). Sans la liste `visites`, le parcours reviendrait à `"A"` indéfiniment (`RecursionError`). Le **variant** est le nombre de sommets **non encore visités**, qui décroît à chaque appel.

L'ensemble des sommets visités depuis un sommet de départ est l'ensemble des sommets **atteignables** : par exemple les machines qu'un message peut atteindre.

## IV. Coût et limites

- Chaque sommet est visité **une seule fois** : le nombre d'appels est au plus le nombre de sommets.
- La profondeur de récursion peut atteindre le nombre de sommets : pour un très grand réseau, on préfère une **pile** explicite (voir S16).
- Le parcours en profondeur ne donne **pas** le plus court chemin (voir S17).

**Test flash.** Quelle est la profondeur d'un dossier vide `{}` ?

<details markdown="1">
<summary>Voir la réponse</summary>

**1** : un dossier a toujours une profondeur d'au moins 1 (lui-même), même sans élément. Seul un fichier a la profondeur 0.

</details>

## À retenir

- Arborescence : dictionnaire imbriqué ; fichier = cas de base, dossier = cas récursif.
- `isinstance(x, int)` distingue un fichier d'un dossier.
- Graphe : dictionnaire sommet → voisins ; DFS avec liste des sommets visités.
- Sans mémoire des sommets visités, un cycle provoque une récursion infinie.

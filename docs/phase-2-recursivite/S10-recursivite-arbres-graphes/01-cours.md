# Cours – Structures arborescentes et parcours en profondeur

*BTS SIO SISR 2e année – Pour aller plus loin – S10 – à lire avant les [exercices](02-exercices.md)*

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

<figure class="graphe">
<svg viewBox="0 0 420 230" role="img" aria-label="Graphe orienté à cinq sommets A à E" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="g-n" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-n"/></marker>
<marker id="g-arbre" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-arbre"/></marker>
<marker id="g-ignore" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-ignore"/></marker>
</defs>
<line x1="90.5" y1="82.0" x2="184.9" y2="44.9" class="arete n" marker-end="url(#g-n)"/>
<line x1="90.5" y1="98.0" x2="184.9" y2="135.1" class="arete n" marker-end="url(#g-n)"/>
<line x1="232.0" y1="35.0" x2="323.0" y2="35.0" class="arete n" marker-end="url(#g-n)"/>
<line x1="227.3" y1="131.4" x2="328.8" y2="51.7" class="arete n" marker-end="url(#g-n)"/>
<line x1="232.0" y1="145.0" x2="323.0" y2="145.0" class="arete n" marker-end="url(#g-n)"/>
<path d="M331.5,156.9 Q210,235 88.8,109.4" class="arete n" marker-end="url(#g-n)"/>
<circle cx="70" cy="90" r="22" class="noeud"/><text x="70" y="96" text-anchor="middle" class="nom">A</text>
<circle cx="210" cy="35" r="22" class="noeud"/><text x="210" y="41" text-anchor="middle" class="nom">B</text>
<circle cx="210" cy="145" r="22" class="noeud"/><text x="210" y="151" text-anchor="middle" class="nom">C</text>
<circle cx="350" cy="35" r="22" class="noeud"/><text x="350" y="41" text-anchor="middle" class="nom">D</text>
<circle cx="350" cy="145" r="22" class="noeud"/><text x="350" y="151" text-anchor="middle" class="nom">E</text>
</svg>
<figcaption>Le graphe <code>g</code> : une flèche va d'un sommet vers l'un de ses voisins. Le cycle A → C → E → A est celui qui oblige à mémoriser les sommets visités.</figcaption>
</figure>

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

Le même parcours en image :

<figure class="graphe">
<svg viewBox="0 0 420 230" role="img" aria-label="Ordre de visite du parcours en profondeur" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="dfs-n" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-n"/></marker>
<marker id="dfs-arbre" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-arbre"/></marker>
<marker id="dfs-ignore" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-ignore"/></marker>
</defs>
<line x1="90.5" y1="82.0" x2="184.9" y2="44.9" class="arete arbre" marker-end="url(#dfs-arbre)"/>
<line x1="232.0" y1="35.0" x2="323.0" y2="35.0" class="arete arbre" marker-end="url(#dfs-arbre)"/>
<line x1="90.5" y1="98.0" x2="184.9" y2="135.1" class="arete arbre" marker-end="url(#dfs-arbre)"/>
<line x1="232.0" y1="145.0" x2="323.0" y2="145.0" class="arete arbre" marker-end="url(#dfs-arbre)"/>
<line x1="227.3" y1="131.4" x2="328.8" y2="51.7" class="arete ignore" marker-end="url(#dfs-ignore)"/>
<path d="M331.5,156.9 Q210,235 88.8,109.4" class="arete ignore" marker-end="url(#dfs-ignore)"/>
<circle cx="70" cy="90" r="22" class="noeud"/><text x="70" y="96" text-anchor="middle" class="nom">A</text>
<circle cx="88" cy="72" r="10" class="badge"/><text x="88" y="76" text-anchor="middle" class="num">1</text>
<circle cx="210" cy="35" r="22" class="noeud"/><text x="210" y="41" text-anchor="middle" class="nom">B</text>
<circle cx="228" cy="17" r="10" class="badge"/><text x="228" y="21" text-anchor="middle" class="num">2</text>
<circle cx="210" cy="145" r="22" class="noeud"/><text x="210" y="151" text-anchor="middle" class="nom">C</text>
<circle cx="228" cy="127" r="10" class="badge"/><text x="228" y="131" text-anchor="middle" class="num">4</text>
<circle cx="350" cy="35" r="22" class="noeud"/><text x="350" y="41" text-anchor="middle" class="nom">D</text>
<circle cx="368" cy="17" r="10" class="badge"/><text x="368" y="21" text-anchor="middle" class="num">3</text>
<circle cx="350" cy="145" r="22" class="noeud"/><text x="350" y="151" text-anchor="middle" class="nom">E</text>
<circle cx="368" cy="127" r="10" class="badge"/><text x="368" y="131" text-anchor="middle" class="num">5</text>
</svg>
<figcaption>Parcours en profondeur depuis A. Le numéro (en haut à droite de chaque sommet) donne l'ordre de visite. Flèches colorées : celles que <code>dfs</code> suit. Flèches grises en pointillés : elles mènent à un sommet <strong>déjà visité</strong> (D, puis A) et sont ignorées.</figcaption>
</figure>

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

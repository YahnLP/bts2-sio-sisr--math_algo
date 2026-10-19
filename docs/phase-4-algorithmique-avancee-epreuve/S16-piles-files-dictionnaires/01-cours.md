# Cours – Piles, files et dictionnaires

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S16 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** listes et dictionnaires Python ; pile d'appels (S07) ; coût d'une recherche (S14).
> - **Outils :** Papier, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Utiliser** une pile et une file ;
- [ ] **Utiliser** un dictionnaire pour compter et retrouver ;
- [ ] **Choisir** la structure adaptée à l'usage ;
- [ ] **Évaluer** le coût des opérations ;
- [ ] **Programmer** des cas d'usage réseau.

## I. La pile : dernier arrivé, premier sorti

Une **pile** (LIFO, *last in, first out*) fonctionne comme une pile d'assiettes : on empile et on dépile **au sommet**.

```python
pile = []
pile.append(1)      # empiler
pile.append(2)
x = pile.pop()      # dépiler : x vaut 2
```

Usages : annuler la dernière action (« annuler »), vérifier des parenthèses, la pile d'appels elle-même (S07), parcours en profondeur sans récursivité.

*Exemple : parenthèses.* On empile chaque ouvrante ; sur une fermante, on dépile et on vérifie qu'elle correspond. `"{[()]}"` est bien formée ; `"([)]"` ne l'est pas.

## II. La file : premier arrivé, premier sorti

Une **file** (FIFO, *first in, first out*) fonctionne comme une file d'attente : on entre par la fin, on sort par le début.

```python
from collections import deque

file = deque()
file.append("a")        # enfiler
file.append("b")
x = file.popleft()      # défiler : x vaut "a"
```

Usages : impression, tâches à exécuter dans l'ordre d'arrivée, ordonnancement, parcours en largeur (S17).

> [!WARNING]
> Pour une file, évite `liste.pop(0)` : il décale tous les éléments suivants, donc coûte \(O(n)\). `deque.popleft()` est en \(O(1)\).

## III. Le dictionnaire : retrouver par la clé

```python
compte = {}
for ligne in journal:
    compte[ligne] = compte.get(ligne, 0) + 1
```

Un dictionnaire associe une **valeur** à une **clé** ; il sert à compter, regrouper, indexer.

## IV. Coût des opérations

| Opération | Coût typique |
|---|---|
| `liste.append(x)`, `liste.pop()` (fin) | \(O(1)\) |
| `liste.pop(0)`, `liste.insert(0, x)` | \(O(n)\) |
| `x in liste` | \(O(n)\) |
| `deque.append`, `deque.popleft` | \(O(1)\) |
| `cle in dict`, `dict[cle]`, `dict[cle] = v` | \(O(1)\) en moyenne |
| `x in set` | \(O(1)\) en moyenne |

> [!NOTE]
> Ces coûts viennent de la documentation Python (« amorti » ou « en moyenne » selon l'opération) ; ils peuvent se vérifier avec le test de doublement de S15.

## V. Choisir

| Besoin | Structure |
|---|---|
| Annuler, empiler/dépiler | pile |
| Traiter dans l'ordre d'arrivée | file |
| Retrouver par un identifiant | dictionnaire |
| Tester l'appartenance rapidement | ensemble |
| Accéder par position | liste |

**Test flash.** Quelle structure pour traiter des demandes dans l'ordre où elles arrivent ?

<details markdown="1">
<summary>Voir la réponse</summary>

Une file (FIFO).

</details>

## À retenir

- Pile : LIFO ; file : FIFO ; dictionnaire : clé → valeur.
- `pop(0)` sur une liste coûte \(O(n)\) ; `popleft` sur une `deque` coûte \(O(1)\).
- Dictionnaire et ensemble : accès en \(O(1)\) en moyenne.

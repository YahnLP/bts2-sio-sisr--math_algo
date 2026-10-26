# Cours – Tris et recherches : comparer et choisir

*BTS SIO SISR 2e année – Pour aller plus loin – S14 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** notation \(O\) (S13) ; recherche dichotomique (S09) ; listes Python.
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Dérouler** le tri par sélection et le tri par insertion ;
- [ ] **Compter** leurs comparaisons ;
- [ ] **Décrire** le principe du tri fusion et son coût ;
- [ ] **Comparer** recherche séquentielle et dichotomique ;
- [ ] **Décider** s'il est rentable de trier avant de chercher.

## I. Tri par sélection

À chaque passage, on cherche le **minimum** de la partie non triée et on l'échange avec le premier élément de cette partie.

```python
def tri_selection(L):
    L = list(L)
    for i in range(len(L) - 1):
        m = i
        for j in range(i + 1, len(L)):
            if L[j] < L[m]:
                m = j
        L[i], L[m] = L[m], L[i]
    return L
```

Nombre de comparaisons : toujours \((n-1) + (n-2) + \dots + 1 = n(n-1)/2\), quelle que soit la liste. Coût : \(O(n^2)\).

*Trace sur `[5, 2, 9, 1, 7]`* : `[1, 2, 9, 5, 7]`, puis `[1, 2, 9, 5, 7]`, puis `[1, 2, 5, 9, 7]`, puis `[1, 2, 5, 7, 9]`. 10 comparaisons.

## II. Tri par insertion

On maintient une partie gauche **déjà triée** ; on insère chaque nouvel élément à sa place en décalant les plus grands vers la droite.

```python
def tri_insertion(L):
    L = list(L)
    for i in range(1, len(L)):
        x = L[i]
        j = i
        while j > 0 and L[j - 1] > x:
            L[j] = L[j - 1]
            j = j - 1
        L[j] = x
    return L
```

Le nombre de comparaisons **dépend de la liste** :

| Liste de 5 éléments | Comparaisons |
|---|---|
| déjà triée | 4 (meilleur cas, \(O(n)\)) |
| `[5, 2, 9, 1, 7]` | 7 |
| en ordre inverse | 10 (pire cas, \(n(n-1)/2\), \(O(n^2)\)) |

## III. Tri fusion (principe)

On **coupe** la liste en deux moitiés, on **trie** chacune récursivement, puis on les **fusionne** en parcourant les deux listes triées simultanément. Il y a environ \(\log_2 n\) niveaux de découpage et chaque niveau coûte \(O(n)\) : le coût est \(O(n\log n)\) dans tous les cas.

> [!NOTE]
> Le tri intégré de Python (`sorted`, `list.sort`) est lui aussi en \(O(n\log n)\) ; en pratique on l'utilise plutôt que de réécrire un tri (à vérifier dans la documentation de la version utilisée).

## IV. Chercher : séquentiel ou dichotomique

| Méthode | Condition | Comparaisons au pire |
|---|---|---|
| Séquentielle | aucune | \(n\) |
| Dichotomique | liste **triée** | \(\lfloor\log_2 n\rfloor + 1\) |

Pour \(n = 100\,000\), la dichotomie fait au plus 17 comparaisons contre 100 000.

## V. Faut-il trier d'abord ?

Pour \(k\) recherches dans une liste de \(n\) éléments :

- sans tri : \(k \times n\) comparaisons ;
- avec tri puis dichotomie : \(\approx n\log_2 n + k(\lfloor\log_2 n\rfloor + 1)\).

*Exemple \(n = 1000\)* : \(n\log_2 n \approx 9\,966\) et une dichotomie coûte 10 comparaisons.

| \(k\) | Séquentielle | Tri + dichotomie |
|---|---|---|
| 1 | 1 000 | 9 976 |
| 10 | 10 000 | 10 066 |
| 11 | 11 000 | 10 076 |

À partir de **11 recherches**, trier d'abord devient rentable. Pour \(n = 100\,000\) et \(k = 1000\) : \(1\,677\,964\) contre \(100\,000\,000\).

**Test flash.** Combien de comparaisons fait le tri par sélection sur 8 éléments ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(8 \times 7 / 2 = 28\).

</details>

## À retenir

- Sélection : toujours \(n(n-1)/2\) comparaisons.
- Insertion : de \(n-1\) à \(n(n-1)/2\) selon la liste.
- Fusion : \(O(n\log n)\).
- Trier avant de chercher est rentable à partir d'un certain nombre de recherches.

# Aide-mémoire – Arborescences et parcours en profondeur

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S10*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Arborescence

Dictionnaire imbriqué : valeur entière = fichier (cas de base), dictionnaire = dossier (cas récursif). `isinstance(x, int)` teste un fichier.

| Fonction | Fichier | Dossier |
|---|---|---|
| Taille | la valeur | somme des éléments |
| Nombre de fichiers | 1 | somme des éléments |
| Profondeur | 0 | 1 + max des éléments (1 si vide) |
| Chemins | `préfixe + nom` | concaténation, préfixe `nom + "/"` |

## Graphe

`g = {sommet: [voisins]}`.

```python
def dfs(g, sommet, visites=None):
    if visites is None:
        visites = []
    visites.append(sommet)
    for voisin in g[sommet]:
        if voisin not in visites:
            dfs(g, voisin, visites)
    return visites
```

## Points de vigilance

- Cycle sans liste des sommets visités : `RecursionError`.
- Variant du DFS : nombre de sommets non visités.
- Atteignables = sommets visités. DFS ne donne pas le plus court chemin.
- Très grand graphe : pile explicite plutôt que récursivité (S16).

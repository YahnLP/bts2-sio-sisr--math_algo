# Cours – Coût d'un algorithme en nombre d'opérations

*BTS SIO SISR 2e année – Pour aller plus loin – S12 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** boucles imbriquées ; somme \(1 + 2 + \dots + n = n(n+1)/2\) (S03, S11).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Choisir** une opération de référence ;
- [ ] **Compter** les opérations d'une boucle simple, imbriquée, triangulaire ;
- [ ] **Distinguer** meilleur, pire et cas moyen ;
- [ ] **Compter** les tours d'une boucle qui divise par 2 ;
- [ ] **Comparer** deux coûts sur une taille donnée.

## I. Mesurer sans chronomètre

Le temps dépend de la machine. On compte plutôt un nombre d'**opérations de référence** (comparaisons, additions, accès) en fonction de la **taille** \(n\) de la donnée. Le résultat est une fonction \(n \mapsto C(n)\).

> [!WARNING]
> Le modèle est une **simplification** : on suppose que chaque opération de référence coûte autant qu'une autre. Il sert à comparer des algorithmes, pas à prédire une durée exacte.

## II. Compter dans les cas courants

| Structure | Opérations | Coût |
|---|---|---|
| Boucle simple `for i in range(n)` | 1 par tour | \(n\) |
| Deux boucles imbriquées de \(n\) tours | 1 au centre | \(n \times n = n^2\) |
| Boucle triangulaire (`j` de `i+1` à `n-1`) | 1 au centre | \(0 + 1 + \dots + (n-1) = \dfrac{n(n-1)}{2}\) |
| Boucle qui divise par 2 | 1 par tour | \(\lfloor \log_2 n \rfloor\) tours |

Pour \(n = 1000\) : \(n^2 = 1\,000\,000\), \(n(n-1)/2 = 499\,500\), et la boucle qui divise par 2 fait **9 tours** (1000, 500, 250, 125, 62, 31, 15, 7, 3, 1).

```python
def doublon(L):
    n = len(L)
    for i in range(n):
        for j in range(i + 1, n):
            if L[i] == L[j]:
                return True
    return False
```

Ici, l'opération de référence est la comparaison `L[i] == L[j]`.

## III. Meilleur, pire, cas moyen

Le coût peut dépendre de la **donnée**, pas seulement de sa taille. Pour une recherche séquentielle d'un élément dans une liste de taille \(n\) :

| Cas | Situation | Comparaisons |
|---|---|---|
| Meilleur | l'élément est en première position | 1 |
| Pire | en dernière position, ou absent | \(n\) |
| Moyen | position équiprobable, élément présent | \(\dfrac{n+1}{2}\) |

Pour `doublon` : meilleur cas 1 comparaison (les deux premiers éléments sont égaux), pire cas \(n(n-1)/2\) (aucun doublon).

> [!TIP]
> En pratique on raisonne sur le **pire cas** : c'est une garantie.

## IV. Comparer deux coûts

Si l'algorithme A coûte \(3n + 5\) et l'algorithme B coûte \(n^2/10\) :

| \(n\) | 10 | 30 | 31 | 32 | 100 |
|---|---|---|---|---|---|
| A | 35 | 95 | 98 | 101 | 305 |
| B | 10 | 90 | 96,1 | 102,4 | 1 000 |

B est meilleur pour les petites tailles, mais à partir de \(n = 32\) il devient plus coûteux que A, et l'écart se creuse.

**Test flash.** Combien de comparaisons au pire pour `doublon` sur \(n = 10\) éléments ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(10 \times 9 / 2 = 45\).

</details>

## À retenir

- On compte des **opérations de référence** en fonction de \(n\).
- Simple : \(n\) ; imbriquée : \(n^2\) ; triangulaire : \(n(n-1)/2\) ; division par 2 : \(\lfloor\log_2 n\rfloor\) tours.
- Meilleur, pire, moyen : on retient le pire cas pour une garantie.
- Un coût plus petit pour de petits \(n\) peut être plus grand pour de grands \(n\).

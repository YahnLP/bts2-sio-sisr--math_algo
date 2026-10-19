# Aide-mémoire – Coût en opérations

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S12*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Compter

| Structure | Coût |
|---|---|
| `for i in range(n)` | \(n\) |
| Deux boucles imbriquées | \(n^2\) |
| Boucle triangulaire | \(\dfrac{n(n-1)}{2}\) |
| Division par 2 jusqu'à 1 | \(\lfloor\log_2 n\rfloor\) tours |

## Recherche séquentielle (n éléments)

| Cas | Comparaisons |
|---|---|
| Meilleur | 1 |
| Pire | \(n\) |
| Moyen | \((n+1)/2\) |

## Méthode

1. Choisir l'opération de référence.
2. Exprimer le nombre de passages en fonction de \(n\).
3. Raisonner sur le pire cas pour une garantie.
4. Comparer sur des valeurs de \(n\) réalistes.

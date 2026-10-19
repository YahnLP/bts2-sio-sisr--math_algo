# Aide-mémoire – Piles, files et dictionnaires

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S16*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Structures

| Structure | Règle | Python |
|---|---|---|
| Pile | LIFO | `append`, `pop()` |
| File | FIFO | `deque`, `append`, `popleft()` |
| Dictionnaire | clé → valeur | `d[k]`, `d.get(k, 0)` |
| Ensemble | sans doublon | `set`, `x in s` |

## Coûts

| Opération | Coût |
|---|---|
| `pop()` à la fin, `append` | \(O(1)\) |
| `liste.pop(0)` | \(O(n)\) |
| `x in liste` | \(O(n)\) |
| `popleft()` | \(O(1)\) |
| dictionnaire, ensemble | \(O(1)\) en moyenne |

## Choisir

Annuler : pile. Ordre d'arrivée : file. Retrouver par identifiant : dictionnaire.

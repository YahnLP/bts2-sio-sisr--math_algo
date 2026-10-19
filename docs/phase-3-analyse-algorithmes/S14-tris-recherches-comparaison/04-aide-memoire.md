# Aide-mémoire – Tris et recherches

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S14*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Tris

| Tri | Principe | Comparaisons |
|---|---|---|
| Sélection | échanger avec le minimum du reste | toujours \(n(n-1)/2\) |
| Insertion | insérer dans la partie triée | de \(n-1\) à \(n(n-1)/2\) |
| Fusion | couper, trier, fusionner | \(O(n\log n)\) |

## Recherches

| Méthode | Pire cas |
|---|---|
| Séquentielle | \(n\) |
| Dichotomique (liste triée) | \(\lfloor\log_2 n\rfloor + 1\) |

## Trier avant de chercher ?

\[ k\,n \quad\text{contre}\quad n\log_2 n + k(\lfloor\log_2 n\rfloor + 1) \]

Pour \(n = 1000\), le tri devient rentable dès \(k = 11\).

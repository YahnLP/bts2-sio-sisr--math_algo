# Aide-mémoire – Récursivité sur les tableaux et les chaînes

*BTS SIO SISR 2e année – Pour aller plus loin – S08*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Structure d'une liste ou d'une chaîne

Vide (ou courte) = cas de base ; `L[0]` + `L[1:]` = cas récursif. Variant : `len(L)`.

## Modèles

| Problème | Cas de base | Cas récursif |
|---|---|---|
| Somme | `[]` : 0 | `L[0] + somme(L[1:])` |
| Maximum | 1 élément : `L[0]` | comparer `L[0]` et `maximum(L[1:])` |
| Comptage | `[]` : 0 | `(L[0] == x)` + `compte(L[1:], x)` |
| Présence | `[]` : `False` | `L[0] == x or present(L[1:], x)` |
| Inversion | `""` : `""` | `inverse(s[1:]) + s[0]` |
| Palindrome | `len(s) <= 1` : `True` | `s[0] == s[-1] and est_palindrome(s[1:-1])` |
| Somme des chiffres | `n < 10` : `n` | `n % 10 + somme_chiffres(n // 10)` |

## Coût

- `L[1:]` copie : \(n(n-1)/2\) éléments copiés au total.
- Profondeur \(n + 1\) : une liste de 1 000 éléments dépasse la limite habituelle.
- Remède : passer un indice, ou utiliser une boucle.

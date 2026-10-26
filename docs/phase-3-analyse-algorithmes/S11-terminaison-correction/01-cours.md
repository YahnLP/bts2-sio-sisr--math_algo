# Cours – Terminaison et correction d'un algorithme

*BTS SIO SISR 2e année – Pour aller plus loin – S11 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** boucles `POUR` / `TANT QUE` (S04 de la 1re année) ; variant d'une fonction récursive (S06).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Trouver** un variant de boucle ;
- [ ] **Énoncer** un invariant ;
- [ ] **Prouver** la correction d'une boucle simple ;
- [ ] **Écrire** des tests pertinents ;
- [ ] **Repérer** les cas limites.

## I. Deux questions à poser à tout algorithme

1. **Termine-t-il ?** Sur toute donnée valide, s'arrête-t-il après un nombre fini d'étapes ?
2. **Est-il correct ?** Quand il s'arrête, le résultat est-il celui qu'on attend ?

Il faut aussi préciser la **spécification** : la **précondition** (ce que l'on suppose vrai en entrée, par exemple « la liste est non vide ») et la **postcondition** (ce que l'on garantit en sortie, par exemple « `m` est le plus grand élément »).

## II. Terminaison : le variant

Un **variant** de boucle est une expression à valeurs **entières**, qui reste **positive ou nulle** et **diminue strictement** à chaque tour. Elle ne peut pas diminuer indéfiniment : la boucle s'arrête.

```python
while n > 0:
    n = n // 2
```

Variant : `n`. Pour `n > 0`, on a `n // 2 < n`, et `n // 2 >= 0`. Pour `n = 100`, les valeurs successives sont 100, 50, 25, 12, 6, 3, 1, 0 : **7 tours**.

Un variant faux, c'est une boucle qui ne s'arrête pas :

```python
i = 0
while i != 10:       # 0, 3, 6, 9, 12, 15, ... : jamais égal à 10
    i = i + 3
```

On corrige avec une condition qui garantit la décroissance : `while i < 10`, dont le variant est `10 - i`.

## III. Correction : l'invariant

Un **invariant** de boucle est une propriété qui est :

1. **vraie avant** le premier tour (initialisation) ;
2. **conservée** par chaque tour : si elle est vraie avant, elle l'est après (conservation) ;
3. **utile à la sortie** : combinée avec la condition d'arrêt, elle donne la postcondition (conclusion).

*Exemple : somme de 1 à n.*

```python
s = 0
for i in range(1, n + 1):
    s = s + i
```

Invariant : après \(k\) tours, `s` vaut \(1 + 2 + \dots + k = \dfrac{k(k+1)}{2}\).

- Initialisation : avant le premier tour (\(k = 0\)), `s = 0`.
- Conservation : au tour \(k+1\), `s` devient \(\dfrac{k(k+1)}{2} + (k+1) = \dfrac{(k+1)(k+2)}{2}\).
- Conclusion : après \(n\) tours, `s` vaut \(\dfrac{n(n+1)}{2}\).

*Exemple : maximum d'une liste non vide.* Invariant : après avoir examiné les \(k\) premiers éléments, `m` est le plus grand d'entre eux. À la sortie (\(k\) = longueur), `m` est le plus grand élément de la liste.

## IV. Tester : cas typiques et cas limites

Une preuve est idéale ; des **tests** sont indispensables. On teste :

| Catégorie | Exemples pour une fonction sur une liste |
|---|---|
| Cas **typique** | `[3, 1, 2]` |
| Cas **limite** : taille minimale | `[5]` (un seul élément) |
| Cas **limite** : répétitions | `[2, 2, 2]` |
| Cas **limite** : valeurs extrêmes | négatifs, zéro |
| Cas **interdit** | liste vide si la précondition l'exclut |
| Cas **déjà ordonné / inversé** | `[1, 2, 3]`, `[3, 2, 1]` |

```python
assert maximum([3, 1, 2]) == 3
assert maximum([5]) == 5
assert maximum([-4, -1, -9]) == -1
```

> [!WARNING]
> Des tests qui réussissent **ne prouvent pas** qu'un algorithme est correct : ils montrent seulement qu'il est correct sur les cas essayés. Un invariant explique pourquoi il l'est sur tous.

**Test flash.** Pour `while n > 1: n = n - 1`, donner un variant et le nombre de tours pour `n = 5`.

<details markdown="1">
<summary>Voir la réponse</summary>

Variant : `n - 1` (positif ou nul, diminue de 1). 4 tours : 5, 4, 3, 2, 1.

</details>

## À retenir

- Terminaison : **variant** entier, positif ou nul, strictement décroissant.
- Correction : **invariant** vrai à l'initialisation, conservé, utile à la sortie.
- Spécification : précondition et postcondition.
- Tests : typiques **et** limites ; ils ne remplacent pas la preuve.

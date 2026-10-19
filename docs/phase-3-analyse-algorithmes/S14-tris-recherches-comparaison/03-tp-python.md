---
render_macros: true
---

# TP Python – Tris, comparaisons et choix

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S14*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Tri par sélection

Écris `tri_selection(L)` qui renvoie une **nouvelle** liste triée (sans modifier `L`), par la méthode de sélection. Pas de `sorted`.

**J'anticipe.** Rappelle la trace de l'exercice 1.

{{ IDE('tri_selection', MAX="+") }}

## Exercice B – Tri par insertion

Écris `tri_insertion(L)` qui renvoie une **nouvelle** liste triée, par insertion, sans `sorted`.

{{ IDE('tri_insertion', MAX="+") }}

## Exercice C – Comparaisons de la sélection

Écris `comparaisons_selection(L)` qui renvoie le nombre de comparaisons `L[j] < L[m]` faites par le tri par sélection de `L`. Pense à la formule : tu peux la programmer directement ou compter dans la boucle.

{{ IDE('comparaisons_selection', MAX="+") }}

## Exercice D – Comparaisons de l'insertion

Écris `comparaisons_insertion(L)` qui compte les évaluations de `L[j - 1] > x` dans le tri par insertion de `L` (la condition `j > 0` n'est pas comptée).

**J'anticipe.** Retrouve 7 pour `[5, 2, 9, 1, 7]` (exercice 2).

{{ IDE('comparaisons_insertion', MAX="+") }}

## Exercice E – Coût de k recherches

Écris `cout_recherches(n, k)` qui renvoie le couple `(sequentielle, tri_dicho)` avec `sequentielle = k * n` et `tri_dicho = round(n * log2(n)) + k * (floor(log2(n)) + 1)` pour `n >= 2`.

**J'anticipe.** Retrouve le tableau du cours pour n = 1000.

{{ IDE('cout_recherches', MAX="+") }}

**Je comprends.** Que représente le terme `round(n * log2(n))` ?

## Exercice F – Quelle stratégie ?

Écris `meilleur_choix(n, k)` qui renvoie `"sequentielle"` si son coût est inférieur ou égal à celui de tri + dichotomie, sinon `"tri+dicho"`. Utilise la même formule qu'en E (recopie-la).

{{ IDE('meilleur_choix', MAX="+") }}

---
render_macros: true
---

# TP Python – Compter les opérations

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S12*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Somme avec compteur

Écris `somme_compte(n)` qui calcule `s = 0 ; for i in range(n): s = s + i` et renvoie le couple `(s, nb_additions)`.

**J'anticipe.** Combien d'additions pour `n = 5` ?

{{ IDE('somme_compte', MAX="+") }}

## Exercice B – Recherche séquentielle comptée

Écris `recherche_compte(L, x)` qui parcourt `L` de gauche à droite et renvoie `(indice, nb_comparaisons)` à la première occurrence de `x`, ou `(-1, len(L))` si `x` est absent.

**J'anticipe.** Combien de comparaisons pour trouver 3 dans `[3, 5, 7]` ? Et 7 ? Et 9 ?

{{ IDE('recherche_compte', MAX="+") }}

## Exercice C – Doublons comptés

Écris `doublons_compte(L)` qui applique la méthode des deux boucles (`i`, puis `j` de `i+1` à la fin) et renvoie `(a_doublon, nb_comparaisons)` ; elle s'arrête à la première égalité trouvée.

**J'anticipe.** Pour `[1, 2, 1, 4]`, dans quel ordre les comparaisons ont-elles lieu ?

{{ IDE('doublons_compte', MAX="+") }}

**Je comprends.** Que vaut le nombre de comparaisons pour une liste de 10 éléments sans doublon ?

## Exercice D – Tours d'une division

Écris `tours_log2(n)` qui renvoie le nombre de tours de `while n > 1: n = n // 2` (pour `n >= 1`).

**J'anticipe.** Combien de tours pour `n = 1000` (exercice 4) ?

{{ IDE('tours_log2', MAX="+") }}

## Exercice E – Premier n où B dépasse A

Écris `premier_n_pire(f, g)` qui renvoie le plus petit entier `n >= 1` tel que `g(n) > f(n)`. On suppose qu'un tel `n` existe (pas de boucle infinie sur les cas de test).

**J'anticipe.** Que renvoie l'appel pour A = 3n + 5 et B = n²/10 (exercice 5) ?

{{ IDE('premier_n_pire', MAX="+") }}

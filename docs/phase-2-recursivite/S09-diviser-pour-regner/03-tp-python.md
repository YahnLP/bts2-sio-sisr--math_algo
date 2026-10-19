---
render_macros: true
---

# TP Python – Dichotomie, puissance rapide et tri fusion

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S09*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Recherche dichotomique

Écris `dicho(L, x)` qui renvoie l'indice de `x` dans la liste **triée** `L` (valeurs distinctes), ou `-1` s'il est absent, par dichotomie (récursive ou avec une boucle).

**J'anticipe.** Pour `L = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]` et `x = 23`, quel indice attends-tu ?

{{ IDE('dicho', MAX="+") }}

**Je comprends.** Quel est le variant (nombre d'éléments restant à examiner) ?

## Exercice B – Compter les comparaisons

Écris `etapes_dicho(L, x)` qui renvoie le nombre d'éléments examinés (un par milieu) par la dichotomie, que `x` soit présent ou non.

**J'anticipe.** Quelles valeurs attends-tu pour 23 et pour 40 (exercice 1) ?

{{ IDE('etapes_dicho', MAX="+") }}

**Je comprends.** Compare avec \(\lfloor \log_2 n \rfloor + 1\) pour `len(L) = 10`.

## Exercice C – Puissance rapide

Écris `puissance_rapide(x, n)` (\(n \ge 0\)) récursive : si `n` est pair, calcule `y = puissance_rapide(x, n // 2)` **une seule fois** et renvoie `y * y` ; sinon `x * puissance_rapide(x, n - 1)`.

{{ IDE('puissance_rapide', MAX="+") }}

**Je comprends.** Que se passerait-il pour le nombre d'appels si tu écrivais deux fois l'appel sur `n // 2` ?

## Exercice D – Fusion de deux listes triées

Écris `fusion(A, B)` qui renvoie la liste triée contenant les éléments de `A` et de `B`, deux listes déjà triées, en un seul passage (deux indices).

**J'anticipe.** Écris la fusion de `[2, 5, 9]` et `[1, 6, 7, 10]` étape par étape.

{{ IDE('fusion', MAX="+") }}

## Exercice E – Tri fusion

Écris `tri_fusion(L)` récursive qui renvoie une **nouvelle** liste triée. Tu peux réécrire ou réutiliser `fusion` : copie sa définition dans l'éditeur.

{{ IDE('tri_fusion', MAX="+") }}

**Je comprends.** Quel est le cas de base ? Quel est le variant ?

## Exercice F – Multiplications de la puissance rapide

Écris `nb_mult(n)` qui renvoie le nombre de multiplications effectuées par `puissance_rapide(x, n)` : 0 si `n == 0` ; `1 + nb_mult(n // 2)` si `n` est pair ; `1 + nb_mult(n - 1)` sinon.

**J'anticipe.** Pour `n = 10`, combien (exercice 3) ?

{{ IDE('nb_mult', MAX="+") }}

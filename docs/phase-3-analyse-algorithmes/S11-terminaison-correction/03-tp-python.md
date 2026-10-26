---
render_macros: true
---

# TP Python – Variants, invariants et tests

*BTS SIO SISR 2e année – Pour aller plus loin – S11*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Compter les tours

Écris `tours_division(n)` qui renvoie le nombre de tours de la boucle `while n > 0: n = n // 2` pour `n >= 0` (la boucle est à écrire, avec un compteur).

**J'anticipe.** Combien de tours pour `n = 100` (exercice 1) ?

{{ IDE('tours_division', MAX="+") }}

**Je comprends.** Quel est le variant ? Quelle fonction connue de `n` obtiens-tu (cherche : `n.bit_length()`) ?

## Exercice B – Observer un invariant

Écris `etats_somme(n)` qui renvoie la liste `[s_0, s_1, ..., s_n]` des valeurs de `s` avant le premier tour puis après chaque tour de `s = 0` ; `for i in range(1, n + 1): s = s + i`.

**J'anticipe.** Écris sur ta feuille les valeurs pour `n = 4`.

{{ IDE('etats_somme', MAX="+") }}

**Je comprends.** Vérifie que `s_k` vaut `k * (k + 1) // 2` : c'est l'invariant de l'exercice 3.

## Exercice C – Maximum d'une liste

Écris `maximum_boucle(L)` (liste non vide) avec une boucle et l'invariant de l'exercice 4. Pas de `max`.

{{ IDE('maximum_boucle', MAX="+") }}

**Je comprends.** Quel test limite as-tu essayé en premier ? Que se passe-t-il pour `L = []` ?

## Exercice D – Liste triée ?

Écris `est_trie(L)` qui renvoie `True` si la liste est triée par ordre croissant (au sens large), `False` sinon, en examinant **toutes** les paires consécutives. Les tests incluent les pièges de l'exercice 7.

**J'anticipe.** Pourquoi `est_trie([1, 2, 0])` doit-il renvoyer `False` ?

{{ IDE('est_trie', MAX="+") }}

## Exercice E – PGCD avec invariant

Écris `pgcd_boucle(a, b)` (entiers positifs ou nuls) avec une boucle : `while b != 0: a, b = b, a % b`. L'**invariant** est « le PGCD de `a` et `b` ne change pas » ; le **variant** est `b`.

**J'anticipe.** Écris les valeurs successives de `(a, b)` pour `(252, 105)`.

{{ IDE('pgcd_boucle', MAX="+") }}

**Je comprends.** Pourquoi `b` décroît-il strictement ? Que vaut le résultat à la sortie ?

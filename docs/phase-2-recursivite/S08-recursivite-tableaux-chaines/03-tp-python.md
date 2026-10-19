---
render_macros: true
---

# TP Python – Listes et chaînes en récursif

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S08*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Somme d'une liste

Écris `somme_liste(L)` de façon récursive (pas de `sum`, pas de boucle).

**J'anticipe.** Combien d'appels pour une liste de 3 éléments ?

{{ IDE('somme_liste', MAX="+") }}

## Exercice B – Maximum

Écris `maximum(L)` (liste non vide) de façon récursive, sans `max`.

{{ IDE('maximum', MAX="+") }}

**Je comprends.** Pourquoi le cas de base est-il une liste à un élément et non la liste vide ?

## Exercice C – Occurrences

Écris `compte(L, x)` qui renvoie le nombre d'occurrences de `x` dans `L`, de façon récursive.

{{ IDE('compte', MAX="+") }}

## Exercice D – Palindrome

Écris `est_palindrome(s)` qui renvoie `True` si la chaîne se lit pareil dans les deux sens (exactement, sans ignorer majuscules ni espaces), de façon récursive.

**J'anticipe.** Écris les appels pour `"radar"` puis `"reseau"`.

{{ IDE('est_palindrome', MAX="+") }}

**Je comprends.** Quel est le variant ? Pourquoi décroît-il de 2 ?

## Exercice E – Inverser une chaîne

Écris `inverse(s)` qui renvoie la chaîne à l'envers, de façon récursive (sans `[::-1]`).

{{ IDE('inverse', MAX="+") }}

## Exercice F – Somme des chiffres

Écris `somme_chiffres(n)` (entier \(n \ge 0\)) de façon récursive, sans `str` : `n % 10` est le dernier chiffre, `n // 10` le reste.

{{ IDE('somme_chiffres', MAX="+") }}

**Je comprends.** Quel est le variant ? Combien d'appels pour un nombre à 4 chiffres ?

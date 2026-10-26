---
render_macros: true
---

# TP Python – Suites, Fibonacci et mémoïsation

*BTS SIO SISR 2e année – Pour aller plus loin – S07*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Une suite récurrente

Écris `u_rec(n)` pour la suite \(u_0 = 3\), \(u_{n+1} = 2u_n - 1\), de façon récursive.

**J'anticipe.** Que vaut `u_rec(4)` ?

{{ IDE('u_rec', MAX="+") }}

## Exercice B – Fibonacci naïf

Écris `fib(n)` (\(F_0 = 0\), \(F_1 = 1\)) avec deux appels récursifs.

**J'anticipe.** Combien d'appels pour `fib(5)` ?

{{ IDE('fib', MAX="+") }}

## Exercice C – Compter les appels

Écris `appels_fib(n)` qui renvoie le nombre d'appels que ferait `fib(n)` (sans calculer Fibonacci) : 1 si `n < 2`, sinon `1 + appels_fib(n-1) + appels_fib(n-2)`.

**J'anticipe.** Vérifie à la main `appels_fib(5)` avec le tableau du cours.

{{ IDE('appels_fib', MAX="+") }}

**Je comprends.** Pourquoi ce nombre croît-il si vite ? Par combien est-il à peu près multiplié à chaque rang ?

## Exercice D – Fibonacci mémoïsé

Écris `fib_memo(n, cache=None)` avec un dictionnaire `cache` créé dans la fonction si besoin (pas de dictionnaire par défaut partagé).

{{ IDE('fib_memo', MAX="+") }}

**Je comprends.** Pourquoi `cache=None` et non `cache={}` ?

## Exercice E – Fibonacci itératif

Écris `fib_iter(n)` avec une boucle et deux variables `a`, `b`.

**J'anticipe.** Écris la trace de `a` et `b` pour `n = 6` (exercice 7).

{{ IDE('fib_iter', MAX="+") }}

**Je comprends.** Quel est l'invariant de ta boucle ?

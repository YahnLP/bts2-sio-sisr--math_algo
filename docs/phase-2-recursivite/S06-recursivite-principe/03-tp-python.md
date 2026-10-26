---
render_macros: true
---

# TP Python – Premières fonctions récursives

*BTS SIO SISR 2e année – Pour aller plus loin – S06*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Factorielle

Écris `factorielle(n)` (\(n \ge 0\)) **sans boucle**, avec un cas de base et un appel récursif.

**J'anticipe.** Combien d'appels pour `factorielle(5)` ?

{{ IDE('factorielle', MAX="+") }}

**Je comprends.** Quel est le variant ? Que se passerait-il en appelant `factorielle(-1)` ?

## Exercice B – Somme des carrés

Écris `somme_carres(n)` qui renvoie \(1^2 + \dots + n^2\), de façon récursive (exercice 2).

{{ IDE('somme_carres', MAX="+") }}

## Exercice C – Puissance

Écris `puissance(x, n)` (\(n \ge 0\)) qui renvoie \(x^n\) de façon récursive, sans utiliser `**`.

{{ IDE('puissance', MAX="+") }}

## Exercice D – Algorithme d'Euclide

Écris `pgcd(a, b)` (entiers positifs ou nuls) avec l'algorithme d'Euclide récursif : si `b == 0`, le PGCD est `a` ; sinon c'est `pgcd(b, a % b)`.

**J'anticipe.** Écris sur ta feuille les appels de `pgcd(252, 105)`.

{{ IDE('pgcd', MAX="+") }}

**Je comprends.** Quel est le variant ? Pourquoi décroît-il strictement ?

## Exercice E – Écriture en binaire

Écris `binaire(n)` (\(n \ge 0\)) qui renvoie l'écriture de `n` en base 2 sous forme de chaîne, de façon récursive : si `n < 2`, c'est `str(n)` ; sinon `binaire(n // 2)` suivi du dernier bit `n % 2`.

**J'anticipe.** Que renvoie `binaire(10)` (exercice 6) ?

{{ IDE('binaire', MAX="+") }}

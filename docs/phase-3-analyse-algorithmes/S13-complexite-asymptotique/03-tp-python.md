---
render_macros: true
---

# TP Python – Rapports de coût et durées

*BTS SIO SISR 2e année – Pour aller plus loin – S13*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Ratio de doublement

Écris `ratio_doublement(f, n)` qui renvoie `f(2 * n) / f(n)`.

**J'anticipe.** Que vaut ce ratio pour `f(n) = n` ? Pour `f(n) = n²` ?

{{ IDE('ratio_doublement', MAX="+") }}

## Exercice B – Estimer la classe

Écris `estime_ordre(f)` qui calcule le ratio de doublement en `n = 64` et renvoie une chaîne : `"O(1)"` si ratio < 1,05 ; `"O(log n)"` si < 1,5 ; `"O(n)"` si < 2,1 ; `"O(n log n)"` si < 3 ; `"O(n^2)"` si < 5 ; `"O(n^3)"` si < 9 ; sinon `"O(2^n)"`. C'est une **heuristique** : elle ne prouve rien.

**J'anticipe.** Calcule à la main les ratios en 64 pour n, n log2 n, log2 n.

{{ IDE('estime_ordre', MAX="+") }}

**Je comprends.** Trouve une fonction que cette heuristique classe mal (indice : une constante grande devant un petit terme).

## Exercice C – Opérations en jours

Écris `duree_jours(ops, par_seconde)` qui renvoie la durée en jours (1 jour = 86 400 s) de `ops` opérations à `par_seconde` opérations par seconde.

**J'anticipe.** Reprends l'exercice 6 : à quoi sert l'hypothèse de vitesse ?

{{ IDE('duree_jours', MAX="+") }}

## Exercice D – Facteur de croissance

Écris `facteur_croissance(f, a, b)` qui renvoie `f(b) / f(a)`. Utilise-la pour retrouver le rapport 13,33 de l'exercice 5 avec `f(n) = n * log2(n)`.

{{ IDE('facteur_croissance', MAX="+") }}

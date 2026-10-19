---
render_macros: true
---

# TP Python – Suites arithmétiques en Python

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S02*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Terme général

Écris `terme_arith(u0, r, n)` qui renvoie \(u_n = u_0 + nr\).

**J'anticipe.** Pour `u0 = 12`, `r = 5`, `n = 20`, quelle valeur attends-tu ?

{{ IDE('terme_arith', MAX="+") }}

## Exercice B – Somme de termes

Écris `somme_arith(u0, r, n)` qui renvoie \(u_0 + u_1 + \dots + u_n\) avec la formule (pas de boucle), en nombres entiers.

**J'anticipe.** Combien de termes la somme contient-elle pour `n = 20` ?

{{ IDE('somme_arith', MAX="+") }}

**Je comprends.** Vérifie ta fonction avec `sum(...)` sur quelques valeurs : pourquoi cette double vérification est-elle utile ?

## Exercice C – Est-ce arithmétique ?

Écris `est_arithmetique(liste)` qui renvoie `True` si les différences entre éléments consécutifs sont toutes égales. Une liste de 0, 1 ou 2 éléments est arithmétique.

{{ IDE('est_arithmetique', MAX="+") }}

**Je comprends.** Une liste finie arithmétique prouve-t-elle que la **suite** l'est ?

## Exercice D – Nombre de termes d'une plage

Écris `nb_termes(a, b, pas)` qui renvoie combien d'entiers de la forme \(a, a+\text{pas}, a+2\,\text{pas}, \dots\) sont inférieurs ou égaux à `b` (avec `pas > 0`). Renvoie 0 si `b < a`.

**J'anticipe.** Combien y a-t-il de termes dans 10, 14, ..., 250 (exercice 6) ?

{{ IDE('nb_termes', MAX="+") }}

## Exercice E – Quelle offre choisir ?

Deux offres coûtent `a0 + ra * n` et `b0 + rb * n`. Écris `rang_moins_cher(a0, ra, b0, rb)` qui renvoie le plus petit entier \(n \ge 0\) pour lequel l'offre B est **strictement** moins chère que A, en supposant `rb < ra` (sinon la boucle ne s'arrêterait pas).

**J'anticipe.** Pour A : 30 + 4n et B : 50 + 3n, quel rang attends-tu (exercice 7) ?

{{ IDE('rang_moins_cher', MAX="+") }}

**Je comprends.** Quel est le variant de ta boucle ? Pourquoi l'hypothèse `rb < ra` est-elle indispensable ?

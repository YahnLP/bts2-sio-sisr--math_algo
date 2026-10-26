---
render_macros: true
---

# TP Python – Suites géométriques en Python

*BTS SIO SISR 2e année – Pour aller plus loin – S03*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Terme général

Écris `terme_geo(u0, q, n)` qui renvoie \(u_n = u_0 q^n\).

**J'anticipe.** Pour `u0 = 3`, `q = 2`, `n = 10`, quelle valeur attends-tu ?

{{ IDE('terme_geo', MAX="+") }}

## Exercice B – Somme de termes

Écris `somme_geo(u0, q, n)` qui renvoie \(u_0 + \dots + u_n\) pour des entiers, avec la formule (traite à part le cas `q == 1`).

**J'anticipe.** Pour `u0 = 1`, `q = 2`, `n = 9`, quelle somme attends-tu (exercice 6) ?

{{ IDE('somme_geo', MAX="+") }}

**Je comprends.** Pourquoi la division `//` est-elle exacte ici ?

## Exercice C – Est-ce géométrique ?

Écris `est_geometrique(liste)` qui renvoie `True` s'il existe un nombre `q` tel que chaque élément soit `q` fois le précédent. Utilise `Fraction` pour éviter les erreurs d'arrondi. Une liste de 0 ou 1 élément est géométrique ; si le premier élément est nul, tous les suivants doivent l'être.

{{ IDE('est_geometrique', MAX="+") }}

**Je comprends.** Pourquoi un test d'égalité entre flottants serait-il risqué ici ?

## Exercice D – Évolution en pourcentage

Écris `valeur_apres(valeur, taux, periodes)` qui renvoie la valeur obtenue après `periodes` évolutions de `taux` % (négatif pour une baisse), arrondie à 2 décimales avec `round`.

**J'anticipe.** Pour 2 000 € avec un taux de −15 % pendant 4 ans, que vaut le résultat (exercice 5) ?

{{ IDE('valeur_apres', MAX="+") }}

## Exercice E – Premier rang dépassant un seuil

Écris `rang_depasse(u0, q, seuil)` qui renvoie le plus petit \(n\) tel que \(u_0 q^n \ge \text{seuil}\), avec `u0 > 0` et `q > 1`, en multipliant à chaque tour (pas de formule avec logarithme).

**J'anticipe.** Pour le trafic de l'exercice 4 (500, 1,2, 2000), quel rang attends-tu ?

{{ IDE('rang_depasse', MAX="+") }}

**Je comprends.** Pourquoi les hypothèses `u0 > 0` et `q > 1` garantissent-elles l'arrêt ?

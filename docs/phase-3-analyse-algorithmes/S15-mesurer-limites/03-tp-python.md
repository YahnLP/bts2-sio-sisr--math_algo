---
render_macros: true
---

# TP Python – Mesures et explosions

*BTS SIO SISR 2e année – Pour aller plus loin – S15*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Temps minimal

Écris `temps_min(f, repetitions)` qui appelle `f()` `repetitions` fois, mesure chaque durée avec `time.perf_counter()` et renvoie la plus petite (un `float` positif ou nul).

**J'anticipe.** Pourquoi garder le minimum plutôt que la moyenne ?

{{ IDE('temps_min', MAX="+") }}

## Exercice B – Essais de force brute

Écris `essais_force_brute(taille_alphabet, longueur)` qui renvoie le nombre d'essais de la force brute.

**J'anticipe.** Retrouve les valeurs de l'exercice 2.

{{ IDE('essais_force_brute', MAX="+") }}

## Exercice C – Durée de la force brute

Écris `jours_force_brute(taille_alphabet, longueur, par_seconde)` qui renvoie la durée **maximale** en jours (tous les essais) à `par_seconde` essais par seconde.

{{ IDE('jours_force_brute', MAX="+") }}

**Je comprends.** Quelle est ton hypothèse de vitesse ? Pourquoi faut-il toujours l'annoncer ?

## Exercice D – Nombre de tournées

Écris `nb_tournees(n)` qui renvoie `(n - 1)!` pour `n >= 1`. Calcule la factorielle avec une boucle (sans `math.factorial`).

{{ IDE('nb_tournees', MAX="+") }}

## Exercice E – Doublons avec un ensemble

Écris `doublons_set(L)` qui renvoie `True` si `L` contient au moins deux éléments égaux, en utilisant un ensemble (`set`).

{{ IDE('doublons_set', MAX="+") }}

**Je comprends.** Quel est le coût mémoire de cette méthode ?

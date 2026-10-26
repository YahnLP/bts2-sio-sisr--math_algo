---
render_macros: true
---

# TP Python – Calculer des suites en Python

*BTS SIO SISR 2e année – Pour aller plus loin – S01*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Formule explicite

Écris `terme_explicite(n)` qui renvoie \(u_n = 3n^2 - n + 2\).

**J'anticipe.** Pour `n = 3`, calcule à la main \(u_3\) avant de coder.

{{ IDE('terme_explicite', MAX="+") }}

## Exercice B – Une suite définie par récurrence

Écris `terme_recurrent(u0, n)` qui renvoie \(u_n\) pour la suite \(u_{n+1} = 2u_n + 1\) de premier terme `u0`, avec une boucle.

**J'anticipe.** Écris la trace de `terme` pour `u0 = 1` et `n = 4` avant de coder.

{{ IDE('terme_recurrent', MAX="+") }}

**Je comprends.** Quel est l'invariant de ta boucle (que vaut `terme` après `k` tours) ?

## Exercice C – Liste des premiers termes

Écris `premiers_termes(f, u0, n)` qui renvoie la liste \([u_0, u_1, \dots, u_n]\) pour la suite \(u_{k+1} = f(u_k)\). Par exemple, `premiers_termes(lambda x: x + 3, 2, 4)` donne `[2, 5, 8, 11, 14]`.

{{ IDE('premiers_termes', MAX="+") }}

**Je comprends.** Combien la liste renvoyée contient-elle d'éléments ? Pourquoi ?

## Exercice D – Une suite est-elle croissante ?

Écris `est_croissante(liste)` qui renvoie `True` si chaque élément est supérieur ou égal au précédent, `False` sinon. Une liste vide ou à un seul élément est croissante.

{{ IDE('est_croissante', MAX="+") }}

**Je comprends.** Un test sur une liste finie prouve-t-il qu'une **suite** est croissante pour tout \(n\) ? Qu'en conclus-tu ?

## Exercice E – Remplissage d'un disque

Un disque contient `depart` Go à la fin du mois 0 et reçoit `ajout` Go chaque mois. Écris `mois_plein(depart, ajout, capacite)` qui renvoie le premier mois \(n\) où la quantité atteint ou dépasse `capacite` (avec `ajout > 0`).

**J'anticipe.** Pour `depart = 120`, `ajout = 15`, `capacite = 300`, quel mois attends-tu (exercice 3) ?

{{ IDE('mois_plein', MAX="+") }}

**Je comprends.** Quel est le variant de ta boucle ? Pourquoi s'arrête-t-elle si `ajout > 0` ?

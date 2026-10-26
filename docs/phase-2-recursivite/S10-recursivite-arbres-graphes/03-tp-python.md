---
render_macros: true
---

# TP Python – Arborescences et graphes en Python

*BTS SIO SISR 2e année – Pour aller plus loin – S10*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Taille d'un dossier

Écris `taille(a)` qui renvoie la taille totale d'une arborescence (dictionnaires imbriqués ; un fichier est un entier). `isinstance(a, int)` teste si `a` est un fichier.

**J'anticipe.** Quelle taille attends-tu pour l'arborescence du cours (exercice 1) ?

{{ IDE('taille', MAX="+") }}

## Exercice B – Nombre de fichiers

Écris `nb_fichiers(a)` qui renvoie le nombre de fichiers (entiers) de l'arborescence.

{{ IDE('nb_fichiers', MAX="+") }}

## Exercice C – Profondeur

Écris `profondeur(a)` : 0 pour un fichier ; pour un dossier, 1 plus la plus grande profondeur de ses éléments (1 pour un dossier vide).

**J'anticipe.** Quelle profondeur attends-tu pour l'arborescence du cours (exercice 2) ?

{{ IDE('profondeur', MAX="+") }}

**Je comprends.** Quel est le variant de ta fonction ?

## Exercice D – Liste des chemins

Écris `chemins(a, prefixe="")` qui renvoie la liste des chemins de tous les fichiers, sous la forme `"docs/archives/2023.zip"`, dans l'ordre des clés.

**J'anticipe.** Écris la liste attendue pour l'arborescence du cours (exercice 3).

{{ IDE('chemins', MAX="+") }}

## Exercice E – Parcours en profondeur

Écris `dfs(g, sommet, visites=None)` qui renvoie la liste des sommets dans l'ordre de visite d'un parcours en profondeur depuis `sommet`. `g` associe chaque sommet à la liste de ses voisins. Ne repasse jamais par un sommet déjà visité.

**J'anticipe.** Écris l'ordre de visite attendu pour le graphe de l'exercice 4.

{{ IDE('dfs', MAX="+") }}

**Je comprends.** Que se passerait-il sans le test sur `visites` ?

## Exercice F – Machines atteignables

Écris `atteignables(g, depart)` qui renvoie la liste **triée** des sommets atteignables depuis `depart` (lui compris). Tu peux réécrire `dfs` dans l'éditeur.

**J'anticipe.** Quelles machines sont atteignables depuis R1 (exercice 6) ?

{{ IDE('atteignables', MAX="+") }}

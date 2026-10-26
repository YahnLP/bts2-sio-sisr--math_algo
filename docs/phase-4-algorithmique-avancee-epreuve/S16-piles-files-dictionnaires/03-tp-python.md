---
render_macros: true
---

# TP Python – Piles, files et dictionnaires

*BTS SIO SISR 2e année – Pour aller plus loin – S16*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Parenthèses bien formées

Écris `parentheses_ok(s)` qui renvoie `True` si les parenthèses `()`, crochets `[]` et accolades `{}` de `s` sont bien formés. Les autres caractères sont ignorés. Utilise une pile.

**J'anticipe.** Déroule la pile pour `"([)]"`.

{{ IDE('parentheses_ok', MAX="+") }}

## Exercice B – Compter les adresses

Écris `compte_ip(lignes)` qui renvoie un dictionnaire `adresse -> nombre d'occurrences` pour une liste de chaînes (adresses d'un journal).

{{ IDE('compte_ip', MAX="+") }}

**Je comprends.** Quel est le coût en fonction du nombre de lignes ?

## Exercice C – Les plus fréquentes

Écris `top_n(compte, n)` qui renvoie la liste des `n` couples `(clé, nombre)` les plus fréquents, triés par nombre décroissant puis par clé croissante (ordre alphabétique).

{{ IDE('top_n', MAX="+") }}

## Exercice D – Tourniquet

Écris `tourniquet(durees, quantum)` : chaque tâche `i` a besoin de `durees[i]` unités ; on les traite avec une **file**, chacune au plus `quantum` unités par tour, puis elle retourne en fin de file si elle n'est pas finie. Renvoie la liste des indices dans l'ordre de fin. Utilise `collections.deque`.

**J'anticipe.** Retrouve l'ordre `[1, 2, 0]` de l'exercice 5.

{{ IDE('tourniquet', MAX="+") }}

## Exercice E – Annuler

Écris `edition(ops)` : `ops` est une liste de chaînes ; `"ANNULE"` retire le dernier élément ajouté (sans effet si rien à annuler), toute autre chaîne est ajoutée. Renvoie la liste finale. Utilise une pile.

{{ IDE('edition', MAX="+") }}

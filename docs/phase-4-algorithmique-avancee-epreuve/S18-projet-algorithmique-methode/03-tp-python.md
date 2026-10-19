---
render_macros: true
---

# TP Python – Analyser un journal de connexions

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S18*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Lire une ligne

Écris `parse_ligne(ligne)` qui renvoie le couple `(adresse, statut)` d'une ligne `"adresse;statut"`, en retirant les espaces autour des deux champs.

**J'anticipe.** Que renvoie `" a ; OK ".split(";")` ? Que faut-il en plus ?

{{ IDE('parse_ligne', MAX="+") }}

## Exercice B – Compter les échecs

Écris `echecs_par_ip(lignes)` qui renvoie un dictionnaire adresse → nombre d'échecs, **uniquement** pour les adresses ayant au moins un échec. Réutilise `parse_ligne` (recopie-la au début du fichier).

{{ IDE('echecs_par_ip', MAX="+") }}

**Je comprends.** Énonce l'invariant de ta boucle.

## Exercice C – Adresses suspectes

Écris `suspectes(lignes, seuil)` qui renvoie la liste **triée** des adresses ayant au moins `seuil` échecs.

{{ IDE('suspectes', MAX="+") }}

## Exercice D – Rafale d'échecs

Écris `rafale(lignes, ip, k)` qui renvoie `True` si l'adresse `ip` a au moins `k` échecs **consécutifs** parmi **ses** lignes (un `OK` interrompt la série). On considère `k >= 1`.

**J'anticipe.** Pour `["a;ECHEC", "a;OK", "a;ECHEC", "a;ECHEC"]`, quelle est la plus longue série d'échecs de `a` ?

{{ IDE('rafale', MAX="+") }}

## Exercice E – Rapport

Écris `rapport(lignes, seuil)` qui renvoie la liste de chaînes `"adresse : n"` pour les adresses suspectes, triée par nombre d'échecs **décroissant**, puis par adresse croissante.

{{ IDE('rapport', MAX="+") }}

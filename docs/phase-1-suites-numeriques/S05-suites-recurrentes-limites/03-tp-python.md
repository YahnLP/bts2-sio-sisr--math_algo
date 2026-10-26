---
render_macros: true
---

# TP Python – Limites et seuils en Python

*BTS SIO SISR 2e année – Pour aller plus loin – S05*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Limite d'une suite géométrique

Écris `limite_geo(u0, q)` qui renvoie la limite de \(u_0 q^n\) : le nombre `0` si \(u_0 = 0\) ou \(|q| < 1\) ; `u0` si \(q = 1\) ; la chaîne `"+inf"` ou `"-inf"` si \(q > 1\) selon le signe de `u0` ; la chaîne `"aucune"` si \(q \le -1\) et \(u_0 \ne 0\).

{{ IDE('limite_geo', MAX="+") }}

**Je comprends.** Pourquoi `q = -1` n'a-t-il pas de limite alors que les valeurs restent bornées ?

## Exercice B – Point fixe et formule explicite

Pour \(u_{n+1} = a u_n + b\) avec \(a \ne 1\), écris `point_fixe(a, b)` qui renvoie \(L = b/(1-a)\) et `terme_affine(a, b, u0, n)` qui renvoie \(u_n = L + (u_0 - L)a^n\).

**J'anticipe.** Pour `a = 0.5`, `b = 10`, que vaut le point fixe ? Et `terme_affine(0.5, 10, 0, 10)` ?

{{ IDE('affine', MAX="+") }}

**Je comprends.** Compare avec une boucle qui applique 10 fois la récurrence : que constates-tu ?

## Exercice C – Rang de seuil avec garde-fou

Écris `rang_seuil(f, u0, seuil, nmax)` qui renvoie le plus petit \(n \le\) `nmax` tel que \(u_n \ge\) `seuil` pour \(u_{k+1} = f(u_k)\), ou `None` si ce rang n'existe pas dans cette limite.

**J'anticipe.** Pour l'exercice 6 (seuil 25), que doit renvoyer ta fonction ?

{{ IDE('rang_seuil', MAX="+") }}

**Je comprends.** Quel est le variant de ta boucle ? Pourquoi s'arrête-t-elle dans tous les cas ?

## Exercice D – Somme qui dépasse un seuil

Écris `rang_somme(seuil)` qui renvoie le plus petit entier \(n \ge 0\) tel que \(1 + 2 + \dots + n \ge\) `seuil` (la somme vide vaut 0).

**J'anticipe.** Pour un seuil de 1 000, quel rang attends-tu (exercice 5) ?

{{ IDE('rang_somme', MAX="+") }}

## Exercice E – Stabilisation

Écris `rang_stable(f, u0, eps, nmax)` qui renvoie le premier rang \(n \le\) `nmax` tel que \(|u_{n+1} - u_n| <\) `eps`, ou `None`. Cela signale qu'une suite se **stabilise**.

**J'anticipe.** Pour \(u_{n+1} = 0{,}5u_n + 10\), \(u_0 = 0\) et `eps = 0.001`, devine à quel rang la suite devient stable (utilise \(u_{n+1} - u_n = 10 \times 0{,}5^n\)).

{{ IDE('rang_stable', MAX="+") }}

**Je comprends.** Une différence petite entre deux termes prouve-t-elle que la suite converge ? Cherche un contre-exemple.

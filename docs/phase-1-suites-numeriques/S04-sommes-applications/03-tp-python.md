---
render_macros: true
---

# TP Python – Intérêts, épargne et emprunt en Python

*BTS SIO SISR 2e année – Pour aller plus loin – S04*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

## Exercice A – Capital en intérêts composés

Écris `capital_compose(c0, taux, n)` qui renvoie le capital après `n` périodes au taux `taux` (en pour cent), arrondi à 2 décimales.

**J'anticipe.** Pour 10 000 € à 3 % sur 5 ans, quel résultat attends-tu ?

{{ IDE('capital_compose', MAX="+") }}

## Exercice B – Épargne à versements réguliers

Écris `epargne(versement, taux, n)` qui renvoie le capital après `n` versements, effectués en fin de période, au taux `taux` (en pour cent) par période, arrondi à 2 décimales. Utilise une **boucle** : à chaque période, le capital est multiplié par \(1 + t\) puis on ajoute le versement.

**J'anticipe.** Pour 1 000 € par an, 4 %, 5 ans, quel résultat attends-tu ?

{{ IDE('epargne', MAX="+") }}

**Je comprends.** Compare avec la formule du cours : pourquoi les deux méthodes donnent-elles le même résultat ?

## Exercice C – Mensualité d'un emprunt

Écris `mensualite(capital, taux, n)` qui renvoie la mensualité d'un emprunt de `capital` euros remboursé en `n` mois au taux mensuel `taux` (en pour cent), arrondie à 2 décimales. Si le taux est nul, la mensualité est `capital / n`.

**J'anticipe.** Pour l'exercice 3 (12 000 €, 0,5 %, 24 mois), quelle mensualité attends-tu ?

{{ IDE('mensualite', MAX="+") }}

## Exercice D – Capital restant dû

Écris `capital_restant(capital, taux, n, k)` qui renvoie le capital restant dû après `k` mensualités (`0 <= k <= n`), arrondi à 2 décimales. Calcule la mensualité exacte (non arrondie) puis applique `K = K * (1 + t) - M` `k` fois.

**J'anticipe.** Quel capital restant dû attends-tu après 0 mois ? après `n` mois (aux arrondis près) ?

{{ IDE('capital_restant', MAX="+") }}

**Je comprends.** Pourquoi le test final utilise-t-il `abs(...) < 0.01` plutôt qu'une égalité ?

## Exercice E – Quand le disque est-il plein ?

Un volume `u0` (en Go) augmente chaque mois de `taux` % puis de `ajout` Go. Écris `mois_stockage_plein(u0, taux, ajout, capacite)` qui renvoie le premier mois \(n\) tel que \(u_n \ge\) `capacite` (avec `ajout > 0`).

**J'anticipe.** Pour 200 Go, 10 %, 50 Go et 1 000 Go, quel mois attends-tu (exercice 4) ?

{{ IDE('mois_stockage_plein', MAX="+") }}

**Je comprends.** Quel est le variant de ta boucle ? Pourquoi `ajout > 0` garantit-il l'arrêt ?

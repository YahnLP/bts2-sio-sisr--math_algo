# Cours – Plan de révision

*BTS SIO SISR 2e année – Pour aller plus loin – S19 – à lire avant le [sujet blanc](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** les séances S01 à S18.
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de cette séance tu sauras

- [ ] **Traiter** un sujet complet en temps limité ;
- [ ] **Mobiliser** calcul, programmation et justification ;
- [ ] **Identifier** tes points faibles ;
- [ ] **Construire** un plan de révision ;
- [ ] **Corriger** ta copie avec un barème.

## I. La carte du programme

| Séances | Thème | À savoir absolument |
|---|---|---|
| S01 à S05 | Suites numériques | Définition par récurrence ; \(u_n = u_0 + nr\) (arithmétique) ; \(u_n = u_0 q^n\) (géométrique) ; sommes ; seuil par boucle |
| S06 à S10 | Récursivité | Cas de base, cas récursif, variant ; pile d'appels ; mémoïsation ; diviser pour régner ; parcours en profondeur |
| S11 à S15 | Analyse d'algorithmes | Variant, invariant, tests ; compter les opérations ; notation \(O\) ; tris et recherches ; mesures et explosions |
| S16 à S17 | Algorithmique avancée | Pile, file, dictionnaire ; parcours en largeur ; Dijkstra |
| S18 | Méthode | Comprendre, décomposer, choisir, tester, justifier |

## II. Formules et réflexes

| Situation | Outil |
|---|---|
| Augmentation constante \(r\) | \(u_n = u_0 + n r\) |
| Augmentation de \(t\,\%\) | \(u_n = u_0 (1 + t/100)^n\) |
| Somme géométrique (\(q \ne 1\)) | \(u_0 + \dots + u_0 q^n = u_0\,\dfrac{1 - q^{n+1}}{1 - q}\) |
| Boucle qui s'arrête | variant entier, positif ou nul, strictement décroissant |
| Récursivité | cas de base + appel sur un problème plus petit |
| Coût | opération de référence, pire cas, classe \(O\) |
| Plus court en sauts | largeur (file) |
| Plus court en coût, poids \(\ge 0\) | Dijkstra |

## III. Organiser ses révisions

1. **Passer le sujet blanc** en 2 h, seul, sans ouvrir le cours.
2. **Corriger avec le barème** (aide-mémoire) et noter les points perdus **par thème**.
3. **Revoir** les deux thèmes où le plus de points ont été perdus : relire l'aide-mémoire de la séance concernée, refaire ses exercices.
4. **Refaire** les TP des séances concernées jusqu'à ce que les tests passent sans aide.
5. **Passer un second sujet** (celui d'un camarade ou un sujet fourni par l'enseignant).

> [!TIP]
> Dans le sujet, commence par les questions que tu maîtrises ; une question bloquée ne doit pas te faire perdre les suivantes.

## IV. Conseils de rédaction

- **Justifier** chaque réponse numérique par la formule ou le calcul utilisé.
- **Indiquer l'unité** (Go, ms, jours).
- Pour un programme : annoncer l'idée, écrire la fonction, donner **un** test.
- Pour le coût : dire quelle opération on compte et pour quelle taille.

**Test flash.** Pour une augmentation de 3 % par mois, par quel nombre multiplie-t-on chaque mois ?

<details markdown="1">
<summary>Voir la réponse</summary>

Par 1,03.

</details>

## À retenir

- Une épreuve se prépare en **se testant** : sujet blanc, correction par barème, révision ciblée.
- Justifier, mettre l'unité, tester.

# Exercices – Complexité asymptotique

*BTS SIO SISR 2e année – Pour aller plus loin – S13*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, puis ouvre « Voir la réponse ». **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Simplifier

Donner la classe de : \(5n^2 + 3n\) ; \(n + \log_2 n\) ; \(100\) ; \(2n\log_2 n + n\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(O(n^2)\) ; \(O(n)\) ; \(O(1)\) ; \(O(n\log n)\).

</details>

## Exercice 2 – Preuve avec la définition

Montrer que \(3n + 5 = O(n)\).

<details markdown="1">
<summary>Voir la réponse</summary>

Pour \(n \ge 5\), \(5 \le n\), donc \(3n + 5 \le 3n + n = 4n\). On prend \(c = 4\) et \(n_0 = 5\).

</details>

## Exercice 3 – Doublement

Un traitement \(O(n^2)\) prend 3 s pour \(n = 10^4\). Estimer le temps pour \(n = 2 \times 10^4\), puis \(10^5\).

<details markdown="1">
<summary>Voir la réponse</summary>

Doubler : ×4, soit 12 s. Passer à \(10^5\) (×10) : ×100, soit 300 s.

</details>

## Exercice 4 – Deux boucles

Quelle classe pour un bloc \(O(n)\) suivi d'un bloc \(O(n^2)\) ? Pour une boucle \(O(n)\) contenant une recherche dichotomique \(O(\log n)\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(O(n^2)\) (le plus grand l'emporte). \(O(n\log n)\) (on multiplie).

</details>

## Exercice 5 – Ratio n log n

Calculer \(n \log_2 n\) pour \(n = 1000\) et \(n = 10\,000\). Quel rapport ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(1000 \times 9{,}966 \approx 9\,966\) ; \(10\,000 \times 13{,}288 \approx 132\,877\). Rapport \(\approx 13{,}33\).

</details>

## Exercice 6 – Une durée exponentielle

Un algorithme exécute \(2^{60}\) opérations. **Hypothèse** : \(10^9\) opérations par seconde. Quelle durée en jours puis en années ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(2^{60} \approx 1{,}153 \times 10^{18}\) ; ÷ \(10^9\) = \(1{,}153 \times 10^9\) s ; ÷ 86 400 \(\approx\) 13 344 jours \(\approx\) 36,5 ans.

</details>

## Je sais faire

- [ ] Simplifier un coût
- [ ] Utiliser la définition de \(O\)
- [ ] Prévoir l'effet d'un doublement
- [ ] Convertir des opérations en durée avec une hypothèse annoncée

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

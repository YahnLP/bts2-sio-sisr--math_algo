# Exercices – Mesurer et limites

*BTS SIO SISR 2e année – Pour aller plus loin – S15*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, puis ouvre « Voir la réponse ». **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Lire un test de doublement

Un traitement prend 0,8 s pour \(n = 10^4\), 3,3 s pour \(2 \times 10^4\) et 12,9 s pour \(4 \times 10^4\) (**mesures fictives**). Quel ordre ?

<details markdown="1">
<summary>Voir la réponse</summary>

Rapports : \(3{,}3/0{,}8 \approx 4{,}1\) et \(12{,}9/3{,}3 \approx 3{,}9\). Proche de 4 : \(O(n^2)\) probable.

</details>

## Exercice 2 – Mot de passe de 8 lettres

Combien d'essais pour 8 lettres minuscules ? Durée à \(10^9\) essais par seconde (**hypothèse**) ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(26^8 = 208\,827\,064\,576\) essais, soit \(\approx 208{,}8\) s, environ 3,5 minutes.

</details>

## Exercice 3 – Mot de passe de 12 lettres

Même question pour 12 lettres, en jours puis en années.

<details markdown="1">
<summary>Voir la réponse</summary>

\(26^{12} = 95\,428\,956\,661\,682\,176\) essais ; ÷ \(10^9\) \(\approx 9{,}54 \times 10^7\) s \(\approx 1\,105\) jours \(\approx 3{,}03\) ans.

</details>

## Exercice 4 – 12 caractères parmi 62

Combien d'essais ? Quel facteur par rapport aux 12 lettres minuscules ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(62^{12} = 3\,226\,266\,762\,397\,899\,821\,056\). Facteur \((62/26)^{12} \approx 33\,800\) environ.

</details>

## Exercice 5 – Tournées

Combien d'ordres de visite pour 8 sites, puis 10, puis 15 (premier site fixé) ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(7! = 5\,040\) ; \(9! = 362\,880\) ; \(14! = 87\,178\,291\,200\).

</details>

## Exercice 6 – Améliorer la recherche de doublons

Expliquer pourquoi l'usage d'un ensemble accélère la détection de doublons dans une liste de \(10^6\) éléments par rapport aux deux boucles.

<details markdown="1">
<summary>Voir la réponse</summary>

Deux boucles : jusqu'à \(\approx 5 \times 10^{11}\) comparaisons. Avec un ensemble : \(10^6\) insertions et tests, chacun en temps moyen quasi constant, soit de l'ordre de \(10^6\) opérations. Le gain est de l'ordre de 500 000 en nombre d'opérations. Ce gain a un coût : de la mémoire supplémentaire.

</details>

## Je sais faire

- [ ] Mesurer un temps de façon raisonnable
- [ ] Interpréter un test de doublement
- [ ] Calculer un nombre d'essais de force brute
- [ ] Calculer \((n-1)!\) et mesurer l'explosion

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

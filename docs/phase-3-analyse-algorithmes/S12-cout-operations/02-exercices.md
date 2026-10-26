# Exercices – Coût en opérations

*BTS SIO SISR 2e année – Pour aller plus loin – S12*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, puis ouvre « Voir la réponse ». **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Compter des additions

Combien d'additions fait `for i in range(n): s = s + i` ? Et `for i in range(n): for j in range(n): s = s + 1` ? Donner les valeurs pour \(n = 100\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(n\) additions, soit 100. Puis \(n^2 = 10\,000\).

</details>

## Exercice 2 – Boucle triangulaire

Combien de passages au centre pour `for i in range(n): for j in range(i + 1, n)` avec \(n = 1000\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

\((n-1) + (n-2) + \dots + 0 = n(n-1)/2 = 499\,500\).

</details>

## Exercice 3 – Recherche séquentielle

Dans une liste de \(n\) éléments, combien de comparaisons au meilleur cas, au pire cas, et en moyenne (élément présent, position équiprobable) ?

<details markdown="1">
<summary>Voir la réponse</summary>

Meilleur : 1. Pire : \(n\). Moyen : \((1 + 2 + \dots + n)/n = (n+1)/2\).

</details>

## Exercice 4 – Boucle qui divise

Combien de tours fait `while n > 1: n = n // 2` pour \(n = 1000\) ? Pour \(n = 1\,000\,000\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

9 tours pour 1000. Pour \(10^6\) : \(\lfloor \log_2 10^6 \rfloor = 19\) tours (car \(2^{19} = 524\,288 \le 10^6 < 2^{20}\)).

</details>

## Exercice 5 – Deux algorithmes

L'algorithme A coûte \(3n + 5\), l'algorithme B coûte \(n^2/10\). À partir de quelle valeur de \(n\) B coûte-t-il plus que A ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(n^2/10 > 3n + 5 \iff n^2 > 30n + 50\). Pour \(n = 31\) : \(961 > 980\) faux. Pour \(n = 32\) : \(1024 > 1010\) vrai. Donc à partir de \(n = 32\).

</details>

## Exercice 6 – Doublons : une durée fictive

Pour une liste de 1 000 éléments sans doublon, `doublon` fait 499 500 comparaisons. **Hypothèse (fictive)** : une comparaison dure 1 µs. Quelle durée ? Et pour \(10^6\) éléments ?

<details markdown="1">
<summary>Voir la réponse</summary>

499 500 µs, soit environ 0,5 s. Pour \(n = 10^6\) : \(n(n-1)/2 = 499\,999\,500\,000\) comparaisons, soit \(499\,999\,500\,000\) µs \(\approx 5{,}79\) jours. Cette durée dépend de l'hypothèse, mais le facteur 1 000 000 en durée pour un facteur 1 000 en taille est, lui, indépendant de la machine.

</details>

## Je sais faire

- [ ] Compter les opérations d'une boucle simple, imbriquée, triangulaire
- [ ] Distinguer meilleur, pire et moyen
- [ ] Compter les tours d'une boucle qui divise par 2
- [ ] Comparer deux coûts

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

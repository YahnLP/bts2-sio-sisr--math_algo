# Exercices – Suites arithmétiques

*BTS SIO SISR 2e année – Pour aller plus loin – S02*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours. Ouvre ensuite « Voir la réponse » pour te corriger. **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Reconnaître

Dire si chaque suite est arithmétique et donner sa raison : (a) \(u_n = 5n - 2\) ; (b) \(u_n = n^2 + 1\) ; (c) \(u_0 = 7\) et \(u_{n+1} = u_n - 4\).

<details markdown="1">
<summary>Voir la réponse</summary>

(a) \(u_{n+1} - u_n = 5(n+1) - 2 - 5n + 2 = 5\) : arithmétique, \(r = 5\).
(b) \(u_0 = 1\), \(u_1 = 2\), \(u_2 = 5\) : différences 1 et 3, **pas arithmétique**.
(c) arithmétique de raison \(r = -4\) (décroissante).

</details>

## Exercice 2 – Terme général et somme

Soit \((u_n)\) arithmétique avec \(u_0 = 12\) et \(r = 5\). Donner \(u_n\), calculer \(u_{20}\) et \(u_0 + u_1 + \dots + u_{20}\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(u_n = 12 + 5n\) ; \(u_{20} = 112\). Il y a 21 termes : \(21 \times \dfrac{12 + 112}{2} = 21 \times 62 = 1\,302\).

</details>

## Exercice 3 – Retrouver la suite

Une suite arithmétique vérifie \(u_3 = 14\) et \(u_8 = 34\). Trouver \(r\), \(u_0\), \(u_n\) et \(u_{20}\).

<details markdown="1">
<summary>Voir la réponse</summary>

De \(u_8 = u_3 + 5r\) on tire \(34 = 14 + 5r\), donc \(r = 4\). Puis \(u_0 = u_3 - 3r = 14 - 12 = 2\). Ainsi \(u_n = 2 + 4n\) et \(u_{20} = 82\).

</details>

## Exercice 4 – Journaux qui grossissent

Le journal d'un pare-feu pèse 100 Mo le jour 1, et chaque jour il pèse 25 Mo de plus que la veille. Quel est le poids du journal le jour 30 ? Quel est le volume cumulé sur les 30 jours ?

<details markdown="1">
<summary>Voir la réponse</summary>

Suite arithmétique de premier terme \(u_1 = 100\) et de raison 25. Jour 30 : \(u_{30} = 100 + 29 \times 25 = 825\) Mo.
Somme de 30 termes : \(30 \times \dfrac{100 + 825}{2} = 30 \times 462{,}5 = 13\,875\) Mo.

</details>

## Exercice 5 – Sommes classiques

Calculer \(1 + 2 + \dots + 100\) et \(1 + 3 + 5 + \dots + 99\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(\dfrac{100 \times 101}{2} = 5\,050\). Les nombres impairs de 1 à 99 forment une suite arithmétique de raison 2 : \(1 + 2k = 99\) donne \(k = 49\), soit 50 termes ; somme \(= 50 \times \dfrac{1 + 99}{2} = 2\,500\) (c'est \(50^2\)).

</details>

## Exercice 6 – Combien d'adresses ?

Une plage utilise les adresses finales 10, 14, 18, …, 250 (de 4 en 4). Combien y en a-t-il ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(10 + 4k = 250\) donne \(k = 60\), donc **61** adresses (rang 0 à 60).

</details>

## Exercice 7 – Comparer deux offres

Offre A : \(30 + 4n\) euros ; offre B : \(50 + 3n\) euros, où \(n\) est le nombre de paliers de 100 Go. À partir de quel \(n\) l'offre B est-elle **strictement** moins chère ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(50 + 3n < 30 + 4n\) équivaut à \(n > 20\). À \(n = 20\), les deux coûtent 110 €. B est strictement moins chère dès **\(n = 21\)** (A : 114 €, B : 113 €).

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Reconnaître une suite arithmétique et donner sa raison
- [ ] Écrire \(u_n = u_p + (n-p)r\)
- [ ] Calculer une somme de termes consécutifs en comptant bien les termes
- [ ] Modéliser une croissance linéaire

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

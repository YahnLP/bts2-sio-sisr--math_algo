# Exercices – Suites géométriques

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S03*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**. Ouvre ensuite « Voir la réponse » pour te corriger. **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Reconnaître

Dire si chaque suite est géométrique et donner sa raison : (a) \(3, 6, 12, 24, \dots\) ; (b) \(u_n = 5 \times (1/2)^n\) ; (c) \(2, 5, 8, 11, \dots\) ; (d) \(u_0 = 4\) et \(u_{n+1} = -3\,u_n\).

<details markdown="1">
<summary>Voir la réponse</summary>

(a) oui, \(q = 2\). (b) oui, \(q = 1/2\). (c) non : rapports \(5/2\) puis \(8/5\) (c'est une suite arithmétique de raison 3). (d) oui, \(q = -3\) : \(4, -12, 36, -108, \dots\) (signes alternés).

</details>

## Exercice 2 – Terme général et somme

Soit \(u_0 = 3\) et \(q = 2\). Calculer \(u_{10}\) et \(u_0 + \dots + u_{10}\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(u_{10} = 3 \times 1\,024 = 3\,072\). Somme : \(3 \times \dfrac{1 - 2^{11}}{1 - 2} = 3 \times 2\,047 = 6\,141\).

</details>

## Exercice 3 – Retrouver la suite

Une suite géométrique de raison positive vérifie \(u_2 = 12\) et \(u_5 = 96\). Trouver \(q\), \(u_0\) et \(u_n\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(u_5 = u_2 \, q^3\) donne \(96 = 12\,q^3\), donc \(q^3 = 8\) et \(q = 2\). Puis \(u_0 = u_2 / q^2 = 12 / 4 = 3\), et \(u_n = 3 \times 2^n\). Contrôle : \(u_2 = 12\), \(u_5 = 96\).

</details>

## Exercice 4 – Trafic

Un trafic de 500 Go par mois augmente de 20 % chaque mois.

1. Quel est le trafic après 3 mois ?
2. À partir de quel mois dépasse-t-il 2 000 Go ? (Calculer les termes un à un.)

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(q = 1{,}2\) : \(u_3 = 500 \times 1{,}2^3 = 864\) Go.
2. \(u_7 = 500 \times 1{,}2^7 \approx 1\,791{,}6\) Go (pas assez) ; \(u_8 \approx 2\,149{,}9\) Go. C'est donc à partir du mois **8**.

</details>

## Exercice 5 – Dépréciation

Un serveur acheté 2 000 € perd 15 % de sa valeur chaque année. Quelle est sa valeur après 4 ans ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(q = 0{,}85\) : \(2\,000 \times 0{,}85^4 = 2\,000 \times 0{,}52200625 \approx 1\,044{,}01\) €.

</details>

## Exercice 6 – Doublement

Une sauvegarde pèse 1 Go le jour 0 et son volume double chaque jour. Quel est le volume total stocké en additionnant les jours 0 à 9 ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(1 + 2 + \dots + 2^9 = 2^{10} - 1 = 1\,023\) Go.

</details>

## Exercice 7 – Linéaire contre exponentiel

Comparer \(a_n = 100 + 50n\) (croissance linéaire) et \(g_n = 100 \times 1{,}1^n\) (croissance de 10 % par période). À partir de quel rang \(g_n\) dépasse-t-il \(a_n\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

On calcule : \(n = 28\) : \(g_n \approx 1\,442{,}1\) pour \(a_n = 1\,500\) (pas encore) ; \(n = 29\) : \(g_n \approx 1\,586{,}3\) pour \(a_n = 1\,550\) : c'est dépassé. Réponse : à partir de **\(n = 29\)**. L'exponentielle démarre au même niveau mais finit par l'emporter.

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Reconnaître une suite géométrique et donner sa raison
- [ ] Passer d'un pourcentage à un coefficient multiplicateur
- [ ] Écrire \(u_n = u_p q^{n-p}\) et la somme de termes
- [ ] Distinguer croissance linéaire et exponentielle

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

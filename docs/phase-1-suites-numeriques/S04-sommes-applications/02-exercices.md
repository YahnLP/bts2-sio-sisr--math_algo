# Exercices – Intérêts, emprunt et croissance de données

*BTS SIO SISR 2e année – Pour aller plus loin – S04*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, calculatrice autorisée. Ouvre ensuite « Voir la réponse » pour te corriger. **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Simples ou composés

5 000 € sont placés à 4 % par an pendant 10 ans. Calculer le capital final en intérêts simples puis en intérêts composés. Quelle est la différence ?

<details markdown="1">
<summary>Voir la réponse</summary>

Simples : \(5\,000 \times (1 + 10 \times 0{,}04) = 7\,000\) €. Composés : \(5\,000 \times 1{,}04^{10} \approx 7\,401{,}22\) €. Différence : environ **401,22 €** en faveur des intérêts composés.

</details>

## Exercice 2 – Épargne mensuelle

On verse 200 € à la fin de chaque mois pendant 12 mois, au taux de 0,25 % par mois. Quel capital obtient-on ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(200 \times \dfrac{1{,}0025^{12} - 1}{0{,}0025} \approx 2\,433{,}28\) €. Les versements totalisent 2 400 € : les intérêts sont d'environ 33,28 €.

</details>

## Exercice 3 – Un emprunt

On emprunte 12 000 € sur 24 mois au taux de 0,5 % par mois.

1. Calculer la mensualité.
2. Compléter les trois premières lignes du tableau d'amortissement.
3. Calculer le coût total des intérêts.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(M = \dfrac{12\,000 \times 0{,}005}{1 - 1{,}005^{-24}} \approx 531{,}85\) €.
2. Mois 1 : intérêts \(12\,000 \times 0{,}005 = 60{,}00\), amortissement \(531{,}85 - 60{,}00 \approx 471{,}85\), capital restant dû \(11\,528{,}15\). Mois 2 : 57,64 ; 474,21 ; 11 053,95. Mois 3 : 55,27 ; 476,58 ; 10 577,37.
3. \(24 \times 531{,}847\ldots - 12\,000 \approx 764{,}34\) € (764,40 € si l'on utilise la mensualité arrondie à 531,85 €).

</details>

## Exercice 4 – Stockage qui grossit

Un serveur stocke 200 Go. Chaque mois, ses données augmentent de 10 % puis 50 Go sont ajoutés. On note \(u_n\) le volume au mois \(n\).

1. Écrire la relation de récurrence.
2. Calculer \(u_1, u_2, u_3\).
3. Le disque fait 1 000 Go. À partir de quel mois est-il plein ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(u_0 = 200\) et \(u_{n+1} = 1{,}1\,u_n + 50\).
2. \(u_1 = 270\), \(u_2 = 347\), \(u_3 = 431{,}7\).
3. En continuant : \(u_4 \approx 524{,}87\), \(u_5 \approx 627{,}36\), \(u_6 \approx 740{,}09\), \(u_7 \approx 864{,}10\), \(u_8 \approx 1\,000{,}51\). Le disque est plein au mois **8**.

</details>

## Exercice 5 – Quel modèle ?

Pour chaque situation, indiquer le modèle (arithmétique, géométrique ou récurrence mixte) : (a) un abonnement coûte 20 € de plus chaque année ; (b) un trafic croît de 5 % par mois ; (c) un emprunt dont on rembourse une mensualité fixe et dont le capital produit des intérêts.

<details markdown="1">
<summary>Voir la réponse</summary>

(a) arithmétique (\(r = 20\)). (b) géométrique (\(q = 1{,}05\)). (c) récurrence mixte \(K_{k+1} = (1 + t)K_k - M\).

</details>

## Exercice 6 – Contrôle de l'emprunt

Montrer, à partir de la récurrence \(K_{k+1} = (1+t)K_k - M\), que le capital restant dû après 24 mois de l'exercice 3 est (quasi) nul.

<details markdown="1">
<summary>Voir la réponse</summary>

On itère 24 fois avec \(K_0 = 12\,000\), \(t = 0{,}005\), \(M = 531{,}847\ldots\) (valeur non arrondie). On trouve \(K_{24} \approx -3 \times 10^{-10}\), c'est-à-dire 0 aux erreurs d'arrondi des flottants près. Avec la mensualité arrondie à 531,85 €, le dernier mois est ajusté de quelques centimes.

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Distinguer intérêts simples et composés
- [ ] Calculer un capital d'épargne
- [ ] Calculer une mensualité et lire un tableau d'amortissement
- [ ] Simuler une croissance « pourcentage plus ajout »

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

# Exercices – Limites, point fixe et seuils

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S05*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**. Ouvre ensuite « Voir la réponse » pour te corriger. **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Limites

Donner le comportement de : (a) \(3 \times 0{,}8^n\) ; (b) \(2 \times 1{,}05^n\) ; (c) \(7 - 2n\) ; (d) \((-1{,}5)^n\).

<details markdown="1">
<summary>Voir la réponse</summary>

(a) \(q = 0{,}8\), \(|q| < 1\) : tend vers 0. (b) \(q = 1{,}05 > 1\), \(u_0 > 0\) : tend vers \(+\infty\). (c) arithmétique de raison \(-2\) : tend vers \(-\infty\). (d) \(q \le -1\) : les signes alternent et les valeurs absolues augmentent ; **pas de limite**.

</details>

## Exercice 2 – Point fixe

Soit \(u_0 = 0\) et \(u_{n+1} = 0{,}5\,u_n + 10\).

1. Calculer \(u_1, \dots, u_4\).
2. Trouver le point fixe \(L\) et montrer que \(v_n = u_n - L\) est géométrique.
3. En déduire \(u_n\) et \(u_{10}\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(10, 15, 17{,}5, 18{,}75\).
2. \(L = 0{,}5L + 10\) donne \(L = 20\). \(v_{n+1} = 0{,}5\,u_n + 10 - 20 = 0{,}5\,(u_n - 20) = 0{,}5\,v_n\) : géométrique de raison \(0{,}5\), de premier terme \(v_0 = -20\).
3. \(u_n = 20 - 20 \times 0{,}5^n\) ; \(u_{10} = 20 - 20/1\,024 = 19{,}98046875\).

</details>

## Exercice 3 – Seuil

Avec la suite de l'exercice 2, à partir de quel rang \(u_n \ge 19{,}9\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(20 - 20 \times 0{,}5^n \ge 19{,}9\) équivaut à \(0{,}5^n \le 0{,}005\). Test : \(u_7 = 20 - 20/128 = 19{,}84375 < 19{,}9\) ; \(u_8 = 20 - 20/256 = 19{,}921875 \ge 19{,}9\). Rang **8**.

</details>

## Exercice 4 – Un disque suffit-il ?

Un serveur contient 50 Go. Chaque mois, 20 % des données sont purgées puis 30 Go sont ajoutés : \(u_{n+1} = 0{,}8\,u_n + 30\).

1. Vers quelle valeur tend le volume ?
2. Un disque de 120 Go suffit-il ? À quel mois est-il plein ? Un disque de 200 Go ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(L = 30/0{,}2 = 150\) Go, et \(u_n = 150 - 100 \times 0{,}8^n\).
2. Le volume tend vers 150 Go : un disque de 120 Go **ne suffit pas** à long terme. \(u_5 = 117{,}232\) (pas encore), \(u_6 \approx 123{,}79\) : il est plein au mois **6**. Un disque de 200 Go suffit toujours (la limite est 150 Go, jamais dépassée).

</details>

## Exercice 5 – Somme qui dépasse un seuil

Quel est le plus petit \(n\) tel que \(1 + 2 + \dots + n \ge 1\,000\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(\dfrac{n(n+1)}{2} \ge 1\,000\). Pour \(n = 44\) : \(990\) (insuffisant) ; pour \(n = 45\) : \(1\,035\). Réponse : **\(n = 45\)**.

</details>

## Exercice 6 – Boucle infinie

On exécute `rang_seuil` avec \(u_{n+1} = 0{,}5\,u_n + 10\), \(u_0 = 0\) et le seuil 25. Que se passe-t-il ? Corriger.

<details markdown="1">
<summary>Voir la réponse</summary>

La suite tend vers 20 et ne dépasse **jamais** 25 : la boucle `while u < seuil` ne s'arrête pas. Correction : vérifier d'abord que la limite dépasse le seuil, ou ajouter un nombre maximal d'itérations `nmax` et renvoyer `None` si le seuil n'est pas atteint.

</details>

## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Donner la limite d'une suite arithmétique ou géométrique
- [ ] Trouver le point fixe de \(u_{n+1} = au_n + b\) et la formule explicite
- [ ] Écrire un algorithme de seuil avec garde-fou
- [ ] Interpréter une limite (saturation ou stabilisation)

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

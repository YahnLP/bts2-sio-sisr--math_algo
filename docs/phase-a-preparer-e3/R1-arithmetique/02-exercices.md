# Exercices – Arithmétique : numération et arithmétique modulaire

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – R1*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, en écrivant les étapes. Ouvre ensuite « Voir la réponse ». Trois niveaux : **socle** (savoir-faire de base), **format épreuve** (énoncés contextualisés, à traiter en temps limité) et **pour aller plus loin** (au-delà du programme de l'épreuve, utile en licence ou en école d'ingénieurs).

## Niveau 1 – Socle

### Exercice 1 – Conversions entre bases

1. Écrire 365 en binaire, puis en hexadécimal.
2. Convertir `2F7` (hexadécimal) en décimal, puis en binaire.
3. Convertir `10110111` (binaire) en hexadécimal, puis en décimal.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Divisions successives par 2 : \(365 = 2 \times 182 + 1\), \(182 = 2 \times 91 + 0\), \(91 = 2 \times 45 + 1\), \(45 = 2 \times 22 + 1\), \(22 = 2 \times 11 + 0\), \(11 = 2 \times 5 + 1\), \(5 = 2 \times 2 + 1\), \(2 = 2 \times 1 + 0\), \(1 = 2 \times 0 + 1\). Restes lus de bas en haut : \(365 = 101101101_2\). Par groupes de 4 bits (\(0001\,0110\,1101\)) : \(365 = \texttt{16D}_{16}\).
2. \(\texttt{2F7} = 2 \times 256 + 15 \times 16 + 7 = 512 + 240 + 7 = 759\). En binaire, chaque chiffre donne 4 bits : \(0010\,1111\,0111\), soit \(1011110111_2\).
3. \(1011\,0111\) : \(1011 = \texttt{B}\) et \(0111 = \texttt{7}\), donc \(\texttt{B7}\). En décimal : \(11 \times 16 + 7 = 183\).

</details>

### Exercice 2 – Nombres à virgule

1. Convertir \(0{,}8125\) puis \(13{,}375\) en binaire.
2. Donner les 8 premiers chiffres de \(0{,}1\) après la virgule en binaire. Quelle valeur décimale représente cette troncature ? Quelle est l'erreur ?
3. Expliquer pourquoi `0.1 + 0.2 == 0.3` vaut `False` en Python.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(0{,}8125 \times 2 = 1{,}625\) (1), \(0{,}625 \times 2 = 1{,}25\) (1), \(0{,}25 \times 2 = 0{,}5\) (0), \(0{,}5 \times 2 = 1\) (1) : \(0{,}8125 = 0{,}1101_2\). Pour \(13{,}375\) : \(13 = 1101_2\) et \(0{,}375 = 0{,}011_2\) (\(0{,}375 \times 2 = 0{,}75\) donne 0, \(0{,}75 \times 2 = 1{,}5\) donne 1, \(0{,}5 \times 2 = 1\) donne 1), donc \(13{,}375 = 1101{,}011_2\).
2. \(0{,}1 \times 2 = 0{,}2\) (0), \(0{,}4\) (0), \(0{,}8\) (0), \(1{,}6\) (1), \(1{,}2\) (1), \(0{,}4\) (0)… on retombe sur \(0{,}4\) : la suite est **périodique**. Les 8 premiers chiffres sont \(00011001\), soit \(25/256 = 0{,}09765625\). L'erreur est \(0{,}1 - 0{,}09765625 = 0{,}00234375\).
3. Ni \(0{,}1\), ni \(0{,}2\), ni \(0{,}3\) n'ont d'écriture binaire finie (leur dénominateur n'est pas une puissance de 2) : l'ordinateur les **tronque**. La somme des deux troncatures n'est pas exactement la troncature de \(0{,}3\) ; Python obtient `0.30000000000000004`. On compare donc avec une tolérance : `abs(a - b) < 1e-9`.

</details>

### Exercice 3 – Calcul en binaire

1. Calculer en binaire \(101101_2 + 11011_2\) et \(101101_2 - 11011_2\). Vérifier en décimal.
2. Calculer \(1101_2 \times 101_2\).
3. Sans poser de division, donner le quotient et le reste de \(100101_2\) par \(2^3\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(101101_2 = 45\) et \(11011_2 = 27\). Somme : \(1001000_2 = 72\). Différence : \(10010_2 = 18\). Vérification : \(45 + 27 = 72\) et \(45 - 27 = 18\).
2. \(1101_2 \times 101_2 = 1101_2 \times 100_2 + 1101_2 = 110100_2 + 1101_2 = 1000001_2\), soit \(13 \times 5 = 65\).
3. Diviser par \(2^3\) revient à **décaler de 3 rangs à droite** : \(100101_2 \to 100_2\) est le quotient (\(4\)) ; les 3 bits sortis, \(101_2\), forment le reste (\(5\)). Vérification : \(37 = 8 \times 4 + 5\).

</details>

### Exercice 4 – Division euclidienne

1. Effectuer la division euclidienne de 1234 par 37.
2. Effectuer la division euclidienne de \(-25\) par 7. Pourquoi le reste n'est-il pas \(-4\) ?
3. Un traitement dure 1000 minutes. L'exprimer en heures et minutes.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(1234 = 37 \times 33 + 13\) (car \(37 \times 33 = 1221\)) : quotient 33, reste 13.
2. \(-25 = 7 \times (-4) + 3\) : quotient \(-4\), reste 3. Le reste doit vérifier \(0 \le r < 7\) ; \(-4\) ne convient pas.
3. \(1000 = 60 \times 16 + 40\) : **16 h 40**.

</details>

### Exercice 5 – Dépassement de capacité

Un compteur est codé sur un octet non signé. Quelle est la plus grande valeur représentable ? Que devient \(200 + 100\) calculé sur 8 bits ? Écrire l'addition en binaire.

<details markdown="1">
<summary>Voir la réponse</summary>

Sur 8 bits non signés : \(0\) à \(2^8 - 1 = 255\). \(200 = 11001000_2\) et \(100 = 01100100_2\) : la somme est \(1\,0010\,1100_2\) (9 bits). Le bit de retenue final est perdu : il reste \(00101100_2 = 44\), soit \(300 - 256\). C'est un **dépassement de capacité** : le résultat est faux modulo 256.

</details>

## Niveau 2 – Format épreuve

### Exercice 6 – Décomposition et primalité

1. Décomposer 1260 en produit de facteurs premiers. Combien a-t-il de diviseurs positifs ?
2. 391 est-il premier ? Et 997 ? Justifier en précisant quels diviseurs on teste.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(1260 = 2^2 \times 3^2 \times 5 \times 7\). Le nombre de diviseurs est \((2+1)(2+1)(1+1)(1+1) = 36\).
2. Pour 391 : \(\sqrt{391} \approx 19{,}8\), on teste les premiers \(\le 19\) : 2, 3, 5, 7, 11, 13 ne divisent pas ; \(391 = 17 \times 23\). **391 n'est pas premier.** Pour 997 : \(\sqrt{997} \approx 31{,}6\), on teste 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 : aucun ne divise 997 (restes non nuls). **997 est premier.**

</details>

### Exercice 7 – PGCD

1. Calculer \(\operatorname{PGCD}(1071, 462)\) par l'algorithme d'Euclide, puis \(\operatorname{PPCM}(1071, 462)\).
2. Les nombres 345 et 1001 sont-ils premiers entre eux ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(1071 = 2 \times 462 + 147\) ; \(462 = 3 \times 147 + 21\) ; \(147 = 7 \times 21 + 0\). Le PGCD est **21**. Comme \(\operatorname{PGCD} \times \operatorname{PPCM} = 1071 \times 462\), \(\operatorname{PPCM} = 494\,802 / 21 = 23\,562\).
2. \(1001 = 2 \times 345 + 311\) ; \(345 = 1 \times 311 + 34\) ; \(311 = 9 \times 34 + 5\) ; \(34 = 6 \times 5 + 4\) ; \(5 = 1 \times 4 + 1\) ; \(4 = 4 \times 1 + 0\). Le PGCD est 1 : **oui, premiers entre eux**.

</details>

### Exercice 8 – Congruences

1. Calculer \(7^{100} \bmod 13\). On pourra utiliser le fait que \(7^{12} \equiv 1 \pmod{13}\).
2. Calculer \(3^{2024} \bmod 7\).
3. Le 4 novembre est un mercredi. Quel jour de la semaine sera-t-on 100 jours plus tard ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(100 = 12 \times 8 + 4\), donc \(7^{100} \equiv (7^{12})^8 \times 7^4 \equiv 7^4\). \(7^2 = 49 \equiv 10\), \(7^4 \equiv 10^2 = 100 \equiv 9 \pmod{13}\). Résultat : **9**.
2. Modulo 7 : \(3^1 \equiv 3\), \(3^2 \equiv 2\), \(3^3 \equiv 6\), \(3^4 \equiv 4\), \(3^5 \equiv 5\), \(3^6 \equiv 1\) : cycle de longueur 6. \(2024 = 6 \times 337 + 2\), donc \(3^{2024} \equiv 3^2 \equiv 2\). Résultat : **2**.
3. \(100 = 7 \times 14 + 2\) : on avance de 2 jours dans la semaine. Mercredi + 2 = **vendredi**.

</details>

### Exercice 9 – Multiples modulo \(n\)

Un tourniquet à 12 positions est avancé de 8 positions à chaque impulsion.

1. Quelles positions peut-on atteindre à partir de la position 0 ? Pourquoi ?
2. Pour quels nombres \(x\) d'impulsions (\(0 \le x < 12\)) est-on en position 4, c'est-à-dire \(8x \equiv 4 \pmod{12}\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. Les multiples de 8 modulo 12 sont les multiples de \(\operatorname{PGCD}(8, 12) = 4\) : on n'atteint que les positions **0, 4 et 8**, dans l'ordre 0, 8, 4, 0, …
2. \(8x \bmod 12\) vaut successivement 0, 8, 4, 0, 8, 4, … pour \(x = 0, 1, 2, \dots\). La position 4 est atteinte pour \(x \equiv 2 \pmod 3\) : \(x \in \{2, 5, 8, 11\}\). Vérification : \(8 \times 5 = 40 = 3 \times 12 + 4\).

</details>

### Exercice 10 – Parcours d'une liste circulaire

Douze serveurs de sauvegarde, numérotés de 0 à 11, sont interrogés en rotation à partir du serveur 0 par sauts de \(k\) positions : le suivant du serveur \(i\) est \((i + k) \bmod 12\).

1. Pour \(k = 5\), écrire l'ordre des serveurs interrogés. Tous sont-ils visités ?
2. Même question pour \(k = 8\), puis \(k = 6\).
3. Pour quelles valeurs de \(k\) (\(1 \le k \le 11\)) le parcours est-il exhaustif ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(0, 5, 10, 3, 8, 1, 6, 11, 4, 9, 2, 7\), puis retour à 0 : les 12 serveurs sont visités, car \(\operatorname{PGCD}(5, 12) = 1\).
2. \(k = 8\) : \(0, 8, 4\) puis retour à 0 : 3 serveurs seulement (\(12 / \operatorname{PGCD}(8, 12) = 12/4 = 3\)). \(k = 6\) : \(0, 6\) : 2 serveurs (\(12/6\)).
3. Le parcours est exhaustif si et seulement si \(\operatorname{PGCD}(k, 12) = 1\), soit \(k \in \{1, 5, 7, 11\}\).

</details>

### Exercice 11 – Clé de contrôle

Un numéro de dossier fictif à 13 chiffres est \(N = 2\,910\,733\,118\,042\). Sa clé est \(c = 97 - (N \bmod 97)\), écrite sur deux chiffres.

1. Calculer la clé. On sait que \(N \bmod 97 = 93\).
2. Montrer que \(N + c\) est divisible par 97.
3. Une erreur de saisie change le dernier chiffre de 2 en 3. L'erreur est-elle détectée ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(c = 97 - 93 = 4\), écrit **04**.
2. \(N + c \equiv 93 + 4 = 97 \equiv 0 \pmod{97}\) : divisible par 97.
3. Le nouveau numéro est \(N' = N + 1\), donc \(N' \bmod 97 = 94\) et \(N' + c \equiv 98 \equiv 1 \pmod{97}\) : le résultat n'est pas nul, **l'erreur est détectée**. Plus généralement, une erreur sur un seul chiffre change \(N\) de \(\delta \times 10^i\) avec \(1 \le \delta \le 9\) ; 97 est premier et ne divise ni \(\delta\) ni \(10^i\), donc il ne divise pas cette différence : l'erreur est toujours détectée.

</details>

### Exercice 12 – Adresse réseau et masques

Une machine a l'adresse `172.16.77.130/26`.

1. Donner le masque en notation décimale pointée.
2. Calculer l'adresse du réseau (ET bit à bit) et l'adresse de diffusion.
3. Combien de machines peut-on adresser ?
4. Calculer `0b10110110 & 0b00001111` et `0b10110110 ^ 0b11110000`. Que fait le premier masque ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. 26 bits à 1 : \(255.255.255.192\) (le dernier octet est \(11000000_2 = 192\)).
2. Dernier octet : \(130 = 10000010_2\) ET \(11000000_2\) = \(10000000_2 = 128\). Réseau : **172.16.77.128**. Diffusion : les 6 bits d'hôte à 1, \(128 + 63 = 191\) : **172.16.77.191**.
3. \(2^6 - 2 = 62\) machines (on retire l'adresse du réseau et celle de diffusion).
4. \(10110110 \;\&\; 00001111 = 00000110\) : le masque **garde les 4 bits de poids faible**. \(10110110 \oplus 11110000 = 01000110\) : le OU exclusif **inverse les 4 bits de poids fort**.

</details>

## Niveau 3 – Pour aller plus loin

> [!NOTE]
> Les exercices ci-dessous dépassent le programme de l'épreuve. Ils préparent la licence d'informatique, les écoles d'ingénieurs et la cryptographie.

### Exercice 13 – Inverse modulaire par l'algorithme d'Euclide étendu

Trouver l'inverse de 17 modulo 3120, c'est-à-dire \(d\) tel que \(17d \equiv 1 \pmod{3120}\).

<details markdown="1">
<summary>Voir la réponse</summary>

Euclide : \(3120 = 183 \times 17 + 9\) ; \(17 = 1 \times 9 + 8\) ; \(9 = 1 \times 8 + 1\). On remonte :

\[
1 = 9 - 8 = 9 - (17 - 9) = 2 \times 9 - 17 = 2\,(3120 - 183 \times 17) - 17 = 2 \times 3120 - 367 \times 17 .
\]

Donc \(17 \times (-367) \equiv 1 \pmod{3120}\), et \(d = 3120 - 367 = \mathbf{2753}\). Vérification : \(17 \times 2753 = 46\,801 = 15 \times 3120 + 1\).

</details>

### Exercice 14 – Un chiffrement RSA de jouet

Soit \(p = 61\), \(q = 53\), \(n = pq = 3233\), \(\varphi = (p-1)(q-1) = 3120\), la clé publique \(e = 17\) et la clé privée \(d = 2753\) (exercice 13).

1. Chiffrer \(m = 65\) : \(c = m^{17} \bmod 3233\). On utilisera \(17 = 16 + 1\) (élévations au carré successives).
2. Pourquoi le déchiffrement \(c^{d} \bmod n\) redonne-t-il \(m\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(65^2 = 4225 \equiv 992\) ; \(992^2 \equiv 1232\) ; \(1232^2 \equiv 1547\) ; \(1547^2 \equiv 789\) (modulo 3233), donc \(65^{16} \equiv 789\). Alors \(65^{17} \equiv 789 \times 65 = 51\,285 \equiv \mathbf{2790}\).
2. Comme \(ed \equiv 1 \pmod{\varphi}\), on a \(m^{ed} \equiv m \pmod{n}\) (théorème d'Euler, ou petit théorème de Fermat et restes chinois). Ici \(2790^{2753} \bmod 3233 = 65\). *Attention : ces valeurs sont minuscules ; un vrai RSA utilise des nombres de plus de 600 chiffres.*

</details>

### Exercice 15 – Restes chinois

Trouver les entiers \(x\) tels que \(x \equiv 2 \pmod 3\), \(x \equiv 3 \pmod 5\) et \(x \equiv 2 \pmod 7\).

<details markdown="1">
<summary>Voir la réponse</summary>

Les nombres \(x \equiv 2 \pmod 3\) et \(x \equiv 2 \pmod 7\) vérifient \(x \equiv 2 \pmod{21}\) (3 et 7 sont premiers entre eux) : \(x \in \{2, 23, 44, 65, 86, \dots\}\). On cherche celui qui est congru à 3 modulo 5 : \(2 \to 2\), \(23 \to 3\). Donc \(x = 23\), et les solutions sont **\(x \equiv 23 \pmod{105}\)** (\(105 = 3 \times 5 \times 7\)), unique modulo 105.

</details>

## Auto-évaluation

- [ ] Je convertis un entier ou un nombre à virgule entre les bases 2, 10 et 16 en écrivant mes étapes.
- [ ] J'effectue une addition, une soustraction, une multiplication et une division par \(2^k\) en binaire.
- [ ] Je décompose un entier en facteurs premiers et j'applique l'algorithme d'Euclide.
- [ ] Je calcule une puissance modulo \(n\) en repérant un cycle.
- [ ] Je sais dire quand un parcours circulaire par sauts est exhaustif.
- [ ] Je calcule une adresse réseau avec un masque.

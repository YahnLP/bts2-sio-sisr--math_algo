# Synthèse – Arithmétique : numération et arithmétique modulaire

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – R1*

> [!NOTE]
> **Rôle de cette page.** Elle rassemble l'essentiel du programme d'arithmétique, les **méthodes** à savoir dérouler sans hésiter et les **pièges** qui coûtent des points. Les démonstrations et les exemples détaillés sont dans le [site de 1re année](https://yahnlp.github.io/bts1-sio-sisr-math_algo/) (séances S01, S02, S05, S06, S07).

## I. Numération

| À savoir faire | Méthode | Contrôle |
|---|---|---|
| Décimal → base \(b\) (entier) | Divisions euclidiennes successives par \(b\) ; on lit les restes **de bas en haut** | Refaire la somme \(\sum r_i b^i\) |
| Base \(b\) → décimal | \(\sum c_i b^i\) (schéma de Horner) | Comparer avec la conversion inverse |
| Binaire ↔ hexadécimal | Groupes de **4 bits** en partant de la droite | `0xB7` \(= 1011\,0111\) |
| Partie fractionnaire → binaire | Multiplications successives par 2 ; on lit les parties entières **de haut en bas** | S'arrêter quand la partie fractionnaire est nulle **ou** quand un reste se répète |
| Addition, soustraction, multiplication en base 2 | Comme en base 10 avec les retenues ; \(1 + 1 = 10_2\) | Reconvertir en décimal |
| Multiplier, diviser par \(2^k\) | **Décalage** de \(k\) rangs à gauche, à droite (quotient) ; les \(k\) bits sortants forment le reste | \(37 = 100101_2\), \(37 \div 8 = 4\) reste \(5\) |

**Précision et arrondi.** Un nombre n'a une écriture binaire finie que si son dénominateur (fraction irréductible) est une puissance de 2. Ainsi \(0{,}8125 = 13/16\) est exact en binaire, mais \(0{,}1 = 1/10\) est **périodique** : \(0{,}0\overline{0011}_2\). Un ordinateur le **tronque** : `0.1 + 0.2 == 0.3` est faux en Python.

> [!WARNING]
> **Pièges.** Lire les restes dans le bon sens. Oublier les zéros de tête sur un octet. Confondre \(2^{10} = 1024\) (Kio) et \(10^3\) (ko). Sur \(n\) bits non signés, les valeurs vont de \(0\) à \(2^n - 1\) : au-delà, il y a **dépassement de capacité**.

## II. Division euclidienne, nombres premiers, PGCD

- **Division euclidienne.** Pour \(a \in \mathbb{Z}\) et \(b \in \mathbb{N}^*\), il existe un **unique** couple \((q, r)\) avec \(a = bq + r\) et \(0 \le r < b\). Le reste est **toujours positif** : \(-25 = 7 \times (-4) + 3\).
- **Nombre premier.** Entier \(\ge 2\) dont les seuls diviseurs positifs sont 1 et lui-même. Pour tester \(n\), il suffit d'essayer les diviseurs premiers \(d\) avec \(d^2 \le n\).
- **Décomposition.** Tout entier \(\ge 2\) s'écrit de façon **unique** comme produit de facteurs premiers.
- **PGCD.** Algorithme d'Euclide : \(\operatorname{PGCD}(a, b) = \operatorname{PGCD}(b, r)\) où \(r\) est le reste de \(a\) par \(b\) ; le dernier reste non nul est le PGCD. Relation : \(\operatorname{PGCD}(a,b) \times \operatorname{PPCM}(a,b) = ab\).
- **Premiers entre eux.** \(\operatorname{PGCD}(a, b) = 1\) (ils peuvent ne pas être premiers : 8 et 15).

## III. Congruences

\(a \equiv b \pmod n\) signifie que \(n\) divise \(a - b\), c'est-à-dire que \(a\) et \(b\) ont le **même reste** dans la division par \(n\).

- Compatibilité : si \(a \equiv b\) et \(c \equiv d\), alors \(a + c \equiv b + d\) et \(ac \equiv bd\) ; donc \(a^k \equiv b^k\).
- **Réduire avant de calculer** : on remplace chaque nombre par son reste, puis on répète.
- **Puissances modulo \(n\)** : repérer un cycle. Modulo 7, \(3^6 \equiv 1\), donc \(3^{2024} \equiv 3^{2024 \bmod 6}\).
- **Multiples modulo \(n\)** : les multiples de \(a\) modulo \(n\) sont exactement les multiples de \(\operatorname{PGCD}(a, n)\). Si \(\operatorname{PGCD}(a, n) = 1\), tous les restes apparaissent : \(a\) est **inversible** modulo \(n\).
- **Parcours d'une liste circulaire** de \(n\) cases par sauts de \(k\) : toutes les cases sont visitées si et seulement si \(\operatorname{PGCD}(k, n) = 1\) ; sinon on ne visite que \(n / \operatorname{PGCD}(k, n)\) cases.

## IV. Liens avec l'informatique

- **Adresse réseau** : ET bit à bit entre l'adresse et le masque ; **adresse de diffusion** : OU avec le complément du masque.
- **Masques binaires** : `x & 0b00001111` garde les 4 bits de poids faible ; `x | m` met à 1 ; `x ^ m` bascule.
- **Clés de contrôle** (NIR, ISBN, IBAN) : on calcule un reste modulo 97, 10 ou 11 pour détecter une erreur de saisie.
- **Chiffrements par décalage et affine** : \(y \equiv ax + b \pmod{26}\) ; le déchiffrement demande l'inverse de \(a\) modulo 26.

## À retenir pour le jour de l'épreuve

1. **Écrire les étapes** (divisions, retenues, restes) : un résultat seul n'est pas complet.
2. **Vérifier** par la conversion inverse, la multiplication \(bq + r\) ou un second chemin.
3. **Conclure par une phrase** qui répond à la question posée, avec l'unité.

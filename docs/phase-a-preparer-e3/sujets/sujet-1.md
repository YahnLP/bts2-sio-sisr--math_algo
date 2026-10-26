# Sujet 1 – L'atelier de maintenance (2 heures, 20 points)

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – sujet d'entraînement de l'auteur, **non officiel***

> [!NOTE]
> **Conditions.** Compose ce sujet **sans aide** et **chronométré** (2 heures). Les trois exercices sont indépendants. Calculatrice : selon les règles de la session. Chaque réponse est **justifiée** (étapes de calcul, tableaux, raisonnement). Le corrigé et le barème sont dans les blocs « Voir le corrigé ».
>
> **Répartition indicative :** exercice 1 (arithmétique) 6 points, exercice 2 (matrices et logique) 6 points, exercice 3 (programmation) 8 points.

## Exercice 1 – Numération, PGCD et congruences (6 points)

**1. (1,5 point)** Numération.

a) Écrire 725 en binaire puis en hexadécimal.
b) Convertir le nombre hexadécimal `1F3` en décimal.
c) Calculer en binaire, sur 8 bits, `10110101` + `01001011`. Que constate-t-on ? Justifier avec les valeurs décimales.

**2. (1 point)** Nombres à virgule.

a) Écrire \(0{,}6875\) en binaire.
b) Le nombre \(0{,}7\) possède-t-il une écriture binaire finie ? Justifier.

**3. (1,5 point)** Deux modèles de pièces sont livrés par lots de 924 et de 1 078 unités. On veut les répartir en caisses **identiques**, de la plus grande taille possible, sans reste.

a) Calculer le PGCD de 924 et de 1 078 par l'algorithme d'Euclide.
b) Vérifier avec les décompositions en facteurs premiers.
c) Combien de caisses de chaque modèle obtient-on ?

**4. (2 points)** Quinze techniciens, numérotés de 0 à 14, sont appelés en rotation : le technicien suivant le numéro \(i\) est \((i + k) \bmod 15\).

a) Pour \(k = 6\) puis \(k = 4\), combien de techniciens sont appelés avant de revenir au numéro 0 ? Justifier avec le PGCD.
b) Calculer \(2^{100} \bmod 7\) (on pourra chercher un cycle).

<details markdown="1">
<summary>Voir le corrigé de l'exercice 1</summary>

**1. (1,5 pt)**

a) *(0,5)* \(725 = 512 + 128 + 64 + 16 + 4 + 1\), soit \(725 = 1011010101_2\). Par groupes de 4 bits : \(0010\,1101\,0101\), soit \(725 = \texttt{2D5}_{16}\).
b) *(0,5)* \(\texttt{1F3} = 1 \times 256 + 15 \times 16 + 3 = 499\).
c) *(0,5)* \(10110101_2 = 181\) et \(01001011_2 = 75\). La somme est \(256 = 1\,0000\,0000_2\) : 9 bits. Sur 8 bits il reste \(00000000\) avec une **retenue sortante** : **dépassement de capacité** (la valeur maximale sur 8 bits est 255).

**2. (1 pt)**

a) *(0,5)* \(0{,}6875 = 11/16 = 0{,}1011_2\) (\(0{,}6875 \times 2 = 1{,}375\) donne 1 ; \(0{,}375 \times 2 = 0{,}75\) donne 0 ; \(0{,}75 \times 2 = 1{,}5\) donne 1 ; \(0{,}5 \times 2 = 1\) donne 1).
b) *(0,5)* \(0{,}7 = 7/10\) : le dénominateur \(10 = 2 \times 5\) n'est pas une puissance de 2, donc l'écriture binaire est **périodique** (infinie).

**3. (1,5 pt)**

a) *(0,5)* \(1078 = 1 \times 924 + 154\) ; \(924 = 6 \times 154 + 0\). Le PGCD est **154**.
b) *(0,5)* \(924 = 2^2 \times 3 \times 7 \times 11\) et \(1078 = 2 \times 7^2 \times 11\). Facteurs communs : \(2 \times 7 \times 11 = 154\).
c) *(0,5)* \(924 / 154 = 6\) caisses et \(1078 / 154 = 7\) caisses, de 154 pièces chacune.

**4. (2 pts)**

a) *(1)* \(k = 6\) : \(\operatorname{PGCD}(6, 15) = 3\), donc \(15 / 3 = 5\) techniciens sont appelés (0, 6, 12, 3, 9). \(k = 4\) : \(\operatorname{PGCD}(4, 15) = 1\), donc les **15** sont appelés.
b) *(1)* Modulo 7 : \(2^1 \equiv 2\), \(2^2 \equiv 4\), \(2^3 \equiv 1\) : cycle de longueur 3. \(100 = 3 \times 33 + 1\), donc \(2^{100} \equiv 2^1 \equiv \mathbf{2}\).

</details>

## Exercice 2 – Système de prix et règle de sauvegarde (6 points)

**1. (3 points)** L'atelier achète des commutateurs (prix unitaire \(x\) euros) et des routeurs (prix unitaire \(y\) euros). Une première commande de 3 commutateurs et 2 routeurs coûte 260 euros ; une seconde, de 4 commutateurs et 3 routeurs, coûte 370 euros.

a) Écrire le système sous la forme \(AX = B\).
b) Vérifier que \(N = \begin{pmatrix} 3 & -2 \\ -4 & 3 \end{pmatrix}\) est l'inverse de \(A\).
c) En déduire \(x\) et \(y\), puis vérifier.

**2. (3 points)** Une sauvegarde nocturne est lancée selon trois indicateurs : \(a\) = « serveur A prêt », \(b\) = « lien réseau actif », \(c\) = « serveur C prêt ». La fonction de lancement est

\[
F = \overline{a}\,b\,c + a\,b\,\overline{c} + a\,b\,c .
\]

a) Dresser la table de vérité de \(F\).
b) Simplifier \(F\) à l'aide d'un tableau de Karnaugh.
c) Traduire la règle simplifiée par une phrase.

<details markdown="1">
<summary>Voir le corrigé de l'exercice 2</summary>

**1. (3 pts)**

a) *(1)* \(\begin{cases} 3x + 2y = 260 \\ 4x + 3y = 370 \end{cases}\), soit \(A = \begin{pmatrix} 3 & 2 \\ 4 & 3 \end{pmatrix}\), \(X = \begin{pmatrix} x \\ y \end{pmatrix}\), \(B = \begin{pmatrix} 260 \\ 370 \end{pmatrix}\).
b) *(1)* \(AN = \begin{pmatrix} 9 - 8 & -6 + 6 \\ 12 - 12 & -8 + 9 \end{pmatrix} = I_2\) (et \(NA = I_2\)) : \(N = A^{-1}\).
c) *(1)* \(X = NB = \begin{pmatrix} 3 \cdot 260 - 2 \cdot 370 \\ -4 \cdot 260 + 3 \cdot 370 \end{pmatrix} = \begin{pmatrix} 40 \\ 70 \end{pmatrix}\). Un commutateur coûte **40 €** et un routeur **70 €**. Vérification : \(3 \cdot 40 + 2 \cdot 70 = 260\) ; \(4 \cdot 40 + 3 \cdot 70 = 370\).

**2. (3 pts)**

a) *(1)*

| \(a\) | \(b\) | \(c\) | \(F\) |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | **1** |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | **1** |
| 1 | 1 | 1 | **1** |

b) *(1,5)*

| \(a \backslash bc\) | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 0 | 0 | **1** | 0 |
| 1 | 0 | 0 | **1** | **1** |

Rectangle vertical de la colonne 11 : \(bc\). Rectangle horizontal \((1, 11)\) et \((1, 10)\) : \(ab\). \(F = bc + ab = b\,(a + c)\).
c) *(0,5)* **La sauvegarde est lancée si le lien réseau est actif et si l'un au moins des deux serveurs est prêt.**

</details>

## Exercice 3 – Journal des sauvegardes et programmation (8 points)

**1. (2 points)** On donne la fonction suivante.

```python
def mystere(t):
    r = []
    for i in range(1, len(t)):
        if t[i] > t[i - 1]:
            r.append(i)
    return r
```

a) Dresser le tableau de suivi pour `t = [5, 8, 8, 3, 9, 12, 2]` et donner la valeur retournée.
b) Quel est le rôle de cette fonction ? Que retourne `mystere([4])` ?

**2. (3 points)** Le journal est une liste de chaînes `"date;statut;durée"`, la durée en minutes. Par exemple :

```python
journal = ["2026-10-01;OK;42", "2026-10-02;ECHEC;0", "2026-10-03;OK;38",
           "2026-10-04;OK;55", "2026-10-05;ECHEC;0"]
```

a) Écrire `taux_reussite(journal)` qui retourne le pourcentage de lignes de statut `OK` (0 si le journal est vide). Que retourne-t-elle pour l'exemple ?
b) Écrire `duree_moyenne_ok(journal)` qui retourne la durée moyenne des sauvegardes réussies, ou `None` s'il n'y en a aucune. Que retourne-t-elle pour l'exemple ?

*Rappel :* `"a;b;c".split(";")` retourne `["a", "b", "c"]` ; `int("42")` retourne 42.

**3. (3 points)** Un octet de statut code trois sauvegardes : le bit 0 pour le disque, le bit 1 pour la base de données, le bit 2 pour la messagerie ; la valeur 1 signifie « réussie ».

a) Écrire `echecs(octet)` qui retourne la liste des noms des sauvegardes en échec (dans l'ordre `disque`, `base`, `messagerie`).
b) Donner les résultats pour `0b101`, `0b111` et `0b010`.
c) Écrire `tout_ok(octet)` qui retourne `True` si les trois bits sont à 1, en une seule comparaison avec un masque.

<details markdown="1">
<summary>Voir le corrigé de l'exercice 3</summary>

**1. (2 pts)**

a) *(1,5)*

| \(i\) | `t[i]` | `t[i-1]` | `t[i] > t[i-1]` | `r` après |
|---|---|---|---|---|
| 1 | 8 | 5 | oui | `[1]` |
| 2 | 8 | 8 | non | `[1]` |
| 3 | 3 | 8 | non | `[1]` |
| 4 | 9 | 3 | oui | `[1, 4]` |
| 5 | 12 | 9 | oui | `[1, 4, 5]` |
| 6 | 2 | 12 | non | `[1, 4, 5]` |

La fonction retourne **`[1, 4, 5]`**.
b) *(0,5)* Elle retourne les **indices** où la valeur est **strictement supérieure** à la précédente (les « hausses »). Pour `[4]`, la boucle ne fait aucun tour : elle retourne la liste vide `[]`.

**2. (3 pts)**

a) *(1,5)*

```python
def taux_reussite(journal):
    if len(journal) == 0:
        return 0
    ok = 0
    for ligne in journal:
        champs = ligne.split(";")
        if champs[1] == "OK":
            ok = ok + 1
    return 100 * ok / len(journal)
```

Pour l'exemple : 3 lignes `OK` sur 5, donc **60,0**.
b) *(1,5)*

```python
def duree_moyenne_ok(journal):
    total = 0
    n = 0
    for ligne in journal:
        champs = ligne.split(";")
        if champs[1] == "OK":
            total = total + int(champs[2])
            n = n + 1
    if n == 0:
        return None
    return total / n
```

Pour l'exemple : \((42 + 38 + 55) / 3 = \mathbf{45{,}0}\) minutes.
*Barème : initialisations (0,5), boucle et découpage (0,5), test et cumul (0,25), cas particulier (0,25).*

**3. (3 pts)**

a) *(1,5)*

```python
def echecs(octet):
    noms = ["disque", "base", "messagerie"]
    liste = []
    for k in range(3):
        if (octet >> k) & 1 == 0:
            liste.append(noms[k])
    return liste
```

b) *(0,5)* `echecs(0b101)` retourne `['base']` ; `echecs(0b111)` retourne `[]` ; `echecs(0b010)` retourne `['disque', 'messagerie']`.
c) *(1)* `def tout_ok(octet): return octet & 0b111 == 0b111`. Le masque `0b111` isole les trois bits utiles ; on compare à 0b111. En Python, on écrit de préférence `(octet & 0b111) == 0b111` pour éviter toute ambiguïté de priorité.

</details>

## Barème récapitulatif

| Exercice | Points |
|---|---|
| 1. Numération, PGCD, congruences | 6 |
| 2. Système et Karnaugh | 6 |
| 3. Programmation | 8 |
| **Total** | **20** |

> [!NOTE]
> **Auto-évaluation.** Sous 10 points : reprendre les séries de révision R1 (arithmétique) et R5 (programmation). Entre 10 et 15 : relire les corrigés et refaire les questions manquées. Au-dessus de 15 : passer au [sujet suivant](sujet-2.md).

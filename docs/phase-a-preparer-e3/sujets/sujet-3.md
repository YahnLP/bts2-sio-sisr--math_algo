# Sujet 3 – La sécurité des accès (2 heures, 20 points)

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – sujet d'entraînement de l'auteur, **non officiel***

> [!NOTE]
> **Conditions.** Compose ce sujet **sans aide** et **chronométré** (2 heures). Les trois exercices sont indépendants. Calculatrice : selon les règles de la session. Chaque réponse est **justifiée**. Le corrigé et le barème sont dans les blocs « Voir le corrigé ».
>
> **Répartition indicative :** exercice 1 (logique et ensembles) 6 points, exercice 2 (arithmétique modulaire) 6 points, exercice 3 (programmation) 8 points.

## Exercice 1 – Règles d'accès : logique et ensembles (6 points)

**1. (2 points)** On note \(P\) : « le pare-feu est actif » et \(Q\) : « le port est fermé ».

a) Dresser les tables de vérité de \(\neg(P \Rightarrow Q)\) et de \(P \wedge \neg Q\). Que constate-t-on ?
b) En déduire la négation de la phrase : « Si le pare-feu est actif, alors le port est fermé. »

**2. (2 points)** Soit \(a(r, p)\) le prédicat « la règle \(r\) autorise le poste \(p\) ».

a) Traduire en français : \(\forall p\ \exists r\ a(r, p)\) et \(\exists r\ \forall p\ a(r, p)\). Ces deux phrases sont-elles équivalentes ? Si non, laquelle entraîne l'autre ?
b) Écrire la négation de \(\forall p\ \exists r\ a(r, p)\) avec des quantificateurs, puis en français.

**3. (2 points)** Parmi 80 serveurs, 52 fonctionnent sous Linux, 38 sont virtualisés et 20 sont à la fois sous Linux et virtualisés.

a) Combien de serveurs sont sous Linux **ou** virtualisés ? Combien ne sont ni l'un ni l'autre ?
b) Combien de serveurs sous Linux ne sont pas virtualisés ?
c) Une configuration est un triplet (système, hyperviseur, site) avec 4 systèmes, 3 hyperviseurs et 2 sites. Combien de configurations ?

<details markdown="1">
<summary>Voir le corrigé de l'exercice 1</summary>

**1. (2 pts)**

a) *(1,5)*

| \(P\) | \(Q\) | \(P \Rightarrow Q\) | \(\neg(P \Rightarrow Q)\) | \(\neg Q\) | \(P \wedge \neg Q\) |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 0 |

Les colonnes 4 et 6 sont identiques : \(\neg(P \Rightarrow Q) \equiv P \wedge \neg Q\).
b) *(0,5)* **« Le pare-feu est actif et le port est ouvert. »**

**2. (2 pts)**

a) *(1)* \(\forall p\ \exists r\ a(r, p)\) : « chaque poste est autorisé par **au moins une** règle (qui peut dépendre du poste) ». \(\exists r\ \forall p\ a(r, p)\) : « il existe **une** règle qui autorise **tous** les postes ». **Non équivalentes** : la seconde entraîne la première, pas l'inverse.
b) *(1)* \(\exists p\ \forall r\ \neg a(r, p)\) : **« Il existe un poste qu'aucune règle n'autorise. »**

**3. (2 pts)**

a) *(0,75)* \(|L \cup V| = 52 + 38 - 20 = 70\). Ni l'un ni l'autre : \(80 - 70 = \mathbf{10}\).
b) *(0,5)* \(52 - 20 = \mathbf{32}\).
c) *(0,75)* \(4 \times 3 \times 2 = \mathbf{24}\) configurations.

</details>

## Exercice 2 – Un chiffrement affine (6 points)

On associe à chaque lettre un nombre : A = 0, B = 1, …, Z = 25. Une lettre de rang \(x\) est chiffrée en la lettre de rang \(y\) avec
\[
y \equiv 5x + 8 \pmod{26}.
\]

**1. (1 point)** Chiffrer la lettre D.

**2. (2 points)**

a) Montrer que 21 est l'inverse de 5 modulo 26.
b) En déduire que \(x \equiv 21\,(y - 8) \pmod{26}\).

**3. (2 points)** Déchiffrer le mot `UWUP`.

**4. (1 point)** On voudrait utiliser \(y \equiv 13x + 8 \pmod{26}\). Pourquoi ce chiffrement est-il inutilisable ? On pourra comparer les images de deux lettres de même parité.

<details markdown="1">
<summary>Voir le corrigé de l'exercice 2</summary>

**1. (1 pt)** D a pour rang 3 : \(y \equiv 5 \times 3 + 8 = 23\), qui est la lettre **X**.

**2. (2 pts)**

a) *(1)* \(5 \times 21 = 105 = 4 \times 26 + 1\), donc \(5 \times 21 \equiv 1 \pmod{26}\) : 21 est l'inverse de 5 modulo 26.
b) *(1)* De \(y \equiv 5x + 8\), on tire \(y - 8 \equiv 5x\). On multiplie par 21 : \(21(y - 8) \equiv 21 \times 5\,x \equiv x \pmod{26}\).

**3. (2 pts)** U = 20 : \(21 \times (20 - 8) = 252 = 9 \times 26 + 18\) : rang 18, **S**. W = 22 : \(21 \times 14 = 294 = 11 \times 26 + 8\) : rang 8, **I**. U : **S**. P = 15 : \(21 \times 7 = 147 = 5 \times 26 + 17\) : rang 17, **R**. Le mot est **SISR**. Contrôle : \(5 \times 18 + 8 = 98 \equiv 20\), donc S donne bien U.

**4. (1 pt)** \(\operatorname{PGCD}(13, 26) = 13 \ne 1\) : 13 n'a pas d'inverse modulo 26. Concrètement, \(13x\) vaut 0 si \(x\) est pair et 13 si \(x\) est impair : \(y\) ne prend que **deux valeurs** (8 et 21) et deux lettres de même parité sont chiffrées de la même façon (A et C, par exemple, donnent toutes deux I) : on ne peut pas déchiffrer sans ambiguïté.

</details>

## Exercice 3 – Programmer le chiffrement (8 points)

**1. (2 points)** Écrire `inverse(a, m)` qui retourne l'inverse de `a` modulo `m` (un entier \(x\) entre 1 et \(m - 1\) tel que \(a x \equiv 1 \pmod m\)), ou `None` s'il n'existe pas. Donner `inverse(5, 26)`, `inverse(7, 26)` et `inverse(13, 26)`.

**2. (3 points)** Écrire `chiffrer(texte, a, b)` qui chiffre les lettres **majuscules** (rang \(x\) devient \((a x + b) \bmod 26\)) et laisse tous les autres caractères inchangés. Donner `chiffrer("SISR", 5, 8)` et `chiffrer("BTS SIO", 5, 8)`.

*Rappel :* `ord("A")` retourne 65 ; `chr(65)` retourne `"A"` ; `"A" <= c <= "Z"` teste une majuscule.

**3. (3 points)** Écrire `dechiffrer(texte, a, b)` qui inverse l'opération et lève une erreur (`ValueError`) si `a` n'est pas inversible modulo 26. Proposer un test qui vérifie que `dechiffrer(chiffrer(t, a, b), a, b)` redonne `t` pour `a = 7` et `b = 3`.

<details markdown="1">
<summary>Voir le corrigé de l'exercice 3</summary>

**1. (2 pts)**

```python
def inverse(a, m):
    for x in range(1, m):
        if a * x % m == 1:
            return x
    return None
```

*(1,5 pour le programme, 0,5 pour les résultats)* `inverse(5, 26)` retourne **21** ; `inverse(7, 26)` retourne **15** (\(7 \times 15 = 105 \equiv 1\)) ; `inverse(13, 26)` retourne **`None`**.

**2. (3 pts)**

```python
def chiffrer(texte, a, b):
    resultat = ""
    for c in texte:
        if "A" <= c <= "Z":
            rang = ord(c) - ord("A")
            resultat = resultat + chr((a * rang + b) % 26 + ord("A"))
        else:
            resultat = resultat + c
    return resultat
```

*Barème : parcours et construction du résultat (1), conversion lettre-rang-lettre (1), cas des caractères non majuscules (1).* `chiffrer("SISR", 5, 8)` retourne **`"UWUP"`** ; `chiffrer("BTS SIO", 5, 8)` retourne **`"NZU UWA"`** (l'espace est conservé).

**3. (3 pts)**

```python
def dechiffrer(texte, a, b):
    inv = inverse(a, 26)
    if inv is None:
        raise ValueError("a n'est pas inversible modulo 26")
    resultat = ""
    for c in texte:
        if "A" <= c <= "Z":
            rang = ord(c) - ord("A")
            resultat = resultat + chr(inv * (rang - b) % 26 + ord("A"))
        else:
            resultat = resultat + c
    return resultat

t = "RESEAU ET SYSTEMES"
assert dechiffrer(chiffrer(t, 7, 3), 7, 3) == t
```

*Barème : calcul de l'inverse et erreur (1), formule de déchiffrement (1), test (1).* L'opérateur `%` de Python retourne un reste **positif** même pour un nombre négatif, ce qui évite d'ajouter 26 à la main (`rang - b` peut être négatif). `dechiffrer("UWUP", 5, 8)` retourne `"SISR"`.

</details>

## Barème récapitulatif

| Exercice | Points |
|---|---|
| 1. Logique et ensembles | 6 |
| 2. Chiffrement affine | 6 |
| 3. Programmation | 8 |
| **Total** | **20** |

> [!NOTE]
> **Auto-évaluation.** Sous 10 points : reprendre R3 (logique), R1 (congruences) et R5 (programmation). Au-dessus de 15 : passer au [sujet suivant](sujet-4.md).

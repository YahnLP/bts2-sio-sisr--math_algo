# Exercices – Logique, ensembles et calcul booléen

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – R3*

> [!NOTE]
> **Comment travailler.** Cherche sur papier, avec tables et schémas, puis compare. Trois niveaux : **socle**, **format épreuve**, **pour aller plus loin** (au-delà du programme de l'épreuve).

## Niveau 1 – Socle

### Exercice 1 – Tables de vérité

Dresser les tables de vérité de \(P \Rightarrow Q\) et de \(\neg P \vee Q\), puis de \(\neg(P \wedge Q)\) et de \(\neg P \vee \neg Q\). Que constate-t-on ?

<details markdown="1">
<summary>Voir la réponse</summary>

| \(P\) | \(Q\) | \(P \Rightarrow Q\) | \(\neg P \vee Q\) | \(\neg(P \wedge Q)\) | \(\neg P \vee \neg Q\) |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 1 | 1 | 1 |
| 0 | 1 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |

Les colonnes deux à deux sont identiques : \(P \Rightarrow Q \equiv \neg P \vee Q\) et \(\neg(P \wedge Q) \equiv \neg P \vee \neg Q\) (loi de Morgan).

</details>

### Exercice 2 – Quantificateurs et négations

On considère l'ensemble \(U\) des utilisateurs d'un service.

1. Écrire avec des quantificateurs : « Tous les utilisateurs ont un mot de passe d'au moins 12 caractères. » Puis sa négation, en français et en symboles.
2. Écrire la négation de « Il existe un port ouvert inutile. »
3. Soit \(t(x, y)\) : « l'utilisateur \(x\) peut se connecter au poste \(y\) ». Traduire \(\forall x\ \exists y\ t(x, y)\) et \(\exists y\ \forall x\ t(x, y)\). Sont-elles équivalentes ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(\forall x \in U,\ \text{long}(x) \ge 12\). Négation : \(\exists x \in U,\ \text{long}(x) < 12\) : « Au moins un utilisateur a un mot de passe de moins de 12 caractères. »
2. « Tout port est utile » (aucun port ouvert n'est inutile) : \(\forall p,\ \neg\,\text{inutile}(p)\).
3. La première : « chaque utilisateur peut se connecter à **au moins un** poste (qui dépend de lui) ». La seconde : « il existe **un** poste auquel **tous** les utilisateurs peuvent se connecter ». La seconde entraîne la première, pas l'inverse : **elles ne sont pas équivalentes**.

</details>

### Exercice 3 – Opérations sur les ensembles

Dans \(E = \{1, 2, \dots, 10\}\), soit \(A\) l'ensemble des nombres pairs et \(B\) celui des multiples de 3. Déterminer \(A \cap B\), \(A \cup B\), \(\overline{A}\), \(A \setminus B\) et \(|A \cup B|\). Vérifier la formule des cardinaux.

<details markdown="1">
<summary>Voir la réponse</summary>

\(A = \{2, 4, 6, 8, 10\}\), \(B = \{3, 6, 9\}\). \(A \cap B = \{6\}\) ; \(A \cup B = \{2, 3, 4, 6, 8, 9, 10\}\) ; \(\overline{A} = \{1, 3, 5, 7, 9\}\) ; \(A \setminus B = \{2, 4, 8, 10\}\). \(|A \cup B| = 7\), et \(|A| + |B| - |A \cap B| = 5 + 3 - 1 = 7\).

</details>

### Exercice 4 – Dénombrement

Sur 150 comptes, 90 utilisent l'authentification multifacteur (MFA), 60 utilisent une clé SSH et 35 utilisent les deux. Combien de comptes utilisent au moins l'un des deux ? Aucun des deux ? Seulement le MFA ?

<details markdown="1">
<summary>Voir la réponse</summary>

Au moins l'un : \(90 + 60 - 35 = 115\). Aucun des deux : \(150 - 115 = 35\). Seulement le MFA : \(90 - 35 = 55\).

</details>

### Exercice 5 – Produit cartésien

Une configuration de test est un triplet (système, navigateur, architecture) avec 3 systèmes, 4 navigateurs et 2 architectures. Combien de configurations ? Citer trois éléments de l'ensemble produit.

<details markdown="1">
<summary>Voir la réponse</summary>

\(|S \times N \times A| = 3 \times 4 \times 2 = 24\) configurations. Par exemple (Linux, Firefox, ARM), (Windows, Edge, x86) et (macOS, Safari, ARM), en supposant ces valeurs dans les ensembles.

</details>

## Niveau 2 – Format épreuve

### Exercice 6 – Une relation d'équivalence

Sur \(E = \{1, 2, 3, 4, 5, 6\}\), on définit \(x \mathcal{R} y\) si \(x - y\) est divisible par 3.

1. Montrer que \(\mathcal{R}\) est une relation d'équivalence.
2. Déterminer ses classes d'équivalence.

<details markdown="1">
<summary>Voir la réponse</summary>

1. *Réflexive* : \(x - x = 0\) est divisible par 3. *Symétrique* : si 3 divise \(x - y\), il divise \(y - x = -(x - y)\). *Transitive* : si 3 divise \(x - y\) et \(y - z\), il divise leur somme \(x - z\). Les trois propriétés sont vérifiées.
2. Les classes sont les ensembles d'éléments de même reste modulo 3 : \(\{1, 4\}\), \(\{2, 5\}\), \(\{3, 6\}\). Elles sont disjointes et leur réunion est \(E\).

</details>

### Exercice 7 – Une relation d'ordre

Sur \(E = \{1, 2, 3, 4, 6, 12\}\), on définit \(x \preceq y\) si \(x\) divise \(y\).

1. Montrer que c'est une relation d'ordre.
2. L'ordre est-il total ? Citer deux éléments non comparables.
3. Tracer le diagramme de Hasse (on ne représente que les liens « directs »). Donner l'élément minimal et l'élément maximal.

<details markdown="1">
<summary>Voir la réponse</summary>

1. *Réflexive* : \(x\) divise \(x\). *Antisymétrique* : si \(x\) divise \(y\) et \(y\) divise \(x\), alors \(x = y\) (entiers positifs). *Transitive* : si \(x \mid y\) et \(y \mid z\), alors \(x \mid z\).
2. **Non total** : 2 ne divise pas 3 et 3 ne divise pas 2 ; de même 4 et 6.
3. Liens directs : \(1 \to 2\), \(1 \to 3\), \(2 \to 4\), \(2 \to 6\), \(3 \to 6\), \(4 \to 12\), \(6 \to 12\). Minimal : **1**. Maximal : **12**.

<figure class="graphe diagramme">
<svg viewBox="0 0 360 250" role="img" aria-label="Diagramme de Hasse de la divisibilité sur 1, 2, 3, 4, 6, 12">
<line class="dg-line" x1="180" y1="210" x2="110" y2="150"/><line class="dg-line" x1="180" y1="210" x2="250" y2="150"/>
<line class="dg-line" x1="110" y1="150" x2="60" y2="90"/><line class="dg-line" x1="110" y1="150" x2="180" y2="90"/>
<line class="dg-line" x1="250" y1="150" x2="180" y2="90"/>
<line class="dg-line" x1="60" y1="90" x2="120" y2="30"/><line class="dg-line" x1="180" y1="90" x2="120" y2="30"/>
<circle class="dg-box" cx="180" cy="210" r="18"/><text class="dg-t" x="180" y="216" text-anchor="middle">1</text>
<circle class="dg-box" cx="110" cy="150" r="18"/><text class="dg-t" x="110" y="156" text-anchor="middle">2</text>
<circle class="dg-box" cx="250" cy="150" r="18"/><text class="dg-t" x="250" y="156" text-anchor="middle">3</text>
<circle class="dg-box" cx="60" cy="90" r="18"/><text class="dg-t" x="60" y="96" text-anchor="middle">4</text>
<circle class="dg-box" cx="180" cy="90" r="18"/><text class="dg-t" x="180" y="96" text-anchor="middle">6</text>
<circle class="dg-box" cx="120" cy="30" r="18"/><text class="dg-t" x="120" y="36" text-anchor="middle">12</text>
</svg>
<figcaption>Diagramme de Hasse : un trait relie deux éléments quand le plus bas divise directement le plus haut.</figcaption>
</figure>

</details>

### Exercice 8 – Applications

1. Soit \(f : \{1, 2, 3, 4\} \to \{a, b, c\}\) avec \(f(1) = a\), \(f(2) = b\), \(f(3) = a\), \(f(4) = c\). Est-ce une application ? Est-elle injective ? surjective ?
2. Étudier \(h : \mathbb{R} \to \mathbb{R},\ x \mapsto x^2\) : injective ? surjective ? Donner \(h^{-1}(\{4\})\) et \(h([-1, 2])\).
3. \(k : \mathbb{R} \to \mathbb{R},\ x \mapsto 2x + 1\) est-elle bijective ? Donner \(k^{-1}\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. Chaque élément de départ a **une seule** image : c'est une application. **Non injective** (\(f(1) = f(3) = a\)). **Surjective** : \(a\), \(b\), \(c\) ont tous un antécédent.
2. **Non injective** (\(h(-2) = h(2) = 4\)), **non surjective** (\(-1\) n'a pas d'antécédent). \(h^{-1}(\{4\}) = \{-2, 2\}\) ; \(h([-1, 2]) = [0, 4]\).
3. Pour tout réel \(y\), \(2x + 1 = y \iff x = (y - 1)/2\) : un unique antécédent, donc **bijective**, avec \(k^{-1}(y) = (y - 1)/2\).

</details>

### Exercice 9 – Composition

Avec \(f(x) = 2x + 1\) et \(g(x) = x^2\) définies sur \(\mathbb{R}\), calculer \(g \circ f\) et \(f \circ g\). Sont-elles égales ? La composée \(g \circ f\) est-elle injective ? Conclure sur le lien avec les propriétés de \(f\) et \(g\).

<details markdown="1">
<summary>Voir la réponse</summary>

\((g \circ f)(x) = (2x + 1)^2\) et \((f \circ g)(x) = 2x^2 + 1\). En \(x = 1\) : 9 et 3, donc **la composition n'est pas commutative**. \(g \circ f\) n'est pas injective (\(x = 0\) et \(x = -1\) donnent 1). Ce n'est pas contradictoire avec le cours : \(f\) est injective mais \(g\) ne l'est pas, et la propriété « composée de deux injections est injective » demande les **deux** injectivités.

</details>

### Exercice 10 – Simplification par Karnaugh

Une alarme se déclenche selon trois indicateurs : \(a\) = accès hors horaires, \(b\) = badge invalide, \(c\) = mouvement détecté. Elle se déclenche dans les cas où \((a, b, c)\) vaut \((0,0,1)\), \((0,1,1)\), \((1,0,1)\), \((1,1,0)\) et \((1,1,1)\).

1. Écrire le tableau de Karnaugh de la fonction \(F\).
2. En déduire une expression simplifiée et l'interpréter.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Lignes : \(a\) ; colonnes : \(bc\) dans l'ordre \(00, 01, 11, 10\) (une seule variable change d'une colonne à la suivante).

| \(a \backslash bc\) | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | 0 | **1** | **1** | 0 |
| 1 | 0 | **1** | **1** | **1** |

2. Premier rectangle : les quatre cases des colonnes 01 et 11 (variables constantes : \(c = 1\)) : terme \(c\). Second rectangle : les cases \((1, 11)\) et \((1, 10)\) (\(a = 1\), \(b = 1\)) : terme \(ab\). Donc \(F = c + ab\) : **l'alarme se déclenche si un mouvement est détecté, ou si l'accès est hors horaires avec un badge invalide.**

</details>

### Exercice 11 – Portes NAND

On note \(x \uparrow y = \overline{x\,y}\) (NAND). Exprimer \(a\,b + c\) uniquement avec des portes NAND. Combien de portes faut-il ?

<details markdown="1">
<summary>Voir la réponse</summary>

On a \(\overline{c} = c \uparrow c\). Alors \((a \uparrow b) \uparrow (c \uparrow c) = \overline{\overline{ab}\cdot\overline{c}} = ab + c\) (Morgan). Il faut **3 portes NAND** : \(a \uparrow b\), \(c \uparrow c\), puis la porte finale. On vérifie sur les 8 lignes de la table : par exemple pour \(a = 0, b = 1, c = 1\) : \(a \uparrow b = 1\), \(c \uparrow c = 0\), \(1 \uparrow 0 = 1 = 0 \cdot 1 + 1\).

</details>

### Exercice 12 – Règle d'accès à deux variables

L'accès à une salle est autorisé quand \(F = ab + a\overline{b} + \overline{a}b\), où \(a\) = « badge personnel valide » et \(b\) = « code valide ». Simplifier \(F\) par Karnaugh, puis par le calcul. Interpréter.

<details markdown="1">
<summary>Voir la réponse</summary>

| \(a \backslash b\) | 0 | 1 |
|---|---|---|
| 0 | 0 | **1** |
| 1 | **1** | **1** |

Rectangle de la ligne \(a = 1\) : terme \(a\). Rectangle de la colonne \(b = 1\) : terme \(b\). \(F = a + b\). Par le calcul : \(ab + a\overline{b} = a\), puis \(a + \overline{a}b = a + b\) (absorption). **L'accès est autorisé si l'un au moins des deux justificatifs est valide.**

</details>

## Niveau 3 – Pour aller plus loin

> [!NOTE]
> Hors programme de l'épreuve : démonstrations par contraposée et par l'absurde, dénombrement d'applications, quotient par une relation d'équivalence.

### Exercice 13 – Démonstration par contraposée et par l'absurde

1. Démontrer par **contraposée** : si \(n^2\) est pair, alors \(n\) est pair.
2. En déduire par l'**absurde** que \(\sqrt{2}\) est irrationnel.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Contraposée : « si \(n\) est impair, alors \(n^2\) est impair ». Si \(n = 2k + 1\), alors \(n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1\) est impair. La contraposée est vraie, donc l'implication aussi.
2. Supposons \(\sqrt{2} = p/q\) avec \(p, q\) entiers sans diviseur commun. Alors \(p^2 = 2q^2\), donc \(p^2\) est pair, donc \(p\) est pair (question 1) : \(p = 2m\). Alors \(4m^2 = 2q^2\), soit \(q^2 = 2m^2\) : \(q\) est pair aussi. Contradiction avec « sans diviseur commun ». Donc \(\sqrt{2}\) est irrationnel.

</details>

### Exercice 14 – Compter les applications (et les collisions)

On range 3 fichiers dans une table de 5 cases (une application \(E \to F\), \(|E| = 3\), \(|F| = 5\)).

1. Combien y a-t-il d'applications ? Combien sont injectives (aucune collision) ?
2. Une application de ce type peut-elle être surjective ?
3. On range maintenant 6 fichiers dans 5 cases. Montrer qu'il y a forcément une collision.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Chaque fichier a 5 choix : \(5^3 = 125\) applications. Injectives : 5 choix pour le premier, 4 pour le deuxième, 3 pour le troisième : \(5 \times 4 \times 3 = 60\).
2. Non : une application surjective sur 5 éléments demande au moins 5 éléments au départ, or \(|E| = 3\).
3. Une application d'un ensemble de 6 éléments dans un ensemble de 5 ne peut pas être injective (il y aurait au plus 5 images distinctes) : **principe des tiroirs**. Ce résultat justifie que toute fonction de hachage vers un espace plus petit produit des collisions.

</details>

### Exercice 15 – Équivalence et sous-réseaux

Sur l'ensemble des adresses IPv4, on pose \(x \mathcal{R} y\) si \(x\) et \(y\) ont la même adresse réseau pour le masque \(255.255.255.192\). Montrer que \(\mathcal{R}\) est une relation d'équivalence. Combien d'adresses y a-t-il dans une classe ? Combien de classes y a-t-il dans \(192.168.1.0/24\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

« Avoir la même adresse réseau » signifie que deux fonctions de \(x\) et de \(y\) sont égales (adresse ET masque). L'égalité étant réflexive, symétrique et transitive, \(\mathcal{R}\) l'est aussi. Chaque classe est un sous-réseau : le masque laisse 6 bits à l'hôte, soit \(2^6 = 64\) adresses (dont 62 utilisables). Dans \(192.168.1.0/24\), il y a \(256 / 64 = 4\) classes : \(.0\), \(.64\), \(.128\), \(.192\).

</details>

## Auto-évaluation

- [ ] Je dresse une table de vérité complète et je démontre une équivalence avec.
- [ ] Je nie une phrase avec quantificateurs.
- [ ] Je calcule un cardinal avec la formule \(|A \cup B|\).
- [ ] Je teste les quatre propriétés d'une relation et j'identifie classes ou diagramme de Hasse.
- [ ] Je classe une application (injective, surjective, bijective) en justifiant.
- [ ] Je simplifie une fonction à trois variables par Karnaugh et je l'interprète.

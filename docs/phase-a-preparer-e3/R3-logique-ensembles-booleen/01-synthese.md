# Synthèse – Logique, ensembles et calcul booléen

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – R3*

> [!NOTE]
> **Rôle de cette page.** L'essentiel de trois chapitres liés : calcul des propositions et des prédicats, langage ensembliste et éléments de théorie des ensembles, algèbre de Boole. Le cours complet est dans le [site de 1re année](https://yahnlp.github.io/bts1-sio-sisr-math_algo/) (séances S08 à S11).

## I. Calcul des propositions

Une **proposition** est un énoncé qui est vrai ou faux. Connecteurs : négation \(\neg P\), conjonction \(P \wedge Q\) (« et »), disjonction \(P \vee Q\) (« ou » inclusif), implication \(P \Rightarrow Q\), équivalence \(P \Leftrightarrow Q\).

| Équivalence à connaître | Nom |
|---|---|
| \(\neg(P \wedge Q) \equiv \neg P \vee \neg Q\) et \(\neg(P \vee Q) \equiv \neg P \wedge \neg Q\) | Lois de **Morgan** |
| \(P \Rightarrow Q \equiv \neg P \vee Q\) | Écriture de l'implication |
| \(P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P\) | **Contraposée** |
| \(\neg(P \Rightarrow Q) \equiv P \wedge \neg Q\) | Négation d'une implication |

**Méthode.** Pour démontrer une équivalence : dresser la **table de vérité** (toutes les combinaisons, \(2^n\) lignes pour \(n\) variables) et comparer les colonnes.

> [!WARNING]
> **Piège.** Une implication est **vraie** quand sa prémisse est fausse. La **réciproque** \(Q \Rightarrow P\) n'est pas équivalente à \(P \Rightarrow Q\).

## II. Prédicats et quantificateurs

Un **prédicat** \(p(x)\) dépend d'une variable. \(\forall x,\ p(x)\) : « pour tout \(x\) » ; \(\exists x,\ p(x)\) : « il existe un \(x\) ».

- \(\neg(\forall x,\ p(x)) \equiv \exists x,\ \neg p(x)\) et \(\neg(\exists x,\ p(x)) \equiv \forall x,\ \neg p(x)\).
- **L'ordre compte** : \(\forall x\,\exists y\) n'est pas équivalent à \(\exists y\,\forall x\). « Chaque salarié a un poste » \(\ne\) « un même poste sert à tous les salariés ».
- Pour réfuter un « \(\forall\) », il suffit d'un **contre-exemple**.

## III. Ensembles

Appartenance \(x \in E\), inclusion \(A \subset B\) (tout élément de \(A\) est dans \(B\)), ensemble des parties \(\mathcal{P}(E)\) (\(2^{|E|}\) éléments si \(E\) est fini).

- Opérations : \(A \cap B\), \(A \cup B\), complémentaire \(\overline{A}\), différence \(A \setminus B\).
- **Morgan** : \(\overline{A \cap B} = \overline{A} \cup \overline{B}\) ; \(\overline{A \cup B} = \overline{A} \cap \overline{B}\).
- **Cardinal** : \(|A \cup B| = |A| + |B| - |A \cap B|\).
- Une relation \(p(x)\) définit la partie \(\{x \in E \mid p(x)\}\) : « et » devient \(\cap\), « ou » devient \(\cup\), « non » devient le complémentaire, \(\Rightarrow\) devient \(\subset\).

**Produit cartésien.** \(E \times F = \{(x, y) \mid x \in E, y \in F\}\) ; \(|E \times F| = |E| \cdot |F|\). Pour \(n\) ensembles finis, le cardinal est le produit des cardinaux.

## IV. Relations binaires

Une relation sur \(E\) est une partie de \(E \times E\). Propriétés :

| Propriété | Définition |
|---|---|
| Réflexive | \(x \mathcal{R} x\) pour tout \(x\) |
| Symétrique | \(x \mathcal{R} y \Rightarrow y \mathcal{R} x\) |
| Antisymétrique | \(x \mathcal{R} y\) et \(y \mathcal{R} x \Rightarrow x = y\) |
| Transitive | \(x \mathcal{R} y\) et \(y \mathcal{R} z \Rightarrow x \mathcal{R} z\) |

- **Relation d'équivalence** : réflexive, symétrique, transitive. Elle partage \(E\) en **classes** disjointes dont la réunion est \(E\).
- **Relation d'ordre** : réflexive, antisymétrique, transitive. L'ordre est **total** si deux éléments quelconques sont comparables, **partiel** sinon.

## V. Applications

Une **application** \(f : E \to F\) associe à **chaque** élément de \(E\) **exactement un** élément de \(F\). Elle est :

- **injective** si deux éléments distincts ont des images distinctes (pas de « collision ») ;
- **surjective** si tout élément de \(F\) a au moins un antécédent ;
- **bijective** si elle est injective et surjective ; elle a alors une réciproque \(f^{-1}\).

Image directe \(f(A) = \{f(x) \mid x \in A\}\) ; **image réciproque** \(f^{-1}(B) = \{x \in E \mid f(x) \in B\}\) (elle existe même si \(f\) n'est pas bijective). Composée : \((g \circ f)(x) = g(f(x))\) : on applique \(f\) d'abord. La composée de deux injections (resp. surjections, bijections) est une injection (resp. surjection, bijection).

## VI. Calcul booléen

Opérations : \(a + b\) (OU), \(a \cdot b\) (ET), \(\overline{a}\) (NON). Propriétés : commutativité, associativité, distributivité (dans les **deux** sens), \(a + a = a\), \(a + \overline{a} = 1\), \(a \cdot \overline{a} = 0\), absorption \(a + ab = a\), **Morgan** \(\overline{a + b} = \overline{a}\,\overline{b}\) et \(\overline{ab} = \overline{a} + \overline{b}\).

**Simplification par tableau de Karnaugh** (2 ou 3 variables) : on range la table de vérité dans une grille où deux cases voisines ne diffèrent que d'une variable ; on entoure les **1** par des rectangles de 1, 2, 4 ou 8 cases (puissances de 2, bords raccordés), les plus grands possibles ; chaque rectangle donne un **terme produit** (on garde les variables qui ne changent pas) ; on additionne les termes.

**Portes NON-ET (NAND) et NON-OU (NOR).** Chacune permet, à elle seule, de réaliser toutes les autres fonctions : \(\overline{a} = a \uparrow a\).

## À retenir pour le jour de l'épreuve

1. Pour prouver une équivalence : table de vérité **complète** ; pour réfuter une affirmation : **un contre-exemple**.
2. Pour une relation : tester **chaque propriété** séparément et citer le cas qui échoue.
3. Pour Karnaugh : **tableau + rectangles + expression finale**, puis une phrase d'interprétation.

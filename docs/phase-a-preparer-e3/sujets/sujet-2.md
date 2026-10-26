# Sujet 2 – Le déploiement Wi-Fi de l'agence (2 heures, 20 points)

*BTS SIO SISR 2e année – Préparer l'épreuve E3 – sujet d'entraînement de l'auteur, **non officiel***

> [!NOTE]
> **Conditions.** Compose ce sujet **sans aide** et **chronométré** (2 heures). Les trois exercices sont indépendants. Calculatrice : selon les règles de la session. Chaque réponse est **justifiée**. Le corrigé et le barème sont dans les blocs « Voir le corrigé ».
>
> **Répartition indicative :** exercice 1 (graphes et ordonnancement) 7 points, exercice 2 (relations et applications) 5 points, exercice 3 (programmation) 8 points.

## Exercice 1 – Planifier le déploiement (7 points)

Le déploiement du Wi-Fi d'une agence se décompose en huit tâches (durées en jours).

| Tâche | Désignation | Durée | Prédécesseurs |
|---|---|---|---|
| A | Étude de couverture | 3 | — |
| B | Commande des bornes | 2 | A |
| C | Câblage | 5 | A |
| D | Installation des bornes | 4 | B, C |
| E | Configuration du contrôleur | 3 | B |
| F | Tests de couverture | 2 | D, E |
| G | Formation des utilisateurs | 3 | C |
| H | Recette | 1 | F, G |

On note \(M\) la matrice d'adjacence du graphe des antériorités (un arc de \(X\) vers \(Y\) si \(X\) est prédécesseur direct de \(Y\)), les tâches étant prises dans l'ordre alphabétique. On donne le coefficient \((A, F)\) de \(M^3\) : il vaut 3.

**1. (2 points)**

a) Déterminer les niveaux du graphe des antériorités.
b) Que représente le coefficient \((A, F)\) de \(M^3\) ? Citer les chemins correspondants.

**2. (3 points)** *Rappel de méthode : date au plus tôt d'une tâche = maximum, sur ses antécédentes, de (date au plus tôt + durée) ; date au plus tard = minimum, sur ses successeurs, de (date au plus tard) moins la durée de la tâche ; marge totale = plus tard moins plus tôt ; une tâche est critique si sa marge est nulle.* Par la méthode MPM :

a) Calculer les dates au plus tôt et la durée minimale du projet.
b) Calculer les dates au plus tard et les marges totales.
c) Donner les tâches critiques et le chemin critique.

**3. (2 points)**

a) Calculer la marge libre et la marge certaine de la tâche E. Interpréter.
b) La tâche D prend finalement 2 jours de plus que prévu : quelle est la nouvelle durée du projet ? Et si c'est la tâche G qui prend 2 jours de plus ?

<details markdown="1">
<summary>Voir le corrigé de l'exercice 1</summary>

**1. (2 pts)**

a) *(1)* Niveau 0 : A. On retire A : niveau 1 : B, C. On retire B, C : niveau 2 : D, E, G. On retire D, E, G : niveau 3 : F. Niveau 4 : H. **Niveaux : \(\{A\}\), \(\{B, C\}\), \(\{D, E, G\}\), \(\{F\}\), \(\{H\}\).**
b) *(1)* C'est le nombre de chemins de longueur 3 de A à F. Il y en a **3** : \(A \to B \to D \to F\), \(A \to C \to D \to F\), \(A \to B \to E \to F\).

**2. (3 pts)**

| Tâche | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| Durée | 3 | 2 | 5 | 4 | 3 | 2 | 3 | 1 |
| Au plus tôt \(t\) | 0 | 3 | 3 | 8 | 5 | 12 | 8 | 14 |
| Au plus tard \(T\) | 0 | 6 | 3 | 8 | 9 | 12 | 11 | 14 |
| Marge totale | 0 | 3 | 0 | 0 | 4 | 0 | 3 | 0 |

a) *(1)* \(t(D) = \max(3 + 2,\ 3 + 5) = 8\) ; \(t(F) = \max(8 + 4,\ 5 + 3) = 12\) ; \(t(H) = \max(12 + 2,\ 8 + 3) = 14\). Durée : \(14 + 1 = \mathbf{15}\) **jours**.
b) *(1,5)* \(T(H) = 14\) ; \(T(F) = 14 - 2 = 12\) ; \(T(G) = 14 - 3 = 11\) ; \(T(E) = 12 - 3 = 9\) ; \(T(D) = 12 - 4 = 8\) ; \(T(C) = \min(8,\ 11) - 5 = 3\) ; \(T(B) = \min(8,\ 9) - 2 = 6\) ; \(T(A) = \min(6,\ 3) - 3 = 0\).
c) *(0,5)* Tâches critiques : A, C, D, F, H. **Chemin critique : A → C → D → F → H** (\(3 + 5 + 4 + 2 + 1 = 15\)).

**3. (2 pts)**

a) *(1,5)* \(M_L(E) = t(F) - t(E) - d(E) = 12 - 5 - 3 = 4\). \(M_C(E) = \max(0,\ t(F) - (T(B) + d(B)) - d(E)) = 12 - 8 - 3 = 1\). La configuration du contrôleur peut **glisser de 4 jours** sans décaler les tâches suivantes si B se termine à sa date au plus tôt, mais **seulement de 1 jour** si B se termine au plus tard.
b) *(0,5)* D est critique : le projet dure **17 jours**. G a une marge totale de 3 jours : un retard de 2 jours **ne change pas** la durée (15 jours).

</details>

## Exercice 2 – Relations et applications (5 points)

Soit \(E = \{1, 2, 3, 4\}\).

**1. (2 points)** La relation \(\mathcal{R}\) sur \(E\) est définie par l'ensemble de couples \(\{(1,1), (2,2), (3,3), (4,4), (1,2), (2,1), (3,4), (4,3)\}\).

a) Montrer que \(\mathcal{R}\) est une relation d'équivalence.
b) Donner ses classes d'équivalence.

**2. (1,5 point)** La relation \(\mathcal{S}\) sur \(E\) est définie par \(\{(1,1), (2,2), (3,3), (4,4), (1,2), (2,3)\}\). Étudier la réflexivité, la symétrie, l'antisymétrie et la transitivité. \(\mathcal{S}\) est-elle une relation d'ordre ? Une relation d'équivalence ?

**3. (1,5 point)** On considère \(f : E \to \{a, b, c\}\) avec \(f(1) = a\), \(f(2) = b\), \(f(3) = c\), \(f(4) = a\), et \(g : \{a, b, c\} \to \{x, y\}\) avec \(g(a) = x\), \(g(b) = y\), \(g(c) = x\).

a) Déterminer \(g \circ f\). Chacune des applications \(f\), \(g\), \(g \circ f\) est-elle injective ? surjective ?
b) Déterminer l'image réciproque \(g^{-1}(\{x\})\).

<details markdown="1">
<summary>Voir le corrigé de l'exercice 2</summary>

**1. (2 pts)**

a) *(1,5)* *Réflexive* : les quatre couples \((x, x)\) sont dans \(\mathcal{R}\). *Symétrique* : \((1, 2)\) et \((2, 1)\) sont tous deux dans \(\mathcal{R}\), de même \((3, 4)\) et \((4, 3)\) ; les autres couples sont des \((x, x)\). *Transitive* : les seuls enchaînements possibles se font à l'intérieur de \(\{1, 2\}\) ou de \(\{3, 4\}\) (par exemple \(1 \mathcal{R} 2\) et \(2 \mathcal{R} 1\) donnent \(1 \mathcal{R} 1\), présent) : aucun couple manquant.
b) *(0,5)* Classes : **\(\{1, 2\}\)** et **\(\{3, 4\}\)**.

**2. (1,5 pt)**

*Réflexive* : oui. *Symétrique* : non (\((1, 2) \in \mathcal{S}\) mais \((2, 1) \notin \mathcal{S}\)). *Antisymétrique* : oui (aucun couple \(x \ne y\) n'est présent dans les deux sens). *Transitive* : **non** : \(1 \mathcal{S} 2\) et \(2 \mathcal{S} 3\) mais \((1, 3) \notin \mathcal{S}\). Donc \(\mathcal{S}\) **n'est ni une relation d'ordre** (pas transitive), **ni une relation d'équivalence** (ni symétrique, ni transitive).

**3. (1,5 pt)**

a) *(1)* \((g \circ f)(1) = g(a) = x\) ; \((g \circ f)(2) = g(b) = y\) ; \((g \circ f)(3) = g(c) = x\) ; \((g \circ f)(4) = g(a) = x\). \(f\) : **surjective** (a, b, c atteints), non injective (\(f(1) = f(4)\)). \(g\) : **surjective**, non injective (\(g(a) = g(c)\)). \(g \circ f\) : **surjective** (x et y atteints), non injective.
b) *(0,5)* \(g^{-1}(\{x\}) = \{a, c\}\).

</details>

## Exercice 3 – Adresses IPv4 et programmation (8 points)

**1. (2 points)** On donne la fonction suivante.

```python
def mystere(n):
    r = ""
    while n > 0:
        r = str(n % 2) + r
        n = n // 2
    return r
```

a) Dresser le tableau de suivi pour \(n = 13\) et donner la valeur retournée.
b) Quel est le rôle de la fonction ? Que retourne `mystere(0)` ?

**2. (3 points)** Écrire `est_ipv4(s)` qui retourne `True` si la chaîne `s` est de la forme `a.b.c.d` où `a`, `b`, `c`, `d` sont **quatre entiers écrits en chiffres** compris entre 0 et 255, et `False` sinon. Donner les résultats pour `"192.168.1.10"`, `"256.1.1.1"`, `"1.2.3"` et `"1.2.3.a"`.

*Rappel :* `s.split(".")` découpe la chaîne ; `c.isdigit()` vaut `True` si `c` est une suite non vide de chiffres.

**3. (3 points)** On suppose les adresses valides.

a) Écrire `en_entier(s)` qui retourne l'entier de 32 bits associé à l'adresse (\(a \times 256^3 + b \times 256^2 + c \times 256 + d\)). Que retourne `en_entier("192.168.1.10")` ?
b) Écrire `meme_reseau(a, b, p)` qui retourne `True` si les adresses `a` et `b` ont les mêmes `p` premiers bits. Donner les résultats pour `"192.168.1.10"` et `"192.168.1.77"` avec \(p = 24\) puis \(p = 26\).

*Indication :* `x >> k` décale \(x\) de \(k\) rangs vers la droite.

<details markdown="1">
<summary>Voir le corrigé de l'exercice 3</summary>

**1. (2 pts)**

a) *(1,5)*

| Tour | \(n\) avant | `n % 2` | `r` après | \(n\) après |
|---|---|---|---|---|
| 1 | 13 | 1 | `"1"` | 6 |
| 2 | 6 | 0 | `"01"` | 3 |
| 3 | 3 | 1 | `"101"` | 1 |
| 4 | 1 | 1 | `"1101"` | 0 |

Retour : **`"1101"`**.
b) *(0,5)* La fonction retourne l'**écriture binaire** de \(n\) sous forme de chaîne ; `mystere(0)` retourne la chaîne vide `""` (la boucle ne s'exécute pas), alors que l'on attendrait `"0"` : cas limite à traiter à part.

**2. (3 pts)**

```python
def est_ipv4(s):
    champs = s.split(".")
    if len(champs) != 4:
        return False
    for c in champs:
        if not c.isdigit():
            return False
        if int(c) > 255:
            return False
    return True
```

*Barème : découpage et test du nombre de champs (1), test des chiffres avant la conversion (1), test de la borne et retour final (1).* Résultats : `"192.168.1.10"` : `True` ; `"256.1.1.1"` : `False` (256 > 255) ; `"1.2.3"` : `False` (3 champs) ; `"1.2.3.a"` : `False` (`"a"` n'est pas un nombre). L'ordre des tests compte : appeler `int("a")` avant `isdigit` provoquerait une erreur.

**3. (3 pts)**

```python
def en_entier(s):
    v = 0
    for c in s.split("."):
        v = v * 256 + int(c)
    return v

def meme_reseau(a, b, p):
    return en_entier(a) >> (32 - p) == en_entier(b) >> (32 - p)
```

a) *(1,5)* `en_entier("192.168.1.10")` retourne \(192 \times 256^3 + 168 \times 256^2 + 1 \times 256 + 10 = \mathbf{3\,232\,235\,786}\).
b) *(1,5)* Le décalage de \(32 - p\) rangs supprime les bits de la partie machine. Pour \(p = 24\) : les deux adresses ont les mêmes 24 premiers bits (`192.168.1`) : **`True`**. Pour \(p = 26\) : le dernier octet vaut \(10 = 00001010_2\) et \(77 = 01001101_2\), leurs 2 premiers bits (`00` et `01`) diffèrent : **`False`**.

</details>

## Barème récapitulatif

| Exercice | Points |
|---|---|
| 1. Ordonnancement et graphe | 7 |
| 2. Relations et applications | 5 |
| 3. Programmation | 8 |
| **Total** | **20** |

> [!NOTE]
> **Auto-évaluation.** Sous 10 points : reprendre les séries R4 (graphes), R3 (relations) et R5 (programmation). Au-dessus de 15 : passer au [sujet suivant](sujet-3.md).

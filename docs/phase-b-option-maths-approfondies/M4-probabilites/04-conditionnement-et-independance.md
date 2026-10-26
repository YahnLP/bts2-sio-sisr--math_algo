# Cours 3 – Probabilités conditionnelles et indépendance

*BTS SIO SISR 2e année – Option mathématiques approfondies – M4, troisième partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : calculer une **probabilité conditionnelle** ; construire et lire un **arbre pondéré** ; appliquer la formule des **probabilités totales** ; **inverser** un conditionnement (formule de Bayes) ; tester l'**indépendance** de deux événements ; calculer l'espérance et la variance de \(aX + b\) et d'une somme de variables indépendantes.
>
> **Prérequis.** Le [cours 1](01-variable-aleatoire-et-loi-binomiale.md) (probabilités, variable aléatoire, espérance).

## 1. Pour démarrer : un filtre qui se trompe parfois

Un filtre anti-spam classe les messages. On sait que 30 % des messages reçus sont des spams. Le filtre détecte 95 % des spams, mais classe à tort 2 % des messages normaux comme spams. **Un message vient d'être classé spam : quelle est la probabilité que ce soit vraiment un spam ?** Beaucoup de gens répondent 95 %. Le calcul va montrer pourquoi la réponse est différente, et pourquoi il faut un outil.

## 2. Probabilité conditionnelle

La probabilité de \(B\) **sachant que** \(A\) est réalisé se note \(P_A(B)\) (ou \(P(B \mid A)\)). Pour \(P(A) > 0\) :

\[
P_A(B) = \dfrac{P(A \cap B)}{P(A)}, \qquad \text{donc} \qquad P(A \cap B) = P(A) \times P_A(B).
\]

**Lecture.** On restreint l'univers aux cas où \(A\) est réalisé, et on regarde la part de \(B\) dans ce sous-ensemble.

## 3. L'arbre pondéré

On note \(S\) : « le message est un spam » et \(D\) : « le filtre le classe spam ».

| Branche | Probabilité |
|---|---|
| \(S\) | 0,30 |
| \(\overline{S}\) | 0,70 |
| \(D\) sachant \(S\) | 0,95 |
| \(\overline{D}\) sachant \(S\) | 0,05 |
| \(D\) sachant \(\overline{S}\) | 0,02 |
| \(\overline{D}\) sachant \(\overline{S}\) | 0,98 |

**Règles de l'arbre.** (1) La somme des probabilités des branches qui partent d'un même nœud vaut 1. (2) La probabilité d'un chemin est le **produit** des probabilités de ses branches. (3) La probabilité d'un événement est la **somme** des probabilités des chemins qui y mènent.

Les quatre chemins :

| Chemin | Probabilité |
|---|---|
| \(S \cap D\) (spam détecté) | \(0{,}30 \times 0{,}95 = 0{,}285\) |
| \(S \cap \overline{D}\) (spam manqué) | \(0{,}30 \times 0{,}05 = 0{,}015\) |
| \(\overline{S} \cap D\) (fausse alerte) | \(0{,}70 \times 0{,}02 = 0{,}014\) |
| \(\overline{S} \cap \overline{D}\) (message normal laissé) | \(0{,}70 \times 0{,}98 = 0{,}686\) |

Les quatre probabilités ont pour somme \(0{,}285 + 0{,}015 + 0{,}014 + 0{,}686 = 1\). ✔

## 4. Probabilités totales

Les événements \(S\) et \(\overline{S}\) forment une **partition** (ils s'excluent et couvrent tout). Alors

\[
P(D) = P(S \cap D) + P(\overline{S} \cap D) = 0{,}285 + 0{,}014 = 0{,}299.
\]

Donc 29,9 % des messages sont classés spam par le filtre.

## 5. Inverser le conditionnement

On veut \(P_D(S)\), la probabilité qu'un message classé spam **en soit vraiment un** :

\[
P_D(S) = \dfrac{P(S \cap D)}{P(D)} = \dfrac{0{,}285}{0{,}299} \approx 0{,}953.
\]

Environ **95,3 %**. Autre question utile : un message **non** classé spam est-il sûr ? \(P_{\overline{D}}(S) = \dfrac{0{,}015}{1 - 0{,}299} = \dfrac{0{,}015}{0{,}701} \approx 0{,}0214\) : environ 2,1 % des messages laissés passer sont en fait des spams.

> [!WARNING]
> **Ne pas confondre \(P_S(D)\) et \(P_D(S)\).** Ici \(P_S(D) = 0{,}95\) (le filtre détecte 95 % des spams) alors que \(P_D(S) \approx 0{,}953\). Les deux sont proches parce que les spams sont fréquents (30 %). Si les spams étaient rares (par exemple 1 % des messages), \(P_D(S)\) tomberait à \(\dfrac{0{,}01 \times 0{,}95}{0{,}01 \times 0{,}95 + 0{,}99 \times 0{,}02} \approx 0{,}324\) : la majorité des alertes serait de fausses alertes.

## 6. Événements indépendants

\(A\) et \(B\) sont **indépendants** si savoir que \(A\) est réalisé ne change pas la probabilité de \(B\) : \(P_A(B) = P(B)\), ce qui équivaut à

\[
P(A \cap B) = P(A) \times P(B).
\]

**Exemple.** Sur 200 tickets d'incident, 80 sont critiques (\(C\)) et 100 sont résolus en moins d'une heure (\(R\)). Donc \(P(C) = 0{,}4\) et \(P(R) = 0{,}5\).

- Si 40 tickets sont à la fois critiques et résolus vite : \(P(C \cap R) = 0{,}2 = 0{,}4 \times 0{,}5\). **Indépendants** : la criticité n'influence pas le délai.
- Si 60 tickets sont à la fois critiques et résolus vite : \(P(C \cap R) = 0{,}3 \ne 0{,}2\). **Non indépendants** (les tickets critiques sont plus vite traités).

> [!WARNING]
> **Incompatibles n'est pas indépendants.** Deux événements incompatibles (\(A \cap B = \emptyset\)) de probabilités non nulles sont au contraire **très dépendants** : si \(A\) est réalisé, \(B\) est impossible.

## 7. Espérance et variance : \(aX + b\) et sommes

Pour une variable aléatoire \(X\) et des réels \(a\), \(b\) :

\[
E(aX + b) = a\,E(X) + b, \qquad V(aX + b) = a^{2}\,V(X), \qquad \sigma(aX + b) = |a|\,\sigma(X).
\]

Le décalage \(b\) change la moyenne mais **pas** la dispersion. Pour deux variables \(X\) et \(Y\) :

\[
E(X + Y) = E(X) + E(Y) \ \text{(toujours)}, \qquad V(X + Y) = V(X) + V(Y) \ \text{(si } X \text{ et } Y \text{ sont indépendantes)}.
\]

**Exemple résolu.** Le nombre \(X\) d'échecs sur 10 tentatives suit \(\mathcal{B}(10\,;\,0{,}05)\). Chaque échec coûte 5 € et il y a 20 € de frais fixes : \(C = 5X + 20\). Calculer \(E(C)\) et \(\sigma(C)\).

<details markdown="1">
<summary>Voir la solution</summary>

\(E(X) = 10 \times 0{,}05 = 0{,}5\) et \(V(X) = 10 \times 0{,}05 \times 0{,}95 = 0{,}475\). Donc \(E(C) = 5 \times 0{,}5 + 20 = 22{,}5\) € et \(V(C) = 25 \times 0{,}475 = 11{,}875\), soit \(\sigma(C) = \sqrt{11{,}875} \approx 3{,}45\) €.

Contrôle sur une somme : si \(Y \sim \mathcal{B}(20\,;\,0{,}05)\) est indépendante de \(X\), alors \(X + Y \sim \mathcal{B}(30\,;\,0{,}05)\) : \(E = 1{,}5 = 0{,}5 + 1\) et \(V = 1{,}425 = 0{,}475 + 0{,}95\). ✔

</details>

## 8. À retenir

> [!NOTE]
> - \(P_A(B) = \dfrac{P(A \cap B)}{P(A)}\) ; \(P(A \cap B) = P(A)\,P_A(B)\).
> - Arbre : produit le long d'un chemin, somme des chemins qui mènent à l'événement ; probabilités totales avec une partition.
> - Inverser un conditionnement : \(P_D(S) = \dfrac{P(S \cap D)}{P(D)}\) ; ne pas confondre \(P_S(D)\) et \(P_D(S)\).
> - Indépendants : \(P(A \cap B) = P(A)\,P(B)\). Incompatibles et indépendants ne sont pas synonymes.
> - \(E(aX+b) = aE(X) + b\) ; \(V(aX+b) = a^{2}V(X)\) ; \(V(X+Y) = V(X) + V(Y)\) si indépendantes.

## 9. Teste-toi

**Question 1.** Dans l'exemple du filtre, quelle est la probabilité qu'un message soit un spam **non détecté** ?

**Question 2.** \(P(A) = 0{,}5\), \(P(B) = 0{,}4\), \(P(A \cap B) = 0{,}2\). Les événements sont-ils indépendants ? Calculer \(P_A(B)\).

**Question 3.** \(E(X) = 10\) et \(V(X) = 4\). Calculer \(E(3X - 2)\) et \(V(3X - 2)\).

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(P(S \cap \overline{D}) = 0{,}30 \times 0{,}05 = 0{,}015\), soit 1,5 %.
2. \(P(A)\,P(B) = 0{,}2 = P(A \cap B)\) : indépendants. \(P_A(B) = \dfrac{0{,}2}{0{,}5} = 0{,}4 = P(B)\).
3. \(E = 3 \times 10 - 2 = 28\) ; \(V = 9 \times 4 = 36\).

</details>

**Pour continuer :** le [cours 4 sur la loi uniforme et l'approximation normale](05-uniforme-et-approximation-normale.md).

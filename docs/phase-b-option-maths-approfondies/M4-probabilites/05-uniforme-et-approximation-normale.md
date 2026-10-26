# Cours 4 – Loi uniforme, loi exponentielle et approximation normale

*BTS SIO SISR 2e année – Option mathématiques approfondies – M4, quatrième partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : utiliser la **loi uniforme** sur un intervalle ; situer la **loi exponentielle** parmi les lois continues ; **approcher** une loi binomiale par une loi normale, avec la **correction de continuité**, et juger si l'approximation est raisonnable.
>
> **Prérequis.** Les cours [1](01-variable-aleatoire-et-loi-binomiale.md) (loi binomiale) et [2](02-poisson-et-normale.md) (loi normale), et l'intégrale (module M2).

## 1. Pour démarrer : une valeur « au hasard » dans un intervalle

Une sauvegarde démarre à un instant **quelconque** entre 0 et 30 minutes après minuit, sans moment privilégié. Quelle est la probabilité qu'elle démarre dans les 10 premières minutes ? Intuitivement : \(\dfrac{10}{30} = \dfrac{1}{3}\). La loi uniforme formalise cette intuition.

## 2. La loi uniforme sur \([a\,;\,b]\)

Une variable \(X\) suit la **loi uniforme** sur \([a\,;\,b]\) si sa densité vaut \(\dfrac{1}{b-a}\) sur cet intervalle (et 0 ailleurs). Pour \([c\,;\,d]\) inclus dans \([a\,;\,b]\) :

\[
P(c \le X \le d) = \int_{c}^{d} \dfrac{1}{b-a}\,dx = \dfrac{d - c}{b - a}.
\]

La probabilité est **proportionnelle à la longueur**. De plus

\[
E(X) = \dfrac{a + b}{2}, \qquad V(X) = \dfrac{(b-a)^{2}}{12}.
\]

**Exemple résolu.** Pour l'heure de démarrage \(X\) de la sauvegarde, uniforme sur \([0\,;\,30]\) : calculer \(P(X \le 10)\), \(P(12 \le X \le 18)\), \(E(X)\) et \(\sigma(X)\).

<details markdown="1">
<summary>Voir la solution</summary>

\(P(X \le 10) = \dfrac{10}{30} = \dfrac{1}{3}\) ; \(P(12 \le X \le 18) = \dfrac{6}{30} = 0{,}2\) ; \(E(X) = 15\) min (le milieu) ; \(V(X) = \dfrac{900}{12} = 75\), donc \(\sigma(X) = \sqrt{75} \approx 8{,}66\) min.

</details>

> [!TIP]
> **Pour une loi continue, \(P(X = c) = 0\).** Les inégalités larges ou strictes donnent donc la même probabilité : \(P(X \le 10) = P(X < 10)\). Ce n'est **pas** vrai pour une loi discrète (binomiale, Poisson).

## 3. La loi exponentielle

La durée de vie d'un composant sans usure, ou l'attente entre deux événements rares, se modélise par la **loi exponentielle** de paramètre \(\lambda > 0\) :

\[
P(X \le t) = 1 - e^{-\lambda t}, \qquad P(X > t) = e^{-\lambda t}, \qquad E(X) = \dfrac{1}{\lambda}, \qquad V(X) = \dfrac{1}{\lambda^{2}}.
\]

Elle est étudiée en détail, avec ses applications à la fiabilité, dans le [module M5](../M5-fiabilite/01-fiabilite-et-loi-exponentielle.md).

## 4. Approcher une loi binomiale par une loi normale

Pour \(n\) grand, les calculs binomiaux sont lourds sans machine, et la forme du diagramme de \(\mathcal{B}(n\,;\,p)\) ressemble à une **cloche**. On l'approche par la loi normale de **même espérance** et de **même écart type** :

\[
X \sim \mathcal{B}(n\,;\,p) \quad \text{est approchée par} \quad Y \sim \mathcal{N}\big(np\,;\,\sqrt{np(1-p)}\big).
\]

**Conditions usuelles.** \(n \ge 30\), \(np \ge 5\) et \(n(1-p) \ge 5\). L'énoncé les rappelle en général.

**La correction de continuité.** \(X\) ne prend que des valeurs entières ; \(Y\) prend toutes les valeurs. On associe à l'entier \(k\) l'intervalle \([k - 0{,}5\,;\,k + 0{,}5]\) :

| Pour \(X\) (discrète) | On calcule avec \(Y\) (continue) |
|---|---|
| \(P(X \le k)\) | \(P(Y \le k + 0{,}5)\) |
| \(P(X \ge k)\) | \(P(Y \ge k - 0{,}5)\) |
| \(P(X = k)\) | \(P(k - 0{,}5 \le Y \le k + 0{,}5)\) |

**Exemple résolu.** Sur 100 postes, chacun a la probabilité 0,4 d'avoir une mise à jour en attente, indépendamment des autres. \(X\) est le nombre de postes concernés. Approcher \(P(X \le 45)\) et \(P(X = 40)\).

<details markdown="1">
<summary>Voir la solution</summary>

\(X \sim \mathcal{B}(100\,;\,0{,}4)\) ; conditions : \(n = 100 \ge 30\), \(np = 40 \ge 5\), \(n(1-p) = 60 \ge 5\). On prend \(Y \sim \mathcal{N}(40\,;\,\sqrt{24})\), avec \(\sqrt{24} \approx 4{,}899\).

- \(P(X \le 45) \approx P(Y \le 45{,}5) \approx 0{,}8692\). La valeur binomiale exacte est \(0{,}8689\) : l'écart est de \(0{,}0003\). Sans la correction, \(P(Y \le 45) \approx 0{,}8463\), nettement moins bon.
- \(P(X = 40) \approx P(39{,}5 \le Y \le 40{,}5) \approx 0{,}0813\). Valeur exacte : \(0{,}0812\).

</details>

```python
from scipy.stats import binom, norm
from math import sqrt
n, p = 100, 0.4
print(binom.cdf(45, n, p))                         # 0.8689 (exact)
print(norm.cdf(45.5, n * p, sqrt(n * p * (1 - p))))  # 0.8692 (approché)
```

(Sans `scipy`, la calculatrice donne les mêmes valeurs : voir l'[aide-mémoire calculatrice](../aide-memoire-calculatrice.md).)

> [!NOTE]
> **Pourquoi apprendre l'approximation si la calculatrice donne la valeur exacte ?** Parce qu'elle explique **pourquoi** tant de phénomènes de comptage ont une forme de cloche, et qu'elle donne un ordre de grandeur rapide : environ 95 % des valeurs de \(X\) sont entre \(np - 2\sigma\) et \(np + 2\sigma\), ici entre 30 et 50.

## 5. À retenir

> [!NOTE]
> - Loi uniforme sur \([a\,;\,b]\) : \(P(c \le X \le d) = \dfrac{d-c}{b-a}\) ; \(E = \dfrac{a+b}{2}\) ; \(V = \dfrac{(b-a)^{2}}{12}\).
> - Loi exponentielle : \(P(X > t) = e^{-\lambda t}\), \(E = \dfrac{1}{\lambda}\), \(V = \dfrac{1}{\lambda^{2}}\) (voir M5).
> - \(\mathcal{B}(n\,;\,p)\) est approchée par \(\mathcal{N}\big(np\,;\,\sqrt{np(1-p)}\big)\) si \(n \ge 30\), \(np \ge 5\), \(n(1-p) \ge 5\), avec la **correction de continuité** (\(\pm 0{,}5\)).

## 6. Teste-toi

**Question 1.** \(X\) suit la loi uniforme sur \([2\,;\,10]\). Calculer \(P(X \ge 8)\) et \(E(X)\).

**Question 2.** Peut-on approcher \(\mathcal{B}(40\,;\,0{,}05)\) par une loi normale ?

**Question 3.** Par quelle probabilité normale approche-t-on \(P(X \ge 50)\) pour \(X \sim \mathcal{B}(200\,;\,0{,}2)\) ?

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(P(X \ge 8) = \dfrac{10 - 8}{10 - 2} = 0{,}25\) ; \(E(X) = 6\).
2. Non : \(np = 2 < 5\). On utiliserait plutôt une loi de Poisson de paramètre 2 (cours 2).
3. \(np = 40\), \(\sigma = \sqrt{32} \approx 5{,}657\) : \(P(X \ge 50) \approx P(Y \ge 49{,}5)\) avec \(Y \sim \mathcal{N}(40\,;\,5{,}657)\), soit environ \(0{,}0465\).

</details>

**Pour continuer :** les [exercices du module](03-exercices.md).

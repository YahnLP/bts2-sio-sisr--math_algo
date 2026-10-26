# Cours 3 – Racine carrée et résolution approchée d'une équation

*BTS SIO SISR 2e année – Option mathématiques approfondies – M1, troisième partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : utiliser la fonction racine carrée et résoudre une équation avec une racine ; compter le **nombre de solutions** de \(f(x) = k\) à partir d'un tableau de variations ; **encadrer** une solution par un balayage, puis par la **dichotomie** ; programmer ces deux méthodes en Python.
>
> **Prérequis.** Les cours [1](01-fonctions-et-modeles.md) et [2](02-exponentielle-et-logarithme.md). Le cours 1 du module M2 (variations) complète celui-ci, mais n'est pas nécessaire pour le lire.

## 1. Pour démarrer : une équation qu'on ne sait pas résoudre

Un serveur reçoit des requêtes. On modélise la charge (en unités de 10 %) à l'instant \(x\) (en heures, de 0 à 10) par

\[
f(x) = x\,e^{-0{,}5x}.
\]

On veut savoir **quand** la charge vaut 0,5. Il faut résoudre \(f(x) = 0{,}5\), c'est-à-dire \(x\,e^{-0{,}5x} = 0{,}5\). Aucune des méthodes du cours 2 ne marche : \(x\) est à la fois en facteur et dans l'exposant. Pourtant, des solutions existent. Ce cours apprend à **les trouver avec la précision voulue**, sans formule.

## 2. La fonction racine carrée

Pour \(x \ge 0\), \(\sqrt{x}\) est le nombre positif dont le carré vaut \(x\). Elle n'existe **que pour \(x \ge 0\)**, elle est **croissante**, et

\[
\sqrt{ab} = \sqrt{a}\,\sqrt{b}, \qquad \sqrt{x^{2}} = |x|, \qquad \sqrt{a + b} \ne \sqrt{a} + \sqrt{b}.
\]

(Par exemple \(\sqrt{9 + 16} = 5\), alors que \(\sqrt{9} + \sqrt{16} = 7\).) L'écart type d'une série est une racine carrée : c'est la racine de la variance.

**Résoudre une équation avec une racine.** On **élève au carré**, puis on **vérifie** : cette opération peut introduire de fausses solutions.

**Exemple résolu.** Résoudre \(\sqrt{2x + 1} = 5\), puis \(\sqrt{2x + 1} = -5\).

<details markdown="1">
<summary>Voir la solution</summary>

Première équation : on élève au carré, \(2x + 1 = 25\), donc \(x = 12\). Contrôle : \(\sqrt{2 \times 12 + 1} = \sqrt{25} = 5\). Elle a une solution : 12.

Seconde équation : une racine carrée est **toujours positive ou nulle**, donc elle ne peut pas valoir \(-5\). Il n'y a **aucune solution**. En élevant au carré on aurait retrouvé \(x = 12\), qui ne convient pas : c'est une fausse solution.

</details>

## 3. Combien de solutions ? Lire un tableau de variations

Reprenons \(f(x) = x\,e^{-0{,}5x}\) sur \([0\,;\,10]\). Un tableau de valeurs (pas de 1) montre l'allure :

| \(x\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| \(f(x)\) | 0 | 0,607 | 0,736 | 0,669 | 0,541 | 0,410 | 0,299 | 0,147 | 0,067 |

La fonction **croît** de 0 jusqu'à \(x = 2\) (où elle atteint son maximum \(2/e \approx 0{,}736\)), puis **décroît**. (Le module M2 explique comment le démontrer avec la dérivée.)

**Règle.** Si \(f\) est **continue** et **strictement monotone** sur un intervalle \([a\,;\,b]\), alors, pour tout \(k\) compris entre \(f(a)\) et \(f(b)\), l'équation \(f(x) = k\) a **exactement une solution** dans \([a\,;\,b]\).

Pour \(k = 0{,}5\) :

- sur \([0\,;\,2]\), \(f\) croît de 0 à 0,736 : comme \(0 < 0{,}5 < 0{,}736\), il y a **une** solution ;
- sur \([2\,;\,10]\), \(f\) décroît de 0,736 à 0,067 : comme \(0{,}067 < 0{,}5 < 0{,}736\), il y a **une** solution ;
- au total, **deux** solutions.

Pour \(k = 0{,}9\) (au-dessus du maximum) : aucune solution. Pour \(k = 2/e\) : une seule, \(x = 2\).

> [!WARNING]
> **Ne pas oublier un intervalle.** Quand la fonction n'est pas monotone sur tout le domaine, on découpe en intervalles où elle l'est, et on cherche **dans chacun**. Oublier l'un d'eux fait rater une solution.

## 4. Premier encadrement : le balayage

On calcule \(f\) pour des valeurs de \(x\) régulièrement espacées et on repère où \(f(x)\) **passe de part et d'autre** de \(k\).

- Entre \(x = 0\) (\(f = 0\)) et \(x = 1\) (\(f = 0{,}607\)), on passe de moins de 0,5 à plus de 0,5 : une solution dans \([0\,;\,1]\).
- Entre \(x = 4\) (\(f = 0{,}541\)) et \(x = 5\) (\(f = 0{,}410\)), on repasse sous 0,5 : une solution dans \([4\,;\,5]\).

On a un encadrement de **largeur 1**. Pour gagner en précision, on refait un balayage avec un pas de 0,1 dans l'intervalle trouvé (largeur 0,1), puis 0,01 (largeur 0,01) : à chaque fois on gagne **un chiffre**. C'est simple, mais long.

## 5. La dichotomie : couper en deux

**Idée.** On connaît un intervalle \([a\,;\,b]\) qui contient la solution (donc \(g(a)\) et \(g(b)\) de signes contraires, où \(g(x) = f(x) - k\)). On regarde le **milieu** \(m\) : la solution est dans la moitié où le signe change. On garde cette moitié et on recommence. **À chaque étape, la largeur est divisée par 2.**

**Exemple résolu.** Encadrer, avec une amplitude inférieure à 0,01, la solution de \(f(x) = 0{,}5\) dans \([0\,;\,2]\).

<details markdown="1">
<summary>Voir la solution</summary>

On pose \(g(x) = x\,e^{-0{,}5x} - 0{,}5\) : \(g(0) = -0{,}5 < 0\) et \(g(2) \approx 0{,}236 > 0\).

| Étape | Intervalle | Milieu | Signe de \(g(m)\) | Nouvel intervalle |
|---|---|---|---|---|
| 1 | \([0\,;\,2]\) | 1 | \(+\) | \([0\,;\,1]\) |
| 2 | \([0\,;\,1]\) | 0,5 | \(-\) | \([0{,}5\,;\,1]\) |
| 3 | \([0{,}5\,;\,1]\) | 0,75 | \(+\) | \([0{,}5\,;\,0{,}75]\) |
| 4 | \([0{,}5\,;\,0{,}75]\) | 0,625 | \(-\) | \([0{,}625\,;\,0{,}75]\) |
| 5 | \([0{,}625\,;\,0{,}75]\) | 0,6875 | \(-\) | \([0{,}6875\,;\,0{,}75]\) |
| 6 | \([0{,}6875\,;\,0{,}75]\) | 0,71875 | \(+\) | \([0{,}6875\,;\,0{,}71875]\) |
| 7 | \([0{,}6875\,;\,0{,}71875]\) | 0,703125 | \(-\) | \([0{,}703125\,;\,0{,}71875]\) |
| 8 | \([0{,}703125\,;\,0{,}71875]\) | 0,7109375 | \(-\) | \([0{,}7109\,;\,0{,}7188]\) |

Après 8 étapes, la largeur est \(2/2^{8} = 0{,}0078 < 0{,}01\). La solution est entre 0,7109 et 0,7188 : \(x \approx 0{,}71\) heure, soit environ 43 minutes.

</details>

**Combien d'étapes ?** Après \(n\) étapes, la largeur vaut \(\dfrac{b - a}{2^{n}}\). On veut qu'elle soit inférieure à une précision \(\varepsilon\) : \(2^{n} > \dfrac{b-a}{\varepsilon}\), soit \(n > \dfrac{\ln\big((b-a)/\varepsilon\big)}{\ln 2}\). Pour passer de largeur 2 à moins de 0,01 : \(2^{n} > 200\), donc \(n \ge 8\). Chaque étape gagne un peu **moins d'un chiffre décimal** (\(\log_{10} 2 \approx 0{,}3\)) : environ 3 étapes pour 1 chiffre.

## 6. L'algorithme en Python

```python
from math import exp

def dichotomie(g, a, b, eps):
    """Encadre une solution de g(x) = 0 dans [a ; b].
    Hypothèse : g(a) et g(b) sont de signes contraires."""
    while b - a > eps:
        m = (a + b) / 2
        if g(a) * g(m) <= 0:      # le signe change dans [a ; m]
            b = m
        else:                     # sinon il change dans [m ; b]
            a = m
    return a, b

g = lambda x: x * exp(-0.5 * x) - 0.5
print(dichotomie(g, 0, 2, 0.01))      # (0.7109375, 0.71875)
print(dichotomie(g, 2, 10, 0.01))     # (4.3046875, 4.3125)
```

La seconde solution est donc \(x \approx 4{,}31\) heures : la charge repasse sous 0,5 au bout de 4 h 18 environ. L'algorithme **s'arrête toujours** (la largeur diminue de moitié à chaque tour) ; la seule hypothèse à vérifier est le **changement de signe** au départ.

> [!TIP]
> **Calculatrice.** Les modèles proposent un « solveur » ou une résolution numérique d'équation, et l'intersection de deux courbes dans le menu graphique. Ils appliquent une méthode de ce type. Pour une épreuve, on **indique la méthode**, on donne l'encadrement et on **interprète** (unité comprise).

## 7. À retenir

> [!NOTE]
> - \(\sqrt{x}\) existe pour \(x \ge 0\) ; \(\sqrt{a+b} \ne \sqrt{a} + \sqrt{b}\) ; après avoir élevé au carré, on **vérifie** les solutions.
> - Si \(f\) est continue et strictement monotone sur \([a\,;\,b]\), \(f(x) = k\) a **une seule** solution quand \(k\) est entre \(f(a)\) et \(f(b)\) ; sinon, aucune.
> - Fonction non monotone : on découpe en intervalles et on cherche dans chacun.
> - Balayage : un chiffre de plus par balayage plus fin. Dichotomie : largeur divisée par 2 à chaque étape, signe de \(g(a)\,g(m)\) pour choisir la moitié.
> - Toujours terminer par une **phrase** avec unité.

## 8. Teste-toi

**Question 1.** Résoudre \(\sqrt{x - 1} = 4\).

**Question 2.** La fonction \(h\) est croissante sur \([0\,;\,5]\) avec \(h(0) = 2\) et \(h(5) = 9\). Combien de solutions a \(h(x) = 12\) ? Et \(h(x) = 5\) ?

**Question 3.** On encadre une solution dans un intervalle de largeur 1. Combien d'étapes de dichotomie pour une largeur inférieure à 0,001 ?

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(x - 1 = 16\), donc \(x = 17\). Contrôle : \(\sqrt{16} = 4\). ✔
2. \(12 > h(5) = 9\) : aucune solution. \(2 < 5 < 9\) : exactement une.
3. \(2^{n} > 1000\) donne \(n \ge 10\) (car \(2^{10} = 1024\)).

</details>

**Pour continuer :** les [exercices du module](03-exercices.md), puis le [module M2 sur la dérivée](../M2-derivees-integrales/01-derivee-et-variations.md), qui explique comment démontrer les variations.

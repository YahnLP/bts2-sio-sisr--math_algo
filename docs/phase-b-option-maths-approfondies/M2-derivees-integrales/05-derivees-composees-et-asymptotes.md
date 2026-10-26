# Cours 4 – Dérivées de fonctions composées et asymptotes

*BTS SIO SISR 2e année – Option mathématiques approfondies – M2, quatrième partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : dériver \(u^{n}\), \(\ln u\), \(e^{u}\) et \(\sqrt{u}\) ; repérer une **asymptote verticale** et une **asymptote oblique** et les justifier par une limite ; mener l'étude complète d'une fonction (limites, dérivée, variations, asymptotes).
>
> **Prérequis.** Les cours [1](01-derivee-et-variations.md) (dérivée, variations) et [2](02-limites-et-asymptotes.md) (limites, asymptote horizontale).

## 1. Pour démarrer : une dérivée qui ne rentre pas dans le tableau

On modélise l'intensité d'un signal par \(f(x) = (2x + 1)^{3}\). On pourrait développer, mais pour \(\left(2x+1\right)^{20}\) ce serait absurde. Il faut une règle pour dériver une **fonction à l'intérieur d'une autre** (une **composée**) : ici, la puissance 3 s'applique à \(u(x) = 2x + 1\).

## 2. Les quatre règles à connaître

Pour une fonction \(u\) dérivable, de dérivée \(u'\) :

| Fonction | Dérivée | Condition |
|---|---|---|
| \(u^{n}\) | \(n\,u'\,u^{n-1}\) | \(n\) entier |
| \(\ln u\) | \(\dfrac{u'}{u}\) | \(u > 0\) |
| \(e^{u}\) | \(u'\,e^{u}\) | |
| \(\sqrt{u}\) | \(\dfrac{u'}{2\sqrt{u}}\) | \(u > 0\) |

**Le réflexe.** Dans les quatre cas, on dérive « comme d'habitude » et on **multiplie par la dérivée de l'intérieur** (\(u'\)). Oublier ce facteur \(u'\) est l'erreur la plus fréquente.

**Exemples résolus.** Dériver \(f(x) = (2x+1)^{3}\), \(g(x) = \ln(x^{2} + 1)\), \(h(x) = e^{x^{2}}\) et \(k(x) = \sqrt{3x + 4}\).

<details markdown="1">
<summary>Voir les solutions</summary>

- \(f\) : \(u = 2x + 1\), \(u' = 2\), \(n = 3\). Donc \(f'(x) = 3 \times 2 \times (2x+1)^{2} = 6(2x+1)^{2}\).
- \(g\) : \(u = x^{2} + 1\) (toujours \(> 0\)), \(u' = 2x\). Donc \(g'(x) = \dfrac{2x}{x^{2} + 1}\).
- \(h\) : \(u = x^{2}\), \(u' = 2x\). Donc \(h'(x) = 2x\,e^{x^{2}}\).
- \(k\) : \(u = 3x + 4\), \(u' = 3\). Donc \(k'(x) = \dfrac{3}{2\sqrt{3x + 4}}\) (pour \(x > -\dfrac{4}{3}\)).

**Contrôle numérique.** Pour \(g\), en \(x = 1\) : \(g'(1) = \dfrac{2}{2} = 1\). Le taux d'accroissement entre 1 et 1,001 vaut \(\dfrac{\ln(2{,}002001) - \ln 2}{0{,}001} \approx 1{,}0000\ \) (à \(10^{-3}\) près) : cohérent.

</details>

> [!WARNING]
> **Piège.** \((e^{2x})'\) n'est pas \(e^{2x}\) : c'est \(2\,e^{2x}\). Et \((\ln(5x))' = \dfrac{5}{5x} = \dfrac{1}{x}\) : le 5 se simplifie.

## 3. Asymptote verticale

**Définition.** Si \(f(x)\) tend vers \(+\infty\) ou \(-\infty\) quand \(x\) tend vers un réel \(a\), la droite \(x = a\) est une **asymptote verticale** : la courbe « colle » à cette droite sans jamais la traverser.

On la rencontre aux **valeurs interdites** : en \(0\) pour \(\dfrac{1}{x}\) (quand \(x \to 0^{+}\), \(\dfrac{1}{x} \to +\infty\)), et pour \(\ln x\) (quand \(x \to 0^{+}\), \(\ln x \to -\infty\)). Le symbole \(0^{+}\) signifie qu'on s'approche de 0 **par valeurs positives**.

## 4. Asymptote oblique

**Définition.** Si \(f(x) - (ax + b)\) tend vers 0 quand \(x \to +\infty\), la droite \(y = ax + b\) est une **asymptote oblique** : à l'infini, la courbe se confond avec cette droite.

**Méthode.** On calcule la différence \(f(x) - (ax + b)\) et on montre qu'elle tend vers 0.

## 5. Une étude complète

Un traitement par lots coûte, pour un lot de \(x\) milliers de requêtes, un coût moyen (en euros)

\[
C(x) = x + \dfrac{4}{x}, \qquad x > 0.
\]

(\(x\) : frais de gestion qui croissent avec la taille du lot ; \(\dfrac{4}{x}\) : frais fixes répartis sur le lot.)

<details markdown="1">
<summary>1. Limites et asymptotes</summary>

Quand \(x \to 0^{+}\), \(\dfrac{4}{x} \to +\infty\) donc \(C(x) \to +\infty\) : la droite \(x = 0\) est **asymptote verticale**.

Quand \(x \to +\infty\), \(C(x) - x = \dfrac{4}{x} \to 0\) : la droite \(y = x\) est **asymptote oblique**. La courbe est toujours au-dessus (car \(\dfrac{4}{x} > 0\)).

</details>

<details markdown="1">
<summary>2. Dérivée et variations</summary>

\(C'(x) = 1 - \dfrac{4}{x^{2}} = \dfrac{x^{2} - 4}{x^{2}}\). Pour \(x > 0\) : \(C'(x) = 0\) en \(x = 2\), négatif avant, positif après.

| \(x\) | 0 | | 2 | | \(+\infty\) |
|---|---|---|---|---|---|
| \(C'(x)\) | | \(-\) | 0 | \(+\) | |
| \(C(x)\) | \(+\infty\) | décroît | **4** | croît | \(+\infty\) |

</details>

<details markdown="1">
<summary>3. Valeurs et interprétation</summary>

| \(x\) | 0,1 | 0,5 | 1 | 2 | 4 | 10 | 100 |
|---|---|---|---|---|---|---|---|
| \(C(x)\) | 40,1 | 8,5 | 5 | 4 | 5 | 10,4 | 100,04 |

Le coût moyen est **minimal pour un lot de 2 000 requêtes** : 4 € par millier. Trop petit, les frais fixes dominent ; trop grand, la gestion coûte trop. À \(x = 100\), \(C\) vaut 100,04 : on est quasi sur l'asymptote \(y = x\) (écart \(0{,}04\)).

</details>

## 6. À retenir

> [!NOTE]
> - \((u^{n})' = n\,u'\,u^{n-1}\) ; \((\ln u)' = \dfrac{u'}{u}\) ; \((e^{u})' = u'\,e^{u}\) ; \((\sqrt{u})' = \dfrac{u'}{2\sqrt{u}}\). On n'oublie jamais \(u'\).
> - Asymptote **verticale** \(x = a\) : \(f(x) \to \pm\infty\) quand \(x \to a\). Asymptote **oblique** \(y = ax + b\) : \(f(x) - (ax + b) \to 0\).
> - Étude complète : domaine, limites aux bornes, dérivée, signe, tableau de variations, asymptotes, interprétation.

## 7. Teste-toi

**Question 1.** Dériver \(f(x) = (x^{2} + 1)^{4}\) et \(g(x) = e^{-3x}\).

**Question 2.** Dériver \(h(x) = \ln(2x + 5)\) pour \(x > -2{,}5\).

**Question 3.** Quelle asymptote a \(f(x) = 2x + 1 + \dfrac{3}{x}\) quand \(x \to +\infty\) ? Quand \(x \to 0^{+}\) ?

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(f'(x) = 4 \times 2x\,(x^{2}+1)^{3} = 8x(x^{2}+1)^{3}\) ; \(g'(x) = -3\,e^{-3x}\).
2. \(h'(x) = \dfrac{2}{2x + 5}\).
3. \(f(x) - (2x + 1) = \dfrac{3}{x} \to 0\) : asymptote oblique \(y = 2x + 1\). Quand \(x \to 0^{+}\), \(\dfrac{3}{x} \to +\infty\) : asymptote verticale \(x = 0\).

</details>

**Pour continuer :** le [cours 5 sur les primitives, les aires et les méthodes numériques](06-primitives-aires-methodes-numeriques.md).

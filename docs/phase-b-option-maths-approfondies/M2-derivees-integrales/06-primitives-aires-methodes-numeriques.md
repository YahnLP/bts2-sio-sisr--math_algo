# Cours 5 – Primitives, aires et méthodes numériques

*BTS SIO SISR 2e année – Option mathématiques approfondies – M2, cinquième partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : **trouver** une primitive de la forme \(u'u^{n}\), \(\dfrac{u'}{u}\) ou \(u'e^{u}\) en reconnaissant la dérivée d'une composée ; calculer l'**aire entre deux courbes** ; **approcher** une intégrale par les méthodes des rectangles, du point milieu et des trapèzes, et par une simulation (Monte-Carlo).
>
> **Prérequis.** Les cours [3](03-primitives-et-integrales.md) (primitives, intégrale) et [4](05-derivees-composees-et-asymptotes.md) (dérivées de composées).

## 1. Pour démarrer : retrouver la fonction de départ

Le cours 4 a appris à dériver \((u^{n})'\), \((\ln u)'\), \((e^{u})'\). Lues **à l'envers**, ces règles donnent des primitives. Exemple : on sait que \((e^{x^{2}})' = 2x\,e^{x^{2}}\). Donc une primitive de \(2x\,e^{x^{2}}\) est \(e^{x^{2}}\).

## 2. Les trois formes à reconnaître

| La fonction a la forme | Une primitive est | Condition |
|---|---|---|
| \(u'\,u^{n}\) | \(\dfrac{u^{n+1}}{n+1}\) | \(n \ne -1\) |
| \(\dfrac{u'}{u}\) | \(\ln u\) | \(u > 0\) |
| \(u'\,e^{u}\) | \(e^{u}\) | |

**Méthode.** (1) Repérer l'intérieur \(u\). (2) Calculer \(u'\). (3) Voir s'il apparaît dans la fonction, **à une constante près** (on la corrige en multipliant par son inverse). (4) **Contrôler en dérivant.**

**Exemples résolus.**

1. Primitive de \(f(x) = x\,e^{x^{2}}\).
2. Calculer \(\displaystyle\int_{0}^{1} \dfrac{2x}{x^{2}+1}\,dx\).
3. Calculer \(\displaystyle\int_{0}^{1} 2x\,(x^{2}+1)^{2}\,dx\).

<details markdown="1">
<summary>Voir les solutions</summary>

1. \(u = x^{2}\), \(u' = 2x\). Il manque un facteur 2 : \(x\,e^{x^{2}} = \dfrac{1}{2}\,u'\,e^{u}\). Primitive : \(F(x) = \dfrac{1}{2}\,e^{x^{2}}\). Contrôle : \(F'(x) = \dfrac{1}{2} \times 2x\,e^{x^{2}} = x\,e^{x^{2}}\). ✔
2. \(u = x^{2} + 1 > 0\), \(u' = 2x\) : c'est \(\dfrac{u'}{u}\). Intégrale : \(\big[\ln(x^{2}+1)\big]_{0}^{1} = \ln 2 - \ln 1 = \ln 2 \approx 0{,}693\).
3. \(u = x^{2} + 1\), \(u' = 2x\), \(n = 2\) : primitive \(\dfrac{(x^{2}+1)^{3}}{3}\). Intégrale : \(\dfrac{2^{3}}{3} - \dfrac{1}{3} = \dfrac{7}{3} \approx 2{,}333\).

</details>

> [!WARNING]
> **Limite du programme.** On ne cherche pas de primitive par intégration par parties, ni pour les fonctions \(\cos(\omega t + \varphi)\) et \(\sin(\omega t + \varphi)\) : ces points sont exclus du programme de l'unité. Quand aucune forme ne se reconnaît, l'énoncé **donne** la primitive, ou on utilise la calculatrice formelle ou une méthode numérique (section 4).

## 3. Aire entre deux courbes

Si \(f \ge g\) sur \([a\,;\,b]\), l'aire entre les deux courbes vaut

\[
\int_{a}^{b} \big(f(x) - g(x)\big)\,dx.
\]

**Exemple résolu.** Le débit entrant d'un lien vaut \(a(t) = t + 2\) et le débit sortant \(b(t) = t^{2}\) (en Go par heure), pour \(t\) entre 0 et 2. Quelle quantité s'accumule entre 0 et 2 heures ?

<details markdown="1">
<summary>Voir la solution</summary>

On vérifie d'abord que \(a \ge b\) sur \([0\,;\,2]\) : \(t + 2 - t^{2} = (2 - t)(t + 1) \ge 0\). On intègre la différence :

\[
\int_{0}^{2} (t + 2 - t^{2})\,dt = \left[\dfrac{t^{2}}{2} + 2t - \dfrac{t^{3}}{3}\right]_{0}^{2} = 2 + 4 - \dfrac{8}{3} = \dfrac{10}{3} \approx 3{,}33.
\]

Il s'accumule environ **3,33 Go** dans la file entre 0 et 2 heures.

</details>

## 4. Approcher une intégrale

Certaines fonctions, comme \(e^{-x^{2}}\), n'ont **aucune primitive** qu'on sache écrire avec les fonctions usuelles. On approche alors l'intégrale. On découpe \([a\,;\,b]\) en \(n\) parts de largeur \(h = \dfrac{b-a}{n}\) et on pose \(x_i = a + ih\).

| Méthode | Formule | Idée |
|---|---|---|
| Rectangles (à gauche) | \(h\,\big(f(x_0) + \dots + f(x_{n-1})\big)\) | rectangle dont la hauteur est la valeur à gauche |
| Point milieu | \(h\,\big(f(m_0) + \dots + f(m_{n-1})\big)\), \(m_i\) milieu de \([x_i ; x_{i+1}]\) | hauteur au milieu |
| Trapèzes | \(h\left(\dfrac{f(x_0)}{2} + f(x_1) + \dots + f(x_{n-1}) + \dfrac{f(x_n)}{2}\right)\) | on joint les points par des segments |

**Exemple.** Approcher \(I = \displaystyle\int_{0}^{1} e^{-x^{2}}\,dx\) avec \(n = 4\) (donc \(h = 0{,}25\)) :

| Méthode | Résultat |
|---|---|
| Trapèzes | 0,7430 |
| Point milieu | 0,7487 |

Avec \(n = 100\), les deux méthodes donnent 0,7468 (trapèzes 0,74682, milieu 0,74683). La valeur de référence est \(I \approx 0{,}7468\). Diviser la largeur par 25 a fait gagner environ **2 chiffres** : on dit que ces méthodes convergent quand \(n\) augmente.

```python
from math import exp

def trapezes(f, a, b, n):
    h = (b - a) / n
    s = (f(a) + f(b)) / 2 + sum(f(a + i * h) for i in range(1, n))
    return h * s

def milieu(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + (i + 0.5) * h) for i in range(n))

f = lambda x: exp(-x * x)
print(trapezes(f, 0, 1, 4))     # 0.7429840978003812
print(milieu(f, 0, 1, 4))       # 0.7487471318910093
```

**Méthode de Monte-Carlo.** Comme \(f\) est comprise entre 0 et 1 sur \([0\,;\,1]\), on tire au hasard \(N\) nombres \(x\) dans \([0\,;\,1]\) et on calcule la **moyenne** des \(f(x)\) : c'est une estimation de la valeur moyenne, donc de l'intégrale (la largeur vaut 1).

```python
import random
random.seed(0)
N = 1000
print(sum(f(random.random()) for _ in range(N)) / N)   # 0.7485 avec cette graine
```

Le résultat **change** d'une exécution à l'autre (sans la graine) et converge lentement : il faut environ 100 fois plus de tirages pour gagner 1 chiffre. En contrepartie, la méthode se généralise facilement à des problèmes compliqués.

## 5. À retenir

> [!NOTE]
> - Primitives à reconnaître : \(u'u^{n} \to \dfrac{u^{n+1}}{n+1}\) ; \(\dfrac{u'}{u} \to \ln u\) ; \(u'e^{u} \to e^{u}\). On corrige une constante manquante et on **contrôle en dérivant**.
> - Hors programme : intégration par parties ; primitives de \(\cos(\omega t + \varphi)\) et \(\sin(\omega t + \varphi)\).
> - Aire entre deux courbes : \(\displaystyle\int_{a}^{b} (f - g)\) avec \(f \ge g\).
> - Intégrale approchée : rectangles, point milieu, trapèzes (plus \(n\) est grand, plus c'est précis) ; Monte-Carlo : moyenne de valeurs tirées au hasard.

## 6. Teste-toi

**Question 1.** Une primitive de \(3x^{2}\,e^{x^{3}}\) ?

**Question 2.** Calculer \(\displaystyle\int_{0}^{1} \dfrac{3x^{2}}{x^{3} + 1}\,dx\).

**Question 3.** Quelle méthode utiliser pour \(\displaystyle\int_{0}^{1} e^{-x^{2}}\,dx\), et pourquoi ?

<details markdown="1">
<summary>Voir les réponses</summary>

1. \(u = x^{3}\), \(u' = 3x^{2}\) : primitive \(e^{x^{3}}\).
2. \(u = x^{3} + 1\), \(u' = 3x^{2}\) : \(\big[\ln(x^{3} + 1)\big]_{0}^{1} = \ln 2 \approx 0{,}693\).
3. Une méthode numérique (trapèzes, point milieu ou Monte-Carlo), car la fonction n'a pas de primitive écrite avec les fonctions usuelles.

</details>

**Pour continuer :** les [exercices du module](04-exercices.md).

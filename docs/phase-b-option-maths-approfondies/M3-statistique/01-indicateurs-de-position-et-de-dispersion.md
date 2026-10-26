# Cours 1 – Résumer une série : position et dispersion

*BTS SIO SISR 2e année – Option mathématiques approfondies – M3, première partie*

> [!NOTE]
> **Objectifs de ce cours.** À la fin, tu sais : calculer et interpréter la **moyenne**, la **médiane**, les **quartiles**, l'**étendue**, la **variance** et l'**écart type** ; traiter une série **groupée en classes** ; choisir un indicateur adapté et **repérer une valeur aberrante**.
>
> **Prérequis.** Calculs de moyennes, racines carrées ; le [cours 1 de M1](../M1-fonctions/01-fonctions-et-modeles.md) pour les notations.

## 1. Pour démarrer : douze mesures, comment les résumer ?

On relève, en millisecondes, le temps de réponse d'un service sur douze requêtes :

\[
12,\ 15,\ 15,\ 16,\ 18,\ 20,\ 21,\ 21,\ 22,\ 25,\ 27,\ 40.
\]

Douze nombres sont difficiles à comparer à ceux d'un autre jour. On veut **résumer** la série par quelques nombres qui répondent à deux questions :

- **Autour de quelle valeur** les temps se situent-ils ? (position)
- **À quel point** s'écartent-ils les uns des autres ? (dispersion)

Les deux sont indispensables : deux services peuvent avoir le même temps moyen, mais l'un très régulier et l'autre très irrégulier.

## 2. La position : autour de quelle valeur ?

### La moyenne

\[
\bar{x} = \dfrac{x_1 + x_2 + \dots + x_n}{n}.
\]

Ici, la somme vaut 252 et \(n = 12\) : \(\bar{x} = \dfrac{252}{12} = 21\) ms. La moyenne est le « centre de gravité » de la série.

### La médiane

La **médiane** partage la série **ordonnée** en deux moitiés de même effectif : au moins la moitié des valeurs lui sont inférieures ou égales, et au moins la moitié lui sont supérieures ou égales.

- Si \(n\) est **impair**, c'est la valeur du milieu.
- Si \(n\) est **pair**, c'est la **moyenne des deux valeurs centrales**.

Ici \(n = 12\) : les valeurs centrales sont les 6e et 7e (20 et 21) et la médiane est \(\dfrac{20 + 21}{2} = 20{,}5\) ms.

### Les quartiles

Les quartiles \(Q_1\) et \(Q_3\) découpent la série en quatre groupes de même effectif.

> [!WARNING]
> **Plusieurs conventions existent** pour calculer les quartiles, et les calculatrices ne donnent pas toutes la même. Dans ce cours : \(Q_1\) est la médiane de la **moitié inférieure** et \(Q_3\) la médiane de la **moitié supérieure**. Précise toujours la convention que tu utilises.

Moitié inférieure : 12, 15, 15, 16, 18, 20, donc \(Q_1 = \dfrac{15 + 16}{2} = 15{,}5\). Moitié supérieure : 21, 21, 22, 25, 27, 40, donc \(Q_3 = \dfrac{22 + 25}{2} = 23{,}5\).

**Lecture.** Un quart des temps sont inférieurs à 15,5 ms, un quart sont supérieurs à 23,5 ms, et la moitié « centrale » est entre 15,5 et 23,5 ms.

## 3. La dispersion : à quel point les valeurs s'écartent-elles ?

- **L'étendue** est la différence entre le plus grand et le plus petit : \(40 - 12 = 28\) ms.
- **L'écart interquartile** est \(Q_3 - Q_1 = 23{,}5 - 15{,}5 = 8\) ms : il décrit la dispersion de la moitié centrale.
- **L'écart type** mesure l'écart « typique » à la moyenne. On le construit en trois temps :

1. on calcule la **variance** \(V\), la moyenne des carrés des écarts à la moyenne : \(V = \dfrac{1}{n}\sum (x_i - \bar{x})^2\) ;
2. on en prend la **racine carrée** : \(\sigma = \sqrt{V}\) ;
3. on obtient un nombre **dans la même unité** que les données.

Pour notre série, \(V \approx 50{,}17\) et \(\sigma \approx 7{,}08\) ms. (On utilise la calculatrice ou Python pour ce calcul ; il est détaillé plus loin.)

> [!TIP]
> **Pourquoi des carrés ?** Si on additionnait les écarts \(x_i - \bar{x}\) sans carré, les écarts positifs et négatifs s'annuleraient (leur somme est toujours nulle). Le carré les rend tous positifs.

**Formule pratique.** La variance vaut aussi \(V = \overline{x^2} - \bar{x}^2\) : la moyenne des carrés moins le carré de la moyenne. Elle est plus rapide à la calculatrice.

> [!WARNING]
> **Deux écarts types.** Les calculatrices affichent \(\sigma_x\) (division par \(n\), utilisé ici) et \(s_x\) (division par \(n-1\), « écart type d'échantillon », qui donne ici \(7{,}40\)). Ne confonds pas : dans ce parcours, c'est \(\sigma_x\).

## 4. La boîte à moustaches : tout voir d'un coup

<figure class="fig-math">
<svg viewBox="0 0 520 170" role="img" aria-label="Boîte à moustaches">
<line class="fm-grid" x1="40.0" y1="20" x2="40.0" y2="120"/><text class="fm-t" x="40.0" y="138" text-anchor="middle">10</text>
<line class="fm-grid" x1="110.3" y1="20" x2="110.3" y2="120"/><text class="fm-t" x="110.3" y="138" text-anchor="middle">15</text>
<line class="fm-grid" x1="180.6" y1="20" x2="180.6" y2="120"/><text class="fm-t" x="180.6" y="138" text-anchor="middle">20</text>
<line class="fm-grid" x1="250.9" y1="20" x2="250.9" y2="120"/><text class="fm-t" x="250.9" y="138" text-anchor="middle">25</text>
<line class="fm-grid" x1="321.2" y1="20" x2="321.2" y2="120"/><text class="fm-t" x="321.2" y="138" text-anchor="middle">30</text>
<line class="fm-grid" x1="391.6" y1="20" x2="391.6" y2="120"/><text class="fm-t" x="391.6" y="138" text-anchor="middle">35</text>
<line class="fm-grid" x1="461.9" y1="20" x2="461.9" y2="120"/><text class="fm-t" x="461.9" y="138" text-anchor="middle">40</text>
<line class="fm-curve" x1="68.1" y1="70" x2="117.3" y2="70"/><line class="fm-curve" x1="229.8" y1="70" x2="461.9" y2="70"/>
<line class="fm-curve" x1="68.1" y1="58" x2="68.1" y2="82"/><line class="fm-curve" x1="461.9" y1="58" x2="461.9" y2="82"/>
<rect class="fm-box" x="117.3" y="48" width="112.5" height="44"/>
<line class="fm-acc" x1="187.7" y1="48" x2="187.7" y2="92"/>
<polygon class="fm-pt2" points="194.7,34 200.7,41 194.7,48 188.7,41"/>
<text class="fm-t" x="68.1" y="108" text-anchor="middle">min 12</text><text class="fm-t" x="117.3" y="40" text-anchor="middle">Q₁ 15,5</text><text class="fm-t" x="187.7" y="108" text-anchor="middle">médiane 20,5</text><text class="fm-t" x="239.8" y="40" text-anchor="start">Q₃ 23,5</text><text class="fm-t" x="461.9" y="108" text-anchor="middle">max 40</text><text class="fm-t fm-i" x="506" y="158" text-anchor="end">temps de réponse (ms)</text><text class="fm-t" x="204.7" y="28" text-anchor="start">moyenne 21</text>
</svg>
<figcaption>Boîte à moustaches de la série : la boîte va de Q₁ à Q₃, la barre est la médiane, le losange la moyenne, les moustaches vont du minimum au maximum.</figcaption>
</figure>

Cette représentation résume les cinq nombres clés (minimum, \(Q_1\), médiane, \(Q_3\), maximum) et la moyenne. Elle permet de comparer **rapidement** deux séries. Ici, la moustache de droite est beaucoup plus longue que celle de gauche : la valeur 40 « tire » la série vers le haut.

## 5. Valeurs aberrantes : moyenne ou médiane ?

La valeur 40 ms est nettement plus grande que les autres. Que se passe-t-il si on la retire ?

| | Avec 40 | Sans 40 |
|---|---|---|
| Moyenne | 21 ms | \(\dfrac{212}{11} \approx 19{,}27\) ms |
| Médiane | 20,5 ms | 20 ms |

La moyenne baisse de près de 2 ms, la médiane de 0,5 ms seulement. La **médiane est robuste** : elle réagit peu aux valeurs extrêmes. La **moyenne est sensible** à ces valeurs.

**Règle pratique.**

- Série **sans valeur extrême** et symétrique : la moyenne et l'écart type conviennent.
- Série avec valeurs extrêmes ou très dissymétrique (salaires, temps de réponse d'un réseau) : on préfère la **médiane** et les **quartiles**.

## 6. Séries groupées en classes

Quand les valeurs sont regroupées en classes, on ne connaît plus chaque valeur : on remplace chaque classe par son **centre** et on pondère par l'**effectif**.

**Exemple.** Durées de 40 sessions (en minutes) :

| Classe | \([0\,;\,10[\) | \([10\,;\,20[\) | \([20\,;\,30[\) | \([30\,;\,40[\) |
|---|---|---|---|---|
| Effectif | 4 | 10 | 18 | 8 |
| Centre | 5 | 15 | 25 | 35 |

**Moyenne.** \(\bar{x} = \dfrac{4 \times 5 + 10 \times 15 + 18 \times 25 + 8 \times 35}{40} = \dfrac{900}{40} = 22{,}5\) min.

**Variance.** \(V = \dfrac{4(5 - 22{,}5)^2 + 10(15 - 22{,}5)^2 + 18(25 - 22{,}5)^2 + 8(35 - 22{,}5)^2}{40} = 78{,}75\), donc \(\sigma \approx 8{,}87\) min.

**Classe médiane.** Les effectifs cumulés sont 4, 14, 32, 40. Les 20e et 21e valeurs (centrales) sont dans la classe \([20\,;\,30[\) : c'est la **classe médiane**.

> [!TIP]
> Les résultats d'une série en classes sont des **approximations** : on a perdu l'information sur la position exacte dans chaque classe.

## 7. Calculer avec Python

```python
from statistics import mean, median, pstdev

temps = [12, 15, 15, 16, 18, 20, 21, 21, 22, 25, 27, 40]
print(mean(temps))      # 21
print(median(temps))    # 20.5
print(pstdev(temps))    # 7.08... (division par n)
```

La fonction `pstdev` donne l'écart type de **population** (division par \(n\)), celui du cours.

## 8. Effet d'un changement d'unité

Si on transforme chaque valeur par \(y = ax + b\) (changement d'unité, ajout d'un délai fixe) :

- la moyenne devient \(\bar{y} = a\bar{x} + b\) ;
- l'écart type devient \(\sigma_y = |a|\,\sigma_x\) : **le décalage \(b\) ne change pas la dispersion**.

**Exemple.** Temps en secondes (moyenne 21, écart type 7,08) convertis en millisecondes (\(a = 1000\)) avec un délai fixe de 50 ms (\(b = 50\)) : moyenne \(21 \times 1000 + 50 = 21\,050\) ms ; écart type \(7\,080\) ms.

## 9. À retenir

> [!NOTE]
> - **Position :** moyenne (sensible aux valeurs extrêmes), médiane (robuste), quartiles.
> - **Dispersion :** étendue, écart interquartile, variance et **écart type** (même unité que les données).
> - Série en classes : centres de classe pondérés par les effectifs, résultats approchés.
> - Valeurs aberrantes : préférer la **médiane**.
> - \(y = ax + b\) : \(\bar{y} = a\bar{x} + b\) et \(\sigma_y = |a|\,\sigma_x\).

## 10. Teste-toi

**Question 1.** Série : 4, 8, 6, 10, 12. Donner la moyenne, la médiane et l'étendue.

**Question 2.** Deux services ont une moyenne de 100 ms. L'écart type est de 5 ms pour A et de 30 ms pour B. Lequel est le plus régulier ?

<details markdown="1">
<summary>Voir les réponses</summary>

1. Moyenne \(\dfrac{4 + 8 + 6 + 10 + 12}{5} = 8\). Série ordonnée : 4, 6, 8, 10, 12 ; la médiane est la valeur du milieu, **8**. Étendue : \(12 - 4 = 8\).
2. Le service **A** : son écart type est plus petit, donc ses temps sont plus proches de la moyenne.

</details>

**Pour continuer :** le [cours 2 sur le lien entre deux grandeurs](02-regression-et-ajustement.md).

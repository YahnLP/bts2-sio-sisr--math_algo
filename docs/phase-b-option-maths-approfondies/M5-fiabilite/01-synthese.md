# Synthèse – Fiabilité

*BTS SIO SISR 2e année – Option mathématiques approfondies – M5*

> [!NOTE]
> **Idée directrice.** Quantifier la capacité d'un équipement ou d'un système à fonctionner sans panne : probabilité de survie, durée moyenne de bon fonctionnement, effet de la redondance, disponibilité. C'est le langage des **SLA** (accords de niveau de service) en infrastructure.

Ce module reprend la partie du référentiel qui relève de l'option ; certains paragraphes du module standard n'y sont pas traités.

## 1. Fonction de fiabilité

Soit \(T\) la durée de bon fonctionnement d'un composant. La **fiabilité** à l'instant \(t\) est \(R(t) = P(T > t)\) : la probabilité qu'il fonctionne encore à \(t\). On a \(R(0) = 1\) et \(R\) est décroissante.

## 2. Loi exponentielle (taux de défaillance constant)

Quand le composant ne « vieillit » pas, le taux de défaillance est une constante \(\lambda\) (en h\(^{-1}\)) :

\[
R(t) = e^{-\lambda t}, \qquad P(T \le t) = 1 - e^{-\lambda t}, \qquad \text{MTBF} = E(T) = \dfrac{1}{\lambda}.
\]

- La **MTBF** (*Mean Time Between Failures*) est la durée moyenne de bon fonctionnement.
- Propriété **sans mémoire** : \(P(T > s + t \mid T > s) = P(T > t)\). Un composant qui a déjà fonctionné \(s\) heures est « comme neuf ».
- **Médiane** : \(t_{1/2} = \dfrac{\ln 2}{\lambda}\), plus petite que la MTBF.

## 3. Systèmes de composants indépendants

| Montage | Principe | Fiabilité |
|---|---|---|
| **Série** | il faut que **tous** fonctionnent | \(R = R_1 \times R_2 \times \dots\) |
| **Parallèle** | il suffit qu'**un** fonctionne (redondance) | \(R = 1 - (1 - R_1)(1 - R_2)\cdots\) |

Pour des composants de taux \(\lambda\) identiques : en série de \(n\), le taux devient \(n\lambda\) (MTBF divisée par \(n\)) ; en parallèle de deux, la MTBF vaut \(\dfrac{3}{2\lambda}\).

Un système mixte se calcule en réduisant d'abord les blocs en parallèle, puis les séries.

## 4. Disponibilité

Avec une durée moyenne de réparation **MTTR**, la disponibilité en régime établi est
\[
A = \dfrac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}.
\]
Le temps d'arrêt annuel est \(8\,760 \times (1 - A)\) heures.

> [!TIP]
> **Lien avec les SLA.** « 99,9 % de disponibilité » autorise environ 8,8 h d'arrêt par an ; « 99,99 % », environ 53 minutes.

## 5. Pièges fréquents

- Confondre MTBF et durée de vie garantie.
- Oublier que la redondance suppose des pannes **indépendantes** (deux machines sur la même alimentation ne le sont pas).
- Appliquer la formule série à un montage parallèle.

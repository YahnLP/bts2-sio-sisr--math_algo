# Synthèse – Calcul des probabilités

*BTS SIO SISR 2e année – Option mathématiques approfondies – M4*

> [!NOTE]
> **Idée directrice.** Modéliser un phénomène aléatoire (panne, arrivée de requêtes, temps de réponse) par une **loi**, puis en tirer des probabilités, une valeur moyenne et une dispersion. Les calculs de probabilité se font à la **calculatrice** ou avec Python ; on les interprète.

Le théorème central limite et les distributions d'échantillonnage ne sont **pas** au programme de l'option.

## 1. Variable aléatoire discrète

Une variable aléatoire \(X\) prend des valeurs \(x_i\) avec des probabilités \(p_i\) (leur somme vaut 1).

- **Espérance** : \(E(X) = \sum p_i x_i\) (valeur moyenne à long terme).
- **Variance** : \(V(X) = \sum p_i x_i^2 - E(X)^2\) ; **écart type** \(\sigma = \sqrt{V}\).

## 2. Loi binomiale \(\mathcal{B}(n, p)\)

On répète \(n\) fois, de façon indépendante, une épreuve à deux issues (succès de probabilité \(p\)). \(X\) compte les succès :

\[
P(X = k) = \binom{n}{k} p^{k}(1-p)^{n-k}, \quad E(X) = np, \quad V(X) = np(1-p).
\]

## 3. Loi de Poisson \(\mathcal{P}(\lambda)\)

Elle modélise le nombre d'événements rares dans un intervalle (pannes par jour, requêtes par seconde) :

\[
P(X = k) = e^{-\lambda}\dfrac{\lambda^{k}}{k!}, \quad E(X) = V(X) = \lambda.
\]

Elle approche \(\mathcal{B}(n, p)\) quand \(n\) est grand et \(p\) petit, avec \(\lambda = np\).

## 4. Loi normale \(\mathcal{N}(m, \sigma)\)

Loi « en cloche » de moyenne \(m\) et d'écart type \(\sigma\). On calcule avec la calculatrice ou en passant par la variable centrée réduite \(Z = \dfrac{X - m}{\sigma}\), de loi \(\mathcal{N}(0, 1)\). Repères : environ 68 % des valeurs sont dans \([m - \sigma\,;\,m + \sigma]\), 95 % dans \([m - 2\sigma\,;\,m + 2\sigma]\).

## 5. Choisir la loi

| Situation | Loi |
|---|---|
| Compter des succès sur \(n\) essais indépendants | binomiale |
| Compter des événements rares sur un intervalle | Poisson |
| Mesure continue autour d'une moyenne | normale |
| Durée avant une panne sans vieillissement | exponentielle (voir M5) |

## 6. Pièges fréquents

- Utiliser la binomiale quand les essais ne sont pas indépendants.
- Oublier que \(P(X \ge 2) = 1 - P(X \le 1)\).
- Lire une probabilité sans la commenter (« 12 % de risque » : est-ce acceptable ?).

# Synthèse – Fonction d'une variable réelle

*BTS SIO SISR 2e année – Option mathématiques approfondies – M1*

> [!NOTE]
> **Idée directrice.** Une fonction est un **modèle** : elle relie une grandeur d'entrée (nombre de postes, temps, quantité) à une grandeur de sortie (coût, durée, charge). On apprend à la lire, à la comparer et à l'interpréter, pas à multiplier les calculs à la main.

## 1. Lire et construire une fonction

Une fonction \(f\) associe à chaque nombre \(x\) d'un ensemble de départ **au plus un** nombre \(f(x)\). On la décrit par une formule, un tableau de valeurs ou une courbe. On travaille ici sur des fonctions à valeurs réelles dont l'ensemble de départ est donné par le problème (la recherche d'un domaine de définition est hors programme).

| Famille | Forme | À retenir |
|---|---|---|
| Affine | \(f(x) = ax + b\) | pente \(a\), ordonnée à l'origine \(b\) ; croissante si \(a > 0\) |
| Second degré | \(f(x) = ax^2 + bx + c\) | sommet en \(x = -\dfrac{b}{2a}\) ; symétrie autour de ce sommet |
| Inverse | \(f(x) = \dfrac{k}{x}\) | décroissante pour \(x > 0\) si \(k > 0\) |
| Exponentielle | \(f(x) = e^{x}\), \(a^{x}\) | strictement positive, croît très vite |
| Logarithme | \(f(x) = \ln x\) | pour \(x > 0\), croît lentement ; \(\ln(e^{x}) = x\) |

## 2. Composition de fonctions

\((f \circ g)(x) = f(g(x))\) : on applique d'abord \(g\), puis \(f\). En général \(f \circ g \ne g \circ f\).

## 3. Exponentielle et logarithme

- \(e^{a+b} = e^{a}e^{b}\), \(\ln(ab) = \ln a + \ln b\), \(\ln(a^{n}) = n \ln a\).
- Résoudre \(e^{u} = k\) (avec \(k > 0\)) : \(u = \ln k\).
- Résoudre \(a^{n} \ge c\) (avec \(a > 1\)) : \(n \ge \dfrac{\ln c}{\ln a}\). C'est la méthode du **seuil** : on en déduit le plus petit entier convenable.

## 4. Résoudre et interpréter

1. Résoudre une équation \(f(x) = k\) : par le calcul si c'est élémentaire, sinon avec la calculatrice ou par lecture de la courbe.
2. Comparer deux modèles : chercher où \(f(x) = g(x)\), puis lire quel modèle est le plus avantageux de chaque côté.
3. **Valider** : une solution négative, non entière ou hors du contexte (un nombre de postes, une durée) est **rejetée** ou arrondie, et on le dit.

> [!TIP]
> **Réflexe de contrôle.** Remplace la solution dans l'énoncé de départ : le résultat a-t-il un sens (unité, ordre de grandeur) ?

## 5. Pièges fréquents

- Confondre \(f(x+h)\) et \(f(x) + h\).
- Écrire \(\ln(a+b) = \ln a + \ln b\) (faux : c'est le produit qui devient somme).
- Donner une solution non entière pour un nombre d'objets sans la discuter.

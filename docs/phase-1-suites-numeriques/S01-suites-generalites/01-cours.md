# Cours – Suites numériques : définition et programmation

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S01 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** les boucles `POUR` et `TANT QUE` (S04 de la 1re année) ; l'écriture d'une fonction en Python.
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Définir** une suite par une formule explicite ou par récurrence ;
- [ ] **Calculer** des termes à la main et par programme ;
- [ ] **Représenter** une suite par un tableau de valeurs ;
- [ ] **Reconnaître** le sens de variation d'une suite ;
- [ ] **Choisir** entre formule explicite et récurrence.

## I. Qu'est-ce qu'une suite ?

Une **suite numérique** associe à chaque entier naturel \(n\) un nombre réel noté \(u_n\) (on lit « u indice n »). L'entier \(n\) est le **rang** ; \(u_n\) est le **terme de rang \(n\)**. La suite entière se note \((u_n)\).

Exemple : la place occupée sur un disque à la fin de chaque mois est une suite. À la fin du mois 0, le disque contient 120 Go ; à la fin du mois 1, 135 Go… Le terme de rang \(n\) est la place occupée à la fin du mois \(n\).

> [!WARNING]
> \(u_n\) est le terme de rang \(n\) ; \(u_{n+1}\) est le terme **suivant** ; \(u_n + 1\) est le terme \(u_n\) **augmenté de 1**. Ce n'est pas la même chose.

## II. Deux façons de définir une suite

### Formule explicite

On donne \(u_n\) directement en fonction de \(n\) : \(u_n = f(n)\).

Exemple : \(u_n = 3n + 2\). Alors \(u_0 = 2\), \(u_1 = 5\), \(u_2 = 8\), \(u_3 = 11\), et \(u_{100} = 302\) **sans calculer les termes précédents**.

### Relation de récurrence

On donne le premier terme et une règle qui fait passer d'un terme au suivant : \(u_{n+1} = f(u_n)\).

Exemple : \(u_0 = 1\) et \(u_{n+1} = 2u_n + 1\). Alors \(u_1 = 3\), \(u_2 = 7\), \(u_3 = 15\), \(u_4 = 31\). Pour obtenir \(u_{100}\), il faut calculer **tous** les termes précédents (ou trouver une formule explicite, ce qu'on apprend à faire dans les séances suivantes).

| Définition | Avantage | Inconvénient |
|---|---|---|
| **Explicite** | Accès direct à n'importe quel terme | Pas toujours connue |
| **Récurrence** | Décrit simplement un mécanisme (« chaque mois on ajoute… ») | Il faut tous les termes précédents |

## III. Calculer par programme

**Formule explicite** : une simple fonction.

```python
def u(n):
    return 3 * n + 2
```

**Récurrence** : une boucle qui garde le terme courant.

```python
def u(n):
    terme = 1              # u_0
    for _ in range(n):     # n passages : u_1, ..., u_n
        terme = 2 * terme + 1
    return terme
```

Après \(k\) tours, `terme` vaut \(u_k\) : c'est l'**invariant** de la boucle. Pour garder tous les termes, on les range dans une liste :

```python
def premiers_termes(n):
    termes = [1]
    for _ in range(n):
        termes.append(2 * termes[-1] + 1)
    return termes          # premiers_termes(4) donne [1, 3, 7, 15, 31]
```

## IV. Tableau de valeurs

| \(n\) | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| \(u_n = 3n + 2\) | 2 | 5 | 8 | 11 | 14 |
| \(u_n\) avec \(u_0 = 1\), \(u_{n+1} = 2u_n+1\) | 1 | 3 | 7 | 15 | 31 |

## V. Sens de variation

Une suite est :

- **croissante** si \(u_{n+1} \ge u_n\) pour tout \(n\) ;
- **décroissante** si \(u_{n+1} \le u_n\) pour tout \(n\) ;
- **constante** si \(u_{n+1} = u_n\) pour tout \(n\).

En pratique, on étudie le **signe de \(u_{n+1} - u_n\)**.

Exemple : \(u_n = n^2 - 4n\). Alors \(u_{n+1} - u_n = (n+1)^2 - 4(n+1) - n^2 + 4n = 2n - 3\). Ce nombre est négatif pour \(n \le 1\) et positif pour \(n \ge 2\). Les premiers termes sont \(0, -3, -4, -3, 0\) : la suite décroît jusqu'à \(u_2\) puis **croît à partir du rang 2**. Une suite peut ne pas être monotone sur tous les rangs.

> [!TIP]
> Pour montrer qu'une suite n'est **pas** croissante, un seul contre-exemple suffit (ici \(u_1 < u_0\)). Pour montrer qu'elle l'est, il faut une preuve valable pour tout \(n\).

## VI. Choisir sa définition

- Pour **prévoir** une valeur lointaine ou comparer deux scénarios : formule explicite.
- Pour **décrire** un mécanisme (« chaque jour, on ajoute les nouveaux journaux ») : récurrence.
- Pour **programmer** : une boucle avec récurrence est simple et exacte ; une formule explicite évite la boucle.

**Test flash.** Avec \(u_0 = 2\) et \(u_{n+1} = 3u_n - 1\), que vaut \(u_2\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(u_1 = 3 \times 2 - 1 = 5\), puis \(u_2 = 3 \times 5 - 1 = 14\).

</details>

## À retenir

- Une suite associe un terme \(u_n\) à chaque rang \(n\).
- **Explicite** : \(u_n = f(n)\). **Récurrence** : \(u_0\) donné et \(u_{n+1} = f(u_n)\).
- En Python : une fonction (explicite) ou une boucle qui garde le terme courant (récurrence).
- Sens de variation : signe de \(u_{n+1} - u_n\).

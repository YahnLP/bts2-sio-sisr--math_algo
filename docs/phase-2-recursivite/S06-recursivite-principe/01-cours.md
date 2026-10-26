# Cours – Récursivité : principe

*BTS SIO SISR 2e année – Pour aller plus loin – S06 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S05 (suites récurrentes, terminaison d'une boucle) ; écrire une fonction en Python.
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Identifier** le cas de base et le cas récursif ;
- [ ] **Écrire** une fonction récursive simple ;
- [ ] **Dérouler** une exécution récursive ;
- [ ] **Justifier** la terminaison par un variant ;
- [ ] **Comparer** avec une version itérative.

## I. L'idée

Une fonction est **récursive** quand elle **s'appelle elle-même** pour résoudre un problème **plus petit** du même type. C'est la version « programmation » d'une suite définie par récurrence (S01) : \(u_n\) se calcule à partir de \(u_{n-1}\).

Exemple : la factorielle \(n! = 1 \times 2 \times \dots \times n\), avec \(0! = 1\). On a \(n! = n \times (n-1)!\).

```python
def fact(n):
    if n == 0:                 # cas de base
        return 1
    return n * fact(n - 1)     # cas récursif
```

## II. Les trois ingrédients

| Ingrédient | Rôle | Dans `fact` |
|---|---|---|
| **Cas de base** | Résultat connu directement, qui arrête les appels | `n == 0` renvoie 1 |
| **Cas récursif** | Ramène le problème à un problème plus petit | `n * fact(n - 1)` |
| **Variant** | Entier qui décroît strictement à chaque appel et reste \(\ge 0\) | `n` |

Sans cas de base, les appels ne s'arrêtent pas : Python s'interrompt avec une erreur `RecursionError`. Si l'appel ne se rapproche pas du cas de base (par exemple `fact(n + 1)`), c'est la même chose.

## III. Dérouler un appel

Pour `fact(3)`, les appels s'empilent (« descente »), puis les résultats remontent (« remontée ») :

```text
fact(3) = 3 × fact(2)
            fact(2) = 2 × fact(1)
                        fact(1) = 1 × fact(0)
                                    fact(0) = 1
                        fact(1) = 1 × 1 = 1
            fact(2) = 2 × 1 = 2
fact(3) = 3 × 2 = 6
```

Il y a \(n + 1\) appels pour `fact(n)` (de \(n\) à 0).

## IV. D'autres exemples

```python
def somme(n):                  # 1 + 2 + ... + n
    if n == 0:
        return 0
    return n + somme(n - 1)

def puissance(x, n):           # x ** n
    if n == 0:
        return 1
    return x * puissance(x, n - 1)

def pgcd(a, b):                # algorithme d'Euclide
    if b == 0:
        return a
    return pgcd(b, a % b)

def binaire(n):                # écriture de n en base 2 (n >= 0)
    if n < 2:
        return str(n)
    return binaire(n // 2) + str(n % 2)
```

Exemple d'Euclide : `pgcd(84, 36)` appelle `pgcd(36, 12)` puis `pgcd(12, 0)` et renvoie 12. Ici le variant est `b` : il diminue strictement car \(a \bmod b < b\).

Exemple de conversion : `binaire(13)` donne `"1101"` (13 → 6 reste 1, 6 → 3 reste 0, 3 → 1 reste 1, 1 est un cas de base).

## V. Récursif ou itératif ?

| | Récursif | Itératif |
|---|---|---|
| Écriture | proche de la définition mathématique | boucle et variables |
| Mémoire | un appel en attente par niveau (pile, voir S07) | quelques variables |
| Risque | profondeur limitée (`RecursionError`) | boucle infinie si le variant est faux |

Un même problème s'écrit souvent des deux façons ; le résultat est identique. On choisit la plus **claire** et la plus **sûre**.

> [!TIP]
> Pour écrire une fonction récursive : (1) quel est le plus petit problème, que l'on sait résoudre directement ? (2) comment ramener un problème à un problème un peu plus petit ? (3) qu'est-ce qui décroît ?

**Test flash.** Que renvoie `f(4)` pour `def f(n): return 0 if n == 0 else 1 + f(n - 1)` ?

<details markdown="1">
<summary>Voir la réponse</summary>

`f(n)` compte les pas jusqu'à 0 : `f(4)` renvoie **4** (4 appels qui ajoutent 1, plus le cas de base).

</details>

## À retenir

- Récursif = cas de base + cas récursif sur un problème plus petit.
- Le **variant** (entier qui décroît) garantit l'arrêt.
- `fact(n)` fait \(n + 1\) appels.
- Sans cas de base ou sans réduction : `RecursionError`.

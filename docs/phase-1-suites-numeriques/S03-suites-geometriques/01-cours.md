# Cours – Suites géométriques

*BTS SIO SISR 2e année – Pour aller plus loin – S03 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S02 (suites arithmétiques) ; les pourcentages d'évolution (coefficient multiplicateur).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Reconnaître** une suite géométrique et déterminer sa raison ;
- [ ] **Écrire** le terme général ;
- [ ] **Calculer** la somme de termes consécutifs ;
- [ ] **Modéliser** une croissance exponentielle (doublement, taux) ;
- [ ] **Programmer** et tester une suite géométrique.

## I. Définition

Une suite \((u_n)\) est **géométrique** s'il existe un nombre \(q\), la **raison**, tel que pour tout \(n\) :

\[ u_{n+1} = q \, u_n \]

On multiplie **toujours par le même nombre**. Si aucun terme n'est nul, on le vérifie avec les rapports \(\dfrac{u_{n+1}}{u_n}\).

Exemple : \(3, 6, 12, 24, \dots\) a pour raison \(q = 2\). La suite \(2, 5, 8, \dots\) n'est pas géométrique (rapports 2,5 puis 1,6) ; elle est arithmétique.

## II. Terme général

\[ u_n = u_0 \, q^n \qquad \text{et plus généralement} \qquad u_n = u_p \, q^{\,n-p} \]

Exemple : \(u_0 = 3\), \(q = 2\) : \(u_{10} = 3 \times 2^{10} = 3\,072\).

**Sens de variation** (avec \(u_0 > 0\)) :

| Raison | Comportement |
|---|---|
| \(q > 1\) | croissante |
| \(0 < q < 1\) | décroissante |
| \(q = 1\) | constante |
| \(q < 0\) | les signes alternent (ni croissante ni décroissante) |

## III. Pourcentages d'évolution

Augmenter de \(t\,\%\) revient à multiplier par \(1 + \dfrac{t}{100}\) ; diminuer de \(t\,\%\), par \(1 - \dfrac{t}{100}\). Une évolution de \(t\,\%\) **par période** donne donc une suite géométrique de raison \(q = 1 \pm \dfrac{t}{100}\).

Exemples : +20 % par mois : \(q = 1{,}2\). −15 % par an : \(q = 0{,}85\).

> [!WARNING]
> Deux augmentations successives de 20 % ne font **pas** 40 % : elles multiplient par \(1{,}2 \times 1{,}2 = 1{,}44\), soit +44 %.

## IV. Somme de termes consécutifs

Pour \(q \ne 1\) :

\[ u_0 + u_1 + \dots + u_n = u_0 \, \frac{1 - q^{\,n+1}}{1 - q} \]

Pour \(q = 1\), tous les termes valent \(u_0\) et la somme vaut \((n+1)\,u_0\).

*Pourquoi ?* En notant \(S\) la somme, \(qS = u_1 + \dots + u_{n+1}\). En retranchant : \(S - qS = u_0 - u_{n+1} = u_0(1 - q^{n+1})\), d'où la formule.

Exemple : \(1 + 2 + 4 + \dots + 2^{10} = \dfrac{1 - 2^{11}}{1 - 2} = 2^{11} - 1 = 2\,047\).

> [!TIP]
> Une somme de puissances de 2 vaut « la puissance suivante moins 1 » : pratique pour compter des valeurs en binaire (un nombre de \(k\) bits va de 0 à \(2^k - 1\)).

## V. Arithmétique ou géométrique ?

| Question | Arithmétique | Géométrique |
|---|---|---|
| Ce qui est constant | la **différence** | le **rapport** |
| Évolution | linéaire | exponentielle |
| Exemple | +25 Mo de plus chaque jour | +20 % chaque mois |

Une croissance **exponentielle** finit toujours par dépasser une croissance linéaire, même si elle démarre plus bas.

## VI. En Python

```python
def terme(u0, q, n):
    return u0 * q ** n

def somme(u0, q, n):          # entiers, q != 1
    return u0 * (q ** (n + 1) - 1) // (q - 1)
```

Avec des taux décimaux, les flottants donnent des valeurs **approchées** : on arrondit à l'affichage (`round(x, 2)`) et on ne teste pas une égalité exacte.

**Test flash.** Un trafic de 500 Go augmente de 20 % par mois. Quel trafic après 3 mois ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(500 \times 1{,}2^3 = 500 \times 1{,}728 = 864\) Go.

</details>

## À retenir

- Géométrique : \(u_{n+1} = q\,u_n\) ; \(u_n = u_0 q^n\).
- Évolution de \(t\,\%\) : \(q = 1 \pm t/100\) ; deux évolutions se multiplient, elles ne s'additionnent pas.
- Somme : \(u_0 \dfrac{1 - q^{n+1}}{1 - q}\) pour \(q \ne 1\).
- Exponentielle : finit par dépasser toute croissance linéaire.

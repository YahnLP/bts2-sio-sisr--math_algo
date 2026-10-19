# Cours – Suites arithmétiques

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S02 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S01 (définition d'une suite, récurrence, formule explicite).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Reconnaître** une suite arithmétique et déterminer sa raison ;
- [ ] **Écrire** le terme général ;
- [ ] **Calculer** la somme de termes consécutifs ;
- [ ] **Modéliser** une croissance linéaire (stockage, tarifs) ;
- [ ] **Programmer** et tester une suite arithmétique.

## I. Définition

Une suite \((u_n)\) est **arithmétique** s'il existe un nombre \(r\), la **raison**, tel que pour tout \(n\) :

\[ u_{n+1} = u_n + r \]

On ajoute **toujours la même quantité**. Pour le vérifier sur des données, on calcule les différences \(u_{n+1} - u_n\) : si elles sont toutes égales, la suite est (peut-être) arithmétique ; si deux différences sont distinctes, elle ne l'est pas.

Exemple : \(5, 9, 13, 17, \dots\) a pour raison \(r = 4\). La suite \(1, 2, 4, 7, \dots\) n'est pas arithmétique : les différences sont 1, 2, 3.

## II. Terme général

Pour une suite arithmétique de premier terme \(u_0\) et de raison \(r\) :

\[ u_n = u_0 + n\,r \]

Plus généralement, pour deux rangs \(p\) et \(n\) : \(u_n = u_p + (n-p)\,r\).

Exemple : \(u_0 = 12\), \(r = 5\) : \(u_{20} = 12 + 100 = 112\).

**Sens de variation** : si \(r > 0\), croissante ; si \(r < 0\), décroissante ; si \(r = 0\), constante (car \(u_{n+1} - u_n = r\)).

## III. Somme de termes consécutifs

La somme de \(k\) termes consécutifs d'une suite arithmétique vaut :

\[ \text{somme} = k \times \frac{\text{premier terme} + \text{dernier terme}}{2} \]

Pour \(u_0 + u_1 + \dots + u_n\) il y a \(n + 1\) termes :

\[ u_0 + \dots + u_n = (n+1)\,\frac{u_0 + u_n}{2} \]

*Pourquoi ?* On écrit la somme dans les deux sens et on additionne terme à terme : chaque paire \(u_0 + u_n\), \(u_1 + u_{n-1}\), … vaut la même quantité \(u_0 + u_n\), et il y a \(n+1\) paires pour une somme comptée deux fois.

Cas classique : \(1 + 2 + \dots + n = \dfrac{n(n+1)}{2}\). Par exemple \(1 + 2 + \dots + 100 = 5\,050\).

> [!WARNING]
> **Compter les termes** : de \(u_p\) à \(u_n\), il y a \(n - p + 1\) termes (et non \(n - p\)). Cette erreur est la plus fréquente.

## IV. Modéliser

Un phénomène est **arithmétique** quand une quantité fixe s'ajoute à chaque période : un journal qui grossit de 25 Mo de plus chaque jour, un tarif fixe plus un prix unitaire, des adresses régulièrement espacées.

*Exemple (tarifs).* Offre A : 30 € + 4 € par palier de 100 Go, soit \(a_n = 30 + 4n\). Offre B : 50 € + 3 € par palier, soit \(b_n = 50 + 3n\). Elles coûtent autant quand \(30 + 4n = 50 + 3n\), soit \(n = 20\) ; au-delà, B est moins chère.

## V. En Python

```python
def terme(u0, r, n):
    return u0 + n * r

def somme(u0, r, n):
    return (n + 1) * (2 * u0 + n * r) // 2   # (n+1)(u0+un)/2 ; le produit est toujours pair
```

La somme avec une boucle sert de **contrôle** : `sum(u0 + k * r for k in range(n + 1))`.

**Test flash.** Combien de termes y a-t-il dans la liste \(7, 10, 13, \dots, 100\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(7 + 3k = 100\) donne \(k = 31\). Le rang va de 0 à 31 : **32 termes**.

</details>

## À retenir

- Arithmétique : \(u_{n+1} = u_n + r\) ; \(u_n = u_0 + nr\) ; \(u_n = u_p + (n-p)r\).
- Somme : nombre de termes \(\times\) (premier + dernier) \(/ 2\).
- Nombre de termes de \(u_p\) à \(u_n\) : \(n - p + 1\).
- Croissance linéaire : on ajoute une quantité fixe.

# Cours – Comportement à long terme et algorithmes de seuil

*BTS SIO SISR 2e année – Pour aller plus loin – S05 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S03 et S04 (suites géométriques, récurrence « pourcentage plus ajout »).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Étudier** la monotonie d'une suite ;
- [ ] **Déterminer** la limite d'une suite arithmétique ou géométrique ;
- [ ] **Étudier** une suite récurrente affine (point fixe) ;
- [ ] **Écrire** un algorithme de seuil et en garantir l'arrêt ;
- [ ] **Interpréter** une limite dans le contexte.

## I. Limites usuelles

On dit que \((u_n)\) **tend vers** \(L\) (elle **converge**) si \(u_n\) devient aussi proche de \(L\) qu'on le veut quand \(n\) est assez grand. Elle peut aussi **tendre vers \(+\infty\)** (elle dépasse tout nombre) ou vers \(-\infty\), ou n'avoir **aucune limite**.

| Suite | Condition | Comportement |
|---|---|---|
| Arithmétique \(u_0 + nr\) | \(r > 0\) | tend vers \(+\infty\) |
| | \(r < 0\) | tend vers \(-\infty\) |
| | \(r = 0\) | constante |
| Géométrique \(u_0 q^n\) (\(u_0 > 0\)) | \(q > 1\) | tend vers \(+\infty\) |
| | \(-1 < q < 1\) | tend vers \(0\) |
| | \(q = 1\) | constante |
| | \(q \le -1\) | pas de limite (alterne) |

Exemple : \(3 \times 0{,}8^n\) tend vers 0 (une baisse de 20 % par période finit par tout réduire à presque rien).

## II. Suite récurrente affine

Une suite de la forme

\[ u_{n+1} = a\,u_n + b \qquad (a \ne 1) \]

a un **point fixe** \(L\) : la valeur qui ne change plus, solution de \(L = aL + b\), soit

\[ L = \frac{b}{1 - a} \]

La suite auxiliaire \(v_n = u_n - L\) est **géométrique de raison \(a\)** : en effet \(v_{n+1} = u_{n+1} - L = a\,u_n + b - (aL + b) = a\,(u_n - L) = a\,v_n\). On en déduit

\[ u_n = L + (u_0 - L)\,a^n \]

Si \(-1 < a < 1\), alors \(a^n \to 0\) et **\(u_n\) tend vers \(L\)**.

*Exemple.* \(u_0 = 0\) et \(u_{n+1} = 0{,}5\,u_n + 10\). Le point fixe est \(L = \dfrac{10}{1 - 0{,}5} = 20\). Donc \(u_n = 20 - 20 \times 0{,}5^n\) : les termes \(0, 10, 15, 17{,}5, 18{,}75, \dots\) se rapprochent de 20 sans le dépasser.

*Sens informatique.* Si chaque mois on supprime la moitié des fichiers temporaires et qu'on en ajoute 10 Go, le volume se **stabilise** vers 20 Go : il n'y a pas de saturation à long terme si le disque dépasse 20 Go.

## III. Algorithme de seuil

On cherche le **premier rang** où la suite atteint un seuil \(S\) :

```python
def rang_seuil(f, u0, seuil):
    u, n = u0, 0
    while u < seuil:
        u = f(u)
        n = n + 1
    return n
```

> [!WARNING]
> Cette boucle **ne s'arrête pas** si la suite ne dépasse jamais le seuil (par exemple si elle converge vers une limite inférieure au seuil). Avant d'écrire un algorithme de seuil, on se demande : **la suite atteint-elle le seuil ?** (limite \(+\infty\), ou limite au-delà du seuil). Sinon, on ajoute un **garde-fou** : un nombre maximal d'itérations.

```python
def rang_seuil_sur(f, u0, seuil, nmax):
    u, n = u0, 0
    while u < seuil and n < nmax:
        u = f(u)
        n = n + 1
    return n if u >= seuil else None
```

*Variant :* l'entier `nmax - n` décroît strictement, donc la boucle s'arrête toujours.

## IV. Sommes qui dépassent un seuil

Pour trouver le plus petit \(n\) tel que \(1 + 2 + \dots + n \ge S\), on accumule dans une boucle : `s` augmente à chaque tour, donc il dépasse \(S\) au bout d'un nombre fini de tours (la somme tend vers \(+\infty\)).

**Test flash.** La suite \(u_{n+1} = 0{,}8\,u_n + 30\) tend vers quelle valeur ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(L = \dfrac{30}{1 - 0{,}8} = 150\). Le volume se stabilise vers 150 Go.

</details>

## À retenir

- Arithmétique : \(\pm\infty\) selon le signe de \(r\). Géométrique : \(\to 0\) si \(|q| < 1\), \(\to +\infty\) si \(q > 1\).
- \(u_{n+1} = a u_n + b\) : point fixe \(L = b/(1-a)\), \(u_n = L + (u_0 - L)a^n\).
- Algorithme de seuil : vérifier que le seuil est atteignable, sinon garde-fou.

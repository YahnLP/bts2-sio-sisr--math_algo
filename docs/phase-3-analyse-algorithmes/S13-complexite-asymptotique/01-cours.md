# Cours – Complexité asymptotique

*BTS SIO SISR 2e année – Pour aller plus loin – S13 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** coût en opérations (S12) ; \(\log_2\) et puissances de 2.
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Simplifier** un coût en notation \(O(\cdot)\) ;
- [ ] **Reconnaître** les classes \(O(1)\), \(O(\log n)\), \(O(n)\), \(O(n\log n)\), \(O(n^2)\), \(O(2^n)\) ;
- [ ] **Prévoir** l'effet d'un doublement ou d'un ×10 de la taille ;
- [ ] **Estimer** une durée à partir d'un nombre d'opérations et d'une hypothèse de vitesse.

## I. Pourquoi simplifier

Un coût comme \(3n + 5\) contient des détails qui dépendent du modèle (une addition de plus ou de moins). Ce qui compte pour de grandes tailles, c'est la **façon dont le coût grandit**. La notation \(O\) garde cet ordre de grandeur.

**Définition.** \(f(n) = O(g(n))\) s'il existe une constante \(c > 0\) et un rang \(n_0\) tels que, pour tout \(n \ge n_0\), \(f(n) \le c \cdot g(n)\).

*Exemple.* \(3n + 5 = O(n)\) : avec \(c = 4\) et \(n_0 = 5\), \(3n + 5 \le 4n\) dès que \(n \ge 5\).

## II. Règles de simplification

1. On **supprime les constantes multiplicatives** : \(5n^2 = O(n^2)\).
2. On **garde le terme dominant** : \(n^2 + 100n + 7 = O(n^2)\).
3. Une boucle dans une boucle **multiplie** les coûts ; deux blocs l'un après l'autre les **additionnent** (le plus grand l'emporte).

## III. Les classes usuelles

| Classe | Nom | Exemple |
|---|---|---|
| \(O(1)\) | constante | accès à `L[i]` |
| \(O(\log n)\) | logarithmique | recherche dichotomique |
| \(O(n)\) | linéaire | recherche séquentielle |
| \(O(n \log n)\) | quasi-linéaire | tri fusion |
| \(O(n^2)\) | quadratique | doublons par deux boucles |
| \(O(2^n)\) | exponentielle | tous les sous-ensembles |

## IV. Effet d'un changement de taille

| Classe | Si \(n\) double | Si \(n\) est multiplié par 10 |
|---|---|---|
| \(O(1)\) | inchangé | inchangé |
| \(O(\log n)\) | +1 opération | +3,3 environ |
| \(O(n)\) | ×2 | ×10 |
| \(O(n\log n)\) | un peu plus de ×2 | environ ×13 (de 1 000 à 10 000 : 13,33) |
| \(O(n^2)\) | ×4 | ×100 |
| \(O(2^n)\) | élevé au carré | gigantesque |

Pour \(O(2^n)\) : passer de \(n\) à \(n+1\) **double** déjà le coût.

## V. De l'opération à la durée

Durée = nombre d'opérations ÷ vitesse (opérations par seconde). Avec l'**hypothèse** d'un milliard d'opérations par seconde (ordre de grandeur, à vérifier sur la machine réelle) :

- \(2^{60}\) opérations \(\approx 1{,}153 \times 10^{18}\), soit \(\approx 1{,}153 \times 10^9\) s, environ **36,5 ans** (13 344 jours).

**Test flash.** Un algorithme \(O(n^2)\) met 2 s pour \(n = 1000\). Combien de temps pour \(n = 10\,000\) (même machine) ?

<details markdown="1">
<summary>Voir la réponse</summary>

Facteur \(10^2 = 100\) : environ 200 s.

</details>

## À retenir

- \(f = O(g)\) : \(f \le c\,g\) à partir d'un certain rang.
- On enlève les constantes et on garde le terme dominant.
- Classes : \(1 < \log n < n < n\log n < n^2 < 2^n\).
- Les durées calculées reposent sur une **hypothèse de vitesse** : à toujours annoncer.

# Cours – Mesurer, et connaître les limites

*BTS SIO SISR 2e année – Pour aller plus loin – S15 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** classes de complexité (S13) ; factorielle et puissances.
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Mesurer** le temps d'une fonction avec `time.perf_counter` ;
- [ ] **Faire** un test de doublement pour estimer un ordre de croissance ;
- [ ] **Évaluer** le coût d'une recherche exhaustive ;
- [ ] **Reconnaître** une explosion factorielle ou exponentielle ;
- [ ] **Citer** deux améliorations classiques (ensemble, mémoïsation).

## I. Mesurer le temps

```python
import time

debut = time.perf_counter()
resultat = ma_fonction(donnees)
duree = time.perf_counter() - debut
```

Une seule mesure est peu fiable (autres processus, cache). On **répète** et on garde le **minimum**, moins perturbé que la moyenne.

> [!WARNING]
> Les durées mesurées dépendent de la machine, de la version de Python et de la charge. Elles ne se comparent qu'entre elles, sur la même machine.

## II. Le test de doublement

On mesure le temps pour \(n\), puis pour \(2n\), puis \(4n\)... Le rapport \(t(2n)/t(n)\) indique l'ordre :

| Rapport proche de | Ordre probable |
|---|---|
| 1 | \(O(1)\) ou \(O(\log n)\) |
| 2 | \(O(n)\) ou \(O(n\log n)\) |
| 4 | \(O(n^2)\) |
| 8 | \(O(n^3)\) |

C'est une **estimation expérimentale** : elle complète l'analyse, elle ne la remplace pas.

## III. Explosion exponentielle : la force brute

La **force brute** essaie toutes les possibilités.

| Cas | Nombre d'essais |
|---|---|
| Mot de passe de 8 lettres minuscules | \(26^8 = 208\,827\,064\,576\) |
| 12 lettres minuscules | \(26^{12} = 95\,428\,956\,661\,682\,176\) |
| 12 caractères parmi 62 (lettres, chiffres) | \(62^{12} = 3\,226\,266\,762\,397\,899\,821\,056\) |

Avec l'**hypothèse** d'un milliard d'essais par seconde : \(26^8\) demande \(\approx 209\) s, \(26^{12}\) demande \(\approx 3{,}03\) ans.

**Tournées (voyageur de commerce).** Visiter \(n\) sites en revenant au départ : en fixant le premier, il y a \((n-1)!\) ordres possibles.

| \(n\) | 8 | 10 | 15 | 20 |
|---|---|---|---|---|
| \((n-1)!\) | 5 040 | 362 880 | 87 178 291 200 | 121 645 100 408 832 000 |

Passer de 15 à 20 sites multiplie le nombre d'ordres par plus d'un million.

## IV. Gagner du temps

1. **Changer de structure.** Chercher les doublons avec un **ensemble** : `len(set(L)) < len(L)`. Un test d'appartenance à un ensemble est, en moyenne, en temps quasi constant (pour les types hachables), d'où un coût de l'ordre de \(O(n)\) au lieu de \(O(n^2)\).
2. **Mémoïser.** Garder en mémoire les résultats déjà calculés pour ne pas les recalculer (vu en S08).
3. **Réduire l'espace de recherche.** Éliminer tôt les possibilités impossibles.

**Test flash.** Combien d'ordres de visite pour 9 sites (premier fixé) ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(8! = 40\,320\).

</details>

## À retenir

- On mesure en répétant et en gardant le minimum.
- Test de doublement : rapport \(\approx 2\) pour linéaire, \(\approx 4\) pour quadratique.
- Force brute : \(a^L\) essais ; tournées : \((n-1)!\).
- Toute durée annoncée suppose une **vitesse hypothétique**.

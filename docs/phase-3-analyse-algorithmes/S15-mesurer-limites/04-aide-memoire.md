# Aide-mémoire – Mesurer et limites

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S15*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Mesure

```python
import time
d = time.perf_counter()
f()
duree = time.perf_counter() - d
```

Répéter, garder le **minimum**. Comparer seulement sur la même machine.

## Test de doublement

Rapport \(t(2n)/t(n)\) : \(\approx 2\) linéaire, \(\approx 4\) quadratique, \(\approx 8\) cubique.

## Explosions

| Situation | Nombre |
|---|---|
| Force brute | \(a^L\) |
| Tournées | \((n-1)!\) |
| Durée | \(\dfrac{\text{essais}}{\text{vitesse}}\) (hypothèse annoncée) |

## Gagner du temps

Ensemble (`set`), mémoïsation, réduction de l'espace de recherche.

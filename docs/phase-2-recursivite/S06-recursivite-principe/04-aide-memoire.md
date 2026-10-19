# Aide-mémoire – Récursivité : principe

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S06*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Structure

```python
def f(donnee):
    if cas_de_base:
        return resultat_direct
    return combiner(f(donnee_plus_petite))
```

| Ingrédient | Question à se poser |
|---|---|
| Cas de base | Quel est le plus petit problème, résolu directement ? |
| Cas récursif | Comment passer à un problème plus petit ? |
| Variant | Quel entier décroît strictement et reste \(\ge 0\) ? |

## Modèles

| Problème | Cas de base | Cas récursif |
|---|---|---|
| \(n!\) | \(0! = 1\) | \(n \times (n-1)!\) |
| \(1 + \dots + n\) | \(0\) | \(n + S(n-1)\) |
| \(x^n\) | \(1\) | \(x \times x^{n-1}\) |
| PGCD | \(b = 0\) : \(a\) | `pgcd(b, a % b)` |
| Binaire de \(n\) | \(n < 2\) : `str(n)` | `binaire(n // 2) + str(n % 2)` |

## Pièges

- Pas de cas de base ou appel qui ne se rapproche pas : `RecursionError`.
- `fact(n)` : \(n + 1\) appels. Profondeur limitée (environ 1 000 par défaut en Python).
- Récursif et itératif donnent le même résultat ; l'itératif ne risque pas la limite de profondeur.

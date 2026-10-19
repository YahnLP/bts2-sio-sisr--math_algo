# Aide-mémoire – Diviser pour régner

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S09*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Principe

Diviser (moitiés) → résoudre → combiner. Environ \(\log_2 n\) niveaux.

## Dichotomie (liste **triée**)

`milieu = (bas + haut) // 2` ; égal : trouvé ; plus petit : `bas = milieu + 1` ; plus grand : `haut = milieu - 1` ; `bas > haut` : absent. Au plus \(\lfloor \log_2 n \rfloor + 1\) comparaisons (10 pour 1 000, 20 pour un million).

## Puissance rapide

| \(n\) | Calcul |
|---|---|
| 0 | 1 |
| pair | \(y = x^{n/2}\) (calculé **une fois**), puis \(y^2\) |
| impair | \(x \cdot x^{n-1}\) |

\(x^{1000}\) : 15 multiplications.

## Tri fusion

`fusion(A, B)` : deux indices, on prend le plus petit des deux fronts, puis on recopie le reste. `tri_fusion(L)` : cas de base `len(L) <= 1`, sinon fusion des deux moitiés triées. Environ \(n \log_2 n\) comparaisons ; \(2n - 1\) appels.

## Pièges

Dichotomie sur liste non triée ; appel dupliqué sur `n // 2` ; oublier le reste à recopier dans la fusion.

# Exercices – Méthode

*BTS SIO SISR 2e année – Mathématiques approfondies et algorithmique – S18*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, puis ouvre « Voir la réponse ». **Aucune réponse sans justification** n'est complète.

## Exercice 1 – Analyser un énoncé

« Une liste de relevés `(machine, temperature)` est donnée. Renvoyer les machines dont la température maximale dépasse un seuil. » Préciser entrées, sorties, un exemple et un cas limite.

<details markdown="1">
<summary>Voir la réponse</summary>

Entrées : liste de couples, un seuil. Sortie : liste de machines (sans doublon, triée). Exemple : `[("m1", 40), ("m2", 70), ("m1", 80)]`, seuil 75 : `["m1"]`. Cas limite : liste vide, donc `[]`.

</details>

## Exercice 2 – Décomposer

Proposer une décomposition en fonctions pour l'exercice 1.

<details markdown="1">
<summary>Voir la réponse</summary>

`maxima(releves)` : dictionnaire machine → température maximale ; `machines_chaudes(releves, seuil)` : machines dont le maximum dépasse le seuil, triées.

</details>

## Exercice 3 – Choisir

Pour l'exercice 1 avec \(10^6\) relevés, comparer deux méthodes : balayer la liste à chaque machine, ou un dictionnaire.

<details markdown="1">
<summary>Voir la réponse</summary>

Avec \(m\) machines distinctes, balayer à chaque machine coûte de l'ordre de \(m \times n\). Un dictionnaire coûte de l'ordre de \(n\) : un seul passage.

</details>

## Exercice 4 – Concevoir des tests

Écrire cinq tests pour `suspectes` du cours.

<details markdown="1">
<summary>Voir la réponse</summary>

Liste vide ; une ligne `ECHEC` avec seuil 1 ; une ligne `OK` avec seuil 1 (résultat vide) ; deux adresses à égalité de seuil (ordre trié) ; une adresse avec `OK` puis `ECHEC` pour vérifier qu'on ne compte que les échecs.

</details>

## Exercice 5 – Justification

Rédiger en trois phrases la justification de `echecs_par_ip`.

<details markdown="1">
<summary>Voir la réponse</summary>

Idée : un dictionnaire adresse → échecs, mis à jour à chaque ligne. Invariant : après \(k\) lignes, il contient les échecs de ces \(k\) lignes. Coût : un passage, de l'ordre de \(n\) opérations.

</details>

## Exercice 6 – Corriger une erreur

La fonction ci-dessous doit compter les échecs ; elle renvoie un résultat faux pour `["a;OK"]`. Pourquoi ?

```python
def echecs(lignes):
    d = {}
    for l in lignes:
        ip = l.split(";")[0]
        d[ip] = d.get(ip, 0) + 1
    return d
```

<details markdown="1">
<summary>Voir la réponse</summary>

Elle compte **toutes** les lignes, pas seulement celles dont le statut est `ECHEC` : elle renvoie `{"a": 1}` au lieu de `{}`. Le test avec une ligne `OK` l'aurait révélé.

</details>

## Je sais faire

- [ ] Analyser un énoncé
- [ ] Décomposer en fonctions
- [ ] Choisir une structure et estimer le coût
- [ ] Rédiger une justification

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________

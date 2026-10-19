# Mathématiques et algorithmique approfondies – BTS SIO SISR 2e année

Cours, exercices corrigés, TP Python et aide-mémoire des **19 séances** de mathématiques approfondies et d'algorithmique de 2e année (option SISR). Suite du dépôt de 1re année `bts1-sio-sisr-math_algo`.

Auteur : **Yahn LE PRETTRE** – Formateur. Licence **CC BY-NC-SA 4.0** (voir `LICENSE`).

> **Contenu proposé par l'enseignant, à valider** : le programme officiel de la 2e année n'a pas été relu pour ce dépôt (voir `docs/ressources/programme-2a.md`).

## Contenu

| Phase | Séances | Thèmes |
|---|---|---|
| 1 – Suites numériques | S01–S05 | Définition, suites arithmétiques et géométriques, applications, limites |
| 2 – Récursivité | S06–S10 | Principe, pile d'appels, tableaux, diviser pour régner, arbres |
| 3 – Analyse d'algorithmes | S11–S15 | Terminaison, coût, complexité, tris, mesures |
| 4 – Algorithmique avancée et épreuve | S16–S19 | Structures de données, graphes en Python, méthode, épreuve blanche |

## Avancement

| Séances | État |
|---|---|
| S01 à S05 (phase 1) | Rédigées (fiche, cours, exercices, TP Python, aide-mémoire, corrigé) ; **à valider** |
| S06 à S10 (phase 2) | Rédigées (fiche, cours, exercices, TP Python, aide-mémoire, corrigé) ; **à valider** |
| S11 à S15 (phase 3) | Rédigées (fiche, cours, exercices, TP Python, aide-mémoire, corrigé) ; **à valider** |
| S16 à S19 (phase 4) | Rédigées (fiche, cours, exercices, TP Python, aide-mémoire, corrigé) ; S19 : sujet blanc de l'auteur avec barème ; **à valider** |

## Travailler en local

```bash
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000
mkdocs build --strict # même vérification que la publication
```

## Organisation du dépôt

| Dossier | Rôle |
|---|---|
| `docs/` | Pages du site (phases, séances, ressources) |
| `docs/<phase>/<séance>/` | Fiche, cours, exercices, TP, aide-mémoire, scripts Python et tests |
| `corriges/` | Corrigés des séances (hors site) |
| `includes/abbr.md` | Infobulles des sigles, **généré** par `scripts/gen_glossaire.py` |
| `scripts/` | Génération du glossaire et du formulaire |
| `my_theme_customizations/` | Éditeur Python intégré (Pyodide) |
| `tools/CONVENTIONS.md` | Règles d'écriture du cours |

Après avoir modifié `scripts/glossaire_data.py` ou un aide-mémoire :

```bash
python3 scripts/gen_glossaire.py
python3 scripts/gen_formulaire.py
```

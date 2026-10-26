# Exercices – Fiabilité

*BTS SIO SISR 2e année – Option mathématiques approfondies – M5*

> [!NOTE]
> Trois niveaux : **socle**, **format épreuve**, **pour aller plus loin**. Les valeurs sont données à \(10^{-4}\) près. Les composants sont indépendants.

## Niveau 1 – Socle

### Exercice 1 – Un disque dur

La durée de vie \(T\) d'un disque suit une loi exponentielle de **MTBF** \(2\,000\) h, donc \(\lambda = \dfrac{1}{2000} = 0{,}0005\) h\(^{-1}\).

1. Calculer la probabilité qu'il fonctionne encore à 1 000 h.
2. Calculer la probabilité qu'il tombe en panne avant 500 h.
3. Calculer la durée médiane de fonctionnement.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(R(1000) = e^{-0{,}0005 \times 1000} = e^{-0{,}5} \approx 0{,}6065\).
2. \(P(T \le 500) = 1 - e^{-0{,}25} \approx 0{,}2212\).
3. \(t_{1/2} = \dfrac{\ln 2}{\lambda} = 2000 \ln 2 \approx 1\,386\) h. La médiane est inférieure à la MTBF (2 000 h) : la moitié des disques tombe en panne avant 1 386 h.

</details>

### Exercice 2 – Sans mémoire

Avec le disque de l'exercice 1, quelle est la probabilité qu'il dure au moins 1 500 h de plus, sachant qu'il a déjà fonctionné 500 h ? Comparer avec la probabilité qu'un disque neuf dure 1 000 h. Que dit ce résultat ?

<details markdown="1">
<summary>Voir la réponse</summary>

Propriété sans mémoire : \(P(T > 1500 \mid T > 500) = P(T > 1000) = e^{-0{,}5} \approx 0{,}6065\).

Calcul direct : \(\dfrac{R(1500)}{R(500)} = \dfrac{e^{-0{,}75}}{e^{-0{,}25}} = e^{-0{,}5}\). La loi exponentielle ne tient pas compte de l'âge : le modèle suppose qu'il n'y a **pas de vieillissement**. C'est une hypothèse à discuter pour un disque réel.

</details>

## Niveau 2 – Format épreuve

### Exercice 3 – Série et parallèle

On installe deux disques identiques de l'exercice 1. À \(t = 1000\) h, la fiabilité de chacun est \(0{,}6065\).

1. Calculer la fiabilité si les deux sont montés **en série** (le service tombe si l'un tombe).
2. La calculer s'ils sont montés **en parallèle** (miroir).
3. Quelle est la MTBF en série ? en parallèle ?
4. Commenter.

<details markdown="1">
<summary>Voir la réponse</summary>

1. Série : \(R = 0{,}6065^{2} = e^{-1} \approx 0{,}3679\).
2. Parallèle : \(R = 1 - (1 - 0{,}6065)^{2} \approx 0{,}8452\).
3. En série, le taux vaut \(2\lambda\) : MTBF \(= \dfrac{2000}{2} = 1\,000\) h. En parallèle : MTBF \(= \dfrac{3}{2\lambda} = 3\,000\) h.
4. Passer d'un disque seul (\(0{,}6065\)) à un miroir fait gagner environ 24 points de fiabilité à 1 000 h, alors que le montage en série la fait perdre. La redondance **augmente** la fiabilité, les dépendances en série la **diminuent**.

</details>

### Exercice 4 – Système mixte

Une application dépend d'un serveur A en **série** avec un bloc de deux serveurs B et C **en parallèle**. À 1 000 h, chaque serveur a une fiabilité de \(0{,}6065\).

1. Calculer la fiabilité du bloc \(\{B, C\}\).
2. En déduire la fiabilité du système.
3. Quel serveur faudrait-il dupliquer en priorité pour améliorer le système ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. Bloc parallèle : \(1 - (1 - 0{,}6065)^2 \approx 0{,}8452\).
2. Série : \(R = 0{,}6065 \times 0{,}8452 \approx 0{,}5126\).
3. Le **serveur A** est le maillon faible : il est seul en série et limite le système à \(0{,}6065\) au mieux. Le dupliquer donnerait un second bloc parallèle (\(0{,}8452\)) et un système à \(0{,}8452^2 \approx 0{,}7143\).

</details>

### Exercice 5 – Disponibilité

Un équipement a une MTBF de \(2\,000\) h et un MTTR de \(8\) h.

1. Calculer sa disponibilité.
2. En déduire le temps d'arrêt annuel (8 760 h).
3. Le contrat exige 99,9 % : est-il respecté ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(A = \dfrac{2000}{2000 + 8} = \dfrac{2000}{2008} \approx 0{,}9960\), soit \(99{,}60\) %.
2. Arrêt annuel : \(8760 \times (1 - 0{,}99602) \approx 34{,}9\) h.
3. Non : \(99{,}60\) % \(< 99{,}9\) %. Le contrat autorise environ \(8{,}8\) h d'arrêt par an. Il faut réduire le MTTR (maintenance plus rapide) ou augmenter la MTBF (redondance).

</details>

## Niveau 3 – Pour aller plus loin

### Exercice 6 – Combien de redondances ?

Chaque serveur a une fiabilité de \(0{,}6065\) à 1 000 h. Combien de serveurs en parallèle faut-il pour que la fiabilité du bloc dépasse \(0{,}99\) ? Proposer une fonction Python qui renvoie ce nombre.

<details markdown="1">
<summary>Voir la réponse</summary>

On veut \(1 - q^{n} \ge 0{,}99\) avec \(q = 1 - 0{,}6065 = 0{,}3935\), soit \(q^{n} \le 0{,}01\), donc \(n \ge \dfrac{\ln 0{,}01}{\ln 0{,}3935} \approx 4{,}94\). Il faut **5 serveurs**.

Contrôle : \(n = 4\) donne \(1 - 0{,}3935^{4} \approx 0{,}976\) (insuffisant) ; \(n = 5\) donne \(\approx 0{,}9906\).

```python
def nb_serveurs(r, objectif):
    q = 1 - r          # probabilité de panne d'un serveur
    n = 1
    while 1 - q ** n < objectif:
        n += 1
    return n

print(nb_serveurs(0.6065, 0.99))   # 5
```

Remarque : cinq serveurs coûtent cher ; au-delà d'un certain nombre, le gain devient marginal, et l'hypothèse d'indépendance des pannes devient décisive.

</details>

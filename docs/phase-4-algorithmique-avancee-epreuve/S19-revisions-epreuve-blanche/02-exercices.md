# Sujet blanc – Mathématiques approfondies et algorithmique

*BTS SIO SISR 2e année – S19 – **sujet de l'auteur, non officiel***

> [!WARNING]
> **Ce sujet a été rédigé pour s'entraîner.** Il n'est pas un sujet d'examen officiel et ne reproduit pas le format d'une épreuve précise. Il n'a pas de réponses sur cette page : la correction est remise par l'enseignant.

**Durée conseillée : 2 heures.** **Barème : 30 points** (A : 10 points, B : 10 points, C : 10 points). Calculatrice autorisée. L'éditeur Python du [TP](03-tp-python.md) sert aux questions de programmation (dossier C) et à vérifier tes fonctions des dossiers A et B.

---

## Dossier A – Croissance des journaux (10 points)

Un serveur conserve ses journaux. Au 1er janvier, ils occupent 200 Go. Chaque mois, l'espace occupé augmente de 3 %. On note \(u_n\) l'espace occupé (en Go) \(n\) mois après le 1er janvier : \(u_0 = 200\).

**A1. (2 points)** Exprimer \(u_{n+1}\) en fonction de \(u_n\). En déduire la nature de la suite et l'expression de \(u_n\) en fonction de \(n\).

**A2. (2 points)** Calculer \(u_{12}\), arrondi au centième.

**A3. (3 points)** Le disque est saturé quand l'espace occupé dépasse 300 Go. Déterminer le plus petit entier \(n\) tel que \(u_n > 300\). Justifier.

**A4. (3 points)** Écrire en Python une fonction `mois_seuil(u0, taux, seuil)` qui renvoie le plus petit entier \(n\) tel que \(u_n > \text{seuil}\), pour une suite qui augmente de `taux` (en proportion, par exemple `0.03`) à chaque mois. Expliquer pourquoi la boucle s'arrête.

---

## Dossier B – Récursivité et coût (10 points)

**B1. (3 points)** Écrire une fonction **récursive** `somme_rec(L)` qui renvoie la somme des éléments d'une liste `L`. Préciser le cas de base, l'appel récursif et le variant.

**B2. (2 points)** Représenter les appels successifs (pile d'appels) pour `somme_rec([4, 1, 3])`. Donner le résultat.

**B3. (2 points)** La fonction naïve `fib(n)` (qui renvoie `n` si `n < 2`, sinon `fib(n-1) + fib(n-2)`) fait \(C(n)\) appels, avec \(C(0) = C(1) = 1\) et \(C(n) = C(n-1) + C(n-2) + 1\). Calculer \(C(5)\).

**B4. (3 points)**

a) Un algorithme A effectue \(50n\) opérations et un algorithme B effectue \(n^2\) opérations sur des données de taille \(n\). À partir de quelle valeur de \(n\) l'algorithme B effectue-t-il **strictement plus** d'opérations que A ?

b) Dans une liste **triée** de 1 000 000 d'éléments, combien de comparaisons au plus pour une recherche dichotomique ? Pour une recherche séquentielle ?

---

## Dossier C – Réseau (10 points)

Un réseau relie cinq routeurs. Les liaisons sont orientées ; le nombre indiqué est la latence en ms.

<figure class="graphe">
<svg viewBox="0 0 540 200" role="img" aria-label="Réseau de cinq routeurs avec latences" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="rx-n" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-n"/></marker>
<marker id="rx-arbre" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-arbre"/></marker>
<marker id="rx-ignore" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-ignore"/></marker>
</defs>
<line x1="80.7" y1="87.4" x2="184.7" y2="49.3" class="arete n" marker-end="url(#rx-n)"/>
<text x="130.2" y="59.4" class="poids" text-anchor="middle">3</text>
<line x1="80.7" y1="102.6" x2="184.7" y2="140.7" class="arete n" marker-end="url(#rx-n)"/>
<text x="130.2" y="140.6" class="poids" text-anchor="middle">1</text>
<line x1="210.0" y1="128.0" x2="210.0" y2="67.0" class="arete n" marker-end="url(#rx-n)"/>
<text x="196.0" y="100.0" class="poids" text-anchor="middle">1</text>
<line x1="230.5" y1="48.0" x2="324.9" y2="85.1" class="arete n" marker-end="url(#rx-n)"/>
<text x="285.1" y="59.5" class="poids" text-anchor="middle">2</text>
<line x1="230.5" y1="142.0" x2="324.9" y2="104.9" class="arete n" marker-end="url(#rx-n)"/>
<text x="285.1" y="140.5" class="poids" text-anchor="middle">6</text>
<line x1="372.0" y1="95.0" x2="453.0" y2="95.0" class="arete n" marker-end="url(#rx-n)"/>
<text x="415.0" y="86.0" class="poids" text-anchor="middle">1</text>
<circle cx="60" cy="95" r="22" class="noeud"/><text x="60" y="101" text-anchor="middle" class="nom">R1</text>
<circle cx="210" cy="40" r="22" class="noeud"/><text x="210" y="46" text-anchor="middle" class="nom">R2</text>
<circle cx="210" cy="150" r="22" class="noeud"/><text x="210" y="156" text-anchor="middle" class="nom">R3</text>
<circle cx="350" cy="95" r="22" class="noeud"/><text x="350" y="101" text-anchor="middle" class="nom">R4</text>
<circle cx="480" cy="95" r="22" class="noeud"/><text x="480" y="101" text-anchor="middle" class="nom">R5</text>
</svg>
<figcaption>Le réseau du dossier C : les nombres sont des latences en ms.</figcaption>
</figure>

**C1. (2 points)** Représenter ce réseau par un dictionnaire Python `rx` qui associe à chaque routeur le dictionnaire de ses voisins et des latences.

**C2. (3 points)** Écrire `sommets_a_k_sauts(g, depart, k)` qui renvoie la liste **triée** des sommets situés à **exactement** `k` sauts de `depart` (plus court chemin en nombre de liaisons, sans tenir compte des latences). Indiquer l'algorithme utilisé et pourquoi.

**C3. (3 points)** Écrire `plus_court_cout(g, a, b)` qui renvoie la latence minimale de `a` à `b`, ou `None` si `b` est inatteignable. Donner la latence minimale de R1 à R5.

**C4. (2 points)** Expliquer pourquoi le parcours en largeur ne suffit pas pour C3, et ce qui change si une liaison avait une latence négative.

---

*Fin du sujet.*

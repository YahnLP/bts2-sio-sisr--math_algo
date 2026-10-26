# Cours – Graphes en Python : parcours et plus court chemin

*BTS SIO SISR 2e année – Pour aller plus loin – S17 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** file (`deque`) et dictionnaire (S16) ; parcours en profondeur (S10) ; graphes de la 1re année.
> - **Outils :** Papier, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Représenter** un graphe orienté, pondéré ou non ;
- [ ] **Écrire** un parcours en largeur ;
- [ ] **Écrire** l'algorithme de Dijkstra ;
- [ ] **Évaluer** leur complexité ;
- [ ] **Tester** sur un petit réseau.

## I. Représenter un graphe

Graphe **non pondéré** : dictionnaire sommet → liste de voisins (comme en S10).

```python
g = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": ["A"]}
```

<figure class="graphe">
<svg viewBox="0 0 420 230" role="img" aria-label="Graphe orienté à cinq sommets A à E" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="g-n" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-n"/></marker>
<marker id="g-arbre" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-arbre"/></marker>
<marker id="g-ignore" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-ignore"/></marker>
</defs>
<line x1="90.5" y1="82.0" x2="184.9" y2="44.9" class="arete n" marker-end="url(#g-n)"/>
<line x1="90.5" y1="98.0" x2="184.9" y2="135.1" class="arete n" marker-end="url(#g-n)"/>
<line x1="232.0" y1="35.0" x2="323.0" y2="35.0" class="arete n" marker-end="url(#g-n)"/>
<line x1="227.3" y1="131.4" x2="328.8" y2="51.7" class="arete n" marker-end="url(#g-n)"/>
<line x1="232.0" y1="145.0" x2="323.0" y2="145.0" class="arete n" marker-end="url(#g-n)"/>
<path d="M331.5,156.9 Q210,235 88.8,109.4" class="arete n" marker-end="url(#g-n)"/>
<circle cx="70" cy="90" r="22" class="noeud"/><text x="70" y="96" text-anchor="middle" class="nom">A</text>
<circle cx="210" cy="35" r="22" class="noeud"/><text x="210" y="41" text-anchor="middle" class="nom">B</text>
<circle cx="210" cy="145" r="22" class="noeud"/><text x="210" y="151" text-anchor="middle" class="nom">C</text>
<circle cx="350" cy="35" r="22" class="noeud"/><text x="350" y="41" text-anchor="middle" class="nom">D</text>
<circle cx="350" cy="145" r="22" class="noeud"/><text x="350" y="151" text-anchor="middle" class="nom">E</text>
</svg>
<figcaption>Le graphe <code>g</code> : une flèche va d'un sommet vers l'un de ses voisins. Le cycle A → C → E → A est celui qui oblige à mémoriser les sommets visités.</figcaption>
</figure>

Graphe **pondéré** : dictionnaire sommet → dictionnaire voisin → poids (coût d'une liaison : latence en ms, distance...).

```python
gp = {"A": {"B": 4, "C": 1}, "B": {"D": 1}, "C": {"B": 2, "D": 5}, "D": {}}
```

<figure class="graphe">
<svg viewBox="0 0 440 200" role="img" aria-label="Graphe pondéré à quatre sommets" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="gp-n" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-n"/></marker>
<marker id="gp-arbre" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-arbre"/></marker>
<marker id="gp-ignore" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-ignore"/></marker>
</defs>
<line x1="91.0" y1="83.4" x2="204.2" y2="48.1" class="arete n" marker-end="url(#gp-n)"/>
<text x="145.8" y="56.6" class="poids" text-anchor="middle">4</text>
<line x1="90.6" y1="97.7" x2="204.7" y2="140.5" class="arete n" marker-end="url(#gp-n)"/>
<text x="145.1" y="138.1" class="poids" text-anchor="middle">1</text>
<line x1="250.7" y1="47.6" x2="354.7" y2="85.7" class="arete n" marker-end="url(#gp-n)"/>
<text x="309.8" y="59.4" class="poids" text-anchor="middle">1</text>
<line x1="230.0" y1="128.0" x2="230.0" y2="67.0" class="arete n" marker-end="url(#gp-n)"/>
<text x="214.0" y="100.0" class="poids" text-anchor="middle">2</text>
<line x1="250.7" y1="142.4" x2="354.7" y2="104.3" class="arete n" marker-end="url(#gp-n)"/>
<text x="309.8" y="140.6" class="poids" text-anchor="middle">5</text>
<circle cx="70" cy="90" r="22" class="noeud"/><text x="70" y="96" text-anchor="middle" class="nom">A</text>
<circle cx="230" cy="40" r="22" class="noeud"/><text x="230" y="46" text-anchor="middle" class="nom">B</text>
<circle cx="230" cy="150" r="22" class="noeud"/><text x="230" y="156" text-anchor="middle" class="nom">C</text>
<circle cx="380" cy="95" r="22" class="noeud"/><text x="380" y="101" text-anchor="middle" class="nom">D</text>
</svg>
<figcaption>Le graphe pondéré <code>gp</code> : le nombre sur une flèche est son poids (par exemple une latence en ms).</figcaption>
</figure>

## II. Parcours en largeur (BFS)

Le **parcours en largeur** visite d'abord les voisins du départ, puis les voisins des voisins, etc. Il utilise une **file**.

```python
from collections import deque

def bfs(g, depart):
    vus = [depart]
    file = deque([depart])
    while file:
        s = file.popleft()
        for v in g[s]:
            if v not in vus:
                vus.append(v)
                file.append(v)
    return vus
```

Depuis `"A"` dans `g` : `["A", "B", "C", "D", "E"]`. Les sommets sont visités par **distance croissante** (en nombre de liaisons) : c'est ce qui donne le **plus court chemin en nombre de sauts**, ce que le parcours en profondeur ne garantit pas.

Pour retrouver un chemin, on mémorise le **parent** de chaque sommet à sa première découverte, puis on remonte du but vers le départ.

> [!NOTE]
> La liste `vus` rend le test `v not in vus` coûteux ; avec un ensemble (`set`) il devient \(O(1)\) en moyenne. Le nombre d'opérations est de l'ordre de \(n + m\) (sommets plus liaisons), d'après l'analyse classique du parcours en largeur.

## III. Plus court chemin pondéré : Dijkstra

Quand les liaisons ont un **coût positif ou nul**, on utilise l'algorithme de **Dijkstra** :

1. distance du départ = 0, les autres = infini ;
2. on prend le sommet non traité de **plus petite distance** ;
3. on met à jour (on **relâche**) la distance de ses voisins : `d[v] = min(d[v], d[s] + poids)` ;
4. on recommence jusqu'à épuisement.

```python
import heapq

def dijkstra(g, depart):
    dist = {depart: 0}
    tas = [(0, depart)]
    while tas:
        d, s = heapq.heappop(tas)
        if d > dist[s]:
            continue
        for v, w in g[s].items():
            nd = d + w
            if v not in dist or nd < dist[v]:
                dist[v] = nd
                heapq.heappush(tas, (nd, v))
    return dist
```

*Trace sur `gp` depuis A.*

| Étape | Sommet traité | Distances connues |
|---|---|---|
| 0 | | A = 0 |
| 1 | A | B = 4, C = 1 |
| 2 | C (1) | B = 3 (via C), D = 6 |
| 3 | B (3) | D = 4 (via B) |
| 4 | D (4) | rien à améliorer |

Résultat : `{"A": 0, "C": 1, "B": 3, "D": 4}`. Le plus court chemin de A à D est A → C → B → D, de coût 4.

<figure class="graphe">
<svg viewBox="0 0 440 200" role="img" aria-label="Plus courts chemins depuis A" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="dij-n" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-n"/></marker>
<marker id="dij-arbre" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-arbre"/></marker>
<marker id="dij-ignore" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="fleche-ignore"/></marker>
</defs>
<line x1="91.0" y1="83.4" x2="204.2" y2="48.1" class="arete ignore" marker-end="url(#dij-ignore)"/>
<text x="145.8" y="56.6" class="poids" text-anchor="middle">4</text>
<line x1="90.6" y1="97.7" x2="204.7" y2="140.5" class="arete arbre" marker-end="url(#dij-arbre)"/>
<text x="145.1" y="138.1" class="poids" text-anchor="middle">1</text>
<line x1="250.7" y1="47.6" x2="354.7" y2="85.7" class="arete arbre" marker-end="url(#dij-arbre)"/>
<text x="309.8" y="59.4" class="poids" text-anchor="middle">1</text>
<line x1="230.0" y1="128.0" x2="230.0" y2="67.0" class="arete arbre" marker-end="url(#dij-arbre)"/>
<text x="214.0" y="100.0" class="poids" text-anchor="middle">2</text>
<line x1="250.7" y1="142.4" x2="354.7" y2="104.3" class="arete ignore" marker-end="url(#dij-ignore)"/>
<text x="309.8" y="140.6" class="poids" text-anchor="middle">5</text>
<circle cx="70" cy="90" r="22" class="noeud"/><text x="70" y="96" text-anchor="middle" class="nom">A</text>
<circle cx="88" cy="72" r="10" class="badge"/><text x="88" y="76" text-anchor="middle" class="num">0</text>
<circle cx="230" cy="40" r="22" class="noeud"/><text x="230" y="46" text-anchor="middle" class="nom">B</text>
<circle cx="248" cy="22" r="10" class="badge"/><text x="248" y="26" text-anchor="middle" class="num">3</text>
<circle cx="230" cy="150" r="22" class="noeud"/><text x="230" y="156" text-anchor="middle" class="nom">C</text>
<circle cx="248" cy="132" r="10" class="badge"/><text x="248" y="136" text-anchor="middle" class="num">1</text>
<circle cx="380" cy="95" r="22" class="noeud"/><text x="380" y="101" text-anchor="middle" class="nom">D</text>
<circle cx="398" cy="77" r="10" class="badge"/><text x="398" y="81" text-anchor="middle" class="num">4</text>
</svg>
<figcaption>Résultat de Dijkstra depuis A : le numéro est la distance minimale. Le chemin le plus court de A à D est A → C → B → D (1 + 2 + 1 = 4) ; les flèches grises ne servent pas.</figcaption>
</figure>

> [!WARNING]
> Dijkstra suppose des poids **positifs ou nuls**. Avec un poids négatif, la distance d'un sommet déjà traité peut encore baisser : l'algorithme n'est plus correct.

Un tas (`heapq`) donne un coût de l'ordre de \((n + m)\log n\), d'après l'analyse classique de l'algorithme.

## IV. Choisir

| Besoin | Algorithme |
|---|---|
| Atteindre / explorer | profondeur ou largeur |
| Plus court en **nombre de sauts** | largeur |
| Plus court en **coût** (poids \(\ge 0\)) | Dijkstra |

**Test flash.** Quelle est la distance de A à D dans `gp` si le poids de C → B passe de 2 à 5 ?

<details markdown="1">
<summary>Voir la réponse</summary>

Trois chemins : A → B → D = 4 + 1 = 5 ; A → C → B → D = 1 + 5 + 1 = 7 ; A → C → D = 1 + 5 = 6. Minimum : **5**.

</details>

## À retenir

- Largeur : file, plus court en nombre de sauts.
- Dijkstra : plus court en coût, poids \(\ge 0\), on traite le sommet de distance minimale.
- On retrouve le chemin grâce aux parents.

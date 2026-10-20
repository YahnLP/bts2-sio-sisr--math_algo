# Corrigé S18

## Exercices

1. Entrées, sortie et exemple précisés.
2. `maxima` puis `machines_chaudes`.
3. \(m \times n\) contre \(n\).
4. Vide, un ​échec, un OK, égalité, mélange OK/ECHEC.
5. Idée, invariant, coût.
6. Elle compte aussi les `OK`.

## TP Python – solutions

```python
def parse_ligne(ligne):
    ip, statut = ligne.split(";")
    return (ip.strip(), statut.strip())

def parse_ligne(ligne):
    ip, statut = ligne.split(";")
    return (ip.strip(), statut.strip())


def echecs_par_ip(lignes):
    d = {}
    for l in lignes:
        ip, statut = parse_ligne(l)
        if statut == "ECHEC":
            d[ip] = d.get(ip, 0) + 1
    return d

def parse_ligne(ligne):
    ip, statut = ligne.split(";")
    return (ip.strip(), statut.strip())


def echecs_par_ip(lignes):
    d = {}
    for l in lignes:
        ip, statut = parse_ligne(l)
        if statut == "ECHEC":
            d[ip] = d.get(ip, 0) + 1
    return d


def suspectes(lignes, seuil):
    d = echecs_par_ip(lignes)
    return sorted(ip for ip in d if d[ip] >= seuil)

def rafale(lignes, ip, k):
    serie = 0
    for l in lignes:
        adresse, statut = l.split(";")
        if adresse.strip() != ip:
            continue
        if statut.strip() == "ECHEC":
            serie = serie + 1
            if serie >= k:
                return True
        else:
            serie = 0
    return False

def rapport(lignes, seuil):
    d = {}
    for l in lignes:
        ip, statut = l.split(";")
        if statut.strip() == "ECHEC":
            ip = ip.strip()
            d[ip] = d.get(ip, 0) + 1
    gardes = [(ip, c) for ip, c in d.items() if c >= seuil]
    gardes.sort(key=lambda t: (-t[1], t[0]))
    return [ip + " : " + str(c) for ip, c in gardes]
```

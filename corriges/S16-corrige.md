# Corrigé S16

## Exercices

1. 3, 4, 2 ; reste `[1]`.
2. `a`, `b` ; reste `c`, `d`.
3. Oui ; non ; non.
4. `{"r": 1, "e": 2, "s": 1, "a": 1, "u": 1}`.
5. ​Ordre de fin : 1, 2, 0.
6. \(10^{10}\) contre ≈ \(10^5\).

## TP Python – solutions

```python
def parentheses_ok(s):
    paires = {")": "(", "]": "[", "}": "{"}
    pile = []
    for c in s:
        if c in "([{":
            pile.append(c)
        elif c in paires:
            if not pile or pile.pop() != paires[c]:
                return False
    return len(pile) == 0

def compte_ip(lignes):
    compte = {}
    for a in lignes:
        compte[a] = compte.get(a, 0) + 1
    return compte

def top_n(compte, n):
    couples = sorted(compte.items(), key=lambda kv: (-kv[1], kv[0]))
    return couples[:n]

from collections import deque


def tourniquet(durees, quantum):
    file = deque((i, d) for i, d in enumerate(durees))
    fin = []
    while file:
        i, reste = file.popleft()
        reste = reste - quantum
        if reste <= 0:
            fin.append(i)
        else:
            file.append((i, reste))
    return fin

def edition(ops):
    pile = []
    for o in ops:
        if o == "ANNULE":
            if pile:
                pile.pop()
        else:
            pile.append(o)
    return pile
```

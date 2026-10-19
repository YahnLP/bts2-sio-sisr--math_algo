assert isinstance(temps_min(lambda: 1, 3), float)
assert temps_min(lambda: sum(range(100)), 5) >= 0
assert (lambda c: (temps_min(lambda: c.append(1), 4), len(c))[1])([]) == 4

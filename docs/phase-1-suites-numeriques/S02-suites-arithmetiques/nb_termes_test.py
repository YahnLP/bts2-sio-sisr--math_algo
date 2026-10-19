assert nb_termes(10, 250, 4) == 61
assert nb_termes(1, 10, 3) == 4
assert nb_termes(5, 4, 1) == 0
assert nb_termes(7, 7, 5) == 1
assert all(nb_termes(a, b, p) == len(range(a, b + 1, p)) for a in range(0, 6) for b in range(0, 20) for p in range(1, 6))

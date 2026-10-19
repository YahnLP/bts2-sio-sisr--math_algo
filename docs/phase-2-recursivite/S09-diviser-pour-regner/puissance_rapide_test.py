assert puissance_rapide(2, 10) == 1024
assert puissance_rapide(3, 0) == 1
assert puissance_rapide(5, 1) == 5
assert puissance_rapide(2, 100) == 2 ** 100
assert all(puissance_rapide(a, b) == a ** b for a in range(-3, 5) for b in range(0, 30))

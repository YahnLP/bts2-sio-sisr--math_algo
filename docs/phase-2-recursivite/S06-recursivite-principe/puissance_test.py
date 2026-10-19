assert puissance(2, 10) == 1024
assert puissance(5, 0) == 1
assert puissance(3, 1) == 3
assert puissance(-2, 3) == -8
assert all(puissance(a, b) == a ** b for a in range(-4, 5) for b in range(0, 12))

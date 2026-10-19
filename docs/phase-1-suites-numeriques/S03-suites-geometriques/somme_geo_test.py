assert somme_geo(1, 2, 9) == 1023
assert somme_geo(3, 2, 10) == 6141
assert somme_geo(5, 1, 4) == 25
assert somme_geo(2, 3, 0) == 2
assert all(somme_geo(a, b, k) == sum(a * b ** j for j in range(k + 1)) for a in range(-3, 4) for b in range(-3, 5) for k in range(0, 8))

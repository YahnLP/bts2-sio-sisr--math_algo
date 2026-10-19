assert somme_carres(0) == 0
assert somme_carres(1) == 1
assert somme_carres(4) == 30
assert all(somme_carres(k) == k * (k + 1) * (2 * k + 1) // 6 for k in range(0, 100))

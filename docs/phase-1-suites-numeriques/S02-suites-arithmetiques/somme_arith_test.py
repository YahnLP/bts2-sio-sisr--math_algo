assert somme_arith(12, 5, 20) == 1302
assert somme_arith(0, 1, 100) == 5050
assert somme_arith(5, 0, 3) == 20
assert somme_arith(100, 25, 29) == 13875
assert all(somme_arith(a, b, k) == sum(a + j * b for j in range(k + 1)) for a in range(-3, 4) for b in range(-3, 4) for k in range(0, 8))

assert ratio_doublement(lambda n: n, 10) == 2.0
assert ratio_doublement(lambda n: n * n, 10) == 4.0
assert ratio_doublement(lambda n: 1, 50) == 1.0
assert abs(ratio_doublement(lambda n: n ** 3, 7) - 8) < 1e-9

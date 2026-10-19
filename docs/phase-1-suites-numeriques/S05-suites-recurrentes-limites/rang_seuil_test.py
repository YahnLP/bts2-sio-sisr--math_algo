assert rang_seuil(lambda x: x + 3, 2, 20, 100) == 6
assert rang_seuil(lambda x: 0.5 * x + 10, 0, 25, 1000) is None
assert rang_seuil(lambda x: 0.5 * x + 10, 0, 19.9, 1000) == 8
assert rang_seuil(lambda x: x, 5, 5, 10) == 0
assert rang_seuil(lambda x: x + 1, 0, 50, 10) is None
assert rang_seuil(lambda x: 0.8 * x + 30, 50, 120, 100) == 6

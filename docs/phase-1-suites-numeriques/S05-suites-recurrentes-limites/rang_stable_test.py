assert rang_stable(lambda x: 0.5 * x + 10, 0, 0.001, 1000) == 14
assert rang_stable(lambda x: x + 1, 0, 0.5, 50) is None
assert rang_stable(lambda x: x, 3, 0.1, 5) == 0
assert rang_stable(lambda x: 0.8 * x + 30, 50, 0.01, 1000) == 35

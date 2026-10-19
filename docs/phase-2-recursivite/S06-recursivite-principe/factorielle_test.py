assert factorielle(0) == 1
assert factorielle(1) == 1
assert factorielle(5) == 120
assert factorielle(10) == 3628800
assert all(factorielle(k) == k * factorielle(k - 1) for k in range(1, 20))

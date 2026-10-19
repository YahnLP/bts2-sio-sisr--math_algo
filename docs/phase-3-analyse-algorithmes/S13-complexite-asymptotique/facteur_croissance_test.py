assert facteur_croissance(lambda n: n, 10, 100) == 10.0
assert facteur_croissance(lambda n: n * n, 10, 100) == 100.0
assert abs(facteur_croissance(lambda n: n * __import__('math').log2(n), 1000, 10000) - 13.33) < 0.01

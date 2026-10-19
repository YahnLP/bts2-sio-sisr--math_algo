assert premiers_termes(lambda x: x + 3, 2, 4) == [2, 5, 8, 11, 14]
assert premiers_termes(lambda x: 2 * x + 1, 1, 4) == [1, 3, 7, 15, 31]
assert premiers_termes(lambda x: x * x, 2, 3) == [2, 4, 16, 256]
assert premiers_termes(lambda x: x, 5, 0) == [5]
assert len(premiers_termes(lambda x: x + 1, 0, 9)) == 10

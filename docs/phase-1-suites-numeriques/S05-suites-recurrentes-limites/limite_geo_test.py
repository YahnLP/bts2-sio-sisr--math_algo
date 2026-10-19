assert limite_geo(3, 0.8) == 0
assert limite_geo(2, 1.05) == '+inf'
assert limite_geo(-2, 3) == '-inf'
assert limite_geo(5, 1) == 5
assert limite_geo(1, -1.5) == 'aucune'
assert limite_geo(0, 7) == 0
assert limite_geo(4, -0.5) == 0
assert limite_geo(4, -1) == 'aucune'

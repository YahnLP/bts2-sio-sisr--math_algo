assert abs(duree_jours(86400, 1) - 1) < 1e-9
assert abs(duree_jours(499999500000, 1e6) - 5.78703) < 1e-4
assert abs(duree_jours(2 ** 60, 1e9) - 13343.9) < 0.1
assert duree_jours(0, 1e9) == 0

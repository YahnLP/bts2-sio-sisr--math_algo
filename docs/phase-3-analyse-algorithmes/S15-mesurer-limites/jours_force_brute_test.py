assert abs(jours_force_brute(26, 8, 1e9) * 86400 - 208.827) < 0.001
assert abs(jours_force_brute(26, 12, 1e9) / 365 - 3.026) < 0.001
assert abs(jours_force_brute(10, 4, 1) - 10000 / 86400) < 1e-9

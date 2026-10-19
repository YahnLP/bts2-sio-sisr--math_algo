assert mois_plein(120, 15, 300) == 12
assert mois_plein(300, 15, 300) == 0
assert mois_plein(0, 7, 20) == 3
assert mois_plein(100, 40, 101) == 1

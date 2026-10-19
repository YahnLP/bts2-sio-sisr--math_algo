assert mois_stockage_plein(200, 10, 50, 1000) == 8
assert mois_stockage_plein(1000, 10, 50, 1000) == 0
assert mois_stockage_plein(100, 0, 25, 200) == 4
assert mois_stockage_plein(10, 100, 1, 100) == 4

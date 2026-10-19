assert mois_seuil(200, 0.03, 300) == 14
assert mois_seuil(200, 0.03, 150) == 0
assert mois_seuil(100, 0.1, 100) == 1
assert mois_seuil(1000, 0.5, 1000000) == 18
assert mois_seuil(1, 1, 8) == 4

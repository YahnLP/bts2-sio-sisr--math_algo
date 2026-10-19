assert meilleur_choix(1000, 1) == "sequentielle"
assert meilleur_choix(1000, 10) == "sequentielle"
assert meilleur_choix(1000, 11) == "tri+dicho"
assert meilleur_choix(100000, 1000) == "tri+dicho"

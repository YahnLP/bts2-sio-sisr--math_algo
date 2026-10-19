assert somme_chiffres(2024) == 8
assert somme_chiffres(0) == 0
assert somme_chiffres(9) == 9
assert somme_chiffres(90210) == 12
assert all(somme_chiffres(k) == sum(int(c) for c in str(k)) for k in range(0, 3000))

assert pgcd_boucle(252, 105) == 21
assert pgcd_boucle(84, 36) == 12
assert pgcd_boucle(7, 0) == 7
assert pgcd_boucle(0, 5) == 5
assert all(pgcd_boucle(a, b) == __import__('math').gcd(a, b) for a in range(0, 40) for b in range(0, 40))

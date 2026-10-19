assert pgcd(84, 36) == 12
assert pgcd(252, 105) == 21
assert pgcd(7, 0) == 7
assert pgcd(0, 5) == 5
assert all(pgcd(a, b) == __import__('math').gcd(a, b) for a in range(0, 40) for b in range(0, 40))

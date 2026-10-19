assert rang_somme(1000) == 45
assert rang_somme(1) == 1
assert rang_somme(0) == 0
assert rang_somme(10) == 4
assert rang_somme(11) == 5
assert all(rang_somme(s) * (rang_somme(s) + 1) // 2 >= s for s in range(0, 200))

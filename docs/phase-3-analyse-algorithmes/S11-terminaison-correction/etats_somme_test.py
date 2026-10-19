assert etats_somme(4) == [0, 1, 3, 6, 10]
assert etats_somme(0) == [0]
assert etats_somme(1) == [0, 1]
assert all(etats_somme(n)[k] == k * (k + 1) // 2 for n in range(0, 20) for k in range(0, n + 1))

assert maximum_boucle([3, 1, 2]) == 3
assert maximum_boucle([5]) == 5
assert maximum_boucle([-4, -1, -9]) == -1
assert maximum_boucle([2, 2, 2]) == 2
assert maximum_boucle([1, 2, 3]) == 3
assert maximum_boucle([3, 2, 1]) == 3
assert all(maximum_boucle([a, b, c]) == max(a, b, c) for a in range(-2, 3) for b in range(-2, 3) for c in range(-2, 3))

assert somme_rec([4, 1, 3]) == 8
assert somme_rec([]) == 0
assert somme_rec([5]) == 5
assert somme_rec(list(range(10))) == 45
assert somme_rec([-2, 2]) == 0
assert somme_rec(list(range(500))) == 124750

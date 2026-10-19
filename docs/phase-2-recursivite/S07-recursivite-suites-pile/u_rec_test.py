assert u_rec(0) == 3
assert u_rec(1) == 5
assert u_rec(4) == 33
assert all(u_rec(k) == 2 ** (k + 1) + 1 for k in range(0, 60))

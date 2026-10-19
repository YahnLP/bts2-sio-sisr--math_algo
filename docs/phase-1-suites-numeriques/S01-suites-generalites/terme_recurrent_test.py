assert terme_recurrent(1, 0) == 1
assert terme_recurrent(1, 4) == 31
assert terme_recurrent(2, 4) == 47
assert terme_recurrent(0, 3) == 7
assert all(terme_recurrent(1, k) == 2 ** (k + 1) - 1 for k in range(0, 30))

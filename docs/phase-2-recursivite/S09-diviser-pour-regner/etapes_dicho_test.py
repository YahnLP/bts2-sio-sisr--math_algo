assert etapes_dicho([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23) == 3
assert etapes_dicho([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 40) == 4
assert etapes_dicho([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 1) == 3
assert all(etapes_dicho(list(range(1000)), v) <= 10 for v in range(-3, 1004))

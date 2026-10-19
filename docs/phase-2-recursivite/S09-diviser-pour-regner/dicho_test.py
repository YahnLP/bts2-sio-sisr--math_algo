assert dicho([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23) == 5
assert dicho([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 40) == -1
assert dicho([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 2) == 0
assert dicho([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 91) == 9
assert dicho([], 3) == -1
assert all(dicho(list(range(0, 100, 3)), v) == (v // 3 if v % 3 == 0 and 0 <= v <= 99 else -1) for v in range(-5, 110))

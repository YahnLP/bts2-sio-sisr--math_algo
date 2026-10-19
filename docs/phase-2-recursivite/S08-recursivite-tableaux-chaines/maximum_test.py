assert maximum([3, 9, 4]) == 9
assert maximum([5]) == 5
assert maximum([-4, -2, -9]) == -2
assert maximum([1, 8, 8, 3]) == 8
assert all(maximum([a, b, c]) == max(a, b, c) for a in range(-2, 3) for b in range(-2, 3) for c in range(-2, 3))

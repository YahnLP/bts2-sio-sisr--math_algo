assert tri_selection([5, 2, 9, 1, 7]) == [1, 2, 5, 7, 9]
assert tri_selection([]) == []
assert tri_selection([3]) == [3]
assert tri_selection([2, 2, 1]) == [1, 2, 2]
assert tri_selection([3, 2, 1]) == [1, 2, 3]
assert all(tri_selection(L) == sorted(L) for L in [[4, 1, 3, 2], [1, 1, 1], [9, -2, 0, 5, 5]])

assert tri_fusion([5, 2, 9, 1, 7]) == [1, 2, 5, 7, 9]
assert tri_fusion([]) == []
assert tri_fusion([4]) == [4]
assert tri_fusion([3, 3, 1, 2, 2]) == [1, 2, 2, 3, 3]
assert all(tri_fusion(list(range(n, 0, -1))) == list(range(1, n + 1)) for n in range(0, 40))
assert tri_fusion([8, 3, 5, 1, 9, 2, 7, 4, 6]) == sorted([8, 3, 5, 1, 9, 2, 7, 4, 6])

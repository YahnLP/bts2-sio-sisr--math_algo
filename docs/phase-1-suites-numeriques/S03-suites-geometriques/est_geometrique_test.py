assert est_geometrique([3, 6, 12, 24]) == True
assert est_geometrique([2, 5, 8]) == False
assert est_geometrique([]) == True
assert est_geometrique([5]) == True
assert est_geometrique([4, -12, 36]) == True
assert est_geometrique([8, 4, 2, 1]) == True
assert est_geometrique([0, 0, 0]) == True
assert est_geometrique([0, 3]) == False
assert est_geometrique([1, 2, 4, 9]) == False

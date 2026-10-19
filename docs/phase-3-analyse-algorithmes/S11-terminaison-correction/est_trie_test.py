assert est_trie([1, 2, 3]) == True
assert est_trie([2, 1]) == False
assert est_trie([1, 2, 0]) == False
assert est_trie([]) == True
assert est_trie([7]) == True
assert est_trie([1, 1, 2, 2]) == True
assert est_trie([5, 4, 3]) == False
assert all(est_trie(L) == (L == sorted(L)) for L in [[1, 3, 2], [1, 2, 2, 5], [3, 3, 3], [2, 4, 3, 5]])

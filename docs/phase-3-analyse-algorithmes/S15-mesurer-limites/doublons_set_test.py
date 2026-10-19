assert doublons_set([1, 2, 3, 4]) == False
assert doublons_set([1, 2, 1, 4]) == True
assert doublons_set([]) == False
assert doublons_set([5]) == False
assert doublons_set(["a", "b", "a"]) == True
assert doublons_set(list(range(1000))) == False

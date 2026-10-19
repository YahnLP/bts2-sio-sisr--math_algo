assert top_n({"a": 3, "b": 5, "c": 3}, 2) == [("b", 5), ("a", 3)]
assert top_n({}, 3) == []
assert top_n({"x": 1}, 5) == [("x", 1)]
assert top_n({"b": 2, "a": 2}, 2) == [("a", 2), ("b", 2)]

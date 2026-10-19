assert distances_bfs({"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": ["A"]}, "A") == {"A": 0, "B": 1, "C": 1, "D": 2, "E": 2}
assert distances_bfs({"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": ["A"]}, "D") == {"D": 0}
assert distances_bfs({"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": ["A"]}, "E") == {"E": 0, "A": 1, "B": 2, "C": 2, "D": 3}

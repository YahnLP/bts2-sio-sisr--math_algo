assert chemin_bfs({"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": ["A"]}, "A", "D") == ["A", "B", "D"]
assert chemin_bfs({"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": ["A"]}, "A", "E") == ["A", "C", "E"]
assert chemin_bfs({"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": ["A"]}, "A", "A") == ["A"]
assert chemin_bfs({"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": ["A"]}, "D", "A") == None
assert chemin_bfs({"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": ["A"]}, "E", "D") == ["E", "A", "B", "D"]

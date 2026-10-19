assert chemin_dijkstra({"A": {"B": 4, "C": 1}, "B": {"D": 1}, "C": {"B": 2, "D": 5}, "D": {}}, "A", "D") == (4, ["A", "C", "B", "D"])
assert chemin_dijkstra({"S": {"A": 7, "B": 2}, "A": {"C": 1}, "B": {"A": 3, "C": 8}, "C": {}}, "S", "C") == (6, ["S", "B", "A", "C"])
assert chemin_dijkstra({"A": {"B": 4, "C": 1}, "B": {"D": 1}, "C": {"B": 2, "D": 5}, "D": {}}, "A", "A") == (0, ["A"])
assert chemin_dijkstra({"A": {"B": 4, "C": 1}, "B": {"D": 1}, "C": {"B": 2, "D": 5}, "D": {}}, "D", "A") == None

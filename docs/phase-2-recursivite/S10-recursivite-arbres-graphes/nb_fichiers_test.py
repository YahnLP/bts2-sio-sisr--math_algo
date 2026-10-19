assert nb_fichiers({"docs": {"rapport.txt": 120, "notes.txt": 30, "archives": {"2023.zip": 500, "2024.zip": 650}}, "photo.png": 800, "config.ini": 5}) == 6
assert nb_fichiers(120) == 1
assert nb_fichiers({}) == 0
assert nb_fichiers({"a": {"b": 1, "c": 2}, "d": 3}) == 3

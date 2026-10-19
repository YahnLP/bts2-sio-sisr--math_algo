assert taille({"docs": {"rapport.txt": 120, "notes.txt": 30, "archives": {"2023.zip": 500, "2024.zip": 650}}, "photo.png": 800, "config.ini": 5}) == 2105
assert taille(120) == 120
assert taille({}) == 0
assert taille({"a": {"b": {"c": 7}}}) == 7

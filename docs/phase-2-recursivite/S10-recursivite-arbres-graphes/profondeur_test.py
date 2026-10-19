assert profondeur({"docs": {"rapport.txt": 120, "notes.txt": 30, "archives": {"2023.zip": 500, "2024.zip": 650}}, "photo.png": 800, "config.ini": 5}) == 3
assert profondeur(120) == 0
assert profondeur({}) == 1
assert profondeur({"a": 1}) == 1
assert profondeur({"a": {"b": {"c": {}}}}) == 4

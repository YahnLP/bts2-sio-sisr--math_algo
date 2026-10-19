assert chemins({"docs": {"rapport.txt": 120, "notes.txt": 30, "archives": {"2023.zip": 500, "2024.zip": 650}}, "photo.png": 800, "config.ini": 5}) == ['docs/rapport.txt', 'docs/notes.txt', 'docs/archives/2023.zip', 'docs/archives/2024.zip', 'photo.png', 'config.ini']
assert chemins({}) == []
assert chemins({"a": 1}) == ['a']
assert chemins({"d": {"e": {"f": 2}}}) == ['d/e/f']

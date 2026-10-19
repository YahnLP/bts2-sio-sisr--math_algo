assert parse_ligne("10.0.0.1;OK") == ("10.0.0.1", "OK")
assert parse_ligne(" 10.0.0.2 ; ECHEC ") == ("10.0.0.2", "ECHEC")
assert parse_ligne("a;ECHEC") == ("a", "ECHEC")

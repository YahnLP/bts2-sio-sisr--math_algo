assert rapport(["10.0.0.1;OK", "10.0.0.2;ECHEC", "10.0.0.2;ECHEC", "10.0.0.3;ECHEC", "10.0.0.2;ECHEC", "10.0.0.1;ECHEC"], 2) == ["10.0.0.2 : 3"]
assert rapport(["10.0.0.1;OK", "10.0.0.2;ECHEC", "10.0.0.2;ECHEC", "10.0.0.3;ECHEC", "10.0.0.2;ECHEC", "10.0.0.1;ECHEC"], 1) == ["10.0.0.2 : 3", "10.0.0.1 : 1", "10.0.0.3 : 1"]
assert rapport(["10.0.0.1;OK", "10.0.0.2;ECHEC", "10.0.0.2;ECHEC", "10.0.0.3;ECHEC", "10.0.0.2;ECHEC", "10.0.0.1;ECHEC"], 9) == []
assert rapport([], 1) == []

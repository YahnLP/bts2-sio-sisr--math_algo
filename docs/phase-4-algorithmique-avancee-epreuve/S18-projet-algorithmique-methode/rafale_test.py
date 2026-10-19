assert rafale(["10.0.0.1;OK", "10.0.0.2;ECHEC", "10.0.0.2;ECHEC", "10.0.0.3;ECHEC", "10.0.0.2;ECHEC", "10.0.0.1;ECHEC"], "10.0.0.2", 3) == True
assert rafale(["10.0.0.1;OK", "10.0.0.2;ECHEC", "10.0.0.2;ECHEC", "10.0.0.3;ECHEC", "10.0.0.2;ECHEC", "10.0.0.1;ECHEC"], "10.0.0.1", 2) == False
assert rafale(["a;ECHEC", "a;OK", "a;ECHEC", "a;ECHEC"], "a", 2) == True
assert rafale(["a;ECHEC", "a;OK", "a;ECHEC", "a;ECHEC"], "a", 3) == False
assert rafale([], "a", 1) == False
assert rafale(["a;ECHEC", "a;OK", "a;ECHEC", "a;ECHEC"], "b", 1) == False

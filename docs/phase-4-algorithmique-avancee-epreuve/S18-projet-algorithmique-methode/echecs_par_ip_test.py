assert echecs_par_ip(["10.0.0.1;OK", "10.0.0.2;ECHEC", "10.0.0.2;ECHEC", "10.0.0.3;ECHEC", "10.0.0.2;ECHEC", "10.0.0.1;ECHEC"]) == {"10.0.0.2": 3, "10.0.0.3": 1, "10.0.0.1": 1}
assert echecs_par_ip([]) == {}
assert echecs_par_ip(["a;OK"]) == {}
assert echecs_par_ip(["a;ECHEC"]) == {"a": 1}
assert echecs_par_ip([" a ; ECHEC ", "a;ECHEC"]) == {"a": 2}

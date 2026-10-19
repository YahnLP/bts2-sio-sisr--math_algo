assert compte_ip(["10.0.0.1", "10.0.0.2", "10.0.0.1"]) == {"10.0.0.1": 2, "10.0.0.2": 1}
assert compte_ip([]) == {}
assert compte_ip(["a"]) == {"a": 1}
assert compte_ip(list("reseau")) == {"r": 1, "e": 2, "s": 1, "a": 1, "u": 1}

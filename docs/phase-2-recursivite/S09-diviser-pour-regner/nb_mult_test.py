assert nb_mult(0) == 0
assert nb_mult(1) == 1
assert nb_mult(10) == 5
assert nb_mult(16) == 5
assert nb_mult(1000) == 15
assert all(nb_mult(k) <= 2 * k.bit_length() for k in range(1, 5000))

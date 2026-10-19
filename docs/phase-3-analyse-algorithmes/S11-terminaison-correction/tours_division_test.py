assert tours_division(100) == 7
assert tours_division(0) == 0
assert tours_division(1) == 1
assert tours_division(1000) == 10
assert all(tours_division(k) == k.bit_length() for k in range(0, 2000))

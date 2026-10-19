assert tours_log2(1000) == 9
assert tours_log2(1) == 0
assert tours_log2(2) == 1
assert tours_log2(1000000) == 19
assert all(tours_log2(k) == k.bit_length() - 1 for k in range(1, 3000))

assert binaire(0) == '0'
assert binaire(1) == '1'
assert binaire(13) == '1101'
assert binaire(10) == '1010'
assert all(binaire(k) == bin(k)[2:] for k in range(0, 300))

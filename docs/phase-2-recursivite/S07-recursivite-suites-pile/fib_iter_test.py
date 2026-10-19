assert fib_iter(0) == 0
assert fib_iter(1) == 1
assert fib_iter(6) == 8
assert fib_iter(30) == 832040
assert fib_iter(90) == 2880067194370816120
assert fib_iter(2000) % 1000 == 125
assert all(fib_iter(k) == fib_iter(k - 1) + fib_iter(k - 2) for k in range(2, 300))

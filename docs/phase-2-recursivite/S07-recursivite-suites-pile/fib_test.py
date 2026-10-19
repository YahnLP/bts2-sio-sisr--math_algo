assert fib(0) == 0
assert fib(1) == 1
assert fib(10) == 55
assert fib(20) == 6765
assert all(fib(k) == fib(k - 1) + fib(k - 2) for k in range(2, 18))

assert fib_memo(0) == 0
assert fib_memo(1) == 1
assert fib_memo(30) == 832040
assert fib_memo(90) == 2880067194370816120
assert all(fib_memo(k) == fib_memo(k - 1) + fib_memo(k - 2) for k in range(2, 100))

assert est_palindrome('radar') == True
assert est_palindrome('reseau') == False
assert est_palindrome('') == True
assert est_palindrome('a') == True
assert est_palindrome('kayak') == True
assert est_palindrome('ab') == False
assert all(est_palindrome(w) == (w == w[::-1]) for w in ['abba', 'abca', 'x', 'xyzzyx', 'aab'])

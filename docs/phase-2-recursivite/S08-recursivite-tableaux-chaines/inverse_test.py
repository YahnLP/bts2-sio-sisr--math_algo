assert inverse('abc') == 'cba'
assert inverse('') == ''
assert inverse('a') == 'a'
assert inverse('radar') == 'radar'
assert all(inverse(w) == w[::-1] for w in ['bonjour', 'ab', 'xyzzy'])

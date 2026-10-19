assert parentheses_ok("{[()]}") == True
assert parentheses_ok("([)]") == False
assert parentheses_ok("(()") == False
assert parentheses_ok("") == True
assert parentheses_ok(")(") == False
assert parentheses_ok("a(b)c[d]") == True
assert parentheses_ok("]") == False

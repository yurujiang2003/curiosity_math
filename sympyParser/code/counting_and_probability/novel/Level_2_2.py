from sympy import symbols, factorial

n = 15
r = 2

combinations = factorial(n) / (factorial(r) * factorial(n - r))
result = combinations.evalf()
result

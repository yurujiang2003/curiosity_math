from sympy import symbols, factorial

n = 15
r = 13

combinations = factorial(n) / (factorial(r) * factorial(n - r))
result = combinations.evalf()
result

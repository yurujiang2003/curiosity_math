from sympy import symbols, factorial, Rational

n = 20
r = 2

combinations = factorial(n) / (factorial(r) * factorial(n - r))
result = combinations.evalf()
result

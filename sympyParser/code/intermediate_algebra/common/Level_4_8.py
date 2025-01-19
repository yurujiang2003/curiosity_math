from sympy import symbols, fibonacci, summation, oo

n = symbols('n')
S = summation(1 / (fibonacci(n) * fibonacci(n + 2)), (n, 1, oo))
result = S.evalf()
result

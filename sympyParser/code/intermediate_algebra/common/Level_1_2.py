from sympy import symbols, summation, S

n = symbols('n')
expr = summation((-1)**(n+1) * n, (n, 1, 100))
result = expr
result

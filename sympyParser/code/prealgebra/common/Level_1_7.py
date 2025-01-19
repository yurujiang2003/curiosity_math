from sympy import symbols, simplify

x = 3
expression = x * x + x * (x + x) - x**3
result = simplify(expression)
result

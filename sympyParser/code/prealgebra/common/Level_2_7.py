from sympy import symbols, ceiling

x = symbols('x')
multiple_of_5 = 5 * ceiling(x / 5)
result = multiple_of_5.subs(x, -32)
result

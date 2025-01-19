from sympy import symbols, expand

x = symbols('x')
expression = 6 * (x + 2) * (x + 3)
expanded_expression = expand(expression)
expanded_expression

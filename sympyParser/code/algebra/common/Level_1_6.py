from sympy import symbols, factor

r = symbols('r')
expression = r**2 + 10*r + 25
factored_expression = factor(expression)
factored_expression

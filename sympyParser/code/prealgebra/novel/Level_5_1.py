from sympy import symbols, simplify

m = symbols('m')
expression = (2*m + 8)/3 - (2 - m)/3
simplified_expression = simplify(expression)
simplified_expression

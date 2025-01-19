from sympy import symbols, cos, sin, simplify, tan

x = symbols('x')
expr = (cos(x) / (1 - sin(x))) - (cos(x) / (1 + sin(x)))
simplified_expr = simplify(expr)
final_answer = simplify(2 * sin(x) / cos(x))

final_answer

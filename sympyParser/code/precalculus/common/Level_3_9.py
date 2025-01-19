from sympy import symbols, cos, sin, tan, simplify

x = symbols('x')
expr = (cos(x) / (1 - sin(x))) - (cos(x) / (1 + sin(x)))
simplified_expr = simplify(expr)
final_answer = simplified_expr

final_answer

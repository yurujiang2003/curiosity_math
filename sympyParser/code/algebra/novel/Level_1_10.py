from sympy import symbols, simplify

x, y = symbols('x y')
expr = (2*x**3 - 3*y**2) / 6
result = expr.subs({x: 3, y: 2})
final_answer = simplify(result)
final_answer

from sympy import symbols, Eq, cos, simplify

x, y = symbols('x y')
r_squared = x**2 + y**2
cos_2theta = (x**2 - y**2) / r_squared

equation = Eq(r_squared * cos_2theta, 4)
simplified_equation = simplify(equation)

final_equation = simplified_equation.subs(r_squared, x**2 + y**2)
final_answer = final_equation

final_answer

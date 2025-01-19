from sympy import symbols, Eq, solve, sqrt

x = symbols('x')
equation = Eq((4 * x**2)**(1/3), 4)
solution = solve(equation, x)
final_values = sorted([sol.evalf() for sol in solution])
final_values

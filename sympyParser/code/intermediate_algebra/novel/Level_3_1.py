from sympy import symbols, sqrt, Eq, solve

x, y = symbols('x y')
equation = Eq(sqrt(x**2 + sqrt(x**2 + 11)) + sqrt(x**2 - sqrt(x**2 + 11)), 4)

y_eq = sqrt(x**2 + 11)
x_eq = y_eq**2 - 11

new_equation = Eq(sqrt(x_eq + y) + sqrt(x_eq - y), 4)

y_squared_plus_y_minus_11 = y**2 + y - 11
y_squared_minus_y_minus_11 = y**2 - y - 11

a, b = symbols('a b')
ab_eq = Eq(a + b, 4)

solutions = solve(new_equation, y)
final_solutions = []

for sol in solutions:
    x_sol = sqrt(sol**2 - 11)
    final_solutions.extend([x_sol, -x_sol])

final_solutions = [sol.evalf() for sol in final_solutions]
final_solutions = list(set(final_solutions))  # Remove duplicates
final_solutions.sort()

final_solutions

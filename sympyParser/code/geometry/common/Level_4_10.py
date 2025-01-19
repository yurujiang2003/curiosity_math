from sympy import symbols, Eq, solve

x = symbols('x')
interior_angle = 6.5 * x
exterior_angle_eq = Eq(interior_angle + x, 180)

x_solution = solve(exterior_angle_eq, x)[0]
n = 360 / x_solution

n

from sympy import symbols, Eq, solve

x = symbols('x')
interior_angle = 6.5 * x
exterior_angle = x

equation = Eq(interior_angle + exterior_angle, 180)
solution = solve(equation, x)[0]

n = 360 / solution
n_value = n.evalf()

n_value

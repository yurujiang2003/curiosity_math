from sympy import symbols, Eq, solve, pi

V = 45 * pi
r = 3
h = symbols('h')

volume_eq = Eq(V, pi * r**2 * h)
height_solution = solve(volume_eq, h)[0]
height_solution

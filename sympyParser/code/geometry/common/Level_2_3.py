from sympy import symbols, Eq, solve, pi

# Define variables
h = symbols('h')
V = 45 * pi
r = 3

# Volume formula
volume_eq = Eq(V, pi * r**2 * h)

# Solve for height
height_solution = solve(volume_eq, h)[0]
height_solution

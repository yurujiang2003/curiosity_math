from sympy import symbols, sqrt, Rational, simplify

s = symbols('s')
r = symbols('r')

# Define the quadratic equation
equation = r**2 - 8*r*s + 4*s**2

# Solve the quadratic equation
solutions = solve(equation, r)

# Select the positive solution
positive_solution = [sol for sol in solutions if sol > s][0]

# Calculate r/s
ratio = simplify(positive_solution / s)
ratio_value = ratio.evalf()

ratio_value

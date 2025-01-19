from sympy import symbols, Eq, solve, sqrt

x = symbols('x')
y = x**2 - 10*x

# Define the equation
equation = Eq((1/(y - 29)) + (1/(y - 45)) - (2/(y - 69)), 0)

# Solve for y
numerator = (y - 45)*(y - 69) + (y - 29)*(y - 69) - 2*(y - 29)*(y - 45)
y_solution = solve(Eq(numerator, 0), y)[0]

# Substitute back to find x
x_eq = Eq(x**2 - 10*x, y_solution)
x_solutions = solve(x_eq, x)

# Filter for positive solutions
positive_solutions = [sol.evalf() for sol in x_solutions if sol > 0]
positive_solutions

from sympy import symbols, Eq, solve

a = symbols('a')
# Define the equation based on the area of the triangle
equation = Eq((9 + a**2)**2 / (4 * a), 25)

# Solve the equation
solutions = solve(equation, a)

# Filter for positive rational solutions
positive_rational_solutions = [sol.evalf() for sol in solutions if sol > 0]

# Return the final answer
positive_rational_solutions

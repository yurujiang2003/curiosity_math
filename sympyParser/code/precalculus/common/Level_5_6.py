from sympy import symbols, sqrt, solve

a = symbols('a')
# Define the quadratic equation
equation = a**2 + 4*a + 1

# Solve the equation
solutions = solve(equation, a)

# Filter solutions within the range [-2, 2]
valid_solutions = [sol.evalf() for sol in solutions if -2 <= sol.evalf() <= 2]

valid_solutions

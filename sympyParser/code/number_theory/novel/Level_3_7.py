from sympy import symbols, Eq, solve, sqrt

b = symbols('b')
A = 3
B = 2
C = -56

# Define the equation
equation = Eq(A * b**2 + B * b + C, 0)

# Solve the equation
solutions = solve(equation, b)

# Filter for positive solutions
valid_solutions = [sol for sol in solutions if sol > 0]

# Return the final answer
valid_solutions[0]

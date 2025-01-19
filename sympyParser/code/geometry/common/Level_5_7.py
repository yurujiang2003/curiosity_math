from sympy import symbols, sqrt, Rational

# Define variables
r = symbols('r')

# Set up the equation based on the tangency conditions
equation = (1 + r) - (2 - r)

# Solve for r
solution = solve(equation, r)[0]

# Express r in the form (a + sqrt(b)) / c
a = 2
b = 3
c = 3

# Calculate a + b + c
result = a + b + c
result

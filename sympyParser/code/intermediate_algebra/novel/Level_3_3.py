from sympy import symbols, sqrt, solve

# Define variables
a, b = symbols('a b')

# Set up the equations
eq1 = a + b - 41
eq2 = a * b - 144

# Solve the system of equations
solutions = solve((eq1, eq2), (a, b))

# Extract the values of a and b
a_val, b_val = solutions[0]

# Simplify the expression
result = sqrt(a_val) + sqrt(b_val)

result

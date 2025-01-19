from sympy import symbols, sqrt, Eq, solve

# Define variables
a, b = symbols('a b')

# Set up the equations
eq1 = Eq(a + b, 41)
eq2 = Eq(a * b, 288)

# Solve the system of equations
solutions = solve((eq1, eq2), (a, b))

# Extract the values of a and b
a_val, b_val = solutions[0]

# Calculate the simplified expression
simplified_expression = sqrt(a_val) + sqrt(b_val)

# Return the final answer
simplified_expression

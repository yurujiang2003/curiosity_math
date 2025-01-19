from sympy import symbols, sqrt, solve, Rational

# Define variables
a, b = symbols('a b')
hypotenuse = 12
area = 4

# Equations
eq1 = a * b - 8  # ab = 8
eq2 = a**2 + b**2 - hypotenuse**2  # a^2 + b^2 = 144

# Solve the equations
solutions = solve((eq1, eq2), (a, b))

# Extract a and b
a_val = solutions[0][0]
b_val = solutions[0][1]

# Calculate sin A and cos A
sin_A = b_val / hypotenuse
cos_A = a_val / hypotenuse

# Calculate sin 2A
sin_2A = 2 * sin_A * cos_A

# Return the final answer
sin_2A.evalf()

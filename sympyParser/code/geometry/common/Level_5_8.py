from sympy import symbols, sqrt, Eq, solve

# Define the variables
x_B, x_C, y_B = symbols('x_B x_C y_B')

# Coordinates of points
D_x = x_C / 2
E_x = x_B

# Lengths of BD and DE
BD = sqrt((x_B - D_x)**2 + y_B**2)
DE = D_x - x_B

# Given condition
equation = Eq(BD, 2 * DE)

# Expand and simplify the equation
expanded_eq = equation.simplify()

# Solve for x_C in terms of x_B and y_B
solutions = solve(expanded_eq, x_C)

# Since we need to compute AB/EC, we express AB and EC
AB = sqrt(x_B**2 + y_B**2)  # c
EC = x_C - x_B  # b - x_B

# Substitute the solution for x_C into the ratio
ratio = AB / EC.subs(x_C, solutions[0])

# Return the final answer
ratio

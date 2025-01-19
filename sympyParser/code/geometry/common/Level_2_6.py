from sympy import symbols, pi, sqrt

# Define the variables
r = symbols('r')
S = 196 * pi

# Surface area formula
surface_area_eq = 4 * pi * r**2 - S

# Solve for r
radius_solution = sqrt(49)

# Calculate the circumference
C = 2 * pi * radius_solution

C

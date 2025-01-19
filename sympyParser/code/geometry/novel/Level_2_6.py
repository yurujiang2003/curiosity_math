from sympy import symbols, pi, sqrt

# Define the variables
r = symbols('r')

# Given surface area
A = 196 * pi

# Surface area formula
surface_area_eq = 4 * pi * r**2 - A

# Solve for radius
radius_solution = sqrt(solve(surface_area_eq, r)[0])

# Circumference formula
C = 2 * pi * radius_solution

# Return the final answer
C

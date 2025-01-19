from sympy import symbols, pi, Rational

# Define the variables
r_A, r_B = symbols('r_A r_B')

# Given angles
theta_A = 55
theta_B = 40

# Arc length equations
arc_length_A = (theta_A / 360) * (2 * pi * r_A)
arc_length_B = (theta_B / 360) * (2 * pi * r_B)

# Set the arc lengths equal
equation = arc_length_A - arc_length_B

# Solve for the ratio of the radii
ratio_radii = (theta_B / theta_A).simplify()

# Calculate the ratio of the areas
ratio_areas = (ratio_radii ** 2).simplify()

# Express the ratio as a common fraction
final_answer = ratio_areas.simplify()

final_answer

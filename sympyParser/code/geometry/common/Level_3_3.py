from sympy import pi

# Define the radii of the circles
r1 = 2
r2 = 4
r3 = 6
r4 = 8

# Calculate the areas of the circles
A1 = pi * r1**2
A2 = pi * r2**2
A3 = pi * r3**2
A4 = pi * r4**2

# Determine the area of the shaded region
shaded_area = A3 - A2

# Return the final answer
shaded_area

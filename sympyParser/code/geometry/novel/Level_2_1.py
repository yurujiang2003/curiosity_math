from sympy import sqrt

# Define the leg lengths of the first triangle
a = 7
b = 24

# Calculate the hypotenuse of the first triangle
c = sqrt(a**2 + b**2)

# Define the hypotenuse of the second triangle
hypotenuse_second_triangle = 100

# Calculate the scale factor
scale_factor = hypotenuse_second_triangle / c

# Calculate the shorter leg of the second triangle
shorter_leg_second_triangle = a * scale_factor

# Return the final answer
shorter_leg_second_triangle

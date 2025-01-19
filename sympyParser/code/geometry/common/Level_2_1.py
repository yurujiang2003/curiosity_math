from sympy import sqrt

# Define the lengths of the legs of the first triangle
a1 = 7
b1 = 24

# Calculate the hypotenuse of the first triangle using the Pythagorean theorem
c1 = sqrt(a1**2 + b1**2)

# Define the hypotenuse of the second triangle
c2 = 100

# Calculate the scale factor
scale_factor = c2 / c1

# Calculate the lengths of the legs of the second triangle
shorter_leg = a1 * scale_factor
longer_leg = b1 * scale_factor

# Return the length of the shorter leg of the second triangle
shorter_leg

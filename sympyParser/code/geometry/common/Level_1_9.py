from sympy import pi

# Define points A and B
A = (2, 5)
B = (10, 5)

# Calculate the diameter
diameter = abs(B[0] - A[0])

# Calculate the radius
radius = diameter / 2

# Calculate the area of the circle
area = pi * radius**2

# Return the final answer
area

from sympy import sqrt, pi

# Define points A and B
A = (2, 5)
B = (10, 5)

# Calculate the diameter using the distance formula
d = sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)

# Calculate the radius
r = d / 2

# Calculate the area of the circle
A_circle = pi * r**2

# Return the final answer
A_circle

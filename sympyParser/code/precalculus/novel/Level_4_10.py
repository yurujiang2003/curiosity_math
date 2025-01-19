from sympy import sqrt, pi

A = (-4, 5, -17)
B = (34, 15, 5)

# Calculate the distance AB
AB = sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2 + (B[2] - A[2])**2)

# Radius of the circles
r = AB

# Total length of the curve
L = 2 * (2 * pi * r)

L

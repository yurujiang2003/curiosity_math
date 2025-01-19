from sympy import Matrix, acos, deg, sqrt

# Define the coordinates of points X, Y, Z
X = Matrix([1/2, 0, 0])
Y = Matrix([1, 1/2, 0])
Z = Matrix([1/2, 0, 1])

# Calculate vectors XY and XZ
XY = Y - X
XZ = Z - X

# Calculate magnitudes of XY and XZ
magnitude_XY = XY.norm()
magnitude_XZ = XZ.norm()

# Calculate the dot product of XY and XZ
dot_product = XY.dot(XZ)

# Calculate the cosine of the angle
cos_theta = dot_product / (magnitude_XY * magnitude_XZ)

# Calculate the angle in radians and convert to degrees
angle = deg(acos(cos_theta))

# Return the final answer
angle

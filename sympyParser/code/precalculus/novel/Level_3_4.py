from sympy import Matrix, acos, deg, pi

# Define the points
X = Matrix([1/2, 0, 0])
Y = Matrix([1, 1/2, 0])
Z = Matrix([0, 1/2, 1])

# Calculate the vectors
XY = Y - X
XZ = Z - X

# Calculate the dot product
dot_product = XY.dot(XZ)

# Calculate the magnitudes
magnitude_XY = XY.norm()
magnitude_XZ = XZ.norm()

# Calculate the angle in radians
angle_radians = acos(dot_product / (magnitude_XY * magnitude_XZ))

# Convert the angle to degrees
angle_degrees = deg(angle_radians)

# Return the final answer
angle_degrees

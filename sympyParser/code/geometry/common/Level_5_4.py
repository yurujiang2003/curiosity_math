from sympy import Matrix, sqrt

# Define the points A, B, C, D
A = Matrix([1, 1, 1])
B = Matrix([1, -1, -1])
C = Matrix([-1, 1, -1])
D = Matrix([-1, -1, 1])

# Calculate the midpoint M of segment CD
M = (C + D) / 2

# Calculate vectors AB and AM
AB = B - A
AM = M - A

# Calculate the dot product of AB and AM
dot_product = AB.dot(AM)

# Calculate the magnitudes of AB and AM
magnitude_AB = AB.norm()
magnitude_AM = AM.norm()

# Calculate cos(angle ABM)
cos_angle_ABM = dot_product / (magnitude_AB * magnitude_AM)

# Final answer
final_answer = cos_angle_ABM.evalf()
final_answer

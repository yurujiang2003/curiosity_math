from sympy import symbols, sqrt, acos, deg

# Define points
A = (0, 0)
B = (0, 1)
D = (1, 0)
E = (1/2, sqrt(3)/2)

# Define vectors
BA = (A[0] - B[0], A[1] - B[1])  # Vector BA
AE = (E[0] - A[0], E[1] - A[1])  # Vector AE

# Calculate dot product
dot_product = BA[0] * AE[0] + BA[1] * AE[1]

# Calculate magnitudes
magnitude_BA = sqrt(BA[0]**2 + BA[1]**2)
magnitude_AE = sqrt(AE[0]**2 + AE[1]**2)

# Calculate cosine of the angle
cos_theta = dot_product / (magnitude_BA * magnitude_AE)

# Calculate angle in degrees
angle_BAE = deg(acos(cos_theta))

angle_BAE.evalf()

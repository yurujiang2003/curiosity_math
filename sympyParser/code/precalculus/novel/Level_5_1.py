from sympy import symbols, cos, pi, sqrt, simplify

# Define the angles
theta_2 = 2 * pi / 7
theta_6 = 6 * pi / 7

# Calculate coordinates of points A, B, D, G
A = 1
B = cos(theta_2) + 1j * sin(theta_2)
D = cos(3 * theta_2) + 1j * sin(3 * theta_2)
G = cos(theta_6) + 1j * sin(theta_6)

# Calculate centroid M of triangle ABD
M = (A + B + D) / 3

# Calculate vectors GO and OM
O = 0
GO = O - G
OM = M - O

# Calculate the dot product GO · OM
dot_product = (GO.real * OM.real + GO.imag * OM.imag)

# Calculate magnitudes |GO| and |OM|
magnitude_GO = sqrt(GO.real**2 + GO.imag**2)
magnitude_OM = sqrt(OM.real**2 + OM.imag**2)

# Calculate cos(angle GOM)
cos_angle_GOM = dot_product / (magnitude_GO * magnitude_OM)

# Calculate cos^2(angle GOM)
cos_squared_angle_GOM = simplify(cos_angle_GOM**2)

# Return the final answer
cos_squared_angle_GOM

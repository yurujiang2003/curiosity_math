from sympy import symbols, cos, sin, simplify

# Define variables
c, b, theta = symbols('c b theta')

# Define points A, B, C
A = (0, 0)
B = (c, 0)
C = (b * cos(theta), b * sin(theta))

# Midpoints D, E, F
D = ((c + b * cos(theta)) / 2, b * sin(theta) / 2)
E = (b * cos(theta) / 2, b * sin(theta) / 2)
F = (c / 2, 0)

# Midpoints P, Q, R
P = ((0 + D[0]) / 2, (0 + D[1]) / 2)
Q = ((B[0] + E[0]) / 2, (B[1] + E[1]) / 2)
R = ((C[0] + F[0]) / 2, (C[1] + F[1]) / 2)

# Compute squared distances
AQ2 = (P[0] - A[0])**2 + (P[1] - A[1])**2
AR2 = (R[0] - A[0])**2 + (R[1] - A[1])**2
BP2 = (P[0] - B[0])**2 + (P[1] - B[1])**2
BR2 = (R[0] - B[0])**2 + (R[1] - B[1])**2
CP2 = (P[0] - C[0])**2 + (P[1] - C[1])**2
CQ2 = (Q[0] - C[0])**2 + (Q[1] - C[1])**2

# Sum of squared distances
numerator = AQ2 + AR2 + BP2 + BR2 + CP2 + CQ2

# Compute squared lengths of sides
AB2 = (B[0] - A[0])**2 + (B[1] - A[1])**2
AC2 = (C[0] - A[0])**2 + (C[1] - A[1])**2
BC2 = (C[0] - B[0])**2 + (C[1] - B[1])**2

# Denominator
denominator = AB2 + AC2 + BC2

# Final result
result = simplify(numerator / denominator)
result

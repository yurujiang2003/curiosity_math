from sympy import symbols, simplify

b, c_x, c_y = symbols('b c_x c_y')

# Coordinates of the points
A = (0, 0)
B = (b, 0)
C = (c_x, c_y)

D = ((b + c_x) / 2, c_y / 2)
E = (c_x / 2, c_y / 2)
F = (b / 2, 0)

P = ((0 + D[0]) / 2, (0 + D[1]) / 2)
Q = ((b + E[0]) / 2, (0 + E[1]) / 2)
R = ((c_x + F[0]) / 2, (c_y + F[1]) / 2)

# Calculate the squares of the distances
AQ2 = (Q[0] - A[0])**2 + (Q[1] - A[1])**2
AR2 = (R[0] - A[0])**2 + (R[1] - A[1])**2
BP2 = (P[0] - B[0])**2 + (P[1] - B[1])**2
BR2 = (R[0] - B[0])**2 + (R[1] - B[1])**2
CP2 = (P[0] - C[0])**2 + (P[1] - C[1])**2
CQ2 = (Q[0] - C[0])**2 + (Q[1] - C[1])**2

# Sum of squares
numerator = AQ2 + AR2 + BP2 + BR2 + CP2 + CQ2

# Sum of squares of sides
AB2 = (B[0] - A[0])**2 + (B[1] - A[1])**2
AC2 = (C[0] - A[0])**2 + (C[1] - A[1])**2
BC2 = (C[0] - B[0])**2 + (C[1] - B[1])**2
denominator = AB2 + AC2 + BC2

# Final result
result = simplify(numerator / denominator)
result

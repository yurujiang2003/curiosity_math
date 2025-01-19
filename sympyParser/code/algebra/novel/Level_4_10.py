from sympy import Rational

# Define the endpoints
A1 = (0, 0)
A2 = (2, 2)
B1 = (5, 0)
B2 = (6, 2)

# Calculate midpoints
M1 = (Rational(A1[0] + A2[0], 2), Rational(A1[1] + A2[1], 2))
M2 = (Rational(B1[0] + B2[0], 2), Rational(B1[1] + B2[1], 2))

# Calculate slope
slope = (M2[1] - M1[1]) / (M2[0] - M1[0])

slope

from sympy import Rational

# Define the endpoints
point1 = (0, 0)
point2 = (2, 2)
point3 = (5, 0)
point4 = (6, 2)

# Calculate midpoints
M1 = (Rational(point1[0] + point2[0], 2), Rational(point1[1] + point2[1], 2))
M2 = (Rational(point3[0] + point4[0], 2), Rational(point3[1] + point4[1], 2))

# Calculate the slope
slope = (M2[1] - M1[1]) / (M2[0] - M1[0])

# Return the final answer
slope

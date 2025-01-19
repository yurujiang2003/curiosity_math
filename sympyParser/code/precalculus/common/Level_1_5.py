from sympy import Rational

# Define the endpoints
x1, y1, z1 = 7, -3, 2
x2, y2, z2 = 4, 1, 0

# Calculate the midpoint
midpoint = (Rational(x1 + x2, 2), Rational(y1 + y2, 2), Rational(z1 + z2, 2))

# Return the final answer
midpoint

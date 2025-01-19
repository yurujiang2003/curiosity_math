from sympy import Rational

# Define the points
x1, y1 = -1, 2
x2, y2 = 1, -2

# Calculate the slope of the line through the points
m = (y2 - y1) / (x2 - x1)

# Calculate the slope of the perpendicular line
perpendicular_slope = Rational(-1, m)

perpendicular_slope

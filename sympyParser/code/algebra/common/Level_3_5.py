from sympy import Rational

# Define the points
x1, y1 = 0, 0
x2, y2 = 9, 6

# Define the ratio
m, n = 1, 2

# Calculate the coordinates of the point
x = (m * x2 + n * x1) / (m + n)
y = (m * y2 + n * y1) / (m + n)

# Calculate the sum of the coordinates
sum_coordinates = x + y

# Return the final answer
sum_coordinates.evalf()

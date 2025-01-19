from sympy import symbols, solve, Matrix

# Define variables
x, y = symbols('x y')

# Define the equations of the lines
line1 = y - 0
line2 = y - (x + 4)
line3 = x + 3*y - 12

# Find intersection points
point1 = solve((line1, line2), (x, y))  # Intersection of y=0 and y=x+4
point2 = solve((line1, line3), (x, y))  # Intersection of y=0 and x+3y=12
point3 = solve((line2, line3), (x, y))  # Intersection of y=x+4 and x+3y=12

# Vertices of the triangle
vertices = [point1, point2, point3]

# Calculate the area using the determinant method
A = Matrix([[1, vertices[0][x], vertices[0][y]],
             [1, vertices[1][x], vertices[1][y]],
             [1, vertices[2][x], vertices[2][y]]])

area = abs(A.det()) / 2
area.evalf()

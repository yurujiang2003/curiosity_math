from sympy import symbols, Eq, solve, Matrix

# Define variables
x, y = symbols('x y')

# Define the equations of the lines
line1 = Eq(y, 0)
line2 = Eq(y, x + 4)
line3 = Eq(x + 3*y, 12)

# Find intersection points
point1 = solve((line1, line2), (x, y))  # Intersection of y = 0 and y = x + 4
point2 = solve((line1, line3), (x, y))  # Intersection of y = 0 and x + 3y = 12
point3 = solve((line2, line3), (x, y))  # Intersection of y = x + 4 and x + 3y = 12

# Convert points to tuples
vertices = [tuple(point1.values()), tuple(point2.values()), tuple(point3.values())]

# Calculate area using the determinant formula
A = Matrix(vertices).det() / 2
area = abs(A)

# Return the final answer
area.evalf()

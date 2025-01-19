from sympy import symbols, Matrix

# Define coordinates of points A, B, C
A = (0, 0)
B = (15, 0)
C = (0, 24)

# Calculate midpoints D, E, F
D = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
E = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
F = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)

# Area calculation using the determinant method
x1, y1 = D
x2, y2 = E
x3, y3 = F

area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
area

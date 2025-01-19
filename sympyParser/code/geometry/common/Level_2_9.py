from sympy import symbols, Matrix

# Define points A, B, C
A = Matrix([0, 0])
B = Matrix([15, 0])
C = Matrix([0, 24])

# Calculate midpoints D, E, F
D = (A + C) / 2
E = (A + B) / 2
F = (B + C) / 2

# Calculate area of triangle DEF
x1, y1 = D[0], D[1]
x2, y2 = E[0], E[1]
x3, y3 = F[0], F[1]

area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
area.evalf()

from sympy import sqrt, symbols, solve, Matrix

# Define the sides of the triangle
AB = sqrt(30)
AC = sqrt(6)
BC = sqrt(15)

# Calculate the semi-perimeter
s = (AB + AC + BC) / 2

# Calculate the areas using Heron's formula
s_AB = s - AB
s_AC = s - AC
s_BC = s - BC

K_ABC = sqrt(s * s_AB * s_AC * s_BC)

# Coordinates of points B and C
B = Matrix([0, 0])
C = Matrix([BC, 0])

# Let A be at (x_A, y_A)
x_A, y_A = symbols('x_A y_A')

# Distance equations
eq1 = x_A**2 + y_A**2 - AB**2
eq2 = (x_A - BC)**2 + y_A**2 - AC**2

# Solve for coordinates of A
sol = solve((eq1, eq2), (x_A, y_A))
A = Matrix([sol[0][0], sol[0][1]])

# Midpoint D of BC
D = (B + C) / 2

# Area of triangle ADB
area_ADB = (1/2) * AB * (D[0] - B[0])

# Ratio of areas
ratio = area_ADB / K_ABC

ratio.evalf()

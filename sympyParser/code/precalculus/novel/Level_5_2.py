from sympy import symbols, cos, sqrt, Matrix, acos, pi, solve

# Define variables
yb, zb, yc, zc = symbols('yb zb yc zc')

# Define the known values
x_b = 1/5
x_c = 1/6

# Unit vector equations
eq1 = (1/5)**2 + yb**2 + zb**2 - 1
eq2 = (1/6)**2 + yc**2 + zc**2 - 1

# Dot product equation for angle between b and c
eq3 = (1/5)*(1/6) + yb*yc + zb*zc - 1/2

# Solve the equations
solutions = solve((eq1, eq2, eq3), (yb, zb, yc, zc))

# Choose one solution for yb, zb, yc, zc
yb_val, zb_val, yc_val, zc_val = solutions[0]

# Define vectors
a = Matrix([1, 0, 0])
b = Matrix([x_b, yb_val, zb_val])
c = Matrix([x_c, yc_val, zc_val])

# Normal vector to the plane P
n = b.cross(c)

# Projection of a onto the normal vector n
proj_n = (a.dot(n) / n.norm()**2) * n

# Projection of a onto the plane P
proj_P = a - proj_n

# Express projection in terms of b and c
p = proj_P.dot(b) / b.norm()**2
q = proj_P.dot(c) / c.norm()**2

# Return the ordered pair (p, q)
(p, q)

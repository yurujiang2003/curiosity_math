from sympy import Matrix

A = Matrix([6, 0, 0])
B = Matrix([0, 4, 0])
C = Matrix([0, 0, 2])
D = Matrix([0, 0, 0])

# Step 1: Calculate the Volume V
V = (1/6) * abs((A - D).determinant((B - D), (C - D)))

# Step 2: Calculate the Surface Area S
area_ABD = (1/2) * 6 * 4
area_ACD = (1/2) * 6 * 2
area_BCD = (1/2) * 4 * 2

# Area of triangle ABC using cross product
AB = B - A
AC = C - A
area_ABC = (1/2) * abs(AB.cross(AC).norm())

S = area_ABD + area_ACD + area_BCD + area_ABC

# Calculate the inradius r
r = (3 * V) / S
r.evalf()

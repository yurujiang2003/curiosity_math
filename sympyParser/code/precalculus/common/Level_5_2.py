from sympy import symbols, acos, cos, Matrix

# Define the unit vectors a, b, c
a, b, c = symbols('a b c')

# Define the angles
angle_ab = acos(1/5)
angle_ac = acos(1/6)
angle_bc = acos(1/2)

# Calculate the dot products
dot_ab = cos(angle_ab)
dot_ac = cos(angle_ac)
dot_bc = cos(angle_bc)

# Projection of a onto b and c
proj_a_b = dot_ab * Matrix([1, 0, 0])  # Assuming b = [1, 0, 0]
proj_a_c = dot_ac * Matrix([cos(angle_bc), sin(angle_bc), 0])  # Assuming c in the plane

# Calculate the projection of a onto the plane P
p = proj_a_b[0]
q = proj_a_c[0]

result = (p, q)
result

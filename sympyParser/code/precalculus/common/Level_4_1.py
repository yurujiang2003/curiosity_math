from sympy import Matrix, gcd

# Define the points
P1 = Matrix([2, 0, 0])
P2 = Matrix([0, -5, 0])
P3 = Matrix([0, 0, -4])

# Find two vectors in the plane
v1 = P2 - P1
v2 = P3 - P1

# Calculate the normal vector using the cross product
n = v1.cross(v2)

# Coefficients of the plane equation
A, B, C = n

# Calculate D using point P1
D = -A * P1[0] - B * P1[1] - C * P1[2]

# Ensure A > 0 and gcd(|A|, |B|, |C|, |D|) = 1
g = gcd([A, B, C, D])
A, B, C, D = A // g, B // g, C // g, D // g

# Return the final answer
(A, B, C, D)

from sympy import Matrix, symbols, gcd

# Define the points
P1 = Matrix([2, 0, 0])
P2 = Matrix([0, -5, 0])
P3 = Matrix([0, 0, -4])

# Find vectors in the plane
v1 = P2 - P1
v2 = P3 - P1

# Find the normal vector using the cross product
n = v1.cross(v2)

# Coefficients of the plane equation
A, B, C = n[0], n[1], n[2]

# Use point P1 to find D
D = -A * P1[0] - B * P1[1] - C * P1[2]

# Ensure A > 0 and gcd condition
if A < 0:
    A, B, C, D = -A, -B, -C, -D

g = gcd(abs(A), abs(B), abs(C), abs(D))
A //= g
B //= g
C //= g
D //= g

# Final equation of the plane
final_equation = f"{A}x + {B}y + {C}z + {D} = 0"
final_equation

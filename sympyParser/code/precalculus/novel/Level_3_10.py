from sympy import Matrix, Rational

# Define the vertices of the tetrahedron
A = (6, 0, 0)
B = (0, 4, 0)
C = (0, 0, 2)
D = (0, 0, 0)

# Calculate the volume of the tetrahedron
V_matrix = Matrix([[A[0], A[1], A[2], 1],
                   [B[0], B[1], B[2], 1],
                   [C[0], C[1], C[2], 1],
                   [D[0], D[1], D[2], 1]])
V = Rational(1, 6) * V_matrix.det()

# Calculate the areas of the faces
Area_ABC = Rational(1, 2) * Matrix([[A[0], A[1], A[2]],
                                     [B[0], B[1], B[2]],
                                     [C[0], C[1], C[2]]]).det()
Area_ABD = Rational(1, 2) * (A[0] * B[1])
Area_ACD = Rational(1, 2) * (A[0] * C[2])
Area_BCD = Rational(1, 2) * (B[1] * C[2])

# Total surface area
S = Area_ABC + Area_ABD + Area_ACD + Area_BCD

# Calculate the radius of the inscribed sphere
r = (3 * V) / S

r

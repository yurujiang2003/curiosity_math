from sympy import Matrix

A = Matrix([2, 3, 0])
B = Matrix([0, 5, 4])
C = Matrix([4, 1, 8])

center = (A + B + C) / 3
center_coordinates = center.tolist()

center_coordinates

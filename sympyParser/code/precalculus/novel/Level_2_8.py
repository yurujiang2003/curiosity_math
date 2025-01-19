from sympy import Matrix

a, b = -3, 5
c, d = -2, 1

vector1 = Matrix([a, b])
vector2 = Matrix([c, d])

dot_product = vector1.dot(vector2)
dot_product

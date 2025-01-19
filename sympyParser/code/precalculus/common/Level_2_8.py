from sympy import Matrix

a = -3
b = 5
c = -2
d = 1

vector1 = Matrix([a, b])
vector2 = Matrix([c, d])

dot_product = vector1.dot(vector2)
dot_product

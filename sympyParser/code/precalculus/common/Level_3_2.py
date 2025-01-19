from sympy import Matrix, Rational

b = Matrix([2, 6, 3])
a_dot_b = 8
b_dot_b = b.dot(b)

proj_a_on_b = (a_dot_b / b_dot_b) * b
proj_a_on_b

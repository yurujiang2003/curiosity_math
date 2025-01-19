from sympy import symbols, Matrix, solve

x = symbols('x')
matrix = Matrix([[1, 1, 1], [x, 7, -2], [x**3, 343, -8]])
determinant = matrix.det()
equation = determinant.simplify()
roots = solve(equation, x)
roots

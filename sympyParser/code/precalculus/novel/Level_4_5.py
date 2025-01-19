from sympy import symbols, Matrix, Eq, solve

x = symbols('x')
det = Matrix([[1, 1, 1], [x, 7, -2], [x**3, 343, -8]]).det()
equation = Eq(det, 0)
solutions = solve(equation, x)
print(solutions)

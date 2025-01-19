from sympy import symbols, Eq, solve, I

x, y = symbols('x y')
eq1 = Eq(3*x - 4*y, 1)
eq2 = Eq(4*x + 3*y, -8)

solution = solve((eq1, eq2), (x, y))
z = solution[x] + solution[y] * I
z

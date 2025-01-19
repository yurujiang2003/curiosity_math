from sympy import symbols, Eq, solve

p, e = symbols('p e')
eq1 = Eq(3*p + e, 124)
eq2 = Eq(5*p + e, 182)

solution = solve((eq1, eq2), (p, e))
cost_of_pencil = solution[p]
cost_of_pencil

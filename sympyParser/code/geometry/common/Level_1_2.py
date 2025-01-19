from sympy import symbols, Eq, solve

r = symbols('r')
area = 40
equation = Eq(4 * r, area)
solution = solve(equation, r)
solution[0]

from sympy import symbols, Eq, solve

b = symbols('b')
lhs = (b + 3) * (b + 5)
rhs = 2 * b**2 + 4 * b + 3

equation = Eq(lhs, rhs)
solution = solve(equation, b)

positive_base = [sol for sol in solution if sol > 0]
positive_base[0]

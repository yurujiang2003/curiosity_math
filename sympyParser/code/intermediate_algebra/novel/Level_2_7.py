from sympy import symbols, solve, S

x = symbols('x')
inequality = (3**x - 7**x) >= 0
solution = solve(inequality, x)

domain = S.Reals.intersect(solution)
domain

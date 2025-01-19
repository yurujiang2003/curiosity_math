from sympy import symbols, solve, sqrt, S

x = symbols('x')
expr = 3**x - 7**x
inequality = expr >= 0

solution = solve(inequality, x)
domain = S.Reals.intersect(solution)

domain

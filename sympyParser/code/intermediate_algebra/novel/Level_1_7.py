from sympy import symbols, solve, S

x = symbols('x')
inequality = 1 / (x - 5) > 0
solution = solve(inequality, x)

interval = S.Reals.intersect(S.Interval.open(5, S.Infinity))
interval

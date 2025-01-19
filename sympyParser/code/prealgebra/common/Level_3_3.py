from sympy import symbols, Eq, solve

d, s = symbols('d s')
equation1 = Eq(d, (3/5) * s)
equation2 = Eq(d + s, 72)

solution = solve((equation1, equation2), (d, s))
dresses = solution[d]
dresses

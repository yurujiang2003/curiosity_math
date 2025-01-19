from sympy import symbols, Eq, solve

d, s = symbols('d s')
total_garments_eq = Eq(d + s, 72)
ratio_eq = Eq(5 * d, 3 * s)

solution = solve((total_garments_eq, ratio_eq), (d, s))
dresses = solution[d]
dresses

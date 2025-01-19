from sympy import symbols, Eq, solve

b, c = symbols('b c')
eq1 = Eq(2*b + c, -1)
eq2 = Eq(4*b + c, -13)

solution = solve((eq1, eq2), (b, c))
c_value = solution[c]
c_value

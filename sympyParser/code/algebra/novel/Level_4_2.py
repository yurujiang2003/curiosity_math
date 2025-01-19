from sympy import symbols, Eq, solve

b, c = symbols('b c')

# Equations based on the points (2, 3) and (4, 3)
eq1 = Eq(2*b + c, -1)
eq2 = Eq(4*b + c, -13)

# Solve the system of equations
solution = solve((eq1, eq2), (b, c))
c_value = solution[c]

c_value

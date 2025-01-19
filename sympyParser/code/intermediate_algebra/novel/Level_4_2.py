from sympy import symbols, Eq, solve

a1, d = symbols('a1 d')

# Given a_13 = 2016
a13 = a1 + 6*d
eq1 = Eq(a13, 2016)

# a_11 = a1 + 5d
a11 = a1 + 5*d
# a_12 = a1 + 6d
a12 = a1 + 6*d

# Geometric sequence property for k=7
eq2 = Eq(a12**2, a11 * (a1 + 7*d))

# Solve the equations
solutions = solve((eq1, eq2), (a1, d))
a1_value = solutions[0][0]
a1_value

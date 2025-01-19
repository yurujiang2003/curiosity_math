from sympy import symbols, Eq, solve

a, r = symbols('a r')
eq1 = Eq(a * r**3, 24)
eq2 = Eq(a * r**10, 3072)

# Dividing eq2 by eq1 to eliminate a
eq3 = Eq(eq2.lhs / eq1.lhs, eq2.rhs / eq1.rhs)

# Simplifying to find r
r_value = solve(eq3, r)[0]
r_value

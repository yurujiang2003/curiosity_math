from sympy import symbols, Eq, solve

r1 = symbols('r1')
a = 6 * r1
r2 = 9 * r1

# From a = r2 / (6 * r1**2)
eq1 = Eq(a, r2 / (6 * r1**2))

# Solve for r1
r1_value = solve(eq1, r1)[0]

# Calculate a
a_value = a.subs(r1, r1_value)
a_value

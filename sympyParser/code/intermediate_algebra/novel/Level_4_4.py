from sympy import symbols, Eq, solve

r = symbols('r')
eq1 = Eq(3 * r, 12)
eq2 = Eq(r**3, 64)

r_value = solve(eq1, r)[0]
a = 3 * (r_value**2)

a_value = a.subs(r, r_value)
a_value

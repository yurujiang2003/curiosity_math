from sympy import symbols, Eq, solve

r = symbols('r')
a1 = -r**2 - r + 2
b1 = r**3 - 2*r

# For r = 2
r1 = 2
a2 = a1.subs(r, r1)
b2 = b1.subs(r, r1)

# For r = -1
r2 = -1
a3 = a1.subs(r, r2)
b3 = b1.subs(r, r2)

quadratics = [(a2, b2), (a3, b3)]
distinct_quadratics = len(quadratics)

distinct_quadratics

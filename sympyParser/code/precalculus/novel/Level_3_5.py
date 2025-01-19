from sympy import symbols, Eq, solve

# Define variables
d, h = symbols('d h')
BC = 32

# Define the equations based on tangent definitions
eq1 = Eq(h, (3/2) * d)
eq2 = Eq(h, (1/2) * (BC - d))

# Solve for d
solution_d = solve(Eq(eq1.lhs, eq2.lhs), d)[0]

# Substitute d back to find h
h_value = eq1.subs(d, solution_d).rhs

# Calculate the area
area = (1/2) * BC * h_value
area_value = area.evalf()

area_value

from sympy import symbols, Eq, solve, Rational

a, d = symbols('a d')

# Equation (1)
eq1 = Eq(2*a + 4000*d, 50)

# Equation (2)
eq2 = Eq(d * (4000 - 40000*a), 10*a**2)

# Solve for d in terms of a from eq1
d_expr = solve(eq1, d)[0]

# Substitute d in eq2
eq2_substituted = eq2.subs(d, d_expr)

# Solve for a
a_solution = solve(eq2_substituted, a)

# Calculate d for each a
d_solutions = [d_expr.subs(a, sol) for sol in a_solution]

# Calculate a_1 and a_4001
a1 = a_solution[0]
a4001 = a1 + 4000*d_solutions[0]

# Calculate |a_1 - a_4001|
result = abs(a1 - a4001)
result

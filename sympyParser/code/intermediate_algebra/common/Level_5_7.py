from sympy import symbols, Eq, solve, simplify

a, b, c = symbols('a b c')

# Define the equations
eq1 = Eq(a + 3*b + 4*c, 25)
eq2 = Eq(a**2 + b**2 + c**2, 25)

# Solve for b and c in terms of a
b_expr = (25 - a - 4*c) / 3
eq2_substituted = eq2.subs(b, b_expr)

# Expand and simplify the second equation
eq2_expanded = simplify(eq2_substituted.lhs - eq2_substituted.rhs)

# Solve for c in terms of a
c_sol = solve(eq2_expanded, c)[0]

# Substitute c back to find b
b_sol = b_expr.subs(c, c_sol)

# Substitute b and c into the first equation to find a
final_eq = eq1.subs({b: b_sol, c: c_sol})
a_solution = solve(final_eq, a)

# Return the largest possible value of a
max_a = max(a_solution)
max_a

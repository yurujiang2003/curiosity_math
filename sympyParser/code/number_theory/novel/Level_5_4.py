from sympy import symbols, Eq, solve

n = symbols('n')
C, M = symbols('C M')

# Equations
eq1 = Eq(C + M, 8 * n)
eq2 = Eq(3 * M + 2 * C, 96)

# Solve for C in terms of M and n
C_expr = 8 * n - M

# Substitute C in the second equation
eq2_substituted = eq2.subs(C, C_expr)

# Solve for M in terms of n
M_solution = solve(eq2_substituted, M)[0]

# Solve for C in terms of n
C_solution = C_expr.subs(M, M_solution)

# Find the range for n
n_values = []
for value in range(5, 7):
    if M_solution.subs(n, value) > 0 and C_solution.subs(n, value) > 0:
        n_values.append(value)

# Return the final answer
n_values[0] if n_values else None

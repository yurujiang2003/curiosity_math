from sympy import symbols, Eq, solve

m, n = symbols('m n')
eq1 = Eq(3*m + 4*n, 47)
eq2 = Eq(m + n, 15)

n_expr = solve(eq2, n)[0]
eq1_substituted = eq1.subs(n, n_expr)

m_solution = solve(eq1_substituted, m)[0]
m_solution

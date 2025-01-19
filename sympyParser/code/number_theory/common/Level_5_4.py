from sympy import symbols, Eq, solve

M, C, n = symbols('M C n')

eq1 = Eq(M + C, 8 * n)
eq2 = Eq(3 * M + 2 * C, 96)

C_expr = solve(eq1, C)[0]
eq2_substituted = eq2.subs(C, C_expr)

M_expr = solve(eq2_substituted, M)[0]
C_expr_final = C_expr.subs(M, M_expr)

n_value = solve(Eq(M_expr, 96 - 16 * n), n)
n_value = [val for val in n_value if val > 4 and val < 6]

final_answer = n_value[0]
final_answer

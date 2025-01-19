from sympy import symbols, Eq, solve

a, r = symbols('a r')
eq1 = Eq(a * r**3, 24)
eq2 = Eq(a * r**10, 3072)

a_expr = solve(eq1, a)[0]
eq2_substituted = eq2.subs(a, a_expr)

r_solution = solve(eq2_substituted, r)[0]
final_answer = r_solution.evalf()

final_answer

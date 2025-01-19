from sympy import symbols, diff, solve, simplify

a, k = symbols('a k', positive=True)

g_k = (1 + k**2)**2 / k
g_k_derivative = diff(g_k, k)

critical_points = solve(g_k_derivative, k)
min_value = min(g_k.subs(k, cp) for cp in critical_points)

final_answer = simplify(min_value)
final_answer

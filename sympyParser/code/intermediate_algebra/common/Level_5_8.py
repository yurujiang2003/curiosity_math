from sympy import symbols, diff, solve, sqrt

a, b, t = symbols('a b t', positive=True)

y = (a**2 + b**2)**2 / (a**3 * b)
t = b / a
y_substituted = (1 + t**2)**2 / t

f_t = (1 + t**2)**2 / t
f_t_diff = diff(f_t, t)

critical_points = solve(f_t_diff, t)
valid_t = [cp.evalf() for cp in critical_points if cp > 0]

min_value = f_t.subs(t, valid_t[0])
final_answer = min_value.simplify()

final_answer

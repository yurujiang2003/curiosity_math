from sympy import symbols, solve, cbrt

x = symbols('x')
f = x**3 - 8

f_inv_19 = solve(f - 19, x)[0]
f_f_inv_19 = f.subs(x, f_inv_19)
f_inv_f_f_inv_19 = solve(f - f_f_inv_19, x)[0]

final_answer = f_inv_f_f_inv_19
final_answer

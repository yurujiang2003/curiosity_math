from sympy import symbols, simplify

x = symbols('x')
f = x**2 - 3
t = 9 + 2*f

f_neg2 = f.subs(x, -2)
t_result = t.subs(x, f_neg2).subs(f, f.subs(x, 1))

final_result = simplify(t_result)
final_result

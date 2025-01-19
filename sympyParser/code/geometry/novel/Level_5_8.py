from sympy import symbols, sqrt, Abs, solve

x, c = symbols('x c')
y = sqrt(3) * Abs(x - c/2)

AB = sqrt(x**2 + 3 * (x - c/2)**2)
EC = Abs(c - x)

ratio = AB / EC

c_value = 2
ratio_at_c = ratio.subs(c, c_value)

final_answer = ratio_at_c.simplify()
final_answer

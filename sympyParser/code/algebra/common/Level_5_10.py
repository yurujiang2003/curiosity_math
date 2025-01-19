from sympy import symbols, Piecewise, Max

x = symbols('x')
f = Piecewise((2, (x >= 1) & (x < 3)), (0, x == 3), (3, x == 3), (2, (x > 3) & (x < 5)), (0, x == 6))

max_value = Max(f.subs(x, 1), f.subs(x, 3), f.subs(x, 5), f.subs(x, 6))
max_value

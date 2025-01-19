from sympy import symbols, Eq, solve

x, y, a = symbols('x y a')
x_value = 3

eq1 = Eq(4*x_value - 3*y, 2*a)
eq2 = Eq(2*x_value + y, 3*a)

y_expr = solve(eq2, y)[0]
eq1_substituted = eq1.subs(y, y_expr)

a_solution = solve(eq1_substituted, a)[0]
a_solution

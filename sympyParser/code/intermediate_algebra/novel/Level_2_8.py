from sympy import symbols, diff, solve, N

x = symbols('x')
f = (x**7 + 32*x**2 + 128) / x**3

f_prime = diff(f, x)
critical_points = solve(f_prime, x)

min_value = N(f.subs(x, critical_points[0]))
min_value

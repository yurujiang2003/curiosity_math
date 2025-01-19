from sympy import symbols, diff, solve, Rational

x = symbols('x', positive=True)
f = x**4 + 32/x + 128/x**3

f_prime = diff(f, x)
critical_points = solve(f_prime, x)

g = x**7 - 8*x**2 - 96
root = 2  # We found x = 2 is a root

minimum_value = f.subs(x, root)
minimum_value

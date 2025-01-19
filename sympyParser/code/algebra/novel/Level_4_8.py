from sympy import symbols, Eq, solve, sqrt

x = symbols('x')
equation = Eq(x**4, 7*x**2 - 10)
rearranged_equation = Eq(x**4 - 7*x**2 + 10, 0)

z = symbols('z')
quadratic_equation = Eq(z**2 - 7*z + 10, 0)
solutions = solve(quadratic_equation, z)

m = max(solutions)
n = min(solutions)

result = m - n
result

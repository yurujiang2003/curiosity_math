from sympy import symbols, Eq, solve, sqrt

x = symbols('x')
equation = Eq(x**4, 7*x**2 - 10)
rearranged_equation = Eq(x**4 - 7*x**2 + 10, 0)

u = symbols('u')
substituted_equation = Eq(u**2 - 7*u + 10, 0)

solutions_u = solve(substituted_equation, u)
m = max(solutions_u)
n = min(solutions_u)

result = m - n
result

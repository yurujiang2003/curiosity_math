from sympy import symbols, sqrt, Eq, solve

x = symbols('x')
eq = Eq(sqrt(x**2 + sqrt(x**2 + 11)) + sqrt(x**2 - sqrt(x**2 + 11)), 4)

# Solve the equation
solutions = solve(eq, x)
solutions

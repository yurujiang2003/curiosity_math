from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq((x + 1) / (x - 1), (x - 2) / (x + 2))
solution = solve(equation, x)
solution

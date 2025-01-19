from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq((x + 26) + (2*x + 10), 180)
solution = solve(equation, x)
solution[0]

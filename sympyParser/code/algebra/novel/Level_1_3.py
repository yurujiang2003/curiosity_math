from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq(2/(3), 4/(x - 5))
solution = solve(equation, x)
solution[0]

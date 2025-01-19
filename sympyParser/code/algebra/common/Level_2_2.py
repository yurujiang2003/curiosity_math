from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq((x + 1) / (x - 1), (x - 2) / (x + 2))
solution = solve(equation, x)
valid_solution = [sol for sol in solution if (sol - 1) != 0 and (sol + 2) != 0]
valid_solution

from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq((4 * x**2)**(1/3), 4)
solution = solve(equation, x)
solution.sort()
solution

from sympy import symbols, Eq, solve, log

x = symbols('x')
equation = Eq(2**3 * 3**x, 72)
solution = solve(equation, x)
solution[0]

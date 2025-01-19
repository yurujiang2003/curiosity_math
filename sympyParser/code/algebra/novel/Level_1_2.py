from sympy import symbols, Eq, solve, Rational

x = symbols('x')
equation = Eq((Rational(3, 4))**x, Rational(81, 256))
solution = solve(equation, x)
solution[0]

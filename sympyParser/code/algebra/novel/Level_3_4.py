from sympy import symbols, Eq, solve, Rational

x = symbols('x')
equation = Eq(x**Rational(3, 2), 7**3)
solution = solve(equation, x)
solution[0]

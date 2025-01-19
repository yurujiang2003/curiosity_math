from sympy import symbols, Eq, solve, sqrt, cbrt

x = symbols('x')
equation = Eq(cbrt(x * sqrt(x)), 7)
solution = solve(equation, x)
solution[0]

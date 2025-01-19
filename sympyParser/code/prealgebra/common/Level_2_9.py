from sympy import symbols, Eq, solve

x, y = symbols('x y')
y_value = 1
equation = Eq(2*x + 3*y_value, 4)
solution = solve(equation, x)[0]
solution

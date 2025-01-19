from sympy import symbols, Eq, solve, simplify

x = symbols('x')
equation = Eq(2**3 * 3**x, 72)
simplified_equation = simplify(equation)

# Isolate 3^x
isolated_equation = Eq(3**x, 72 / 8)

# Solve for x
solution = solve(isolated_equation, x)
solution[0]

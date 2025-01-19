from sympy import symbols, Eq, solve

r = symbols('r')
area = 40
height = 8

equation = Eq((1/2) * r * height, area)
solution = solve(equation, r)

solution[0]

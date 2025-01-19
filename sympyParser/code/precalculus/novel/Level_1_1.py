from sympy import symbols, solve

a = symbols('a')
max_value = 3
min_value = -3

equation = a - max_value
solution = solve(equation, a)[0]
solution

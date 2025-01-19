from sympy import symbols, solve, S

x = symbols('x')
inequality = 6 - x > -9
solution = solve(inequality, x)

greatest_integer = int(solution[0]) - 1
greatest_integer

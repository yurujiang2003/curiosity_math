from sympy import symbols, solve, Abs

x = symbols('x')
inequality = Abs(x - 4) <= 3

solution = solve(inequality, x)
length = solution[1] - solution[0]
length

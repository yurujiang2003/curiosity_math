from sympy import symbols, solve, S

n = symbols('n')
inequality = 5*n + 3 > -10
solution = solve(inequality, n)

smallest_integer = S.Integers.filter(lambda x: x > solution[0]).args[0]
smallest_integer

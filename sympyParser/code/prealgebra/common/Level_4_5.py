from sympy import symbols, solve, S

n = symbols('n')
inequality = 5*n + 3 > -10
solution = solve(inequality, n)

smallest_integer = S.Integers.least(solution[0])
smallest_integer

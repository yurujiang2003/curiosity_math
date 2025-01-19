from sympy import symbols, solve

A = 100000
r = 0.06
t = 5
P = symbols('P')

equation = A - P * (1 + r)**t
solution = solve(equation, P)[0]

final_amount = round(solution)
final_amount

from sympy import symbols, solve, S, Interval

x = symbols('x')
inequality = 1 / (x - 5) > 0
solution = solve(inequality, x)

final_answer = Interval(5, S.Infinity)
final_answer

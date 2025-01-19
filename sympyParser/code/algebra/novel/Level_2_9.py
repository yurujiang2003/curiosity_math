from sympy import symbols, log, solve, sqrt

x = symbols('x')
equation = log(49, x) - 2
solution = solve(equation, x)
final_answer = [sol.evalf() for sol in solution if sol > 0]
final_answer

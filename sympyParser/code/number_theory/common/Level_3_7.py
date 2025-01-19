from sympy import symbols, Eq, solve, sqrt

b = symbols('b')
equation = Eq(3*b**2 + 2*b - 56, 0)
solutions = solve(equation, b)
valid_solutions = [sol.evalf() for sol in solutions if sol > 0]
final_answer = valid_solutions[0] if valid_solutions else None
final_answer

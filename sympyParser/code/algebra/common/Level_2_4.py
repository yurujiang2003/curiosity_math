from sympy import symbols, Eq, solve, Abs

x = symbols('x')
equation = Eq(Abs(4*x + 2), 10)

solutions = solve(equation, x)
valid_solution = [sol for sol in solutions if sol < 0]

final_answer = valid_solution[0] if valid_solution else None
final_answer

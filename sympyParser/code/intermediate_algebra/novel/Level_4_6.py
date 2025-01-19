from sympy import symbols, Eq, solve

a = symbols('a', positive=True)
equation = Eq((9 + a**2)**2, 100 * a)
solutions = solve(equation, a)
rational_solutions = [sol.evalf() for sol in solutions if sol.is_rational]
final_answer = rational_solutions
final_answer

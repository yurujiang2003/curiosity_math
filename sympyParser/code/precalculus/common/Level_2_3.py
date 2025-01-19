from sympy import symbols, Eq, sin, cos, solve, pi

x = symbols('x')
equation = Eq(tan(x), sin(x))
solutions = solve(equation, x)

# Filter solutions in the interval [0, 2*pi]
valid_solutions = [sol.evalf() for sol in solutions if 0 <= sol.evalf() <= 2*pi]

# Get unique solutions
unique_solutions = set(valid_solutions)
final_solutions = sorted(unique_solutions)

final_solutions

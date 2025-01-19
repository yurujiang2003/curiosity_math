from sympy import symbols, Eq, sin, cos, solve, pi

x = symbols('x')
equation = Eq(tan(x), sin(x))

# Solve the equation
solutions = solve(equation, x)

# Include the case when sin(x) = 0
zero_solutions = [0, pi, 2*pi]

# Combine all solutions
all_solutions = set(solutions).union(zero_solutions)

# Filter solutions within the interval [0, 2*pi]
final_solutions = [sol.evalf() for sol in all_solutions if 0 <= sol.evalf() <= 2*pi]

final_solutions

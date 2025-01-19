from sympy import symbols, sqrt, Eq, solve

a = symbols('a')
# Set up the equation derived from the minimum value condition
equation = Eq(a**2 + 4*a + 1, 0)
# Solve for a
solutions = solve(equation, a)
# Filter valid solutions
valid_solutions = [sol.evalf() for sol in solutions if sol > -2]
# Return the final answer
valid_solutions

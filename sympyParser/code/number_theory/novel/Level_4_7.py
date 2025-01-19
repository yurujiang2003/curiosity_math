from sympy import symbols, Eq, solve

b = symbols('b')
# Convert 13_b and 15_b to decimal
expr1 = (b + 3) * (b + 5)
# Convert 243_b to decimal
expr2 = 2 * b**2 + 4 * b + 3
# Set the two expressions equal to each other
equation = Eq(expr1, expr2)
# Rearranging the equation
rearranged_equation = Eq(0, expr2 - expr1)
# Solve for b
solutions = solve(rearranged_equation, b)
# Filter for positive solutions
positive_solutions = [sol for sol in solutions if sol > 0]
# Return the final answer
positive_solutions[0]

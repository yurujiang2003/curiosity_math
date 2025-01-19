from sympy import symbols, Eq, solve

a = symbols('a')

# Case 1: Assume 6a + 1 is the longest side
eq1 = Eq((6*a + 1)**2, (a + 1)**2 + (6*a)**2)
solution1 = solve(eq1, a)

# Filter valid solutions
valid_solutions = [sol.evalf() for sol in solution1 if sol >= 0]

valid_solutions

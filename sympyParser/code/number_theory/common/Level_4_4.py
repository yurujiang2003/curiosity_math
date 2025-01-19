from sympy import symbols, Eq, solve

A, B = symbols('A B', integer=True)

# Set up the equation based on the derived equation A - B = 1
equation = Eq(A - B, 1)

# Solve for the nonnegative difference
solution = solve(equation, A)[0] - B

# Return the absolute value of the difference
result = abs(solution)
result

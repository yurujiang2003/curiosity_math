from sympy import symbols, Eq, solve

A, B = symbols('A B', integer=True)

# Set up the equation based on the derived expression
equation = Eq(A - B, 1)

# Solve the equation
solution = solve(equation, A)

# Calculate the nonnegative difference
nonnegative_difference = abs(solution[0] - B)

nonnegative_difference

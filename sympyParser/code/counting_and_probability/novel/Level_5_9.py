from sympy import symbols, Eq, solve

# Define variables
a, b, c = symbols('a b c')

# Given equations based on the problem
eq1 = Eq(a + b, 22)  # Basketball
eq2 = Eq(a + c, 12)  # Soccer
eq3 = Eq(b + c, 32)  # Mathletics

# Solve the equations
solution = solve((eq1, eq2, eq3), (a, b, c))

# Extract values
a_val = solution[a]
b_val = solution[b]
c_val = solution[c]

# Calculate total number of students playing exactly two teams
total_exactly_two = a_val + b_val + c_val

total_exactly_two

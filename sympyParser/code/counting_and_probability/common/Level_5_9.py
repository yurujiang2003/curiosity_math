from sympy import symbols, Eq, solve

# Define variables
x = symbols('x')
B = 3 * x
S = 2 * x
M = 4 * x

# Total students equation
total_students_eq = Eq(B + S + M - (symbols('B_and_S') + symbols('B_and_M') + symbols('S_and_M')) + 8, 60)

# Solve for x
x_value = solve(total_students_eq, x)[0]

# Calculate B, S, M
B_value = B.subs(x, x_value)
S_value = S.subs(x, x_value)
M_value = M.subs(x, x_value)

# Calculate intersection terms
intersection_sum = 9 * x_value - 52

# Let a, b, c be the number of students in the respective pairs (exactly two teams)
a, b, c = symbols('a b c')
exactly_two_teams_eq = Eq(a + b + c + 24, intersection_sum)

# Solve for a + b + c
exactly_two_teams = solve(exactly_two_teams_eq, a + b + c)[0]

# Return the final answer
exactly_two_teams

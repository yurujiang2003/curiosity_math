from sympy import symbols, Eq, solve

# Define the variable
N = symbols('N')

# Define the congruences
congruence1 = Eq(N % 4, 0)
congruence2 = Eq(N % 3, 2)
congruence3 = Eq(N % 11, 5)

# Solve the first two congruences
k = symbols('k')
N_expr = 3*k + 2
equation1 = Eq(N_expr % 4, 0)
solution_k = solve(equation1, k)[0]

# Substitute back to find N
N_substituted = N_expr.subs(k, solution_k)
N_expr_final = N_substituted

# Solve the third congruence
p = symbols('p')
N_expr_final = 12*p + 8
equation2 = Eq(N_expr_final % 11, 5)
solution_p = solve(equation2, p)[0]

# Substitute back to find N
N_final = N_expr_final.subs(p, solution_p)

# Find values around 200
possible_N = [N_final.subs('q', q) for q in range(2)]
final_values = [n for n in possible_N if 180 < n < 220]

final_values

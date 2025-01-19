from sympy import symbols, Eq, solve

N = symbols('N')
k = symbols('k')
m = symbols('m')
n = symbols('n')

# Conditions
eq1 = Eq(N % 4, 0)
eq2 = Eq(N % 3, 2)
eq3 = Eq(N % 11, 5)

# Express N in terms of k
N_expr = 3*k + 2

# Substitute into the second condition
eq2_substituted = eq2.subs(N, N_expr)

# Solve for k
k_solution = solve(eq2_substituted, k)[0]

# Express k in terms of m
k_expr = 11*m + 1

# Substitute back to find N
N_final_expr = N_expr.subs(k, k_expr)

# Now express N in terms of n
N_final_expr = N_final_expr.subs(m, 4*n)

# Find N around 200
possible_N = [N_final_expr.subs(n, i) for i in range(3)]

# Filter valid N
valid_N = [N_val for N_val in possible_N if N_val >= 200]

# Return the valid N
valid_N

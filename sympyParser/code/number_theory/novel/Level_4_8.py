from sympy import symbols, Eq, solve

k_values = range(1, 6)
no_solution_count = 0

for k in k_values:
    if k % 3 != 0:
        no_solution_count += 1

no_solution_count

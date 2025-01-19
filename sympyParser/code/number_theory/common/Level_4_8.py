from sympy import symbols, mod

k_values = [1, 2, 3, 4, 5]
no_solution_count = 0

for k in k_values:
    if k % 3 != 0:
        no_solution_count += 1

no_solution_count

from sympy import symbols, solve, Abs

m, n, k = symbols('m n k')
equation = 3*m + 4*n - 100

# Express n in terms of m
n_expr = (100 - 3*m) / 4

# m must be of the form 4k
k_values = [3, 4]
min_value = float('inf')

for k in k_values:
    m_val = 4*k
    n_val = 25 - 3*k
    abs_diff = Abs(m_val - n_val)
    if abs_diff < min_value:
        min_value = abs_diff

min_value

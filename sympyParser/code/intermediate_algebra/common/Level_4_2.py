from sympy import symbols, Eq, solve

# Define variables
a1, d, k = symbols('a1 d k')

# Given condition
a_13 = a1 + 12 * d
eq1 = Eq(a_13, 2016)

# Define the geometric condition
a_2k_minus_1 = a1 + (k - 1) * d
a_2k = a1 + k * d
a_2k_plus_1 = a1 + (k + 1) * d

# Geometric condition equation
geometric_eq = Eq(a_2k**2, a_2k_minus_1 * a_2k_plus_1)

# Arithmetic condition
a_2k_plus_2 = 2 * a_2k_plus_1 - a_2k
arithmetic_eq = Eq(a_2k_plus_2, a1 + (k + 2) * d)

# Solve for a1 and d
solutions = solve((eq1, geometric_eq.subs(k, 1)), (a1, d))
a1_value = solutions[a1]

# Output the result
a1_value

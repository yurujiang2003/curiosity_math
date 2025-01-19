from sympy import ceiling, floor

# Define the range for two-digit numbers
lower_bound = 10
upper_bound = 99

# Finding N (the least positive two-digit multiple of 13)
k_N = ceiling(lower_bound / 13)
N = 13 * k_N

# Finding M (the greatest positive two-digit multiple of 13)
k_M = floor(upper_bound / 13)
M = 13 * k_M

# Calculating M + N
result = M + N
result

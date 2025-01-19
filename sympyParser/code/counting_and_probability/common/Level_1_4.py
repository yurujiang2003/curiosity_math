from sympy import ceiling, floor

# Define the range of three-digit integers
lower_bound = 100
upper_bound = 999

# Calculate the smallest three-digit multiple of 11
smallest_multiple = 11 * ceiling(lower_bound / 11)

# Calculate the largest three-digit multiple of 11
largest_multiple = 11 * floor(upper_bound / 11)

# Determine the range of n
n_min = smallest_multiple // 11
n_max = largest_multiple // 11

# Calculate the number of integers from n_min to n_max
count = n_max - n_min + 1

# Return the final answer
count

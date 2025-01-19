from sympy import ceiling, floor

# Define the range of three-digit integers
lower_bound = 100
upper_bound = 999

# Find the smallest three-digit multiple of 11
smallest_multiple = ceiling(lower_bound / 11) * 11

# Find the largest three-digit multiple of 11
largest_multiple = floor(upper_bound / 11) * 11

# Define the first term, common difference, and last term
a = smallest_multiple
d = 11
l = largest_multiple

# Calculate the number of terms in the arithmetic sequence
n = (l - a) // d + 1

# Return the final answer
n

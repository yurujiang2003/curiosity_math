from sympy import sqrt, ceiling, floor

# Define the range
lower_bound = 200
upper_bound = 300

# Finding the smallest perfect square ≥ 200
smallest_integer = ceiling(sqrt(lower_bound))
smallest_perfect_square = smallest_integer**2

# Finding the largest perfect square ≤ 300
largest_integer = floor(sqrt(upper_bound))
largest_perfect_square = largest_integer**2

# Counting the perfect squares between the two bounds
perfect_squares_count = largest_integer - smallest_integer + 1

# Return the final answer
perfect_squares_count

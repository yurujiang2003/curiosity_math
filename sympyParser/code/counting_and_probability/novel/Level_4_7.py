from sympy import factorial

# Define the number of people
n = 6

# Treat John and Sam as a single unit
units = n - 1  # 5 units (John-Sam block + 4 other people)

# Calculate the arrangements in a circle
arrangements = factorial(units - 1)  # (5-1)!

# Calculate the arrangements of John and Sam within their block
internal_arrangements = 2  # John can be on the left or Sam can be on the left

# Total arrangements
total_arrangements = arrangements * internal_arrangements

total_arrangements

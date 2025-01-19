from sympy import factorial

# Number of people
n = 6

# Treat John and Sam as a single block
blocks = n - 1  # 5 blocks

# Arrangements in a circle
circular_arrangements = factorial(blocks - 1)

# Arrangements within the John-Sam block
internal_arrangements = 2

# Total arrangements
total_arrangements = circular_arrangements * internal_arrangements
total_arrangements

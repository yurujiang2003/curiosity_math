from sympy import binomial

# Define the number of switches
n = 8

# Case 1: One bank of lights on
case_1 = binomial(n, 1)

# Case 2: Two banks of lights on
case_2 = binomial(n, 2)

# Total combinations
total_ways = case_1 + case_2

# Return the final answer
total_ways

from sympy import binomial

# Define the number of Republicans and Democrats
num_republicans = 55
num_democrats = 45

# Calculate combinations
combinations_republicans = binomial(num_republicans, 3)
combinations_democrats = binomial(num_democrats, 2)

# Calculate total ways to form the committee
total_ways = combinations_republicans * combinations_democrats

# Return the final answer
total_ways

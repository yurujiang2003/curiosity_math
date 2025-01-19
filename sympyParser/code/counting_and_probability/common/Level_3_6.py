from sympy import binomial

# Define the number of Republicans and Democrats
num_republicans = 55
num_democrats = 45

# Calculate the number of ways to choose 3 Republicans from 55
ways_republicans = binomial(num_republicans, 3)

# Calculate the number of ways to choose 2 Democrats from 45
ways_democrats = binomial(num_democrats, 2)

# Calculate the total number of ways to form the committee
total_ways = ways_republicans * ways_democrats

# Return the final answer
total_ways

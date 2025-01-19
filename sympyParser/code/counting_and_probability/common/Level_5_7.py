from sympy import binomial

# Variables
n_apples = 3
n_oranges = 3
k_friends_apples = 4
k_friends_oranges = 3

# Step 1: Distributing the Apples
ways_apples = binomial(n_apples + k_friends_apples - 1, k_friends_apples - 1)

# Step 2: Distributing the Oranges
ways_oranges = binomial(n_oranges + k_friends_oranges - 1, k_friends_oranges - 1)

# Final Calculation
total_ways = ways_apples * ways_oranges

total_ways

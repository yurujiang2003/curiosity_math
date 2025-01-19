from sympy import binomial

# Step 1: Distributing Apples
n_apples = 3
k_friends = 4
ways_apples = binomial(n_apples + k_friends - 1, k_friends - 1)

# Step 2: Distributing Oranges
n_oranges = 3
k_friends_oranges = 3  # Only 3 friends can receive oranges
ways_oranges = binomial(n_oranges + k_friends_oranges - 1, k_friends_oranges - 1)

# Final Calculation: Combining the Two Parts
total_ways = ways_apples * ways_oranges
total_ways

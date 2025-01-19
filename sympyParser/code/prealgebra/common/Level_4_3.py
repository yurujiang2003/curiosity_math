from sympy import symbols, floor

# Define the upper limit
upper_limit = 20

# Calculate the number of positive multiples of 3 less than 20
n_multiples_of_3 = floor((upper_limit - 1) / 3)

# Calculate the number of positive multiples of 6 less than 20
n_multiples_of_6 = floor((upper_limit - 1) / 6)

# Subtract the two results
result = n_multiples_of_6 - n_multiples_of_3

result

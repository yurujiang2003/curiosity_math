from sympy import *

# Define variables
average_original = 13
number_of_weights = 5
new_weight = 7

# Calculate total weight of the original five weights
total_weight = average_original * number_of_weights

# Add the new weight
new_total_weight = total_weight + new_weight

# Calculate the new average
new_average = new_total_weight / (number_of_weights + 1)

# Return the final answer
new_average

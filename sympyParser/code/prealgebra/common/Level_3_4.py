from sympy import symbols, Rational

# Define variables
average_five_weights = 13
number_of_weights = 5
new_weight = 7

# Calculate total weight of five weights
total_weight_five = average_five_weights * number_of_weights

# Add the new weight
total_weight_six = total_weight_five + new_weight

# Calculate average of six weights
average_six_weights = total_weight_six / (number_of_weights + 1)

# Return the final answer
average_six_weights.evalf()

from sympy import symbols

# Define variables
average_1, count_1 = 30, 20
average_2, count_2 = 20, 30

# Calculate total sums
total_sum_1 = average_1 * count_1
total_sum_2 = average_2 * count_2

# Combine sums
total_sum_all = total_sum_1 + total_sum_2

# Calculate average of all numbers
count_all = count_1 + count_2
average_all = total_sum_all / count_all

# Return the final answer
average_all

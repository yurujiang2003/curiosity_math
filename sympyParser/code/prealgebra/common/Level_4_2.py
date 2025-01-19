from sympy import symbols, Rational

# Define variables
avg1, count1 = 30, 20
avg2, count2 = 20, 30

# Calculate total sums
sum1 = avg1 * count1
sum2 = avg2 * count2

# Calculate total sum of all numbers
total_sum = sum1 + sum2

# Calculate average of all numbers
total_count = count1 + count2
average_all = total_sum / total_count

average_all

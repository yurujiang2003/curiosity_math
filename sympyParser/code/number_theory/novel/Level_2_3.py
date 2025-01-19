from sympy import *

# Define the coefficients and powers of ten
a1, a2 = 9.2, 8
p1, p2 = 2, 6

# Calculate the product of coefficients and powers of ten
coefficient_product = a1 * a2
power_product = p1 + p2

# Combine the results
combined_result = coefficient_product * 10**power_product

# Convert coefficient to standard form
standard_coefficient = coefficient_product / 10**(len(str(int(coefficient_product))) - 1)
exponent_adjustment = len(str(int(coefficient_product))) - 1

# Final result in standard form
final_result = standard_coefficient * 10**(power_product + exponent_adjustment)

# Count the number of zeroes
number_of_zeroes = power_product + exponent_adjustment

number_of_zeroes

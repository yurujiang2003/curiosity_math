from sympy import *

# Define the coefficients and exponents
coeff1 = 9.2
exp1 = 2
coeff2 = 8
exp2 = 6

# Multiply the coefficients
product_coeff = coeff1 * coeff2

# Add the exponents of 10
product_exp = exp1 + exp2

# Combine the results
final_coeff = product_coeff * 10**product_exp

# Convert to standard form
standard_coeff = final_coeff / 10**(product_exp)
standard_exp = product_exp + 1

# Count the number of zeros
num_zeros = standard_exp - 1

# Return the final answer
num_zeros

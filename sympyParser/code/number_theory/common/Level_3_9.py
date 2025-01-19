from sympy import *

# Calculate the product
product = 5 * 6 * 7 * 8 * 9 * 10

# Convert the product to a string to find the hundreds digit
product_str = str(product)

# Get the hundreds digit
hundreds_digit = int(product_str[-3])

# Return the final answer
hundreds_digit

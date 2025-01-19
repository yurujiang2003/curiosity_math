from sympy import *

# Calculate the product
product = 5 * 6 * 7 * 8 * 9 * 10

# Convert the product to a string to find the hundreds digit
product_str = str(product)

# The hundreds digit is the third digit from the right
hundreds_digit = int(product_str[-3])

# Return the final answer
hundreds_digit

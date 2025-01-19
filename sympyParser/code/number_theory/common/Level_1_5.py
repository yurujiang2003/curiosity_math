from sympy import *

# Define the variables
dividend = 2003
divisor = 11

# Perform the division
integer_part = floor(dividend / divisor)

# Calculate the product of the integer part and the divisor
product = integer_part * divisor

# Calculate the remainder
remainder = dividend - product

# Return the final answer
remainder

from sympy import floor

# Define the variables
num = 2003
divisor = 11

# Calculate the quotient
quotient = floor(num / divisor)

# Calculate the product of the quotient and the divisor
product = quotient * divisor

# Calculate the remainder
remainder = num - product

# Return the final answer
remainder

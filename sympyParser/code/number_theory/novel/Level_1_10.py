from sympy import *

# Define the variables
a = 71
b = 3

# Calculate the quotient
quotient = a // b

# Calculate the largest multiple of b less than or equal to a
largest_multiple = quotient * b

# Calculate the remainder
remainder = a - largest_multiple

# Return the final answer
remainder

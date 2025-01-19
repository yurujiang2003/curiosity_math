from sympy import *

# Define binary numbers
binary_numbers = ['1', '11', '111', '1111']

# Convert binary to decimal and sum
decimal_sum = sum(int(b, 2) for b in binary_numbers)

# Convert the sum back to binary
binary_result = bin(decimal_sum)[2:]

binary_result

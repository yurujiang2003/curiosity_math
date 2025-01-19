from sympy import *

# Define the binary numbers
numbers = ['1', '11', '111', '1111']

# Convert binary numbers to decimal and sum them
decimal_sum = sum(int(num, 2) for num in numbers)

# Convert the sum back to binary
binary_sum = bin(decimal_sum)[2:]

# Return the final answer
binary_sum

from sympy import *

# Define the odd numbers
odd_numbers = [1, 3, 5, 7, 9, 11, 13]

# Initialize the product
product = 1

# Calculate the product focusing on the ones digit
for number in odd_numbers:
    product = (product * number) % 10

# Return the final answer
product

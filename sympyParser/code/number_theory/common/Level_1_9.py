from sympy import *

# Define the factors
factors = [1, 3, 5, 7, 9, 11, 13]

# Initialize the product
product = 1

# Calculate the product while keeping track of the ones digit
for factor in factors:
    product = (product * factor) % 10

# Return the final answer
product

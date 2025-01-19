from sympy import symbols, factorint

# Define the numbers
numbers = [2, 4, 6, 8, 10, 12]

# Calculate the product
product = 1
for number in numbers:
    product *= number

# Get the prime factorization
factors = factorint(product)

# Calculate the number of perfect square factors
perfect_square_factors = 1
for exponent in factors.values():
    perfect_square_factors *= (exponent // 2 + 1)

# Return the final answer
perfect_square_factors

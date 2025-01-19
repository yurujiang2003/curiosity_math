from sympy import symbols, factorint, prod

# Define the numbers
numbers = [2, 4, 6, 8, 10, 12]

# Calculate the product
product = prod(numbers)

# Get the prime factorization
factorization = factorint(product)

# Count the number of perfect square factors
perfect_square_factors_count = 1
for prime, exponent in factorization.items():
    # Count even exponents
    perfect_square_factors_count *= (exponent // 2 + 1)

# Return the final answer
perfect_square_factors_count

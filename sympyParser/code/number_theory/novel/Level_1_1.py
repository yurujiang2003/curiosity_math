from sympy import primerange, max

# Get all prime numbers less than 40
primes = list(primerange(1, 40))

# Find the two largest distinct primes
largest_primes = sorted(primes)[-2:]

# Calculate the product
greatest_product = largest_primes[0] * largest_primes[1]

# Return the final answer
greatest_product

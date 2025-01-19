from sympy import symbols, binomial

# Define the number of prime factors
n = 5

# Calculate the number of ways to choose 3 distinct primes from 5
result = binomial(n, 3)

# Return the final answer
result

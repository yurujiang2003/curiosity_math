from sympy import symbols, binomial

# Define the number of distinct prime factors
n_primes = 5

# Calculate the number of ways to choose 3 primes from 5
num_sets = binomial(n_primes, 3)

# Return the final answer
num_sets

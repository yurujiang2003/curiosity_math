from sympy import Rational

# Define the first six prime numbers
primes = [2, 3, 5, 7, 11, 13]

# Count even and odd primes
even_count = 1  # Only the prime number 2
odd_count = len(primes) - even_count  # 5 odd primes

# Total outcomes
total_outcomes = len(primes) ** 2

# Favorable outcomes (both choose odd primes)
favorable_outcomes = odd_count ** 2

# Calculate the probability
probability_even_sum = Rational(favorable_outcomes, total_outcomes)

# Return the final answer
probability_even_sum

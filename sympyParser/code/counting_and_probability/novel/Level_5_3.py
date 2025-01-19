from sympy import Rational

# Define the number of primes and categorize them
total_primes = 6
even_primes = 1
odd_primes = 5

# Calculate total outcomes
total_outcomes = total_primes * total_primes

# Calculate favorable outcomes (both numbers are odd)
favorable_outcomes = odd_primes * odd_primes

# Calculate probability
probability = Rational(favorable_outcomes, total_outcomes)

# Return the final answer
probability

from sympy import Rational

# Total outcomes when rolling two 6-sided dice
total_outcomes = 6 * 6

# Successful outcomes that sum to 7
successful_outcomes = 6

# Calculate the probability
probability = Rational(successful_outcomes, total_outcomes)

# Return the final answer
probability

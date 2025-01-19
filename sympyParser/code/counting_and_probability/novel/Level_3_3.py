from sympy import Rational

# Total outcomes when rolling two cubes
total_outcomes = 6 * 6

# Favorable outcomes
favorable_outcomes = (3 * 3) + (3 * 3)

# Probability calculation
probability = Rational(favorable_outcomes, total_outcomes)

# Return the final answer
probability

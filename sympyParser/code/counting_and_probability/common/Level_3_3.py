from sympy import Rational

# Total outcomes when rolling two cubes
total_outcomes = 6 * 6

# Favorable outcomes
favorable_outcomes_case1 = 3 * 3  # First cube red, second cube white
favorable_outcomes_case2 = 3 * 3  # First cube white, second cube red

# Total favorable outcomes
total_favorable_outcomes = favorable_outcomes_case1 + favorable_outcomes_case2

# Probability
probability = Rational(total_favorable_outcomes, total_outcomes)

# Return the final answer
probability

from sympy import binomial, Rational

# Step 1: Calculate total combinations of choosing 3 cards from 52
total_outcomes = binomial(52, 3)

# Step 2: Calculate the number of favorable outcomes for forming a pair
favorable_outcomes = binomial(13, 1) * binomial(4, 2) * binomial(12, 1) * 4

# Step 3: Calculate the probability
probability_pair = Rational(favorable_outcomes, total_outcomes)

# Step 4: Return the final answer
probability_pair

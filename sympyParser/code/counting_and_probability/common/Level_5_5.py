from sympy import Rational, binomial

# Define the sets
tina_set = {1, 2, 3, 4, 5}
sergio_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Calculate the number of ways Tina can choose 2 distinct numbers
tina_choices = binomial(len(tina_set), 2)

# Possible sums from Tina's choices
sums = [sum(pair) for pair in [(x, y) for x in tina_set for y in tina_set if x < y]]

# Count favorable outcomes for each sum
favorable_outcomes = 0
for s in sums:
    favorable_outcomes += len([num for num in sergio_set if num > s])

# Total outcomes
total_outcomes = tina_choices * len(sergio_set)

# Calculate probability
probability = Rational(favorable_outcomes, total_outcomes)

# Return the final answer
probability

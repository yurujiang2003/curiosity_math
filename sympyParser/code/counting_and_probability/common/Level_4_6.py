from sympy import binomial, factorial

# Step 1: Count the arrangements without considering symmetry
n_beads = 8
k_beads = 5

# Choose 5 beads out of 8
combinations = binomial(n_beads, k_beads)
# Arrange the 5 beads
arrangements = factorial(k_beads)

# Total arrangements without considering symmetry
total_arrangements = combinations * arrangements

# Step 2: Account for symmetries using Burnside's Lemma
# Rotations
rotation_contribution = total_arrangements / k_beads

# Reflections
reflection_contribution = 0

# Final Calculation
distinct_arrangements = rotation_contribution + reflection_contribution

distinct_arrangements

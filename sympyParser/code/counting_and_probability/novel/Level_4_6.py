from sympy import symbols, simplify

# Define the variables
n_beads = 8
k_beads = 5

# Calculate fixed arrangements under rotations
fixed_rotations = n_beads**k_beads

# Calculate fixed arrangements under reflections
fixed_reflections = 5 * (n_beads - 1)**(k_beads - 2)

# Total fixed arrangements
total_fixed = fixed_rotations + fixed_reflections

# Apply Burnside's lemma
distinct_necklaces = total_fixed / (k_beads * 2)

# Return the final answer
distinct_necklaces.evalf()

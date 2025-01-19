from sympy import *

# Define the range
start = 25
end = 250

# Count total integers
total_integers = end - start + 1

# Count perfect cubes
n_start = ceil(start**(1/3))
n_end = floor(end**(1/3))

perfect_cubes_count = n_end - n_start + 1

# Calculate not perfect cubes
not_perfect_cubes = total_integers - perfect_cubes_count

not_perfect_cubes

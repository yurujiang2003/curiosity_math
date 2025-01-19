from sympy import *

# Define the range
start = 25
end = 250

# Total count of integers from start to end
total_count = end - start + 1

# Find the smallest integer n such that n^3 >= start
n = ceil(start**(1/3))

# Find the largest integer m such that m^3 <= end
m = floor(end**(1/3))

# Count the perfect cubes in the range
perfect_cubes_count = m - n + 1

# Count of integers that are not perfect cubes
not_perfect_cubes_count = total_count - perfect_cubes_count

not_perfect_cubes_count

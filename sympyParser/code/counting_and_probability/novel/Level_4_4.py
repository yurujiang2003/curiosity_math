from sympy import factorial, Pow

# Define the number of planes and runways
num_planes = 3
num_runways = 2

# Calculate the number of arrangements and runway combinations
arrangements = factorial(num_planes)
runway_combinations = Pow(num_runways, num_planes)

# Calculate the total ways
total_ways = arrangements * runway_combinations

# Return the final answer
total_ways

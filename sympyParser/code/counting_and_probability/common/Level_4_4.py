from sympy import factorial, Pow

# Define the number of planes and runways
num_planes = 3
num_runways = 2

# Calculate the number of arrangements of the planes
arrangements = factorial(num_planes)

# Calculate the number of runway assignments
runway_assignments = Pow(num_runways, num_planes)

# Calculate the total ways to schedule the takeoffs
total_ways = arrangements * runway_assignments

total_ways

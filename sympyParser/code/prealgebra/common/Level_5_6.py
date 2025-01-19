from sympy import symbols, Rational

# Define variables
time_hours = 2.5
distance_km = 1
time_seconds_hallway = 90

# Convert time from hours to seconds
time_seconds = time_hours * 3600

# Calculate speed in meters per second
speed = distance_km * 1000 / time_seconds

# Calculate the length of the hallway
length_hallway = speed * time_seconds_hallway

# Return the final answer
length_hallway.evalf()

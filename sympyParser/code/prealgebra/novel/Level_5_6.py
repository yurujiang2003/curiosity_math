from sympy import symbols, Rational

# Define variables
time_hours = 2.5
time_seconds = 90

# Convert hours to seconds
time_seconds_robot = time_hours * 3600

# Calculate speed in meters per second
speed = Rational(1000, time_seconds_robot)  # 1 kilometer = 1000 meters

# Calculate length of the hallway
length_hallway = speed * time_seconds

# Return the final answer
length_hallway.evalf()

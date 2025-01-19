from sympy import lcm

# Define the blinking intervals
red_light = 2
yellow_light = 3
blue_light = 5

# Calculate the least common multiple (LCM)
lcm_blink = lcm(red_light, yellow_light, blue_light)

# Convert seven minutes into seconds
seven_minutes = 7 * 60

# Calculate how many times the LCM fits into the total seconds
num_blinks = seven_minutes // lcm_blink

# Include the initial blink at t = 0
total_blinks = num_blinks + 1

# Return the final answer
total_blinks

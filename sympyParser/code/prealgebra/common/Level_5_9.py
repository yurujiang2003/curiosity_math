from sympy import lcm

# Define the blinking intervals
red_light = 2
yellow_light = 3
blue_light = 5

# Calculate the LCM of the intervals
interval_lcm = lcm(red_light, yellow_light, blue_light)

# Total duration of the dance in seconds
dance_duration = 7 * 60

# Calculate the number of times they blink together
blinks_together = dance_duration // interval_lcm

# Include the very beginning
total_blinks = blinks_together + 1

# Return the final answer
total_blinks

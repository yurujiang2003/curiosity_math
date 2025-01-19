from sympy import symbols, Abs

# Define variables
minutes = 20
hour = 4

# Calculate the position of the minute hand
minute_angle = (360 / 60) * minutes

# Calculate the position of the hour hand
hour_angle_at_4 = hour * 30
additional_hour_movement = (30 / 60) * minutes
hour_angle = hour_angle_at_4 + additional_hour_movement

# Calculate the angle between the two hands
angle_between_hands = Abs(hour_angle - minute_angle)

# Return the final answer
angle_between_hands.evalf()

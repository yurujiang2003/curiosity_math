from sympy import symbols, Abs

# Define the variables
hour = 4
minutes = 20

# Calculate the position of the hour hand
hour_hand_position = hour * 30 + minutes * 0.5

# Calculate the position of the minute hand
minute_hand_position = minutes * 6

# Calculate the angle between the two hands
angle_between_hands = Abs(hour_hand_position - minute_hand_position)

# Return the final answer
angle_between_hands.evalf()

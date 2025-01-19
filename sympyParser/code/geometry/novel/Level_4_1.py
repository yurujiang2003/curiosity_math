from sympy import sin, pi, sqrt

# Define the angle in degrees
angle_deg = 1755

# Reduce the angle to the range [0, 360)
reduced_angle = angle_deg % 360

# Calculate the sine of the reduced angle
result = sin(reduced_angle * pi / 180)

# Return the final answer
result

from sympy import tan, pi, sqrt

# Define the angle in degrees
angle_deg = 240

# Convert degrees to radians
angle_rad = angle_deg * (pi / 180)

# Compute the tangent
result = tan(angle_rad)

# Return the final answer
result.evalf()

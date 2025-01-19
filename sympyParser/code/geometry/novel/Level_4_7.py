from sympy import sqrt, tan, pi

# Define the angle in degrees
angle = 300

# Calculate the reference angle
reference_angle = 360 - angle

# Calculate the tangent of the reference angle
tan_reference = tan(reference_angle * pi / 180)

# Since tangent is negative in the fourth quadrant
tan_300 = -tan_reference

# Final result
result = tan_300.evalf()
result

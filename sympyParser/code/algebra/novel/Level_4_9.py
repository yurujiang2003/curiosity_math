from sympy import Rational, Abs

# Define the coordinates of Annie and Barbara's initial locations
annie_location = (3, 5)
barbara_initial_location = (-6, 2)
barbara_correct_location = (-10, 4)

# Calculate the agreed meeting point (midpoint)
agreed_midpoint_x = Rational(annie_location[0] + barbara_initial_location[0], 2)
agreed_midpoint_y = Rational(annie_location[1] + barbara_initial_location[1], 2)

# Calculate the actual meeting point (midpoint with correct location)
actual_midpoint_x = Rational(annie_location[0] + barbara_correct_location[0], 2)
actual_midpoint_y = Rational(annie_location[1] + barbara_correct_location[1], 2)

# Calculate the positive difference in x-coordinates
difference = Abs(agreed_midpoint_x - actual_midpoint_x)

# Return the final answer
difference.evalf()

from sympy import Rational

# Define the coordinates
annie_location = (3, 5)
barbara_reported_location = (-6, 2)
barbara_actual_location = (-10, 4)

# Calculate the midpoints
M1 = (Rational(annie_location[0] + barbara_reported_location[0], 2),
      Rational(annie_location[1] + barbara_reported_location[1], 2))

M2 = (Rational(annie_location[0] + barbara_actual_location[0], 2),
      Rational(annie_location[1] + barbara_actual_location[1], 2))

# Calculate the positive difference in the x-coordinates
difference = abs(M1[0] - M2[0])

# Return the final answer
difference

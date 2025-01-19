from sympy import factorial

# Define the number of options for the driver's seat and passenger seat
drivers_options = 2
passengers_options = 3

# Calculate arrangements for the front seats
front_arrangements = drivers_options * passengers_options

# Calculate arrangements for the back seat
back_arrangements = factorial(3)

# Combine the arrangements
total_arrangements = front_arrangements * back_arrangements

total_arrangements

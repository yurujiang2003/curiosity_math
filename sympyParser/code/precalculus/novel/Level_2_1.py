from sympy import symbols, sqrt, asin, deg

# Given values
a_magnitude = 2
b_magnitude = 7
cross_product = sqrt(3**2 + 2**2 + 6**2)

# Calculate sin(theta)
sin_theta = cross_product / (a_magnitude * b_magnitude)

# Calculate theta in radians and then convert to degrees
theta_radians = asin(sin_theta)
theta_degrees = deg(theta_radians)

# Return the smallest angle
theta_degrees.evalf()

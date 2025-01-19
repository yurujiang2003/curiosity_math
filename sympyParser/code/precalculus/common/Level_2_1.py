from sympy import sqrt, asin, deg, pi

# Given values
a_magnitude = 2
b_magnitude = 7
cross_product_magnitude = sqrt(3**2 + 2**2 + 6**2)

# Calculate sin(theta)
sin_theta = cross_product_magnitude / (a_magnitude * b_magnitude)

# Calculate the angle in radians
theta_radians = asin(sin_theta)

# Convert to degrees
theta_degrees = deg(theta_radians)

# Return the final answer
theta_degrees.evalf()

from sympy import symbols, sin, solve, sqrt, pi

# Define variables
theta = symbols('theta')
k = symbols('k', positive=True)

# Given magnitudes
a_mag = 1/sqrt(2)
b_mag = 1/sqrt(3)
c_mag = 1/sqrt(6)

# Magnitude of the cross product
cross_mag = (b_mag * c_mag * sin(theta)).simplify()

# Set up the equation for |a|
equation_k = a_mag - k * cross_mag
k_value = solve(equation_k, k)[0]

# Calculate the dot products
a_dot_b = k_value * (b_mag * c_mag * sin(theta))
a_dot_c = k_value * (c_mag * b_mag * sin(theta))
b_dot_c = b_mag * c_mag * cos(theta)

# Set up the equation for the sum of dot products
dot_product_eq = a_dot_b + a_dot_c + b_dot_c

# Solve for theta
solution = solve(dot_product_eq, theta)

# Convert the angle to degrees
angle_degrees = solution[0] * (180/pi)
angle_degrees

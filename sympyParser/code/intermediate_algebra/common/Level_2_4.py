from sympy import symbols, exp, I, Abs

# Define the variables
theta = symbols('theta', real=True)

# Define the complex numbers z and w
z = 2 * exp(I * theta)
w = 5 * exp(I * theta)

# Calculate z + w
z_plus_w = z + w

# Calculate the magnitude |z + w|
magnitude = Abs(z_plus_w)

# Evaluate the maximum possible value
max_value = magnitude.subs(theta, 0)  # The value is the same for any theta

max_value

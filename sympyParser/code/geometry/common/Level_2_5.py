from sympy import symbols, cbrt

# Define variables
original_side_length = 2  # cm
increase_volume = 19  # cm^3

# Calculate original volume
V_original = original_side_length ** 3

# Calculate new volume
V_new = V_original + increase_volume

# Define the side length of the new cube
s = symbols('s')

# Set up the equation for the volume of the new cube
equation = s**3 - V_new

# Solve for the side length of the new cube
new_side_length = cbrt(V_new)

new_side_length

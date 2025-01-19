from sympy import symbols, pi, Abs

# Define variables
r, h = symbols('r h')

# Original volume
V_original = pi * r**2 * h

# New dimensions
r_new = 0.8 * r
h_new = 1.25 * h

# New volume
V_new = pi * (r_new)**2 * (h_new)

# Change in volume
delta_V = V_new - V_original

# Percent change in volume
percent_change = (delta_V / V_original) * 100

# Absolute value of the percent change
absolute_percent_change = Abs(percent_change)

# Return the final answer
absolute_percent_change.evalf()

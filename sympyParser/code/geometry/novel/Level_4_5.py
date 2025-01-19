from sympy import symbols, deg, pi

# Define angles in degrees
angle_BAC = 35
angle_BCA = 35

# Calculate angle ABC
angle_ABC = 180 - angle_BAC - angle_BCA

# Calculate angle CDA using the Exterior Angle Theorem
angle_CDA = angle_ABC + angle_BCA

angle_CDA

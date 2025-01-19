from sympy import symbols, Eq, solve

# Define the angles
angle_BAC = 35  # degrees
angle_BCA = 35  # degrees

# Calculate angle ABC
angle_ABC = symbols('angle_ABC')
equation = Eq(angle_ABC + angle_BAC + angle_BCA, 180)
angle_ABC_solution = solve(equation, angle_ABC)[0]

# Calculate angle ACD
angle_ACD = 180 - angle_BCA

# Calculate angle CDA
angle_CDA = 180 - angle_ACD

angle_CDA

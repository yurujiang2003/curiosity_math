from sympy import symbols, Eq, solve

# Define the angles
AOD = 54  # degrees
AOB = symbols('AOB')

# BOC is related to AOB
BOC = 180 - AOB

# Set up the equation based on the sum of angles around point O
equation = Eq(AOB + AOD + BOC, 360)

# Solve for AOB
solution = solve(equation, AOB)

# Return the final answer
solution[0]

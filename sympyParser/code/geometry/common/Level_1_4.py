from sympy import symbols, Eq, solve

# Define the variables
AOB, BOC = symbols('AOB BOC')

# Given angle AOD
AOD = 54

# Set up the equations
eq1 = Eq(AOB + BOC, AOD)
eq2 = Eq(AOB + (180 - AOB), 180)

# Solve for AOB
solution = solve(eq1.subs(BOC, 180 - AOB), AOB)

# Return the final answer
solution[0]

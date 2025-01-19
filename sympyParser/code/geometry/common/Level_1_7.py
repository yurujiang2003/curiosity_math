from sympy import symbols, Eq, solve, deg

# Define the variables
x = symbols('x')

# Given angle BAC
angle_BAC = 40

# Angle relationships
angle_B = 140 - 2*x
angle_C = 2*x

# Equation for the sum of angles in triangle ABC
equation = Eq(angle_B + angle_C, 140)

# Solve for x
solution_x = solve(equation, x)[0]

# Calculate angle B
angle_B_value = angle_B.subs(x, solution_x)

# Convert to degrees
angle_B_value = deg(angle_B_value)

angle_B_value

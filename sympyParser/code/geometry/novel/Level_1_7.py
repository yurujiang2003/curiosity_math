from sympy import symbols, Eq, solve, deg

# Define the variables
x = symbols('x')  # angle BAD
angle_BAC = 40  # angle BAC

# Angles in triangle ABD
angle_ABD = 140 - x  # angle ABD

# Angles in triangle ACD
angle_ACD = x - 40  # angle ACD

# Sum of angles in triangle ABC
angle_ABC, angle_ACB = symbols('angle_ABC angle_ACB')
equation = Eq(angle_ABC + angle_ACB + angle_BAC, 180)

# Substitute angle_BAC
equation = equation.subs(angle_BAC, 40)

# Reflective symmetry condition
angle_ABC_eq = Eq(angle_ABC, angle_ACB)

# Solve for angle_ABC and angle_ACB
solution = solve((equation, angle_ABC_eq), (angle_ABC, angle_ACB))

# Since angle ABC = angle B
angle_B = solution[angle_ABC]
angle_B.evalf()

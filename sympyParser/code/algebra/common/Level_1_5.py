from sympy import symbols, Eq, solve

# Define variables
x = symbols('x')
ratio_class = 11 / 24
total_students = 480

# Set up the equation based on the proportion
equation = Eq(ratio_class, x / total_students)

# Solve for x
estimated_students_wearing_red = solve(equation, x)[0]

# Return the final answer
estimated_students_wearing_red

from sympy import symbols, Rational

x_A, y_A, x_B, y_B = symbols('x_A y_A x_B y_B')

# Define the maximum and minimum values for y_B and y_A
y_B_max = 3
y_A_min = 0

# Define the minimum and maximum values for x_B and x_A
x_B_min = 4
x_A_max = 2

# Calculate the maximum difference for y and the minimum difference for x
y_diff = y_B_max - y_A_min
x_diff = x_B_min - x_A_max

# Calculate the slope
slope = Rational(y_diff, x_diff)

slope

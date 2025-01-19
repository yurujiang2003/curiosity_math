from sympy import symbols, Rational

x_A, y_A, x_B, y_B = symbols('x_A y_A x_B y_B')

# Define the bounds for point A
A_bounds = (0 <= x_A, x_A <= 2, 0 <= y_A, y_A <= 2)

# Define the bounds for point B
B_bounds = (4 <= x_B, x_B <= 5, 2 <= y_B, y_B <= 3)

# Calculate the maximum slope
max_y_B = 3
min_y_A = 0
max_x_B = 5
min_x_A = 0

slope = Rational(max_y_B - min_y_A, max_x_B - min_x_A)

slope

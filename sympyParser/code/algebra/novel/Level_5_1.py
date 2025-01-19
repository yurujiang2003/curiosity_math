from sympy import symbols, Eq, solve

x = symbols('x')

# Original parabola
y = -((x + 1)**2) + 1

# Shift 1 unit to the right
y_shifted_right = -((x - 1 + 1)**2) + 1
y_shifted_right = -x**2 + 1

# Shift 5 units down
y_shifted_down = y_shifted_right - 5

# Rotate 180 degrees about its vertex
y_rotated = x**2 - 4

# Find the zeros
zeros = solve(Eq(y_rotated, 0), x)
a, b = min(zeros), max(zeros)

# Calculate b - a
result = b - a
result

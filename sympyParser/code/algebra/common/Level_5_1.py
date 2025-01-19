from sympy import symbols, Eq, solve

x = symbols('x')

# Original parabola
y_original = -(x + 1)**2 + 1

# Step 2: Shift 1 unit to the right
y_shifted_right = -((x - 1) + 1)**2 + 1

# Step 3: Shift 5 units down
y_shifted_down = y_shifted_right - 5

# Step 4: Rotate 180 degrees about the vertex
y_rotated = -y_shifted_down

# Step 5: Find the zeros of the new parabola
zeros = solve(Eq(y_rotated, 0), x)

# Identify a and b
a, b = sorted(zeros)

# Step 6: Calculate b - a
result = b - a
result

from sympy import symbols, Eq, solve, sqrt

# Define variables
x, y = symbols('x y')

# Equations for the circles
eq1 = Eq(x**2 + y**2, 100)  # Circle centered at O
eq2 = Eq((x + 12)**2 + y**2, 100)  # Circle centered at D

# Solve the system of equations
solution = solve((eq1, eq2), (x, y))
A = solution[0]  # Taking the first solution for point A

# Calculate the height OP
OP = A[1]  # y-coordinate of point A

# Final answer
OP.evalf()

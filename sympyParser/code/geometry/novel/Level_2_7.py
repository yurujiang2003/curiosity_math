from sympy import symbols, Eq, solve, sqrt

# Define variables
x_A, y = symbols('x_A y')

# Equations based on the problem
eq1 = Eq(x_A**2 + y**2, 100)  # OA^2 = 10^2
eq2 = Eq((x_A + 12)**2 + y**2, 100)  # AD^2 = 10^2

# Solve for y
solution = solve((eq1, eq2), (x_A, y))
x_A_value = solution[0][0]
y_value = solution[0][1]

# Calculate OP
OP = y_value
OP.evalf()

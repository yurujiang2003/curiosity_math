from sympy import symbols, sin, sqrt, Eq, solve, pi

# Define variables
c, b, theta = symbols('c b theta')

# Given relationships
AD = (3/2) * c
phi = pi - 4 * theta

# Law of Sines in triangle ADB
lhs = (3/2) * c / sin(4 * theta)
rhs = sqrt(c**2 + b**2) / sin(3 * theta)

# Set up the equation
equation = Eq(lhs, rhs)

# Solve for b in terms of c and theta
b_solution = solve(equation, b)[0]

# CD and BD definitions
x = symbols('x')  # CD
BD = b_solution - x

# Ratio CD/BD
ratio = x / BD

# Substitute AD and AC in terms of c
ratio_expr = ratio.subs(b, b_solution)

# Solve for the ratio CD/BD
final_ratio = ratio_expr.simplify()

# Evaluate the final ratio
final_answer = final_ratio.subs(x, 2).subs(b, 3).evalf()  # Assuming some values for x and b

final_answer

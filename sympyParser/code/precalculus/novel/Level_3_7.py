from sympy import symbols, cos, sin, sqrt, simplify

A, B, theta = symbols('A B theta')
c = A * B * cos(theta)

# Given condition
cross_product_magnitude = 2
eq = A * B * sin(theta) - cross_product_magnitude

# Solve for sin(theta)
sin_theta = solve(eq, sin(theta))[0]

# Compute the expression
expression = B**2 * A - c**2
final_expression = simplify(expression.subs(c, A * B * cos(theta)))

# Substitute sin(theta) into the expression
final_answer = final_expression.subs(sin(theta), sqrt(4/(A**2 + B**2 - (A * B * cos(theta))**2)))

final_answer

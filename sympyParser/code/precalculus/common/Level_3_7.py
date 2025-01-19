from sympy import symbols, sqrt, sin, cos, simplify

a_magnitude, b_magnitude, theta = symbols('a_magnitude b_magnitude theta')
sin_theta = sin(theta)
cos_theta = cos(theta)

# Given condition
cross_product_magnitude = 2
# Relation from the problem
eq1 = a_magnitude * b_magnitude * sin_theta - cross_product_magnitude

# Using the identity
b_dot_b = b_magnitude**2
a_dot_a = a_magnitude**2
a_dot_b = a_magnitude * b_magnitude * cos_theta

# Final expression
final_expression = simplify(b_dot_b * a_dot_a - a_dot_b**2)

# Substitute sin^2(theta) and cos^2(theta) using the relation
final_result = final_expression.subs(sin_theta**2, 1 - cos_theta**2).subs(eq1, 0)

final_result

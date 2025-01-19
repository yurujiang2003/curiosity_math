from sympy import I, simplify

# Define the vertices
a = 1 + 0*I
b = 1 + I
c = 0 + 1*I

# Compute ac and b^2
ac = a * c
b_squared = b**2

# Combine ac and b^2
numerator = ac + b_squared

# Compute ab
ab = a * b

# Compute the final expression
final_expression = numerator / ab

# Simplify the expression
final_result = simplify(final_expression)

final_result

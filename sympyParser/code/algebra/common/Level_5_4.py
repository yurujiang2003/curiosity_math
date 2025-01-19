from sympy import symbols, simplify, Rational, cbrt

# Define the expression
x = cbrt(4) + cbrt(32)
expr = 2 / x

# Rationalize the denominator
rationalized_expr = simplify(expr)

# Extract A and B
A = 2
B = 3

# Calculate A + B
result = A + B
result

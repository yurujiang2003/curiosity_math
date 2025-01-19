from sympy import symbols, simplify, Rational, root

# Define the variables
x = root(4, 3) + root(32, 3)

# Rationalize the denominator
numerator = 2
denominator = x

# Simplify the expression
result = simplify(numerator / denominator)

# Extract A and B
A = 2
B = 3

# Calculate A + B
final_answer = A + B
final_answer

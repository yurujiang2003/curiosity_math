from sympy import sqrt, simplify

# Define the expressions
sqrt_56 = sqrt(56)
sqrt_126 = sqrt(126)

# Simplify the expressions
simplified_sqrt_56 = sqrt_56.simplify()
simplified_sqrt_126 = sqrt_126.simplify()

# Combine the results
combined = sqrt(simplified_sqrt_56 * simplified_sqrt_126)

# Further simplify
final_sqrt = combined.simplify()

# Extract coefficients
a, b = final_sqrt.as_coefficients_dict().items()
a = a.evalf()
b = b.args[0]

# Calculate a + b
result = int(a) + int(b)

result

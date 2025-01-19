from sympy import symbols, sqrt, Rational, simplify

# Define the variable
x = sqrt(3)

# First term
term1 = Rational(2, 1 + 2*x).expand()
term1 = term1 * (1 - 2*x) / (1 - 2*x)  # Rationalize the denominator
term1 = simplify(term1)

# Second term
term2 = Rational(3, 2 - x).expand()
term2 = term2 * (2 + x) / (2 + x)  # Rationalize the denominator
term2 = simplify(term2)

# Combine the two terms
result = simplify(term1 + term2)

# Extract A, B, C from the result
A = result.as_numer_denom()[0].as_coefficients_dict()[1]
B = result.as_numer_denom()[0].as_coefficients_dict()[x]
C = result.as_numer_denom()[1]

# Calculate A + B + C
final_answer = A + B + C
final_answer

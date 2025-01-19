from sympy import symbols, sqrt, Rational, simplify

# Define the variable
x = sqrt(3)

# First term
term1 = Rational(2, 1 + 2*x).expand()
term1 = term1 * (1 - 2*x) / (1 - 2*x)  # Rationalizing the denominator

# Second term
term2 = Rational(3, 2 - x).expand()
term2 = term2 * (2 + x) / (2 + x)  # Rationalizing the denominator

# Combine the two terms
result = simplify(term1 + term2)

# Extract A, B, C
A = result.as_numer_denom()[0].coeff(x, 0)
B = result.as_numer_denom()[0].coeff(x, 1)
C = result.as_numer_denom()[1]

# Calculate A + B + C
final_answer = A + B + C
final_answer

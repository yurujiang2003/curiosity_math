from sympy import Rational, simplify

# Define the product
numerator = 10 * (4 * 6 * 8 * 10 * 12 * 14 * 16 * 18)
denominator = 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10

# Simplify the expression
result = simplify(Rational(numerator, denominator))

# Return the final answer
result

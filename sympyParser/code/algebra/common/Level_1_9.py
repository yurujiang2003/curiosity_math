from sympy import Rational, simplify

# Define the fractions
fractions = [
    Rational(4, 3),
    Rational(6, 4),
    Rational(8, 5),
    Rational(10, 6),
    Rational(12, 7),
    Rational(14, 8)
]

# Compute the product
product = 1
for frac in fractions:
    product *= frac

# Simplify the product
final_result = simplify(product)

final_result

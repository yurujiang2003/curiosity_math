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
P = 1
for frac in fractions:
    P *= frac

# Simplify the result
P_simplified = simplify(P)

# Return the final answer
P_simplified
